

# RcsAgent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**accountId** | **String** | The rcs inbox account, created once the agent exists with the carriers. |  [optional] |
|**country** | **String** | Launch market (ISO 3166-1 alpha-2). US agents run through the carriers automatically; other markets are filed by our team and skip the testing and launch_review steps (send the launch request while the agent is still in review). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**useCase** | [**UseCaseEnum**](#UseCaseEnum) |  |  [optional] |
|**profile** | [**RcsAgentProfile**](RcsAgentProfile.md) |  |  [optional] |
|**brand** | [**RcsBrand**](RcsBrand.md) |  |  [optional] |
|**launchRequest** | [**RcsLaunchRequest**](RcsLaunchRequest.md) |  |  [optional] |
|**carrierApprovals** | [**List&lt;RcsCarrierApproval&gt;**](RcsCarrierApproval.md) |  |  [optional] |
|**testDevices** | [**List&lt;RcsTestDevice&gt;**](RcsTestDevice.md) |  |  [optional] |
|**smsFallbackFrom** | **String** |  |  [optional] |
|**reviewNote** | **String** | Our note while status is changes_requested. |  [optional] |
|**declineReason** | **String** |  |  [optional] |
|**requestedAt** | **OffsetDateTime** |  |  [optional] |
|**submittedAt** | **OffsetDateTime** |  |  [optional] |
|**liveAt** | **OffsetDateTime** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| CHANGES_REQUESTED | &quot;changes_requested&quot; |
| BRAND_VETTING | &quot;brand_vetting&quot; |
| AGENT_REVIEW | &quot;agent_review&quot; |
| TESTING | &quot;testing&quot; |
| LAUNCH_REVIEW | &quot;launch_review&quot; |
| LAUNCHING | &quot;launching&quot; |
| LIVE | &quot;live&quot; |
| REJECTED | &quot;rejected&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



## Enum: UseCaseEnum

| Name | Value |
|---- | -----|
| MULTI_USE | &quot;MULTI_USE&quot; |
| PROMOTIONAL | &quot;PROMOTIONAL&quot; |
| TRANSACTIONAL | &quot;TRANSACTIONAL&quot; |
| OTP | &quot;OTP&quot; |



