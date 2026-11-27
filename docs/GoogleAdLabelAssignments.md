

# GoogleAdLabelAssignments

At least one id across the four target lists. Up to 1000 ids per list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**accountId** | **String** | Zernio SocialAccount id (Google Ads) |  |
|**adAccountId** | **String** | Google customer id. Required when the connection has multiple customers. |  [optional] |
|**customerId** | **String** | Alias of adAccountId |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Google campaign ids |  [optional] |
|**adSetIds** | **List&lt;String&gt;** | Google ad group ids |  [optional] |
|**adIds** | **List&lt;String&gt;** | Google ad group ad ids, {adGroupId}~{adId} |  [optional] |
|**keywordIds** | **List&lt;String&gt;** | Google keyword criterion ids, {adGroupId}~{criterionId} |  [optional] |



