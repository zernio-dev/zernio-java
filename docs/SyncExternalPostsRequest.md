

# SyncExternalPostsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | SocialAccount ID whose posts to sync. Must be connected to Zernio. |  |
|**url** | **String** | The post URL to locate. Optional. Provide &#x60;url&#x60; or &#x60;postId&#x60; to return a specific post; omit both to just refresh and return the account&#39;s recent posts. |  [optional] |
|**postId** | **String** | The platform post/media/video id to locate, as an alternative to &#x60;url&#x60;. Optional. |  [optional] |



