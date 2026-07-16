

# UpdateAdCampaignRequestPlatformSpecificData

Platform-specific campaign settings. The platform is implied by the `platform` body param (same convention as platformSpecificData on POST /v1/ads/create). Meta (facebook/instagram) only; other platforms return 400. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spendCap** | **BigDecimal** | Campaign lifetime spend cap, in the ad account&#39;s currency (Meta &#x60;spend_cap&#x60;). Pass null to remove the cap (0 is rejected by Meta). |  [optional] |



