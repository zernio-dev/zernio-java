

# CreatorPortalEconomicsOneOf


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**percentOfSalesBps** | **Integer** | Share of the sales in basis points: 1500 is 15%. |  [optional] |
|**perOrderCents** | **Integer** | A flat amount per credited order. |  [optional] |
|**attribution** | [**AttributionEnum**](#AttributionEnum) | How an order is credited: the creator&#39;s discount code, the last click on their tracking link, or both with the code winning. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: AttributionEnum

| Name | Value |
|---- | -----|
| CODE_OR_LINK | &quot;code_or_link&quot; |
| CODE | &quot;code&quot; |
| LINK | &quot;link&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMMISSION | &quot;commission&quot; |



