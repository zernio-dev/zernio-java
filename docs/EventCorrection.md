

# EventCorrection

What happened to a correction at one destination the event was forwarded to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**destinationId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;corrected&#x60;: the platform changed its count. &#x60;not_supported&#x60;: the platform has no API to change a conversion it already counted. &#x60;failed&#x60;: see &#x60;error&#x60;. |  [optional] |
|**error** | **String** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CORRECTED | &quot;corrected&quot; |
| NOT_SUPPORTED | &quot;not_supported&quot; |
| FAILED | &quot;failed&quot; |



