"""Run static analysis on the project."""

import argparse
import os
import sys
import shutil
import subprocess
import tempfile


def do_process(args, shell=False):
    """Run program provided by args.

    Return True on success.

    Output failed message on non-zero exit and return False.

    Exit if command is not found.
    """
    print(f"Executing: {' '.join(args)}")
    try:
        subprocess.check_call(args, shell=shell)
    except subprocess.CalledProcessError:
        print(f"\nFailed: {' '.join(args)}")
        return False
    except Exception as e:
        sys.stderr.write(f"{str(e)}\n")
        sys.exit(1)
    return True


def main():
    if not os.path.exists("env"):
        raise SystemExit(
            "env/ directory not found, you must first create a virtual environment to run this script. See README.md"
        )

    # run black
    do_process(["env/bin/black", "."])

    # run static code analysers
    do_process(
        [
            "env/bin/flake8",
            "twitter_scraper.py",
        ]
    )
    do_process(
        [
            "env/bin/pydocstyle",
            "twitter_scraper.py",
        ]
    )

    # print coverage report
    do_process(["env/bin/coverage", "report", "-m"])


if __name__ == "__main__":
    main()
