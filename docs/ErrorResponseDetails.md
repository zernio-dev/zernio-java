

# ErrorResponseDetails

Meta ads refusals customers hit most come back with their own `code` instead of `platform_api_error`, the field to fix in `param`, and `details.fix` ({ label, url }) pointing at the Meta page that resolves it: `ad_account_payment_required`, `ad_account_policy_not_accepted`, `meta_security_check_required`, `meta_action_blocked`, `whatsapp_number_not_linked` and `invalid_targeting`. Meta's own error stays in the message and in `platformError`. Additional structured context (e.g. field-level validation errors), for example `privateReplyConsumed` on the private-reply endpoint's 400 when the comment's single reply is already spent, and `privateReplyOutcome: \"unknown\"` on its 502 when Meta answered a server error and the reply may have been delivered.  On a Google Ads or YouTube Analytics 429 it carries `quotaExhausted: true`, which marks the failure as Google's own quota rather than a Zernio rate limit, so you can keep calling other platforms instead of backing off everywhere. When Google names the scope it also carries `quotaScope`: `DEVELOPER` means the shared budget (the developer token for Google Ads, the Google Cloud project for YouTube Analytics; every account on Zernio is affected and there is nothing to change on your side), `ACCOUNT` means your own ad account (Google Ads only). A Meta 429 carries neither field.  A Zernio Google Ads burst-limit 429 carries `budgetScope` instead, and never `quotaExhausted`: these are Zernio's own limits, applied before the call reaches Google, and both clear within a minute. `account` is the limit of 15 requests per minute per connected Google Ads account; `user` is the ceiling of 120 requests per minute per Zernio user across all their Google Ads accounts. Both are separate axes from `quotaScope`, not the same pool named twice.  A failed Meta ad create (`POST /v1/ads/create`, `POST /v1/ads/boost`, `POST /v1/ads/ctwa`) carries `stage`, `adAccountId` and `createdObjects`: where it failed, on which ad account, and every object this request had already created with what cleanup did to it. `left_behind` objects still exist on the ad account (Meta refused the delete, typically on a held account, or the delete hit a network error), so delete them yourself or reuse them. `unconfirmedWrite` is set when Meta answered a create with a 5xx or dropped the connection and Zernio could not confirm whether the object exists: check that parent before creating it again.  When Meta refuses a write because the ad account's status is ineligible to manage ads (Meta subcode 2490592 or 4841021, on the write itself or on a cleanup delete), any Meta ads write (create, boost, CTWA, campaign / ad set / ad updates and status changes) answers 422 `ad_account_unusable`. The message names the ad account when known, links Meta's fix (https://www.facebook.com/business/help/422289316306981), lists the objects left behind and ends with Meta's original error, which also stays verbatim in `platformError`. Meta often reports the first failure under an unrelated code (e.g. 1487194 on the creative), so branch on `code`, not on `platformError`.  When Meta refuses a write because the Facebook user behind the connection's token lacks the Advertise permission on the ad account (Meta subcode 2490585, 2490591 or 4841020 on the write, or a code 200 refusal such as 1487194 whose cleanup deletes Meta refused with 2490591 or 4841020), any Meta ads write answers 403 `insufficient_permissions`. Meta may still accept the campaign and ad set and refuse only the ad. The message names the ad account, asks for the Advertise or Manage permission on it (or a token granted `ads_management`, by reconnecting), lists the objects left behind and ends with Meta's `error_user_title`, `error_user_msg` and subcode; the raw error stays in `platformError`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | [**StageEnum**](#StageEnum) | Meta ad create failures only. The step that failed: &#x60;media&#x60; (image/video download or upload), &#x60;campaign&#x60;, &#x60;adset&#x60;, &#x60;creative&#x60;, &#x60;ad&#x60; (the ad POST itself, where Meta&#39;s code 31 / 3858385 hold and 100 / 1359188 payment rejections land), &#x60;activation&#x60; (switching the created objects on), or &#x60;other&#x60; (a read or check before any write). |  [optional] |
|**adAccountId** | **String** | Meta ad create failures only. The ad account the request wrote to (&#x60;act_...&#x60;). |  [optional] |
|**createdObjects** | [**List&lt;ErrorResponseDetailsCreatedObjectsInner&gt;**](ErrorResponseDetailsCreatedObjectsInner.md) | Meta ad create failures only. Every object this request created before failing, in creation order. Objects you referenced (an existing campaign, ad set, creative or video) are never listed and never deleted. |  [optional] |
|**unconfirmedWrite** | [**ErrorResponseDetailsUnconfirmedWrite**](ErrorResponseDetailsUnconfirmedWrite.md) |  |  [optional] |
|**quotaExhausted** | **Boolean** | Google Ads and YouTube Analytics 429 only. True when the upstream Google quota is spent rather than a Zernio limit. |  [optional] |
|**quotaScope** | [**QuotaScopeEnum**](#QuotaScopeEnum) | Google Ads and YouTube Analytics 429 only, when the scope is known. DEVELOPER is the shared budget (the developer token for Google Ads, the Google Cloud project for YouTube Analytics); ACCOUNT is your ad account (Google Ads only). |  [optional] |
|**budgetScope** | [**BudgetScopeEnum**](#BudgetScopeEnum) | Zernio Google Ads burst-limit 429 only (never set alongside &#x60;quotaExhausted&#x60;). &#x60;account&#x60; is the limit of 15 requests per minute per connected Google Ads account; &#x60;user&#x60; is the ceiling of 120 requests per minute per Zernio user across all their Google Ads accounts. Both clear within a minute. |  [optional] |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| MEDIA | &quot;media&quot; |
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |
| CREATIVE | &quot;creative&quot; |
| AD | &quot;ad&quot; |
| ACTIVATION | &quot;activation&quot; |
| OTHER | &quot;other&quot; |



## Enum: QuotaScopeEnum

| Name | Value |
|---- | -----|
| DEVELOPER | &quot;DEVELOPER&quot; |
| ACCOUNT | &quot;ACCOUNT&quot; |



## Enum: BudgetScopeEnum

| Name | Value |
|---- | -----|
| ACCOUNT | &quot;account&quot; |
| USER | &quot;user&quot; |



