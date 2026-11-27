

# DismissGoogleRecommendationsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**accountId** | **String** | Google ads SocialAccount id. |  |
|**adAccountId** | **String** | Google customer id, digits only. Required when the connection has several customers. |  [optional] |
|**resourceNames** | **List&lt;String&gt;** | Recommendation resource names from the list, or their ids. |  |



