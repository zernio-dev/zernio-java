

# AutomationRunResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;unknown&#x60; when the platform never answered, so the outcome is not known. |  |
|**reason** | **String** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NOTIFY_SEND | &quot;notify.send&quot; |
| ADS_BOOST_POST | &quot;ads.boost_post&quot; |
| MESSAGES_SEND | &quot;messages.send&quot; |
| WORKFLOWS_START | &quot;workflows.start&quot; |
| SEQUENCES_ENROLL | &quot;sequences.enroll&quot; |
| WEBHOOK_CALL | &quot;webhook.call&quot; |
| CONTACTS_TAG | &quot;contacts.tag&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPLIED | &quot;applied&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |
| UNKNOWN | &quot;unknown&quot; |



