

# GetAdAccountHealth200ResponseChecksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**title** | **String** |  |  |
|**message** | **String** |  |  |
|**code** | **String** | When the check is not &#x60;ok&#x60;: the error code a create refused for this reason returns. |  [optional] |
|**hint** | **String** |  |  [optional] |
|**fix** | [**GetAdAccountHealth200ResponseBlockersInnerFix**](GetAdAccountHealth200ResponseBlockersInnerFix.md) |  |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| ACCOUNT_STATUS | &quot;account_status&quot; |
| PAYMENT | &quot;payment&quot; |
| SPEND_CAP | &quot;spend_cap&quot; |
| PAGE | &quot;page&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| LEAD_TERMS | &quot;lead_terms&quot; |
| PIXEL | &quot;pixel&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| LAST_REFUSAL | &quot;last_refusal&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| WARNING | &quot;warning&quot; |
| ERROR | &quot;error&quot; |
| MISSING | &quot;missing&quot; |
| UNKNOWN | &quot;unknown&quot; |



