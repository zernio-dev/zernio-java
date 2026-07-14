

# LinkedInAdsPlatformData

LinkedIn campaign bidding and delivery controls for POST /v1/ads/boost and POST /v1/ads/create. Unknown keys are rejected. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costType** | [**CostTypeEnum**](#CostTypeEnum) | Campaign cost model (billing event). Defaults to &#x60;CPM&#x60;. Required when &#x60;unitCost&#x60; is set so the manual bid applies to an explicit cost model.  |  [optional] |
|**unitCost** | **BigDecimal** | Manual bid in WHOLE account-currency units (e.g. 2.5 &#x3D; $2.50). Requires &#x60;costType&#x60;. Omit for LinkedIn&#39;s automated (max delivery) bidding. LinkedIn enforces its own per-audience min/max bid bounds.  |  [optional] |
|**optimizationTargetType** | **String** | Campaign &#x60;optimizationTargetType&#x60; (e.g. &#x60;MAX_CLICK&#x60;, &#x60;TARGET_COST_PER_CLICK&#x60;, &#x60;MAX_IMPRESSION&#x60;). Forwarded verbatim — LinkedIn validates compatibility with the objective and &#x60;costType&#x60;. Omit for the objective-derived default.  |  [optional] |
|**creativeSelection** | [**CreativeSelectionEnum**](#CreativeSelectionEnum) | How LinkedIn rotates creatives within the campaign. Defaults to &#x60;OPTIMIZED&#x60;. |  [optional] |
|**audienceExpansionEnabled** | **Boolean** | Enable LinkedIn audience expansion. Defaults to false. |  [optional] |
|**offsiteDeliveryEnabled** | **Boolean** | Deliver on the LinkedIn Audience Network. Defaults to false. |  [optional] |
|**connectedTelevisionOnly** | **Boolean** | Restrict delivery to Connected TV inventory. |  [optional] |



## Enum: CostTypeEnum

| Name | Value |
|---- | -----|
| CPM | &quot;CPM&quot; |
| CPC | &quot;CPC&quot; |
| CPV | &quot;CPV&quot; |



## Enum: CreativeSelectionEnum

| Name | Value |
|---- | -----|
| OPTIMIZED | &quot;OPTIMIZED&quot; |
| ROUND_ROBIN | &quot;ROUND_ROBIN&quot; |



