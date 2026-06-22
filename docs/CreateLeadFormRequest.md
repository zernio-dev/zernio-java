

# CreateLeadFormRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**name** | **String** |  |  |
|**questions** | [**List&lt;CreateLeadFormRequestQuestionsInner&gt;**](CreateLeadFormRequestQuestionsInner.md) |  |  |
|**privacyPolicyUrl** | **URI** |  |  |
|**privacyPolicyLinkText** | **String** |  |  [optional] |
|**followUpActionUrl** | **URI** |  |  [optional] |
|**locale** | **String** |  |  [optional] |
|**thankYouTitle** | **String** |  |  [optional] |
|**thankYouBody** | **String** |  |  [optional] |
|**thankYouButtonText** | **String** |  |  [optional] |
|**thankYouButtonType** | **String** |  |  [optional] |
|**thankYouWebsiteUrl** | **URI** |  |  [optional] |
|**isOptimizedForQuality** | **Boolean** | Legacy form type toggle. Prefer formType instead. false &#x3D; More Volume, true &#x3D; Higher Intent. |  [optional] |
|**formType** | [**FormTypeEnum**](#FormTypeEnum) | Form type. MORE_VOLUME &#x3D; optimized for lead quantity (default). HIGHER_INTENT &#x3D; adds a review/confirmation step before submit. RICH_CREATIVE &#x3D; includes context card and custom headline to educate users before they submit. Supersedes isOptimizedForQuality. |  [optional] |
|**blockDisplayForNonTargetedViewer** | **Boolean** | Sharing setting. true &#x3D; Restricted (only people targeted by the ad can open the form link). false &#x3D; Open (shareable link, default). |  [optional] |
|**allowOrganicLeadGen** | **Boolean** | Flexible form delivery. true &#x3D; the form can surface organically on the Page (not just as a paid ad). Defaults to false. |  [optional] |
|**questionPageCustomHeadline** | **String** | Custom subheadline shown above the form fields on the questions page (the contact-information section description). Defaults to Meta&#39;s generic copy when omitted. |  [optional] |
|**contextCard** | [**CreateLeadFormRequestContextCard**](CreateLeadFormRequestContextCard.md) |  |  [optional] |



## Enum: FormTypeEnum

| Name | Value |
|---- | -----|
| MORE_VOLUME | &quot;MORE_VOLUME&quot; |
| HIGHER_INTENT | &quot;HIGHER_INTENT&quot; |
| RICH_CREATIVE | &quot;RICH_CREATIVE&quot; |



