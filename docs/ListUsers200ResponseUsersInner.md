

# ListUsers200ResponseUsersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**role** | **String** |  |  [optional] |
|**isRoot** | **Boolean** |  |  [optional] |
|**profileAccess** | **List&lt;String&gt;** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**lastLoginAt** | **OffsetDateTime** | Last sign-in, stamped at most once an hour, so it is accurate to within an hour rather than to the exact session. Omitted for members with no recorded sign-in since the field shipped, which does not mean they never signed in. |  [optional] |



