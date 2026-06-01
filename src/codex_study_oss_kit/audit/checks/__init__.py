from .agents import check_agents
from .readme import check_readme
from .rubric import check_rubric
from .source import check_source_folder
from .tests import check_tests_folder
from .validation import check_validation_command

DEFAULT_CHECKS = [
    check_agents,
    check_readme,
    check_tests_folder,
    check_rubric,
    check_source_folder,
    check_validation_command,
]

__all__ = [
    "DEFAULT_CHECKS",
    "check_agents",
    "check_readme",
    "check_rubric",
    "check_source_folder",
    "check_tests_folder",
    "check_validation_command",
]
