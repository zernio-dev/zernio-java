

# ListCampaignOrders200ResponseReferralsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**participantId** | **String** |  |  |
|**creatorName** | **String** |  |  |
|**creatorAvatarUrl** | **String** | The creator&#39;s profile picture. Same source as a participant&#39;s &#x60;creator.avatarUrl&#x60;. |  |
|**code** | **String** |  |  |
|**codeStatus** | [**CodeStatusEnum**](#CodeStatusEnum) | Null until the code is first created, when the creator opens their page. |  |
|**codeFailureReason** | **String** |  |  |
|**trackingUrl** | **String** |  |  |



## Enum: CodeStatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;ready&quot; |
| FAILED | &quot;failed&quot; |



