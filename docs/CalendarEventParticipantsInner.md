

# CalendarEventParticipantsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** |  |  |
|**name** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**comment** | **String** |  |  [optional] |
|**optional** | **Boolean** | The guest may skip the event. |  [optional] |
|**resource** | **Boolean** | A room or equipment address. |  [optional] |
|**self** | **Boolean** | This guest is the connected mailbox. |  [optional] |
|**organizer** | **Boolean** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| DECLINED | &quot;declined&quot; |
| TENTATIVE | &quot;tentative&quot; |
| PENDING | &quot;pending&quot; |



