

# UpdateCampaignTargeting200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignId** | **String** |  |  [optional] |
|**adGroupId** | **String** | Demand Gen only: the ad group that received the locations and languages. |  [optional] |
|**updated** | [**List&lt;UpdatedEnum&gt;**](#List&lt;UpdatedEnum&gt;) | Which targeting fields were applied. |  [optional] |
|**locationTargetingType** | [**LocationTargetingTypeEnum**](#LocationTargetingTypeEnum) | The value read back from Google after the edit. |  [optional] |
|**devices** | [**List&lt;UpdateCampaignTargeting200ResponseDevicesInner&gt;**](UpdateCampaignTargeting200ResponseDevicesInner.md) |  |  [optional] |
|**locations** | [**List&lt;UpdateCampaignTargeting200ResponseLocationsInner&gt;**](UpdateCampaignTargeting200ResponseLocationsInner.md) |  |  [optional] |
|**excludedLocations** | [**List&lt;UpdateCampaignTargeting200ResponseExcludedLocationsInner&gt;**](UpdateCampaignTargeting200ResponseExcludedLocationsInner.md) | The negative (excluded) location criteria read back after the edit, same item shape as &#x60;locations&#x60;. |  [optional] |
|**languages** | [**List&lt;UpdateCampaignTargeting200ResponseLanguagesInner&gt;**](UpdateCampaignTargeting200ResponseLanguagesInner.md) |  |  [optional] |



## Enum: List&lt;UpdatedEnum&gt;

| Name | Value |
|---- | -----|
| DEVICES | &quot;devices&quot; |
| LOCATIONS | &quot;locations&quot; |
| EXCLUDED_LOCATIONS | &quot;excludedLocations&quot; |
| LANGUAGES | &quot;languages&quot; |
| LOCATION_TARGETING_TYPE | &quot;locationTargetingType&quot; |



## Enum: LocationTargetingTypeEnum

| Name | Value |
|---- | -----|
| PRESENCE | &quot;presence&quot; |
| PRESENCE_OR_INTEREST | &quot;presence_or_interest&quot; |



