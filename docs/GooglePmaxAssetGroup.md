

# GooglePmaxAssetGroup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Stable Google asset group id. Use it in the asset-group endpoints below. |  |
|**resourceName** | **String** | customers/{customerId}/assetGroups/{assetGroupId} |  |
|**campaignId** | **String** |  |  |
|**name** | **String** |  |  |
|**status** | **String** | Asset-group status on Google. Campaign status independently controls delivery. |  |
|**finalUrls** | **List&lt;URI&gt;** |  |  |
|**finalMobileUrls** | **List&lt;URI&gt;** |  |  |
|**path1** | **String** |  |  |
|**path2** | **String** |  |  |
|**adStrength** | **String** | Google ad strength, such as POOR, AVERAGE, GOOD or EXCELLENT. |  |
|**primaryStatus** | **String** | Why the group is or is not serving, such as ELIGIBLE, PAUSED or NOT_ELIGIBLE. |  |
|**primaryStatusReasons** | **List&lt;String&gt;** |  |  |
|**assets** | [**List&lt;GooglePmaxAssetGroupAssetsInner&gt;**](GooglePmaxAssetGroupAssetsInner.md) |  |  |



