# -*- coding: utf-8 -*-
"""Epical GDPR agent system — client for Azure AI Foundry agents.

Quick start::

    from epical_agents import OrchestratorAgent
    print(OrchestratorAgent().ask("Tell me what you can help with."))

The orchestrator is `epical-na`; see `config.py` for the full agent roster.
"""
from .config import AgentSpec, ORCHESTRATOR, STAGE_AGENTS, REGISTRY, resolve
from .base import Agent
from .orchestrator import OrchestratorAgent, get_agent

__all__ = [
    "AgentSpec",
    "ORCHESTRATOR",
    "STAGE_AGENTS",
    "REGISTRY",
    "resolve",
    "Agent",
    "OrchestratorAgent",
    "get_agent",
]
