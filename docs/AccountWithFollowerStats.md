

# AccountWithFollowerStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**profileId** | [**SocialAccountProfileId**](SocialAccountProfileId.md) |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**profileUrl** | **String** | Full profile URL for the connected account on its platform. |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**followersCount** | **BigDecimal** | Follower count (only included if user has analytics add-on) |  [optional] |
|**followersLastUpdated** | **OffsetDateTime** | Last time follower count was updated (only included if user has analytics add-on) |  [optional] |
|**metadata** | **Object** | Platform-specific metadata. Fields vary by platform. For WhatsApp accounts, includes: - &#x60;qualityRating&#x60;: Phone number quality rating from Meta (&#x60;GREEN&#x60;, &#x60;YELLOW&#x60;, &#x60;RED&#x60;, or &#x60;UNKNOWN&#x60;) - &#x60;nameStatus&#x60;: Display name review status (&#x60;APPROVED&#x60;, &#x60;PENDING_REVIEW&#x60;, &#x60;DECLINED&#x60;, or &#x60;NONE&#x60;). Messages cannot be sent until the display name is approved by Meta. - &#x60;messagingLimitTier&#x60;: Maximum unique business-initiated conversations per 24h rolling window (&#x60;TIER_250&#x60;, &#x60;TIER_1K&#x60;, &#x60;TIER_10K&#x60;, &#x60;TIER_100K&#x60;, or &#x60;TIER_UNLIMITED&#x60;). Scales automatically as quality rating improves. - &#x60;verifiedName&#x60;: Meta-verified business display name - &#x60;displayPhoneNumber&#x60;: Formatted phone number (e.g., \&quot;+1 555-123-4567\&quot;) - &#x60;wabaId&#x60;: WhatsApp Business Account ID - &#x60;phoneNumberId&#x60;: Meta phone number ID  |  [optional] |
|**profilePicture** | **String** |  |  [optional] |
|**currentFollowers** | **BigDecimal** | Current follower count |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**growth** | **BigDecimal** | Follower change over period |  [optional] |
|**growthPercentage** | **BigDecimal** | Percentage growth |  [optional] |
|**dataPoints** | **BigDecimal** | Number of historical snapshots |  [optional] |
|**accountStats** | [**AccountWithFollowerStatsAllOfAccountStats**](AccountWithFollowerStatsAllOfAccountStats.md) |  |  [optional] |



