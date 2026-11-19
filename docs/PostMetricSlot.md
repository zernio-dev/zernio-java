

# PostMetricSlot


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfWeek** | **Integer** | UTC weekday the posts were published, 1 (Monday) to 7. |  |
|**hour** | **Integer** | UTC hour the posts were published, 0 to 23. |  |
|**postCount** | **Integer** | Posts published in the slot that have been synced at least once. |  |
|**metrics** | **Map&lt;String, BigDecimal&gt;** | Each metric asked, summed over each post&#39;s latest snapshot; engagementRate pools them. null when no platform of the slot reports it. |  |



