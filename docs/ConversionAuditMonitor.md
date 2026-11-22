

# ConversionAuditMonitor


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The monitor id. |  |
|**host** | **String** | The watched host, lowercase and without &#x60;www.&#x60;. |  |
|**reportUrl** | **String** | The host&#39;s public report on is-bleeding.com. |  |
|**score** | **Integer** | The score of the last check (0 to 100), or null before the first readable scan. |  |
|**grade** | **String** | The grade of the last check. |  |
|**scoreHistory** | [**List&lt;ConversionAuditMonitorScoreHistoryInner&gt;**](ConversionAuditMonitorScoreHistoryInner.md) | The score of each of the last 30 checks, oldest first. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**lastCheckedAt** | **OffsetDateTime** |  |  |
|**nextCheckAt** | **OffsetDateTime** | When the next daily check is due. |  |
|**lastAlertedAt** | **OffsetDateTime** | When the last alert email went out. |  |



