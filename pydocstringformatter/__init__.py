# pylint: disable = import-outside-toplevel

import sys
from typing import List, Union

__version__ = "0.1.0+dev"


def run_docstring_formatter(argv: Union[List[str], None] = None) -> None:
    """Run the formatter"""
    from pydocstringformatter.run import _Run

    _Run(argv or sys.argv[1:])
