

# CreatorCampaignCommissionTerms

Commission on store orders. Set `percentOfSalesBps`, `perOrderCents` or both. Sales are the line items after discounts, before shipping and tax; refunds come off them, and a cancelled or fully refunded order earns nothing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**percentOfSalesBps** | **Integer** | Share of the sales in basis points: 1500 is 15%. |  [optional] |
|**perOrderCents** | **Integer** | A flat amount per credited order. |  [optional] |
|**attribution** | [**AttributionEnum**](#AttributionEnum) | How an order is credited: the creator&#39;s discount code, the last click on their tracking link, or both with the code winning. |  [optional] |



## Enum: AttributionEnum

| Name | Value |
|---- | -----|
| CODE_OR_LINK | &quot;code_or_link&quot; |
| CODE | &quot;code&quot; |
| LINK | &quot;link&quot; |



