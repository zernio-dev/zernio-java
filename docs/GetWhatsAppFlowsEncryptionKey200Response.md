

# GetWhatsAppFlowsEncryptionKey200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publicKey** | **String** | The registered RSA public key in PEM format, or null when none is registered. |  [optional] |
|**signatureStatus** | [**SignatureStatusEnum**](#SignatureStatusEnum) | VALID (key matches Meta&#39;s records) or MISMATCH (no key registered, or the key does not match); null when unknown. |  [optional] |
|**registered** | **Boolean** | Whether a key is currently registered. Derived from publicKey, not signatureStatus. |  [optional] |



## Enum: SignatureStatusEnum

| Name | Value |
|---- | -----|
| VALID | &quot;VALID&quot; |
| MISMATCH | &quot;MISMATCH&quot; |



