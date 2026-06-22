

# SearchAdTargeting200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The platform&#39;s opaque id. Use as a geo &#x60;key&#x60; (regions/cities/zips/metros) or an entity &#x60;id&#x60; (interests/behaviors) in TargetingSpec. |  |
|**name** | **String** | Human-readable label. |  |
|**type** | **String** | What the result is (e.g. city, region, country, zip, metro, interest, behavior, income). |  |
|**path** | **List&lt;String&gt;** | Optional breadcrumb of parent labels (e.g. [&#39;United States&#39;, &#39;California&#39;, &#39;Los Angeles&#39;]). Disambiguates same-named results. |  [optional] |
|**audienceSize** | **Integer** | Optional estimated reachable users for this option, when the platform returns it. |  [optional] |
|**latitude** | **Float** | Centre latitude of the location. Populated on Meta geo results (city, neighborhood, place, etc.). Useful for map views. |  [optional] |
|**longitude** | **Float** | Centre longitude of the location. |  [optional] |



