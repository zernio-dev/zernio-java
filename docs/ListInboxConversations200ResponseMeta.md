

# ListInboxConversations200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountsQueried** | **Integer** |  |  [optional] |
|**accountsFailed** | **Integer** |  |  [optional] |
|**failedAccounts** | [**List&lt;ListInboxConversations200ResponseMetaFailedAccountsInner&gt;**](ListInboxConversations200ResponseMetaFailedAccountsInner.md) |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**accountsSkipped** | [**List&lt;ListInboxConversations200ResponseMetaAccountsSkippedInner&gt;**](ListInboxConversations200ResponseMetaAccountsSkippedInner.md) | Connected accounts that were not queried: their platform does not support this feature, or the account is not enabled for it |  [optional] |



