

# StartCreatorPayouts200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** | Stripe-hosted onboarding page. Send the creator here; Stripe returns them to their Zernio creator page when done. Expires after a few minutes, so request it when the creator clicks. |  |
|**clientSecret** | **String** | Account session secret for Stripe&#39;s embedded onboarding component. Only usable on Zernio&#39;s own creator page; integrations use &#x60;url&#x60;. |  |



