

# EmailSendAs

An address the mailbox can send from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**replyTo** | **String** | Gmail alias reply-to address, if set. |  [optional] |
|**isPrimary** | **Boolean** | The mailbox&#39;s own address. |  [optional] |
|**isDefault** | **Boolean** | The address Gmail picks by default in its compose window. |  [optional] |
|**verified** | **Boolean** | Gmail sends from an alias only once it is verified. Always &#x60;true&#x60; on Outlook. |  [optional] |
|**signature** | **String** | Signature html. Gmail only; always &#x60;null&#x60; on Outlook. |  [optional] |



