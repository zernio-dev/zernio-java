

# RespondToPhoneNumberReviewer200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;resubmitted&#x60; when corrections were submitted, &#x60;replied&#x60; when it was message-only. |  [optional] |
|**posted** | **Boolean** | Whether a message/attachments were posted to the reviewer. |  [optional] |
|**phoneNumber** | [**RemediatePhoneNumber200ResponsePhoneNumber**](RemediatePhoneNumber200ResponsePhoneNumber.md) |  |  [optional] |
|**siblingsResubmitted** | **Integer** | Other numbers on the same registration the correction fanned out to. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RESUBMITTED | &quot;resubmitted&quot; |
| REPLIED | &quot;replied&quot; |



