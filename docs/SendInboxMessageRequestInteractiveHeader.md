

# SendInboxMessageRequestInteractiveHeader

Optional header shown above the body. Required with `type: \"text\"` for `product_list`; not allowed for `product` or `carousel`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**text** | **String** | Required when header type is text. |  [optional] |
|**image** | [**SendInboxMessageRequestInteractiveHeaderImage**](SendInboxMessageRequestInteractiveHeaderImage.md) |  |  [optional] |
|**video** | [**SendInboxMessageRequestInteractiveHeaderImage**](SendInboxMessageRequestInteractiveHeaderImage.md) |  |  [optional] |
|**document** | [**SendInboxMessageRequestInteractiveHeaderImage**](SendInboxMessageRequestInteractiveHeaderImage.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| DOCUMENT | &quot;document&quot; |



