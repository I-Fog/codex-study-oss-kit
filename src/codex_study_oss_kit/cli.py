from __future__ import annotations

import argparse
from pathlib import Path

from .audit import audit_project
from .handoff import write_handoff
from .scaffold import scaffold_project


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codex-study",
        description="Prepare educational OSS repositories for Codex-style maintenance.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scaffold = subparsers.add_parser("scaffold", help="Create an agent-ready practice layout.")
    scaffold.add_argument("target", type=Path)
    scaffold.add_argument("--title", default="Practica educativa")
    scaffold.add_argument("--language", default="python")
    scaffold.add_argument("--force", action="store_true", help="Overwrite existing scaffold files.")
    scaffold.set_defaults(func=_scaffold_command)

    audit = subparsers.add_parser("audit", help="Check whether a repo is ready for agent maintenance.")
    audit.add_argument("target", type=Path)
    audit.set_defaults(func=_audit_command)

    handoff = subparsers.add_parser("handoff", help="Write a compact continuation note.")
    handoff.add_argument("target", type=Path)
    handoff.add_argument("--objective", required=True)
    handoff.add_argument("--current", required=True)
    handoff.add_argument("--done", default="")
    handoff.add_argument("--pending", default="")
    handoff.add_argument("--command", default="")
    handoff.add_argument("--restriction", default="")
    handoff.add_argument("--output", type=Path)
    handoff.set_defaults(func=_handoff_command)

    return parser


def _scaffold_command(args: argparse.Namespace) -> int:
    created = scaffold_project(args.target, args.title, args.language, args.force)
    print(f"Created or updated {len(created)} files in {args.target}")
    for path in created:
        print(f"- {path}")
    return 0


def _audit_command(args: argparse.Namespace) -> int:
    report = audit_project(args.target)
    print(report.to_markdown())
    return 0 if report.ok else 1


def _handoff_command(args: argparse.Namespace) -> int:
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
