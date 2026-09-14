

# TargetingSpecExcludedLocations

Geo to exclude from the audience. Mirrors the inclusion geo shape: excluded cities can carry a radius catchment and excluded custom (lat/lng) pins are supported, both on Meta (excluded_geo_locations).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countries** | **List&lt;String&gt;** |  |  [optional] |
|**countryGroups** | [**List&lt;CountryGroupsEnum&gt;**](#List&lt;CountryGroupsEnum&gt;) | Meta only. Continents and trade blocs to exclude (&#x60;excluded_geo_locations.country_groups&#x60;). |  [optional] |
|**regions** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) |  |  [optional] |
|**cities** | [**List&lt;TargetingSpecExcludedLocationsCitiesInner&gt;**](TargetingSpecExcludedLocationsCitiesInner.md) | Cities to exclude. Optional &#x60;radius&#x60; + &#x60;distanceUnit&#x60; exclude a catchment around the city (both must be set together or both omitted); Meta honours the radius on excluded cities. |  [optional] |
|**zips** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) |  |  [optional] |
|**places** | [**List&lt;TargetingSpecExcludedLocationsPlacesInner&gt;**](TargetingSpecExcludedLocationsPlacesInner.md) | Named points of interest to exclude. &#x60;key&#x60; from /v1/ads/targeting/search. |  [optional] |
|**neighborhoods** | [**List&lt;TargetingSpecExcludedLocationsPlacesInner&gt;**](TargetingSpecExcludedLocationsPlacesInner.md) | Named neighbourhood areas to exclude. &#x60;key&#x60; from /v1/ads/targeting/search. |  [optional] |
|**customLocations** | [**List&lt;TargetingSpecCustomLocationsInner&gt;**](TargetingSpecCustomLocationsInner.md) | Point-radius (lat/lng) pins to exclude (Meta excluded_geo_locations.custom_locations). Mirrors the inclusion customLocations shape. |  [optional] |



## Enum: List&lt;CountryGroupsEnum&gt;

| Name | Value |
|---- | -----|
| AFRICA | &quot;africa&quot; |
| ASIA | &quot;asia&quot; |
| EUROPE | &quot;europe&quot; |
| NORTH_AMERICA | &quot;north_america&quot; |
| SOUTH_AMERICA | &quot;south_america&quot; |
| OCEANIA | &quot;oceania&quot; |
| CENTRAL_AMERICA | &quot;central_america&quot; |
| CARIBBEAN | &quot;caribbean&quot; |
| EEA | &quot;eea&quot; |
| EURO_AREA | &quot;euro_area&quot; |
| NAFTA | &quot;nafta&quot; |
| MERCOSUR | &quot;mercosur&quot; |
| AFTA | &quot;afta&quot; |
| APEC | &quot;apec&quot; |
| GCC | &quot;gcc&quot; |
| CISFTA | &quot;cisfta&quot; |
| EMERGING_MARKETS | &quot;emerging_markets&quot; |
| ITUNES_APP_STORE | &quot;itunes_app_store&quot; |
| ANDROID_FREE_STORE | &quot;android_free_store&quot; |
| ANDROID_PAID_STORE | &quot;android_paid_store&quot; |



