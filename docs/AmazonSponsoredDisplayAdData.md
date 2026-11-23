

# AmazonSponsoredDisplayAdData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adProduct** | [**AdProductEnum**](#AdProductEnum) |  |  |
|**tactic** | [**TacticEnum**](#TacticEnum) | Required for a new campaign. T00020 targets products and categories; T00030 also targets audiences (views, purchases, audience). |  [optional] |
|**portfolioId** | **String** |  |  [optional] |
|**asins** | **List&lt;String&gt;** | Vendor profiles: the ASINs to advertise, one product ad each. |  [optional] |
|**skus** | **List&lt;String&gt;** | Seller profiles: the SKUs to advertise, one product ad each. Sending the identifier the profile does not use returns a 400. |  [optional] |
|**defaultBid** | **BigDecimal** | US: 0.02 to 1000 per click, 1 to 1000 per thousand viewable impressions (goal awareness). |  [optional] |
|**targets** | [**List&lt;AmazonSponsoredDisplayAdDataAllOfTargets&gt;**](AmazonSponsoredDisplayAdDataAllOfTargets.md) | Required for a new ad group. Each entry is one Amazon targeting clause, in Amazon&#39;s own shape:  - Contextual: &#x60;{ type: similarProduct }&#x60;, &#x60;{ type: asinSameAs, value: B0... }&#x60;, &#x60;{ type: asinCategorySameAs, value: \&quot;12345\&quot; }&#x60; with optional brand, price or rating refinements in the same expression, &#x60;{ type: contentCategorySameAs, value: \&quot;amzn1.iab-content.325\&quot; }&#x60;. - Audiences (tactic T00030 only): &#x60;{ type: views | purchases, value: [{ type: exactProduct | similarProduct | relatedProduct | asinCategorySameAs ... }, { type: lookback, value: \&quot;30\&quot; }] }&#x60;, or &#x60;{ type: audience, value: [{ type: audienceSameAs, value: \&quot;&lt;audience id&gt;\&quot; }] }&#x60; for in-market and lifestyle audiences.  |  [optional] |
|**negativeTargets** | [**List&lt;AmazonSponsoredBrandsAdDataAllOfNegativeProductTargets&gt;**](AmazonSponsoredBrandsAdDataAllOfNegativeProductTargets.md) |  |  [optional] |



## Enum: AdProductEnum

| Name | Value |
|---- | -----|
| SPONSORED_DISPLAY | &quot;SPONSORED_DISPLAY&quot; |



## Enum: TacticEnum

| Name | Value |
|---- | -----|
| T00020 | &quot;T00020&quot; |
| T00030 | &quot;T00030&quot; |



