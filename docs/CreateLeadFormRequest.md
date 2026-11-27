

# CreateLeadFormRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**accountId** | **String** |  |  |
|**name** | **String** |  |  |
|**questions** | [**List&lt;CreateLeadFormRequestQuestionsInner&gt;**](CreateLeadFormRequestQuestionsInner.md) | Deprecated (Meta legacy shape): use platformSpecificData.questions. |  [optional] |
|**privacyPolicyUrl** | **URI** |  |  |
|**privacyPolicyLinkText** | **String** | Deprecated: use platformSpecificData.privacyPolicyLinkText. |  [optional] |
|**followUpActionUrl** | **URI** | Deprecated: use platformSpecificData.followUpActionUrl. |  [optional] |
|**locale** | **String** | Deprecated: use platformSpecificData.locale. |  [optional] |
|**thankYouTitle** | **String** | Deprecated: use platformSpecificData.thankYouTitle. |  [optional] |
|**thankYouBody** | **String** | Deprecated: use platformSpecificData.thankYouBody. |  [optional] |
|**thankYouButtonText** | **String** | Deprecated: use platformSpecificData.thankYouButtonText. |  [optional] |
|**thankYouButtonType** | **String** | Deprecated: use platformSpecificData.thankYouButtonType. |  [optional] |
|**thankYouWebsiteUrl** | **URI** | Deprecated: use platformSpecificData.thankYouWebsiteUrl. |  [optional] |
|**isOptimizedForQuality** | **Boolean** | Deprecated: use platformSpecificData.isOptimizedForQuality. |  [optional] |
|**platformSpecificData** | [**CreateLeadFormRequestPlatformSpecificData**](CreateLeadFormRequestPlatformSpecificData.md) |  |  [optional] |



