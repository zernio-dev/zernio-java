

# SendWhatsAppConversion200ResponseFailuresInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventIndex** | **Integer** | Index into the submitted events array. |  [optional] |
|**eventId** | **String** | Echoes back the eventId of the failed event. |  [optional] |
|**message** | **String** |  |  [optional] |
|**code** | [**SendConversions200ResponseFailuresInnerCode**](SendConversions200ResponseFailuresInnerCode.md) |  |  [optional] |
|**platformError** | **Map&lt;String, Object&gt;** | Meta&#39;s own error for the rejected event, with credentials redacted: &#x60;message&#x60;, &#x60;type&#x60;, &#x60;code&#x60;, &#x60;error_subcode&#x60;, &#x60;error_user_title&#x60;, &#x60;error_user_msg&#x60; and &#x60;fbtrace_id&#x60; when Meta sends them. &#x60;message&#x60; above already ends with &#x60;error_user_msg&#x60;. Absent when Meta returned no error body.  |  [optional] |



