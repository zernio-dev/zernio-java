

# WebhookPayloadReactionReactionSender

Whoever added or removed the reaction. Usually the participant, but on WhatsApp, Slack, Instagram and Facebook Messenger it is the business own platform id when the business reacted from the native app or via the reactions API: compare it with conversation.participantId.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**contactId** | **String** | Zernio CRM Contact id for this sender, when one exists. |  [optional] |
|**name** | **String** |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**picture** | **String** |  |  [optional] |
|**phoneNumber** | **String** | WhatsApp only. Sender&#39;s phone number in E.164 format (with leading &#x60;+&#x60;), when available. |  [optional] |



