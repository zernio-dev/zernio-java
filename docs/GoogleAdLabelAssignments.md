

# GoogleAdLabelAssignments

At least one id across the four target lists. Up to 1000 ids per list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (Google Ads) |  |
|**adAccountId** | **String** | Google customer id. Required when the connection has multiple customers. |  [optional] |
|**customerId** | **String** | Alias of adAccountId |  [optional] |
|**campaignIds** | **List&lt;String&gt;** | Google campaign ids |  [optional] |
|**adSetIds** | **List&lt;String&gt;** | Google ad group ids |  [optional] |
|**adIds** | **List&lt;String&gt;** | Google ad group ad ids, {adGroupId}~{adId} |  [optional] |
|**keywordIds** | **List&lt;String&gt;** | Google keyword criterion ids, {adGroupId}~{criterionId} |  [optional] |



