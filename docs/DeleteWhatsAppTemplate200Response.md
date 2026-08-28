

# DeleteWhatsAppTemplate200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Whether the whole family or one variant was deleted. |  [optional] |
|**language** | **String** | The deleted variant; only when scope is language. |  [optional] |
|**message** | **String** |  |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| ALL_LANGUAGES | &quot;all_languages&quot; |
| LANGUAGE | &quot;language&quot; |



