

# UpdateAdLabelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**accountId** | **String** | Zernio SocialAccount id (Google Ads) |  |
|**adAccountId** | **String** | Google customer id. Required when the connection has multiple customers. |  [optional] |
|**customerId** | **String** | Alias of adAccountId |  [optional] |
|**name** | **String** |  |  [optional] |
|**backgroundColor** | **String** |  |  [optional] |
|**description** | **String** | Send \&quot;\&quot; to clear it. |  [optional] |



