# Conversation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the conversation. | 
**name** | **str** | Name of the conversation. | 
**description** | **str** | Description of the conversation. | [optional] 
**state** | **str** | The current state of the conversation (e.g., COMPLETE, RUNNING, FAILED). | 
**documents** | [**List[DocumentDetails]**](DocumentDetails.md) |  | [optional] 

## Example

```python
from aihub.models.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print Conversation.to_json()

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_form_dict = conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


