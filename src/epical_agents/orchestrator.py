# -*- coding: utf-8 -*-
"""The orchestrator agent: `epical-na`.

`epical-na` is the entry point for the system. In Azure AI Foundry it is
configured to plan the GDPR / DSAR work and delegate to connected stage agents
(ingest → index → analyse → redact → produce). From the client side you simply
talk to it; the delegation happens server-side.

The `delegate()` helper is provided for the case where you want to call a stage
agent *directly* from code rather than through the orchestrator.
"""
from __future__ import annotations

from . import config
from .base import Agent


class OrchestratorAgent(Agent):
    """Handle to the `epical-na` orchestrator."""

    def __init__(self, version: str | None = None, **kwargs):
        spec = config.ORCHESTRATOR
        if version is not None:
            spec = config.AgentSpec(spec.name, version, spec.role,
                                    spec.description, spec.deployed)
        super().__init__(spec, **kwargs)

    def delegate(self, role_or_name: str, prompt: str, **kwargs) -> str:
        """Call a stage agent directly (bypassing server-side orchestration)."""
        return Agent.get(role_or_name).ask(prompt, **kwargs)


def get_agent(name_or_role: str = "epical-na", version: str | None = None) -> Agent:
    """Return an Agent for any registered name/role; defaults to the orchestrator."""
    if name_or_role in ("epical-na", "orchestrator"):
        return OrchestratorAgent(version=version)
    return Agent.get(name_or_role, version=version)
