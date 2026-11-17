

# AutomationAdFilterOneOf7

Picks or leaves out search terms by Google's status: added as a keyword, excluded as a negative, both, or neither. Search term subjects only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) |  |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**values** | [**List&lt;ValuesEnum&gt;**](#List&lt;ValuesEnum&gt;) |  |  |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| SEARCH_TERM_STATUS | &quot;search_term_status&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| IN | &quot;in&quot; |
| NOT_IN | &quot;not_in&quot; |



## Enum: List&lt;ValuesEnum&gt;

| Name | Value |
|---- | -----|
| ADDED | &quot;ADDED&quot; |
| EXCLUDED | &quot;EXCLUDED&quot; |
| ADDED_EXCLUDED | &quot;ADDED_EXCLUDED&quot; |
| NONE | &quot;NONE&quot; |



