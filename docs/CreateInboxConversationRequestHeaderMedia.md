

# CreateInboxConversationRequestHeaderMedia

WhatsApp only. Overrides a media-header template's header asset for THIS send, so a template with an image/video/document header can carry a different asset per message (e.g. each recipient their own invoice PDF). Without it, the template's approved sample asset is sent. Provide exactly one of link or id.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Must match the template header&#39;s media type. |  |
|**link** | **String** | Public URL of the asset to send. Must be reachable without auth. |  [optional] |
|**id** | **String** | A Meta media id (from the media upload endpoint), as an alternative to link. |  [optional] |
|**filename** | **String** | Document display name shown to the recipient (e.g. \&quot;Factura 0001-123.pdf\&quot;). document type only; ignored for image/video. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| DOCUMENT | &quot;document&quot; |



