

# WebhookPayloadEmailBouncedBounce


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recipient** | **String** | The address that refused the mail. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;hard&#x60;: 5.x.x, the address does not take mail. &#x60;soft&#x60;: 4.x.x, a temporary refusal the sending server gave up on. &#x60;undetermined&#x60;: the report gave no status. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional] |
|**status** | **String** | RFC 3463 enhanced status, such as 5.1.1. |  [optional] |
|**smtpCode** | **Integer** | The SMTP reply code, such as 550. Always a number. |  [optional] |
|**diagnostic** | **String** | The receiving server&#39;s answer. |  [optional] |
|**recommendedAction** | [**RecommendedActionEnum**](#RecommendedActionEnum) | &#x60;remove&#x60; only for an address that does not take mail. Sender-side refusals (authentication, blocklists, spam filters) are &#x60;fix_configuration&#x60; or &#x60;review&#x60;, never &#x60;remove&#x60;. |  [optional] |
|**reportingMta** | **String** |  |  [optional] |
|**detection** | [**DetectionEnum**](#DetectionEnum) | &#x60;dsn&#x60;: a standard delivery report with the bounced Message-ID. &#x60;ndr&#x60;: a non-standard report read from its headers and text. |  [optional] |
|**bounceMessageId** | **String** | Provider id of the bounce report in the mailbox. |  [optional] |
|**bouncedAt** | **OffsetDateTime** | When the report arrived in the mailbox. |  [optional] |
|**detectedAt** | **OffsetDateTime** | When Zernio read it. Reports can arrive minutes to days after the send. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HARD | &quot;hard&quot; |
| SOFT | &quot;soft&quot; |
| UNDETERMINED | &quot;undetermined&quot; |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| USER_UNKNOWN | &quot;user_unknown&quot; |
| MAILBOX_FULL | &quot;mailbox_full&quot; |
| DOMAIN_NOT_FOUND | &quot;domain_not_found&quot; |
| POLICY_BLOCKED | &quot;policy_blocked&quot; |
| SPAM_BLOCKED | &quot;spam_blocked&quot; |
| BLOCKLISTED | &quot;blocklisted&quot; |
| MESSAGE_TOO_LARGE | &quot;message_too_large&quot; |
| CONTENT_REJECTED | &quot;content_rejected&quot; |
| AUTH_FAILURE | &quot;auth_failure&quot; |
| RATE_LIMITED | &quot;rate_limited&quot; |
| OTHER | &quot;other&quot; |



## Enum: RecommendedActionEnum

| Name | Value |
|---- | -----|
| REMOVE | &quot;remove&quot; |
| RETRY | &quot;retry&quot; |
| REVIEW | &quot;review&quot; |
| FIX_CONFIGURATION | &quot;fix_configuration&quot; |



## Enum: DetectionEnum

| Name | Value |
|---- | -----|
| DSN | &quot;dsn&quot; |
| NDR | &quot;ndr&quot; |



