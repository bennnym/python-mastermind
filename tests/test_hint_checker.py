import pytest

from enums.hints import Hints
from enums.colours import Colours
from hint_checker import HintChecker


@pytest.mark.parametrize(
    "secret_code, user_input, expected_hints",
    [
        ([Colours.Red, Colours.Red, Colours.Red, Colours.Red],
         [Colours.Red, Colours.Red, Colours.Red, Colours.Red],
         [Hints.Black, Hints.Black, Hints.Black, Hints.Black]),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Yellow, Colours.Green, Colours.Blue, Colours.Purple],
         [Hints.Black, Hints.Black, Hints.Black]),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Yellow, Colours.Green, Colours.Purple, Colours.Purple],
         [Hints.Black, Hints.Black]),
        ([Colours.Yellow, Colours.Green, Colours.Purple, Colours.Red],
         [Colours.Red, Colours.Blue, Colours.Red, Colours.Red],
         [Hints.Black])
    ]
)
def test_hint_checker_returns_correct_black_hints(secret_code, user_input, expected_hints):
    hint_checker = HintChecker()
    hints = hint_checker.get_hints(user_input, secret_code)

    assert hints == expected_hints


@pytest.mark.parametrize(
    "secret_code, user_input, expected_hints",
    [
        ([Colours.Green, Colours.Red, Colours.Blue, Colours.Yellow],
         [Colours.Yellow, Colours.Green, Colours.Red, Colours.Blue],
         [Hints.White, Hints.White, Hints.White, Hints.White]),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Green, Colours.Blue, Colours.Yellow, Colours.Purple],
         [Hints.White, Hints.White, Hints.White]),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Green, Colours.Blue, Colours.Purple, Colours.Purple],
         [Hints.White, Hints.White]),
        ([Colours.Purple, Colours.Purple, Colours.Purple, Colours.Red],
         [Colours.Red, Colours.Blue, Colours.Red, Colours.Yellow],
         [Hints.White])
    ]
)
def test_hint_checker_returns_correct_white_hints(secret_code, user_input, expected_hints):
    hint_checker = HintChecker()
    hints = hint_checker.get_hints(user_input, secret_code)

    assert hints == expected_hints


@pytest.mark.parametrize(
    "secret_code, user_input, expected_black_hints, expected_white_hints",
    [
        ([Colours.Green, Colours.Red, Colours.Blue, Colours.Yellow],
         [Colours.Yellow, Colours.Purple, Colours.Blue, Colours.Blue],
         1, 1),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Yellow, Colours.Green, Colours.Red, Colours.Purple],
         2, 1),
        ([Colours.Yellow, Colours.Green, Colours.Blue, Colours.Red],
         [Colours.Blue, Colours.Yellow, Colours.Green, Colours.Red],
         1, 3),
        ([Colours.Red, Colours.Purple, Colours.Purple, Colours.Red],
         [Colours.Red, Colours.Purple, Colours.Red, Colours.Purple],
         2, 2)
    ]
)
def test_hint_checker_returns_correct_black_and_white_hints(secret_code, user_input, expected_black_hints, expected_white_hints):
    hint_checker = HintChecker()
    hints = hint_checker.get_hints(user_input, secret_code)

    assert hints.count(Hints.Black) == expected_black_hints
    assert hints.count(Hints.White) == expected_white_hints
