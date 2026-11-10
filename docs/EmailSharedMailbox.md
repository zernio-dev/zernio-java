

# EmailSharedMailbox

An Outlook shared mailbox added under a connected Microsoft account. It is an account of its own, so every `/v1/email` endpoint takes its `accountId`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Pass it as &#x60;accountId&#x60; to any /v1/email endpoint. |  [optional] |
|**address** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**parentAccountId** | **String** | The Outlook account whose access opens this mailbox. |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**addedAt** | **OffsetDateTime** |  |  [optional] |



