

# InlineObject2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** | Human-readable error message suitable for end-user display. |  |
|**code** | [**CodeEnum**](#CodeEnum) | Machine-readable error code. Stable across versions. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Discriminator for which gate fired. |  |
|**documentationUrl** | **URI** | Link to the relevant documentation page. |  [optional] |
|**dashboardUrl** | **URI** | Deep-link to send the end-user to. For &#x60;free_tier_exceeded&#x60; and &#x60;twitter_passthrough&#x60; this is the Zernio billing tab. For &#x60;enterprise_required&#x60; this is the Zernio enterprise contact page.  |  [optional] |
|**details** | [**InlineObject2Details**](InlineObject2Details.md) |  |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| PAYMENT_REQUIRED | &quot;PAYMENT_REQUIRED&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| FREE_TIER_EXCEEDED | &quot;free_tier_exceeded&quot; |
| TWITTER_PASSTHROUGH | &quot;twitter_passthrough&quot; |
| ENTERPRISE_REQUIRED | &quot;enterprise_required&quot; |



