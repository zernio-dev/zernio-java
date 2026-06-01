

# SubmitWhatsAppNumberKycRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**country** | **String** |  |  |
|**reuse** | **Boolean** | Reuse a prior approved verification for this country (skips document/field collection; places the order immediately). |  [optional] |
|**endUserFirstName** | **String** | End user&#39;s legal first name. Required when the country has an action/ID-verification (Onfido) requirement. |  [optional] |
|**endUserLastName** | **String** | End user&#39;s legal last name. Same condition as endUserFirstName. |  [optional] |
|**values** | **Map&lt;String, String&gt;** | requirementId → textual value |  [optional] |
|**documents** | [**List&lt;SubmitWhatsAppNumberKycRequestDocumentsInner&gt;**](SubmitWhatsAppNumberKycRequestDocumentsInner.md) |  |  [optional] |
|**address** | [**SubmitWhatsAppNumberKycRequestAddress**](SubmitWhatsAppNumberKycRequestAddress.md) |  |  [optional] |



