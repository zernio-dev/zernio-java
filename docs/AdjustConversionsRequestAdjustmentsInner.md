

# AdjustConversionsRequestAdjustmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustmentType** | [**AdjustmentTypeEnum**](#AdjustmentTypeEnum) |  |  |
|**adjustmentTime** | **BigDecimal** | When the adjustment occurred, unix seconds. |  |
|**orderId** | **String** | Transaction ID of the original conversion (the &#x60;eventId&#x60; you sent). Recommended; required for ENHANCEMENT. |  [optional] |
|**gclid** | **String** | Alternative key — the original click ID. Pair with &#x60;conversionTime&#x60;. Not valid for ENHANCEMENT. |  [optional] |
|**conversionTime** | **BigDecimal** | The original conversion&#39;s time, unix seconds. Required when identifying by &#x60;gclid&#x60;. |  [optional] |
|**restatementValue** | **BigDecimal** | RESTATEMENT only — the corrected TOTAL conversion value. |  [optional] |
|**currency** | **String** | RESTATEMENT only — ISO 4217 currency for &#x60;restatementValue&#x60;. |  [optional] |
|**user** | [**AdjustConversionsRequestAdjustmentsInnerUser**](AdjustConversionsRequestAdjustmentsInnerUser.md) |  |  [optional] |
|**userAgent** | **String** | ENHANCEMENT only — the original conversion&#39;s user agent (improves match quality). |  [optional] |



## Enum: AdjustmentTypeEnum

| Name | Value |
|---- | -----|
| RETRACTION | &quot;RETRACTION&quot; |
| RESTATEMENT | &quot;RESTATEMENT&quot; |
| ENHANCEMENT | &quot;ENHANCEMENT&quot; |



