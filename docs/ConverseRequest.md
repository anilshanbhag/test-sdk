# ConverseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | The question to ask the document. | 
**document_ids** | **List[int]** | The IDs of the documents to ask the question. | 
**mode** | **str** | The mode of the model, either &#39;default&#39; or &#39;advanced&#39;. | [optional] 

## Example

```python
from aihub.models.converse_request import ConverseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConverseRequest from a JSON string
converse_request_instance = ConverseRequest.from_json(json)
# print the JSON string representation of the object
print ConverseRequest.to_json()

# convert the object into a dict
converse_request_dict = converse_request_instance.to_dict()
# create an instance of ConverseRequest from a dict
converse_request_form_dict = converse_request.from_dict(converse_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


