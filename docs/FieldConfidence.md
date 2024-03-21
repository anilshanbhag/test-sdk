# FieldConfidence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **float** | The model&#39;s confidence in the extracted value. | [optional] 

## Example

```python
from aihub.models.field_confidence import FieldConfidence

# TODO update the JSON string below
json = "{}"
# create an instance of FieldConfidence from a JSON string
field_confidence_instance = FieldConfidence.from_json(json)
# print the JSON string representation of the object
print FieldConfidence.to_json()

# convert the object into a dict
field_confidence_dict = field_confidence_instance.to_dict()
# create an instance of FieldConfidence from a dict
field_confidence_form_dict = field_confidence.from_dict(field_confidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


