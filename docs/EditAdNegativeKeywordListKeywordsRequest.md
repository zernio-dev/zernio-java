

# EditAdNegativeKeywordListKeywordsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id. |  |
|**adAccountId** | **String** | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers. |  [optional] |
|**customerId** | **String** | Alias of adAccountId, kept for existing callers |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Optional courtesy field. The resolved account or campaign determines support; other platforms return 501. |  [optional] |
|**add** | [**List&lt;KeywordEntry&gt;**](KeywordEntry.md) | Keywords to add. Send at least one entry in add or remove. |  [optional] |
|**remove** | [**List&lt;KeywordEntry&gt;**](KeywordEntry.md) | Keywords to remove. Bare strings mean broad match. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| TIKTOK | &quot;tiktok&quot; |
| LINKEDIN | &quot;linkedin&quot; |
| PINTEREST | &quot;pinterest&quot; |
| GOOGLE | &quot;google&quot; |
| TWITTER | &quot;twitter&quot; |
| OPENAI | &quot;openai&quot; |
| REDDIT | &quot;reddit&quot; |



