# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from .types.base_check import BaseCheck
from .types.notification_block import NotificationBlock
from .types.notification_channel import NotificationChannel
from .types.notification_get_content_response import NotificationGetContentResponse
from .types.notification_list_response import NotificationListResponse
from .types.submission_checks_get_response import SubmissionChecksGetResponse
from .types.submission_checks_replace_response import SubmissionChecksReplaceResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, cursor: typing.Optional[str] = None) -> NotificationListResponse:
        """
        Parameters:
            - cursor: typing.Optional[str].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "notifications"),
            params=remove_none_from_dict({"cursor": cursor}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationListResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_content(self, id: str) -> NotificationGetContentResponse:
        """
        Parameters:
            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/content"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationGetContentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_draft_content(self, id: str) -> NotificationGetContentResponse:
        """
        Parameters:
            - id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/draft/content"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationGetContentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_variations(
        self,
        id: str,
        *,
        blocks: typing.Optional[typing.List[NotificationBlock]] = OMIT,
        channels: typing.Optional[typing.List[NotificationChannel]] = OMIT,
    ) -> None:
        """
        Parameters:
            - id: str.

            - blocks: typing.Optional[typing.List[NotificationBlock]].

            - channels: typing.Optional[typing.List[NotificationChannel]].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if blocks is not OMIT:
            _request["blocks"] = blocks
        if channels is not OMIT:
            _request["channels"] = channels
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/variations"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_draft_variations(
        self,
        id: str,
        *,
        blocks: typing.Optional[typing.List[NotificationBlock]] = OMIT,
        channels: typing.Optional[typing.List[NotificationChannel]] = OMIT,
    ) -> None:
        """
        Parameters:
            - id: str.

            - blocks: typing.Optional[typing.List[NotificationBlock]].

            - channels: typing.Optional[typing.List[NotificationChannel]].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if blocks is not OMIT:
            _request["blocks"] = blocks
        if channels is not OMIT:
            _request["channels"] = channels
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/draft/variations"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_submission_checks(self, id: str, submission_id: str) -> SubmissionChecksGetResponse:
        """
        Parameters:
            - id: str.

            - submission_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/{submission_id}/checks"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SubmissionChecksGetResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def replace_submission_checks(
        self, id: str, submission_id: str, *, checks: typing.List[BaseCheck]
    ) -> SubmissionChecksReplaceResponse:
        """
        Parameters:
            - id: str.

            - submission_id: str.

            - checks: typing.List[BaseCheck].
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/{submission_id}/checks"
            ),
            json=jsonable_encoder({"checks": checks}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SubmissionChecksReplaceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def cancel_submission(self, id: str, submission_id: str) -> None:
        """
        Parameters:
            - id: str.

            - submission_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/{submission_id}/checks"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, cursor: typing.Optional[str] = None) -> NotificationListResponse:
        """
        Parameters:
            - cursor: typing.Optional[str].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "notifications"),
            params=remove_none_from_dict({"cursor": cursor}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationListResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_content(self, id: str) -> NotificationGetContentResponse:
        """
        Parameters:
            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/content"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationGetContentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_draft_content(self, id: str) -> NotificationGetContentResponse:
        """
        Parameters:
            - id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/draft/content"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(NotificationGetContentResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_variations(
        self,
        id: str,
        *,
        blocks: typing.Optional[typing.List[NotificationBlock]] = OMIT,
        channels: typing.Optional[typing.List[NotificationChannel]] = OMIT,
    ) -> None:
        """
        Parameters:
            - id: str.

            - blocks: typing.Optional[typing.List[NotificationBlock]].

            - channels: typing.Optional[typing.List[NotificationChannel]].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if blocks is not OMIT:
            _request["blocks"] = blocks
        if channels is not OMIT:
            _request["channels"] = channels
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/variations"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_draft_variations(
        self,
        id: str,
        *,
        blocks: typing.Optional[typing.List[NotificationBlock]] = OMIT,
        channels: typing.Optional[typing.List[NotificationChannel]] = OMIT,
    ) -> None:
        """
        Parameters:
            - id: str.

            - blocks: typing.Optional[typing.List[NotificationBlock]].

            - channels: typing.Optional[typing.List[NotificationChannel]].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if blocks is not OMIT:
            _request["blocks"] = blocks
        if channels is not OMIT:
            _request["channels"] = channels
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/draft/variations"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_submission_checks(self, id: str, submission_id: str) -> SubmissionChecksGetResponse:
        """
        Parameters:
            - id: str.

            - submission_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/{submission_id}/checks"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SubmissionChecksGetResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def replace_submission_checks(
        self, id: str, submission_id: str, *, checks: typing.List[BaseCheck]
    ) -> SubmissionChecksReplaceResponse:
        """
        Parameters:
            - id: str.

            - submission_id: str.

            - checks: typing.List[BaseCheck].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/{submission_id}/checks"
            ),
            json=jsonable_encoder({"checks": checks}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SubmissionChecksReplaceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def cancel_submission(self, id: str, submission_id: str) -> None:
        """
        Parameters:
            - id: str.

            - submission_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"notifications/{id}/{submission_id}/checks"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
