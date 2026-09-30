

# WebhookPayloadWhatsAppAccountQualityUpdatedQuality


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**SourceEnum**](#SourceEnum) | The Meta webhook field that reported the change. |  |
|**metaEvent** | **String** | Meta&#39;s &#x60;event&#x60; on phone_number_quality_update (for example FLAGGED, UNFLAGGED, UPGRADE, DOWNGRADE, ONBOARDING, THROUGHPUT_UPGRADE). Null on business_capability_update. |  |
|**qualityRating** | **String** | Current quality rating (GREEN, YELLOW, RED, UNKNOWN), read live from Meta on FLAGGED/UNFLAGGED. |  |
|**previousQualityRating** | **String** |  |  |
|**messagingLimitTier** | **String** | Current messaging limit tier, for example TIER_250, TIER_2K, TIER_10K, TIER_100K, TIER_UNLIMITED. |  |
|**previousMessagingLimitTier** | **String** |  |  |
|**displayPhoneNumber** | **String** |  |  |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PHONE_NUMBER_QUALITY_UPDATE | &quot;phone_number_quality_update&quot; |
| BUSINESS_CAPABILITY_UPDATE | &quot;business_capability_update&quot; |



