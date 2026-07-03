

# GetWhatsAppNumberKycForm200ResponseFieldsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requirementId** | **String** |  |  [optional] |
|**label** | **String** |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | \&quot;action\&quot; &#x3D; an out-of-band verification (e.g. Onfido); not filled here, fulfilled after the order via a link. |  [optional] |
|**description** | **String** | Plain-English explanation of what to provide. |  [optional] |
|**example** | **String** | Concrete example value. |  [optional] |
|**localTo** | **String** | ISO country the value must be local to |  [optional] |
|**audience** | [**AudienceEnum**](#AudienceEnum) | When set, the requirement applies ONLY to this end-user type — provide it for that type and OMIT it for the other (e.g. Brazil: \&quot;Cartão CNPJ\&quot; is business-only, \&quot;CPF\&quot; and \&quot;ID/Passport Copy\&quot; are personal-only). Submitting both sets makes the regulator ask whether the number is for personal or business use and stalls the review. Pass &#x60;entityType&#x60; on POST so the server drops the inapplicable set. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| DATE | &quot;date&quot; |
| ADDRESS | &quot;address&quot; |
| FILE | &quot;file&quot; |
| ACTION | &quot;action&quot; |



## Enum: AudienceEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;business&quot; |
| INDIVIDUAL | &quot;individual&quot; |



