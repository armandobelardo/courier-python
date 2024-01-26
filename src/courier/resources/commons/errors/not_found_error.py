# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.not_found import NotFound


class NotFoundError(ApiError):
    def __init__(self, body: NotFound):
        super().__init__(status_code=404, body=body)