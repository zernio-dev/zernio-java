

# CreatePhoneNumberKycLinkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**country** | **String** | ISO 3166-1 alpha-2 country code (must be a regulated/KYC country). |  |
|**areaCode** | **String** | Area code (NDC) the eventual number must be in. Hard constraint carried by the link; the end customer filling the form makes no area choice. Options come from GET /v1/phone-numbers/availability (areaOptions). |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) | Language of the hosted page: its copy, the carrier requirement texts (translated once per country and cached), the pre-submit review notes and the status emails to the end customer. Omitted: the browser language of the end customer, falling back to English. The end customer can also switch with &#x60;?lang&#x3D;&#x60; on the page. |  [optional] |
|**branding** | [**CreatePhoneNumberKycLinkRequestBranding**](CreatePhoneNumberKycLinkRequestBranding.md) |  |  [optional] |
|**redirectUrl** | **URI** | Where to send the end customer&#39;s browser after a successful submit. On completion Zernio appends &#x60;kyc&#x3D;submitted&#x60; and &#x60;country&#x3D;&lt;ISO-2&gt;&#x60; as query params. When omitted, the hosted page shows a built-in confirmation screen instead.  |  [optional] |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| EN | &quot;en&quot; |
| ES | &quot;es&quot; |
| PT_BR | &quot;pt-BR&quot; |



