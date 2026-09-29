

# CommerceStore


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Zernio SocialAccount id of the store. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**name** | **String** |  |  |
|**domain** | **String** | The platform domain of the store, e.g. my-store.myshopify.com. |  |
|**url** | **String** | Public storefront URL. |  |
|**currency** | **String** | ISO 4217 code the store sells in. |  |
|**country** | **String** | ISO 3166-1 alpha-2 country of the store. |  |
|**capabilities** | **List&lt;CommerceCapability&gt;** |  |  |
|**missingCapabilities** | **List&lt;CommerceCapability&gt;** | Capabilities the platform supports that this store has not granted yet. |  |
|**grantPermissionsUrl** | **String** | Shopify: a page in the Shopify admin where the store owner approves the permissions missingCapabilities need, on the existing install (no reinstall; they can revoke them later). Null when nothing is missing or the store cannot grant them this way (a store connected with its own custom-app token). |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |
| WOOCOMMERCE | &quot;woocommerce&quot; |



