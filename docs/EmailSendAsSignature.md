

# EmailSendAsSignature

What `appendSignature` appends for this address: the Zernio default first, else the Gmail signature. `null` means `appendSignature` answers 400.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**SourceEnum**](#SourceEnum) |  |  [optional] |
|**id** | **String** | The Zernio signature id. &#x60;null&#x60; for a Gmail signature. |  [optional] |
|**html** | **String** |  |  [optional] |
|**text** | **String** |  |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| ZERNIO | &quot;zernio&quot; |
| GMAIL | &quot;gmail&quot; |



