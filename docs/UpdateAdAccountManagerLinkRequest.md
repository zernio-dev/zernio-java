

# UpdateAdAccountManagerLinkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
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



