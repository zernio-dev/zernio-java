

# ListAdSets200ResponseAdSetsInnerTargeting

The audience this ad set delivers to, as the platform reports it at the last sync. LinkedIn and Meta; null for every other platform and for ad sets not yet re-synced.  On Meta it is the ad set's `targeting` verbatim (snake_case: geo_locations, age_min, custom_audiences, flexible_spec, ...), so it can be read, edited and sent back as is. On LinkedIn `include` and `exclude` (below) are the campaign's `targetingCriteria` verbatim, without reconstructing them from our normalized targeting spec. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**include** | **Object** | LinkedIn &#x60;targetingCriteria.include&#x60;, verbatim (an &#x60;and&#x60; of &#x60;or&#x60; facet clauses). |  [optional] |
|**exclude** | **Object** | LinkedIn &#x60;targetingCriteria.exclude&#x60;, verbatim. Absent when the campaign excludes nothing. |  [optional] |
|**audienceExpansionEnabled** | **Boolean** | LinkedIn audience expansion: whether LinkedIn may also serve to members similar to the criteria. |  [optional] |
|**offsiteDeliveryEnabled** | **Boolean** | Whether the campaign may deliver on the LinkedIn Audience Network, off LinkedIn itself. |  [optional] |



