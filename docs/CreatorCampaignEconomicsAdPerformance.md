

# CreatorCampaignEconomicsAdPerformance

Pays on what the ads running a post achieve. `spend` and `purchase_value` take `rateBps` (a share of the amount), `purchases` and `clicks` take `centsPerUnit` each, and `impressions` takes `centsPerUnit` per 1,000.  Sending the other rate field, or `organicViewsOnly`, answers 400. Every campaign platform must be Instagram, Facebook or TikTok. Money from an ad billed in another currency than the campaign does not count. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**metric** | [**MetricEnum**](#MetricEnum) |  |  |
|**rateBps** | **Integer** | Basis points of the spend or purchase value: 1000 is 10%. |  [optional] |
|**centsPerUnit** | **Integer** | Cents per purchase or click, or per 1,000 impressions. |  [optional] |
|**maxPayoutPerPostCents** | **Integer** |  |  [optional] |
|**budgetCents** | **Integer** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AD_PERFORMANCE | &quot;ad_performance&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| SPEND | &quot;spend&quot; |
| PURCHASES | &quot;purchases&quot; |
| PURCHASE_VALUE | &quot;purchase_value&quot; |
| CLICKS | &quot;clicks&quot; |
| IMPRESSIONS | &quot;impressions&quot; |



