

# BoostPost201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ad** | [**Ad**](Ad.md) |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**instagramVideoFallback** | [**InstagramVideoFallback**](InstagramVideoFallback.md) |  |  [optional] |
|**warnings** | **List&lt;String&gt;** | Present with instagramVideoFallback: one human-readable line saying how the Instagram video was boosted. On Meta also present, as an entry starting with &#x60;activation_failed:&#x60;, when Meta refused the final switch to ACTIVE of the campaign, ad set or ad this boost created: nothing was deleted, &#x60;message&#x60; says not everything is ACTIVE, and the entry names what was kept PAUSED and what was switched ACTIVE, and quotes Meta&#39;s error and the status calls that switch the PAUSED ones on later. A retry without Idempotency-Key inside the 10-minute dedup window that finds the stored ad PAUSED although it asks for ACTIVE gets a &#x60;replayed_paused:&#x60; entry with the same status calls instead. |  [optional] |



