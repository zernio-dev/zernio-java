

# MetaDatasetAudit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  |
|**adAccountId** | **String** |  |  |
|**dataset** | [**MetaDatasetAuditDataset**](MetaDatasetAuditDataset.md) |  |  |
|**datasets** | [**List&lt;MetaDatasetAuditDatasetsInner&gt;**](MetaDatasetAuditDatasetsInner.md) | Every pixel assigned to the ad account. |  |
|**window** | [**MetaDatasetAuditWindow**](MetaDatasetAuditWindow.md) |  |  |
|**events** | [**List&lt;MetaDatasetAuditEventsInner&gt;**](MetaDatasetAuditEventsInner.md) | One entry per event Meta counted in the window or scored, busiest first. |  |
|**findings** | [**List&lt;MetaDatasetAuditFindingsInner&gt;**](MetaDatasetAuditFindingsInner.md) | Problems the numbers show, most damaging first. |  |
|**unavailable** | [**List&lt;MetaDatasetAuditUnavailableInner&gt;**](MetaDatasetAuditUnavailableInner.md) | What the audit could not read, and why. |  |
|**checkedAt** | **OffsetDateTime** |  |  |



