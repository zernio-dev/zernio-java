

# SetCampaignResultMetricRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** |  |  |
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**currency** | **String** | ISO 4217, money metrics only. |  [optional] |
|**formula** | **String** | Makes it a computed metric. Null or absent for a number you send. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;count&quot; |
| MONEY | &quot;money&quot; |
| PERCENT | &quot;percent&quot; |
| RATIO | &quot;ratio&quot; |



