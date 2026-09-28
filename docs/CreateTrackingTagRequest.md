

# CreateTrackingTagRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** | Meta ad account id, e.g. &#x60;act_123456789&#x60;. Required by this endpoint but ignored for OpenAI Ads. |  |
|**name** | **String** |  |  |
|**defaultEventType** | [**DefaultEventTypeEnum**](#DefaultEventTypeEnum) | OpenAI Ads only (ignored by Meta). When set, also provisions a standard conversion event setting wired to the new pixel, so &#x60;goal: conversions&#x60; ad creates on &#x60;POST /v1/ads/create&#x60; have an event to reference immediately. |  [optional] |
|**automaticMatchingFields** | [**List&lt;AutomaticMatchingFieldsEnum&gt;**](#List&lt;AutomaticMatchingFieldsEnum&gt;) | Pinterest only (400 elsewhere). Customer data the new tag matches automatically (automatic enhanced match): &#x60;em&#x60; email, &#x60;ph&#x60; phone, &#x60;fn&#x60;/&#x60;ln&#x60; name, &#x60;ge&#x60; gender, &#x60;db&#x60; date of birth, &#x60;ct&#x60;/&#x60;st&#x60;/&#x60;zp&#x60;/&#x60;country&#x60; location, &#x60;external_id&#x60;. Pinterest has one switch for the name and one for the location, so &#x60;fn&#x60; turns on &#x60;ln&#x60; too and any location code turns on all four. |  [optional] |



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



## Enum: List&lt;AutomaticMatchingFieldsEnum&gt;

| Name | Value |
|---- | -----|
| EM | &quot;em&quot; |
| PH | &quot;ph&quot; |
| FN | &quot;fn&quot; |
| LN | &quot;ln&quot; |
| GE | &quot;ge&quot; |
| DB | &quot;db&quot; |
| CT | &quot;ct&quot; |
| ST | &quot;st&quot; |
| ZP | &quot;zp&quot; |
| COUNTRY | &quot;country&quot; |
| EXTERNAL_ID | &quot;external_id&quot; |



