

# ListWhatsAppFlows200ResponseFlowsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**categories** | **List&lt;String&gt;** |  |  [optional] |
|**validationErrors** | **List&lt;Object&gt;** |  |  [optional] |
|**version** | **Integer** | 1-based version within the flow&#39;s clone lineage (Zernio-tracked; Meta has no native versioning). Standalone flows are version 1. |  [optional] |
|**lineageId** | **String** | Stable group key for the flow&#39;s version lineage (the root flow&#39;s ID). |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;DRAFT&quot; |
| PUBLISHED | &quot;PUBLISHED&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| BLOCKED | &quot;BLOCKED&quot; |
| THROTTLED | &quot;THROTTLED&quot; |



