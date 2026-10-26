

# SendEvents200ResponseDestinationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**destinationId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**eventsSent** | **Integer** | Events the platform accepted. |  [optional] |
|**eventsFailed** | **Integer** |  |  [optional] |
|**failures** | [**List&lt;SendEvents200ResponseDestinationsInnerFailuresInner&gt;**](SendEvents200ResponseDestinationsInnerFailuresInner.md) |  |  [optional] |
|**error** | **String** | Set when the destination could not be reached at all (account disconnected, unsupported platform, platform error). |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| METAADS | &quot;metaads&quot; |
| GOOGLEADS | &quot;googleads&quot; |
| LINKEDINADS | &quot;linkedinads&quot; |
| TIKTOKADS | &quot;tiktokads&quot; |
| OPENAIADS | &quot;openaiads&quot; |
| PINTERESTADS | &quot;pinterestads&quot; |
| REDDITADS | &quot;redditads&quot; |



