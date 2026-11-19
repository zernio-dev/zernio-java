

# PostMetricChange


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**profileId** | **String** |  |  |
|**platform** | **String** |  |  |
|**platformPostId** | **String** |  |  |
|**publishedAt** | **String** |  |  |
|**syncedAt** | **String** | When the account&#39;s sync cycle that read these numbers started. Not an order: resume with the cursor only. |  |
|**deleted** | **Boolean** | True when the post was removed from the platform. |  |
|**metrics** | **Map&lt;String, BigDecimal&gt;** | Each metric asked, as the platform reported it in this change; null when the post&#39;s platform does not report it. |  |
|**breakdowns** | [**Map&lt;String, PostMetricRowBreakdownsValue&gt;**](PostMetricRowBreakdownsValue.md) |  |  [optional] |



