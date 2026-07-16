

# BoostPostRequestTargeting

Same geo/demographic fields as the `TargetingSpec` used by /v1/ads/create. Geo keys (`regions`/`cities`/`zips`/`metros`) resolve via GET /v1/ads/targeting/search?dimension=geo. City radius and lat/lng `customLocations` are Meta-only and preserve the boosted post's social proof (the ad references the existing post). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ageMin** | **Integer** |  |  [optional] |
|**ageMax** | **Integer** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | Meta only. |  [optional] |
|**languages** | **List&lt;String&gt;** | Meta locale ids (numeric), passed through as given. |  [optional] |
|**countries** | **List&lt;String&gt;** | ISO country codes. Required for TikTok boosts (TikTok&#39;s ad group requires location_ids); optional on other platforms. |  [optional] |
|**regions** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) | Region/state targeting. &#x60;key&#x60; from /v1/ads/targeting/search?dimension&#x3D;geo&amp;geoType&#x3D;region. |  [optional] |
|**cities** | [**List&lt;BoostPostRequestTargetingCitiesInner&gt;**](BoostPostRequestTargetingCitiesInner.md) | City targeting. Optional &#x60;radius&#x60; + &#x60;distance_unit&#x60; extend beyond the city limits (both set together, Meta only). |  [optional] |
|**zips** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) | Postal/ZIP targeting. &#x60;key&#x60; is the platform&#39;s postal location ID (e.g. Meta &#x60;US:94304&#x60;). |  [optional] |
|**metros** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) | DMA / metro-area targeting. &#x60;key&#x60; is the platform&#39;s metro ID (e.g. Meta &#x60;DMA:807&#x60;). |  [optional] |
|**customLocations** | [**List&lt;BoostPostRequestTargetingCustomLocationsInner&gt;**](BoostPostRequestTargetingCustomLocationsInner.md) | Point-radius (lat/lng) targeting (Meta custom_locations). No geo &#x60;key&#x60; lookup needed. |  [optional] |
|**interests** | [**List&lt;UpdateAdRequestTargetingInterestsInner&gt;**](UpdateAdRequestTargetingInterestsInner.md) | Interest objects from /v1/ads/interests. Each must include id and name. |  [optional] |
|**advantageAudience** | [**AdvantageAudienceEnum**](#AdvantageAudienceEnum) | Meta only. 0 &#x3D; disabled (default), 1 &#x3D; enabled. |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



## Enum: AdvantageAudienceEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



