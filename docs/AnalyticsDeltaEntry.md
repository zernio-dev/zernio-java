

# AnalyticsDeltaEntry

One changed analytics snapshot. Metrics are the absolute values recorded at `syncedAt`, not the amount they moved by since the previous snapshot, so a later entry for the same `postId` always supersedes an earlier one. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postId** | **String** | External post ID. The same identifier as &#x60;posts[]._id&#x60; in GET /v1/analytics. |  |
|**accountId** | **String** | Social account this post was published through |  |
|**profileId** | **String** | Profile the account belongs to |  |
|**platform** | **String** |  |  |
|**platformPostId** | **String** | Platform-side post ID (for example the YouTube video ID) |  |
|**publishedAt** | **OffsetDateTime** | When the post was published, ISO-8601 UTC |  |
|**syncedAt** | **OffsetDateTime** | When the sync cycle that produced this snapshot STARTED, ISO-8601 UTC. This is NOT the order entries arrive in and it is not a resume point: a slow cycle writes its rows after a faster cycle that started later, so &#x60;syncedAt&#x60; can go backwards between consecutive entries. Use &#x60;nextCursor&#x60; to resume.  |  |
|**isDeleted** | **Boolean** | True when the post was detected as deleted on the platform at this sync |  |
|**metrics** | [**AnalyticsDeltaEntryMetrics**](AnalyticsDeltaEntryMetrics.md) |  |  |



