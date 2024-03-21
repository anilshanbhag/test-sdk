# FileResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[Document]**](Document.md) |  | [optional] 

## Example

```python
from aihub.models.file_result import FileResult

# TODO update the JSON string below
json = "{}"
# create an instance of FileResult from a JSON string
file_result_instance = FileResult.from_json(json)
# print the JSON string representation of the object
print FileResult.to_json()

# convert the object into a dict
file_result_dict = file_result_instance.to_dict()
# create an instance of FileResult from a dict
file_result_form_dict = file_result.from_dict(file_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


