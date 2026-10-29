

# CreateStandaloneAdRequestBrandIdentity

TikTok only; non-TikTok platforms ignore this field. Synthetic Brand Identity used when the ad attributes to a CUSTOMIZED_USER (instead of a real TT_USER @username).  Required on the FIRST CUSTOMIZED_USER ad on a `tiktokads` SocialAccount with no cached identity. Omit it on later ads: the identity is cached on the account after first creation.  Alternative: configure once via `PATCH /v1/connect/tiktok-ads`, then create ads without this field. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Brand name shown above the ad on TikTok. |  |
|**imageUrl** | **URI** | Public URL of a square brand image (≥98×98 px, JPG/PNG). Used as the brand avatar on the ad. |  |



