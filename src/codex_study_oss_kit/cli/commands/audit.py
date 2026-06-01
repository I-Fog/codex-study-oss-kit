from __future__ import annotations

import argparse
from pathlib import Path

from ...audit import audit_project
from ...audit.output import render_audit_report, write_audit_report


def register(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    command = subparsers.add_parser("audit", help="Check whether a repo is ready for agent maintenance.")
    command.add_argument("target", type=Path)
    command.add_argument("--format", choices=["markdown", "json"], default="markdown")
    command.add_argument("--output", type=Path, help="Write the audit report to a file.")
    command.set_defaults(func=handle)


def handle(args: argparse.Namespace) -> int:
    report = audit_project(args.target)
    rendered = render_audit_report(report, args.format)
    if args.output:
        path = write_audit_report(rendered, args.output)
        print(f"Wrote audit report: {path}")
    else:
        print(rendered, end="")
    return 0 if report.ok else 1
