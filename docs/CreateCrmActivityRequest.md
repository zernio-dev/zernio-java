

# CreateCrmActivityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | The text to log. |  |
|**subject** | **String** | Salesforce Task subject (default &#x60;&lt;Channel&gt; activity (&lt;direction&gt;)&#x60;); on HubSpot, the bold first line. |  [optional] |
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  [optional] |
|**occurredAt** | **OffsetDateTime** | When it happened. Defaults to now. |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| WHATSAPP | &quot;whatsapp&quot; |
| SMS | &quot;sms&quot; |
| EMAIL | &quot;email&quot; |
| CALL | &quot;call&quot; |
| MEETING | &quot;meeting&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| MESSENGER | &quot;messenger&quot; |
| TELEGRAM | &quot;telegram&quot; |
| OTHER | &quot;other&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



