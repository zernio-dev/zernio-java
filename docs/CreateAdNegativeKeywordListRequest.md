

# CreateAdNegativeKeywordListRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id. |  |
|**customerId** | **String** | Connected Google Ads customer id, without dashes. Required when the connection has multiple customers. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Optional courtesy field. The resolved account or campaign determines support; other platforms return 501. |  [optional] |
|**name** | **String** | Nonempty list name, trimmed before use. |  |
|**keywords** | [**List&lt;KeywordEntry&gt;**](KeywordEntry.md) | Full desired keyword set. Bare strings use broad match. Send [] to clear the list. |  [optional] |



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



