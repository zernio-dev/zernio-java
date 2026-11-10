

# EmailCapabilitiesSignatures


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provider** | [**ProviderEnum**](#ProviderEnum) | &#x60;read&#x60;: &#x60;appendSignature&#x60; falls back to the provider signature when no Zernio default exists. |  [optional] |
|**zernio** | **Boolean** | Zernio-stored signatures (&#x60;/v1/email/signatures&#x60;) work on this mailbox. |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| NONE | &quot;none&quot; |



