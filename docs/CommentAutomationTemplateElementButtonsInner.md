

# CommentAutomationTemplateElementButtonsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**title** | **String** |  |  |
|**url** | **URI** | Target URL (required when type is url) |  [optional] |
|**payload** | **String** | Postback payload delivered via the messaging_postbacks webhook (required when type is postback) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| URL | &quot;url&quot; |
| POSTBACK | &quot;postback&quot; |



