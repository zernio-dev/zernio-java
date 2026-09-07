

# CreateTrackingTagRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** | Meta ad account id, e.g. &#x60;act_123456789&#x60;. Required by this endpoint but ignored for OpenAI Ads. |  |
|**name** | **String** |  |  |
|**defaultEventType** | [**DefaultEventTypeEnum**](#DefaultEventTypeEnum) | OpenAI Ads only (ignored by Meta). When set, also provisions a standard conversion event setting wired to the new pixel, so &#x60;goal: conversions&#x60; ad creates on &#x60;POST /v1/ads/create&#x60; have an event to reference immediately. |  [optional] |



## Enum: DefaultEventTypeEnum

| Name | Value |
|---- | -----|
| ORDER_CREATED | &quot;order_created&quot; |
| LEAD_CREATED | &quot;lead_created&quot; |
| ITEMS_ADDED | &quot;items_added&quot; |
| CONTENTS_VIEWED | &quot;contents_viewed&quot; |
| CHECKOUT_STARTED | &quot;checkout_started&quot; |
| REGISTRATION_COMPLETED | &quot;registration_completed&quot; |
| SUBSCRIPTION_CREATED | &quot;subscription_created&quot; |
| TRIAL_STARTED | &quot;trial_started&quot; |
| APPOINTMENT_SCHEDULED | &quot;appointment_scheduled&quot; |
| PAGE_VIEWED | &quot;page_viewed&quot; |
| APP_INSTALLED | &quot;app_installed&quot; |
| APP_OPENED | &quot;app_opened&quot; |



