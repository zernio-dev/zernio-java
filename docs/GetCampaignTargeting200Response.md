

# GetCampaignTargeting200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**devices** | [**List&lt;GetCampaignTargeting200ResponseDevicesInner&gt;**](GetCampaignTargeting200ResponseDevicesInner.md) |  |  [optional] |
|**locations** | [**List&lt;GetCampaignTargeting200ResponseLocationsInner&gt;**](GetCampaignTargeting200ResponseLocationsInner.md) |  |  [optional] |
|**languages** | [**List&lt;GetCampaignTargeting200ResponseLanguagesInner&gt;**](GetCampaignTargeting200ResponseLanguagesInner.md) |  |  [optional] |
|**cachedAt** | **OffsetDateTime** | When this targeting was fetched from Google. Null when it was never served from cache. |  [optional] |
|**stale** | **Boolean** | True when Google&#39;s daily API quota was exhausted and this is the last successful fetch, not a live read. |  [optional] |



