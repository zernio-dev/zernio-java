

# ListEmailSendAs200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_list** | [**ListEnum**](#ListEnum) | &#x60;provider&#x60;: the provider lists every address (Gmail), nothing can be declared. &#x60;partial&#x60;: declare the addresses the provider cannot list (Outlook). |  [optional] |
|**providerSignatures** | **Boolean** | Whether the provider&#39;s own signatures appear here (Gmail). |  [optional] |



## Enum: ListEnum

| Name | Value |
|---- | -----|
| PROVIDER | &quot;provider&quot; |
| PARTIAL | &quot;partial&quot; |



