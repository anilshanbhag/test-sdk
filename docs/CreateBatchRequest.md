# CreateBatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the batch. Maximum length is 255 characters. | 
**workspace_name** | **str** | Name of the workspace in which the batch is being created. | [optional] 

## Example

```python
from aihub.models.create_batch_request import CreateBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatchRequest from a JSON string
create_batch_request_instance = CreateBatchRequest.from_json(json)
# print the JSON string representation of the object
print CreateBatchRequest.to_json()

# convert the object into a dict
create_batch_request_dict = create_batch_request_instance.to_dict()
# create an instance of CreateBatchRequest from a dict
create_batch_request_form_dict = create_batch_request.from_dict(create_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


