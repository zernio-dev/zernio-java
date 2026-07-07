

# GetAdsTimeline200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rows** | [**List&lt;GetAdsTimeline200ResponseRowsInner&gt;**](GetAdsTimeline200ResponseRowsInner.md) |  |  [optional] |
|**backfillPending** | **Boolean** | Present and true only on &#x60;202&#x60; responses: part of the requested date range is still being backfilled from the platform in the background. Retry the same request shortly; it returns 200 once the range is fully ingested. |  [optional] |



