

# AdsTimelineResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backfillPending** | **Boolean** | Meta only. Present and true while historical data is being backfilled. |  [optional] |
|**previousRows** | **List&lt;Map&lt;String, Object&gt;&gt;** | Only with &#x60;compare&#x3D;previous&#x60;. The daily rows of &#x60;previousRange&#x60;, in the same shape as &#x60;rows&#x60;. |  [optional] |
|**previousRange** | [**AdsTimelineResponsePreviousRange**](AdsTimelineResponsePreviousRange.md) |  |  [optional] |
|**rows** | [**List&lt;AdsTimelineResponseRowsInner&gt;**](AdsTimelineResponseRowsInner.md) |  |  [optional] |



