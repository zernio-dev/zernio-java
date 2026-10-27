

# SendConversions200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**eventsReceived** | **Integer** | Events accepted by the platform. |  [optional] |
|**eventsFailed** | **Integer** | Events rejected (see failures). |  [optional] |
|**failures** | [**List&lt;SendConversions200ResponseFailuresInner&gt;**](SendConversions200ResponseFailuresInner.md) |  |  [optional] |
|**traceId** | **String** | Platform trace ID for debugging. fbtrace_id for Meta, requestId for Google. Absent for LinkedIn (LinkedIn&#39;s conversionEvents endpoint does not surface a trace ID), OpenAI Ads and Reddit (no trace ID surfaced).  |  [optional] |
|**testCode** | **String** | The test code sent to the platform, as received (from &#x60;testCode&#x60; or &#x60;test_event_code&#x60;). &#x60;null&#x60; when the request carried none, so the events were sent as production events. |  [optional] |



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



