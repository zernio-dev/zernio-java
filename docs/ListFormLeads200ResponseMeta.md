

# ListFormLeads200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**formId** | **String** |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | persisted: leads stored from the webhook and the recovery pass. live: read from Meta because none are stored for this form yet, or because content is not retained. |  [optional] |
|**lastCheckedAt** | **OffsetDateTime** | For persisted leads, when the recovery pass last ran for the Page, failed or parked passes included (null before the first one). It does not prove every lead is stored. For live reads, when Meta was read. |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PERSISTED | &quot;persisted&quot; |
| LIVE | &quot;live&quot; |



