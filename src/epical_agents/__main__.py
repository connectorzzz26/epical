# -*- coding: utf-8 -*-
"""Command-line entry point.

    python -m epical_agents "Tell me what you can help with."
    python -m epical_agents --agent analyse "Summarise the Article 15 gaps."
    python -m epical_agents --interactive
    python -m epical_agents --list
"""
from __future__ import annotations

import argparse
import sys

from . import config
from .orchestrator import get_agent

DEFAULT_PROMPT = "Tell me what you can help with."


def _list_agents() -> None:
    print(f"Project endpoint: {config.ENDPOINT}\n")
    print(f"{'AGENT':<16}{'VER':<5}{'ROLE':<13}{'DEPLOYED':<10}DESCRIPTION")
    for spec in config.REGISTRY.values():
        print(f"{spec.name:<16}{spec.version:<5}{spec.role:<13}"
              f"{'yes' if spec.deployed else 'no':<10}{spec.description}")


def _interactive(agent) -> None:
    print(f"Chatting with {agent.spec.name} (v{agent.spec.version}). "
          "Empty line or Ctrl-D to exit.\n")
    history: list[dict] = []
    while True:
        try:
            user = input("you> ").strip()
        except EOFError:
            print()
            break
        if not user:
            break
        history.append({"role": "user", "content": user})
        reply = agent.ask(history)
        print(f"\n{agent.spec.name}> {reply}\n")
        history.append({"role": "assistant", "content": reply})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="epical_agents",
        description="Talk to the Epical GDPR agents (orchestrator: epical-na).",
    )
    parser.add_argument("prompt", nargs="*", help="Prompt to send (default: a greeting).")
    parser.add_argument("--agent", "-a", default="epical-na",
                        help="Agent name or role to call (default: epical-na).")
    parser.add_argument("--version", "-v", default=None, help="Agent version to call.")
    parser.add_argument("--stream", action="store_true", help="Stream the response.")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Start an interactive chat session.")
    parser.add_argument("--list", action="store_true",
                        help="List the configured agents and exit.")
    args = parser.parse_args(argv)

    if args.list:
        _list_agents()
        return 0

    try:
        agent = get_agent(args.agent, args.version)
    except KeyError as exc:
        parser.error(str(exc))

    if not agent.spec.deployed:
        print(f"warning: agent '{agent.spec.name}' is marked not-yet-deployed in "
              "config.py; the call may fail until it exists in Foundry.",
              file=sys.stderr)

    try:
        if args.interactive:
            _interactive(agent)
            return 0

        prompt = " ".join(args.prompt) if args.prompt else DEFAULT_PROMPT
        if args.stream:
            for delta in agent.stream(prompt):
                print(delta, end="", flush=True)
            print()
        else:
            print(agent.ask(prompt))
    except Exception as exc:  # noqa: BLE001 - surface a friendly hint
        print(f"\nerror calling '{agent.spec.name}': {exc}", file=sys.stderr)
        print("hint: run `az login` (DefaultAzureCredential) and confirm the agent "
              "name/version and AZURE_AI_PROJECT_ENDPOINT.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
