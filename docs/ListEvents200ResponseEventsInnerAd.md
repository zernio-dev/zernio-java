

# ListEvents200ResponseEventsInnerAd

The ad behind the event, when Zernio can name it. Google: from the click behind `clickIds.gclid` (synced daily from Google Ads click_view for clicks up to 14 days before the event; gbraid/wbraid clicks are not resolved). Meta: from the `zrn` ad id, for Meta ads Zernio holds. `null` otherwise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**customerId** | **String** | Google Ads customer id (Google only). |  [optional] |
|**campaignId** | **String** |  |  [optional] |
|**adGroupId** | **String** | Google only. |  [optional] |
|**adSetId** | **String** | Meta only. |  [optional] |
|**adId** | **String** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLEADS | &quot;googleads&quot; |
| METAADS | &quot;metaads&quot; |



