

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
|**thankYouButtonType** | **String** |  |  [optional] |
|**thankYouWebsiteUrl** | **URI** |  |  [optional] |
|**thankYouEnableMessenger** | **Boolean** | Adds a &#39;Continue in Messenger&#39; option to the thank-you page (Meta thank_you_page.enable_messenger), so the lead can carry on chatting with the Page. Set thankYouButtonType to MESSAGE_BUSINESS or P2B_MESSENGER to make the chat the primary button. |  [optional] |
|**isOptimizedForQuality** | **Boolean** | Set true for a higher-intent form (adds a review step before submit). |  [optional] |
|**isPhoneSmsVerifyEnabled** | **Boolean** | Requires the lead to verify their phone number over SMS before the form submits (Meta is_phone_sms_verify_enabled). Only meaningful on a form with a PHONE question. Meta can restrict this parameter to apps holding a capability: when it does, the create fails with a 422 naming platformSpecificData.isPhoneSmsVerifyEnabled, and the toggle then has to be set in Meta&#39;s form builder. |  [optional] |
|**blockDisplayForNonTargetedViewer** | **Boolean** |  |  [optional] |
|**questionPageCustomHeadline** | **String** |  |  [optional] |
|**contextCard** | [**MetaLeadFormPlatformDataContextCard**](MetaLeadFormPlatformDataContextCard.md) |  |  [optional] |



