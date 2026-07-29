

# GenerateKeywordHistoricalMetricsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio googleads SocialAccount id. |  |
|**customerId** | **String** | Numeric Google Ads customer id (no dashes); only needed when the connection has several accounts. |  [optional] |
|**keywords** | **List&lt;String&gt;** |  |  |
|**countries** | **List&lt;String&gt;** | ISO 3166-1 alpha-2 country codes. Omitted &#x3D; worldwide. |  [optional] |
|**languageConstantId** | **String** | Google languageConstant id (1000 &#x3D; English). |  [optional] |
|**network** | [**NetworkEnum**](#NetworkEnum) |  |  [optional] |
|**includeAdultKeywords** | **Boolean** |  |  [optional] |
|**includeAverageCpc** | **Boolean** | Adds averageCpcMicros to each row&#39;s keywordMetrics. |  [optional] |



## Enum: NetworkEnum

| Name | Value |
|---- | -----|
| GOOGLE_SEARCH | &quot;GOOGLE_SEARCH&quot; |
| GOOGLE_SEARCH_AND_PARTNERS | &quot;GOOGLE_SEARCH_AND_PARTNERS&quot; |



