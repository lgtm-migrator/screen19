import pytest

try:
    import dials_data as _  # noqa: F401
except ImportError:

    @pytest.fixture(scope="session")
    def dials_data():
        pytest.skip("Test requires python package dials_data")
