"""Module to run Pylint on input file."""
import subprocess


def run_pylint_on_file(input_file):
    """Run pylint on the specified file and return the output."""
    result = subprocess.run(
        ['python3', '-m', 'pylint', input_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False
    )
    return result.stdout + result.stderr
