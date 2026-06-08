# -*- coding: utf-8 -*-
"""The Agent wrapper.

An `Agent` is a thin client-side handle to an agent deployed in Azure AI
Foundry. Calling it sends a Responses API request with the agent's
`agent_reference`, exactly like the Foundry quickstart:

    response = openai_client.responses.create(
        input=[{"role": "user", "content": "..."}],
        extra_body={"agent_reference": {"name": "epical-na", "version": "1",
                                        "type": "agent_reference"}},
    )
"""
from __future__ import annotations

from typing import Iterable, Iterator

from .config import AgentSpec, resolve
from .client import get_openai_client

Message = dict  # {"role": "user"|"assistant"|"system", "content": str}


class Agent:
    """Client-side handle to a Foundry agent."""

    def __init__(self, spec: AgentSpec, *, client=None):
        self.spec = spec
        self._client = client

    # -- construction helpers -------------------------------------------------
    @classmethod
    def get(cls, name_or_role: str, version: str | None = None) -> "Agent":
        """Build an Agent from the registry by name ('epical-na') or role."""
        spec = resolve(name_or_role)
        if version is not None:
            spec = AgentSpec(spec.name, version, spec.role, spec.description, spec.deployed)
        return cls(spec)

    @property
    def client(self):
        if self._client is None:
            self._client = get_openai_client()
        return self._client

    # -- core call ------------------------------------------------------------
    @staticmethod
    def _build_input(prompt: "str | Iterable[Message]",
                     history: Iterable[Message] | None) -> list[Message]:
        messages: list[Message] = list(history or [])
        if isinstance(prompt, str):
            messages.append({"role": "user", "content": prompt})
        else:
            messages.extend(prompt)
        return messages

    def respond(self, prompt: "str | Iterable[Message]", *,
                history: Iterable[Message] | None = None, **kwargs):
        """Send a request and return the raw Responses object."""
        return self.client.responses.create(
            input=self._build_input(prompt, history),
            extra_body={"agent_reference": self.spec.reference()},
            **kwargs,
        )

    def ask(self, prompt: "str | Iterable[Message]", **kwargs) -> str:
        """Send a request and return just the text output."""
        return self.respond(prompt, **kwargs).output_text

    def stream(self, prompt: "str | Iterable[Message]", *,
               history: Iterable[Message] | None = None, **kwargs) -> Iterator[str]:
        """Yield text deltas as the agent responds."""
        events = self.client.responses.create(
            input=self._build_input(prompt, history),
            extra_body={"agent_reference": self.spec.reference()},
            stream=True,
            **kwargs,
        )
        for event in events:
            if getattr(event, "type", "") == "response.output_text.delta":
                delta = getattr(event, "delta", "")
                if delta:
                    yield delta

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        s = self.spec
        return f"<Agent {s.name} v{s.version} role={s.role!r} deployed={s.deployed}>"
