

# AutomationAdFilterOneOf3

Days since the campaign's budget, bidding, status or goal last changed, from the platform's change history. Campaign rules on Meta and Google only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) |  |  |
|**change** | [**ChangeEnum**](#ChangeEnum) |  |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**value** | **Integer** |  |  |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| DAYS_SINCE_CHANGE | &quot;days_since_change&quot; |



## Enum: ChangeEnum

| Name | Value |
|---- | -----|
| BUDGET | &quot;budget&quot; |
| BIDDING | &quot;bidding&quot; |
| STATUS | &quot;status&quot; |
| GOAL | &quot;goal&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| GREATER_THAN_OR_EQUAL_TO | &quot;&gt;&#x3D;&quot; |
| LESS_THAN | &quot;&lt;&quot; |



