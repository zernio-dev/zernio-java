

# TargetingSpecCitiesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** |  |  |
|**name** | **String** |  |  [optional] |
|**radius** | **BigDecimal** | Radius around the city. Requires distance_unit. |  [optional] |
|**distanceUnit** | [**DistanceUnitEnum**](#DistanceUnitEnum) | Required if radius is set. |  [optional] |



## Enum: DistanceUnitEnum

| Name | Value |
|---- | -----|
| MILE | &quot;mile&quot; |
| KILOMETER | &quot;kilometer&quot; |



