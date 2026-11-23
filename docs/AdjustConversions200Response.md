

# AdjustConversions200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**adjustmentsReceived** | **Integer** | Adjustments accepted by the platform. |  [optional] |
|**adjustmentsFailed** | **Integer** | Adjustments rejected (see failures). |  [optional] |
|**failures** | [**List&lt;AdjustConversions200ResponseFailuresInner&gt;**](AdjustConversions200ResponseFailuresInner.md) |  |  [optional] |
|**traceId** | **String** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLEADS | &quot;googleads&quot; |
| IMPACT | &quot;impact&quot; |



