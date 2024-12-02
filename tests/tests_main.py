import pytest

from main import add


# list all tests
@pytest.mark.parametrize(
    "int1, int2, expected",
    [
        (2, 3, 5),
        (100, 100, 200),
        (
            "a",
            "b",
            "error",
        ),
    ],
)
# test function
def test_add(int1, int2, expected) -> None:
    assert add(int1, int2) == expected
