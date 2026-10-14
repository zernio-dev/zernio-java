

# GetAd200ResponseDarkPost

Only when `{adId}` is a Facebook ad dark post with no resolvable ad (then `ad` is null).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**platformPostId** | **String** | The dark post id, &#x60;{pageId}_{postId}&#x60;. |  [optional] |
|**pageId** | **String** |  |  [optional] |
|**isDarkPost** | **Boolean** | Always true. |  [optional] |
|**adId** | **String** | Always null: Meta exposes no link from a placement dark post to its ad. |  [optional] |
|**accountId** | **String** | Zernio Meta Ads account id for the Page, null when none is connected. |  [optional] |
|**facebookAccountId** | **String** | Zernio Facebook account id of the Page. |  [optional] |
|**platformAdAccountIds** | **List&lt;String&gt;** | Meta ad accounts (&#x60;act_...&#x60;) with synced ads on this Page. |  [optional] |
|**firstSeenAt** | **OffsetDateTime** |  |  [optional] |
|**lastActivityAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |



