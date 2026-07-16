

# TargetingSpec

Normalized, platform-agnostic ad-targeting spec. Every field is optional, an empty object targets the platform's default broadest audience. Field names are camelCase and identical across `POST /v1/ads/create` (the `targeting` object), `POST /v1/ads/targeting/reach-estimate`, and `saved_targeting` audiences, so a spec resolved once can be reused verbatim.  Entity ids (`regions[].key`, `cities[].key`, `zips[].key`, `metros[].key`, `interests[].id`, `behaviors[].id`) are the platform's opaque identifiers resolved via `GET /v1/ads/targeting/search`. A spec is therefore meaningful only for the platform it was built against, except the portable fields (`countries`, `ageMin`/`ageMax`, `gender`, `incomeTier`, `languages`) which carry across platforms. Fields a platform cannot honour are rejected at create time with `INVALID_FIELD_VALUE` naming the offending field (not silently dropped). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countries** | **List&lt;String&gt;** | ISO 3166-1 alpha-2 country codes (e.g. [&#39;US&#39;]). |  [optional] |
|**regions** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) | Region/state targeting. &#x60;key&#x60; is the platform location ID from /v1/ads/targeting/search?dimension&#x3D;geo&amp;geoType&#x3D;region. |  [optional] |
|**cities** | [**List&lt;TargetingSpecCitiesInner&gt;**](TargetingSpecCitiesInner.md) | City targeting. Optional &#x60;radius&#x60; + &#x60;distance_unit&#x60; extend beyond the city limits; both must be set together or both omitted. &#x60;radius&#x60; is only honoured on platforms whose capability map allows city radius (Meta). |  [optional] |
|**zips** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) | Postal/ZIP targeting. &#x60;key&#x60; is the platform&#39;s postal location ID (e.g. Meta &#x60;US:94304&#x60;). Supported on Meta, Google, TikTok, Pinterest, X. |  [optional] |
|**metros** | [**List&lt;BoostPostRequestTargetingRegionsInner&gt;**](BoostPostRequestTargetingRegionsInner.md) | DMA / metro-area targeting. &#x60;key&#x60; is the platform&#39;s metro ID (e.g. Meta &#x60;DMA:807&#x60;). |  [optional] |
|**customLocations** | [**List&lt;TargetingSpecCustomLocationsInner&gt;**](TargetingSpecCustomLocationsInner.md) | Point-radius (lat/lng) targeting (Meta custom_locations / Google proximity). Honoured only where the capability map allows radius (Meta). |  [optional] |
|**excludedLocations** | [**TargetingSpecExcludedLocations**](TargetingSpecExcludedLocations.md) |  |  [optional] |
|**ageMin** | **Integer** |  |  [optional] |
|**ageMax** | **Integer** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | Restrict by gender. &#39;all&#39; (default) targets everyone. |  [optional] |
|**incomeTier** | [**IncomeTierEnum**](#IncomeTierEnum) | Normalized household-income tier (ZIP/percentile based). Meta and TikTok express all four. Google maps only &#x60;top_10&#x60; (its INCOME_RANGE_90_UP); other tiers on Google, and any income tier on LinkedIn / X / Pinterest, are rejected. On Meta, income/zip targeting requires the relevant &#x60;specialAdCategories&#x60; to be unset (housing/employment/credit ads cannot use it).  |  [optional] |
|**languages** | **List&lt;String&gt;** | Language codes (e.g. [&#39;en&#39;]). |  [optional] |
|**interests** | [**List&lt;CreateStandaloneAdRequestBehaviorsInner&gt;**](CreateStandaloneAdRequestBehaviorsInner.md) | Interest entities from /v1/ads/targeting/search?dimension&#x3D;interest. Each carries the platform&#39;s opaque id. |  [optional] |
|**behaviors** | [**List&lt;CreateStandaloneAdRequestBehaviorsInner&gt;**](CreateStandaloneAdRequestBehaviorsInner.md) | Behaviour entities from /v1/ads/targeting/search?dimension&#x3D;behavior. Supported on Meta and TikTok. |  [optional] |
|**industries** | **List&lt;String&gt;** | LinkedIn B2B only. Industry URN id fragments. |  [optional] |
|**companySizes** | **List&lt;String&gt;** | LinkedIn B2B only. |  [optional] |
|**seniorities** | **List&lt;String&gt;** | LinkedIn B2B only. |  [optional] |
|**jobFunctions** | **List&lt;String&gt;** | LinkedIn B2B only. |  [optional] |
|**audienceInclude** | **List&lt;String&gt;** | Platform audience IDs to include. |  [optional] |
|**audienceExclude** | **List&lt;String&gt;** | Platform audience IDs to exclude. |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



## Enum: IncomeTierEnum

| Name | Value |
|---- | -----|
| TOP_5 | &quot;top_5&quot; |
| TOP_10 | &quot;top_10&quot; |
| TOP_10_25 | &quot;top_10_25&quot; |
| TOP_25_50 | &quot;top_25_50&quot; |



