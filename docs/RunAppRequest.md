# RunAppRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the app to run. | [optional] 
**app_id** | **str** | The ID of the app to run. | [optional] 
**batch_id** | **int** | Batch ID. | [optional] 
**input_dir** | **int** | Input directory. | [optional] 

## Example

```python
from aihub.models.run_app_request import RunAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunAppRequest from a JSON string
run_app_request_instance = RunAppRequest.from_json(json)
# print the JSON string representation of the object
print RunAppRequest.to_json()

# convert the object into a dict
run_app_request_dict = run_app_request_instance.to_dict()
# create an instance of RunAppRequest from a dict
run_app_request_form_dict = run_app_request.from_dict(run_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


