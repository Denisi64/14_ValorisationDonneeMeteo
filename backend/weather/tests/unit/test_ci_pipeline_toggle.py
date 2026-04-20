import os


def test_ci_pipeline_toggle():
    """Used only for Exercise 2 to simulate a failing test in CI."""
    assert os.getenv("CI_BREAK_TEST", "false") != "true"
