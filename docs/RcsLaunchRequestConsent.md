

# RcsLaunchRequestConsent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**optInMethods** | [**List&lt;RcsLaunchRequestConsentOptInMethodsInner&gt;**](RcsLaunchRequestConsentOptInMethodsInner.md) |  |  |
|**callToAction** | **String** | The opt-in wording people agree to. |  |
|**callToActionUrl** | **URI** | Required for WEBSITE opt-in. |  [optional] |
|**callToActionMediaUrl** | **URI** | Screenshot of the opt-in. Required for WEBSITE and MOBILE_APP opt-in. |  [optional] |
|**doubleOptIn** | **Boolean** |  |  |
|**doubleOptInMessage** | **String** | Required when doubleOptIn is true. |  [optional] |
|**optInMessage** | **String** |  |  |
|**helpResponse** | **String** |  |  |
|**optOutResponse** | **String** |  |  |



