

# QueryGoogleSearchConsoleSearchAnalyticsRequestDimensionFilterGroupsInnerFiltersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | [**DimensionEnum**](#DimensionEnum) | Narrow dates with startDate and endDate instead. |  |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Defaults to &#x60;equals&#x60;. |  [optional] |
|**expression** | **String** | The value to match. Countries are ISO 3166-1 alpha-3 codes (&#x60;usa&#x60;), devices &#x60;DESKTOP&#x60;, &#x60;MOBILE&#x60; or &#x60;TABLET&#x60;. |  |



## Enum: DimensionEnum

| Name | Value |
|---- | -----|
| QUERY | &quot;query&quot; |
| PAGE | &quot;page&quot; |
| COUNTRY | &quot;country&quot; |
| DEVICE | &quot;device&quot; |
| SEARCH_APPEARANCE | &quot;searchAppearance&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUALS | &quot;equals&quot; |
| NOT_EQUALS | &quot;notEquals&quot; |
| CONTAINS | &quot;contains&quot; |
| NOT_CONTAINS | &quot;notContains&quot; |
| INCLUDING_REGEX | &quot;includingRegex&quot; |
| EXCLUDING_REGEX | &quot;excludingRegex&quot; |



