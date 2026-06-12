

# GetWhatsAppNumberKycForm200ResponseReusable

Present when this account already has an approved verification for the country that can be reused (skip the form). `fromPhoneNumber`/`details` mirror the newest option; `options` lists ALL approved verifications (agencies hold one per end client) — pass the chosen option's `fromPhoneNumber` as `reuseFrom` on POST.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** |  |  [optional] |
|**fromPhoneNumber** | **String** |  |  [optional] |
|**details** | [**List&lt;GetWhatsAppNumberKycForm200ResponseReusableDetailsInner&gt;**](GetWhatsAppNumberKycForm200ResponseReusableDetailsInner.md) | Human-readable summary of the verification on file (field labels + values, plus the address as one line). Best-effort — may be empty if the provider lookup fails. |  [optional] |
|**options** | [**List&lt;GetWhatsAppNumberKycForm200ResponseReusableOptionsInner&gt;**](GetWhatsAppNumberKycForm200ResponseReusableOptionsInner.md) | One entry per distinct approved verification, newest first. |  [optional] |



