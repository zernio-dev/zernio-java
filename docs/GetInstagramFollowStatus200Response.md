

# GetInstagramFollowStatus200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userId** | **String** |  |  |
|**accountId** | **String** |  |  |
|**isFollower** | **Boolean** | The user follows this account. Null &#x3D; unknown, never \&quot;no\&quot;. |  |
|**isFollowedByAccount** | **Boolean** | This account follows the user. |  [optional] |
|**followerCount** | **Integer** |  |  [optional] |
|**isVerified** | **Boolean** |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**unavailableReason** | [**UnavailableReasonEnum**](#UnavailableReasonEnum) | Why the follow relationship could not be resolved. Null when it was. |  [optional] |



## Enum: UnavailableReasonEnum

| Name | Value |
|---- | -----|
| CONSENT_REQUIRED | &quot;consent_required&quot; |
| DM_ACCESS_DISABLED | &quot;dm_access_disabled&quot; |
| NOT_MESSAGEABLE | &quot;not_messageable&quot; |
| ERROR | &quot;error&quot; |



