from __future__ import annotations

import argparse

from .commands import audit, handoff, scaffold


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

    scaffold.register(subparsers)
    audit.register(subparsers)
    handoff.register(subparsers)

    return parser
