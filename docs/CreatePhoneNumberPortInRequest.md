

# CreatePhoneNumberPortInRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumbers** | **List&lt;String&gt;** | E.164 numbers to port in. |  |
|**endUser** | [**CreatePhoneNumberPortInRequestEndUser**](CreatePhoneNumberPortInRequestEndUser.md) |  |  |
|**loaDocumentId** | **String** | Document id from POST /v1/phone-numbers/port-in/documents (kind&#x3D;loa). |  |
|**invoiceDocumentId** | **String** | Document id from POST /v1/phone-numbers/port-in/documents (kind&#x3D;invoice). |  |
|**focDatetimeRequested** | **OffsetDateTime** | Requested port date; the carrier confirms the actual FOC later. |  [optional] |
|**customerReference** | **String** |  |  [optional] |



