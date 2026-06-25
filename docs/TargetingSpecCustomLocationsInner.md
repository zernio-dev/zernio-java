

# TargetingSpecCustomLocationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**latitude** | **BigDecimal** |  |  |
|**longitude** | **BigDecimal** |  |  |
|**radius** | **BigDecimal** | Positive radius around the point. |  |
|**distanceUnit** | [**DistanceUnitEnum**](#DistanceUnitEnum) |  |  |
|**name** | **String** |  |  [optional] |
|**address** | **String** | Optional label, sent to Meta as &#x60;address_string&#x60;. latitude/longitude take precedence for the pin location. |  [optional] |



## Enum: DistanceUnitEnum

| Name | Value |
|---- | -----|
| MILE | &quot;mile&quot; |
| KILOMETER | &quot;kilometer&quot; |



