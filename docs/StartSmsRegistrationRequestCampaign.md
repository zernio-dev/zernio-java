

# StartSmsRegistrationRequestCampaign

Required for 10DLC. What you'll send and how recipients opt in/out. The opt-in/opt-out/help auto-responses (`optinMessage`, `optoutMessage`, `helpMessage`) are optional: when omitted, a compliant, brand-named template with the carrier-required disclosures is generated for you. If you do send them, they must name the registered brand and carry the disclosures — submissions that don't are rewritten to the compliant template before the campaign is filed. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**usecase** | **String** |  |  |
|**subUsecases** | [**List&lt;SubUsecasesEnum&gt;**](#List&lt;SubUsecasesEnum&gt;) | The concrete kinds of messages a MIXED campaign sends (the carrier registry requires 2-5, and reviewers match them against the sample messages). Omitted: a default pair is applied for MIXED.  |  [optional] |
|**description** | **String** |  |  |
|**messageFlow** | **String** | How a recipient ends up receiving your messages (the opt-in flow). Include a link to the page or form where they opt in — carrier reviewers reject campaigns whose consent they can&#39;t verify. |  |
|**sample1** | **String** |  |  |
|**sample2** | **String** | Second example message; carriers require two distinct samples, so it must differ from sample1. |  |
|**helpMessage** | **String** |  |  [optional] |
|**optinKeywords** | **String** |  |  |
|**optinMessage** | **String** |  |  [optional] |
|**optoutKeywords** | **String** |  |  |
|**optoutMessage** | **String** |  |  [optional] |
|**helpKeywords** | **String** |  |  |
|**embeddedLink** | **Boolean** | Whether messages carry links. Auto-derived from the samples when omitted, so the declaration matches what the reviewer reads. |  [optional] |
|**embeddedPhone** | **Boolean** | Whether messages carry phone numbers. Auto-derived from the samples when omitted. |  [optional] |
|**numberPool** | **Boolean** |  |  [optional] |
|**ageGated** | **Boolean** |  |  [optional] |
|**directLending** | **Boolean** |  |  [optional] |
|**privacyPolicyLink** | **String** | Link to your privacy policy. Recommended: reviewers check that it says mobile information is not sold or shared with third parties for promotional purposes. A bare domain is normalized to https://. |  [optional] |
|**termsAndConditionsLink** | **String** | Link to your terms &amp; conditions. A bare domain is normalized to https://. |  [optional] |



## Enum: List&lt;SubUsecasesEnum&gt;

| Name | Value |
|---- | -----|
| _2_FA | &quot;2FA&quot; |
| ACCOUNT_NOTIFICATION | &quot;ACCOUNT_NOTIFICATION&quot; |
| CUSTOMER_CARE | &quot;CUSTOMER_CARE&quot; |
| DELIVERY_NOTIFICATION | &quot;DELIVERY_NOTIFICATION&quot; |
| FRAUD_ALERT | &quot;FRAUD_ALERT&quot; |
| HIGHER_EDUCATION | &quot;HIGHER_EDUCATION&quot; |
| MARKETING | &quot;MARKETING&quot; |
| POLLING_VOTING | &quot;POLLING_VOTING&quot; |
| PUBLIC_SERVICE_ANNOUNCEMENT | &quot;PUBLIC_SERVICE_ANNOUNCEMENT&quot; |
| SECURITY_ALERT | &quot;SECURITY_ALERT&quot; |



