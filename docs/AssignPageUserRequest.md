

# AssignPageUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id used to resolve the Meta token. |  |
|**pageId** | **String** | Facebook Page id. |  |
|**businessId** | **String** | Business portfolio the user belongs to. |  |
|**userId** | **String** | Business-scoped user id from GET /v1/ads/businesses/users. |  |
|**tasks** | [**List&lt;TasksEnum&gt;**](#List&lt;TasksEnum&gt;) |  |  |



## Enum: List&lt;TasksEnum&gt;

| Name | Value |
|---- | -----|
| MANAGE | &quot;MANAGE&quot; |
| CREATE_CONTENT | &quot;CREATE_CONTENT&quot; |
| MODERATE | &quot;MODERATE&quot; |
| MESSAGING | &quot;MESSAGING&quot; |
| ADVERTISE | &quot;ADVERTISE&quot; |
| ANALYZE | &quot;ANALYZE&quot; |



