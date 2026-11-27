

# CreateGoogleAssetGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stage** | **Boolean** | Send true to store this write as a staged change instead of applying it. The response is &#x60;202&#x60; with the change, and POST /v1/ads/changes/{changeId}/confirm applies it later. Cannot be combined with &#x60;validateOnly&#x60;. |  [optional] |
|**name** | **String** | Unique within the campaign. |  |
|**finalUrls** | **List&lt;URI&gt;** |  |  |
|**finalMobileUrls** | **List&lt;URI&gt;** |  |  [optional] |
|**path1** | **String** |  |  [optional] |
|**path2** | **String** | Requires path1. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**assets** | [**List&lt;GoogleAssetGroupAssetLink&gt;**](GoogleAssetGroupAssetLink.md) |  |  [optional] |
|**listingGroupFilter** | [**GoogleListingGroupTree**](GoogleListingGroupTree.md) |  |  [optional] |
|**validateOnly** | **Boolean** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| PAUSED | &quot;PAUSED&quot; |



