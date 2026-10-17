

# UploadAdVideoRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (posting or ads variant); its platform decides where the campaign is created. |  |
|**adAccountId** | **String** | Platform ad account id (Meta act_&lt;n&gt;, Google customer id, LinkedIn account id, ...). |  |
|**videoUrl** | **String** | Public https URL of the video; downloaded server-side (SSRF-guarded) before chunked upload. Provide exactly one of videoUrl or videoBase64. |  [optional] |
|**videoBase64** | **String** | Raw base64 video bytes, or a full data URL (the data:video/...;base64, prefix is stripped). Capped by Vercel&#39;s body limit (~4.5 MB payload). Provide exactly one of videoUrl or videoBase64. |  [optional] |
|**filename** | **String** | Optional file name, sent to Meta as the video&#39;s name and title so it shows and is searchable in the Ads Manager media library. Applies to both videoUrl and videoBase64. Without it (and without name), a videoUrl upload is named after the last path segment of the URL. |  [optional] |
|**name** | **String** | Optional video name shown in the Ads Manager media library. Takes precedence over filename. |  [optional] |
|**async** | **Boolean** | true: answer 202 once Meta accepts the upload instead of waiting for processing. Poll GET /v1/ads/videos/{videoId} or subscribe to ad.video.processed. |  [optional] |



