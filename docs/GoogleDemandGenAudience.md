

# GoogleDemandGenAudience

Created as a Google Audience and attached to the ad group. Send at least one dimension. Ids are numeric Google ids (user lists, interest categories, custom audiences) from the same customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userLists** | **List&lt;String&gt;** |  |  [optional] |
|**userInterests** | **List&lt;String&gt;** |  |  [optional] |
|**customAudiences** | **List&lt;String&gt;** |  |  [optional] |
|**ageRanges** | [**List&lt;GoogleDemandGenAudienceAgeRangesInner&gt;**](GoogleDemandGenAudienceAgeRangesInner.md) |  |  [optional] |
|**genders** | [**List&lt;GendersEnum&gt;**](#List&lt;GendersEnum&gt;) |  |  [optional] |



## Enum: List&lt;GendersEnum&gt;

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |
| UNDETERMINED | &quot;undetermined&quot; |



