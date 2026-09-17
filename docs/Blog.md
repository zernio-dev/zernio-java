

# Blog

A blog container on the connected platform. All content lives on the platform; Zernio proxies it and stores nothing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native blog id. Shopify uses a numeric blog id. WordPress.com uses the numeric site id; self-hosted WordPress uses &#x60;1&#x60;, scoped to the connected account. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**handle** | **String** | URL slug on Shopify; site hostname on WordPress. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WORDPRESS | &quot;wordpress&quot; |



