

# CreateAdInsightsReportRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (posting or ads variant). |  |
|**objectId** | **String** | Meta insights node: act_&lt;n&gt;, campaign id, ad set id or ad id. |  |
|**level** | [**LevelEnum**](#LevelEnum) |  |  [optional] |
|**fields** | **String** | Comma-separated Graph insights fields. |  [optional] |
|**breakdowns** | **String** | Comma-separated Graph breakdowns. |  [optional] |
|**actionBreakdowns** | **String** | Comma-separated Graph action breakdowns (e.g. action_type,action_destination). |  [optional] |
|**actionAttributionWindows** | **List&lt;String&gt;** | Meta attribution windows (e.g. [\&quot;7d_click\&quot;, \&quot;1d_view\&quot;]). Action values are returned keyed per window. |  [optional] |
|**actionReportTime** | **String** | When actions are counted: impression, conversion or mixed. |  [optional] |
|**useUnifiedAttributionSetting** | **Boolean** | Use the ad sets&#39; own attribution settings for action counting. |  [optional] |
|**filtering** | [**List&lt;CreateAdInsightsReportRequestFilteringInner&gt;**](CreateAdInsightsReportRequestFilteringInner.md) | Meta filter objects, applied server-side. |  [optional] |
|**datePreset** | **String** | Mutually exclusive with fromDate/toDate. |  [optional] |
|**fromDate** | **LocalDate** |  |  [optional] |
|**toDate** | **LocalDate** |  |  [optional] |
|**timeIncrement** | [**CreateAdInsightsReportRequestTimeIncrement**](CreateAdInsightsReportRequestTimeIncrement.md) |  |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| AD | &quot;ad&quot; |
| ADSET | &quot;adset&quot; |
| CAMPAIGN | &quot;campaign&quot; |
| ACCOUNT | &quot;account&quot; |



