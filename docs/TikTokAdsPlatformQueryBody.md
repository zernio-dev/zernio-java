

# TikTokAdsPlatformQueryBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Zernio id of the connected TikTok ads account. |  |
|**adAccountId** | **String** | The numeric TikTok advertiser id. |  |
|**reportType** | [**ReportTypeEnum**](#ReportTypeEnum) | Defaults to BASIC. |  [optional] |
|**dataLevel** | [**DataLevelEnum**](#DataLevelEnum) | The level of each row. |  |
|**dimensions** | **List&lt;String&gt;** | TikTok dimensions, 1 to 4. |  |
|**metrics** | **List&lt;String&gt;** | TikTok metrics, up to 100. |  |
|**filtering** | [**List&lt;MetaAdsPlatformQueryBodyFilteringInner&gt;**](MetaAdsPlatformQueryBodyFilteringInner.md) | TikTok filters of field, operator and value, up to 25. A filter on an entity finer than dataLevel is refused. |  [optional] |
|**fromDate** | **LocalDate** | First day, YYYY-MM-DD, inclusive. |  |
|**toDate** | **LocalDate** | Last day, YYYY-MM-DD, inclusive. |  |
|**pageSize** | **Integer** | Rows per page, up to 1,000. Defaults to 1,000. |  [optional] |
|**cursor** | **String** | The pagination.nextCursor of the previous page, unchanged. |  [optional] |



## Enum: ReportTypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;BASIC&quot; |
| AUDIENCE | &quot;AUDIENCE&quot; |



## Enum: DataLevelEnum

| Name | Value |
|---- | -----|
| AUCTION_ADVERTISER | &quot;AUCTION_ADVERTISER&quot; |
| AUCTION_CAMPAIGN | &quot;AUCTION_CAMPAIGN&quot; |
| AUCTION_ADGROUP | &quot;AUCTION_ADGROUP&quot; |
| AUCTION_AD | &quot;AUCTION_AD&quot; |



