

# ConversionAuditReportServerSide


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**signals** | [**List&lt;ConversionAuditReportServerSideSignalsInner&gt;**](ConversionAuditReportServerSideSignalsInner.md) |  |  |
|**note** | **String** |  |  |
|**firstPartyCollection** | **String** | The server-side path that collects on the site&#39;s own domain, when the scan saw one. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DETECTED | &quot;detected&quot; |
| LIKELY | &quot;likely&quot; |
| NOT_VISIBLE | &quot;not-visible&quot; |



