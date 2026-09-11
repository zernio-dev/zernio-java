

# CreateAdAccount201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** | New Meta ad account ID for subsequent ads calls. |  |
|**businessId** | **String** | Owning business portfolio ID. |  |
|**connectionUpdated** | **Boolean** | Whether the connection scope and discovery schedule were updated. |  |
|**paymentMethodRequired** | **Boolean** | Always true as a delivery prerequisite. This is not a live funding-source check. Confirm payment or invoicing in Ads Manager. |  |
|**adsManagerUrl** | **URI** | Open the created account in Ads Manager. |  |
|**nextSteps** | **String** | Payment setup instructions for the user. |  |
|**warnings** | **List&lt;String&gt;** | Recovery instructions if the account could not be attached to the connection. |  |



