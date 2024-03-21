# aihub.DefaultApi

All URIs are relative to *https://aihub.instabase.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_to_batch**](DefaultApi.md#add_file_to_batch) | **PUT** /api/v2/batches/{id}/files/{filename} | Upload a file to the batch.
[**converse**](DefaultApi.md#converse) | **POST** /api/v2/conversations/{id}/prompts | Converse with the documents in a conversation.
[**create_batch**](DefaultApi.md#create_batch) | **POST** /api/v2/batches | Create a new batch.
[**create_conversation**](DefaultApi.md#create_conversation) | **POST** /api/v2/conversations | Create a new conversation and upload files.
[**get_conversation**](DefaultApi.md#get_conversation) | **GET** /api/v2/conversations/{id} | Get the details of the conversation.
[**get_run_results**](DefaultApi.md#get_run_results) | **GET** /api/v2/jobs/{id}/results | Retrieve run results
[**get_run_status**](DefaultApi.md#get_run_status) | **GET** /api/v2/apps/runs/{id} | Get the status of a run.
[**list_conversations**](DefaultApi.md#list_conversations) | **GET** /api/v2/conversations | List all conversations created.
[**run_app**](DefaultApi.md#run_app) | **POST** /api/v2/apps/runs | Run a given app.


# **add_file_to_batch**
> add_file_to_batch(id, filename, body)

Upload a file to the batch.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    id = 56 # int | The ID of the batch to which the file is being uploaded.
    filename = 'filename_example' # str | The name of the file being uploaded.
    body = None # bytearray | 

    try:
        # Upload a file to the batch.
        api_instance.add_file_to_batch(id, filename, body)
    except Exception as e:
        print("Exception when calling DefaultApi->add_file_to_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the batch to which the file is being uploaded. | 
 **filename** | **str**| The name of the file being uploaded. | 
 **body** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | File uploaded successfully. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **converse**
> PromptResponse converse(id, converse_request)

Converse with the documents in a conversation.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.converse_request import ConverseRequest
from aihub.models.prompt_response import PromptResponse
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    id = 'id_example' # str | The ID of the conversation.
    converse_request = aihub.ConverseRequest() # ConverseRequest | 

    try:
        # Converse with the documents in a conversation.
        api_response = api_instance.converse(id, converse_request)
        print("The response of DefaultApi->converse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->converse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the conversation. | 
 **converse_request** | [**ConverseRequest**](ConverseRequest.md)|  | 

### Return type

[**PromptResponse**](PromptResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response, providing the answer to the question. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch**
> Batch create_batch(create_batch_request)

Create a new batch.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.batch import Batch
from aihub.models.create_batch_request import CreateBatchRequest
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    create_batch_request = aihub.CreateBatchRequest() # CreateBatchRequest | 

    try:
        # Create a new batch.
        api_response = api_instance.create_batch(create_batch_request)
        print("The response of DefaultApi->create_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_batch_request** | [**CreateBatchRequest**](CreateBatchRequest.md)|  | 

### Return type

[**Batch**](Batch.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch created successfully. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_conversation**
> ConversationResponse create_conversation(files, name=name, description=description, org=org, workspace=workspace, enable_object_detection=enable_object_detection)

Create a new conversation and upload files.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.conversation_response import ConversationResponse
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    files = None # List[bytearray] | 
    name = 'name_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    org = 'org_example' # str |  (optional)
    workspace = 'workspace_example' # str |  (optional)
    enable_object_detection = True # bool |  (optional)

    try:
        # Create a new conversation and upload files.
        api_response = api_instance.create_conversation(files, name=name, description=description, org=org, workspace=workspace, enable_object_detection=enable_object_detection)
        print("The response of DefaultApi->create_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **List[bytearray]**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **org** | **str**|  | [optional] 
 **workspace** | **str**|  | [optional] 
 **enable_object_detection** | **bool**|  | [optional] 

### Return type

[**ConversationResponse**](ConversationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Conversation created successfully. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation**
> Conversation get_conversation(id)

Get the details of the conversation.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.conversation import Conversation
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    id = 'id_example' # str | The ID of the conversation.

    try:
        # Get the details of the conversation.
        api_response = api_instance.get_conversation(id)
        print("The response of DefaultApi->get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the conversation. | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_results**
> ResultsResponse get_run_results(id)

Retrieve run results

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.results_response import ResultsResponse
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    id = 'id_example' # str | The unique identifier for the run.

    try:
        # Retrieve run results
        api_response = api_instance.get_run_results(id)
        print("The response of DefaultApi->get_run_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_run_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the run. | 

### Return type

[**ResultsResponse**](ResultsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run results retrieved successfully. |  -  |
**400** | Bad request, id is required. |  -  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_status**
> Run get_run_status(id)

Get the status of a run.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.run import Run
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    id = 'id_example' # str | The run ID for which the status is being queried.

    try:
        # Get the status of a run.
        api_response = api_instance.get_run_status(id)
        print("The response of DefaultApi->get_run_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_run_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The run ID for which the status is being queried. | 

### Return type

[**Run**](Run.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**202** | Successful response. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversations**
> ListConversations200Response list_conversations()

List all conversations created.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.list_conversations200_response import ListConversations200Response
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)

    try:
        # List all conversations created.
        api_response = api_instance.list_conversations()
        print("The response of DefaultApi->list_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_conversations: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListConversations200Response**](ListConversations200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all conversations. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_app**
> Run run_app(run_app_request)

Run a given app.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import aihub
from aihub.models.run import Run
from aihub.models.run_app_request import RunAppRequest
from aihub.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aihub.instabase.com
# See configuration.py for a list of all supported configuration parameters.
configuration = aihub.Configuration(
    host = "https://aihub.instabase.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = aihub.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with aihub.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aihub.DefaultApi(api_client)
    run_app_request = aihub.RunAppRequest() # RunAppRequest | 

    try:
        # Run a given app.
        api_response = api_instance.run_app(run_app_request)
        print("The response of DefaultApi->run_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_app_request** | [**RunAppRequest**](RunAppRequest.md)|  | 

### Return type

[**Run**](Run.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job started successfully. |  -  |
**202** | Job started successfully. |  -  |
**0** | Error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

