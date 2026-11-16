

# UsageStatsProfile

Present with `profileId` / `externalId` on `GET /v1/usage-stats`: the per-profile counters. Everything outside this block stays team-level.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**externalId** | **String** | The externalId set on the profile, null when it has none. |  |
|**usage** | [**UsageStatsProfileAllOfUsage**](UsageStatsProfileAllOfUsage.md) |  |  [optional] |



