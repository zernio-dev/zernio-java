

# CreateCreatorCampaignRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | Profile the campaign lives in. Creator accounts connect into the same workspace. |  |
|**name** | **String** |  |  |
|**brandName** | **String** |  |  |
|**economics** | [**CreatorCampaignEconomics**](CreatorCampaignEconomics.md) |  |  |
|**caps** | [**CreatorCampaignCaps**](CreatorCampaignCaps.md) | Omitted, the campaign starts with authenticityThreshold 40 and no other caps. |  [optional] |
|**platforms** | [**List&lt;PlatformsEnum&gt;**](#List&lt;PlatformsEnum&gt;) | Platforms creators may post on. At least one is needed to activate. &#x60;twitter&#x60; (X) needs usage-based billing: X reads are billed at cost, up to &#x60;caps.maxXReadSpendCents&#x60;, and X views are the post&#39;s impressions. &#x60;facebook&#x60; takes Page reels and videos only. |  [optional] |
|**contentRules** | **String** |  |  [optional] |
|**startsAt** | **OffsetDateTime** |  |  [optional] |
|**endsAt** | **OffsetDateTime** |  |  [optional] |
|**trackingDays** | **Integer** |  |  [optional] |
|**holdDays** | **Integer** |  |  [optional] |
|**maxPostAgeMinutes** | **Integer** | Optional maximum age in minutes of a post when it is submitted. Null or omitted (the default) accepts any age. Posts published before the campaign started are always refused. |  [optional] |
|**settlement** | [**SettlementEnum**](#SettlementEnum) |  |  [optional] |
|**branding** | [**CreatorCampaignBranding**](CreatorCampaignBranding.md) |  |  [optional] |
|**landingUrl** | **URI** | The page creator tracking links open. Required unless &#x60;attribution&#x60; is &#x60;code&#x60;. |  [optional] |
|**codeDiscountPercent** | **Integer** | What each creator&#39;s discount code takes off an order. Required unless &#x60;attribution&#x60; is &#x60;link&#x60;. |  [optional] |
|**joinApproval** | [**JoinApprovalEnum**](#JoinApprovalEnum) | manual holds creators who join through the open link as &#x60;pending&#x60; until you approve them. Personal invites are never held. |  [optional] |
|**requireDraftApproval** | **Boolean** | Creators upload a draft for review before publishing, and each submitted post must name an approved draft. |  [optional] |
|**storeAccountId** | **String** | A connected Shopify or WooCommerce store account. On &#x60;commission&#x60; and smart &#x60;retainer&#x60; economics its orders pay commission: required there, and fixed once such a campaign leaves draft.  On any campaign creators can ask for free samples of its products (&#x60;sampleProductIds&#x60;). Changing it without &#x60;sampleProductIds&#x60; clears the sample products; null removes the store and the products.  |  [optional] |
|**sampleProductIds** | **List&lt;String&gt;** | Product ids in the store that creators can ask a free sample of. Each is read from the store and saved as &#x60;sampleProducts&#x60;; an unknown product answers 404 &#x60;product_not_found&#x60;. Needs a store, otherwise 400 &#x60;missing_required_field&#x60; (&#x60;param: storeAccountId&#x60;). |  [optional] |
|**sampleContentDueDays** | **Integer** | Days after a sample is approved before a creator with no post since shows as owing content. |  [optional] |



## Enum: List&lt;PlatformsEnum&gt;

| Name | Value |
|---- | -----|
| TIKTOK | &quot;tiktok&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| YOUTUBE | &quot;youtube&quot; |
| THREADS | &quot;threads&quot; |
| PINTEREST | &quot;pinterest&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TWITTER | &quot;twitter&quot; |



## Enum: SettlementEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| EXTERNAL | &quot;external&quot; |
| TREASURY | &quot;treasury&quot; |



## Enum: JoinApprovalEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| MANUAL | &quot;manual&quot; |



