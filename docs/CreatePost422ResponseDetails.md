

# CreatePost422ResponseDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |
|**since** | **OffsetDateTime** |  |  [optional] |
|**lastFailedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| RESTRICTED | &quot;restricted&quot; |
| SUSPENDED | &quot;suspended&quot; |
| VERIFICATION_REQUIRED | &quot;verification_required&quot; |
| AUTH_EXPIRED | &quot;auth_expired&quot; |



