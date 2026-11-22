

# TrackingSite


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**install** | [**TrackingSiteInstall**](TrackingSiteInstall.md) |  |  [optional] |
|**storeOrders** | **Boolean** | True when the store&#39;s orders reach Zernio from the store itself, so website purchases are forwarded but not counted twice. |  [optional] |
|**siteKey** | **String** | Public key that names the site in the snippet, such as &#x60;zs_...&#x60;. |  [optional] |
|**domains** | **List&lt;String&gt;** |  |  [optional] |
|**customHostname** | [**TrackingSiteCustomHostname**](TrackingSiteCustomHostname.md) |  |  [optional] |
|**proxy** | [**TrackingSiteProxy**](TrackingSiteProxy.md) |  |  [optional] |
|**googleTagIds** | **List&lt;String&gt;** | The site&#39;s own Google tags (Tag Manager, GA4, Google Ads) its own-domain path relays to Google, so they load and measure from the site&#39;s domain. |  [optional] |
|**consentMode** | **TrackingSiteConsentMode** |  |  [optional] |
|**pixels** | [**List&lt;TrackingSitePixel&gt;**](TrackingSitePixel.md) | The ad pixels the tag loads itself. In the EEA, UK and Switzerland none loads before the visitor accepts on the site&#39;s consent banner; elsewhere &#x60;consentMode&#x60; decides. |  [optional] |
|**consentModeBridge** | **Boolean** | The tag writes the answer on the site&#39;s consent banner into Google Consent Mode v2: denied by default in the EEA, UK and Switzerland, then updated. On for sites created from November 2026. |  [optional] |
|**checks** | [**List&lt;TrackingSiteChecksInner&gt;**](TrackingSiteChecksInner.md) | One per setup step: &#x60;script&#x60; for the install, then one per ad account the site sends to, keyed by its platform and ids. |  [optional] |
|**setup** | [**TrackingSiteSetup**](TrackingSiteSetup.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| REMOVING | &quot;removing&quot; |



