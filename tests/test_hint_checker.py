import pytest

from src.enums.hints import Hints
from src.enums.colours import Colours
from src.hint_checker import HintChecker


@pytest.mark.parametrize(
    "secret_code, user_input, expected_hints",
    [
        ([Colours.Red, Colours.Red, Colours.Red, Colours.Red],
         [Colours.Red, Colours.Red, Colours.Red, Colours.Red],
         [Hints.Black, Hints.Black, Hints.Black, Hints.Black]),

        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Red, Colours.Purple, Colours.Purple, Colours.Purple],
         [Hints.White]),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Red, Colours.Blue, Colours.Purple, Colours.Purple],
         [Hints.White, Hints.White]),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Red, Colours.Blue, Colours.Yellow, Colours.Purple],
         [Hints.White, Hints.White, Hints.White]),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Red, Colours.Yellow, Colours.Green, Colours.Blue],
         [Hints.White, Hints.White, Hints.White, Hints.White]),

    ]
)
def test_hint_checker_returns_correct_hints(secret_code, user_input, expected_hints):
    hint_checker = HintChecker()
    hints = hint_checker.get_hints(user_input, secret_code)

    assert hints == expected_hints
