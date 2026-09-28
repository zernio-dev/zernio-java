

# InstallTrackingTagOnStore200ResponseInstall


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storeAccountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**shopDomain** | **String** |  |  [optional] |
|**installed** | **Boolean** | True when this tag is the pixel the store fires. |  [optional] |
|**installedTagId** | **String** | The Meta pixel the store fires now (may be a different tag), or null. |  [optional] |
|**webPixelId** | **String** | Shopify web pixel id, or null when nothing is installed. |  [optional] |
|**replacedTagId** | **String** | The pixel this install replaced on the store, if any. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |



