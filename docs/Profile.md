

# Profile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**color** | **String** |  |  [optional] |
|**timezone** | **String** | IANA timezone new posts on this profile use when the request names no &#x60;timezone&#x60;. Null means UTC. |  [optional] |
|**externalId** | **String** | Your own identifier for this profile, set on create or update. Null when none is set. |  [optional] |
|**isDefault** | **Boolean** |  |  [optional] |
|**isOverLimit** | **Boolean** | Only present when includeOverLimit&#x3D;true. Indicates if this profile exceeds the plan limit. |  [optional] |
|**accountCount** | **Integer** | In the profile list. Connected accounts on the profile, including ones that need reconnecting; phone and SMS number internals and posting accounts hidden by an ads connect are not counted. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



