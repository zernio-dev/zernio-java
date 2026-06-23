

# CreateWhatsAppNumberKycLinkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**country** | **String** | ISO 3166-1 alpha-2 country code (must be a regulated/KYC country). |  |
|**branding** | [**CreateWhatsAppNumberKycLinkRequestBranding**](CreateWhatsAppNumberKycLinkRequestBranding.md) |  |  [optional] |
|**redirectUrl** | **URI** | Where to send the end customer&#39;s browser after a successful submit. On completion Zernio appends &#x60;kyc&#x3D;submitted&#x60; and &#x60;country&#x3D;&lt;ISO-2&gt;&#x60; as query params. When omitted, the hosted page shows a built-in confirmation screen instead.  |  [optional] |



