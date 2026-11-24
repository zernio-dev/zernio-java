

# ListInboxReviews200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountsQueried** | **Integer** |  |  [optional] |
|**accountsFailed** | **Integer** |  |  [optional] |
|**failedAccounts** | [**List&lt;ListInboxConversations200ResponseMetaFailedAccountsInner&gt;**](ListInboxConversations200ResponseMetaFailedAccountsInner.md) |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**accountsSkipped** | [**List&lt;ListInboxConversations200ResponseMetaAccountsSkippedInner&gt;**](ListInboxConversations200ResponseMetaAccountsSkippedInner.md) | Connected accounts that were not queried: their platform does not support this feature, or the account is not enabled for it |  [optional] |
|**truncatedAccounts** | [**List&lt;ListInboxConversations200ResponseMetaAccountsSkippedInner&gt;**](ListInboxConversations200ResponseMetaAccountsSkippedInner.md) | Accounts whose listing hit the read budget with pages left: their reviews in data, and the Google Business Profile summary, are partial. Empty when every account was read in full. |  [optional] |



