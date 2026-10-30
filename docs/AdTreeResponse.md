

# AdTreeResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaigns** | [**List&lt;AdTreeCampaign&gt;**](AdTreeCampaign.md) |  |  [optional] |
|**pagination** | [**Pagination**](Pagination.md) |  |  [optional] |
|**syncedAt** | **OffsetDateTime** | When the most recently synced ad on this page was last read from the platform. Null before the first sync. |  [optional] |
|**previousRange** | [**AdTreeResponsePreviousRange**](AdTreeResponsePreviousRange.md) |  |  [optional] |
|**resultMetrics** | [**List&lt;CampaignResultMetric&gt;**](CampaignResultMetric.md) | Only with &#x60;results&#x3D;true&#x60;. Your metrics and formulas, to label each campaign&#39;s &#x60;results&#x60;. |  [optional] |
|**backfillPending** | **Boolean** | Meta only. Present and true while historical data is being backfilled. |  [optional] |



