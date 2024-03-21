# PromptResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_id** | **str** | The ID of the prompt. | [optional] 
**answer** | **str** | The answer to the question asked. | [optional] 

## Example

```python
from aihub.models.prompt_response import PromptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptResponse from a JSON string
prompt_response_instance = PromptResponse.from_json(json)
# print the JSON string representation of the object
print PromptResponse.to_json()

# convert the object into a dict
prompt_response_dict = prompt_response_instance.to_dict()
# create an instance of PromptResponse from a dict
prompt_response_form_dict = prompt_response.from_dict(prompt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


