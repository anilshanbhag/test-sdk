# ListConversations200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversations** | [**List[ConversationSummary]**](ConversationSummary.md) |  | [optional] 

## Example

```python
from aihub.models.list_conversations200_response import ListConversations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListConversations200Response from a JSON string
list_conversations200_response_instance = ListConversations200Response.from_json(json)
# print the JSON string representation of the object
print ListConversations200Response.to_json()

# convert the object into a dict
list_conversations200_response_dict = list_conversations200_response_instance.to_dict()
# create an instance of ListConversations200Response from a dict
list_conversations200_response_form_dict = list_conversations200_response.from_dict(list_conversations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


