

# SearchInboxConversations200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountsQueried** | **Integer** |  |  [optional] |
|**accountsFailed** | **Integer** |  |  [optional] |
|**failedAccounts** | [**List&lt;SearchInboxConversations200ResponseMetaFailedAccountsInner&gt;**](SearchInboxConversations200ResponseMetaFailedAccountsInner.md) |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**contentNotRetained** | **Boolean** | True when a searched account belongs to a team that does not retain content. Message text is not searchable there, only identifiers match. |  [optional] |
|**accountsSkipped** | [**List&lt;ListInboxConversations200ResponseMetaAccountsSkippedInner&gt;**](ListInboxConversations200ResponseMetaAccountsSkippedInner.md) | Connected messaging accounts that cannot be searched (live-fetched platforms) |  [optional] |



