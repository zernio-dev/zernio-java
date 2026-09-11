

# GooglePmaxAssetGroupInput

Google Performance Max creative assets. At least one description must be 60 characters or fewer. Texts within each list must be distinct.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Defaults to the request name. |  [optional] |
|**finalUrl** | **URI** | Required destination URL. |  |
|**headlines** | **Set&lt;String&gt;** |  |  |
|**longHeadline** | **String** |  |  |
|**descriptions** | **Set&lt;String&gt;** | At least one description must be 60 characters or fewer. |  |
|**businessName** | **String** |  |  |
|**images** | [**GooglePmaxAssetGroupInputImages**](GooglePmaxAssetGroupInputImages.md) |  |  |
|**youtubeVideoId** | **String** | Optional existing YouTube video id. Google can generate video when omitted. Video uploads and arbitrary video URLs are not supported. |  [optional] |



