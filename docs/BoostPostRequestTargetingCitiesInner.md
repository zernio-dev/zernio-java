

# BoostPostRequestTargetingCitiesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** |  |  |
|**name** | **String** |  |  [optional] |
|**radius** | **BigDecimal** | Requires distanceUnit. Meta enforces a minimum city radius (~17 km / 10 mi); smaller values resolve to a 0-size audience and the ad fails at launch. For a tighter catchment use customLocations (lat/lng). |  [optional] |
|**distanceUnit** | [**DistanceUnitEnum**](#DistanceUnitEnum) |  |  [optional] |



## Enum: DistanceUnitEnum

| Name | Value |
|---- | -----|
| MILE | &quot;mile&quot; |
| KILOMETER | &quot;kilometer&quot; |



