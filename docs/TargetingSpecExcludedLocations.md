

# TargetingSpecExcludedLocations

Geo to exclude from the audience. Mirrors the inclusion geo shape: excluded cities can carry a radius catchment and excluded custom (lat/lng) pins are supported, both on Meta (excluded_geo_locations).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countries** | **List&lt;String&gt;** |  |  [optional] |
|**regions** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) |  |  [optional] |
|**cities** | [**List&lt;TargetingSpecExcludedLocationsCitiesInner&gt;**](TargetingSpecExcludedLocationsCitiesInner.md) | Cities to exclude. Optional &#x60;radius&#x60; + &#x60;distance_unit&#x60; exclude a catchment around the city (both must be set together or both omitted); Meta honours the radius on excluded cities. |  [optional] |
|**zips** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) |  |  [optional] |
|**places** | [**List&lt;TargetingSpecExcludedLocationsPlacesInner&gt;**](TargetingSpecExcludedLocationsPlacesInner.md) | Named points of interest to exclude. &#x60;key&#x60; from /v1/ads/targeting/search. |  [optional] |
|**neighborhoods** | [**List&lt;TargetingSpecExcludedLocationsPlacesInner&gt;**](TargetingSpecExcludedLocationsPlacesInner.md) | Named neighbourhood areas to exclude. &#x60;key&#x60; from /v1/ads/targeting/search. |  [optional] |
|**customLocations** | [**List&lt;TargetingSpecCustomLocationsInner&gt;**](TargetingSpecCustomLocationsInner.md) | Point-radius (lat/lng) pins to exclude (Meta excluded_geo_locations.custom_locations). Mirrors the inclusion customLocations shape. |  [optional] |



