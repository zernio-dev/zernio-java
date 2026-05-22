

# ListAdAudiences200ResponseAudiencesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**platformAudienceId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**spec** | [**TargetingSpec**](TargetingSpec.md) | Present (and the only meaningful payload) when &#x60;type&#x60; is &#x60;saved_targeting&#x60;. Null for uploaded/derived audience types. |  [optional] |
|**platform** | **String** |  |  [optional] |
|**size** | **Integer** |  |  [optional] |
|**status** | **String** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_LIST | &quot;customer_list&quot; |
| WEBSITE | &quot;website&quot; |
| LOOKALIKE | &quot;lookalike&quot; |
| SAVED_TARGETING | &quot;saved_targeting&quot; |



