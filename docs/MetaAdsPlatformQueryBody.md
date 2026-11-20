

# MetaAdsPlatformQueryBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Zernio id of the connected Meta ads account. |  |
|**adAccountId** | **String** | The Meta ad account, act_&lt;n&gt;. Read its campaigns, ad sets or ads with level and filtering. |  |
|**level** | [**LevelEnum**](#LevelEnum) | The level of each row. Defaults to the ad account. |  [optional] |
|**fields** | **List&lt;String&gt;** | Meta insights fields, such as spend or impressions, up to 100. |  [optional] |
|**breakdowns** | **List&lt;String&gt;** | Meta breakdowns, up to 5. |  [optional] |
|**actionBreakdowns** | **List&lt;String&gt;** | An empty array asks Meta for no action breakdown at all. |  [optional] |
|**actionAttributionWindows** | **List&lt;String&gt;** | Meta attribution windows, such as 7d_click or 1d_view. |  [optional] |
|**actionReportTime** | **String** | impression, conversion or mixed. |  [optional] |
|**useUnifiedAttributionSetting** | **Boolean** | Use each ad set&#39;s own attribution setting. |  [optional] |
|**filtering** | [**List&lt;MetaAdsPlatformQueryBodyFilteringInner&gt;**](MetaAdsPlatformQueryBodyFilteringInner.md) | Meta filters of field, operator and value, up to 25. |  [optional] |
|**datePreset** | **String** | A Meta date preset, such as last_30d. Not with fromDate and toDate. |  [optional] |
|**fromDate** | **LocalDate** | First day, YYYY-MM-DD, sent with toDate. |  [optional] |
|**toDate** | **LocalDate** | Last day, YYYY-MM-DD, sent with fromDate. |  [optional] |
|**timeIncrement** | [**MetaAdsPlatformQueryBodyTimeIncrement**](MetaAdsPlatformQueryBodyTimeIncrement.md) |  |  [optional] |
|**limit** | **Integer** | Rows per page, up to 500. Defaults to 500. |  [optional] |
|**cursor** | **String** | The pagination.nextCursor of the previous page, unchanged. |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| AD | &quot;ad&quot; |
| ADSET | &quot;adset&quot; |
| CAMPAIGN | &quot;campaign&quot; |
| ACCOUNT | &quot;account&quot; |



