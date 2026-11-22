

# MetaDatasetAuditEventsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**last7Days** | **Integer** |  |  |
|**last24Hours** | **Integer** |  |  |
|**lastSeenHour** | **OffsetDateTime** | Start of the last hour Meta counted the event in: Meta&#39;s stats are hourly. |  |
|**daily** | [**List&lt;MetaDatasetAuditEventsInnerDailyInner&gt;**](MetaDatasetAuditEventsInnerDailyInner.md) |  |  |
|**serverSharePct** | **BigDecimal** | Percent of the window&#39;s events received through the Conversions API. Null when not measured (only the 12 busiest events are split by source). |  |
|**matchQuality** | **BigDecimal** | Event Match Quality, 0 to 10. Meta rates 6 and above as good. |  |
|**matchKeys** | [**List&lt;MetaDatasetAuditEventsInnerMatchKeysInner&gt;**](MetaDatasetAuditEventsInnerMatchKeysInner.md) |  |  |
|**diagnostics** | [**List&lt;MetaDatasetAuditEventsInnerDiagnosticsInner&gt;**](MetaDatasetAuditEventsInnerDiagnosticsInner.md) |  |  |
|**dedup** | [**List&lt;MetaDatasetAuditEventsInnerDedupInner&gt;**](MetaDatasetAuditEventsInnerDedupInner.md) | Per deduplication key, the share of browser and server copies carrying it and of browser copies Meta paired through it. |  |



