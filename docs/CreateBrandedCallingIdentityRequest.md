

# CreateBrandedCallingIdentityRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enterpriseId** | **String** | A business from POST /v1/branded-calling/enterprises. |  |
|**displayName** | **String** | Shown on the callee&#39;s screen. No emoji. |  |
|**callReasons** | **List&lt;String&gt;** | 1 to 10 reasons you call, each up to 64 characters. Pick from GET /v1/branded-calling/call-reasons to skip manual vetting. |  |
|**logoUrl** | **String** | HTTPS URL of a PNG, JPEG, WebP or SVG logo. Zernio converts it to the 256x256 BMP the carriers require and hosts it. |  [optional] |
|**authorizer** | [**CreateBrandedCallingIdentityRequestAuthorizer**](CreateBrandedCallingIdentityRequestAuthorizer.md) |  |  |
|**references** | [**BrandedCallingReferences**](BrandedCallingReferences.md) |  |  |



