

# CampaignParticipant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**campaignId** | **String** |  |  |
|**creator** | [**CampaignParticipantCreator**](CampaignParticipantCreator.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**joinedAt** | **OffsetDateTime** |  |  |
|**accounts** | [**List&lt;CampaignParticipantAccountsInner&gt;**](CampaignParticipantAccountsInner.md) | Social accounts the creator connected, verified once Zernio confirmed the creator owns them. |  |
|**balances** | [**CampaignParticipantBalances**](CampaignParticipantBalances.md) |  |  |
|**flags** | [**List&lt;CampaignParticipantFlagsInner&gt;**](CampaignParticipantFlagsInner.md) |  |  |
|**submissionCounts** | [**CampaignSubmissionCounts**](CampaignSubmissionCounts.md) |  |  |
|**payout** | [**CampaignParticipantPayout**](CampaignParticipantPayout.md) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVITED | &quot;invited&quot; |
| ACTIVE | &quot;active&quot; |
| SUSPENDED | &quot;suspended&quot; |
| REMOVED | &quot;removed&quot; |



