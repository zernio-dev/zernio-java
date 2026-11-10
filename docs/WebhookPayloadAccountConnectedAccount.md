

# WebhookPayloadAccountConnectedAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The account&#39;s unique identifier (same as used in /v1/accounts/{accountId}) |  |
|**profileId** | **String** | The profile&#39;s unique identifier this account belongs to |  |
|**platform** | **String** |  |  |
|**username** | **String** |  |  |
|**displayName** | **String** |  |  [optional] |
|**reconnected** | **Boolean** | Present and true when a reconnect restored an existing account in place, keeping its accountId. |  [optional] |
|**replacedAccountId** | **String** | The IMAP account this connection replaces, when a reconnected mailbox moved to Google or Microsoft. That account is retired at the same time, with account.disconnected and reasonCode replaced. |  [optional] |



