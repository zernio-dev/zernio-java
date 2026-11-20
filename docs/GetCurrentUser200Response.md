

# GetCurrentUser200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**email** | **String** | Only returned to a dashboard session. Omitted for API keys. |  [optional] |
|**image** | **String** |  |  [optional] |
|**role** | **String** | One of owner, admin, billing_admin, member or viewer. Always owner when isRoot is true. |  [optional] |
|**isRoot** | **Boolean** | True when the user owns the account, false when they were invited to it. |  [optional] |
|**invitedBy** | **String** | Id of the user who invited this user. Null when isRoot is true. |  [optional] |
|**invitedToProfile** | **String** | Only present when isRoot is false. |  [optional] |
|**invitedToProfiles** | **List&lt;String&gt;** | Ids of the profiles an invited user is limited to. Empty means every profile. Only present when isRoot is false. |  [optional] |
|**disabledResourceGroups** | **List&lt;String&gt;** | Resource groups turned off for an invited user. Null or empty means none. Only present when isRoot is false. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**lastLoginAt** | **OffsetDateTime** | Last sign-in, stamped at most once an hour. Null when no sign-in has been recorded. |  [optional] |
|**workspaceId** | **String** | Id of the workspace the credential acts in. Null when the user has no workspace yet. |  [optional] |
|**workspaceName** | **String** | Name of that workspace. Null when workspaceId is null. |  [optional] |



