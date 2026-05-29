

# WhatsAppSandboxSession

A per-user activation session against the shared WhatsApp sandbox number. Transitions `pending → active` when the inbound webhook receives a reply from the matching phone (the reply itself proves ownership). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Session id. Use this to revoke via DELETE. |  |
|**phoneE164** | **String** | Digits-only E.164 form (no +, spaces, or dashes). |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;pending&#x60; until the phone replies to the activation template, then &#x60;active&#x60;. Expired sessions are pruned by TTL and never appear in list responses.  |  |
|**expiresAt** | **OffsetDateTime** | UTC timestamp at which the session becomes invalid. Pending sessions get a 24h window; activated sessions get 7 days.  |  |
|**activatedAt** | **OffsetDateTime** | When the session transitioned &#x60;pending → active&#x60;, or null. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACTIVE | &quot;active&quot; |



