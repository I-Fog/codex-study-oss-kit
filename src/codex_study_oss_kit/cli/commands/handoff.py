from __future__ import annotations

import argparse
from pathlib import Path

from ...handoff import write_handoff


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    command = subparsers.add_parser("handoff", help="Write a compact continuation note.")
    command.add_argument("target", type=Path)
    command.add_argument("--objective", required=True)
    command.add_argument("--current", required=True)
    command.add_argument("--done", default="")
    command.add_argument("--pending", default="")
    command.add_argument("--command", default="")
    command.add_argument("--restriction", default="")
    command.add_argument("--output", type=Path)
    command.set_defaults(func=handle)


def handle(args: argparse.Namespace) -> int:
    path = write_handoff(
        root=args.target,
        objective=args.objective,
        current=args.current,
        done=args.done,
        pending=args.pending,
        command=args.command,
        restriction=args.restriction,
        output=args.output,
    )
    print(f"Wrote handoff: {path}")
    return 0
