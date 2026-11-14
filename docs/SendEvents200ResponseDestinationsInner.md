

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
|**retrying** | **Boolean** | The destination failed for now (platform error, timeout, rate limit) and the send is queued for retries; its outcome shows on GET /v1/events/{eventId}. |  [optional] |
|**traceId** | **String** | The platform trace ID of the send (Meta &#x60;fbtrace_id&#x60;, Google &#x60;requestId&#x60;, TikTok &#x60;request_id&#x60;), to quote to the platform support. Absent when the platform returns none. |  [optional] |
|**platformMessages** | **List&lt;String&gt;** | Meta&#39;s &#x60;messages&#x60; (warnings about the events it accepted), each distinct one once, at most 20. Absent when the platform sent none. |  [optional] |



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



