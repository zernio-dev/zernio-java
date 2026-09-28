

# TrackingTagEventInput

Conversion event fields. Each platform stores a subset; a field it does not store answers 400 naming the supported ones.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** | Scopes the lookup on platforms whose tag ids live inside an ad account. |  [optional] |
|**name** | **String** |  |  [optional] |
|**type** | **String** | The platform&#39;s own event type enum value (e.g. &#x60;PURCHASE&#x60;). |  [optional] |
|**siteEvent** | [**SiteEventEnum**](#SiteEventEnum) | Neutral alternative to &#x60;type&#x60;, mapped to the platform&#39;s closest type. |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**defaultValue** | **BigDecimal** |  |  [optional] |
|**currency** | **String** | ISO 4217 code. |  [optional] |
|**clickWindowDays** | **Integer** |  |  [optional] |
|**viewWindowDays** | **Integer** |  |  [optional] |



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



