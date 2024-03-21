# Document


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_processed_paths** | **List[str]** |  | [optional] 
**fields** | [**Dict[str, Field]**](Field.md) |  | [optional] 
**review_completed** | **bool** | Whether manual review has been completed. | [optional] 
**class_name** | **str** | The classification label of the document. | [optional] 

## Example

```python
from aihub.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print Document.to_json()

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


