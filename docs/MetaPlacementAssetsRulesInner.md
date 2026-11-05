

# MetaPlacementAssetsRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageUrl** | **URI** | Image mode. The image to deliver for this rule&#39;s placements. |  [optional] |
|**videoUrl** | **URI** | Video mode. The video to deliver for this rule&#39;s placements. Each rule needs this or &#x60;videoId&#x60;. |  [optional] |
|**videoId** | **String** | Video mode. ID of a video already on the ad account, used for this rule instead of uploading &#x60;videoUrl&#x60;. Wins over &#x60;videoUrl&#x60;. A video still processing after 30 seconds returns 409. |  [optional] |
|**thumbnailUrl** | **URI** | Video mode (optional). Poster image for this rule&#39;s video; auto-generated when omitted. |  [optional] |
|**headline** | **String** | One headline pinned to this rule. Omit to inherit the top-level headline. |  [optional] |
|**body** | **String** | One primary text pinned to this rule. Omit to inherit the top-level body. |  [optional] |
|**description** | **String** | One link description pinned to this rule. Omit to inherit the top-level description. |  [optional] |
|**placements** | [**MetaPlacementAssetsRulesInnerPlacements**](MetaPlacementAssetsRulesInnerPlacements.md) |  |  |



