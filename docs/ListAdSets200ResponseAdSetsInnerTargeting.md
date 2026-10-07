

# ListAdSets200ResponseAdSetsInnerTargeting

The audience this ad set delivers to, as the platform reports it at the last sync, in the platform's own shape. Every platform; null only for an ad set not re-synced yet, or when the platform's targeting read failed on every sync so far (a failed read keeps the last stored value).  - Meta: the ad set's `targeting` verbatim (snake_case: geo_locations, age_min,   custom_audiences, flexible_spec, ...), so it can be read, edited and sent back as is. - LinkedIn: `include` and `exclude` (below) are the campaign's `targetingCriteria`   verbatim, without reconstructing them from our normalized targeting spec. - TikTok: the ad group's targeting fields from adgroup/get, verbatim (placement_type,   placements, location_ids, age_groups, gender, languages, interest_category_ids,   actions, audience_ids, excluded_audience_ids, operating_systems, ...). Only fields   TikTok returned are present. - Google: `campaignCriteria` (LOCATION, LANGUAGE, PROXIMITY, DEVICE, AGE_RANGE, GENDER,   USER_LIST, INCOME_RANGE, PARENTAL_STATUS) and `adGroupCriteria` (AGE_RANGE, GENDER,   USER_LIST, USER_INTEREST, INCOME_RANGE, PARENTAL_STATUS), each a Google criterion   verbatim (camelCase: resourceName, type, negative, bidModifier and the payload its type sets, for   example `location.geoTargetConstant`). Most Google targeting lives on the campaign,   so every ad group of a campaign carries the same `campaignCriteria`. Keywords are   not included (they have their own endpoints). Synced on Google's slower keyword cycle. - Pinterest: the ad group's `targeting_spec` verbatim (GEO, AGE_BUCKET, GENDER,   INTEREST, AUDIENCE_INCLUDE, LOCALE, ...). - X: `targeting_criteria`, the line item's criteria as X lists them (targeting_type,   targeting_value, operator_type, name), the same shape X's batch create takes. - OpenAI: the campaign's `targeting` (OpenAI targets at the campaign), plus the ad   group's `context_hints` when it has any. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**include** | **Object** | LinkedIn &#x60;targetingCriteria.include&#x60;, verbatim (an &#x60;and&#x60; of &#x60;or&#x60; facet clauses). |  [optional] |
|**exclude** | **Object** | LinkedIn &#x60;targetingCriteria.exclude&#x60;, verbatim. Absent when the campaign excludes nothing. |  [optional] |
|**audienceExpansionEnabled** | **Boolean** | LinkedIn audience expansion: whether LinkedIn may also serve to members similar to the criteria. |  [optional] |
|**offsiteDeliveryEnabled** | **Boolean** | Whether the campaign may deliver on the LinkedIn Audience Network, off LinkedIn itself. |  [optional] |



