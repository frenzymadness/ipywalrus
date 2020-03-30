from IPython.testing.globalipapp import start_ipython
from IPython.utils.io import capture_output
import pytest


@pytest.fixture(scope="session")
def pure_ipython():
    yield start_ipython()


@pytest.fixture(scope="function")
def ipywalrus_enabled(pure_ipython):
    pure_ipython.run_line_magic(magic_name='load_ext', line='ipywalrus')
    yield pure_ipython
    pure_ipython.run_line_magic(magic_name='unload_ext', line='ipywalrus')


tests = [
    ("a := 5", 5),
    ("b := 5 + 5", 10),
    ("c := [5]", [5]),
    ("d := [z := 5]", [5]),
    ("e := (x := 5)", 5),
]


@pytest.mark.parametrize("input, expected_output", tests)
def test_syntaxerror_without_extension(pure_ipython, input, expected_output):
    with capture_output() as captured:
        pure_ipython.run_cell(raw_cell=input)
    assert "SyntaxError: invalid syntax" in captured.stdout
    assert input in captured.stdout


@pytest.mark.parametrize("input, expected_output", tests)
def test_works_with_extension(ipywalrus_enabled, input, expected_output):
    with capture_output() as captured:
        ipywalrus_enabled.run_cell(raw_cell=input)
    assert captured.stdout == "Out[1]: " + str(expected_output) + "\n"


@pytest.mark.parametrize("input, expected_output", tests)
def test_syntaxerror_unloaded_extension(pure_ipython, input, expected_output):
    with capture_output() as captured:
        pure_ipython.run_cell(raw_cell=input)
    assert "SyntaxError: invalid syntax" in captured.stdout
    assert input in captured.stdout
