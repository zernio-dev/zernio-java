

# TrackingTagEvent

A conversion event tied to a tracking tag (Google conversion action, LinkedIn conversion rule, X web event tag, OpenAI event setting, TikTok pixel event, Meta custom conversion).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native event id, the &#x60;{eventId}&#x60; of the per-event routes. |  |
|**name** | **String** |  |  |
|**type** | **String** | Platform event type or category. |  [optional] |
|**siteEvent** | [**SiteEventEnum**](#SiteEventEnum) | The neutral site event this conversion is fired for, when it maps to one. |  [optional] |
|**siteEventId** | **String** | What the site sends to fire this event (Google conversion label, LinkedIn conversion rule id, X &#x60;tw-&#x60; event id). |  [optional] |
|**status** | **String** |  |  [optional] |
|**defaultValue** | **BigDecimal** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**clickWindowDays** | **Integer** |  |  [optional] |
|**viewWindowDays** | **Integer** |  |  [optional] |
|**urlContains** | **String** | Fires only on pages whose URL contains this text (case-insensitive). |  [optional] |
|**alwaysUseDefaultValue** | **Boolean** | &#x60;defaultValue&#x60; is recorded even when the conversion sends its own value. |  [optional] |
|**primary** | **Boolean** | Primary conversions count toward bidding and the Conversions column; secondary ones are observation only (Google &#x60;primary_for_goal&#x60;). |  [optional] |
|**countingType** | [**CountingTypeEnum**](#CountingTypeEnum) | &#x60;one&#x60; counts at most one conversion per ad interaction (leads), &#x60;every&#x60; counts each (purchases). |  [optional] |



## Enum: SiteEventEnum

| Name | Value |
|---- | -----|
| PAGE_VIEW | &quot;page_view&quot; |
| VIEW_CONTENT | &quot;view_content&quot; |
| ADD_TO_CART | &quot;add_to_cart&quot; |
| SEARCH | &quot;search&quot; |
| INITIATE_CHECKOUT | &quot;initiate_checkout&quot; |
| ADD_PAYMENT_INFO | &quot;add_payment_info&quot; |
| PURCHASE | &quot;purchase&quot; |



## Enum: CountingTypeEnum

| Name | Value |
|---- | -----|
| ONE | &quot;one&quot; |
| EVERY | &quot;every&quot; |



