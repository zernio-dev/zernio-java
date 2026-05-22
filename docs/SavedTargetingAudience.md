

# SavedTargetingAudience

A reusable, stored TargetingSpec. No member upload step, no adAccountId, the spec is the audience. Reference it later via `savedTargetingId` on POST /v1/ads/create.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**accountId** | **String** | Social account ID on the target ad platform. |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**spec** | [**TargetingSpec**](TargetingSpec.md) | The targeting spec to store. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SAVED_TARGETING | &quot;saved_targeting&quot; |



