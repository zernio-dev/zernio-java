

# ListInboxComments200ResponseDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**accountUsername** | **String** |  |  [optional] |
|**content** | **String** |  |  [optional] |
|**picture** | **String** |  |  [optional] |
|**permalink** | **String** |  |  [optional] |
|**createdTime** | **OffsetDateTime** |  |  [optional] |
|**commentCount** | **Integer** |  |  [optional] |
|**likeCount** | **Integer** |  |  [optional] |
|**cid** | **String** | Bluesky content identifier |  [optional] |
|**subreddit** | **String** | Reddit subreddit name |  [optional] |
|**isAd** | **Boolean** | True when this row is an ad (boosted/dark post). &#x60;platform&#x60; is then the comment platform (facebook or instagram), &#x60;id&#x60; equals &#x60;adId&#x60;, and the thread is at GET /v1/ads/{adId}/comments. |  [optional] |
|**adId** | **String** | Internal Zernio ad id — only on ad rows (same value as &#x60;id&#x60;). |  [optional] |



