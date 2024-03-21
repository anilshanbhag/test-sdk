# coding: utf-8

# flake8: noqa

"""
    AIHub API

    The AIHub REST API. Please see https://aihub.instabase.com/docs/ for more details.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from aihub.api.default_api import DefaultApi

# import ApiClient
from aihub.api_response import ApiResponse
from aihub.api_client import ApiClient
from aihub.configuration import Configuration
from aihub.exceptions import OpenApiException
from aihub.exceptions import ApiTypeError
from aihub.exceptions import ApiValueError
from aihub.exceptions import ApiKeyError
from aihub.exceptions import ApiAttributeError
from aihub.exceptions import ApiException

# import models into sdk package
from aihub.models.batch import Batch
from aihub.models.conversation import Conversation
from aihub.models.conversation_response import ConversationResponse
from aihub.models.conversation_response_upload_status import ConversationResponseUploadStatus
from aihub.models.conversation_response_upload_status_failure_inner import ConversationResponseUploadStatusFailureInner
from aihub.models.conversation_response_upload_status_success_inner import ConversationResponseUploadStatusSuccessInner
from aihub.models.conversation_summary import ConversationSummary
from aihub.models.converse_request import ConverseRequest
from aihub.models.create_batch_request import CreateBatchRequest
from aihub.models.document import Document
from aihub.models.document_details import DocumentDetails
from aihub.models.error import Error
from aihub.models.field import Field
from aihub.models.field_confidence import FieldConfidence
from aihub.models.file_result import FileResult
from aihub.models.list_conversations200_response import ListConversations200Response
from aihub.models.prompt_response import PromptResponse
from aihub.models.results_response import ResultsResponse
from aihub.models.run import Run
from aihub.models.run_app_request import RunAppRequest

from aihub.aihub import AIHub