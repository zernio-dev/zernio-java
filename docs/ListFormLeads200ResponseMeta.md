

# ListFormLeads200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**formId** | **String** |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | persisted: leads stored from the webhook and the reconcile pass. live: read from Meta because none are stored for this form yet. |  [optional] |
|**lastCheckedAt** | **OffsetDateTime** | When Zernio last read this form&#39;s leads from Meta. For persisted leads, the last reconcile pass for the Page (null before the first one). For live reads, when the cached Graph read was made. |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PERSISTED | &quot;persisted&quot; |
| LIVE | &quot;live&quot; |



