# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ComparisonOperator(str, enum.Enum):
    ENDS_WITH = "ENDS_WITH"
    EQ = "EQ"
    EXISTS = "EXISTS"
    GT = "GT"
    GTE = "GTE"
    INCLUDES = "INCLUDES"
    IS_AFTER = "IS_AFTER"
    IS_BEFORE = "IS_BEFORE"
    LT = "LT"
    LTE = "LTE"
    NEQ = "NEQ"
    OMIT = "OMIT"
    STARTS_WITH = "STARTS_WITH"

    def visit(
        self,
        ends_with: typing.Callable[[], T_Result],
        eq: typing.Callable[[], T_Result],
        exists: typing.Callable[[], T_Result],
        gt: typing.Callable[[], T_Result],
        gte: typing.Callable[[], T_Result],
        includes: typing.Callable[[], T_Result],
        is_after: typing.Callable[[], T_Result],
        is_before: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
        neq: typing.Callable[[], T_Result],
        omit: typing.Callable[[], T_Result],
        starts_with: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ComparisonOperator.ENDS_WITH:
            return ends_with()
        if self is ComparisonOperator.EQ:
            return eq()
        if self is ComparisonOperator.EXISTS:
            return exists()
        if self is ComparisonOperator.GT:
            return gt()
        if self is ComparisonOperator.GTE:
            return gte()
        if self is ComparisonOperator.INCLUDES:
            return includes()
        if self is ComparisonOperator.IS_AFTER:
            return is_after()
        if self is ComparisonOperator.IS_BEFORE:
            return is_before()
        if self is ComparisonOperator.LT:
            return lt()
        if self is ComparisonOperator.LTE:
            return lte()
        if self is ComparisonOperator.NEQ:
            return neq()
        if self is ComparisonOperator.OMIT:
            return omit()
        if self is ComparisonOperator.STARTS_WITH:
            return starts_with()