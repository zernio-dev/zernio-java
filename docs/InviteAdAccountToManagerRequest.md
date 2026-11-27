

# InviteAdAccountToManagerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**managerCustomerId** | **String** | Manager customer id, digits only. |  |
|**clientCustomerId** | **String** | Client customer id to invite, digits only. |  |
|**validateOnly** | **Boolean** |  |  [optional] |



