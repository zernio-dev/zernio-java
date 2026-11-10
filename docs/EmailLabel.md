

# EmailLabel

A Gmail label or an Outlook category. Outlook categories are addressed by name, so their `id` is the name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Gmail label id such as &#x60;Label_12&#x60;, or the Outlook category name. |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) |  |  [optional] |
|**name** | **String** | Gmail nests labels with a slash, as in &#x60;Hermia/Handled&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**color** | [**EmailLabelColor**](EmailLabelColor.md) |  |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;system&quot; |
| USER | &quot;user&quot; |



