# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.recipient_preferences import RecipientPreferences

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GetListSubscriptionsList(pydantic.BaseModel):
    id: str
    name: str = pydantic.Field(description="List name")
    created: str = pydantic.Field(
        description="The date/time of when the list was created. Represented as a string in ISO format."
    )
    updated: str = pydantic.Field(
        description="The date/time of when the list was updated. Represented as a string in ISO format."
    )
    preferences: typing.Optional[RecipientPreferences]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}