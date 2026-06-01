from __future__ import annotations

import argparse
from pathlib import Path

from ...scaffold import scaffold_project


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    command = subparsers.add_parser("scaffold", help="Create an agent-ready practice layout.")
    command.add_argument("target", type=Path)
    command.add_argument("--title", default="Practica educativa")
    command.add_argument("--language", default="python")
    command.add_argument("--force", action="store_true", help="Overwrite existing scaffold files.")
    command.set_defaults(func=handle)


def handle(args: argparse.Namespace) -> int:
    created = scaffold_project(args.target, args.title, args.language, args.force)
    print(f"Created or updated {len(created)} files in {args.target}")
    for path in created:
        print(f"- {path}")
    return 0
