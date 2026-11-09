

# ListAdsInstagramAccounts200ResponseAccountsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**igUserId** | **String** | Instagram identity ID. |  |
|**username** | **String** | Instagram username; empty when Meta does not expose it. |  |
|**profilePictureUrl** | **String** | Profile picture URL when available. |  [optional] |
|**isPageBacked** | **Boolean** | Whether this is a Page-backed Instagram identity. |  |
|**source** | [**SourceEnum**](#SourceEnum) | Discovery source; Page linkage also uses page_backed. business_partner is a partner asset shared with the ad account&#39;s business; promote_pages is linked to a Page the ad account promotes. |  |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| AD_ACCOUNT | &quot;ad_account&quot; |
| PAGE_BACKED | &quot;page_backed&quot; |
| BUSINESS | &quot;business&quot; |
| BUSINESS_PARTNER | &quot;business_partner&quot; |
| PROMOTE_PAGES | &quot;promote_pages&quot; |



