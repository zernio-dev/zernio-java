

# CommerceCatalogSync

A store kept in sync with an ad-platform product catalog.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** | The store SocialAccount id. |  [optional] |
|**catalogPlatform** | [**CatalogPlatformEnum**](#CatalogPlatformEnum) |  |  [optional] |
|**catalogAccountId** | **String** | The Meta login account whose token writes to the catalog. |  [optional] |
|**catalogId** | **String** |  |  [optional] |
|**runStatus** | [**RunStatusEnum**](#RunStatusEnum) |  |  [optional] |
|**lastRunStartedAt** | **OffsetDateTime** |  |  [optional] |
|**lastRunFinishedAt** | **OffsetDateTime** |  |  [optional] |
|**lastError** | **String** | Why the last run failed, or how many items Meta rejected in a run that otherwise succeeded. Null after a clean run. |  [optional] |
|**itemsSent** | **Integer** | Catalog items (one per variant) Meta accepted in the last full run. |  [optional] |
|**itemsSkipped** | **Integer** | Products the last full run could not list: not published to the online store or without an image. |  [optional] |
|**itemsDeleted** | **Integer** | Items the last full run removed because the store no longer has them. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



## Enum: CatalogPlatformEnum

| Name | Value |
|---- | -----|
| META | &quot;meta&quot; |



## Enum: RunStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |



