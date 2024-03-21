# ConversationResponseUploadStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | [**List[ConversationResponseUploadStatusSuccessInner]**](ConversationResponseUploadStatusSuccessInner.md) |  | [optional] 
**failure** | [**List[ConversationResponseUploadStatusFailureInner]**](ConversationResponseUploadStatusFailureInner.md) |  | [optional] 

## Example

```python
from aihub.models.conversation_response_upload_status import ConversationResponseUploadStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResponseUploadStatus from a JSON string
conversation_response_upload_status_instance = ConversationResponseUploadStatus.from_json(json)
# print the JSON string representation of the object
print ConversationResponseUploadStatus.to_json()

# convert the object into a dict
conversation_response_upload_status_dict = conversation_response_upload_status_instance.to_dict()
# create an instance of ConversationResponseUploadStatus from a dict
conversation_response_upload_status_form_dict = conversation_response_upload_status.from_dict(conversation_response_upload_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


