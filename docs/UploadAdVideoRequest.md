

# UploadAdVideoRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. |  |
|**adAccountId** | **String** | Meta ad account id (act_&lt;n&gt;). |  |
|**videoUrl** | **String** | Public https URL of the video; downloaded server-side (SSRF-guarded) before chunked upload. Provide exactly one of videoUrl or videoBase64. |  [optional] |
|**videoBase64** | **String** | Raw base64 video bytes, or a full data URL (the data:video/...;base64, prefix is stripped). Capped by Vercel&#39;s body limit (~4.5 MB payload). Provide exactly one of videoUrl or videoBase64. |  [optional] |
|**filename** | **String** | Optional filename shown alongside the upload session. Applied only when uploading via videoBase64. |  [optional] |



