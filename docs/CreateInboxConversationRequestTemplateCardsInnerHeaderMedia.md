

# CreateInboxConversationRequestTemplateCardsInnerHeaderMedia

Overrides this card's header asset for THIS send. Without it, the card's approved sample asset is sent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Must match the card header&#39;s media type. |  |
|**link** | **String** | Public URL of the asset to send. Must be reachable without auth. |  [optional] |
|**id** | **String** | A Meta media id (from the media upload endpoint), as an alternative to link. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| DOCUMENT | &quot;document&quot; |



