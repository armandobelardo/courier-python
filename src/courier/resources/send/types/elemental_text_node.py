# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .elemental_base_node import ElementalBaseNode
from .locales import Locales
from .text_align import TextAlign
from .text_style import TextStyle

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ElementalTextNode(ElementalBaseNode):
    """
    Represents a body of text to be rendered inside of the notification.
    """

    content: str = pydantic.Field(
        description=(
            "The text content displayed in the notification. Either this\n"
            "field must be specified, or the elements field\n"
        )
    )
    align: TextAlign = pydantic.Field(description="Text alignment.")
    text_style: typing.Optional[TextStyle] = pydantic.Field(
        description="Allows the text to be rendered as a heading level."
    )
    color: typing.Optional[str] = pydantic.Field(
        description="Specifies the color of text. Can be any valid css color value"
    )
    bold: typing.Optional[str] = pydantic.Field(description="Apply bold to the text")
    italic: typing.Optional[str] = pydantic.Field(description="Apply italics to the text")
    strikethrough: typing.Optional[str] = pydantic.Field(description="Apply a strike through the text")
    underline: typing.Optional[str] = pydantic.Field(description="Apply an underline to the text")
    locales: typing.Optional[Locales] = pydantic.Field(
        description="Region specific content. See [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/) for more details."
    )
    format: typing.Optional[typing_extensions.Literal["markdown"]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
