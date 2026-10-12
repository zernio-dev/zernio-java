

# WebhookPayloadSequenceEnrollment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Event id, the dedupe key. |  |
|**profiles** | [**List&lt;WebhookProfilesInner&gt;**](WebhookProfilesInner.md) | The profiles this event belongs to, each with the externalId you set on it (null when none is set). Present on every event tied to a profile and absent on events that belong to none. Events spanning several profiles (a post published to accounts of different profiles) list each once. Use it to route the event to your tenant without storing Zernio profile ids. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**sequence** | [**UpdateFacebookPage200ResponseSelectedPage**](UpdateFacebookPage200ResponseSelectedPage.md) |  |  |
|**contact** | [**WebhookPayloadContactTagContact**](WebhookPayloadContactTagContact.md) |  |  |
|**enrollment** | [**CreateTestLead200ResponseTestLead**](CreateTestLead200ResponseTestLead.md) |  |  |
|**exitReason** | [**ExitReasonEnum**](#ExitReasonEnum) | sequence.exited only. completed: the last step was sent; replied: the contact replied and the sequence exits on reply; manual: unenrolled through the API; failed: the step kept failing to send; unsubscribed: the contact opted out. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| SEQUENCE_ENROLLED | &quot;sequence.enrolled&quot; |
| SEQUENCE_EXITED | &quot;sequence.exited&quot; |



## Enum: ExitReasonEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| REPLIED | &quot;replied&quot; |
| MANUAL | &quot;manual&quot; |
| FAILED | &quot;failed&quot; |
| UNSUBSCRIBED | &quot;unsubscribed&quot; |



