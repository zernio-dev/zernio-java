

# GetAdsTimeline202Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backfillPending** | **Boolean** | Always true on this response. Part of the requested range is still being backfilled; retry until the request returns 200. |  |
|**previousRows** | **List&lt;Map&lt;String, Object&gt;&gt;** | Only with &#x60;compare&#x3D;previous&#x60;. The daily rows of &#x60;previousRange&#x60;, in the same shape as &#x60;rows&#x60;. |  [optional] |
|**previousRange** | [**AdsTimelineResponsePreviousRange**](AdsTimelineResponsePreviousRange.md) |  |  [optional] |
|**rows** | [**List&lt;AdsTimelineResponseRowsInner&gt;**](AdsTimelineResponseRowsInner.md) |  |  [optional] |



