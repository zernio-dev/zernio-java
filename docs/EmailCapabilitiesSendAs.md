

# EmailCapabilitiesSendAs


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_list** | [**ListEnum**](#ListEnum) | &#x60;provider&#x60;: &#x60;GET /v1/email/send-as&#x60; lists every address the provider accepts. &#x60;partial&#x60;: shared mailboxes are not listed and the provider decides at send time. |  [optional] |
|**sharedMailboxes** | **Boolean** |  |  [optional] |



## Enum: ListEnum

| Name | Value |
|---- | -----|
| PROVIDER | &quot;provider&quot; |
| PARTIAL | &quot;partial&quot; |
| DECLARED | &quot;declared&quot; |



