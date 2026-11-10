

# CreatorPortalReferral


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The creator&#39;s discount code. Null while the store has not created it yet, or on a link-only campaign. |  |
|**discountPercent** | **Integer** | What the code takes off an order. |  |
|**trackingUrl** | **String** | The landing page with the UTM parameters that credit the creator. Null on a code-only campaign. |  |
|**orders** | [**List&lt;CreatorPortalReferralOrdersInner&gt;**](CreatorPortalReferralOrdersInner.md) | The latest 50 credited orders. |  |
|**totals** | [**CreatorPortalReferralTotals**](CreatorPortalReferralTotals.md) |  |  |



