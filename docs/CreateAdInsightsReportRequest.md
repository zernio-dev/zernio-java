

# CreateAdInsightsReportRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id (posting or ads variant). |  |
|**objectId** | **String** | Meta insights node: act_&lt;n&gt;, campaign id, ad set id or ad id. |  |
|**level** | [**LevelEnum**](#LevelEnum) |  |  [optional] |
|**fields** | **String** | Comma-separated Graph insights fields. |  [optional] |
|**breakdowns** | **String** | Comma-separated Graph breakdowns. |  [optional] |
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



