

# ListInboxComments200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**content** | **String** | The post text/caption. On ad rows (isAd: true) this is the AD NAME, not the underlying post&#39;s caption — the creative text isn&#39;t exposed here. |  [optional] |
|**picture** | **String** | Post media thumbnail. On ad rows this is the ad creative thumbnail. |  [optional] |
|**permalink** | **String** | Public URL of the post. On ad rows: the Facebook dark-post URL (facebook placement) or the IG media permalink (instagram placement); may be null when unknown. |  [optional] |
|**createdTime** | **OffsetDateTime** |  |  [optional] |
|**commentCount** | **Integer** |  |  [optional] |
|**likeCount** | **Integer** | Not fetched for ad rows (always 0 there). |  [optional] |
|**cid** | **String** | Bluesky content identifier |  [optional] |
|**subreddit** | **String** | Reddit subreddit name |  [optional] |
|**isAd** | **Boolean** | True when this row is an ad (boosted/dark post). &#x60;platform&#x60; is then the placement (facebook &#x3D; the Page dark post / instagram &#x3D; the IG media), &#x60;id&#x60; is &#x60;{adId}:{placement}&#x60;, and the thread is at GET /v1/ads/{adId}/comments?placement&#x3D;{placement}. |  [optional] |
|**adId** | **String** | Internal Zernio ad id — only on ad rows. |  [optional] |
|**placement** | [**PlacementEnum**](#PlacementEnum) | Which side of the ad this row&#39;s comments are on — only on ad rows. |  [optional] |



## Enum: PlacementEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |



