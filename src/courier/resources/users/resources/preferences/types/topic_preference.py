# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.channel_classification import ChannelClassification
from .....commons.types.preference_status import PreferenceStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TopicPreference(pydantic.BaseModel):
    custom_routing: typing.Optional[typing.List[ChannelClassification]] = pydantic.Field(
        description="The Channels a user has chosen to receive notifications through for this topic"
    )
    default_status: PreferenceStatus
    has_custom_routing: typing.Optional[bool]
    status: PreferenceStatus
    topic_id: str
    topic_name: str

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
