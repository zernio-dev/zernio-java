

# AdKeywordQuality

Google Quality Score and the three component ratings behind it (`ad_group_criterion.quality_info`). Every field is null until Google has rated the keyword: a keyword with too little traffic is unrated, and negatives are never rated. Google's own UNKNOWN / UNSPECIFIED buckets are reported as null so \"unrated\" has a single representation. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**score** | **Integer** | Quality Score, 1-10. |  [optional] |
|**expectedCtr** | [**ExpectedCtrEnum**](#ExpectedCtrEnum) | How the click-through rate compares with other ads in the same position (&#x60;search_predicted_ctr&#x60;). |  [optional] |
|**adRelevance** | [**AdRelevanceEnum**](#AdRelevanceEnum) | How closely the ad matches the intent behind the search (&#x60;creative_quality_score&#x60;). |  [optional] |
|**landingPageExperience** | [**LandingPageExperienceEnum**](#LandingPageExperienceEnum) | How relevant and useful the landing page is to people who click (&#x60;post_click_quality_score&#x60;). |  [optional] |



## Enum: ExpectedCtrEnum

| Name | Value |
|---- | -----|
| BELOW_AVERAGE | &quot;BELOW_AVERAGE&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| ABOVE_AVERAGE | &quot;ABOVE_AVERAGE&quot; |



## Enum: AdRelevanceEnum

| Name | Value |
|---- | -----|
| BELOW_AVERAGE | &quot;BELOW_AVERAGE&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| ABOVE_AVERAGE | &quot;ABOVE_AVERAGE&quot; |



## Enum: LandingPageExperienceEnum

| Name | Value |
|---- | -----|
| BELOW_AVERAGE | &quot;BELOW_AVERAGE&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| ABOVE_AVERAGE | &quot;ABOVE_AVERAGE&quot; |



