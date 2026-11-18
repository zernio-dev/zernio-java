

# QueryGoogleSearchConsoleSearchAnalyticsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio account ID of the Google Search Console connection. |  |
|**fromDate** | **LocalDate** |  |  [optional] |
|**toDate** | **LocalDate** |  |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Which Google surface to read. Defaults to &#x60;web&#x60;. |  [optional] |
|**dimensionFilterGroups** | [**List&lt;QueryGoogleSearchConsoleSearchAnalyticsRequestDimensionFilterGroupsInner&gt;**](QueryGoogleSearchConsoleSearchAnalyticsRequestDimensionFilterGroupsInner.md) |  |  [optional] |
|**aggregationType** | [**AggregationTypeEnum**](#AggregationTypeEnum) |  |  [optional] |
|**rowLimit** | **Integer** | Defaults to 1000. |  [optional] |
|**startRow** | **Integer** | Row offset for paging past &#x60;rowLimit&#x60;. |  [optional] |
|**dataState** | [**DataStateEnum**](#DataStateEnum) | &#x60;final&#x60; (default) leaves out the last two or three days; &#x60;all&#x60; includes them while Google is still filling them in; &#x60;hourly_all&#x60; is required with the &#x60;hour&#x60; dimension. |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DATE | &quot;date&quot; |
| HOUR | &quot;hour&quot; |
| QUERY | &quot;query&quot; |
| PAGE | &quot;page&quot; |
| COUNTRY | &quot;country&quot; |
| DEVICE | &quot;device&quot; |
| SEARCH_APPEARANCE | &quot;searchAppearance&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |
| NEWS | &quot;news&quot; |
| DISCOVER | &quot;discover&quot; |
| GOOGLE_NEWS | &quot;googleNews&quot; |



## Enum: AggregationTypeEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;auto&quot; |
| BY_PAGE | &quot;byPage&quot; |
| BY_PROPERTY | &quot;byProperty&quot; |



## Enum: DataStateEnum

| Name | Value |
|---- | -----|
| FINAL | &quot;final&quot; |
| ALL | &quot;all&quot; |
| HOURLY_ALL | &quot;hourly_all&quot; |



