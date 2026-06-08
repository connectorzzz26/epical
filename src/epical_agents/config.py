# -*- coding: utf-8 -*-
"""Configuration and the agent roster for the Epical GDPR agent system.

The agents themselves (their instructions, tools and connected sub-agents) live
in Azure AI Foundry. This module only describes *which* agents exist and how to
reach the project, so the client code can invoke them by reference.

Environment variables (all optional — sensible defaults are provided):
    AZURE_AI_PROJECT_ENDPOINT   Foundry project endpoint.
    EPICAL_NA_VERSION           Version of the orchestrator agent to call.
"""
from __future__ import annotations

import os
from dataclasses import dataclass


def _load_dotenv() -> None:
    """Minimal .env loader (no dependency).

    Looks for a `.env` next to the CWD, in `src/`, and at the repo root, and
    sets any keys that aren't already in the environment. Existing environment
    variables always win, so real env/CI config is never overridden.
    """
    pkg_dir = os.path.dirname(os.path.abspath(__file__))   # .../src/epical_agents
    src_dir = os.path.dirname(pkg_dir)                      # .../src
    root_dir = os.path.dirname(src_dir)                     # repo root
    for path in (os.path.join(os.getcwd(), ".env"),
                 os.path.join(src_dir, ".env"),
                 os.path.join(root_dir, ".env")):
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key, value = key.strip(), value.strip().strip('"').strip("'")
                os.environ.setdefault(key, value)


_load_dotenv()

# Foundry project endpoint. Override with AZURE_AI_PROJECT_ENDPOINT in the env.
DEFAULT_ENDPOINT = (
    "https://genesismesh-resource.services.ai.azure.com/api/projects/genesismesh"
)
ENDPOINT = os.environ.get("AZURE_AI_PROJECT_ENDPOINT", DEFAULT_ENDPOINT)

# Optional API-key auth. If set, it is used instead of DefaultAzureCredential.
API_KEY = os.environ.get("AZURE_AI_PROJECT_API_KEY") or os.environ.get("AZURE_AI_API_KEY")


@dataclass(frozen=True)
class AgentSpec:
    """A reference to an agent deployed in Azure AI Foundry."""

    name: str
    version: str = "1"
    role: str = ""
    description: str = ""
    deployed: bool = True

    def reference(self) -> dict:
        """The `agent_reference` payload expected by responses.create()."""
        return {"name": self.name, "version": str(self.version), "type": "agent_reference"}


# --- The orchestrator: the single entry point for the system. ----------------
# `epical-na` plans the work and (server-side, via Foundry connected agents)
# delegates to the stage agents below.
ORCHESTRATOR = AgentSpec(
    name=os.environ.get("EPICAL_AGENT_NAME", "epical-na"),
    version=os.environ.get("EPICAL_NA_VERSION", "1"),
    role="orchestrator",
    description=(
        "Top-level GDPR / DSAR orchestrator for the Epical matter. Plans the work "
        "and delegates to the stage agents."
    ),
    deployed=True,
)

# --- Stage agents: one per stage of the pipeline documented in the repo README.
# These are placeholders until you deploy them in Foundry. Once deployed, set
# `deployed=True` (and adjust the version). The orchestrator can call them
# server-side as connected agents, or you can invoke them directly from code.
STAGE_AGENTS = [
    AgentSpec("epical-ingest", "1", "ingest",
              "Collect and normalise raw enterprise exports (M365, Unit4).", deployed=False),
    AgentSpec("epical-index", "1", "index",
              "Extract text, count identifiers, and build the inventory.", deployed=False),
    AgentSpec("epical-analyse", "1", "analyse",
              "Map data to GDPR obligations; find Article 15 gaps and over-disclosure.",
              deployed=False),
    AgentSpec("epical-redact", "1", "redact",
              "Minimise evidence and mask third-party identifiers.", deployed=False),
    AgentSpec("epical-produce", "1", "produce",
              "Draft the legal deliverables (letter before action, IMY complaint).",
              deployed=False),
]

# Lookup by agent name and by logical role.
REGISTRY = {a.name: a for a in [ORCHESTRATOR, *STAGE_AGENTS]}
BY_ROLE = {a.role: a for a in [ORCHESTRATOR, *STAGE_AGENTS] if a.role}


def resolve(name_or_role: str) -> AgentSpec:
    """Resolve an AgentSpec by agent name (e.g. 'epical-na') or role ('analyse')."""
    if name_or_role in REGISTRY:
        return REGISTRY[name_or_role]
    if name_or_role in BY_ROLE:
        return BY_ROLE[name_or_role]
    known = ", ".join(sorted(REGISTRY)) + " | roles: " + ", ".join(sorted(BY_ROLE))
    raise KeyError(f"Unknown agent '{name_or_role}'. Known: {known}")
