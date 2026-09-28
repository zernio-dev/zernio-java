

# TrackingTagEventsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**name** | **String** |  |  |
|**type** | **String** | Platform category of the event. |  [optional] |
|**siteEvent** | [**SiteEventEnum**](#SiteEventEnum) | The neutral site event this conversion is fired for, when it maps to one. |  [optional] |
|**siteEventId** | **String** | What the site sends to fire this event (Google conversion label, LinkedIn conversion rule id, X &#x60;tw-&#x60; event id). |  [optional] |
|**status** | **String** |  |  [optional] |



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



