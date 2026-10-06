

# TriggerApiCallWorkflowRequest

Exactly one of `conversationId`, `contactId` or `to`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationId** | **String** | A conversation on the workflow&#39;s account |  [optional] |
|**contactId** | **String** | A contact with a conversation on the workflow&#39;s account |  [optional] |
|**to** | **String** | Recipient phone in E.164 (WhatsApp workflows only) |  [optional] |
|**variables** | **Map&lt;String, Object&gt;** | Seed variables, merged over the standard run variables |  [optional] |



