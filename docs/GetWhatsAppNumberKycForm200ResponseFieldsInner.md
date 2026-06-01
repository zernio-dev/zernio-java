

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



## Enum: KindEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| DATE | &quot;date&quot; |
| ADDRESS | &quot;address&quot; |
| FILE | &quot;file&quot; |
| ACTION | &quot;action&quot; |



