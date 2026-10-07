

# GetAdAccountLiveEntities200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** |  |  [optional] |
|**adAccountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**currency** | **String** | ISO 4217 code every budget and bid amount is expressed in. |  [optional] |
|**readAt** | **OffsetDateTime** | When the platform was read. |  [optional] |
|**campaigns** | [**List&lt;GetAdAccountLiveEntities200ResponseCampaignsInner&gt;**](GetAdAccountLiveEntities200ResponseCampaignsInner.md) | Absent when &#x60;level&#x3D;adSet&#x60;. |  [optional] |
|**adSets** | [**List&lt;GetAdAccountLiveEntities200ResponseAdSetsInner&gt;**](GetAdAccountLiveEntities200ResponseAdSetsInner.md) | Absent when &#x60;level&#x3D;campaign&#x60;. |  [optional] |
|**paging** | [**GetAdAccountLiveEntities200ResponsePaging**](GetAdAccountLiveEntities200ResponsePaging.md) |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| TIKTOK | &quot;tiktok&quot; |



