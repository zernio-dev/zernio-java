

# TriggerWorkflowRequest

Provide either `to` (WhatsApp phone) or `conversationId`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**to** | **String** | Recipient phone (WhatsApp only) |  [optional] |
|**conversationId** | **String** | An existing conversation to run in (required for non-WhatsApp workflows) |  [optional] |
|**text** | **String** | Simulated inbound text, seeded as the run&#39;s lastMessage variable |  [optional] |



