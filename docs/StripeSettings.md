

# StripeSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio account ID of the Stripe connection. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**stripeAccountId** | **String** | The connected Stripe account ID (&#x60;acct_...&#x60;). |  |
|**livemode** | **Boolean** | Whether the connection counts live payments (&#x60;true&#x60;) or test payments (&#x60;false&#x60;). |  |
|**forwardSales** | **Boolean** | Whether new customers&#39; first payments go to the profile&#39;s forwarding rules. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| STRIPE | &quot;stripe&quot; |



