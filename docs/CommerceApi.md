# CommerceApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCommerceDiscountCodes**](CommerceApi.md#addCommerceDiscountCodes) | **POST** /v1/commerce/discounts/{discountId}/codes | Add codes to a discount |
| [**addCommerceDiscountCodesWithHttpInfo**](CommerceApi.md#addCommerceDiscountCodesWithHttpInfo) | **POST** /v1/commerce/discounts/{discountId}/codes | Add codes to a discount |
| [**addCommerceMarketingEngagement**](CommerceApi.md#addCommerceMarketingEngagement) | **POST** /v1/commerce/marketing-activities/{remoteId}/engagements | Report daily engagement |
| [**addCommerceMarketingEngagementWithHttpInfo**](CommerceApi.md#addCommerceMarketingEngagementWithHttpInfo) | **POST** /v1/commerce/marketing-activities/{remoteId}/engagements | Report daily engagement |
| [**addCommerceProductImages**](CommerceApi.md#addCommerceProductImages) | **POST** /v1/commerce/products/{productId}/images | Add images |
| [**addCommerceProductImagesWithHttpInfo**](CommerceApi.md#addCommerceProductImagesWithHttpInfo) | **POST** /v1/commerce/products/{productId}/images | Add images |
| [**changeCommerceCollectionChannels**](CommerceApi.md#changeCommerceCollectionChannels) | **POST** /v1/commerce/collections/{collectionId}/channels | Publish or unpublish a collection |
| [**changeCommerceCollectionChannelsWithHttpInfo**](CommerceApi.md#changeCommerceCollectionChannelsWithHttpInfo) | **POST** /v1/commerce/collections/{collectionId}/channels | Publish or unpublish a collection |
| [**changeCommerceCollectionProducts**](CommerceApi.md#changeCommerceCollectionProducts) | **POST** /v1/commerce/collections/{collectionId}/products | Add or remove products in a collection |
| [**changeCommerceCollectionProductsWithHttpInfo**](CommerceApi.md#changeCommerceCollectionProductsWithHttpInfo) | **POST** /v1/commerce/collections/{collectionId}/products | Add or remove products in a collection |
| [**changeCommerceInventory**](CommerceApi.md#changeCommerceInventory) | **POST** /v1/commerce/products/{productId}/inventory | Set or adjust stock |
| [**changeCommerceInventoryWithHttpInfo**](CommerceApi.md#changeCommerceInventoryWithHttpInfo) | **POST** /v1/commerce/products/{productId}/inventory | Set or adjust stock |
| [**changeCommerceProductChannels**](CommerceApi.md#changeCommerceProductChannels) | **POST** /v1/commerce/products/{productId}/channels | Publish or unpublish a product |
| [**changeCommerceProductChannelsWithHttpInfo**](CommerceApi.md#changeCommerceProductChannelsWithHttpInfo) | **POST** /v1/commerce/products/{productId}/channels | Publish or unpublish a product |
| [**changeCommerceProductState**](CommerceApi.md#changeCommerceProductState) | **POST** /v1/commerce/products/state | Activate, deactivate, archive or delete products |
| [**changeCommerceProductStateWithHttpInfo**](CommerceApi.md#changeCommerceProductStateWithHttpInfo) | **POST** /v1/commerce/products/state | Activate, deactivate, archive or delete products |
| [**changeCommerceProductTags**](CommerceApi.md#changeCommerceProductTags) | **POST** /v1/commerce/products/tags | Add or remove tags in bulk |
| [**changeCommerceProductTagsWithHttpInfo**](CommerceApi.md#changeCommerceProductTagsWithHttpInfo) | **POST** /v1/commerce/products/tags | Add or remove tags in bulk |
| [**createCommerceCatalogSync**](CommerceApi.md#createCommerceCatalogSync) | **POST** /v1/commerce/catalog-syncs | Sync a store into a Meta catalog |
| [**createCommerceCatalogSyncWithHttpInfo**](CommerceApi.md#createCommerceCatalogSyncWithHttpInfo) | **POST** /v1/commerce/catalog-syncs | Sync a store into a Meta catalog |
| [**createCommerceCollection**](CommerceApi.md#createCommerceCollection) | **POST** /v1/commerce/collections | Create a collection |
| [**createCommerceCollectionWithHttpInfo**](CommerceApi.md#createCommerceCollectionWithHttpInfo) | **POST** /v1/commerce/collections | Create a collection |
| [**createCommerceDiscount**](CommerceApi.md#createCommerceDiscount) | **POST** /v1/commerce/discounts | Create a discount |
| [**createCommerceDiscountWithHttpInfo**](CommerceApi.md#createCommerceDiscountWithHttpInfo) | **POST** /v1/commerce/discounts | Create a discount |
| [**createCommerceMenu**](CommerceApi.md#createCommerceMenu) | **POST** /v1/commerce/menus | Create a navigation menu |
| [**createCommerceMenuWithHttpInfo**](CommerceApi.md#createCommerceMenuWithHttpInfo) | **POST** /v1/commerce/menus | Create a navigation menu |
| [**createCommerceMetaobject**](CommerceApi.md#createCommerceMetaobject) | **POST** /v1/commerce/metaobjects | Create a metaobject |
| [**createCommerceMetaobjectWithHttpInfo**](CommerceApi.md#createCommerceMetaobjectWithHttpInfo) | **POST** /v1/commerce/metaobjects | Create a metaobject |
| [**createCommercePage**](CommerceApi.md#createCommercePage) | **POST** /v1/commerce/pages | Create a page |
| [**createCommercePageWithHttpInfo**](CommerceApi.md#createCommercePageWithHttpInfo) | **POST** /v1/commerce/pages | Create a page |
| [**createCommerceProduct**](CommerceApi.md#createCommerceProduct) | **POST** /v1/commerce/products | Create a product |
| [**createCommerceProductWithHttpInfo**](CommerceApi.md#createCommerceProductWithHttpInfo) | **POST** /v1/commerce/products | Create a product |
| [**createCommerceProductOptions**](CommerceApi.md#createCommerceProductOptions) | **POST** /v1/commerce/products/{productId}/options | Add options |
| [**createCommerceProductOptionsWithHttpInfo**](CommerceApi.md#createCommerceProductOptionsWithHttpInfo) | **POST** /v1/commerce/products/{productId}/options | Add options |
| [**createCommerceProductVariants**](CommerceApi.md#createCommerceProductVariants) | **POST** /v1/commerce/products/{productId}/variants | Add variants |
| [**createCommerceProductVariantsWithHttpInfo**](CommerceApi.md#createCommerceProductVariantsWithHttpInfo) | **POST** /v1/commerce/products/{productId}/variants | Add variants |
| [**createCommerceRedirect**](CommerceApi.md#createCommerceRedirect) | **POST** /v1/commerce/redirects | Create a URL redirect |
| [**createCommerceRedirectWithHttpInfo**](CommerceApi.md#createCommerceRedirectWithHttpInfo) | **POST** /v1/commerce/redirects | Create a URL redirect |
| [**deleteCommerceCatalogSync**](CommerceApi.md#deleteCommerceCatalogSync) | **DELETE** /v1/commerce/catalog-syncs/{syncId} | Stop a catalog sync |
| [**deleteCommerceCatalogSyncWithHttpInfo**](CommerceApi.md#deleteCommerceCatalogSyncWithHttpInfo) | **DELETE** /v1/commerce/catalog-syncs/{syncId} | Stop a catalog sync |
| [**deleteCommerceCollection**](CommerceApi.md#deleteCommerceCollection) | **DELETE** /v1/commerce/collections/{collectionId} | Delete a collection |
| [**deleteCommerceCollectionWithHttpInfo**](CommerceApi.md#deleteCommerceCollectionWithHttpInfo) | **DELETE** /v1/commerce/collections/{collectionId} | Delete a collection |
| [**deleteCommerceCollectionMetafields**](CommerceApi.md#deleteCommerceCollectionMetafields) | **DELETE** /v1/commerce/collections/{collectionId}/metafields | Delete collection metafields |
| [**deleteCommerceCollectionMetafieldsWithHttpInfo**](CommerceApi.md#deleteCommerceCollectionMetafieldsWithHttpInfo) | **DELETE** /v1/commerce/collections/{collectionId}/metafields | Delete collection metafields |
| [**deleteCommerceDiscount**](CommerceApi.md#deleteCommerceDiscount) | **DELETE** /v1/commerce/discounts/{discountId} | Delete a discount |
| [**deleteCommerceDiscountWithHttpInfo**](CommerceApi.md#deleteCommerceDiscountWithHttpInfo) | **DELETE** /v1/commerce/discounts/{discountId} | Delete a discount |
| [**deleteCommerceMarketingActivity**](CommerceApi.md#deleteCommerceMarketingActivity) | **DELETE** /v1/commerce/marketing-activities/{remoteId} | Delete a marketing activity |
| [**deleteCommerceMarketingActivityWithHttpInfo**](CommerceApi.md#deleteCommerceMarketingActivityWithHttpInfo) | **DELETE** /v1/commerce/marketing-activities/{remoteId} | Delete a marketing activity |
| [**deleteCommerceMenu**](CommerceApi.md#deleteCommerceMenu) | **DELETE** /v1/commerce/menus/{menuId} | Delete a navigation menu |
| [**deleteCommerceMenuWithHttpInfo**](CommerceApi.md#deleteCommerceMenuWithHttpInfo) | **DELETE** /v1/commerce/menus/{menuId} | Delete a navigation menu |
| [**deleteCommerceMetaobject**](CommerceApi.md#deleteCommerceMetaobject) | **DELETE** /v1/commerce/metaobjects/{metaobjectId} | Delete a metaobject |
| [**deleteCommerceMetaobjectWithHttpInfo**](CommerceApi.md#deleteCommerceMetaobjectWithHttpInfo) | **DELETE** /v1/commerce/metaobjects/{metaobjectId} | Delete a metaobject |
| [**deleteCommercePage**](CommerceApi.md#deleteCommercePage) | **DELETE** /v1/commerce/pages/{pageId} | Delete a page |
| [**deleteCommercePageWithHttpInfo**](CommerceApi.md#deleteCommercePageWithHttpInfo) | **DELETE** /v1/commerce/pages/{pageId} | Delete a page |
| [**deleteCommercePriceListPrices**](CommerceApi.md#deleteCommercePriceListPrices) | **DELETE** /v1/commerce/price-lists/{priceListId}/prices | Remove fixed prices |
| [**deleteCommercePriceListPricesWithHttpInfo**](CommerceApi.md#deleteCommercePriceListPricesWithHttpInfo) | **DELETE** /v1/commerce/price-lists/{priceListId}/prices | Remove fixed prices |
| [**deleteCommerceProductMetafields**](CommerceApi.md#deleteCommerceProductMetafields) | **DELETE** /v1/commerce/products/{productId}/metafields | Delete product metafields |
| [**deleteCommerceProductMetafieldsWithHttpInfo**](CommerceApi.md#deleteCommerceProductMetafieldsWithHttpInfo) | **DELETE** /v1/commerce/products/{productId}/metafields | Delete product metafields |
| [**deleteCommerceProductOptions**](CommerceApi.md#deleteCommerceProductOptions) | **DELETE** /v1/commerce/products/{productId}/options | Delete options |
| [**deleteCommerceProductOptionsWithHttpInfo**](CommerceApi.md#deleteCommerceProductOptionsWithHttpInfo) | **DELETE** /v1/commerce/products/{productId}/options | Delete options |
| [**deleteCommerceProductVariants**](CommerceApi.md#deleteCommerceProductVariants) | **DELETE** /v1/commerce/products/{productId}/variants | Delete variants |
| [**deleteCommerceProductVariantsWithHttpInfo**](CommerceApi.md#deleteCommerceProductVariantsWithHttpInfo) | **DELETE** /v1/commerce/products/{productId}/variants | Delete variants |
| [**deleteCommerceRedirect**](CommerceApi.md#deleteCommerceRedirect) | **DELETE** /v1/commerce/redirects/{redirectId} | Delete a URL redirect |
| [**deleteCommerceRedirectWithHttpInfo**](CommerceApi.md#deleteCommerceRedirectWithHttpInfo) | **DELETE** /v1/commerce/redirects/{redirectId} | Delete a URL redirect |
| [**duplicateCommerceProduct**](CommerceApi.md#duplicateCommerceProduct) | **POST** /v1/commerce/products/{productId}/duplicate | Duplicate a product |
| [**duplicateCommerceProductWithHttpInfo**](CommerceApi.md#duplicateCommerceProductWithHttpInfo) | **POST** /v1/commerce/products/{productId}/duplicate | Duplicate a product |
| [**getCommerceCatalogSync**](CommerceApi.md#getCommerceCatalogSync) | **GET** /v1/commerce/catalog-syncs/{syncId} | Get a catalog sync |
| [**getCommerceCatalogSyncWithHttpInfo**](CommerceApi.md#getCommerceCatalogSyncWithHttpInfo) | **GET** /v1/commerce/catalog-syncs/{syncId} | Get a catalog sync |
| [**getCommerceCollection**](CommerceApi.md#getCommerceCollection) | **GET** /v1/commerce/collections/{collectionId} | Get a collection |
| [**getCommerceCollectionWithHttpInfo**](CommerceApi.md#getCommerceCollectionWithHttpInfo) | **GET** /v1/commerce/collections/{collectionId} | Get a collection |
| [**getCommerceDiscount**](CommerceApi.md#getCommerceDiscount) | **GET** /v1/commerce/discounts/{discountId} | Get a discount |
| [**getCommerceDiscountWithHttpInfo**](CommerceApi.md#getCommerceDiscountWithHttpInfo) | **GET** /v1/commerce/discounts/{discountId} | Get a discount |
| [**getCommerceMenu**](CommerceApi.md#getCommerceMenu) | **GET** /v1/commerce/menus/{menuId} | Get a navigation menu |
| [**getCommerceMenuWithHttpInfo**](CommerceApi.md#getCommerceMenuWithHttpInfo) | **GET** /v1/commerce/menus/{menuId} | Get a navigation menu |
| [**getCommerceMetaobject**](CommerceApi.md#getCommerceMetaobject) | **GET** /v1/commerce/metaobjects/{metaobjectId} | Get a metaobject |
| [**getCommerceMetaobjectWithHttpInfo**](CommerceApi.md#getCommerceMetaobjectWithHttpInfo) | **GET** /v1/commerce/metaobjects/{metaobjectId} | Get a metaobject |
| [**getCommercePage**](CommerceApi.md#getCommercePage) | **GET** /v1/commerce/pages/{pageId} | Get a page |
| [**getCommercePageWithHttpInfo**](CommerceApi.md#getCommercePageWithHttpInfo) | **GET** /v1/commerce/pages/{pageId} | Get a page |
| [**getCommerceProduct**](CommerceApi.md#getCommerceProduct) | **GET** /v1/commerce/products/{productId} | Get a product |
| [**getCommerceProductWithHttpInfo**](CommerceApi.md#getCommerceProductWithHttpInfo) | **GET** /v1/commerce/products/{productId} | Get a product |
| [**getCommerceStore**](CommerceApi.md#getCommerceStore) | **GET** /v1/commerce/store | Get a store |
| [**getCommerceStoreWithHttpInfo**](CommerceApi.md#getCommerceStoreWithHttpInfo) | **GET** /v1/commerce/store | Get a store |
| [**listCommerceCatalogSyncs**](CommerceApi.md#listCommerceCatalogSyncs) | **GET** /v1/commerce/catalog-syncs | List catalog syncs |
| [**listCommerceCatalogSyncsWithHttpInfo**](CommerceApi.md#listCommerceCatalogSyncsWithHttpInfo) | **GET** /v1/commerce/catalog-syncs | List catalog syncs |
| [**listCommerceChannels**](CommerceApi.md#listCommerceChannels) | **GET** /v1/commerce/channels | List sales channels |
| [**listCommerceChannelsWithHttpInfo**](CommerceApi.md#listCommerceChannelsWithHttpInfo) | **GET** /v1/commerce/channels | List sales channels |
| [**listCommerceCollectionMetafields**](CommerceApi.md#listCommerceCollectionMetafields) | **GET** /v1/commerce/collections/{collectionId}/metafields | List collection metafields |
| [**listCommerceCollectionMetafieldsWithHttpInfo**](CommerceApi.md#listCommerceCollectionMetafieldsWithHttpInfo) | **GET** /v1/commerce/collections/{collectionId}/metafields | List collection metafields |
| [**listCommerceCollections**](CommerceApi.md#listCommerceCollections) | **GET** /v1/commerce/collections | List collections |
| [**listCommerceCollectionsWithHttpInfo**](CommerceApi.md#listCommerceCollectionsWithHttpInfo) | **GET** /v1/commerce/collections | List collections |
| [**listCommerceDiscounts**](CommerceApi.md#listCommerceDiscounts) | **GET** /v1/commerce/discounts | List discounts |
| [**listCommerceDiscountsWithHttpInfo**](CommerceApi.md#listCommerceDiscountsWithHttpInfo) | **GET** /v1/commerce/discounts | List discounts |
| [**listCommerceInventory**](CommerceApi.md#listCommerceInventory) | **GET** /v1/commerce/inventory | Get a product&#39;s stock |
| [**listCommerceInventoryWithHttpInfo**](CommerceApi.md#listCommerceInventoryWithHttpInfo) | **GET** /v1/commerce/inventory | Get a product&#39;s stock |
| [**listCommerceLocations**](CommerceApi.md#listCommerceLocations) | **GET** /v1/commerce/locations | List locations |
| [**listCommerceLocationsWithHttpInfo**](CommerceApi.md#listCommerceLocationsWithHttpInfo) | **GET** /v1/commerce/locations | List locations |
| [**listCommerceMarkets**](CommerceApi.md#listCommerceMarkets) | **GET** /v1/commerce/markets | List markets |
| [**listCommerceMarketsWithHttpInfo**](CommerceApi.md#listCommerceMarketsWithHttpInfo) | **GET** /v1/commerce/markets | List markets |
| [**listCommerceMenus**](CommerceApi.md#listCommerceMenus) | **GET** /v1/commerce/menus | List navigation menus |
| [**listCommerceMenusWithHttpInfo**](CommerceApi.md#listCommerceMenusWithHttpInfo) | **GET** /v1/commerce/menus | List navigation menus |
| [**listCommerceMetaobjectDefinitions**](CommerceApi.md#listCommerceMetaobjectDefinitions) | **GET** /v1/commerce/metaobject-definitions | List metaobject definitions |
| [**listCommerceMetaobjectDefinitionsWithHttpInfo**](CommerceApi.md#listCommerceMetaobjectDefinitionsWithHttpInfo) | **GET** /v1/commerce/metaobject-definitions | List metaobject definitions |
| [**listCommerceMetaobjects**](CommerceApi.md#listCommerceMetaobjects) | **GET** /v1/commerce/metaobjects | List metaobjects of a type |
| [**listCommerceMetaobjectsWithHttpInfo**](CommerceApi.md#listCommerceMetaobjectsWithHttpInfo) | **GET** /v1/commerce/metaobjects | List metaobjects of a type |
| [**listCommercePages**](CommerceApi.md#listCommercePages) | **GET** /v1/commerce/pages | List pages |
| [**listCommercePagesWithHttpInfo**](CommerceApi.md#listCommercePagesWithHttpInfo) | **GET** /v1/commerce/pages | List pages |
| [**listCommercePriceLists**](CommerceApi.md#listCommercePriceLists) | **GET** /v1/commerce/price-lists | List price lists |
| [**listCommercePriceListsWithHttpInfo**](CommerceApi.md#listCommercePriceListsWithHttpInfo) | **GET** /v1/commerce/price-lists | List price lists |
| [**listCommerceProductMetafields**](CommerceApi.md#listCommerceProductMetafields) | **GET** /v1/commerce/products/{productId}/metafields | List product metafields |
| [**listCommerceProductMetafieldsWithHttpInfo**](CommerceApi.md#listCommerceProductMetafieldsWithHttpInfo) | **GET** /v1/commerce/products/{productId}/metafields | List product metafields |
| [**listCommerceProducts**](CommerceApi.md#listCommerceProducts) | **GET** /v1/commerce/products | List products |
| [**listCommerceProductsWithHttpInfo**](CommerceApi.md#listCommerceProductsWithHttpInfo) | **GET** /v1/commerce/products | List products |
| [**listCommerceRedirects**](CommerceApi.md#listCommerceRedirects) | **GET** /v1/commerce/redirects | List URL redirects |
| [**listCommerceRedirectsWithHttpInfo**](CommerceApi.md#listCommerceRedirectsWithHttpInfo) | **GET** /v1/commerce/redirects | List URL redirects |
| [**removeCommerceProductImages**](CommerceApi.md#removeCommerceProductImages) | **DELETE** /v1/commerce/products/{productId}/images | Remove images |
| [**removeCommerceProductImagesWithHttpInfo**](CommerceApi.md#removeCommerceProductImagesWithHttpInfo) | **DELETE** /v1/commerce/products/{productId}/images | Remove images |
| [**reorderCommerceCollectionProducts**](CommerceApi.md#reorderCommerceCollectionProducts) | **POST** /v1/commerce/collections/{collectionId}/reorder | Reorder products in a collection |
| [**reorderCommerceCollectionProductsWithHttpInfo**](CommerceApi.md#reorderCommerceCollectionProductsWithHttpInfo) | **POST** /v1/commerce/collections/{collectionId}/reorder | Reorder products in a collection |
| [**reorderCommerceProductImages**](CommerceApi.md#reorderCommerceProductImages) | **POST** /v1/commerce/products/{productId}/images/reorder | Reorder images |
| [**reorderCommerceProductImagesWithHttpInfo**](CommerceApi.md#reorderCommerceProductImagesWithHttpInfo) | **POST** /v1/commerce/products/{productId}/images/reorder | Reorder images |
| [**runCommerceCatalogSync**](CommerceApi.md#runCommerceCatalogSync) | **POST** /v1/commerce/catalog-syncs/{syncId}/run | Run a catalog sync now |
| [**runCommerceCatalogSyncWithHttpInfo**](CommerceApi.md#runCommerceCatalogSyncWithHttpInfo) | **POST** /v1/commerce/catalog-syncs/{syncId}/run | Run a catalog sync now |
| [**setCommerceCollectionMetafields**](CommerceApi.md#setCommerceCollectionMetafields) | **PUT** /v1/commerce/collections/{collectionId}/metafields | Set collection metafields |
| [**setCommerceCollectionMetafieldsWithHttpInfo**](CommerceApi.md#setCommerceCollectionMetafieldsWithHttpInfo) | **PUT** /v1/commerce/collections/{collectionId}/metafields | Set collection metafields |
| [**setCommerceDiscountActive**](CommerceApi.md#setCommerceDiscountActive) | **POST** /v1/commerce/discounts/{discountId}/state | Activate or deactivate a discount |
| [**setCommerceDiscountActiveWithHttpInfo**](CommerceApi.md#setCommerceDiscountActiveWithHttpInfo) | **POST** /v1/commerce/discounts/{discountId}/state | Activate or deactivate a discount |
| [**setCommercePriceListPrices**](CommerceApi.md#setCommercePriceListPrices) | **PUT** /v1/commerce/price-lists/{priceListId}/prices | Set fixed prices |
| [**setCommercePriceListPricesWithHttpInfo**](CommerceApi.md#setCommercePriceListPricesWithHttpInfo) | **PUT** /v1/commerce/price-lists/{priceListId}/prices | Set fixed prices |
| [**setCommerceProductMetafields**](CommerceApi.md#setCommerceProductMetafields) | **PUT** /v1/commerce/products/{productId}/metafields | Set product metafields |
| [**setCommerceProductMetafieldsWithHttpInfo**](CommerceApi.md#setCommerceProductMetafieldsWithHttpInfo) | **PUT** /v1/commerce/products/{productId}/metafields | Set product metafields |
| [**updateCommerceCollection**](CommerceApi.md#updateCommerceCollection) | **PATCH** /v1/commerce/collections/{collectionId} | Update a collection |
| [**updateCommerceCollectionWithHttpInfo**](CommerceApi.md#updateCommerceCollectionWithHttpInfo) | **PATCH** /v1/commerce/collections/{collectionId} | Update a collection |
| [**updateCommerceDiscount**](CommerceApi.md#updateCommerceDiscount) | **PATCH** /v1/commerce/discounts/{discountId} | Update a discount |
| [**updateCommerceDiscountWithHttpInfo**](CommerceApi.md#updateCommerceDiscountWithHttpInfo) | **PATCH** /v1/commerce/discounts/{discountId} | Update a discount |
| [**updateCommerceMenu**](CommerceApi.md#updateCommerceMenu) | **PUT** /v1/commerce/menus/{menuId} | Replace a navigation menu |
| [**updateCommerceMenuWithHttpInfo**](CommerceApi.md#updateCommerceMenuWithHttpInfo) | **PUT** /v1/commerce/menus/{menuId} | Replace a navigation menu |
| [**updateCommerceMetaobject**](CommerceApi.md#updateCommerceMetaobject) | **PATCH** /v1/commerce/metaobjects/{metaobjectId} | Update a metaobject |
| [**updateCommerceMetaobjectWithHttpInfo**](CommerceApi.md#updateCommerceMetaobjectWithHttpInfo) | **PATCH** /v1/commerce/metaobjects/{metaobjectId} | Update a metaobject |
| [**updateCommercePage**](CommerceApi.md#updateCommercePage) | **PATCH** /v1/commerce/pages/{pageId} | Update a page |
| [**updateCommercePageWithHttpInfo**](CommerceApi.md#updateCommercePageWithHttpInfo) | **PATCH** /v1/commerce/pages/{pageId} | Update a page |
| [**updateCommerceProduct**](CommerceApi.md#updateCommerceProduct) | **PATCH** /v1/commerce/products/{productId} | Update a product |
| [**updateCommerceProductWithHttpInfo**](CommerceApi.md#updateCommerceProductWithHttpInfo) | **PATCH** /v1/commerce/products/{productId} | Update a product |
| [**updateCommerceProductPrices**](CommerceApi.md#updateCommerceProductPrices) | **POST** /v1/commerce/products/{productId}/price | Update variant prices |
| [**updateCommerceProductPricesWithHttpInfo**](CommerceApi.md#updateCommerceProductPricesWithHttpInfo) | **POST** /v1/commerce/products/{productId}/price | Update variant prices |
| [**updateCommerceRedirect**](CommerceApi.md#updateCommerceRedirect) | **PATCH** /v1/commerce/redirects/{redirectId} | Update a URL redirect |
| [**updateCommerceRedirectWithHttpInfo**](CommerceApi.md#updateCommerceRedirectWithHttpInfo) | **PATCH** /v1/commerce/redirects/{redirectId} | Update a URL redirect |
| [**upsertCommerceMarketingActivity**](CommerceApi.md#upsertCommerceMarketingActivity) | **PUT** /v1/commerce/marketing-activities | Record a marketing activity |
| [**upsertCommerceMarketingActivityWithHttpInfo**](CommerceApi.md#upsertCommerceMarketingActivityWithHttpInfo) | **PUT** /v1/commerce/marketing-activities | Record a marketing activity |



## addCommerceDiscountCodes

> ReorderCommerceProductImages200Response addCommerceDiscountCodes(discountId, addCommerceDiscountCodesRequest)

Add codes to a discount

Adds up to 250 more codes to a code discount, for example one per influencer. The platform adds them in the background. Needs discounts.codes, which WooCommerce stores do not have. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        AddCommerceDiscountCodesRequest addCommerceDiscountCodesRequest = new AddCommerceDiscountCodesRequest(); // AddCommerceDiscountCodesRequest | 
        try {
            ReorderCommerceProductImages200Response result = apiInstance.addCommerceDiscountCodes(discountId, addCommerceDiscountCodesRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#addCommerceDiscountCodes");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **addCommerceDiscountCodesRequest** | [**AddCommerceDiscountCodesRequest**](AddCommerceDiscountCodesRequest.md)|  | |

### Return type

[**ReorderCommerceProductImages200Response**](ReorderCommerceProductImages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Codes queued |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## addCommerceDiscountCodesWithHttpInfo

> ApiResponse<ReorderCommerceProductImages200Response> addCommerceDiscountCodes addCommerceDiscountCodesWithHttpInfo(discountId, addCommerceDiscountCodesRequest)

Add codes to a discount

Adds up to 250 more codes to a code discount, for example one per influencer. The platform adds them in the background. Needs discounts.codes, which WooCommerce stores do not have. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        AddCommerceDiscountCodesRequest addCommerceDiscountCodesRequest = new AddCommerceDiscountCodesRequest(); // AddCommerceDiscountCodesRequest | 
        try {
            ApiResponse<ReorderCommerceProductImages200Response> response = apiInstance.addCommerceDiscountCodesWithHttpInfo(discountId, addCommerceDiscountCodesRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#addCommerceDiscountCodes");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **addCommerceDiscountCodesRequest** | [**AddCommerceDiscountCodesRequest**](AddCommerceDiscountCodesRequest.md)|  | |

### Return type

ApiResponse<[**ReorderCommerceProductImages200Response**](ReorderCommerceProductImages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Codes queued |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## addCommerceMarketingEngagement

> AddCommerceMarketingEngagement201Response addCommerceMarketingEngagement(remoteId, addCommerceMarketingEngagementRequest)

Report daily engagement

Reports one day&#39;s numbers for an activity (UTC day), shown next to it in the store&#39;s Marketing section. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String remoteId = "remoteId_example"; // String | The remoteId given when recording it.
        AddCommerceMarketingEngagementRequest addCommerceMarketingEngagementRequest = new AddCommerceMarketingEngagementRequest(); // AddCommerceMarketingEngagementRequest | 
        try {
            AddCommerceMarketingEngagement201Response result = apiInstance.addCommerceMarketingEngagement(remoteId, addCommerceMarketingEngagementRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#addCommerceMarketingEngagement");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **remoteId** | **String**| The remoteId given when recording it. | |
| **addCommerceMarketingEngagementRequest** | [**AddCommerceMarketingEngagementRequest**](AddCommerceMarketingEngagementRequest.md)|  | |

### Return type

[**AddCommerceMarketingEngagement201Response**](AddCommerceMarketingEngagement201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Engagement recorded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## addCommerceMarketingEngagementWithHttpInfo

> ApiResponse<AddCommerceMarketingEngagement201Response> addCommerceMarketingEngagement addCommerceMarketingEngagementWithHttpInfo(remoteId, addCommerceMarketingEngagementRequest)

Report daily engagement

Reports one day&#39;s numbers for an activity (UTC day), shown next to it in the store&#39;s Marketing section. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String remoteId = "remoteId_example"; // String | The remoteId given when recording it.
        AddCommerceMarketingEngagementRequest addCommerceMarketingEngagementRequest = new AddCommerceMarketingEngagementRequest(); // AddCommerceMarketingEngagementRequest | 
        try {
            ApiResponse<AddCommerceMarketingEngagement201Response> response = apiInstance.addCommerceMarketingEngagementWithHttpInfo(remoteId, addCommerceMarketingEngagementRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#addCommerceMarketingEngagement");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **remoteId** | **String**| The remoteId given when recording it. | |
| **addCommerceMarketingEngagementRequest** | [**AddCommerceMarketingEngagementRequest**](AddCommerceMarketingEngagementRequest.md)|  | |

### Return type

ApiResponse<[**AddCommerceMarketingEngagement201Response**](AddCommerceMarketingEngagement201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Engagement recorded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## addCommerceProductImages

> CreateCommerceProduct201Response addCommerceProductImages(productId, addCommerceProductImagesRequest)

Add images

Adds images from public URLs. The platform fetches them, so they can appear on the product a few seconds after the call returns. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        AddCommerceProductImagesRequest addCommerceProductImagesRequest = new AddCommerceProductImagesRequest(); // AddCommerceProductImagesRequest | 
        try {
            CreateCommerceProduct201Response result = apiInstance.addCommerceProductImages(productId, addCommerceProductImagesRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#addCommerceProductImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **addCommerceProductImagesRequest** | [**AddCommerceProductImagesRequest**](AddCommerceProductImagesRequest.md)|  | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## addCommerceProductImagesWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> addCommerceProductImages addCommerceProductImagesWithHttpInfo(productId, addCommerceProductImagesRequest)

Add images

Adds images from public URLs. The platform fetches them, so they can appear on the product a few seconds after the call returns. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        AddCommerceProductImagesRequest addCommerceProductImagesRequest = new AddCommerceProductImagesRequest(); // AddCommerceProductImagesRequest | 
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.addCommerceProductImagesWithHttpInfo(productId, addCommerceProductImagesRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#addCommerceProductImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **addCommerceProductImagesRequest** | [**AddCommerceProductImagesRequest**](AddCommerceProductImagesRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## changeCommerceCollectionChannels

> ChangeCommerceCollectionChannels200Response changeCommerceCollectionChannels(collectionId, changeCommerceProductChannelsRequest)

Publish or unpublish a collection

Publishes to and/or unpublishes from sales channels (the online store, Shop, POS and others). List channels with GET /v1/commerce/channels. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        ChangeCommerceProductChannelsRequest changeCommerceProductChannelsRequest = new ChangeCommerceProductChannelsRequest(); // ChangeCommerceProductChannelsRequest | 
        try {
            ChangeCommerceCollectionChannels200Response result = apiInstance.changeCommerceCollectionChannels(collectionId, changeCommerceProductChannelsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceCollectionChannels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **changeCommerceProductChannelsRequest** | [**ChangeCommerceProductChannelsRequest**](ChangeCommerceProductChannelsRequest.md)|  | |

### Return type

[**ChangeCommerceCollectionChannels200Response**](ChangeCommerceCollectionChannels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Publication changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## changeCommerceCollectionChannelsWithHttpInfo

> ApiResponse<ChangeCommerceCollectionChannels200Response> changeCommerceCollectionChannels changeCommerceCollectionChannelsWithHttpInfo(collectionId, changeCommerceProductChannelsRequest)

Publish or unpublish a collection

Publishes to and/or unpublishes from sales channels (the online store, Shop, POS and others). List channels with GET /v1/commerce/channels. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        ChangeCommerceProductChannelsRequest changeCommerceProductChannelsRequest = new ChangeCommerceProductChannelsRequest(); // ChangeCommerceProductChannelsRequest | 
        try {
            ApiResponse<ChangeCommerceCollectionChannels200Response> response = apiInstance.changeCommerceCollectionChannelsWithHttpInfo(collectionId, changeCommerceProductChannelsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceCollectionChannels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **changeCommerceProductChannelsRequest** | [**ChangeCommerceProductChannelsRequest**](ChangeCommerceProductChannelsRequest.md)|  | |

### Return type

ApiResponse<[**ChangeCommerceCollectionChannels200Response**](ChangeCommerceCollectionChannels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Publication changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## changeCommerceCollectionProducts

> ChangeCommerceCollectionProducts200Response changeCommerceCollectionProducts(collectionId, changeCommerceCollectionProductsRequest)

Add or remove products in a collection

Adds and/or removes hand-picked products. Products a collection includes through its own rules are not affected. &#x60;pending&#x60; is true when the platform finishes the change in the background; the product count then catches up a few seconds later. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        ChangeCommerceCollectionProductsRequest changeCommerceCollectionProductsRequest = new ChangeCommerceCollectionProductsRequest(); // ChangeCommerceCollectionProductsRequest | 
        try {
            ChangeCommerceCollectionProducts200Response result = apiInstance.changeCommerceCollectionProducts(collectionId, changeCommerceCollectionProductsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceCollectionProducts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **changeCommerceCollectionProductsRequest** | [**ChangeCommerceCollectionProductsRequest**](ChangeCommerceCollectionProductsRequest.md)|  | |

### Return type

[**ChangeCommerceCollectionProducts200Response**](ChangeCommerceCollectionProducts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Membership changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## changeCommerceCollectionProductsWithHttpInfo

> ApiResponse<ChangeCommerceCollectionProducts200Response> changeCommerceCollectionProducts changeCommerceCollectionProductsWithHttpInfo(collectionId, changeCommerceCollectionProductsRequest)

Add or remove products in a collection

Adds and/or removes hand-picked products. Products a collection includes through its own rules are not affected. &#x60;pending&#x60; is true when the platform finishes the change in the background; the product count then catches up a few seconds later. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        ChangeCommerceCollectionProductsRequest changeCommerceCollectionProductsRequest = new ChangeCommerceCollectionProductsRequest(); // ChangeCommerceCollectionProductsRequest | 
        try {
            ApiResponse<ChangeCommerceCollectionProducts200Response> response = apiInstance.changeCommerceCollectionProductsWithHttpInfo(collectionId, changeCommerceCollectionProductsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceCollectionProducts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **changeCommerceCollectionProductsRequest** | [**ChangeCommerceCollectionProductsRequest**](ChangeCommerceCollectionProductsRequest.md)|  | |

### Return type

ApiResponse<[**ChangeCommerceCollectionProducts200Response**](ChangeCommerceCollectionProducts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Membership changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## changeCommerceInventory

> ListCommerceInventory200Response changeCommerceInventory(productId, changeCommerceInventoryRequest)

Set or adjust stock

&#x60;set&#x60; makes &#x60;quantity&#x60; the new available count; &#x60;adjust&#x60; adds &#x60;quantity&#x60; (negative to subtract). The variant must be stocked at the location. Answers the product&#39;s stock after the change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        ChangeCommerceInventoryRequest changeCommerceInventoryRequest = new ChangeCommerceInventoryRequest(); // ChangeCommerceInventoryRequest | 
        try {
            ListCommerceInventory200Response result = apiInstance.changeCommerceInventory(productId, changeCommerceInventoryRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceInventory");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **changeCommerceInventoryRequest** | [**ChangeCommerceInventoryRequest**](ChangeCommerceInventoryRequest.md)|  | |

### Return type

[**ListCommerceInventory200Response**](ListCommerceInventory200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stock changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## changeCommerceInventoryWithHttpInfo

> ApiResponse<ListCommerceInventory200Response> changeCommerceInventory changeCommerceInventoryWithHttpInfo(productId, changeCommerceInventoryRequest)

Set or adjust stock

&#x60;set&#x60; makes &#x60;quantity&#x60; the new available count; &#x60;adjust&#x60; adds &#x60;quantity&#x60; (negative to subtract). The variant must be stocked at the location. Answers the product&#39;s stock after the change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        ChangeCommerceInventoryRequest changeCommerceInventoryRequest = new ChangeCommerceInventoryRequest(); // ChangeCommerceInventoryRequest | 
        try {
            ApiResponse<ListCommerceInventory200Response> response = apiInstance.changeCommerceInventoryWithHttpInfo(productId, changeCommerceInventoryRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceInventory");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **changeCommerceInventoryRequest** | [**ChangeCommerceInventoryRequest**](ChangeCommerceInventoryRequest.md)|  | |

### Return type

ApiResponse<[**ListCommerceInventory200Response**](ListCommerceInventory200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stock changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## changeCommerceProductChannels

> ChangeCommerceProductChannels200Response changeCommerceProductChannels(productId, changeCommerceProductChannelsRequest)

Publish or unpublish a product

Publishes to and/or unpublishes from sales channels (the online store, Shop, POS and others). List channels with GET /v1/commerce/channels. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        ChangeCommerceProductChannelsRequest changeCommerceProductChannelsRequest = new ChangeCommerceProductChannelsRequest(); // ChangeCommerceProductChannelsRequest | 
        try {
            ChangeCommerceProductChannels200Response result = apiInstance.changeCommerceProductChannels(productId, changeCommerceProductChannelsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceProductChannels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **changeCommerceProductChannelsRequest** | [**ChangeCommerceProductChannelsRequest**](ChangeCommerceProductChannelsRequest.md)|  | |

### Return type

[**ChangeCommerceProductChannels200Response**](ChangeCommerceProductChannels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Publication changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## changeCommerceProductChannelsWithHttpInfo

> ApiResponse<ChangeCommerceProductChannels200Response> changeCommerceProductChannels changeCommerceProductChannelsWithHttpInfo(productId, changeCommerceProductChannelsRequest)

Publish or unpublish a product

Publishes to and/or unpublishes from sales channels (the online store, Shop, POS and others). List channels with GET /v1/commerce/channels. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        ChangeCommerceProductChannelsRequest changeCommerceProductChannelsRequest = new ChangeCommerceProductChannelsRequest(); // ChangeCommerceProductChannelsRequest | 
        try {
            ApiResponse<ChangeCommerceProductChannels200Response> response = apiInstance.changeCommerceProductChannelsWithHttpInfo(productId, changeCommerceProductChannelsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceProductChannels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **changeCommerceProductChannelsRequest** | [**ChangeCommerceProductChannelsRequest**](ChangeCommerceProductChannelsRequest.md)|  | |

### Return type

ApiResponse<[**ChangeCommerceProductChannels200Response**](ChangeCommerceProductChannels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Publication changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## changeCommerceProductState

> ChangeCommerceProductState200Response changeCommerceProductState(changeCommerceProductStateRequest)

Activate, deactivate, archive or delete products

Applies one action to up to 50 products and reports each product&#39;s outcome, so one failure does not abort the rest. On Shopify, &#x60;deactivate&#x60; sets the product to draft and &#x60;delete&#x60; is permanent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        ChangeCommerceProductStateRequest changeCommerceProductStateRequest = new ChangeCommerceProductStateRequest(); // ChangeCommerceProductStateRequest | 
        try {
            ChangeCommerceProductState200Response result = apiInstance.changeCommerceProductState(changeCommerceProductStateRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceProductState");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **changeCommerceProductStateRequest** | [**ChangeCommerceProductStateRequest**](ChangeCommerceProductStateRequest.md)|  | |

### Return type

[**ChangeCommerceProductState200Response**](ChangeCommerceProductState200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Action applied |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## changeCommerceProductStateWithHttpInfo

> ApiResponse<ChangeCommerceProductState200Response> changeCommerceProductState changeCommerceProductStateWithHttpInfo(changeCommerceProductStateRequest)

Activate, deactivate, archive or delete products

Applies one action to up to 50 products and reports each product&#39;s outcome, so one failure does not abort the rest. On Shopify, &#x60;deactivate&#x60; sets the product to draft and &#x60;delete&#x60; is permanent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        ChangeCommerceProductStateRequest changeCommerceProductStateRequest = new ChangeCommerceProductStateRequest(); // ChangeCommerceProductStateRequest | 
        try {
            ApiResponse<ChangeCommerceProductState200Response> response = apiInstance.changeCommerceProductStateWithHttpInfo(changeCommerceProductStateRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceProductState");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **changeCommerceProductStateRequest** | [**ChangeCommerceProductStateRequest**](ChangeCommerceProductStateRequest.md)|  | |

### Return type

ApiResponse<[**ChangeCommerceProductState200Response**](ChangeCommerceProductState200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Action applied |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## changeCommerceProductTags

> ChangeCommerceProductTags200Response changeCommerceProductTags(changeCommerceProductTagsRequest)

Add or remove tags in bulk

Adds and/or removes tags on up to 50 products and reports each product&#39;s outcome. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        ChangeCommerceProductTagsRequest changeCommerceProductTagsRequest = new ChangeCommerceProductTagsRequest(); // ChangeCommerceProductTagsRequest | 
        try {
            ChangeCommerceProductTags200Response result = apiInstance.changeCommerceProductTags(changeCommerceProductTagsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceProductTags");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **changeCommerceProductTagsRequest** | [**ChangeCommerceProductTagsRequest**](ChangeCommerceProductTagsRequest.md)|  | |

### Return type

[**ChangeCommerceProductTags200Response**](ChangeCommerceProductTags200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tags changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## changeCommerceProductTagsWithHttpInfo

> ApiResponse<ChangeCommerceProductTags200Response> changeCommerceProductTags changeCommerceProductTagsWithHttpInfo(changeCommerceProductTagsRequest)

Add or remove tags in bulk

Adds and/or removes tags on up to 50 products and reports each product&#39;s outcome. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        ChangeCommerceProductTagsRequest changeCommerceProductTagsRequest = new ChangeCommerceProductTagsRequest(); // ChangeCommerceProductTagsRequest | 
        try {
            ApiResponse<ChangeCommerceProductTags200Response> response = apiInstance.changeCommerceProductTagsWithHttpInfo(changeCommerceProductTagsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#changeCommerceProductTags");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **changeCommerceProductTagsRequest** | [**ChangeCommerceProductTagsRequest**](ChangeCommerceProductTagsRequest.md)|  | |

### Return type

ApiResponse<[**ChangeCommerceProductTags200Response**](ChangeCommerceProductTags200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tags changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceCatalogSync

> CreateCommerceCatalogSync202Response createCommerceCatalogSync(createCommerceCatalogSyncRequest)

Sync a store into a Meta catalog

Keeps a Meta product catalog in sync with the store, for catalog ads (&#x60;goal: catalog_sales&#x60;) and Shops. The first full run starts right away in the background; &#x60;runStatus&#x60; and the item counts report its outcome. Every active product variant that is published to the online store and has an image becomes a catalog item, grouped by product (&#x60;item_group_id&#x60;). After that, product changes on the store update the catalog within minutes, and a daily full run removes items for products or variants the store no longer has. Items are namespaced to the store, so a catalog can take several stores and a run never touches items it did not create.  &#x60;catalogAccountId&#x60; is a connected facebook, instagram or metaads account whose Meta login can manage the catalog (the catalog_management permission); find catalogs with &#x60;GET /v1/ads/catalogs&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceCatalogSyncRequest createCommerceCatalogSyncRequest = new CreateCommerceCatalogSyncRequest(); // CreateCommerceCatalogSyncRequest | 
        try {
            CreateCommerceCatalogSync202Response result = apiInstance.createCommerceCatalogSync(createCommerceCatalogSyncRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceCatalogSyncRequest** | [**CreateCommerceCatalogSyncRequest**](CreateCommerceCatalogSyncRequest.md)|  | |

### Return type

[**CreateCommerceCatalogSync202Response**](CreateCommerceCatalogSync202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Sync created; the first run is queued |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The Meta login cannot manage the catalog (code insufficient_permissions). |  -  |
| **404** | Account or catalog not found (code account_not_found or resource_not_found). |  -  |
| **409** | The store already syncs to that catalog (code catalog_sync_conflict). |  -  |

## createCommerceCatalogSyncWithHttpInfo

> ApiResponse<CreateCommerceCatalogSync202Response> createCommerceCatalogSync createCommerceCatalogSyncWithHttpInfo(createCommerceCatalogSyncRequest)

Sync a store into a Meta catalog

Keeps a Meta product catalog in sync with the store, for catalog ads (&#x60;goal: catalog_sales&#x60;) and Shops. The first full run starts right away in the background; &#x60;runStatus&#x60; and the item counts report its outcome. Every active product variant that is published to the online store and has an image becomes a catalog item, grouped by product (&#x60;item_group_id&#x60;). After that, product changes on the store update the catalog within minutes, and a daily full run removes items for products or variants the store no longer has. Items are namespaced to the store, so a catalog can take several stores and a run never touches items it did not create.  &#x60;catalogAccountId&#x60; is a connected facebook, instagram or metaads account whose Meta login can manage the catalog (the catalog_management permission); find catalogs with &#x60;GET /v1/ads/catalogs&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceCatalogSyncRequest createCommerceCatalogSyncRequest = new CreateCommerceCatalogSyncRequest(); // CreateCommerceCatalogSyncRequest | 
        try {
            ApiResponse<CreateCommerceCatalogSync202Response> response = apiInstance.createCommerceCatalogSyncWithHttpInfo(createCommerceCatalogSyncRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceCatalogSyncRequest** | [**CreateCommerceCatalogSyncRequest**](CreateCommerceCatalogSyncRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceCatalogSync202Response**](CreateCommerceCatalogSync202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Sync created; the first run is queued |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The Meta login cannot manage the catalog (code insufficient_permissions). |  -  |
| **404** | Account or catalog not found (code account_not_found or resource_not_found). |  -  |
| **409** | The store already syncs to that catalog (code catalog_sync_conflict). |  -  |


## createCommerceCollection

> CreateCommerceCollection201Response createCommerceCollection(createCommerceCollectionRequest)

Create a collection

Creates a collection, optionally with hand-picked products. On Shopify the collection starts unpublished from the online store; publish it from the Shopify admin. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceCollectionRequest createCommerceCollectionRequest = new CreateCommerceCollectionRequest(); // CreateCommerceCollectionRequest | 
        try {
            CreateCommerceCollection201Response result = apiInstance.createCommerceCollection(createCommerceCollectionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceCollectionRequest** | [**CreateCommerceCollectionRequest**](CreateCommerceCollectionRequest.md)|  | |

### Return type

[**CreateCommerceCollection201Response**](CreateCommerceCollection201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Collection created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceCollectionWithHttpInfo

> ApiResponse<CreateCommerceCollection201Response> createCommerceCollection createCommerceCollectionWithHttpInfo(createCommerceCollectionRequest)

Create a collection

Creates a collection, optionally with hand-picked products. On Shopify the collection starts unpublished from the online store; publish it from the Shopify admin. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceCollectionRequest createCommerceCollectionRequest = new CreateCommerceCollectionRequest(); // CreateCommerceCollectionRequest | 
        try {
            ApiResponse<CreateCommerceCollection201Response> response = apiInstance.createCommerceCollectionWithHttpInfo(createCommerceCollectionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceCollectionRequest** | [**CreateCommerceCollectionRequest**](CreateCommerceCollectionRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceCollection201Response**](CreateCommerceCollection201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Collection created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceDiscount

> CreateCommerceDiscount201Response createCommerceDiscount(createCommerceDiscountRequest)

Create a discount

Creates a code discount (buyers enter a code) or an automatic one (applied at checkout), as a percentage, a fixed amount or free shipping. It applies to every product unless productIds or collectionIds narrow it, and to every buyer. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceDiscountRequest createCommerceDiscountRequest = new CreateCommerceDiscountRequest(); // CreateCommerceDiscountRequest | 
        try {
            CreateCommerceDiscount201Response result = apiInstance.createCommerceDiscount(createCommerceDiscountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceDiscountRequest** | [**CreateCommerceDiscountRequest**](CreateCommerceDiscountRequest.md)|  | |

### Return type

[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Discount created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceDiscountWithHttpInfo

> ApiResponse<CreateCommerceDiscount201Response> createCommerceDiscount createCommerceDiscountWithHttpInfo(createCommerceDiscountRequest)

Create a discount

Creates a code discount (buyers enter a code) or an automatic one (applied at checkout), as a percentage, a fixed amount or free shipping. It applies to every product unless productIds or collectionIds narrow it, and to every buyer. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceDiscountRequest createCommerceDiscountRequest = new CreateCommerceDiscountRequest(); // CreateCommerceDiscountRequest | 
        try {
            ApiResponse<CreateCommerceDiscount201Response> response = apiInstance.createCommerceDiscountWithHttpInfo(createCommerceDiscountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceDiscountRequest** | [**CreateCommerceDiscountRequest**](CreateCommerceDiscountRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Discount created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceMenu

> CreateCommerceMenu201Response createCommerceMenu(createCommerceMenuRequest)

Create a navigation menu

Creates a navigation menu from &#x60;title&#x60;, &#x60;handle&#x60; and up to 100 &#x60;items&#x60;, and returns it with status 201. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceMenuRequest createCommerceMenuRequest = new CreateCommerceMenuRequest(); // CreateCommerceMenuRequest | 
        try {
            CreateCommerceMenu201Response result = apiInstance.createCommerceMenu(createCommerceMenuRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceMenuRequest** | [**CreateCommerceMenuRequest**](CreateCommerceMenuRequest.md)|  | |

### Return type

[**CreateCommerceMenu201Response**](CreateCommerceMenu201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Menu created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceMenuWithHttpInfo

> ApiResponse<CreateCommerceMenu201Response> createCommerceMenu createCommerceMenuWithHttpInfo(createCommerceMenuRequest)

Create a navigation menu

Creates a navigation menu from &#x60;title&#x60;, &#x60;handle&#x60; and up to 100 &#x60;items&#x60;, and returns it with status 201. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceMenuRequest createCommerceMenuRequest = new CreateCommerceMenuRequest(); // CreateCommerceMenuRequest | 
        try {
            ApiResponse<CreateCommerceMenu201Response> response = apiInstance.createCommerceMenuWithHttpInfo(createCommerceMenuRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceMenuRequest** | [**CreateCommerceMenuRequest**](CreateCommerceMenuRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceMenu201Response**](CreateCommerceMenu201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Menu created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceMetaobject

> CreateCommerceMetaobject201Response createCommerceMetaobject(createCommerceMetaobjectRequest)

Create a metaobject

Creates a metaobject of &#x60;type&#x60; with its &#x60;fields&#x60; (key and string value, up to 100) and an optional &#x60;handle&#x60;, and returns it with status 201. Shopify only. Needs metaobjects.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceMetaobjectRequest createCommerceMetaobjectRequest = new CreateCommerceMetaobjectRequest(); // CreateCommerceMetaobjectRequest | 
        try {
            CreateCommerceMetaobject201Response result = apiInstance.createCommerceMetaobject(createCommerceMetaobjectRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceMetaobjectRequest** | [**CreateCommerceMetaobjectRequest**](CreateCommerceMetaobjectRequest.md)|  | |

### Return type

[**CreateCommerceMetaobject201Response**](CreateCommerceMetaobject201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Metaobject created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceMetaobjectWithHttpInfo

> ApiResponse<CreateCommerceMetaobject201Response> createCommerceMetaobject createCommerceMetaobjectWithHttpInfo(createCommerceMetaobjectRequest)

Create a metaobject

Creates a metaobject of &#x60;type&#x60; with its &#x60;fields&#x60; (key and string value, up to 100) and an optional &#x60;handle&#x60;, and returns it with status 201. Shopify only. Needs metaobjects.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceMetaobjectRequest createCommerceMetaobjectRequest = new CreateCommerceMetaobjectRequest(); // CreateCommerceMetaobjectRequest | 
        try {
            ApiResponse<CreateCommerceMetaobject201Response> response = apiInstance.createCommerceMetaobjectWithHttpInfo(createCommerceMetaobjectRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceMetaobjectRequest** | [**CreateCommerceMetaobjectRequest**](CreateCommerceMetaobjectRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceMetaobject201Response**](CreateCommerceMetaobject201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Metaobject created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommercePage

> CreateCommercePage201Response createCommercePage(createCommercePageRequest)

Create a page

Creates a content page from &#x60;title&#x60;, optional &#x60;handle&#x60;, &#x60;bodyHtml&#x60; and &#x60;isPublished&#x60;, and returns it with status 201. Needs pages.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommercePageRequest createCommercePageRequest = new CreateCommercePageRequest(); // CreateCommercePageRequest | 
        try {
            CreateCommercePage201Response result = apiInstance.createCommercePage(createCommercePageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommercePageRequest** | [**CreateCommercePageRequest**](CreateCommercePageRequest.md)|  | |

### Return type

[**CreateCommercePage201Response**](CreateCommercePage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Page created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommercePageWithHttpInfo

> ApiResponse<CreateCommercePage201Response> createCommercePage createCommercePageWithHttpInfo(createCommercePageRequest)

Create a page

Creates a content page from &#x60;title&#x60;, optional &#x60;handle&#x60;, &#x60;bodyHtml&#x60; and &#x60;isPublished&#x60;, and returns it with status 201. Needs pages.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommercePageRequest createCommercePageRequest = new CreateCommercePageRequest(); // CreateCommercePageRequest | 
        try {
            ApiResponse<CreateCommercePage201Response> response = apiInstance.createCommercePageWithHttpInfo(createCommercePageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommercePageRequest** | [**CreateCommercePageRequest**](CreateCommercePageRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommercePage201Response**](CreateCommercePage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Page created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceProduct

> CreateCommerceProduct201Response createCommerceProduct(createCommerceProductRequest)

Create a product

Creates a product with its options and variants. &#x60;status&#x60; defaults to &#x60;draft&#x60;: no platform offers a sandbox for product writes, so nothing goes on sale unless you ask for &#x60;active&#x60;. A product without &#x60;options&#x60; has exactly one variant. Images are fetched by the platform from the given URLs and may appear on the product a few seconds later. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceProductRequest createCommerceProductRequest = new CreateCommerceProductRequest(); // CreateCommerceProductRequest | 
        try {
            CreateCommerceProduct201Response result = apiInstance.createCommerceProduct(createCommerceProductRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceProductRequest** | [**CreateCommerceProductRequest**](CreateCommerceProductRequest.md)|  | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceProductWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> createCommerceProduct createCommerceProductWithHttpInfo(createCommerceProductRequest)

Create a product

Creates a product with its options and variants. &#x60;status&#x60; defaults to &#x60;draft&#x60;: no platform offers a sandbox for product writes, so nothing goes on sale unless you ask for &#x60;active&#x60;. A product without &#x60;options&#x60; has exactly one variant. Images are fetched by the platform from the given URLs and may appear on the product a few seconds later. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceProductRequest createCommerceProductRequest = new CreateCommerceProductRequest(); // CreateCommerceProductRequest | 
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.createCommerceProductWithHttpInfo(createCommerceProductRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceProductRequest** | [**CreateCommerceProductRequest**](CreateCommerceProductRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceProductOptions

> CreateCommerceProduct201Response createCommerceProductOptions(productId, createCommerceProductOptionsRequest)

Add options

Adds option axes (e.g. Size, Color) and their values. With createVariants true the platform creates a variant for every new combination; otherwise existing variants take the first value. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        CreateCommerceProductOptionsRequest createCommerceProductOptionsRequest = new CreateCommerceProductOptionsRequest(); // CreateCommerceProductOptionsRequest | 
        try {
            CreateCommerceProduct201Response result = apiInstance.createCommerceProductOptions(productId, createCommerceProductOptionsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceProductOptions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **createCommerceProductOptionsRequest** | [**CreateCommerceProductOptionsRequest**](CreateCommerceProductOptionsRequest.md)|  | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceProductOptionsWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> createCommerceProductOptions createCommerceProductOptionsWithHttpInfo(productId, createCommerceProductOptionsRequest)

Add options

Adds option axes (e.g. Size, Color) and their values. With createVariants true the platform creates a variant for every new combination; otherwise existing variants take the first value. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        CreateCommerceProductOptionsRequest createCommerceProductOptionsRequest = new CreateCommerceProductOptionsRequest(); // CreateCommerceProductOptionsRequest | 
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.createCommerceProductOptionsWithHttpInfo(productId, createCommerceProductOptionsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceProductOptions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **createCommerceProductOptionsRequest** | [**CreateCommerceProductOptionsRequest**](CreateCommerceProductOptionsRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceProductVariants

> CreateCommerceProduct201Response createCommerceProductVariants(productId, createCommerceProductVariantsRequest)

Add variants

Adds variants to a product. Each variant names a value for every product option (create options first with POST .../options). A product&#39;s placeholder default variant is replaced when real ones arrive. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        CreateCommerceProductVariantsRequest createCommerceProductVariantsRequest = new CreateCommerceProductVariantsRequest(); // CreateCommerceProductVariantsRequest | 
        try {
            CreateCommerceProduct201Response result = apiInstance.createCommerceProductVariants(productId, createCommerceProductVariantsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceProductVariants");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **createCommerceProductVariantsRequest** | [**CreateCommerceProductVariantsRequest**](CreateCommerceProductVariantsRequest.md)|  | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceProductVariantsWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> createCommerceProductVariants createCommerceProductVariantsWithHttpInfo(productId, createCommerceProductVariantsRequest)

Add variants

Adds variants to a product. Each variant names a value for every product option (create options first with POST .../options). A product&#39;s placeholder default variant is replaced when real ones arrive. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        CreateCommerceProductVariantsRequest createCommerceProductVariantsRequest = new CreateCommerceProductVariantsRequest(); // CreateCommerceProductVariantsRequest | 
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.createCommerceProductVariantsWithHttpInfo(productId, createCommerceProductVariantsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceProductVariants");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **createCommerceProductVariantsRequest** | [**CreateCommerceProductVariantsRequest**](CreateCommerceProductVariantsRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## createCommerceRedirect

> CreateCommerceRedirect201Response createCommerceRedirect(createCommerceRedirectRequest)

Create a URL redirect

Creates a redirect from &#x60;path&#x60; (starting with &#x60;/&#x60;) to &#x60;target&#x60; (a path or a full URL) and returns it with status 201. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceRedirectRequest createCommerceRedirectRequest = new CreateCommerceRedirectRequest(); // CreateCommerceRedirectRequest | 
        try {
            CreateCommerceRedirect201Response result = apiInstance.createCommerceRedirect(createCommerceRedirectRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceRedirect");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceRedirectRequest** | [**CreateCommerceRedirectRequest**](CreateCommerceRedirectRequest.md)|  | |

### Return type

[**CreateCommerceRedirect201Response**](CreateCommerceRedirect201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Redirect created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## createCommerceRedirectWithHttpInfo

> ApiResponse<CreateCommerceRedirect201Response> createCommerceRedirect createCommerceRedirectWithHttpInfo(createCommerceRedirectRequest)

Create a URL redirect

Creates a redirect from &#x60;path&#x60; (starting with &#x60;/&#x60;) to &#x60;target&#x60; (a path or a full URL) and returns it with status 201. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        CreateCommerceRedirectRequest createCommerceRedirectRequest = new CreateCommerceRedirectRequest(); // CreateCommerceRedirectRequest | 
        try {
            ApiResponse<CreateCommerceRedirect201Response> response = apiInstance.createCommerceRedirectWithHttpInfo(createCommerceRedirectRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#createCommerceRedirect");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCommerceRedirectRequest** | [**CreateCommerceRedirectRequest**](CreateCommerceRedirectRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceRedirect201Response**](CreateCommerceRedirect201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Redirect created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceCatalogSync

> DeleteCommerceCatalogSync200Response deleteCommerceCatalogSync(syncId)

Stop a catalog sync

Stops syncing. Items already in the catalog stay there.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String syncId = "syncId_example"; // String | 
        try {
            DeleteCommerceCatalogSync200Response result = apiInstance.deleteCommerceCatalogSync(syncId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **syncId** | **String**|  | |

### Return type

[**DeleteCommerceCatalogSync200Response**](DeleteCommerceCatalogSync200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog sync stopped |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Catalog sync not found (code resource_not_found). |  -  |

## deleteCommerceCatalogSyncWithHttpInfo

> ApiResponse<DeleteCommerceCatalogSync200Response> deleteCommerceCatalogSync deleteCommerceCatalogSyncWithHttpInfo(syncId)

Stop a catalog sync

Stops syncing. Items already in the catalog stay there.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String syncId = "syncId_example"; // String | 
        try {
            ApiResponse<DeleteCommerceCatalogSync200Response> response = apiInstance.deleteCommerceCatalogSyncWithHttpInfo(syncId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **syncId** | **String**|  | |

### Return type

ApiResponse<[**DeleteCommerceCatalogSync200Response**](DeleteCommerceCatalogSync200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog sync stopped |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Catalog sync not found (code resource_not_found). |  -  |


## deleteCommerceCollection

> DeleteCommerceCollection200Response deleteCommerceCollection(collectionId, accountId)

Delete a collection

Deletes the collection. Its products are not affected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            DeleteCommerceCollection200Response result = apiInstance.deleteCommerceCollection(collectionId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**DeleteCommerceCollection200Response**](DeleteCommerceCollection200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceCollectionWithHttpInfo

> ApiResponse<DeleteCommerceCollection200Response> deleteCommerceCollection deleteCommerceCollectionWithHttpInfo(collectionId, accountId)

Delete a collection

Deletes the collection. Its products are not affected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<DeleteCommerceCollection200Response> response = apiInstance.deleteCommerceCollectionWithHttpInfo(collectionId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**DeleteCommerceCollection200Response**](DeleteCommerceCollection200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceCollectionMetafields

> DeleteCommerceProductMetafields200Response deleteCommerceCollectionMetafields(collectionId, accountId, keys)

Delete collection metafields

Deletes the collection metafields named in &#x60;keys&#x60; (comma-separated &#x60;namespace.key&#x60;, up to 25). Needs collections.metafields: WooCommerce answers 400 platform_not_supported.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String keys = "keys_example"; // String | Comma-separated namespace.key pairs.
        try {
            DeleteCommerceProductMetafields200Response result = apiInstance.deleteCommerceCollectionMetafields(collectionId, accountId, keys);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceCollectionMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **keys** | **String**| Comma-separated namespace.key pairs. | |

### Return type

[**DeleteCommerceProductMetafields200Response**](DeleteCommerceProductMetafields200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceCollectionMetafieldsWithHttpInfo

> ApiResponse<DeleteCommerceProductMetafields200Response> deleteCommerceCollectionMetafields deleteCommerceCollectionMetafieldsWithHttpInfo(collectionId, accountId, keys)

Delete collection metafields

Deletes the collection metafields named in &#x60;keys&#x60; (comma-separated &#x60;namespace.key&#x60;, up to 25). Needs collections.metafields: WooCommerce answers 400 platform_not_supported.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String keys = "keys_example"; // String | Comma-separated namespace.key pairs.
        try {
            ApiResponse<DeleteCommerceProductMetafields200Response> response = apiInstance.deleteCommerceCollectionMetafieldsWithHttpInfo(collectionId, accountId, keys);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceCollectionMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **keys** | **String**| Comma-separated namespace.key pairs. | |

### Return type

ApiResponse<[**DeleteCommerceProductMetafields200Response**](DeleteCommerceProductMetafields200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceDiscount

> DeleteCommerceDiscount200Response deleteCommerceDiscount(discountId, accountId)

Delete a discount

Deletes the discount; its codes stop working at checkout. This cannot be undone. Needs discounts.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            DeleteCommerceDiscount200Response result = apiInstance.deleteCommerceDiscount(discountId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**DeleteCommerceDiscount200Response**](DeleteCommerceDiscount200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceDiscountWithHttpInfo

> ApiResponse<DeleteCommerceDiscount200Response> deleteCommerceDiscount deleteCommerceDiscountWithHttpInfo(discountId, accountId)

Delete a discount

Deletes the discount; its codes stop working at checkout. This cannot be undone. Needs discounts.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<DeleteCommerceDiscount200Response> response = apiInstance.deleteCommerceDiscountWithHttpInfo(discountId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**DeleteCommerceDiscount200Response**](DeleteCommerceDiscount200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceMarketingActivity

> DeleteCommerceMarketingActivity200Response deleteCommerceMarketingActivity(remoteId, accountId)

Delete a marketing activity

Deletes the marketing activity you created with PUT /v1/commerce/marketing-activities, identified by the &#x60;remoteId&#x60; you gave it. Shopify only. Needs marketing.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String remoteId = "remoteId_example"; // String | The remoteId given when recording it.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            DeleteCommerceMarketingActivity200Response result = apiInstance.deleteCommerceMarketingActivity(remoteId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceMarketingActivity");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **remoteId** | **String**| The remoteId given when recording it. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**DeleteCommerceMarketingActivity200Response**](DeleteCommerceMarketingActivity200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceMarketingActivityWithHttpInfo

> ApiResponse<DeleteCommerceMarketingActivity200Response> deleteCommerceMarketingActivity deleteCommerceMarketingActivityWithHttpInfo(remoteId, accountId)

Delete a marketing activity

Deletes the marketing activity you created with PUT /v1/commerce/marketing-activities, identified by the &#x60;remoteId&#x60; you gave it. Shopify only. Needs marketing.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String remoteId = "remoteId_example"; // String | The remoteId given when recording it.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<DeleteCommerceMarketingActivity200Response> response = apiInstance.deleteCommerceMarketingActivityWithHttpInfo(remoteId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceMarketingActivity");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **remoteId** | **String**| The remoteId given when recording it. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**DeleteCommerceMarketingActivity200Response**](DeleteCommerceMarketingActivity200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceMenu

> DeleteCommerceMenu200Response deleteCommerceMenu(menuId, accountId)

Delete a navigation menu

Deletes the navigation menu. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String menuId = "menuId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            DeleteCommerceMenu200Response result = apiInstance.deleteCommerceMenu(menuId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **menuId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**DeleteCommerceMenu200Response**](DeleteCommerceMenu200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceMenuWithHttpInfo

> ApiResponse<DeleteCommerceMenu200Response> deleteCommerceMenu deleteCommerceMenuWithHttpInfo(menuId, accountId)

Delete a navigation menu

Deletes the navigation menu. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String menuId = "menuId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<DeleteCommerceMenu200Response> response = apiInstance.deleteCommerceMenuWithHttpInfo(menuId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **menuId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**DeleteCommerceMenu200Response**](DeleteCommerceMenu200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceMetaobject

> DeleteCommerceMetaobject200Response deleteCommerceMetaobject(metaobjectId, accountId)

Delete a metaobject

Deletes the metaobject. References to it from metafields stop resolving. Shopify only. Needs metaobjects.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String metaobjectId = "metaobjectId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            DeleteCommerceMetaobject200Response result = apiInstance.deleteCommerceMetaobject(metaobjectId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **metaobjectId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**DeleteCommerceMetaobject200Response**](DeleteCommerceMetaobject200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobject deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceMetaobjectWithHttpInfo

> ApiResponse<DeleteCommerceMetaobject200Response> deleteCommerceMetaobject deleteCommerceMetaobjectWithHttpInfo(metaobjectId, accountId)

Delete a metaobject

Deletes the metaobject. References to it from metafields stop resolving. Shopify only. Needs metaobjects.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String metaobjectId = "metaobjectId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<DeleteCommerceMetaobject200Response> response = apiInstance.deleteCommerceMetaobjectWithHttpInfo(metaobjectId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **metaobjectId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**DeleteCommerceMetaobject200Response**](DeleteCommerceMetaobject200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobject deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommercePage

> DeleteCommercePage200Response deleteCommercePage(pageId, accountId)

Delete a page

Deletes the page from the store. This cannot be undone. Needs pages.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String pageId = "pageId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            DeleteCommercePage200Response result = apiInstance.deleteCommercePage(pageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pageId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**DeleteCommercePage200Response**](DeleteCommercePage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommercePageWithHttpInfo

> ApiResponse<DeleteCommercePage200Response> deleteCommercePage deleteCommercePageWithHttpInfo(pageId, accountId)

Delete a page

Deletes the page from the store. This cannot be undone. Needs pages.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String pageId = "pageId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<DeleteCommercePage200Response> response = apiInstance.deleteCommercePageWithHttpInfo(pageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pageId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**DeleteCommercePage200Response**](DeleteCommercePage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommercePriceListPrices

> DeleteCommercePriceListPrices200Response deleteCommercePriceListPrices(priceListId, accountId, variantIds)

Remove fixed prices

The variants go back to the market&#39;s converted price. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String priceListId = "priceListId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String variantIds = "variantIds_example"; // String | Comma-separated ids.
        try {
            DeleteCommercePriceListPrices200Response result = apiInstance.deleteCommercePriceListPrices(priceListId, accountId, variantIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommercePriceListPrices");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **priceListId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **variantIds** | **String**| Comma-separated ids. | |

### Return type

[**DeleteCommercePriceListPrices200Response**](DeleteCommercePriceListPrices200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prices removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommercePriceListPricesWithHttpInfo

> ApiResponse<DeleteCommercePriceListPrices200Response> deleteCommercePriceListPrices deleteCommercePriceListPricesWithHttpInfo(priceListId, accountId, variantIds)

Remove fixed prices

The variants go back to the market&#39;s converted price. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String priceListId = "priceListId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String variantIds = "variantIds_example"; // String | Comma-separated ids.
        try {
            ApiResponse<DeleteCommercePriceListPrices200Response> response = apiInstance.deleteCommercePriceListPricesWithHttpInfo(priceListId, accountId, variantIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommercePriceListPrices");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **priceListId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **variantIds** | **String**| Comma-separated ids. | |

### Return type

ApiResponse<[**DeleteCommercePriceListPrices200Response**](DeleteCommercePriceListPrices200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prices removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceProductMetafields

> DeleteCommerceProductMetafields200Response deleteCommerceProductMetafields(productId, accountId, keys)

Delete product metafields

Deletes the product custom fields named in &#x60;keys&#x60; (comma-separated &#x60;namespace.key&#x60;, up to 25) and returns how many were deleted. Needs metafields.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String keys = "keys_example"; // String | Comma-separated namespace.key pairs.
        try {
            DeleteCommerceProductMetafields200Response result = apiInstance.deleteCommerceProductMetafields(productId, accountId, keys);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceProductMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **keys** | **String**| Comma-separated namespace.key pairs. | |

### Return type

[**DeleteCommerceProductMetafields200Response**](DeleteCommerceProductMetafields200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceProductMetafieldsWithHttpInfo

> ApiResponse<DeleteCommerceProductMetafields200Response> deleteCommerceProductMetafields deleteCommerceProductMetafieldsWithHttpInfo(productId, accountId, keys)

Delete product metafields

Deletes the product custom fields named in &#x60;keys&#x60; (comma-separated &#x60;namespace.key&#x60;, up to 25) and returns how many were deleted. Needs metafields.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String keys = "keys_example"; // String | Comma-separated namespace.key pairs.
        try {
            ApiResponse<DeleteCommerceProductMetafields200Response> response = apiInstance.deleteCommerceProductMetafieldsWithHttpInfo(productId, accountId, keys);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceProductMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **keys** | **String**| Comma-separated namespace.key pairs. | |

### Return type

ApiResponse<[**DeleteCommerceProductMetafields200Response**](DeleteCommerceProductMetafields200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceProductOptions

> CreateCommerceProduct201Response deleteCommerceProductOptions(productId, accountId, names)

Delete options

Deletes options by name, with the variants that depended on them. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String names = "names_example"; // String | Comma-separated option names.
        try {
            CreateCommerceProduct201Response result = apiInstance.deleteCommerceProductOptions(productId, accountId, names);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceProductOptions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **names** | **String**| Comma-separated option names. | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceProductOptionsWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> deleteCommerceProductOptions deleteCommerceProductOptionsWithHttpInfo(productId, accountId, names)

Delete options

Deletes options by name, with the variants that depended on them. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String names = "names_example"; // String | Comma-separated option names.
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.deleteCommerceProductOptionsWithHttpInfo(productId, accountId, names);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceProductOptions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **names** | **String**| Comma-separated option names. | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceProductVariants

> CreateCommerceProduct201Response deleteCommerceProductVariants(productId, accountId, variantIds)

Delete variants

Deletes the variants in &#x60;variantIds&#x60; (comma-separated, up to 100) and returns the updated product. A product keeps at least one variant, so deleting every variant is refused by the platform. Needs products.variants.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String variantIds = "variantIds_example"; // String | Comma-separated ids.
        try {
            CreateCommerceProduct201Response result = apiInstance.deleteCommerceProductVariants(productId, accountId, variantIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceProductVariants");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **variantIds** | **String**| Comma-separated ids. | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceProductVariantsWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> deleteCommerceProductVariants deleteCommerceProductVariantsWithHttpInfo(productId, accountId, variantIds)

Delete variants

Deletes the variants in &#x60;variantIds&#x60; (comma-separated, up to 100) and returns the updated product. A product keeps at least one variant, so deleting every variant is refused by the platform. Needs products.variants.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String variantIds = "variantIds_example"; // String | Comma-separated ids.
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.deleteCommerceProductVariantsWithHttpInfo(productId, accountId, variantIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceProductVariants");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **variantIds** | **String**| Comma-separated ids. | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## deleteCommerceRedirect

> DeleteCommerceRedirect200Response deleteCommerceRedirect(redirectId, accountId)

Delete a URL redirect

Deletes the redirect; the old path answers 404 again. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String redirectId = "redirectId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            DeleteCommerceRedirect200Response result = apiInstance.deleteCommerceRedirect(redirectId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceRedirect");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **redirectId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**DeleteCommerceRedirect200Response**](DeleteCommerceRedirect200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Redirect deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## deleteCommerceRedirectWithHttpInfo

> ApiResponse<DeleteCommerceRedirect200Response> deleteCommerceRedirect deleteCommerceRedirectWithHttpInfo(redirectId, accountId)

Delete a URL redirect

Deletes the redirect; the old path answers 404 again. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String redirectId = "redirectId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<DeleteCommerceRedirect200Response> response = apiInstance.deleteCommerceRedirectWithHttpInfo(redirectId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#deleteCommerceRedirect");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **redirectId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**DeleteCommerceRedirect200Response**](DeleteCommerceRedirect200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Redirect deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## duplicateCommerceProduct

> CreateCommerceProduct201Response duplicateCommerceProduct(productId, duplicateCommerceProductRequest)

Duplicate a product

Copies a product with its options, variants and (by default) images. The copy starts as a draft. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        DuplicateCommerceProductRequest duplicateCommerceProductRequest = new DuplicateCommerceProductRequest(); // DuplicateCommerceProductRequest | 
        try {
            CreateCommerceProduct201Response result = apiInstance.duplicateCommerceProduct(productId, duplicateCommerceProductRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#duplicateCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **duplicateCommerceProductRequest** | [**DuplicateCommerceProductRequest**](DuplicateCommerceProductRequest.md)|  | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product duplicated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## duplicateCommerceProductWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> duplicateCommerceProduct duplicateCommerceProductWithHttpInfo(productId, duplicateCommerceProductRequest)

Duplicate a product

Copies a product with its options, variants and (by default) images. The copy starts as a draft. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        DuplicateCommerceProductRequest duplicateCommerceProductRequest = new DuplicateCommerceProductRequest(); // DuplicateCommerceProductRequest | 
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.duplicateCommerceProductWithHttpInfo(productId, duplicateCommerceProductRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#duplicateCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **duplicateCommerceProductRequest** | [**DuplicateCommerceProductRequest**](DuplicateCommerceProductRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product duplicated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## getCommerceCatalogSync

> CreateCommerceCatalogSync202Response getCommerceCatalogSync(syncId)

Get a catalog sync

One catalog sync with the status and counts of its last run (&#x60;itemsSent&#x60;, &#x60;itemsSkipped&#x60;, &#x60;itemsDeleted&#x60;, &#x60;lastError&#x60;). Poll it after POST /v1/commerce/catalog-syncs/{syncId}/run to follow a run.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String syncId = "syncId_example"; // String | 
        try {
            CreateCommerceCatalogSync202Response result = apiInstance.getCommerceCatalogSync(syncId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **syncId** | **String**|  | |

### Return type

[**CreateCommerceCatalogSync202Response**](CreateCommerceCatalogSync202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog sync fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Catalog sync not found (code resource_not_found). |  -  |

## getCommerceCatalogSyncWithHttpInfo

> ApiResponse<CreateCommerceCatalogSync202Response> getCommerceCatalogSync getCommerceCatalogSyncWithHttpInfo(syncId)

Get a catalog sync

One catalog sync with the status and counts of its last run (&#x60;itemsSent&#x60;, &#x60;itemsSkipped&#x60;, &#x60;itemsDeleted&#x60;, &#x60;lastError&#x60;). Poll it after POST /v1/commerce/catalog-syncs/{syncId}/run to follow a run.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String syncId = "syncId_example"; // String | 
        try {
            ApiResponse<CreateCommerceCatalogSync202Response> response = apiInstance.getCommerceCatalogSyncWithHttpInfo(syncId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **syncId** | **String**|  | |

### Return type

ApiResponse<[**CreateCommerceCatalogSync202Response**](CreateCommerceCatalogSync202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog sync fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Catalog sync not found (code resource_not_found). |  -  |


## getCommerceCollection

> CreateCommerceCollection201Response getCommerceCollection(collectionId, accountId)

Get a collection

One collection (a category on WooCommerce) with its image, sort order and product count. List its products with GET /v1/commerce/products?collectionId&#x3D;. Needs collections.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            CreateCommerceCollection201Response result = apiInstance.getCommerceCollection(collectionId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**CreateCommerceCollection201Response**](CreateCommerceCollection201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## getCommerceCollectionWithHttpInfo

> ApiResponse<CreateCommerceCollection201Response> getCommerceCollection getCommerceCollectionWithHttpInfo(collectionId, accountId)

Get a collection

One collection (a category on WooCommerce) with its image, sort order and product count. List its products with GET /v1/commerce/products?collectionId&#x3D;. Needs collections.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<CreateCommerceCollection201Response> response = apiInstance.getCommerceCollectionWithHttpInfo(collectionId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**CreateCommerceCollection201Response**](CreateCommerceCollection201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## getCommerceDiscount

> CreateCommerceDiscount201Response getCommerceDiscount(discountId, accountId)

Get a discount

One discount with its value, targets, minimum, usage and schedule. Needs discounts.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            CreateCommerceDiscount201Response result = apiInstance.getCommerceDiscount(discountId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## getCommerceDiscountWithHttpInfo

> ApiResponse<CreateCommerceDiscount201Response> getCommerceDiscount getCommerceDiscountWithHttpInfo(discountId, accountId)

Get a discount

One discount with its value, targets, minimum, usage and schedule. Needs discounts.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<CreateCommerceDiscount201Response> response = apiInstance.getCommerceDiscountWithHttpInfo(discountId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## getCommerceMenu

> CreateCommerceMenu201Response getCommerceMenu(menuId, accountId)

Get a navigation menu

One navigation menu with its nested items. Shopify only. Needs navigation.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String menuId = "menuId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            CreateCommerceMenu201Response result = apiInstance.getCommerceMenu(menuId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **menuId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**CreateCommerceMenu201Response**](CreateCommerceMenu201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## getCommerceMenuWithHttpInfo

> ApiResponse<CreateCommerceMenu201Response> getCommerceMenu getCommerceMenuWithHttpInfo(menuId, accountId)

Get a navigation menu

One navigation menu with its nested items. Shopify only. Needs navigation.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String menuId = "menuId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<CreateCommerceMenu201Response> response = apiInstance.getCommerceMenuWithHttpInfo(menuId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **menuId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**CreateCommerceMenu201Response**](CreateCommerceMenu201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## getCommerceMetaobject

> CreateCommerceMetaobject201Response getCommerceMetaobject(metaobjectId, accountId)

Get a metaobject

One metaobject with its fields. Shopify only. Needs metaobjects.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String metaobjectId = "metaobjectId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            CreateCommerceMetaobject201Response result = apiInstance.getCommerceMetaobject(metaobjectId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **metaobjectId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**CreateCommerceMetaobject201Response**](CreateCommerceMetaobject201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobject fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## getCommerceMetaobjectWithHttpInfo

> ApiResponse<CreateCommerceMetaobject201Response> getCommerceMetaobject getCommerceMetaobjectWithHttpInfo(metaobjectId, accountId)

Get a metaobject

One metaobject with its fields. Shopify only. Needs metaobjects.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String metaobjectId = "metaobjectId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<CreateCommerceMetaobject201Response> response = apiInstance.getCommerceMetaobjectWithHttpInfo(metaobjectId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **metaobjectId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**CreateCommerceMetaobject201Response**](CreateCommerceMetaobject201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobject fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## getCommercePage

> CreateCommercePage201Response getCommercePage(pageId, accountId)

Get a page

One content page with its body. Needs pages.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String pageId = "pageId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            CreateCommercePage201Response result = apiInstance.getCommercePage(pageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pageId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**CreateCommercePage201Response**](CreateCommercePage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## getCommercePageWithHttpInfo

> ApiResponse<CreateCommercePage201Response> getCommercePage getCommercePageWithHttpInfo(pageId, accountId)

Get a page

One content page with its body. Needs pages.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String pageId = "pageId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<CreateCommercePage201Response> response = apiInstance.getCommercePageWithHttpInfo(pageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pageId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**CreateCommercePage201Response**](CreateCommercePage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## getCommerceProduct

> CreateCommerceProduct201Response getCommerceProduct(productId, accountId)

Get a product

One product with all its variants, options and images. Needs products.read. 404 product_not_found when the id does not exist in the store.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native product id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            CreateCommerceProduct201Response result = apiInstance.getCommerceProduct(productId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native product id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found (code account_not_found) or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## getCommerceProductWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> getCommerceProduct getCommerceProductWithHttpInfo(productId, accountId)

Get a product

One product with all its variants, options and images. Needs products.read. 404 product_not_found when the id does not exist in the store.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native product id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.getCommerceProductWithHttpInfo(productId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native product id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found (code account_not_found) or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## getCommerceStore

> GetCommerceStore200Response getCommerceStore(accountId)

Get a store

Returns the connected store with its currency, country and the &#x60;capabilities&#x60; it supports, so an integration can tell up front which Commerce operations the store serves. On Shopify, stock, sales channels, discounts, navigation, metaobjects, markets, marketing and image removal need permissions the store owner approves separately: &#x60;missingCapabilities&#x60; lists what is not granted yet and &#x60;grantPermissionsUrl&#x60; is the page where the owner approves it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            GetCommerceStore200Response result = apiInstance.getCommerceStore(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceStore");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**GetCommerceStore200Response**](GetCommerceStore200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Store fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## getCommerceStoreWithHttpInfo

> ApiResponse<GetCommerceStore200Response> getCommerceStore getCommerceStoreWithHttpInfo(accountId)

Get a store

Returns the connected store with its currency, country and the &#x60;capabilities&#x60; it supports, so an integration can tell up front which Commerce operations the store serves. On Shopify, stock, sales channels, discounts, navigation, metaobjects, markets, marketing and image removal need permissions the store owner approves separately: &#x60;missingCapabilities&#x60; lists what is not granted yet and &#x60;grantPermissionsUrl&#x60; is the page where the owner approves it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<GetCommerceStore200Response> response = apiInstance.getCommerceStoreWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#getCommerceStore");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**GetCommerceStore200Response**](GetCommerceStore200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Store fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceCatalogSyncs

> ListCommerceCatalogSyncs200Response listCommerceCatalogSyncs(accountId)

List catalog syncs

The ad-platform catalogs this store is kept in sync with.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceCatalogSyncs200Response result = apiInstance.listCommerceCatalogSyncs(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceCatalogSyncs");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceCatalogSyncs200Response**](ListCommerceCatalogSyncs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog syncs listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |

## listCommerceCatalogSyncsWithHttpInfo

> ApiResponse<ListCommerceCatalogSyncs200Response> listCommerceCatalogSyncs listCommerceCatalogSyncsWithHttpInfo(accountId)

List catalog syncs

The ad-platform catalogs this store is kept in sync with.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceCatalogSyncs200Response> response = apiInstance.listCommerceCatalogSyncsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceCatalogSyncs");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceCatalogSyncs200Response**](ListCommerceCatalogSyncs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog syncs listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |


## listCommerceChannels

> ListCommerceChannels200Response listCommerceChannels(accountId)

List sales channels

Where products and collections can be published: the online store, Shop, POS and installed channel apps. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceChannels200Response result = apiInstance.listCommerceChannels(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceChannels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceChannels200Response**](ListCommerceChannels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channels listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceChannelsWithHttpInfo

> ApiResponse<ListCommerceChannels200Response> listCommerceChannels listCommerceChannelsWithHttpInfo(accountId)

List sales channels

Where products and collections can be published: the online store, Shop, POS and installed channel apps. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceChannels200Response> response = apiInstance.listCommerceChannelsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceChannels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceChannels200Response**](ListCommerceChannels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channels listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceCollectionMetafields

> ListCommerceProductMetafields200Response listCommerceCollectionMetafields(collectionId, accountId)

List collection metafields

The collection&#39;s metafields as namespace, key, type and value. Needs collections.metafields: WooCommerce keeps custom fields on products only and answers 400 platform_not_supported.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceProductMetafields200Response result = apiInstance.listCommerceCollectionMetafields(collectionId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceCollectionMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceCollectionMetafieldsWithHttpInfo

> ApiResponse<ListCommerceProductMetafields200Response> listCommerceCollectionMetafields listCommerceCollectionMetafieldsWithHttpInfo(collectionId, accountId)

List collection metafields

The collection&#39;s metafields as namespace, key, type and value. Needs collections.metafields: WooCommerce keeps custom fields on products only and answers 400 platform_not_supported.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceProductMetafields200Response> response = apiInstance.listCommerceCollectionMetafieldsWithHttpInfo(collectionId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceCollectionMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceCollections

> ListCommerceCollections200Response listCommerceCollections(accountId, limit, cursor, query)

List collections

Lists the store&#39;s product collections. Cursor-paginated like products. List a collection&#39;s products with &#x60;GET /v1/commerce/products?collectionId&#x3D;...&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform collection search syntax (Shopify: title, handle, collection_type, ...).
        try {
            ListCommerceCollections200Response result = apiInstance.listCommerceCollections(accountId, limit, cursor, query);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceCollections");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform collection search syntax (Shopify: title, handle, collection_type, ...). | [optional] |

### Return type

[**ListCommerceCollections200Response**](ListCommerceCollections200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collections listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceCollectionsWithHttpInfo

> ApiResponse<ListCommerceCollections200Response> listCommerceCollections listCommerceCollectionsWithHttpInfo(accountId, limit, cursor, query)

List collections

Lists the store&#39;s product collections. Cursor-paginated like products. List a collection&#39;s products with &#x60;GET /v1/commerce/products?collectionId&#x3D;...&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform collection search syntax (Shopify: title, handle, collection_type, ...).
        try {
            ApiResponse<ListCommerceCollections200Response> response = apiInstance.listCommerceCollectionsWithHttpInfo(accountId, limit, cursor, query);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceCollections");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform collection search syntax (Shopify: title, handle, collection_type, ...). | [optional] |

### Return type

ApiResponse<[**ListCommerceCollections200Response**](ListCommerceCollections200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collections listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceDiscounts

> ListCommerceDiscounts200Response listCommerceDiscounts(accountId, limit, cursor, query)

List discounts

The store&#39;s discounts (Shopify code and automatic discounts, WooCommerce coupons), cursor-paginated with &#x60;limit&#x60;, &#x60;cursor&#x60; and an optional &#x60;query&#x60;. Each discount lists its first 10 codes; &#x60;codeCount&#x60; has the total. Needs discounts.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform search syntax, passed through.
        try {
            ListCommerceDiscounts200Response result = apiInstance.listCommerceDiscounts(accountId, limit, cursor, query);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceDiscounts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform search syntax, passed through. | [optional] |

### Return type

[**ListCommerceDiscounts200Response**](ListCommerceDiscounts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discounts listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceDiscountsWithHttpInfo

> ApiResponse<ListCommerceDiscounts200Response> listCommerceDiscounts listCommerceDiscountsWithHttpInfo(accountId, limit, cursor, query)

List discounts

The store&#39;s discounts (Shopify code and automatic discounts, WooCommerce coupons), cursor-paginated with &#x60;limit&#x60;, &#x60;cursor&#x60; and an optional &#x60;query&#x60;. Each discount lists its first 10 codes; &#x60;codeCount&#x60; has the total. Needs discounts.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform search syntax, passed through.
        try {
            ApiResponse<ListCommerceDiscounts200Response> response = apiInstance.listCommerceDiscountsWithHttpInfo(accountId, limit, cursor, query);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceDiscounts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform search syntax, passed through. | [optional] |

### Return type

ApiResponse<[**ListCommerceDiscounts200Response**](ListCommerceDiscounts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discounts listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceInventory

> ListCommerceInventory200Response listCommerceInventory(accountId, productId)

Get a product&#39;s stock

Stock per variant and location: available, on hand, committed to orders and incoming. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String productId = "productId_example"; // String | 
        try {
            ListCommerceInventory200Response result = apiInstance.listCommerceInventory(accountId, productId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceInventory");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **productId** | **String**|  | |

### Return type

[**ListCommerceInventory200Response**](ListCommerceInventory200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stock fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceInventoryWithHttpInfo

> ApiResponse<ListCommerceInventory200Response> listCommerceInventory listCommerceInventoryWithHttpInfo(accountId, productId)

Get a product&#39;s stock

Stock per variant and location: available, on hand, committed to orders and incoming. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String productId = "productId_example"; // String | 
        try {
            ApiResponse<ListCommerceInventory200Response> response = apiInstance.listCommerceInventoryWithHttpInfo(accountId, productId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceInventory");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **productId** | **String**|  | |

### Return type

ApiResponse<[**ListCommerceInventory200Response**](ListCommerceInventory200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stock fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceLocations

> ListCommerceLocations200Response listCommerceLocations(accountId)

List locations

The store&#39;s stock locations (warehouses, shops). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceLocations200Response result = apiInstance.listCommerceLocations(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceLocations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceLocations200Response**](ListCommerceLocations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceLocationsWithHttpInfo

> ApiResponse<ListCommerceLocations200Response> listCommerceLocations listCommerceLocationsWithHttpInfo(accountId)

List locations

The store&#39;s stock locations (warehouses, shops). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceLocations200Response> response = apiInstance.listCommerceLocationsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceLocations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceLocations200Response**](ListCommerceLocations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceMarkets

> ListCommerceMarkets200Response listCommerceMarkets(accountId)

List markets

The regions the store sells to, each with its own currency and pricing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceMarkets200Response result = apiInstance.listCommerceMarkets(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMarkets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceMarkets200Response**](ListCommerceMarkets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Markets listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceMarketsWithHttpInfo

> ApiResponse<ListCommerceMarkets200Response> listCommerceMarkets listCommerceMarketsWithHttpInfo(accountId)

List markets

The regions the store sells to, each with its own currency and pricing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceMarkets200Response> response = apiInstance.listCommerceMarketsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMarkets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceMarkets200Response**](ListCommerceMarkets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Markets listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceMenus

> ListCommerceMenus200Response listCommerceMenus(accountId)

List navigation menus

The store&#39;s navigation menus with their items. Shopify only. Needs navigation.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceMenus200Response result = apiInstance.listCommerceMenus(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMenus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceMenus200Response**](ListCommerceMenus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menus listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceMenusWithHttpInfo

> ApiResponse<ListCommerceMenus200Response> listCommerceMenus listCommerceMenusWithHttpInfo(accountId)

List navigation menus

The store&#39;s navigation menus with their items. Shopify only. Needs navigation.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceMenus200Response> response = apiInstance.listCommerceMenusWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMenus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceMenus200Response**](ListCommerceMenus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menus listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceMetaobjectDefinitions

> ListCommerceMetaobjectDefinitions200Response listCommerceMetaobjectDefinitions(accountId)

List metaobject definitions

The custom content types defined on the store and their fields. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceMetaobjectDefinitions200Response result = apiInstance.listCommerceMetaobjectDefinitions(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMetaobjectDefinitions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceMetaobjectDefinitions200Response**](ListCommerceMetaobjectDefinitions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Definitions listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceMetaobjectDefinitionsWithHttpInfo

> ApiResponse<ListCommerceMetaobjectDefinitions200Response> listCommerceMetaobjectDefinitions listCommerceMetaobjectDefinitionsWithHttpInfo(accountId)

List metaobject definitions

The custom content types defined on the store and their fields. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceMetaobjectDefinitions200Response> response = apiInstance.listCommerceMetaobjectDefinitionsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMetaobjectDefinitions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceMetaobjectDefinitions200Response**](ListCommerceMetaobjectDefinitions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Definitions listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceMetaobjects

> ListCommerceMetaobjects200Response listCommerceMetaobjects(accountId, type, limit, cursor)

List metaobjects of a type

The metaobjects of one &#x60;type&#x60; (a definition handle from GET /v1/commerce/metaobject-definitions), cursor-paginated with &#x60;limit&#x60; and &#x60;cursor&#x60;. Shopify only. Needs metaobjects.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String type = "type_example"; // String | Definition type from GET /v1/commerce/metaobject-definitions.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ListCommerceMetaobjects200Response result = apiInstance.listCommerceMetaobjects(accountId, type, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMetaobjects");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **type** | **String**| Definition type from GET /v1/commerce/metaobject-definitions. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |

### Return type

[**ListCommerceMetaobjects200Response**](ListCommerceMetaobjects200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobjects listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceMetaobjectsWithHttpInfo

> ApiResponse<ListCommerceMetaobjects200Response> listCommerceMetaobjects listCommerceMetaobjectsWithHttpInfo(accountId, type, limit, cursor)

List metaobjects of a type

The metaobjects of one &#x60;type&#x60; (a definition handle from GET /v1/commerce/metaobject-definitions), cursor-paginated with &#x60;limit&#x60; and &#x60;cursor&#x60;. Shopify only. Needs metaobjects.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String type = "type_example"; // String | Definition type from GET /v1/commerce/metaobject-definitions.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ApiResponse<ListCommerceMetaobjects200Response> response = apiInstance.listCommerceMetaobjectsWithHttpInfo(accountId, type, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceMetaobjects");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **type** | **String**| Definition type from GET /v1/commerce/metaobject-definitions. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListCommerceMetaobjects200Response**](ListCommerceMetaobjects200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobjects listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommercePages

> ListCommercePages200Response listCommercePages(accountId, limit, cursor, query)

List pages

The store&#39;s content pages (Shopify online store pages, WordPress pages), cursor-paginated with &#x60;limit&#x60;, &#x60;cursor&#x60; and an optional &#x60;query&#x60;. Needs pages.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform search syntax, passed through.
        try {
            ListCommercePages200Response result = apiInstance.listCommercePages(accountId, limit, cursor, query);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommercePages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform search syntax, passed through. | [optional] |

### Return type

[**ListCommercePages200Response**](ListCommercePages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommercePagesWithHttpInfo

> ApiResponse<ListCommercePages200Response> listCommercePages listCommercePagesWithHttpInfo(accountId, limit, cursor, query)

List pages

The store&#39;s content pages (Shopify online store pages, WordPress pages), cursor-paginated with &#x60;limit&#x60;, &#x60;cursor&#x60; and an optional &#x60;query&#x60;. Needs pages.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform search syntax, passed through.
        try {
            ApiResponse<ListCommercePages200Response> response = apiInstance.listCommercePagesWithHttpInfo(accountId, limit, cursor, query);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommercePages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform search syntax, passed through. | [optional] |

### Return type

ApiResponse<[**ListCommercePages200Response**](ListCommercePages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommercePriceLists

> ListCommercePriceLists200Response listCommercePriceLists(accountId)

List price lists

Price lists hold fixed prices per variant for a market. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommercePriceLists200Response result = apiInstance.listCommercePriceLists(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommercePriceLists");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommercePriceLists200Response**](ListCommercePriceLists200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Price lists listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommercePriceListsWithHttpInfo

> ApiResponse<ListCommercePriceLists200Response> listCommercePriceLists listCommercePriceListsWithHttpInfo(accountId)

List price lists

Price lists hold fixed prices per variant for a market. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommercePriceLists200Response> response = apiInstance.listCommercePriceListsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommercePriceLists");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommercePriceLists200Response**](ListCommercePriceLists200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Price lists listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceProductMetafields

> ListCommerceProductMetafields200Response listCommerceProductMetafields(productId, accountId)

List product metafields

The product&#39;s custom fields (metafields on Shopify, public meta on WooCommerce) as namespace, key, type and value. Needs metafields.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ListCommerceProductMetafields200Response result = apiInstance.listCommerceProductMetafields(productId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceProductMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceProductMetafieldsWithHttpInfo

> ApiResponse<ListCommerceProductMetafields200Response> listCommerceProductMetafields listCommerceProductMetafieldsWithHttpInfo(productId, accountId)

List product metafields

The product&#39;s custom fields (metafields on Shopify, public meta on WooCommerce) as namespace, key, type and value. Needs metafields.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        try {
            ApiResponse<ListCommerceProductMetafields200Response> response = apiInstance.listCommerceProductMetafieldsWithHttpInfo(productId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceProductMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |

### Return type

ApiResponse<[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceProducts

> ListCommerceProducts200Response listCommerceProducts(accountId, limit, cursor, status, query, collectionId)

List products

Lists the store&#39;s products with their variants, options and images. Cursor-paginated: pass &#x60;limit&#x60; (1-100, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;, which is null on the last page. Filter with &#x60;status&#x60; and/or &#x60;query&#x60; (the platform&#39;s product search syntax, passed through verbatim). A status the platform has no equivalent of returns an empty page. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        CommerceProductStatus status = CommerceProductStatus.fromValue("active"); // CommerceProductStatus | 
        String query = "query_example"; // String | Platform product search syntax (Shopify: title, vendor, product_type, tag, sku, handle, ...).
        String collectionId = "collectionId_example"; // String | Only products in this collection.
        try {
            ListCommerceProducts200Response result = apiInstance.listCommerceProducts(accountId, limit, cursor, status, query, collectionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceProducts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |
| **status** | [**CommerceProductStatus**](.md)|  | [optional] [enum: active, draft, pending_review, rejected, inactive, archived, deleted] |
| **query** | **String**| Platform product search syntax (Shopify: title, vendor, product_type, tag, sku, handle, ...). | [optional] |
| **collectionId** | **String**| Only products in this collection. | [optional] |

### Return type

[**ListCommerceProducts200Response**](ListCommerceProducts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). A Shopify store connected before product access was added must be reconnected through GET /v1/connect/shopify. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceProductsWithHttpInfo

> ApiResponse<ListCommerceProducts200Response> listCommerceProducts listCommerceProductsWithHttpInfo(accountId, limit, cursor, status, query, collectionId)

List products

Lists the store&#39;s products with their variants, options and images. Cursor-paginated: pass &#x60;limit&#x60; (1-100, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;, which is null on the last page. Filter with &#x60;status&#x60; and/or &#x60;query&#x60; (the platform&#39;s product search syntax, passed through verbatim). A status the platform has no equivalent of returns an empty page. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        CommerceProductStatus status = CommerceProductStatus.fromValue("active"); // CommerceProductStatus | 
        String query = "query_example"; // String | Platform product search syntax (Shopify: title, vendor, product_type, tag, sku, handle, ...).
        String collectionId = "collectionId_example"; // String | Only products in this collection.
        try {
            ApiResponse<ListCommerceProducts200Response> response = apiInstance.listCommerceProductsWithHttpInfo(accountId, limit, cursor, status, query, collectionId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceProducts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |
| **status** | [**CommerceProductStatus**](.md)|  | [optional] [enum: active, draft, pending_review, rejected, inactive, archived, deleted] |
| **query** | **String**| Platform product search syntax (Shopify: title, vendor, product_type, tag, sku, handle, ...). | [optional] |
| **collectionId** | **String**| Only products in this collection. | [optional] |

### Return type

ApiResponse<[**ListCommerceProducts200Response**](ListCommerceProducts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). A Shopify store connected before product access was added must be reconnected through GET /v1/connect/shopify. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## listCommerceRedirects

> ListCommerceRedirects200Response listCommerceRedirects(accountId, limit, cursor, query)

List URL redirects

The store&#39;s URL redirects (old path to new target), cursor-paginated with &#x60;limit&#x60;, &#x60;cursor&#x60; and an optional &#x60;query&#x60; on the path. Shopify only. Needs navigation.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform search syntax, passed through.
        try {
            ListCommerceRedirects200Response result = apiInstance.listCommerceRedirects(accountId, limit, cursor, query);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceRedirects");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform search syntax, passed through. | [optional] |

### Return type

[**ListCommerceRedirects200Response**](ListCommerceRedirects200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Redirects listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## listCommerceRedirectsWithHttpInfo

> ApiResponse<ListCommerceRedirects200Response> listCommerceRedirects listCommerceRedirectsWithHttpInfo(accountId, limit, cursor, query)

List URL redirects

The store&#39;s URL redirects (old path to new target), cursor-paginated with &#x60;limit&#x60;, &#x60;cursor&#x60; and an optional &#x60;query&#x60; on the path. Shopify only. Needs navigation.read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | 
        String query = "query_example"; // String | Platform search syntax, passed through.
        try {
            ApiResponse<ListCommerceRedirects200Response> response = apiInstance.listCommerceRedirectsWithHttpInfo(accountId, limit, cursor, query);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#listCommerceRedirects");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected store SocialAccount id. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **query** | **String**| Platform search syntax, passed through. | [optional] |

### Return type

ApiResponse<[**ListCommerceRedirects200Response**](ListCommerceRedirects200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Redirects listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## removeCommerceProductImages

> CreateCommerceProduct201Response removeCommerceProductImages(productId, accountId, imageIds)

Remove images

Removes images from the product by image id (the &#x60;id&#x60; on each image). The file stays in the store&#39;s media library. Needs the products.images_remove capability. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String imageIds = "imageIds_example"; // String | Comma-separated ids.
        try {
            CreateCommerceProduct201Response result = apiInstance.removeCommerceProductImages(productId, accountId, imageIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#removeCommerceProductImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **imageIds** | **String**| Comma-separated ids. | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## removeCommerceProductImagesWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> removeCommerceProductImages removeCommerceProductImagesWithHttpInfo(productId, accountId, imageIds)

Remove images

Removes images from the product by image id (the &#x60;id&#x60; on each image). The file stays in the store&#39;s media library. Needs the products.images_remove capability. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        String accountId = "accountId_example"; // String | Connected store SocialAccount id.
        String imageIds = "imageIds_example"; // String | Comma-separated ids.
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.removeCommerceProductImagesWithHttpInfo(productId, accountId, imageIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#removeCommerceProductImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **accountId** | **String**| Connected store SocialAccount id. | |
| **imageIds** | **String**| Comma-separated ids. | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## reorderCommerceCollectionProducts

> ReorderCommerceProductImages200Response reorderCommerceCollectionProducts(collectionId, reorderCommerceCollectionProductsRequest)

Reorder products in a collection

Moves products to new 0-based positions. Only for collections sorted &#x60;manual&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        ReorderCommerceCollectionProductsRequest reorderCommerceCollectionProductsRequest = new ReorderCommerceCollectionProductsRequest(); // ReorderCommerceCollectionProductsRequest | 
        try {
            ReorderCommerceProductImages200Response result = apiInstance.reorderCommerceCollectionProducts(collectionId, reorderCommerceCollectionProductsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#reorderCommerceCollectionProducts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **reorderCommerceCollectionProductsRequest** | [**ReorderCommerceCollectionProductsRequest**](ReorderCommerceCollectionProductsRequest.md)|  | |

### Return type

[**ReorderCommerceProductImages200Response**](ReorderCommerceProductImages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reorder accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## reorderCommerceCollectionProductsWithHttpInfo

> ApiResponse<ReorderCommerceProductImages200Response> reorderCommerceCollectionProducts reorderCommerceCollectionProductsWithHttpInfo(collectionId, reorderCommerceCollectionProductsRequest)

Reorder products in a collection

Moves products to new 0-based positions. Only for collections sorted &#x60;manual&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        ReorderCommerceCollectionProductsRequest reorderCommerceCollectionProductsRequest = new ReorderCommerceCollectionProductsRequest(); // ReorderCommerceCollectionProductsRequest | 
        try {
            ApiResponse<ReorderCommerceProductImages200Response> response = apiInstance.reorderCommerceCollectionProductsWithHttpInfo(collectionId, reorderCommerceCollectionProductsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#reorderCommerceCollectionProducts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **reorderCommerceCollectionProductsRequest** | [**ReorderCommerceCollectionProductsRequest**](ReorderCommerceCollectionProductsRequest.md)|  | |

### Return type

ApiResponse<[**ReorderCommerceProductImages200Response**](ReorderCommerceProductImages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reorder accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## reorderCommerceProductImages

> ReorderCommerceProductImages200Response reorderCommerceProductImages(productId, reorderCommerceProductImagesRequest)

Reorder images

Puts the product&#39;s images in the given order; the first becomes the featured image. &#x60;pending&#x60; is true while the platform finishes in the background. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        ReorderCommerceProductImagesRequest reorderCommerceProductImagesRequest = new ReorderCommerceProductImagesRequest(); // ReorderCommerceProductImagesRequest | 
        try {
            ReorderCommerceProductImages200Response result = apiInstance.reorderCommerceProductImages(productId, reorderCommerceProductImagesRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#reorderCommerceProductImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **reorderCommerceProductImagesRequest** | [**ReorderCommerceProductImagesRequest**](ReorderCommerceProductImagesRequest.md)|  | |

### Return type

[**ReorderCommerceProductImages200Response**](ReorderCommerceProductImages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reorder accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## reorderCommerceProductImagesWithHttpInfo

> ApiResponse<ReorderCommerceProductImages200Response> reorderCommerceProductImages reorderCommerceProductImagesWithHttpInfo(productId, reorderCommerceProductImagesRequest)

Reorder images

Puts the product&#39;s images in the given order; the first becomes the featured image. &#x60;pending&#x60; is true while the platform finishes in the background. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        ReorderCommerceProductImagesRequest reorderCommerceProductImagesRequest = new ReorderCommerceProductImagesRequest(); // ReorderCommerceProductImagesRequest | 
        try {
            ApiResponse<ReorderCommerceProductImages200Response> response = apiInstance.reorderCommerceProductImagesWithHttpInfo(productId, reorderCommerceProductImagesRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#reorderCommerceProductImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **reorderCommerceProductImagesRequest** | [**ReorderCommerceProductImagesRequest**](ReorderCommerceProductImagesRequest.md)|  | |

### Return type

ApiResponse<[**ReorderCommerceProductImages200Response**](ReorderCommerceProductImages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reorder accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## runCommerceCatalogSync

> CreateCommerceCatalogSync202Response runCommerceCatalogSync(syncId)

Run a catalog sync now

Queues a full run. Poll GET /v1/commerce/catalog-syncs/{syncId} for the outcome.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String syncId = "syncId_example"; // String | 
        try {
            CreateCommerceCatalogSync202Response result = apiInstance.runCommerceCatalogSync(syncId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#runCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **syncId** | **String**|  | |

### Return type

[**CreateCommerceCatalogSync202Response**](CreateCommerceCatalogSync202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run queued |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Catalog sync not found (code resource_not_found). |  -  |
| **409** | A run is already in progress (code catalog_sync_conflict). |  -  |

## runCommerceCatalogSyncWithHttpInfo

> ApiResponse<CreateCommerceCatalogSync202Response> runCommerceCatalogSync runCommerceCatalogSyncWithHttpInfo(syncId)

Run a catalog sync now

Queues a full run. Poll GET /v1/commerce/catalog-syncs/{syncId} for the outcome.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String syncId = "syncId_example"; // String | 
        try {
            ApiResponse<CreateCommerceCatalogSync202Response> response = apiInstance.runCommerceCatalogSyncWithHttpInfo(syncId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#runCommerceCatalogSync");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **syncId** | **String**|  | |

### Return type

ApiResponse<[**CreateCommerceCatalogSync202Response**](CreateCommerceCatalogSync202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run queued |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Catalog sync not found (code resource_not_found). |  -  |
| **409** | A run is already in progress (code catalog_sync_conflict). |  -  |


## setCommerceCollectionMetafields

> ListCommerceProductMetafields200Response setCommerceCollectionMetafields(collectionId, setCommerceProductMetafieldsRequest)

Set collection metafields

Creates or updates custom fields by namespace and key. Needs collections.metafields: WooCommerce keeps custom fields on products only and answers 400 platform_not_supported. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        SetCommerceProductMetafieldsRequest setCommerceProductMetafieldsRequest = new SetCommerceProductMetafieldsRequest(); // SetCommerceProductMetafieldsRequest | 
        try {
            ListCommerceProductMetafields200Response result = apiInstance.setCommerceCollectionMetafields(collectionId, setCommerceProductMetafieldsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommerceCollectionMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **setCommerceProductMetafieldsRequest** | [**SetCommerceProductMetafieldsRequest**](SetCommerceProductMetafieldsRequest.md)|  | |

### Return type

[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## setCommerceCollectionMetafieldsWithHttpInfo

> ApiResponse<ListCommerceProductMetafields200Response> setCommerceCollectionMetafields setCommerceCollectionMetafieldsWithHttpInfo(collectionId, setCommerceProductMetafieldsRequest)

Set collection metafields

Creates or updates custom fields by namespace and key. Needs collections.metafields: WooCommerce keeps custom fields on products only and answers 400 platform_not_supported. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native id.
        SetCommerceProductMetafieldsRequest setCommerceProductMetafieldsRequest = new SetCommerceProductMetafieldsRequest(); // SetCommerceProductMetafieldsRequest | 
        try {
            ApiResponse<ListCommerceProductMetafields200Response> response = apiInstance.setCommerceCollectionMetafieldsWithHttpInfo(collectionId, setCommerceProductMetafieldsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommerceCollectionMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native id. | |
| **setCommerceProductMetafieldsRequest** | [**SetCommerceProductMetafieldsRequest**](SetCommerceProductMetafieldsRequest.md)|  | |

### Return type

ApiResponse<[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## setCommerceDiscountActive

> CreateCommerceDiscount201Response setCommerceDiscountActive(discountId, setCommerceDiscountActiveRequest)

Activate or deactivate a discount

Deactivating ends the discount now; activating starts it now. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        SetCommerceDiscountActiveRequest setCommerceDiscountActiveRequest = new SetCommerceDiscountActiveRequest(); // SetCommerceDiscountActiveRequest | 
        try {
            CreateCommerceDiscount201Response result = apiInstance.setCommerceDiscountActive(discountId, setCommerceDiscountActiveRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommerceDiscountActive");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **setCommerceDiscountActiveRequest** | [**SetCommerceDiscountActiveRequest**](SetCommerceDiscountActiveRequest.md)|  | |

### Return type

[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount state changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## setCommerceDiscountActiveWithHttpInfo

> ApiResponse<CreateCommerceDiscount201Response> setCommerceDiscountActive setCommerceDiscountActiveWithHttpInfo(discountId, setCommerceDiscountActiveRequest)

Activate or deactivate a discount

Deactivating ends the discount now; activating starts it now. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        SetCommerceDiscountActiveRequest setCommerceDiscountActiveRequest = new SetCommerceDiscountActiveRequest(); // SetCommerceDiscountActiveRequest | 
        try {
            ApiResponse<CreateCommerceDiscount201Response> response = apiInstance.setCommerceDiscountActiveWithHttpInfo(discountId, setCommerceDiscountActiveRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommerceDiscountActive");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **setCommerceDiscountActiveRequest** | [**SetCommerceDiscountActiveRequest**](SetCommerceDiscountActiveRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount state changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## setCommercePriceListPrices

> SetCommercePriceListPrices200Response setCommercePriceListPrices(priceListId, setCommercePriceListPricesRequest)

Set fixed prices

Sets fixed prices for variants in the price list&#39;s currency, overriding the converted price in that market. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String priceListId = "priceListId_example"; // String | Platform-native id.
        SetCommercePriceListPricesRequest setCommercePriceListPricesRequest = new SetCommercePriceListPricesRequest(); // SetCommercePriceListPricesRequest | 
        try {
            SetCommercePriceListPrices200Response result = apiInstance.setCommercePriceListPrices(priceListId, setCommercePriceListPricesRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommercePriceListPrices");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **priceListId** | **String**| Platform-native id. | |
| **setCommercePriceListPricesRequest** | [**SetCommercePriceListPricesRequest**](SetCommercePriceListPricesRequest.md)|  | |

### Return type

[**SetCommercePriceListPrices200Response**](SetCommercePriceListPrices200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prices set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## setCommercePriceListPricesWithHttpInfo

> ApiResponse<SetCommercePriceListPrices200Response> setCommercePriceListPrices setCommercePriceListPricesWithHttpInfo(priceListId, setCommercePriceListPricesRequest)

Set fixed prices

Sets fixed prices for variants in the price list&#39;s currency, overriding the converted price in that market. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String priceListId = "priceListId_example"; // String | Platform-native id.
        SetCommercePriceListPricesRequest setCommercePriceListPricesRequest = new SetCommercePriceListPricesRequest(); // SetCommercePriceListPricesRequest | 
        try {
            ApiResponse<SetCommercePriceListPrices200Response> response = apiInstance.setCommercePriceListPricesWithHttpInfo(priceListId, setCommercePriceListPricesRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommercePriceListPrices");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **priceListId** | **String**| Platform-native id. | |
| **setCommercePriceListPricesRequest** | [**SetCommercePriceListPricesRequest**](SetCommercePriceListPricesRequest.md)|  | |

### Return type

ApiResponse<[**SetCommercePriceListPrices200Response**](SetCommercePriceListPrices200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prices set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## setCommerceProductMetafields

> ListCommerceProductMetafields200Response setCommerceProductMetafields(productId, setCommerceProductMetafieldsRequest)

Set product metafields

Creates or updates custom fields by namespace and key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        SetCommerceProductMetafieldsRequest setCommerceProductMetafieldsRequest = new SetCommerceProductMetafieldsRequest(); // SetCommerceProductMetafieldsRequest | 
        try {
            ListCommerceProductMetafields200Response result = apiInstance.setCommerceProductMetafields(productId, setCommerceProductMetafieldsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommerceProductMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **setCommerceProductMetafieldsRequest** | [**SetCommerceProductMetafieldsRequest**](SetCommerceProductMetafieldsRequest.md)|  | |

### Return type

[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## setCommerceProductMetafieldsWithHttpInfo

> ApiResponse<ListCommerceProductMetafields200Response> setCommerceProductMetafields setCommerceProductMetafieldsWithHttpInfo(productId, setCommerceProductMetafieldsRequest)

Set product metafields

Creates or updates custom fields by namespace and key. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native id.
        SetCommerceProductMetafieldsRequest setCommerceProductMetafieldsRequest = new SetCommerceProductMetafieldsRequest(); // SetCommerceProductMetafieldsRequest | 
        try {
            ApiResponse<ListCommerceProductMetafields200Response> response = apiInstance.setCommerceProductMetafieldsWithHttpInfo(productId, setCommerceProductMetafieldsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#setCommerceProductMetafields");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native id. | |
| **setCommerceProductMetafieldsRequest** | [**SetCommerceProductMetafieldsRequest**](SetCommerceProductMetafieldsRequest.md)|  | |

### Return type

ApiResponse<[**ListCommerceProductMetafields200Response**](ListCommerceProductMetafields200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metafields set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommerceCollection

> CreateCommerceCollection201Response updateCommerceCollection(collectionId, updateCommerceCollectionRequest)

Update a collection

Partial update; at least one field besides accountId is required. Change membership with POST /v1/commerce/collections/{collectionId}/products.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        UpdateCommerceCollectionRequest updateCommerceCollectionRequest = new UpdateCommerceCollectionRequest(); // UpdateCommerceCollectionRequest | 
        try {
            CreateCommerceCollection201Response result = apiInstance.updateCommerceCollection(collectionId, updateCommerceCollectionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **updateCommerceCollectionRequest** | [**UpdateCommerceCollectionRequest**](UpdateCommerceCollectionRequest.md)|  | |

### Return type

[**CreateCommerceCollection201Response**](CreateCommerceCollection201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommerceCollectionWithHttpInfo

> ApiResponse<CreateCommerceCollection201Response> updateCommerceCollection updateCommerceCollectionWithHttpInfo(collectionId, updateCommerceCollectionRequest)

Update a collection

Partial update; at least one field besides accountId is required. Change membership with POST /v1/commerce/collections/{collectionId}/products.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String collectionId = "collectionId_example"; // String | Platform-native collection id.
        UpdateCommerceCollectionRequest updateCommerceCollectionRequest = new UpdateCommerceCollectionRequest(); // UpdateCommerceCollectionRequest | 
        try {
            ApiResponse<CreateCommerceCollection201Response> response = apiInstance.updateCommerceCollectionWithHttpInfo(collectionId, updateCommerceCollectionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceCollection");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **collectionId** | **String**| Platform-native collection id. | |
| **updateCommerceCollectionRequest** | [**UpdateCommerceCollectionRequest**](UpdateCommerceCollectionRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceCollection201Response**](CreateCommerceCollection201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). Reconnect the store. |  -  |
| **404** | Account not found (code account_not_found) or collection not found (code resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommerceDiscount

> CreateCommerceDiscount201Response updateCommerceDiscount(discountId, updateCommerceDiscountRequest)

Update a discount

Changes a percentage, fixed-amount or free-shipping discount. Buy-X-get-Y and app discounts are read-only here. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        UpdateCommerceDiscountRequest updateCommerceDiscountRequest = new UpdateCommerceDiscountRequest(); // UpdateCommerceDiscountRequest | 
        try {
            CreateCommerceDiscount201Response result = apiInstance.updateCommerceDiscount(discountId, updateCommerceDiscountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **updateCommerceDiscountRequest** | [**UpdateCommerceDiscountRequest**](UpdateCommerceDiscountRequest.md)|  | |

### Return type

[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommerceDiscountWithHttpInfo

> ApiResponse<CreateCommerceDiscount201Response> updateCommerceDiscount updateCommerceDiscountWithHttpInfo(discountId, updateCommerceDiscountRequest)

Update a discount

Changes a percentage, fixed-amount or free-shipping discount. Buy-X-get-Y and app discounts are read-only here. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String discountId = "discountId_example"; // String | Platform-native id.
        UpdateCommerceDiscountRequest updateCommerceDiscountRequest = new UpdateCommerceDiscountRequest(); // UpdateCommerceDiscountRequest | 
        try {
            ApiResponse<CreateCommerceDiscount201Response> response = apiInstance.updateCommerceDiscountWithHttpInfo(discountId, updateCommerceDiscountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceDiscount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **discountId** | **String**| Platform-native id. | |
| **updateCommerceDiscountRequest** | [**UpdateCommerceDiscountRequest**](UpdateCommerceDiscountRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceDiscount201Response**](CreateCommerceDiscount201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discount updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommerceMenu

> CreateCommerceMenu201Response updateCommerceMenu(menuId, updateCommerceMenuRequest)

Replace a navigation menu

Replaces the title and the whole item tree. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String menuId = "menuId_example"; // String | Platform-native id.
        UpdateCommerceMenuRequest updateCommerceMenuRequest = new UpdateCommerceMenuRequest(); // UpdateCommerceMenuRequest | 
        try {
            CreateCommerceMenu201Response result = apiInstance.updateCommerceMenu(menuId, updateCommerceMenuRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **menuId** | **String**| Platform-native id. | |
| **updateCommerceMenuRequest** | [**UpdateCommerceMenuRequest**](UpdateCommerceMenuRequest.md)|  | |

### Return type

[**CreateCommerceMenu201Response**](CreateCommerceMenu201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommerceMenuWithHttpInfo

> ApiResponse<CreateCommerceMenu201Response> updateCommerceMenu updateCommerceMenuWithHttpInfo(menuId, updateCommerceMenuRequest)

Replace a navigation menu

Replaces the title and the whole item tree. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String menuId = "menuId_example"; // String | Platform-native id.
        UpdateCommerceMenuRequest updateCommerceMenuRequest = new UpdateCommerceMenuRequest(); // UpdateCommerceMenuRequest | 
        try {
            ApiResponse<CreateCommerceMenu201Response> response = apiInstance.updateCommerceMenuWithHttpInfo(menuId, updateCommerceMenuRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceMenu");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **menuId** | **String**| Platform-native id. | |
| **updateCommerceMenuRequest** | [**UpdateCommerceMenuRequest**](UpdateCommerceMenuRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceMenu201Response**](CreateCommerceMenu201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommerceMetaobject

> CreateCommerceMetaobject201Response updateCommerceMetaobject(metaobjectId, updateCommerceMetaobjectRequest)

Update a metaobject

Sets the given field values; fields left out keep theirs. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String metaobjectId = "metaobjectId_example"; // String | Platform-native id.
        UpdateCommerceMetaobjectRequest updateCommerceMetaobjectRequest = new UpdateCommerceMetaobjectRequest(); // UpdateCommerceMetaobjectRequest | 
        try {
            CreateCommerceMetaobject201Response result = apiInstance.updateCommerceMetaobject(metaobjectId, updateCommerceMetaobjectRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **metaobjectId** | **String**| Platform-native id. | |
| **updateCommerceMetaobjectRequest** | [**UpdateCommerceMetaobjectRequest**](UpdateCommerceMetaobjectRequest.md)|  | |

### Return type

[**CreateCommerceMetaobject201Response**](CreateCommerceMetaobject201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobject updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommerceMetaobjectWithHttpInfo

> ApiResponse<CreateCommerceMetaobject201Response> updateCommerceMetaobject updateCommerceMetaobjectWithHttpInfo(metaobjectId, updateCommerceMetaobjectRequest)

Update a metaobject

Sets the given field values; fields left out keep theirs. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String metaobjectId = "metaobjectId_example"; // String | Platform-native id.
        UpdateCommerceMetaobjectRequest updateCommerceMetaobjectRequest = new UpdateCommerceMetaobjectRequest(); // UpdateCommerceMetaobjectRequest | 
        try {
            ApiResponse<CreateCommerceMetaobject201Response> response = apiInstance.updateCommerceMetaobjectWithHttpInfo(metaobjectId, updateCommerceMetaobjectRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceMetaobject");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **metaobjectId** | **String**| Platform-native id. | |
| **updateCommerceMetaobjectRequest** | [**UpdateCommerceMetaobjectRequest**](UpdateCommerceMetaobjectRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceMetaobject201Response**](CreateCommerceMetaobject201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metaobject updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommercePage

> CreateCommercePage201Response updateCommercePage(pageId, updateCommercePageRequest)

Update a page

Updates the fields you pass (&#x60;title&#x60;, &#x60;handle&#x60;, &#x60;bodyHtml&#x60;, &#x60;isPublished&#x60;) and returns the page. Needs pages.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String pageId = "pageId_example"; // String | Platform-native id.
        UpdateCommercePageRequest updateCommercePageRequest = new UpdateCommercePageRequest(); // UpdateCommercePageRequest | 
        try {
            CreateCommercePage201Response result = apiInstance.updateCommercePage(pageId, updateCommercePageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pageId** | **String**| Platform-native id. | |
| **updateCommercePageRequest** | [**UpdateCommercePageRequest**](UpdateCommercePageRequest.md)|  | |

### Return type

[**CreateCommercePage201Response**](CreateCommercePage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommercePageWithHttpInfo

> ApiResponse<CreateCommercePage201Response> updateCommercePage updateCommercePageWithHttpInfo(pageId, updateCommercePageRequest)

Update a page

Updates the fields you pass (&#x60;title&#x60;, &#x60;handle&#x60;, &#x60;bodyHtml&#x60;, &#x60;isPublished&#x60;) and returns the page. Needs pages.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String pageId = "pageId_example"; // String | Platform-native id.
        UpdateCommercePageRequest updateCommercePageRequest = new UpdateCommercePageRequest(); // UpdateCommercePageRequest | 
        try {
            ApiResponse<CreateCommercePage201Response> response = apiInstance.updateCommercePageWithHttpInfo(pageId, updateCommercePageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommercePage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pageId** | **String**| Platform-native id. | |
| **updateCommercePageRequest** | [**UpdateCommercePageRequest**](UpdateCommercePageRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommercePage201Response**](CreateCommercePage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommerceProduct

> CreateCommerceProduct201Response updateCommerceProduct(productId, updateCommerceProductRequest)

Update a product

Partial-updates the product&#39;s own fields; at least one besides &#x60;accountId&#x60; is required. &#x60;tags&#x60; replaces the full list. Change prices with &#x60;POST /v1/commerce/products/{productId}/price&#x60; and status with &#x60;POST /v1/commerce/products/state&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native product id.
        UpdateCommerceProductRequest updateCommerceProductRequest = new UpdateCommerceProductRequest(); // UpdateCommerceProductRequest | 
        try {
            CreateCommerceProduct201Response result = apiInstance.updateCommerceProduct(productId, updateCommerceProductRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native product id. | |
| **updateCommerceProductRequest** | [**UpdateCommerceProductRequest**](UpdateCommerceProductRequest.md)|  | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found (code account_not_found) or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommerceProductWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> updateCommerceProduct updateCommerceProductWithHttpInfo(productId, updateCommerceProductRequest)

Update a product

Partial-updates the product&#39;s own fields; at least one besides &#x60;accountId&#x60; is required. &#x60;tags&#x60; replaces the full list. Change prices with &#x60;POST /v1/commerce/products/{productId}/price&#x60; and status with &#x60;POST /v1/commerce/products/state&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native product id.
        UpdateCommerceProductRequest updateCommerceProductRequest = new UpdateCommerceProductRequest(); // UpdateCommerceProductRequest | 
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.updateCommerceProductWithHttpInfo(productId, updateCommerceProductRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceProduct");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native product id. | |
| **updateCommerceProductRequest** | [**UpdateCommerceProductRequest**](UpdateCommerceProductRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found (code account_not_found) or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommerceProductPrices

> CreateCommerceProduct201Response updateCommerceProductPrices(productId, updateCommerceProductPricesRequest)

Update variant prices

Sets the price and/or compare-at price of the listed variants. Other variants are untouched. Amounts are in the store currency; send &#x60;compareAtPrice: null&#x60; to remove a strike-through price. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native product id.
        UpdateCommerceProductPricesRequest updateCommerceProductPricesRequest = new UpdateCommerceProductPricesRequest(); // UpdateCommerceProductPricesRequest | 
        try {
            CreateCommerceProduct201Response result = apiInstance.updateCommerceProductPrices(productId, updateCommerceProductPricesRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceProductPrices");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native product id. | |
| **updateCommerceProductPricesRequest** | [**UpdateCommerceProductPricesRequest**](UpdateCommerceProductPricesRequest.md)|  | |

### Return type

[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prices updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found (code account_not_found) or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommerceProductPricesWithHttpInfo

> ApiResponse<CreateCommerceProduct201Response> updateCommerceProductPrices updateCommerceProductPricesWithHttpInfo(productId, updateCommerceProductPricesRequest)

Update variant prices

Sets the price and/or compare-at price of the listed variants. Other variants are untouched. Amounts are in the store currency; send &#x60;compareAtPrice: null&#x60; to remove a strike-through price. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String productId = "productId_example"; // String | Platform-native product id.
        UpdateCommerceProductPricesRequest updateCommerceProductPricesRequest = new UpdateCommerceProductPricesRequest(); // UpdateCommerceProductPricesRequest | 
        try {
            ApiResponse<CreateCommerceProduct201Response> response = apiInstance.updateCommerceProductPricesWithHttpInfo(productId, updateCommerceProductPricesRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceProductPrices");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**| Platform-native product id. | |
| **updateCommerceProductPricesRequest** | [**UpdateCommerceProductPricesRequest**](UpdateCommerceProductPricesRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceProduct201Response**](CreateCommerceProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prices updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found (code account_not_found) or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## updateCommerceRedirect

> CreateCommerceRedirect201Response updateCommerceRedirect(redirectId, updateCommerceRedirectRequest)

Update a URL redirect

Changes the redirect&#39;s &#x60;path&#x60; and/or &#x60;target&#x60;. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String redirectId = "redirectId_example"; // String | Platform-native id.
        UpdateCommerceRedirectRequest updateCommerceRedirectRequest = new UpdateCommerceRedirectRequest(); // UpdateCommerceRedirectRequest | 
        try {
            CreateCommerceRedirect201Response result = apiInstance.updateCommerceRedirect(redirectId, updateCommerceRedirectRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceRedirect");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **redirectId** | **String**| Platform-native id. | |
| **updateCommerceRedirectRequest** | [**UpdateCommerceRedirectRequest**](UpdateCommerceRedirectRequest.md)|  | |

### Return type

[**CreateCommerceRedirect201Response**](CreateCommerceRedirect201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Redirect updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## updateCommerceRedirectWithHttpInfo

> ApiResponse<CreateCommerceRedirect201Response> updateCommerceRedirect updateCommerceRedirectWithHttpInfo(redirectId, updateCommerceRedirectRequest)

Update a URL redirect

Changes the redirect&#39;s &#x60;path&#x60; and/or &#x60;target&#x60;. Shopify only. Needs navigation.write.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        String redirectId = "redirectId_example"; // String | Platform-native id.
        UpdateCommerceRedirectRequest updateCommerceRedirectRequest = new UpdateCommerceRedirectRequest(); // UpdateCommerceRedirectRequest | 
        try {
            ApiResponse<CreateCommerceRedirect201Response> response = apiInstance.updateCommerceRedirectWithHttpInfo(redirectId, updateCommerceRedirectRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#updateCommerceRedirect");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **redirectId** | **String**| Platform-native id. | |
| **updateCommerceRedirectRequest** | [**UpdateCommerceRedirectRequest**](UpdateCommerceRedirectRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommerceRedirect201Response**](CreateCommerceRedirect201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Redirect updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |


## upsertCommerceMarketingActivity

> UpsertCommerceMarketingActivity200Response upsertCommerceMarketingActivity(upsertCommerceMarketingActivityRequest)

Record a marketing activity

Creates or updates (by &#x60;remoteId&#x60;) an activity in the store&#39;s Marketing section, so the merchant sees a post, ad or message you ran for them, with its link and UTM parameters for attribution. Use your own id (for example the Zernio post or ad id) as &#x60;remoteId&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        UpsertCommerceMarketingActivityRequest upsertCommerceMarketingActivityRequest = new UpsertCommerceMarketingActivityRequest(); // UpsertCommerceMarketingActivityRequest | 
        try {
            UpsertCommerceMarketingActivity200Response result = apiInstance.upsertCommerceMarketingActivity(upsertCommerceMarketingActivityRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#upsertCommerceMarketingActivity");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **upsertCommerceMarketingActivityRequest** | [**UpsertCommerceMarketingActivityRequest**](UpsertCommerceMarketingActivityRequest.md)|  | |

### Return type

[**UpsertCommerceMarketingActivity200Response**](UpsertCommerceMarketingActivity200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity recorded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

## upsertCommerceMarketingActivityWithHttpInfo

> ApiResponse<UpsertCommerceMarketingActivity200Response> upsertCommerceMarketingActivity upsertCommerceMarketingActivityWithHttpInfo(upsertCommerceMarketingActivityRequest)

Record a marketing activity

Creates or updates (by &#x60;remoteId&#x60;) an activity in the store&#39;s Marketing section, so the merchant sees a post, ad or message you ran for them, with its link and UTM parameters for attribution. Use your own id (for example the Zernio post or ad id) as &#x60;remoteId&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommerceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommerceApi apiInstance = new CommerceApi(defaultClient);
        UpsertCommerceMarketingActivityRequest upsertCommerceMarketingActivityRequest = new UpsertCommerceMarketingActivityRequest(); // UpsertCommerceMarketingActivityRequest | 
        try {
            ApiResponse<UpsertCommerceMarketingActivity200Response> response = apiInstance.upsertCommerceMarketingActivityWithHttpInfo(upsertCommerceMarketingActivityRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommerceApi#upsertCommerceMarketingActivity");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **upsertCommerceMarketingActivityRequest** | [**UpsertCommerceMarketingActivityRequest**](UpsertCommerceMarketingActivityRequest.md)|  | |

### Return type

ApiResponse<[**UpsertCommerceMarketingActivity200Response**](UpsertCommerceMarketingActivity200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity recorded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The store has not granted this permission, or the token was revoked (code insufficient_permissions). Reconnect the store to grant the latest permissions; GET /v1/commerce/store lists what the current grant allows. |  -  |
| **404** | Account not found (code account_not_found) or the resource was not found (code product_not_found or resource_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by the platform. Retry later. |  -  |

