

# AssignAdAccountUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
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



