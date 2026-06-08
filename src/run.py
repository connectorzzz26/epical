# -*- coding: utf-8 -*-
"""Convenience launcher so you can run from the repo root without installing:

    python src/run.py "Tell me what you can help with."
    python src/run.py --list

Equivalent to `python -m epical_agents ...` run from inside `src/`.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from epical_agents.__main__ import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
