

# CrmActivity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | HubSpot &#x60;note&#x60; or &#x60;communication&#x60; (WhatsApp, SMS); Salesforce &#x60;task&#x60;; HighLevel &#x60;note&#x60;. |  |
|**contactId** | **String** |  |  |
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) |  |  |
|**subject** | **String** |  |  |
|**body** | **String** |  |  |
|**occurredAt** | **OffsetDateTime** |  |  |
|**url** | **URI** | The Salesforce Task, or the HubSpot or HighLevel contact whose record shows it. |  |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| NOTE | &quot;note&quot; |
| COMMUNICATION | &quot;communication&quot; |
| TASK | &quot;task&quot; |



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



