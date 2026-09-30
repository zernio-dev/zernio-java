

# WebhookPayloadWhatsAppAccountStatusUpdatedStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;active&#x60; only on a reinstatement (DISABLED_UPDATE with ban state REINSTATE). |  |
|**metaEvent** | **String** | Meta &#x60;account_update&#x60; event: ACCOUNT_RESTRICTION, ACCOUNT_VIOLATION, ACCOUNT_DELETED or DISABLED_UPDATE. |  |
|**reason** | **String** | Human-readable summary. Null on reinstatement. |  |
|**violationType** | **String** | ACCOUNT_VIOLATION only, for example SCAM, ADULT. |  |
|**restrictions** | [**List&lt;WebhookPayloadWhatsAppAccountStatusUpdatedStatusRestrictionsInner&gt;**](WebhookPayloadWhatsAppAccountStatusUpdatedStatusRestrictionsInner.md) | ACCOUNT_RESTRICTION only. Empty otherwise. |  |
|**banState** | **String** | DISABLED_UPDATE only (for example DISABLE, REINSTATE). |  |
|**banDate** | **String** | DISABLED_UPDATE only, as Meta sent it (for example \&quot;September 23, 2026\&quot;). |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RESTRICTED | &quot;restricted&quot; |
| ACTIVE | &quot;active&quot; |



