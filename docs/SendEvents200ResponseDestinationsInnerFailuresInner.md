

# SendEvents200ResponseDestinationsInnerFailuresInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventIndex** | **Integer** | Position of the event in the request&#39;s &#x60;events&#x60; array, counted from 0, also when repeats or events this destination does not take were left out. |  [optional] |
|**eventId** | **String** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**code** | [**SendConversions200ResponseFailuresInnerCode**](SendConversions200ResponseFailuresInnerCode.md) |  |  [optional] |
|**field** | **String** | Google Ads and Campaign Manager 360 only: the event field Google refused (&#x60;event_timestamp&#x60;, &#x60;currency&#x60;...), without the &#x60;events.events[N].&#x60; prefix. Absent when Google named the event but no field. |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Google Ads and Campaign Manager 360 only, when Google refused the request. Absent for other platforms.  - &#x60;event&#x60;: Google named this event, and &#x60;message&#x60; is its own violation. - &#x60;batch&#x60;: the refusal is about the whole request (destination, account, an outage) and is copied to every event of it. - &#x60;batch_rejected&#x60;: Google did not name this event, but its resend without the named events failed too. &#x60;message&#x60; is that resend&#39;s error. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;event&quot; |
| BATCH | &quot;batch&quot; |
| BATCH_REJECTED | &quot;batch_rejected&quot; |



