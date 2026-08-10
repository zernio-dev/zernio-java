

# CreateCustomConversionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** | Meta ad account id (act_&lt;n&gt;). |  |
|**name** | **String** | Also the reuse key, together with pixelId. |  |
|**pixelId** | **String** | Meta pixel id (event_source_id). From GET /v1/accounts/{accountId}/tracking-tags. |  |
|**customEventType** | **String** | Meta custom_event_type, e.g. LEAD, PURCHASE, OTHER. |  |
|**rule** | **Object** | Meta conversion rule, forwarded verbatim. |  |



