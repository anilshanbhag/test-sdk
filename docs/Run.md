# Run


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Job ID. | [optional] 
**status** | **str** | The current state of the run. | [optional] 
**start_timestamp** | **int** | 10-digit Unix timestamp of Job start. | [optional] 
**finish_timestamp** | **int** | 10-digit Unix timestamp of Job end. Null if still running. | [optional] 
**msg** | **str** | Job error message. Present if status equals ERROR. | [optional] 

## Example

```python
from aihub.models.run import Run

# TODO update the JSON string below
json = "{}"
# create an instance of Run from a JSON string
run_instance = Run.from_json(json)
# print the JSON string representation of the object
print Run.to_json()

# convert the object into a dict
run_dict = run_instance.to_dict()
# create an instance of Run from a dict
run_form_dict = run.from_dict(run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


