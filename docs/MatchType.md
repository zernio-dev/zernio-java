

# MatchType

Picks (`in`) or leaves out (`not_in`) keywords by match type, or search terms by the match type of the keyword that matched them. Keyword and search term rules only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) |  |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**values** | [**List&lt;ValuesEnum&gt;**](#List&lt;ValuesEnum&gt;) |  |  |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| MATCH_TYPE | &quot;match_type&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| IN | &quot;in&quot; |
| NOT_IN | &quot;not_in&quot; |



## Enum: List&lt;ValuesEnum&gt;

| Name | Value |
|---- | -----|
| EXACT | &quot;EXACT&quot; |
| PHRASE | &quot;PHRASE&quot; |
| BROAD | &quot;BROAD&quot; |



