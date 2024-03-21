# DocumentDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the document. | [optional] 
**name** | **str** | Name of the document. | [optional] 
**state** | **str** | The processing state of the document (e.g., PROCESSED, PROCESSING, FAILED). | [optional] 
**upload_timestamp** | **datetime** | The timestamp when the document was uploaded. | [optional] 

## Example

```python
from aihub.models.document_details import DocumentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetails from a JSON string
document_details_instance = DocumentDetails.from_json(json)
# print the JSON string representation of the object
print DocumentDetails.to_json()

# convert the object into a dict
document_details_dict = document_details_instance.to_dict()
# create an instance of DocumentDetails from a dict
document_details_form_dict = document_details.from_dict(document_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


