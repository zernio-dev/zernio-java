

# SavedTargetingAudience

A reusable, stored TargetingSpec. No member upload step, no adAccountId, the spec is the audience. Reference it later via `savedTargetingId` on POST /v1/ads/create.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**accountId** | **String** | Account ID on the target ad platform. |  |
|**name** | **String** |  |  |
|**description** | **String** |  |  [optional] |
|**spec** | [**TargetingSpec**](TargetingSpec.md) | The targeting spec to store. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SAVED_TARGETING | &quot;saved_targeting&quot; |



