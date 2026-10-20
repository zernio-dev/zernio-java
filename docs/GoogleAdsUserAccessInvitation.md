

# GoogleAdsUserAccessInvitation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**invitationId** | **String** |  |  [optional] |
|**emailAddress** | **String** |  |  [optional] |
|**accessRole** | [**AccessRoleEnum**](#AccessRoleEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**createdAt** | **String** | Google&#39;s creation time, yyyy-MM-dd HH:mm:ss.ssssss in the account&#39;s time zone. |  [optional] |



## Enum: AccessRoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;ADMIN&quot; |
| STANDARD | &quot;STANDARD&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| EMAIL_ONLY | &quot;EMAIL_ONLY&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| DECLINED | &quot;DECLINED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



