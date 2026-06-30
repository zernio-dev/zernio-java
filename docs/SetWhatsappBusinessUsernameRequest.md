

# SetWhatsappBusinessUsernameRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | WhatsApp social account ID |  |
|**username** | **String** | Desired username. Letters, digits, period, and underscore only. Must contain at least one letter. No leading, trailing, or consecutive periods. No www prefix. No domain TLD suffix.  |  |
|**transferAction** | [**TransferActionEnum**](#TransferActionEnum) | Pass &#x60;force_transfer&#x60; to request a transfer if the username is held by another account |  [optional] |



## Enum: TransferActionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| FORCE_TRANSFER | &quot;force_transfer&quot; |



