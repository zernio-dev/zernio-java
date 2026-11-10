

# ScheduledEmail

An email sent with `scheduledFor`. `status` moves scheduled, sending, then sent or failed; a cancelled one never leaves.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The &#x60;scheduleId&#x60;. |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** |  |  [optional] |
|**to** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) |  |  [optional] |
|**subject** | **String** | Empty on a reply that keeps the thread subject. &#x60;null&#x60; once the send finishes under zero content retention. |  [optional] |
|**contentNotRetained** | **Boolean** | Present and &#x60;true&#x60; when the email content was dropped under [zero content retention](/security/zero-content-retention). |  [optional] |
|**replyToMessageId** | **String** | Set when scheduled through the reply route. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**sentAt** | **OffsetDateTime** |  |  [optional] |
|**sentMessageId** | **String** | Provider id of the sent message once &#x60;status&#x60; is sent. |  [optional] |
|**sentThreadId** | **String** |  |  [optional] |
|**error** | **String** | Why a failed send did not leave. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SCHEDULED | &quot;scheduled&quot; |
| SENDING | &quot;sending&quot; |
| SENT | &quot;sent&quot; |
| FAILED | &quot;failed&quot; |
| CANCELLED | &quot;cancelled&quot; |



