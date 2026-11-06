

# AutomationAdFilterOneOf1

Picks or leaves out objects by platform ID.

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



