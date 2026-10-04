

# GetFacebookDemographics200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) |  |  [optional] |
|**snapshotDate** | **LocalDate** | Date of Meta&#39;s snapshot (YYYY-MM-DD), or null when Meta has no snapshot yet. |  [optional] |
|**demographics** | [**GetFacebookDemographics200ResponseDemographics**](GetFacebookDemographics200ResponseDemographics.md) |  |  [optional] |
|**note** | **String** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| FOLLOWER_DEMOGRAPHICS | &quot;follower_demographics&quot; |



