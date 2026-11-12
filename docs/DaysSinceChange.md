

# DaysSinceChange

Days since the campaign's budget, bidding, status or conversion goal last changed, on the campaign or, on Meta, one of its ad sets. Read from the platform's change history, Meta and Google only.  A campaign with no such change in the history passes `>=` and fails `<`. Google records an edit of conversion goals as a campaign update naming no field, so `goal` reads those.  On Google, a change to a shared (portfolio) bid strategy does not count as a `bidding` change of its campaigns. 

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



