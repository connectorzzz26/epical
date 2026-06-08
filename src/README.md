# `src/` — Epical GDPR agents

Client code for the Azure AI Foundry agents that drive the GDPR / DSAR work in
this repository. The orchestrator is **`epical-na`**; the stage agents map 1:1 to
the pipeline in the [top-level README](../README.md) (ingest → index → analyse →
redact → produce).

The agents' instructions, tools and connected sub-agents live in **Azure AI
Foundry**. This package is just the *client* that invokes them, wrapping the
standard quickstart call:

```python
response = openai_client.responses.create(
    input=[{"role": "user", "content": "..."}],
    extra_body={"agent_reference": {"name": "epical-na", "version": "1",
                                    "type": "agent_reference"}},
)
```

## Layout

```
src/
├── README.md
├── requirements.txt
├── .env.example
├── run.py                     Convenience launcher (python src/run.py "...")
└── epical_agents/
    ├── __init__.py            Public API: OrchestratorAgent, Agent, get_agent, REGISTRY
    ├── __main__.py            CLI (python -m epical_agents ...)
    ├── config.py              Project endpoint + the agent roster (AgentSpec)
    ├── client.py              Cached AIProjectClient / OpenAI client factory
    ├── base.py                Agent wrapper: .ask() / .respond() / .stream()
    └── orchestrator.py        OrchestratorAgent (epical-na) + get_agent()
```

## Setup

```powershell
pip install -r src/requirements.txt
# copy src/.env.example to .env and fill in auth (see below)
```

**Authentication** (pick one, configured in `.env`):

- **API key** — set `AZURE_AI_PROJECT_API_KEY`. The client then calls
  `{endpoint}/openai/v1` directly with that key. Simplest to get going.
- **Microsoft Entra ID** — leave the key unset and run `az login`
  (DefaultAzureCredential). Used automatically when no key is present.

## Use

From the command line:

```powershell
# Ask the orchestrator (epical-na)
python src/run.py "Tell me what you can help with."

# List the configured agents
python src/run.py --list

# Call a stage agent directly by role (once deployed in Foundry)
python src/run.py --agent analyse "Summarise the Article 15 gaps."

# Stream, or chat interactively
python src/run.py --stream "Draft the key allegations."
python src/run.py --interactive
```

Or as a module (from inside `src/`): `python -m epical_agents "..."`.

From Python:

```python
from epical_agents import OrchestratorAgent, get_agent

orchestrator = OrchestratorAgent()
print(orchestrator.ask("Tell me what you can help with."))

# Direct call to a stage agent (bypasses server-side orchestration)
print(get_agent("analyse").ask("What are the strongest findings?"))
```

## The agent roster

| Agent | Role | Status | Purpose |
|-------|------|--------|---------|
| `epical-na` | orchestrator | **deployed** | Plans the DSAR work and delegates to the stage agents. |
| `epical-ingest` | ingest | placeholder | Collect & normalise raw enterprise exports (M365, Unit4). |
| `epical-index` | index | placeholder | Extract text, count identifiers, build the inventory. |
| `epical-analyse` | analyse | placeholder | Map data to GDPR obligations; find Article 15 gaps & over-disclosure. |
| `epical-redact` | redact | placeholder | Minimise evidence and mask third-party identifiers. |
| `epical-produce` | produce | placeholder | Draft the legal deliverables (letter before action, IMY complaint). |

The stage agents are scaffolded in [`epical_agents/config.py`](epical_agents/config.py)
with `deployed=False`. As you create each one in Azure AI Foundry, set its
`deployed` flag (and version) — no other code changes are needed. The
orchestrator can then call them as **connected agents** server-side, or you can
invoke them directly via `get_agent("<role>")`.

> **Note** — `config.ENDPOINT` defaults to the `genesismesh` project from the
> quickstart you provided. Override it with `AZURE_AI_PROJECT_ENDPOINT`.
