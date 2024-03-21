# ConversationSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the conversation. | 
**name** | **str** | Name of the conversation. | 
**description** | **str** | A brief description of the conversation. | [optional] 

## Example

```python
from aihub.models.conversation_summary import ConversationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationSummary from a JSON string
conversation_summary_instance = ConversationSummary.from_json(json)
# print the JSON string representation of the object
print ConversationSummary.to_json()

# convert the object into a dict
conversation_summary_dict = conversation_summary_instance.to_dict()
# create an instance of ConversationSummary from a dict
conversation_summary_form_dict = conversation_summary.from_dict(conversation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


