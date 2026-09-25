

# ErrorResponseDetails

Additional structured context (e.g. field-level validation errors), for example `privateReplyConsumed` on the private-reply endpoint's 400 when the comment's single reply is already spent.  On a Google Ads 429 it carries `quotaExhausted: true`, which marks the failure as Google's own ads quota rather than a Zernio rate limit, so you can keep calling other platforms instead of backing off everywhere. When Google names the scope it also carries `quotaScope`: `DEVELOPER` means the shared developer-token budget (every Google account is affected and there is nothing to change on your side), `ACCOUNT` means your own ad account. A Meta 429 carries neither field.  A Zernio Google Ads budget 429 carries `budgetScope` instead, and never `quotaExhausted`: these are Zernio's own limits, applied before the call reaches Google. `user` is your own burst or daily allowance, so the work is yours to reschedule; `platform` is the fleet-wide daily budget shared with every other customer, so only waiting for the reset clears it. The two scopes are separate axes from `quotaScope`, not the same pool named twice.  A failed Meta ad create (`POST /v1/ads/create`, `POST /v1/ads/boost`, `POST /v1/ads/ctwa`) carries `stage`, `adAccountId` and `createdObjects`: where it failed, on which ad account, and every object this request had already created with what cleanup did to it. `left_behind` objects still exist on the ad account (Meta refused the delete, typically on a held account), so delete them yourself or reuse them. `unconfirmedWrite` is set when Meta answered a create with a 5xx or dropped the connection and Zernio could not confirm whether the object exists: check that parent before creating it again. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | [**StageEnum**](#StageEnum) | Meta ad create failures only. The step that failed: &#x60;media&#x60; (image/video download or upload), &#x60;campaign&#x60;, &#x60;adset&#x60;, &#x60;creative&#x60;, &#x60;ad&#x60; (the ad POST itself, where Meta&#39;s code 31 / 3858385 hold and 100 / 1359188 payment rejections land), &#x60;activation&#x60; (switching the created objects on), or &#x60;other&#x60; (a read or check before any write). |  [optional] |
|**adAccountId** | **String** | Meta ad create failures only. The ad account the request wrote to (&#x60;act_...&#x60;). |  [optional] |
|**createdObjects** | [**List&lt;ErrorResponseDetailsCreatedObjectsInner&gt;**](ErrorResponseDetailsCreatedObjectsInner.md) | Meta ad create failures only. Every object this request created before failing, in creation order. Objects you referenced (an existing campaign, ad set, creative or video) are never listed and never deleted. |  [optional] |
|**unconfirmedWrite** | [**ErrorResponseDetailsUnconfirmedWrite**](ErrorResponseDetailsUnconfirmedWrite.md) |  |  [optional] |
|**quotaExhausted** | **Boolean** | Google Ads 429 only. True when the upstream Google Ads quota is spent rather than a Zernio limit. |  [optional] |
|**quotaScope** | [**QuotaScopeEnum**](#QuotaScopeEnum) | Google Ads 429 only, when Google names the scope. DEVELOPER is the shared developer-token budget; ACCOUNT is your ad account. |  [optional] |
|**budgetScope** | [**BudgetScopeEnum**](#BudgetScopeEnum) | Zernio Google Ads operations-budget 429 only (never set alongside &#x60;quotaExhausted&#x60;). &#x60;user&#x60; is your own burst/daily allowance; &#x60;platform&#x60; is the fleet-wide daily budget shared across customers. |  [optional] |



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
| USER | &quot;user&quot; |
| PLATFORM | &quot;platform&quot; |



