

# UpdateCampaignTargeting200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignId** | **String** |  |  [optional] |
|**updated** | [**List&lt;UpdatedEnum&gt;**](#List&lt;UpdatedEnum&gt;) | Which targeting fields were applied. |  [optional] |
|**devices** | [**List&lt;UpdateCampaignTargeting200ResponseDevicesInner&gt;**](UpdateCampaignTargeting200ResponseDevicesInner.md) |  |  [optional] |
|**locations** | [**List&lt;GetCampaignTargeting200ResponseLocationsInner&gt;**](GetCampaignTargeting200ResponseLocationsInner.md) |  |  [optional] |
|**languages** | [**List&lt;UpdateCampaignTargeting200ResponseLanguagesInner&gt;**](UpdateCampaignTargeting200ResponseLanguagesInner.md) |  |  [optional] |



## Enum: List&lt;UpdatedEnum&gt;

| Name | Value |
|---- | -----|
| DEVICES | &quot;devices&quot; |
| LOCATIONS | &quot;locations&quot; |
| LANGUAGES | &quot;languages&quot; |



