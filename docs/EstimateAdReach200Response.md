

# EstimateAdReach200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** | Whether a pre-flight estimate is available on this platform. False for Google and TikTok. |  |
|**lower** | **Integer** | Lower bound of the estimated reachable audience. Present only when available. |  [optional] |
|**upper** | **Integer** | Upper bound of the estimated reachable audience. Present only when available. |  [optional] |
|**daily** | **Integer** | Optional estimated daily reach/results at the given budget, when the platform returns it. |  [optional] |
|**currency** | **String** | Currency of any monetary fields in the estimate, when applicable. |  [optional] |
|**estimateReady** | **Boolean** | Meta only. False when Meta is still computing the estimate (the audience is too new); retry shortly. |  [optional] |



