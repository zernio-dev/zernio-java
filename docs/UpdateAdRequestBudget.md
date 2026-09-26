

# UpdateAdRequestBudget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | Minimum varies by platform: TikTok&#x3D;$20, Pinterest&#x3D;$5, others&#x3D;$1 |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | OpenAI Ads accepts both and sets the campaign&#39;s single spend cap, replacing the previous daily or lifetime cap. A daily cap cannot go back to lifetime (422). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| LIFETIME | &quot;lifetime&quot; |



