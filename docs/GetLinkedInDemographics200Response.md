

# GetLinkedInDemographics200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) |  |  [optional] |
|**demographics** | **Map&lt;String, List&lt;GetLinkedInDemographics200ResponseDemographicsValueInner&gt;&gt;** | Only the requested breakdowns are present. Entries are sorted by value, largest first. |  [optional] |
|**note** | **String** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| LINKEDIN | &quot;linkedin&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| FOLLOWER_DEMOGRAPHICS | &quot;follower_demographics&quot; |



