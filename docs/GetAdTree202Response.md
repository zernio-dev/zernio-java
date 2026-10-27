

# GetAdTree202Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaigns** | [**List&lt;AdTreeCampaign&gt;**](AdTreeCampaign.md) |  |  [optional] |
|**pagination** | [**Pagination**](Pagination.md) |  |  [optional] |
|**syncedAt** | **OffsetDateTime** | When the most recently synced ad on this page was last read from the platform. Null before the first sync. |  [optional] |
|**previousRange** | [**AdTreeResponsePreviousRange**](AdTreeResponsePreviousRange.md) |  |  [optional] |
|**backfillPending** | **Boolean** | Always true on this response. Part of the requested range is still being backfilled; retry until the request returns 200. |  |



