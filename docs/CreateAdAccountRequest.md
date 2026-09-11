

# CreateAdAccountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio metaads SocialAccount ID. |  |
|**businessId** | **String** | Business portfolio that will own the account. |  |
|**name** | **String** | Ad account name. Whitespace is trimmed. |  |
|**currency** | **String** | Uppercase ISO 4217 currency supported by Meta. |  |
|**timezoneId** | **Integer** | Numeric Meta timezone ID from the linked timezone list. For example 1 is America/Los_Angeles. |  |
|**endAdvertiser** | **String** | End advertiser business or page ID. NONE uses the owning business. |  [optional] |
|**mediaAgency** | **String** | Media agency business or page ID. NONE for self-serve customers. |  [optional] |
|**partner** | **String** | Partner business or page ID. NONE for self-serve customers. |  [optional] |
|**invoice** | **Boolean** | Request Meta invoicing. Eligibility is determined by Meta. |  [optional] |
|**invoiceGroupId** | **String** | Existing Meta invoice group ID. |  [optional] |
|**invoicingEmails** | **List&lt;String&gt;** | Addresses for Meta invoices. |  [optional] |
|**io** | **Boolean** | Meta insertion-order invoicing option. |  [optional] |
|**poNumber** | **String** | Purchase order number. |  [optional] |
|**fundingId** | **String** | Existing Meta funding reference. Does not add a payment method. |  [optional] |
|**adAccountCreatedFromBmFlag** | **Boolean** | Meta Business Manager creation flag. |  [optional] |



