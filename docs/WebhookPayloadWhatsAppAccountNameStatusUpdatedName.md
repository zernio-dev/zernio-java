

# WebhookPayloadWhatsAppAccountNameStatusUpdatedName


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | Normalized from Meta&#39;s &#x60;decision&#x60; (REJECTED -&gt; DECLINED, DEFERRED -&gt; PENDING_REVIEW; the review is still open on DEFERRED, not a rejection). |  |
|**requestedName** | **String** | The display name Meta reviewed. Null if Meta did not send one. |  |
|**rejectionReason** | **String** | Meta&#39;s free-form decline reason. Null on approval, or when Meta sends the literal string \&quot;NONE\&quot;. |  |
|**displayPhoneNumber** | **String** | The phone number this review is for, as Meta reported it. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;APPROVED&quot; |
| DECLINED | &quot;DECLINED&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |



