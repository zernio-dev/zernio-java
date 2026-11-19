

# StoredEventCampaign

The campaign behind the event and how Zernio knows it, with the names Zernio holds for its campaign, ad group or ad set and ad. `null` when nothing ties the event to a campaign; a Google click shows here the day after it, once Google reports it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**via** | [**ViaEnum**](#ViaEnum) | &#x60;google_click&#x60;: the click behind &#x60;clickIds.gclid&#x60;. &#x60;zernio_tag&#x60;: the &#x60;zrn&#x60; ad. &#x60;matched&#x60;: the campaign Zernio matched the event to. &#x60;utm&#x60;: only its &#x60;utm_campaign&#x60;, as &#x60;name&#x60;. |  [optional] |
|**id** | **String** | The ad platform campaign id; &#x60;null&#x60; for &#x60;utm&#x60;. |  [optional] |
|**name** | **String** |  |  [optional] |
|**adGroupName** | **String** | The Google ad group or Meta ad set. |  [optional] |
|**adName** | **String** |  |  [optional] |



## Enum: ViaEnum

| Name | Value |
|---- | -----|
| GOOGLE_CLICK | &quot;google_click&quot; |
| ZERNIO_TAG | &quot;zernio_tag&quot; |
| MATCHED | &quot;matched&quot; |
| UTM | &quot;utm&quot; |



