

# ListWhatsAppAccountEvents200ResponseEventsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**type** | **String** | Event kind, e.g. template_approved, template_rejected, account_restricted, account_disconnected |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**detail** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFO | &quot;info&quot; |
| SUCCESS | &quot;success&quot; |
| WARNING | &quot;warning&quot; |
| CRITICAL | &quot;critical&quot; |



