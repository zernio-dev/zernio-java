

# ConversionEventUserClickIds

Platform click identifiers captured from the originating ad click.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fbc** | **String** | Meta click ID (from fbclid URL param). |  [optional] |
|**fbp** | **String** | Meta browser ID (_fbp cookie). |  [optional] |
|**gclid** | **String** | Google click ID (from gclid URL param). |  [optional] |
|**gbraid** | **String** | Google iOS 14.5+ app attribution ID. |  [optional] |
|**wbraid** | **String** | Google iOS 14.5+ web-to-app attribution ID. |  [optional] |
|**liFatId** | **String** | LinkedIn first-party ad tracking click ID. Captured by parsing &#x60;li_fat_id&#x60; from landing-page URLs after the advertiser enables enhanced conversion tracking on the LinkedIn Insight Tag. Sent to LinkedIn as the LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID userId. Opaque token, not hashed.  |  [optional] |
|**epik** | **String** | Pinterest click ID (the &#x60;epik&#x60; URL param or &#x60;_epik&#x60; cookie). Sent to Pinterest as &#x60;click_id&#x60;, not hashed. |  [optional] |
|**rdtCid** | **String** | Reddit click ID (the &#x60;rdt_cid&#x60; URL param Reddit adds to ad clicks). Sent to Reddit as &#x60;click_id&#x60;, not hashed. |  [optional] |
|**rdtUuid** | **String** | Reddit Pixel browser id (the &#x60;_rdt_uuid&#x60; first-party cookie). Sent to Reddit as &#x60;user.uuid&#x60;, not hashed. |  [optional] |
|**aleid** | **String** | Axon (AppLovin) click id (the &#x60;aleid&#x60; URL param Axon adds to ad clicks, kept by its pixel in the &#x60;_axeid&#x60; cookie). Sent to Axon as &#x60;user_data.aleid&#x60;, not hashed. |  [optional] |
|**alart** | **String** | Axon (AppLovin) attribution token (the &#x60;alart&#x60; URL param, &#x60;_axart&#x60; cookie). Sent to Axon as &#x60;user_data.alart&#x60;, not hashed. |  [optional] |
|**axwrt** | **String** | Axon Pixel browser id (the &#x60;_axwrt&#x60; cookie). Sent to Axon as &#x60;user_data.axwrt&#x60;, not hashed. |  [optional] |
|**twclid** | **String** | X click ID (the &#x60;twclid&#x60; URL param X adds to ad clicks). Sent to X as a &#x60;twclid&#x60; identifier, not hashed. |  [optional] |
|**msclkid** | **String** | Microsoft Advertising click ID (the &#x60;msclkid&#x60; URL param Microsoft adds to ad clicks). Sent to Microsoft as &#x60;MicrosoftClickId&#x60; (offline goals) or &#x60;userData.msclkid&#x60; (UET tags), not hashed. |  [optional] |
|**sccid** | **String** | Snapchat click ID (the &#x60;ScCid&#x60; URL param Snap adds to ad clicks). Sent to Snapchat as &#x60;sc_click_id&#x60;, not hashed. |  [optional] |
|**scid** | **String** | Snap Pixel browser id (the &#x60;_scid&#x60; cookie). Sent to Snapchat as &#x60;sc_cookie1&#x60;, not hashed. |  [optional] |
|**irclickid** | **String** | Impact partner click id (the &#x60;irclickid&#x60; URL param Impact adds to partner links). Sent to Impact as &#x60;ClickId&#x60;. |  [optional] |
|**awc** | **String** | Awin click id (the &#x60;awc&#x60; URL param Awin adds to publisher links). Sent to Awin as the order&#39;s &#x60;awc&#x60;. |  [optional] |
|**dclid** | **String** | Campaign Manager 360 / Display &amp; Video 360 click ID (the &#x60;dclid&#x60; URL param). Sent to Floodlight as is. |  [optional] |
|**tdid** | **String** | The Trade Desk browser id (TDID) from a TTD cookie sync. Sent to The Trade Desk as &#x60;adid&#x60; of type &#x60;TDID&#x60;. |  [optional] |
|**uid2** | **String** | A raw UID2 for the person, from your UID2 integration. Sent to The Trade Desk as &#x60;adid&#x60; of type &#x60;UID2&#x60;. |  [optional] |
|**uid2Token** | **String** | A UID2 token (encrypted, from the UID2 SDK on your site). Sent to The Trade Desk as &#x60;uid2_token&#x60;. |  [optional] |



