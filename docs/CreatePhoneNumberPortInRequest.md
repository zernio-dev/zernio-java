

# CreatePhoneNumberPortInRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumbers** | **List&lt;String&gt;** | E.164 numbers to port in. |  |
|**endUser** | [**CreatePhoneNumberPortInRequestEndUser**](CreatePhoneNumberPortInRequestEndUser.md) |  |  |
|**loaDocumentId** | **String** | Document id from POST /v1/phone-numbers/port-in/documents (kind&#x3D;loa). |  |
|**invoiceDocumentId** | **String** | Document id from POST /v1/phone-numbers/port-in/documents (kind&#x3D;invoice). |  |
|**focDatetimeRequested** | **OffsetDateTime** | Requested port date; the carrier confirms the actual FOC later. Defaults to one week out (shifted off weekends) when omitted. |  [optional] |
|**customerReference** | **String** |  |  [optional] |
|**portType** | [**PortTypeEnum**](#PortTypeEnum) | Whether the losing account ports all its numbers (full) or keeps some (partial). |  [optional] |



## Enum: PortTypeEnum

| Name | Value |
|---- | -----|
| FULL | &quot;full&quot; |
| PARTIAL | &quot;partial&quot; |



