

# CreateStandaloneAdRequestCitiesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Meta city ID, from /v1/ads/targeting/search results. |  |
|**radius** | **BigDecimal** | Optional radius around the city. Must be set together with distance_unit. |  [optional] |
|**distanceUnit** | [**DistanceUnitEnum**](#DistanceUnitEnum) | Unit for radius. Required if radius is set. |  [optional] |



## Enum: DistanceUnitEnum

| Name | Value |
|---- | -----|
| MILE | &quot;mile&quot; |
| KILOMETER | &quot;kilometer&quot; |



