

# MetaLeadFormPlatformData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**questions** | [**List&lt;CreateLeadFormRequestQuestionsInner&gt;**](CreateLeadFormRequestQuestionsInner.md) |  |  |
|**privacyPolicyLinkText** | **String** |  |  [optional] |
|**followUpActionUrl** | **URI** |  |  [optional] |
|**locale** | **String** |  |  [optional] |
|**thankYouTitle** | **String** |  |  [optional] |
|**thankYouBody** | **String** |  |  [optional] |
|**thankYouButtonText** | **String** |  |  [optional] |
|**thankYouButtonType** | **String** | Meta thank_you_page.button_type. Defaults to VIEW_WEBSITE. Case-insensitive, sent to Meta in uppercase. CALL_BUSINESS requires businessPhoneNumber and countryCode (a 400 otherwise). Meta rejects MESSAGE_BUSINESS on thank-you pages with (#100) This button type is not yet supported for Thank You Page. |  [optional] |
|**businessPhoneNumber** | **String** | International E.164 number the CALL_BUSINESS thank-you button dials (Meta thank_you_page.business_phone_number).  - Must start with + and the country calling code matching countryCode. Spaces, dashes, dots and parentheses are stripped; a local number such as 2025550123 is a 400. - Required when thankYouButtonType is CALL_BUSINESS; a 400 with any other button type. - Accepted only inside platformSpecificData; a top-level businessPhoneNumber is a 400. |  [optional] |
|**countryCode** | **String** | ISO 3166-1 alpha-2 country of businessPhoneNumber (Meta thank_you_page.country_code), sent in uppercase. Required when thankYouButtonType is CALL_BUSINESS and a 400 with any other button type. Accepted only inside platformSpecificData: a top-level countryCode is a 400. |  [optional] |
|**thankYouWebsiteUrl** | **URI** |  |  [optional] |
|**thankYouEnableMessenger** | **Boolean** | Sent as Meta thank_you_page.enable_messenger (boolean). Accepted only inside platformSpecificData: a top-level thankYouEnableMessenger is a 400. |  [optional] |
|**isOptimizedForQuality** | **Boolean** | Set true for a higher-intent form (adds a review step before submit). |  [optional] |
|**isPhoneSmsVerifyEnabled** | **Boolean** | Requires the lead to verify their phone number over SMS before the form submits (Meta is_phone_sms_verify_enabled). Only meaningful on a form with a PHONE question.  Meta can restrict this parameter to apps holding a capability. When it does, the create fails with a 422 naming platformSpecificData.isPhoneSmsVerifyEnabled, and the toggle must then be set in Meta&#39;s form builder. |  [optional] |
|**blockDisplayForNonTargetedViewer** | **Boolean** |  |  [optional] |
|**questionPageCustomHeadline** | **String** |  |  [optional] |
|**contextCard** | [**MetaLeadFormPlatformDataContextCard**](MetaLeadFormPlatformDataContextCard.md) |  |  [optional] |
|**customDisclaimer** | [**MetaLeadFormPlatformDataCustomDisclaimer**](MetaLeadFormPlatformDataCustomDisclaimer.md) |  |  [optional] |



