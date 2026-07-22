

# CreateAdCreativeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token and Page. |  |
|**adAccountId** | **String** | Meta ad account id (act_&lt;n&gt;). |  |
|**headline** | **String** |  |  |
|**body** | **String** | Primary text |  |
|**description** | **String** | Link description below the headline; omitted &#x3D; Meta scrapes the destination&#39;s OG description. |  [optional] |
|**callToAction** | **String** | CTA type (same whitelist as POST /v1/ads/create). |  [optional] |
|**linkUrl** | **URI** |  |  |
|**imageUrl** | **URI** | Publicly reachable image; uploaded to the account&#39;s library server-side. |  [optional] |
|**imageHash** | **String** | Existing library image hash (POST /v1/ads/images or GET /v1/ads/images). |  [optional] |
|**carouselCards** | [**List&lt;CreateAdCreativeRequestCarouselCardsInner&gt;**](CreateAdCreativeRequestCarouselCardsInner.md) |  |  [optional] |
|**urlTags** | **String** | Appended to every outbound URL (e.g. utm_source&#x3D;fb). |  [optional] |



