

# WebhookPayloadMessageSentMessageSender

**On this event the sender is your own business, not the person you are talking to.** `id` is the Zernio account id and `name`, `username` and `picture` are that connected account's own profile.  Do not read these to name or update a contact: doing so on an echo relabels the customer's record with your business name. The other party is `conversation.participantId` / `participantName` / `participantUsername`, which are populated in both directions. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The Zernio account id of the connected account that sent the message, not a contact id. |  |
|**contactId** | **String** | Always omitted on this event: the sender is the business, not a contact. Use conversation.contactId to join back to the CRM Contact. |  [optional] |
|**name** | **String** | Display name of your connected account. |  [optional] |
|**username** | **String** | Username of your connected account. |  [optional] |
|**picture** | **String** | Profile picture of your connected account. |  [optional] |



