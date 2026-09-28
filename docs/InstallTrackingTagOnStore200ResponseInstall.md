

# InstallTrackingTagOnStore200ResponseInstall


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storeAccountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | The store platform. |  [optional] |
|**tagPlatform** | **String** | Platform of the tag this install is about (e.g. &#x60;metaads&#x60;). |  [optional] |
|**siteTagId** | **String** | The id the tag carries on the site (see &#x60;TrackingTag.siteTagId&#x60;). |  [optional] |
|**installed** | **Boolean** | Shopify: this tag is the one the store fires for its platform. WordPress: the Zernio widget for this tag is in an active widget area with its script intact. |  [optional] |
|**shopDomain** | **String** | Shopify only. |  [optional] |
|**installedTagId** | **String** | Shopify only: the tag of the same platform the store fires now (may be a different tag), or null. |  [optional] |
|**tags** | [**List&lt;StorePixelInstallTagsInner&gt;**](StorePixelInstallTagsInner.md) | GET only on WordPress, always on Shopify: every Zernio tag on the store, all platforms. |  [optional] |
|**webPixelId** | **String** | Shopify only: web pixel id, or null when nothing is installed. |  [optional] |
|**siteUrl** | **String** | WordPress only. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | WordPress only. |  [optional] |
|**widgetId** | **String** | WordPress only: widget id, e.g. &#x60;custom_html-3&#x60;. |  [optional] |
|**sidebarId** | **String** | WordPress only: widget area holding the widget. |  [optional] |
|**replacedTagId** | **String** | Shopify only: the pixel this install replaced on the store, if any. |  [optional] |
|**sidebarName** | **String** | WordPress only: name of the widget area used. |  [optional] |
|**created** | **Boolean** | WordPress only: false when an existing Zernio widget was updated. |  [optional] |
|**homepageCheck** | [**HomepageCheckEnum**](#HomepageCheckEnum) | WordPress only: whether the pixel appeared in the homepage HTML. &#x60;not_found&#x60; can be a stale page cache. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WORDPRESS | &quot;wordpress&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| WORDPRESS_WIDGET | &quot;wordpress_widget&quot; |



## Enum: HomepageCheckEnum

| Name | Value |
|---- | -----|
| FOUND | &quot;found&quot; |
| NOT_FOUND | &quot;not_found&quot; |
| UNREACHABLE | &quot;unreachable&quot; |
| SKIPPED | &quot;skipped&quot; |



