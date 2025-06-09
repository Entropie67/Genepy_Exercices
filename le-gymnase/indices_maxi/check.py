import gettext
import sys
from functools import cache
from hashlib import sha1
from pathlib import Path

import correction_helper as checker

checker.exclude_file_from_traceback(__file__)
Path("solution").rename("solution.py")
_ = gettext.translation("hkis", fallback=True).gettext


@cache
def get_student_function():
    with checker.student_code(prefix="While importing your solution:"):
        from solution import indices_maxi

    if not callable(indices_maxi):
        checker.fail(
            _("I need you to implement a function called `indices_maxi`."),
            _(
                "Currently, in your code, `indices_maxi` "
                "is a {indices_maxi}."
            ).format(type_of_indices_maxi=type(indices_maxi)),
        )
    return indices_maxi


def test_first_example():
    indices_maxi = get_student_function()
    with checker.student_code():
        result = indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
    if result != (9, [3, 8]):
        checker.fail(
            _(
                "I tried the 1st example, "
                "`indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])`, "
                "expected `(9, [3, 8])` but I got:"
            ),
            checker.code(result),
        )


def test_second_example():
    indices_maxi = get_student_function()
    with checker.student_code():
        result = indices_maxi([7])
    if result != (7, [0]) :
        checker.fail(
            _(
                "I tried the 2nd example, "
                "`indices_maxi([7]) `"
                "expected `(7, [0]) ` but I got:"
            ),
            checker.code(result),
        )


def check():
    for name, function in globals().items():
        if callable(function) and name.startswith("test_"):
            function()

    # If no test failed, consider the answer is right.
    print(checker.congrats())


if __name__ == "__main__":
    check()