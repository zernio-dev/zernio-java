

# CreatePhoneNumberPortInRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumbers** | **List&lt;String&gt;** | E.164 numbers to port in. |  |
|**endUser** | [**CreatePhoneNumberPortInRequestEndUser**](CreatePhoneNumberPortInRequestEndUser.md) |  |  |
|**loaDocumentId** | **String** | Document id from POST /v1/phone-numbers/port-in/documents (kind&#x3D;loa). |  |
|**invoiceDocumentId** | **String** | Document id from POST /v1/phone-numbers/port-in/documents (kind&#x3D;invoice). |  |
|**focDatetimeRequested** | **OffsetDateTime** | Requested port date; the carrier confirms the actual FOC later. US/CA default is one week out (shifted off weekends); international orders are scheduled into the carrier&#39;s next allowed porting window at or after this date. |  [optional] |
|**customerReference** | **String** |  |  [optional] |
|**portType** | [**PortTypeEnum**](#PortTypeEnum) | Whether the losing account ports all its numbers (full) or keeps some (partial). |  [optional] |
|**requirements** | [**List&lt;CreatePhoneNumberPortInRequestRequirementsInner&gt;**](CreatePhoneNumberPortInRequestRequirementsInner.md) | Country-specific requirement values for international ports (from GET /v1/phone-numbers/port-in/requirements). Not needed for US/CA. The LOA and invoice requirements are satisfied automatically by loaDocumentId/invoiceDocumentId, and address-type requirements by the endUser service address. |  [optional] |



## Enum: PortTypeEnum

| Name | Value |
|---- | -----|
| FULL | &quot;full&quot; |
| PARTIAL | &quot;partial&quot; |



