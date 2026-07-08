

# ListAdAudiences200ResponseAudiencesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**accountId** | **String** | Social account the audience was created against. Returned for saved_targeting items. |  [optional] |
|**platformAudienceId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**spec** | [**TargetingSpec**](TargetingSpec.md) |  |  [optional] |
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



