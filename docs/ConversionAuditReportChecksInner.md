

# ConversionAuditReportChecksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable check id, such as &#x60;pixels&#x60;, &#x60;server-side&#x60;, &#x60;first-party&#x60;, &#x60;consent&#x60;, &#x60;consent-timing&#x60; or &#x60;match-quality&#x60;. New checks can appear. |  |
|**title** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;unknown&#x60; &#x3D; the scan cannot see it from outside; &#x60;not-applicable&#x60; checks are left out of the score. |  |
|**tier** | [**TierEnum**](#TierEnum) | A &#x60;bonus&#x60; check can only add points, never cost them. |  [optional] |
|**weight** | **BigDecimal** |  |  |
|**detail** | **String** |  |  |
|**pointsToGain** | **BigDecimal** | Points the score gains when this check alone is fixed. |  [optional] |
|**verify** | [**ConversionAuditReportChecksInnerVerify**](ConversionAuditReportChecksInnerVerify.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PASS | &quot;pass&quot; |
| PARTIAL | &quot;partial&quot; |
| FAIL | &quot;fail&quot; |
| UNKNOWN | &quot;unknown&quot; |
| NOT_APPLICABLE | &quot;not-applicable&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| ESSENTIAL | &quot;essential&quot; |
| RECOMMENDED | &quot;recommended&quot; |
| BONUS | &quot;bonus&quot; |



