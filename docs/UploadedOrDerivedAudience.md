

# UploadedOrDerivedAudience

customer_list, website, lookalike or engagement audience (uploaded or derived from a source).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**adAccountId** | **String** | Platform ad account ID. Must start with act_ for Meta; bare platform id for others (Google customer id, X/TikTok/LinkedIn/Pinterest account id). |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**matchRules** | [**List&lt;UploadedOrDerivedAudienceMatchRulesInner&gt;**](UploadedOrDerivedAudienceMatchRulesInner.md) | Required for website_retargeting audiences (LinkedIn only). Each rule is a URL pattern; a member who visits any matching page enters the segment. Needs the LinkedIn Insight Tag installed on the customer&#39;s site; the segment only starts filling once the tag reports visits.  The response&#39;s &#x60;platformAudienceId&#x60; is the LinkedIn adSegment id, valid for downstream use. These segments appear in GET /v1/ads/audiences with  &#x60;type: website_retargeting&#x60; once LinkedIn has finished building them.  |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Required for engagement audiences (LinkedIn only): what members engaged with: a video/leadgen/single-image ad campaign, a Company Page or an Event page.  |  [optional] |
|**trigger** | **String** | Required for engagement audiences. The action, validated by LinkedIn against &#x60;sourceType&#x60;. Common values: VIDEO_ADS FIRST_QUARTILE / MIDPOINT / THIRD_QUARTILE / FULL_COMPLETE; LEAD_GEN_FORMS VIEW_FORM / LEAD_FORM_SUBMIT; ORGANIZATION_PAGES VIEW / CTA_CLICK; EVENT_PAGES RSVPED / VIDEO_VIEWED / ENGAGEMENT / CLICK.  |  [optional] |
|**lookbackDays** | [**LookbackDaysEnum**](#LookbackDaysEnum) | Required for engagement audiences. Rolling window. |  [optional] |
|**engagementSources** | **List&lt;String&gt;** | Required for engagement audiences. Campaign URNs for the ad source types, organization URNs for pages and events. LinkedIn creates one rule per source, all sharing the same trigger and lookbackDays.  |  [optional] |
|**companies** | [**List&lt;UploadedOrDerivedAudienceCompaniesInner&gt;**](UploadedOrDerivedAudienceCompaniesInner.md) | Required for company_list audiences (LinkedIn only): plain-text company rows for account targeting. Each row needs at least one identifier. Not hashed, LinkedIn matches these against its own company graph. LinkedIn recommends 1,000+ companies for a usable match rate and takes up to 48h to process the list. Replace the list later with POST /v1/ads/audiences/{audienceId}/companies.  |  [optional] |
|**pixelId** | **String** | website: the Meta pixel, TikTok pixel or Pinterest tag id. Required on those three, rejected on Google. |  [optional] |
|**retentionDays** | **Integer** | Required for website (Meta max 180, TikTok 7/14/30/60/90/180, Pinterest and Google max 540), meta_engagement (max 365) and tiktok_engagement (7/14/30/60/90/180; organic and live video and most business-account events only 7/14/30). |  [optional] |
|**engagementSource** | [**EngagementSourceEnum**](#EngagementSourceEnum) | Required for meta_engagement audiences (Meta only): what people engaged with. &#x60;page&#x60; &#x3D; a Facebook Page, &#x60;instagram&#x60; &#x3D; an IG professional account, &#x60;video&#x60; &#x3D; a video.  |  [optional] |
|**sourceId** | **String** | Required for meta_engagement: the Page / IG account / video id. |  [optional] |
|**event** | **String** | meta_engagement: the engagement event; defaults per source (page → page_engaged, instagram → ig_business_profile_all, video → video_watched). Ignored when &#x60;rule&#x60; is provided.  website on TikTok: the pixel event (default &#x60;PAGE BROWSE&#x60;). website on Pinterest: the tag event (&#x60;pagevisit&#x60;, &#x60;signup&#x60;, &#x60;checkout&#x60;, &#x60;viewcategory&#x60;, &#x60;search&#x60;, &#x60;addtocart&#x60;, &#x60;watchvideo&#x60;, &#x60;lead&#x60;, &#x60;custom&#x60; or a partner-defined event).  tiktok_engagement (required): the TikTok engagement event, validated per &#x60;source&#x60; (TikTok&#39;s filter values, spaces included): - ads: &#x60;CLICK&#x60;, &#x60;IMPRESSION&#x60;, &#x60;PLAY 2S&#x60;, &#x60;PLAY 6S&#x60;, &#x60;PLAY 25&#x60;, &#x60;PLAY 50&#x60;, &#x60;PLAY 75&#x60;,   &#x60;PLAY OVER&#x60;, and the &#x60;ENGAGEMENT APP PROFILE&#x60; / &#x60;ENGAGEMENT TIKTOK INSTANT&#x60; /   &#x60;ENGAGEMENT COLLECTION ADS&#x60; &#x60;CLICK&#x60; and &#x60;IMPRESSION&#x60; events. - organic_video: &#x60;ORGANIC VIDEO PLAY 2S&#x60;, &#x60;ORGANIC VIDEO PLAY 6S&#x60;,   &#x60;ORGANIC VIDEO PLAY OVER&#x60;, &#x60;ORGANIC VIDEO ENGAGEMENT&#x60;. - live_video: &#x60;LIVE VIDEO VIEW&#x60;, &#x60;LIVE VIDEO ENGAGEMENT&#x60;. - business_account: &#x60;BUSINESS ACCOUNT PROFILE FOLLOW&#x60;, &#x60;BUSINESS ACCOUNT PROFILE VISIT&#x60;,   &#x60;BUSINESS ACCOUNT ENGAGEMENT&#x60;, &#x60;BUSINESS ACCOUNT PLAY 2S&#x60;, &#x60;BUSINESS ACCOUNT PLAY 6S&#x60;,   &#x60;BUSINESS ACCOUNT PLAY OVER&#x60; and the rest of TikTok&#39;s business-account events. An unknown value is a 400 that lists the valid ones.  |  [optional] |
|**sourceAudienceId** | **String** | Required for lookalike audiences |  [optional] |
|**country** | **String** | 2-letter code, required for lookalike audiences |  [optional] |
|**ratio** | **BigDecimal** | lookalike on Meta (0.01-0.20) and Pinterest (0.01-0.10, whole percents). Rejected on TikTok and Google. |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | lookalike on TikTok and Google: audience breadth. Rejected on Meta and Pinterest. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | Required for tiktok_engagement: what people engaged with. |  [optional] |
|**sourceIds** | **List&lt;String&gt;** | tiktok_engagement: ad group / campaign ids for &#x60;ads&#x60;, video ids for &#x60;organic_video&#x60; and &#x60;live_video&#x60; (max 10). Required except for &#x60;business_account&#x60;. |  [optional] |
|**identityId** | **String** | tiktok_engagement: the TikTok identity that owns the videos or business account. Required for organic_video, live_video and business_account. |  [optional] |
|**identityType** | [**IdentityTypeEnum**](#IdentityTypeEnum) | tiktok_engagement: type of &#x60;identityId&#x60;. |  [optional] |
|**identityAuthorizedBcId** | **String** | tiktok_engagement: required when identityType is BC_AUTH_TT. |  [optional] |
|**engagerType** | [**EngagerTypeEnum**](#EngagerTypeEnum) | pinterest_engagement: Pinterest&#39;s &#x60;engager_type&#x60;, passed through when set. |  [optional] |
|**engagementType** | [**EngagementTypeEnum**](#EngagementTypeEnum) | pinterest_engagement: limit to one engagement action. |  [optional] |
|**engagementDomains** | **List&lt;String&gt;** | pinterest_engagement: people who engaged with Pins from these domains. The domain must be claimed on the Pinterest account or Pinterest rejects it. |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | pinterest_engagement: people who engaged with these campaigns&#39; ads. |  [optional] |
|**adIds** | **List&lt;String&gt;** | pinterest_engagement: people who engaged with these ads. |  [optional] |
|**pinIds** | **List&lt;String&gt;** | pinterest_engagement: people who engaged with these Pins. At least one of engagementDomains, campaignIds, adIds or pinIds is required. |  [optional] |
|**urlContains** | **String** | website on Meta, TikTok and Google. Narrows the audience from all visitors to visitors of URLs containing this substring. Ignored when &#x60;rule&#x60; is supplied. A 400 on Pinterest, which only matches exact URLs.  |  [optional] |
|**rule** | **Object** | Meta only (a 400 elsewhere). Optional raw Meta rule, replacing the one we build. Omit it for all visitors of &#x60;pixelId&#x60;, or use &#x60;urlContains&#x60; for the common page-match case.  For &#x60;website&#x60; this is Meta&#39;s Flexible Audience Rule and is VALIDATED before we call Meta: every entry in &#x60;inclusions.rules&#x60; (and &#x60;exclusions.rules&#x60;) must carry &#x60;event_sources&#x60;, &#x60;retention_seconds&#x60; AND &#x60;filter&#x60;. Meta rejects a rule missing any of the three with code 100 / subcode 1713098 (\&quot;Invalid rule JSON format\&quot;), so a bad shape is a 400 here instead. The pre-2018 flat shapes (&#x60;{url: ...}&#x60;, &#x60;{event: ...}&#x60;) are not accepted by Meta at all (subcode 1870029).  Example, visitors of /checkout in the last 30 days: &#x60;{\&quot;inclusions\&quot;:{\&quot;operator\&quot;:\&quot;or\&quot;,\&quot;rules\&quot;:[{\&quot;event_sources\&quot;:[{\&quot;id\&quot;:\&quot;&lt;pixelId&gt;\&quot;,\&quot;type\&quot;:\&quot;pixel\&quot;}],\&quot;retention_seconds\&quot;:2592000,\&quot;filter\&quot;:{\&quot;operator\&quot;:\&quot;and\&quot;,\&quot;filters\&quot;:[{\&quot;field\&quot;:\&quot;url\&quot;,\&quot;operator\&quot;:\&quot;i_contains\&quot;,\&quot;value\&quot;:\&quot;/checkout\&quot;}]}}]}}&#x60;  Note Meta DERIVES &#x60;retention_days&#x60; from &#x60;retention_seconds&#x60; and stores &#x60;event_sources[].id&#x60; as a number, so a rule read back will not be byte-identical to the one you sent.  For &#x60;meta_engagement&#x60; the rule is forwarded verbatim and NOT validated: that type has two dialects (the &#x60;video&#x60; source uses a legacy flat array), so no single schema covers both.  |  [optional] |
|**customerFileSource** | **String** | Data source declaration for GDPR compliance (customer_list only) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_LIST | &quot;customer_list&quot; |
| COMPANY_LIST | &quot;company_list&quot; |
| ENGAGEMENT | &quot;engagement&quot; |
| META_ENGAGEMENT | &quot;meta_engagement&quot; |
| TIKTOK_ENGAGEMENT | &quot;tiktok_engagement&quot; |
| PINTEREST_ENGAGEMENT | &quot;pinterest_engagement&quot; |
| WEBSITE | &quot;website&quot; |
| WEBSITE_RETARGETING | &quot;website_retargeting&quot; |
| LOOKALIKE | &quot;lookalike&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| VIDEO_ADS | &quot;VIDEO_ADS&quot; |
| LEAD_GEN_FORMS | &quot;LEAD_GEN_FORMS&quot; |
| ORGANIZATION_PAGES | &quot;ORGANIZATION_PAGES&quot; |
| EVENT_PAGES | &quot;EVENT_PAGES&quot; |
| SINGLE_IMAGE_ADS | &quot;SINGLE_IMAGE_ADS&quot; |



## Enum: LookbackDaysEnum

| Name | Value |
|---- | -----|
| NUMBER_30 | 30 |
| NUMBER_60 | 60 |
| NUMBER_90 | 90 |
| NUMBER_180 | 180 |
| NUMBER_365 | 365 |



## Enum: EngagementSourceEnum

| Name | Value |
|---- | -----|
| PAGE | &quot;page&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| VIDEO | &quot;video&quot; |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| NARROW | &quot;narrow&quot; |
| BALANCED | &quot;balanced&quot; |
| BROAD | &quot;broad&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| ADS | &quot;ads&quot; |
| ORGANIC_VIDEO | &quot;organic_video&quot; |
| LIVE_VIDEO | &quot;live_video&quot; |
| BUSINESS_ACCOUNT | &quot;business_account&quot; |



## Enum: IdentityTypeEnum

| Name | Value |
|---- | -----|
| TT_USER | &quot;TT_USER&quot; |
| BC_AUTH_TT | &quot;BC_AUTH_TT&quot; |



## Enum: EngagerTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: EngagementTypeEnum

| Name | Value |
|---- | -----|
| CLICK | &quot;click&quot; |
| SAVE | &quot;save&quot; |
| CLOSEUP | &quot;closeup&quot; |
| COMMENT | &quot;comment&quot; |
| LIKE | &quot;like&quot; |



