# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TextAlign(str, enum.Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

    def visit(
        self,
        left: typing.Callable[[], T_Result],
        center: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextAlign.LEFT:
            return left()
        if self is TextAlign.CENTER:
            return center()
        if self is TextAlign.RIGHT:
            return right()