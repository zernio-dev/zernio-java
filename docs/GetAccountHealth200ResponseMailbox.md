

# GetAccountHealth200ResponseMailbox

Microsoft only: present while the login has no Exchange Online mailbox (no Exchange license, inactive, soft-deleted or on-premises). Mail and calendar requests then answer 412 `mailbox_not_available`; files are not affected. Absent when the mailbox works. `status` is also `warning`, with the reason in `issues`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**detectedAt** | **OffsetDateTime** | When Microsoft last answered that the login has no mailbox. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| NO_MAILBOX | &quot;no_mailbox&quot; |



