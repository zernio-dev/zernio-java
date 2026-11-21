

# ConversionAuditReportChecksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  |
|**title** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;unknown&#x60; &#x3D; the scan cannot see it from outside; &#x60;not-applicable&#x60; checks are left out of the score. |  |
|**tier** | [**TierEnum**](#TierEnum) | A &#x60;bonus&#x60; check can only add points, never cost them. |  [optional] |
|**weight** | **BigDecimal** |  |  |
|**detail** | **String** |  |  |
|**pointsToGain** | **BigDecimal** | Points the score gains when this check alone is fixed. |  [optional] |
|**verify** | [**ConversionAuditReportChecksInnerVerify**](ConversionAuditReportChecksInnerVerify.md) |  |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| PIXELS | &quot;pixels&quot; |
| SERVER_SIDE | &quot;server-side&quot; |
| FIRST_PARTY | &quot;first-party&quot; |
| CONSENT | &quot;consent&quot; |
| MATCH_QUALITY | &quot;match-quality&quot; |



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



