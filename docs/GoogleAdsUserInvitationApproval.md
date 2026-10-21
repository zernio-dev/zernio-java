

# GoogleAdsUserInvitationApproval


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**multiPartyAuthReviewId** | **String** | Pass to DELETE /v1/ads/accounts/user-invitations/pending-approvals to withdraw the request. |  [optional] |
|**emailAddress** | **String** | Invited email address. |  [optional] |
|**accessRole** | [**AccessRoleEnum**](#AccessRoleEnum) |  |  [optional] |
|**requestUserEmail** | **String** | Google user who sent the invitation. Only this user can withdraw it. |  [optional] |
|**createdAt** | **String** | Google&#39;s creation time, yyyy-MM-dd HH:mm:ss.ssssss in the account&#39;s time zone. |  [optional] |



## Enum: AccessRoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;ADMIN&quot; |
| STANDARD | &quot;STANDARD&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| EMAIL_ONLY | &quot;EMAIL_ONLY&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



