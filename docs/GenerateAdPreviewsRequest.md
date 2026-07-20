

# GenerateAdPreviewsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id used to resolve the Meta token. |  |
|**adAccountId** | **String** | Meta ad account id (act_&lt;n&gt;). |  |
|**formats** | **List&lt;String&gt;** | Meta ad_format values, one preview per format. Defaults to [DESKTOP_FEED_STANDARD]. |  [optional] |
|**existingCreativeId** | **String** | Preview an existing ad-account creative by id. Mutually exclusive with creativeSpec. |  [optional] |
|**creativeSpec** | **Map&lt;String, Object&gt;** | Raw Meta creative spec forwarded verbatim to /generatepreviews. Mutually exclusive with existingCreativeId. |  [optional] |



