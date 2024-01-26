# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TextStyle(str, enum.Enum):
    TEXT = "text"
    H_1 = "h1"
    H_2 = "h2"
    SUBTEXT = "subtext"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        h_1: typing.Callable[[], T_Result],
        h_2: typing.Callable[[], T_Result],
        subtext: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextStyle.TEXT:
            return text()
        if self is TextStyle.H_1:
            return h_1()
        if self is TextStyle.H_2:
            return h_2()
        if self is TextStyle.SUBTEXT:
            return subtext()