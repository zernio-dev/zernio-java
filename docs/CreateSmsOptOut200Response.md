

# CreateSmsOptOut200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**optedOut** | **Boolean** | Always true. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | What set the current opt-out. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| INBOUND_STOP | &quot;inbound_stop&quot; |



