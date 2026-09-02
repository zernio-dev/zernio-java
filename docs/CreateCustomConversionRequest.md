

# CreateCustomConversionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** | Platform ad account id (Meta act_&lt;n&gt;, Google customer id, LinkedIn account id, ...). |  |
|**name** | **String** | Also the reuse key, together with pixelId. |  |
|**pixelId** | **String** | Meta pixel id (event_source_id). From GET /v1/accounts/{accountId}/tracking-tags. |  |
|**customEventType** | **String** | Meta custom_event_type, e.g. LEAD, PURCHASE, OTHER. |  |
|**rule** | **Object** | Meta conversion rule, forwarded verbatim. |  |



