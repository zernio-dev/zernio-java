

# GetPhoneNumberKycForm200ResponseReusable

Present when a number on the requested profile already holds a reusable verification for the country (skip the form). Without `profileId` it covers the whole account, except for keys and team members limited to some profiles, who get none.  - `fromPhoneNumber`/`details` mirror the first option. - `options` lists the reusable verifications held by numbers on `profileId` (all of the account's when omitted), approved-first. Pass the chosen option's `id` as `reuseOptionId` on POST. - Each option's `instant` says whether it activates in minutes (group-approved) or still queues for carrier review (1-3 days). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** |  |  [optional] |
|**fromPhoneNumber** | **String** |  |  [optional] |
|**details** | [**List&lt;GetPhoneNumberKycForm200ResponseReusableDetailsInner&gt;**](GetPhoneNumberKycForm200ResponseReusableDetailsInner.md) | Human-readable summary of the verification on file (field labels + values, plus the address as one line). Best-effort. May be empty if the provider lookup fails. |  [optional] |
|**options** | [**List&lt;GetPhoneNumberKycForm200ResponseReusableOptionsInner&gt;**](GetPhoneNumberKycForm200ResponseReusableOptionsInner.md) | One entry per distinct approved verification, newest first. |  [optional] |



