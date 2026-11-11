

# GetEventsOverview200ResponseSourcesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | **String** | Source id, such as &#x60;web&#x60;, &#x60;shopify&#x60; or &#x60;api&#x60; (which also covers &#x60;relay&#x60;). |  [optional] |
|**label** | **String** | The source in plain words, such as &#x60;Shopify orders&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Always &#x60;on&#x60; for now: the source is sending events. |  [optional] |
|**eventsToday** | **Integer** |  |  [optional] |
|**lastSeenAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ON | &quot;on&quot; |
| AVAILABLE | &quot;available&quot; |
| CONNECT | &quot;connect&quot; |



