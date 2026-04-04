

# CreateInboxConversationRequest1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The social account ID to send from |  |
|**participantId** | **String** | Twitter numeric user ID of the recipient |  [optional] |
|**participantUsername** | **String** | Twitter username (with or without @) of the recipient |  [optional] |
|**message** | **String** | Text content of the message |  [optional] |
|**attachment** | **File** | Media attachment (image or video). One attachment per message. |  [optional] |
|**skipDmCheck** | [**SkipDmCheckEnum**](#SkipDmCheckEnum) | Skip the DM eligibility check |  [optional] |



## Enum: SkipDmCheckEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |



