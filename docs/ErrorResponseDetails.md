

# ErrorResponseDetails

Additional structured context (e.g. field-level validation errors), for example `privateReplyConsumed` on the private-reply endpoint's 400 when the comment's single reply is already spent.  On a Google Ads 429 it carries `quotaExhausted: true`, which marks the failure as Google's own ads quota rather than a Zernio rate limit, so you can keep calling other platforms instead of backing off everywhere. When Google names the scope it also carries `quotaScope`: `DEVELOPER` means the shared developer-token budget (every Google account is affected and there is nothing to change on your side), `ACCOUNT` means your own ad account. A Meta 429 carries neither field. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**quotaExhausted** | **Boolean** | Google Ads 429 only. True when the upstream Google Ads quota is spent rather than a Zernio limit. |  [optional] |
|**quotaScope** | [**QuotaScopeEnum**](#QuotaScopeEnum) | Google Ads 429 only, when Google names the scope. DEVELOPER is the shared developer-token budget; ACCOUNT is your ad account. |  [optional] |



## Enum: QuotaScopeEnum

| Name | Value |
|---- | -----|
| DEVELOPER | &quot;DEVELOPER&quot; |
| ACCOUNT | &quot;ACCOUNT&quot; |



