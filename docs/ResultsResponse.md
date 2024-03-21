# ResultsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**Dict[str, FileResult]**](FileResult.md) |  | [optional] 

## Example

```python
from aihub.models.results_response import ResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsResponse from a JSON string
results_response_instance = ResultsResponse.from_json(json)
# print the JSON string representation of the object
print ResultsResponse.to_json()

# convert the object into a dict
results_response_dict = results_response_instance.to_dict()
# create an instance of ResultsResponse from a dict
results_response_form_dict = results_response.from_dict(results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


