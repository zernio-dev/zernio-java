

# BulkUpdateAdCampaignStatus200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformCampaignId** | **String** |  |  [optional] |
|**platform** | **String** |  |  [optional] |
|**updated** | [**UpdatedEnum**](#UpdatedEnum) |  |  [optional] |
|**skipped** | [**SkippedEnum**](#SkippedEnum) |  |  [optional] |
|**platformCampaignStatus** | **String** | The campaign&#39;s own switch read back from the platform; null when it could not be read. |  [optional] |
|**error** | **String** |  |  [optional] |



## Enum: UpdatedEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



## Enum: SkippedEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



