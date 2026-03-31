

# UpdatePostMetadataRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) | The platform to update metadata on |  |
|**videoId** | **String** | YouTube video ID (required for direct mode, ignored for post-based mode) |  [optional] |
|**accountId** | **String** | Zernio social account ID (required for direct mode, ignored for post-based mode) |  [optional] |
|**title** | **String** | New video title (max 100 characters for YouTube) |  [optional] |
|**description** | **String** | New video description |  [optional] |
|**tags** | **List&lt;String&gt;** | Array of keyword tags (max 500 characters combined for YouTube) |  [optional] |
|**categoryId** | **String** | YouTube video category ID |  [optional] |
|**privacyStatus** | [**PrivacyStatusEnum**](#PrivacyStatusEnum) | Video privacy setting |  [optional] |
|**thumbnailUrl** | **URI** | Public URL of a custom thumbnail image (JPEG, PNG, or GIF, max 2 MB, recommended 1280x720). Works on any video you own, including existing videos not published through Zernio. The channel must be verified (phone verification) to set custom thumbnails. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| YOUTUBE | &quot;youtube&quot; |



## Enum: PrivacyStatusEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |
| UNLISTED | &quot;unlisted&quot; |



