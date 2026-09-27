

# UpdateAdAccountManagerLinkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**managerCustomerId** | **String** | Manager customer id, digits only. |  |
|**clientCustomerId** | **String** | Client customer id, digits only. |  |
|**managerLinkId** | **String** | Numeric link id from GET /v1/ads/accounts/hierarchy. |  |
|**action** | [**ActionEnum**](#ActionEnum) |  |  |
|**validateOnly** | **Boolean** |  |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACCEPT | &quot;accept&quot; |
| DECLINE | &quot;decline&quot; |
| CANCEL | &quot;cancel&quot; |
| UNLINK | &quot;unlink&quot; |



