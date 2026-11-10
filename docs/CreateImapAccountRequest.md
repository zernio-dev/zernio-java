

# CreateImapAccountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**email** | **String** |  |  |
|**name** | **String** | Shown to people the mailbox emails. |  [optional] |
|**password** | **String** | Shortcut for imap.password. |  [optional] |
|**imap** | [**CreateImapAccountRequestImap**](CreateImapAccountRequestImap.md) |  |  [optional] |
|**smtp** | [**CreateImapAccountRequestSmtp**](CreateImapAccountRequestSmtp.md) |  |  [optional] |
|**identities** | [**List&lt;CreateImapAccountRequestIdentitiesInner&gt;**](CreateImapAccountRequestIdentitiesInner.md) | Other addresses this mailbox sends as. |  [optional] |
|**dryRun** | **Boolean** | Run every check and store nothing, for live validation in your own form. |  [optional] |
|**allowSelfSignedCertificate** | **Boolean** | On-premise servers only: accept a certificate that cannot be verified. The hosted page never offers it. |  [optional] |
|**reconnectAccountId** | **String** | Reconnect this account in place with a new password; the stored servers are reused. |  [optional] |



