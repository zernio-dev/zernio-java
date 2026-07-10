

# StartSmsRegistrationRequestCampaign

Required for 10DLC. What you'll send and how recipients opt in/out. Opt-in/opt-out/help auto-responses must name the registered brand and carry the carrier-required disclosures; submissions that don't (or that are blank) are automatically rewritten to a compliant, brand-named template before the campaign is filed. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**usecase** | **String** |  |  |
|**subUsecases** | [**List&lt;SubUsecasesEnum&gt;**](#List&lt;SubUsecasesEnum&gt;) | The concrete kinds of messages a MIXED campaign sends (the carrier registry requires 2-5, and reviewers match them against the sample messages). Omitted: a default pair is applied for MIXED.  |  [optional] |
|**description** | **String** |  |  |
|**messageFlow** | **String** | How a recipient ends up receiving your messages (the opt-in flow). Include a link to the page or form where they opt in — carrier reviewers reject campaigns whose consent they can&#39;t verify. |  |
|**sample1** | **String** |  |  |
|**sample2** | **String** | Second example message; carriers require two distinct samples |  |
|**helpMessage** | **String** |  |  |
|**optinKeywords** | **String** |  |  |
|**optinMessage** | **String** |  |  |
|**optoutKeywords** | **String** |  |  |
|**optoutMessage** | **String** |  |  |
|**helpKeywords** | **String** |  |  |
|**embeddedLink** | **Boolean** |  |  [optional] |
|**embeddedPhone** | **Boolean** |  |  [optional] |
|**numberPool** | **Boolean** |  |  [optional] |
|**ageGated** | **Boolean** |  |  [optional] |
|**directLending** | **Boolean** |  |  [optional] |



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



