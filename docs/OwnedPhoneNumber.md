

# OwnedPhoneNumber

A number you bought or ported. Null fields are omitted, except `socialAccountId` and `ownerAccountId`. Credentials stored for the number (such as the SIP digest password) are never returned; `sipAuthUsername` is the only SIP credential field exposed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**numberType** | **String** | For example local, mobile, national or toll_free. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**profileId** | [**OwnedPhoneNumberProfileId**](OwnedPhoneNumberProfileId.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**telnyxOrderId** | **String** | Present once the number order has been placed (i.e. the requirement group was approved). Absent while still in identity review. |  [optional] |
|**telnyxAdvancedOrderId** | **String** | Present on a pre-order: the carrier request placed for a number with no stock yet. |  [optional] |
|**registrantName** | **String** | For regulated numbers, who it&#39;s registered for (company or person), set from the submitted KYC. |  [optional] |
|**endUserFirstName** | **String** |  |  [optional] |
|**endUserLastName** | **String** |  |  [optional] |
|**regulatoryDeclineReason** | **String** | Reviewer rejection reason when status is regulatory_declined. |  [optional] |
|**regulatoryReviewComment** | **String** | The latest reviewer comment on a regulated number still in review. |  [optional] |
|**regulatoryInfoStatus** | **String** | &#x60;action_required&#x60; when the reviewer is waiting on you. |  [optional] |
|**onfidoVerificationUrl** | **String** | For regulated (Tier 3/4) numbers with an Onfido ID-verification step: the link to forward to the end user. Set once the order is placed; null otherwise. Poll this field after submitting KYC. |  [optional] |
|**verifyUrl** | **String** | Stable redirect to the live Onfido session. Prefer it over &#x60;onfidoVerificationUrl&#x60;, since it always resolves to a fresh session. |  [optional] |
|**onfidoOpened** | **Boolean** | True once the verify link has been opened at least once. |  [optional] |
|**metaPreverifiedId** | **String** |  |  [optional] |
|**metaVerificationStatus** | [**MetaVerificationStatusEnum**](#MetaVerificationStatusEnum) |  |  [optional] |
|**metaVerifiedAt** | **OffsetDateTime** |  |  [optional] |
|**metaVerificationExpiresAt** | **OffsetDateTime** |  |  [optional] |
|**socialAccountId** | **String** | The WhatsApp account the number is linked to; null when WhatsApp is not connected. |  [optional] |
|**ownerAccountId** | **String** | The telephony account that owns Calls and SMS on the number. |  [optional] |
|**sipTrunkId** | **String** | SIP trunk the number is attached to; null when not trunked. While attached, enabling Calls or WhatsApp calling, requesting WhatsApp verification, and releasing the number all return 409. |  [optional] |
|**whatsAppRequested** | **Boolean** | False for a standalone phone bought for Calls or SMS only. |  [optional] |
|**smsRequested** | **Boolean** |  |  [optional] |
|**provisionedAt** | **OffsetDateTime** |  |  [optional] |
|**activatedAt** | **OffsetDateTime** |  |  [optional] |
|**connectedAt** | **OffsetDateTime** |  |  [optional] |
|**suspendedAt** | **OffsetDateTime** |  |  [optional] |
|**releasedAt** | **OffsetDateTime** |  |  [optional] |
|**signupError** | **String** | Meta&#39;s Embedded Signup error from the last failed connect attempt (raw text, often localized). |  [optional] |
|**signupErrorAt** | **OffsetDateTime** |  |  [optional] |
|**signupErrorStep** | **String** |  |  [optional] |
|**monthlyCents** | **Integer** | What this number bills each month, in cents. Stamped when the number was bought, so an existing number keeps its price when the rate card changes. |  [optional] |
|**hostedByZernio** | **Boolean** | False for numbers you brought yourself (connected via Meta embedded signup). They live on your own carrier, so SMS/Calls can&#39;t be enabled on them. |  [optional] |
|**smsCapable** | **Boolean** | Whether the number can send SMS. Absent while unknown. |  [optional] |
|**mmsCapable** | **Boolean** | Whether the number can send MMS. Absent while unknown. |  [optional] |
|**domesticOnly** | **Boolean** | True when the number can only text numbers in its own country. Absent while unknown. |  [optional] |
|**smsRegistrationPending** | **Boolean** | True while a 10DLC registration covering this number is in review. |  [optional] |
|**smsSendApproved** | **Boolean** | True when outbound SMS is unlocked: an approved 10DLC covers the number, or the number is outside the US. |  [optional] |
|**smsBrandName** | **String** | Brand of the 10DLC registration covering the number. |  [optional] |
|**features** | [**OwnedPhoneNumberFeatures**](OwnedPhoneNumberFeatures.md) |  |  [optional] |
|**callingEnabled** | **Boolean** | Whether WhatsApp Business Calling is enabled on this number (manage via /v1/whatsapp/phone-numbers/{id}/calling). |  [optional] |
|**forwardTo** | **String** | WhatsApp calling forward destination. |  [optional] |
|**sipAuthUsername** | **String** | SIP digest username for a sip: forward destination. The password is never returned. |  [optional] |
|**callerIdVerifiedAt** | **OffsetDateTime** |  |  [optional] |
|**maxCallDurationSeconds** | **Integer** |  |  [optional] |
|**recordingEnabled** | **Boolean** |  |  [optional] |
|**transcriptionEnabled** | **Boolean** |  |  [optional] |
|**transcriptionLanguage** | [**TranscriptionLanguageEnum**](#TranscriptionLanguageEnum) |  |  [optional] |
|**callIconCountries** | **List&lt;String&gt;** |  |  [optional] |
|**forwardCallerId** | [**ForwardCallerIdEnum**](#ForwardCallerIdEnum) |  |  [optional] |
|**pstnVoiceEnabled** | **Boolean** | Whether Calls (PSTN voice) is on. |  [optional] |
|**pstnForwardTo** | **String** |  |  [optional] |
|**voicemailEnabled** | **Boolean** |  |  [optional] |
|**voicemailGreeting** | **String** |  |  [optional] |
|**businessHoursEnabled** | **Boolean** |  |  [optional] |
|**businessHoursTimezone** | **String** |  |  [optional] |
|**businessHours** | [**List&lt;EnableVoiceOnNumber200ResponseBusinessHoursInner&gt;**](EnableVoiceOnNumber200ResponseBusinessHoursInner.md) |  |  [optional] |
|**blockedCallers** | **List&lt;String&gt;** |  |  [optional] |
|**ivrEnabled** | **Boolean** |  |  [optional] |
|**ivrPrompt** | **String** |  |  [optional] |
|**ivrOptions** | [**List&lt;EnableVoiceOnNumber200ResponseIvrOptionsInner&gt;**](EnableVoiceOnNumber200ResponseIvrOptionsInner.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_PAYMENT | &quot;pending_payment&quot; |
| PENDING_REGULATORY | &quot;pending_regulatory&quot; |
| REGULATORY_DECLINED | &quot;regulatory_declined&quot; |
| PROVISIONING | &quot;provisioning&quot; |
| VERIFYING | &quot;verifying&quot; |
| ACTIVE | &quot;active&quot; |
| SUSPENDED | &quot;suspended&quot; |
| RELEASING | &quot;releasing&quot; |
| RELEASED | &quot;released&quot; |



## Enum: MetaVerificationStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| CODE_REQUESTED | &quot;code_requested&quot; |
| VERIFIED | &quot;verified&quot; |
| EXPIRED | &quot;expired&quot; |



## Enum: TranscriptionLanguageEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |



## Enum: ForwardCallerIdEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| CALLER | &quot;caller&quot; |



