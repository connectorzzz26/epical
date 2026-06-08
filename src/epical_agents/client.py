# -*- coding: utf-8 -*-
"""Azure AI Foundry client factory.

Wraps the boilerplate from the Foundry quickstart:

    project_client = AIProjectClient(endpoint=..., credential=DefaultAzureCredential())
    openai_client  = project_client.get_openai_client()

Both clients are cached so the whole process shares one authenticated session.
Authentication uses DefaultAzureCredential — run `az login` (or set the standard
AZURE_* service-principal env vars) before invoking an agent.
"""
from __future__ import annotations

from functools import lru_cache

from . import config


@lru_cache(maxsize=1)
def get_project_client():
    """Return a cached AIProjectClient (Entra ID / DefaultAzureCredential auth)."""
    # Imported lazily so that importing this package never requires the Azure
    # SDKs to be installed (useful for tests, tooling and `--list`).
    from azure.identity import DefaultAzureCredential
    from azure.ai.projects import AIProjectClient

    return AIProjectClient(
        endpoint=config.ENDPOINT,
        credential=DefaultAzureCredential(),
    )


@lru_cache(maxsize=1)
def get_openai_client():
    """Return the OpenAI-compatible client bound to the Foundry project.

    Two auth modes:
    * If AZURE_AI_PROJECT_API_KEY is set, build an OpenAI client directly against
      the project's OpenAI-compatible endpoint ({endpoint}/openai/v1) using the
      key. (AIProjectClient itself only accepts a token credential, not a key.)
    * Otherwise, use AIProjectClient with DefaultAzureCredential (run `az login`).
    """
    if config.API_KEY:
        from openai import OpenAI

        base_url = config.ENDPOINT.rstrip("/") + "/openai/v1"
        return OpenAI(
            base_url=base_url,
            api_key=config.API_KEY,                       # -> Authorization: Bearer
            default_headers={"api-key": config.API_KEY},  # Azure-style key header
        )
    return get_project_client().get_openai_client()
