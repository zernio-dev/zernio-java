

# ConversionEventCampaign

The ad campaign behind the event, when you know it. Read only by `POST /v1/events`, which ties the event to the campaign named by `campaign.id`, then by the `utm_campaign` of `sourceUrl`, then by `campaign.name`. See its Storage notes for how the event then counts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform campaign ID. |  [optional] |
|**name** | **String** | Campaign name as it appears on the ad platform (case-insensitive). |  [optional] |



