# Field


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The extracted value of the field. | [optional] 
**type** | **str** | The type of the field. | [optional] 
**confidence** | [**FieldConfidence**](FieldConfidence.md) |  | [optional] 

## Example

```python
from aihub.models.field import Field

# TODO update the JSON string below
json = "{}"
# create an instance of Field from a JSON string
field_instance = Field.from_json(json)
# print the JSON string representation of the object
print Field.to_json()

# convert the object into a dict
field_dict = field_instance.to_dict()
# create an instance of Field from a dict
field_form_dict = field.from_dict(field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


