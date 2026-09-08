

# InboxWebhookAccount

The account context included in inbox webhook payloads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Account ID |  |
|**accountId** | **String** | Account ID (same value as id). Canonical field so consumers can filter every webhook event on one field (e.g. route staging vs production by account). id is kept for backward compatibility. |  [optional] |
|**profileId** | **String** | Zernio profile ID this account belongs to. Use it to route or filter inbox webhooks by profile. This is the profile ID only, not its name (resolve the name via the API with this ID). Optional; omitted on the shared WhatsApp sandbox account and when the account has no resolvable profile. |  [optional] |
|**platform** | **String** |  |  |
|**username** | **String** |  |  |
|**displayName** | **String** |  |  [optional] |



