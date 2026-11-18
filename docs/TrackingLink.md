

# TrackingLink


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**code** | **String** | The short code in &#x60;url&#x60;, such as &#x60;aB3dE5fG&#x60;. Unique across Zernio. |  [optional] |
|**siteId** | **String** | The tracking site the link belongs to. |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**destinations** | [**List&lt;TrackingLinkDestination&gt;**](TrackingLinkDestination.md) |  |  [optional] |
|**campaign** | [**TrackingLinkCampaign**](TrackingLinkCampaign.md) |  |  [optional] |
|**url** | **String** | The link to put in ads, such as &#x60;https://t.brand.com/r/aB3dE5fG&#x60;. It uses the site&#39;s custom subdomain once that is active. |  [optional] |
|**postbackUrl** | **String** | The server-to-server postback URL to give the network. Replace &#x60;{clickid}&#x60;, &#x60;{payout}&#x60; and &#x60;{txid}&#x60; with the network&#39;s own macros. It holds a secret: rotate it with &#x60;POST /v1/tracking-links/{linkId}/rotate-postback-token&#x60; if it leaks. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



