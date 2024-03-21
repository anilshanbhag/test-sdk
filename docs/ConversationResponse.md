# ConversationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the conversation. | 
**name** | **str** | Name of the conversation. | 
**upload_status** | [**ConversationResponseUploadStatus**](ConversationResponseUploadStatus.md) |  | 

## Example

```python
from aihub.models.conversation_response import ConversationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationResponse from a JSON string
conversation_response_instance = ConversationResponse.from_json(json)
# print the JSON string representation of the object
print ConversationResponse.to_json()

# convert the object into a dict
conversation_response_dict = conversation_response_instance.to_dict()
# create an instance of ConversationResponse from a dict
conversation_response_form_dict = conversation_response.from_dict(conversation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


