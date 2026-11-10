

# EmailSendAs

An address the mailbox can send from: listed by the provider, or declared with `POST /v1/email/send-as`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** |  |  [optional] |
|**name** | **String** | Display name used when &#x60;fromName&#x60; is not given. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;primary&#x60; is the mailbox&#39;s own address, &#x60;alias&#x60; a provider alias, &#x60;shared&#x60; a declared address (shared mailbox, delegate or alias). |  [optional] |
|**verificationStatus** | [**VerificationStatusEnum**](#VerificationStatusEnum) | &#x60;pending&#x60;: Gmail has not verified the alias, so sends from it are refused. &#x60;unverified&#x60;: declared and not sent from yet; it becomes &#x60;accepted&#x60; after its first send. |  [optional] |
|**isDefault** | **Boolean** | The address the provider picks by default. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) |  |  [optional] |
|**replyTo** | **String** | Gmail alias reply-to address, if set. |  [optional] |
|**signature** | [**EmailSendAsSignature**](EmailSendAsSignature.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;primary&quot; |
| ALIAS | &quot;alias&quot; |
| SHARED | &quot;shared&quot; |



## Enum: VerificationStatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| PENDING | &quot;pending&quot; |
| UNVERIFIED | &quot;unverified&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PROVIDER | &quot;provider&quot; |
| DECLARED | &quot;declared&quot; |



