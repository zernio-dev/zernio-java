

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
|**consentMode** | **TrackingSiteConsentMode** |  |  [optional] |
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



