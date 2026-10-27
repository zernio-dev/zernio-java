

# AccountWithFollowerStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**profileId** | [**SocialAccountProfileId**](SocialAccountProfileId.md) |  |  |
|**username** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**platformUserId** | **String** | The account&#39;s id on its platform as the platform reports it to Zernio; stable across reconnects, so it is the key to match an account against your own records. Instagram: the app-scoped user id on Instagram Login accounts (the professional account id is in &#x60;metadata.instagramScopedId&#x60;), the professional account id (&#x60;17841...&#x60;) on Facebook Login accounts. TikTok: the open_id of Zernio&#39;s TikTok app, which differs from the open_id any other app sees for the same user. Either value can be passed back as &#x60;expectedPlatformUserId&#x60; on GET /v1/connect/{platform}. |  [optional] |
|**tiktokAccountType** | [**TiktokAccountTypeEnum**](#TiktokAccountTypeEnum) | TikTok accounts only. The account type TikTok reported when the account was connected. &#x60;personal&#x60; accounts cannot use TikTok direct messages through the API (TikTok limits Business Messaging to Business Accounts): skip the inbox for them and tell the user to switch to a Business Account in the TikTok app, then reconnect. &#x60;business&#x60; is the prerequisite, not a guarantee; messaging also needs the messaging scopes granted and TikTok&#39;s regional availability. &#x60;unknown&#x60; on accounts connected before this was captured or whose grant left out the account-type scope. |  [optional] |
|**profilePicture** | **String** | URL to the account&#39;s profile picture on the platform. May be null if the platform does not provide one. |  [optional] |
|**profileUrl** | **String** | Full profile URL for the connected account on its platform. |  [optional] |
|**isActive** | **Boolean** |  |  |
|**needsReconnection** | **Boolean** | The platform definitively reported the stored OAuth token as dead. While true, GET /v1/connect/{platform}/ads returns a fresh authUrl (implicit force&#x3D;true) instead of alreadyConnected, so re-running the connect flow recovers the account. Cleared automatically when the account is re-authorized.  |  [optional] |
|**followersCount** | **BigDecimal** | Follower count (only included if user has analytics add-on) |  [optional] |
|**followersLastUpdated** | **OffsetDateTime** | Last time follower count was updated (only included if user has analytics add-on) |  [optional] |
|**parentAccountId** | **String** | Reference to the parent posting SocialAccount. Set for ads accounts that share or derive from a posting account&#39;s OAuth token. null for standalone ads (Google Ads) and all posting accounts. Meta ads business-login accounts also have no parent.  |  [optional] |
|**enabled** | **Boolean** | Whether the user explicitly activated this account. false means the account was created as a side effect (e.g., posting account auto-created when user connected ads first). GET /v1/accounts still returns such accounts unless &#x60;excludeHidden&#x3D;true&#x60; is passed. They cannot be posted to (&#x60;ACCOUNT_NOT_ENABLED_FOR_POSTING&#x60;) and are not billed as connected accounts. On an ads account (&#x60;metaads&#x60;, &#x60;googleads&#x60;, ...) the value does not hide the connection: ads accounts are listed whatever their &#x60;enabled&#x60; value and keep working for ads.  |  [optional] |
|**rateLimitedUntil** | **OffsetDateTime** | End of the account&#39;s publishing cooldown. Compare it with the current time: a value in the past means the cooldown has ended (the field is cleared on the next successful publish), null means no cooldown since the last successful publish. A cooldown starts when a post to the account fails with &#x60;errorCategory&#x60; &#x60;user_abuse&#x60; (spam, abuse or rate-limit errors), or when 10 or more posts to it fail within an hour with &#x60;user_content&#x60;, &#x60;platform_error&#x60;, &#x60;platform_rate_limit&#x60; or &#x60;unknown&#x60;. It doubles with each start inside a 24-hour window that opens at the first one (10, 20, 40, 80 minutes and so on, capped at 24 hours). On a YouTube account with a recorded successful upload it instead runs until 24 hours after that upload, or 1 hour when that upload is older than 24 hours. While it is in the future, POST /v1/posts (drafts excepted) and POST /v1/posts/{postId}/retry return 429 for this account, and this account&#39;s pending targets on posts scheduled before the cooldown ends are failed when it starts.  |  [optional] |
|**metadata** | **Object** | Platform-specific metadata. Fields vary by platform. For WhatsApp accounts, includes: - qualityRating: Phone number quality rating from Meta (GREEN, YELLOW, RED, or UNKNOWN) - nameStatus: Display name review status (APPROVED, PENDING_REVIEW, DECLINED, or NONE). A declined or pending display name does not by itself block sending; sendability is reported separately via health_status (can_send_message). - messagingLimitTier: Maximum unique business-initiated conversations per 24h rolling window (TIER_250, TIER_1K, TIER_10K, TIER_100K, or TIER_UNLIMITED). Scales automatically as quality rating improves. - verifiedName: Meta-verified business display name - displayPhoneNumber: Formatted phone number (e.g., \&quot;+1 555-123-4567\&quot;) - wabaId: WhatsApp Business Account ID - phoneNumberId: Meta phone number ID  For Meta ads business-login accounts: - tokenType: system-user - businessId: The owning Business Manager ID when there is one owner; null for multiple owners. - businessIds: Owning Business Manager IDs discovered from granted ad accounts. - grantedAdAccountIds: Ad-account IDs granted to the token. - adAccountBusinesses: Map from ad-account ID to its owning business ID or null. - availablePages: Granted Page IDs and names. No Page tokens are exposed. - selectedPageId: The Page selected for creatives and lead forms, or null. - scopedAdAccountIds: Existing sync scope preserved on reconnect. Non-expiring tokens have no tokenExpiresAt field. Parent posting reconnects do not replace this token.  For LinkedIn accounts, profileData carries the profile details refreshed on each daily snapshot: - profileData.bio: The member&#39;s headline for personal accounts, or the organization description for organization accounts. null when the member has not set one. - profileData.extraData.vanityName: The member&#39;s profile slug, i.e. the /in/{vanityName} segment of profileUrl. Personal accounts only; an organization&#39;s own slug is in metadata.organizationInfo.vanityName.  For Instagram accounts: - loginMethod: \&quot;facebook_login\&quot; when the account was connected through Facebook Login. Absent on accounts connected with Instagram Login. On facebook_login accounts, comment reads leave hidden comments out entirely instead of returning them with isHidden true. - instagramScopedId: the Instagram professional account id (&#x60;17841...&#x60;). On Instagram Login accounts this is the id that is the same whichever app connected the account, while platformUserId is app-scoped; Facebook Login accounts hold this id as platformUserId.  For X (Twitter) accounts: - profileData.extraData.isPremium: Whether X reports a paid subscription (Basic, Premium, Premium+, or a blue verified badge), which raises the post length limit from 280 to 25,000 characters. Read live at connect and reconnect and refreshed by the daily follower snapshot; because X intermittently reports no subscription for subscribed accounts, a cancellation is stored on the fourth consecutive daily snapshot that reports it (about four days). Accounts connected before the extraData layout carry the same flag at profileData.isPremium.  |  [optional] |
|**currentFollowers** | **BigDecimal** | Current follower count |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**growth** | **BigDecimal** | Follower change over period |  [optional] |
|**growthPercentage** | **BigDecimal** | Percentage growth |  [optional] |
|**dataPoints** | **BigDecimal** | Number of historical snapshots |  [optional] |
|**accountStats** | [**AccountWithFollowerStatsAllOfAccountStats**](AccountWithFollowerStatsAllOfAccountStats.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| TIKTOK | &quot;tiktok&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| YOUTUBE | &quot;youtube&quot; |
| LINKEDIN | &quot;linkedin&quot; |
| TWITTER | &quot;twitter&quot; |
| THREADS | &quot;threads&quot; |
| PINTEREST | &quot;pinterest&quot; |
| REDDIT | &quot;reddit&quot; |
| BLUESKY | &quot;bluesky&quot; |
| GOOGLEBUSINESS | &quot;googlebusiness&quot; |
| TELEGRAM | &quot;telegram&quot; |
| SNAPCHAT | &quot;snapchat&quot; |
| DISCORD | &quot;discord&quot; |
| SLACK | &quot;slack&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| SHOPIFY | &quot;shopify&quot; |
| WORDPRESS | &quot;wordpress&quot; |
| WIX | &quot;wix&quot; |
| LINKEDINADS | &quot;linkedinads&quot; |
| METAADS | &quot;metaads&quot; |
| PINTERESTADS | &quot;pinterestads&quot; |
| TIKTOKADS | &quot;tiktokads&quot; |
| XADS | &quot;xads&quot; |
| GOOGLEADS | &quot;googleads&quot; |
| OPENAIADS | &quot;openaiads&quot; |
| REDDITADS | &quot;redditads&quot; |
| SMS | &quot;sms&quot; |
| PHONE | &quot;phone&quot; |
| RCS | &quot;rcs&quot; |
| WHOPADS | &quot;whopads&quot; |
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |
| HUBSPOT | &quot;hubspot&quot; |
| WEBFLOW | &quot;webflow&quot; |
| GOOGLEANALYTICS | &quot;googleanalytics&quot; |



## Enum: TiktokAccountTypeEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| PERSONAL | &quot;personal&quot; |
| UNKNOWN | &quot;unknown&quot; |



