

# GetPhoneNumberKycForm200ResponseReusable

Present when this account already has a reusable verification for the country (skip the form). `fromPhoneNumber`/`details` mirror the first option; `options` lists ALL reusable verifications (agencies hold one per end client), approved-first. Pass the chosen option's `id` as `reuseOptionId` on POST. Each option's `instant` says whether it activates in minutes (group-approved) or still queues for carrier review (1-3 days).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** |  |  [optional] |
|**fromPhoneNumber** | **String** |  |  [optional] |
|**details** | [**List&lt;GetPhoneNumberKycForm200ResponseReusableDetailsInner&gt;**](GetPhoneNumberKycForm200ResponseReusableDetailsInner.md) | Human-readable summary of the verification on file (field labels + values, plus the address as one line). Best-effort — may be empty if the provider lookup fails. |  [optional] |
|**options** | [**List&lt;GetPhoneNumberKycForm200ResponseReusableOptionsInner&gt;**](GetPhoneNumberKycForm200ResponseReusableOptionsInner.md) | One entry per distinct approved verification, newest first. |  [optional] |



