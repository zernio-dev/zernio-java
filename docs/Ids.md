

# Ids

Picks (`in`) or leaves out (`not_in`) campaigns, ad sets or ads by their platform ids.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) |  |  |
|**op** | [**OpEnum**](#OpEnum) |  |  |
|**values** | **List&lt;String&gt;** |  |  |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| CAMPAIGN_ID | &quot;campaign_id&quot; |
| ADSET_ID | &quot;adset_id&quot; |
| AD_ID | &quot;ad_id&quot; |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| IN | &quot;in&quot; |
| NOT_IN | &quot;not_in&quot; |



