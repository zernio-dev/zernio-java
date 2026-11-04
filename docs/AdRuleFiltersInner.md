

# AdRuleFiltersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) | The object&#39;s own name, its campaign&#39;s or ad set&#39;s name, or the campaign goal (objective) as the platform reports it. |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**value** | **String** |  |  |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| NAME | &quot;name&quot; |
| CAMPAIGN_NAME | &quot;campaign_name&quot; |
| ADSET_NAME | &quot;adset_name&quot; |
| GOAL | &quot;goal&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| CONTAINS | &quot;contains&quot; |
| NOT_CONTAINS | &quot;not_contains&quot; |
| EQUALS | &quot;equals&quot; |
| NOT_EQUALS | &quot;not_equals&quot; |
| STARTS_WITH | &quot;starts_with&quot; |



