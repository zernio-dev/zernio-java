

# WebhookPayloadLeadLead


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio lead ID (AdLead document ID) |  |
|**leadgenId** | **String** | Meta lead ID (the platform&#39;s leadgen_id) |  |
|**formId** | **String** | Lead Gen form ID the lead was submitted against |  |
|**formName** | **String** | Human-readable form name (best-effort; may be null) |  [optional] |
|**adId** | **String** | Meta ad ID that drove the lead (null for organic/test leads) |  [optional] |
|**adsetId** | **String** |  |  [optional] |
|**campaignId** | **String** |  |  [optional] |
|**fields** | **Map&lt;String, String&gt;** | Flattened question key -&gt; answer map. For multiple-choice questions the value is the option key (e.g. \&quot;k1\&quot;), not the display label.  |  |
|**isOrganic** | **Boolean** | True when the lead came from an organic post rather than a paid ad |  |
|**createdAt** | **OffsetDateTime** | Meta&#39;s lead creation time (ISO 8601) |  |



