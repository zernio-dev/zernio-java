

# AssignAdAccountUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id used to resolve the Meta token. |  |
|**adAccountId** | **String** | Meta ad account id (act_&lt;n&gt;). |  |
|**userId** | **String** | Business-scoped user id from GET /v1/ads/businesses/users. |  |
|**tasks** | [**List&lt;TasksEnum&gt;**](#List&lt;TasksEnum&gt;) |  |  |



## Enum: List&lt;TasksEnum&gt;

| Name | Value |
|---- | -----|
| MANAGE | &quot;MANAGE&quot; |
| ADVERTISE | &quot;ADVERTISE&quot; |
| ANALYZE | &quot;ANALYZE&quot; |
| DRAFT | &quot;DRAFT&quot; |



