

# CreateGoogleAssetGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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



