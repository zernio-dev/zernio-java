

# GetCampaignAnalytics200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaign** | [**GetCampaignAnalytics200ResponseCampaign**](GetCampaignAnalytics200ResponseCampaign.md) |  |  [optional] |
|**backfillPending** | **Boolean** | Present and true only on &#x60;202&#x60; responses: part of the requested date range is still being backfilled from the platform in the background. Retry the same request shortly; it returns 200 once the range is fully ingested. |  [optional] |
|**analytics** | [**GetCampaignAnalytics200ResponseAnalytics**](GetCampaignAnalytics200ResponseAnalytics.md) |  |  [optional] |



