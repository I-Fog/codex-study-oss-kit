from __future__ import annotations

import argparse
from pathlib import Path

from ...audit import audit_project


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    command = subparsers.add_parser("audit", help="Check whether a repo is ready for agent maintenance.")
    command.add_argument("target", type=Path)
    command.set_defaults(func=handle)


def handle(args: argparse.Namespace) -> int:
    report = audit_project(args.target)
    print(report.to_markdown())
    return 0 if report.ok else 1
