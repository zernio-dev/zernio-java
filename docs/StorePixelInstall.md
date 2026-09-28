

# StorePixelInstall

A tracking tag's install on a connected store: a Shopify web pixel, or a Custom HTML widget on a WordPress site. Fields marked Shopify or WordPress are present only for that platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storeAccountId** | **String** |  |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**installed** | **Boolean** | Shopify: this tag is the pixel the store fires. WordPress: the Zernio widget for this tag is in an active widget area with its script intact. |  [optional] |
|**shopDomain** | **String** | Shopify only. |  [optional] |
|**installedTagId** | **String** | Shopify only: the Meta pixel the store fires now (may be a different tag), or null. |  [optional] |
|**webPixelId** | **String** | Shopify only: web pixel id, or null when nothing is installed. |  [optional] |
|**siteUrl** | **String** | WordPress only. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | WordPress only. |  [optional] |
|**widgetId** | **String** | WordPress only: widget id, e.g. &#x60;custom_html-3&#x60;. |  [optional] |
|**sidebarId** | **String** | WordPress only: widget area holding the widget. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WORDPRESS | &quot;wordpress&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| WORDPRESS_WIDGET | &quot;wordpress_widget&quot; |



