

# WebhookPayloadCallPermissionRequestPermission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | **String** | Consumer wa_id who replied |  [optional] |
|**response** | [**ResponseEnum**](#ResponseEnum) |  |  [optional] |
|**isPermanent** | **Boolean** |  |  [optional] |
|**expirationTimestamp** | **OffsetDateTime** | Present only when temporary |  [optional] |
|**responseSource** | **String** | Meta&#39;s response source, typically &#x60;user_action&#x60; |  [optional] |



## Enum: ResponseEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;accept&quot; |
| REJECT | &quot;reject&quot; |



