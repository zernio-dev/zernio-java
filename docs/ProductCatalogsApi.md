# ProductCatalogsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchAdCatalogProducts**](ProductCatalogsApi.md#batchAdCatalogProducts) | **POST** /v1/ads/catalogs/{catalogId}/products/batch | Create, update or delete products in bulk |
| [**batchAdCatalogProductsWithHttpInfo**](ProductCatalogsApi.md#batchAdCatalogProductsWithHttpInfo) | **POST** /v1/ads/catalogs/{catalogId}/products/batch | Create, update or delete products in bulk |
| [**createAdCatalog**](ProductCatalogsApi.md#createAdCatalog) | **POST** /v1/ads/catalogs | Create a Meta product catalog |
| [**createAdCatalogWithHttpInfo**](ProductCatalogsApi.md#createAdCatalogWithHttpInfo) | **POST** /v1/ads/catalogs | Create a Meta product catalog |
| [**createAdCatalogFeed**](ProductCatalogsApi.md#createAdCatalogFeed) | **POST** /v1/ads/catalogs/{catalogId}/feeds | Create a product feed |
| [**createAdCatalogFeedWithHttpInfo**](ProductCatalogsApi.md#createAdCatalogFeedWithHttpInfo) | **POST** /v1/ads/catalogs/{catalogId}/feeds | Create a product feed |
| [**createAdCatalogFeedUpload**](ProductCatalogsApi.md#createAdCatalogFeedUpload) | **POST** /v1/ads/catalogs/{catalogId}/feeds/{feedId}/uploads | Fetch a feed file now |
| [**createAdCatalogFeedUploadWithHttpInfo**](ProductCatalogsApi.md#createAdCatalogFeedUploadWithHttpInfo) | **POST** /v1/ads/catalogs/{catalogId}/feeds/{feedId}/uploads | Fetch a feed file now |
| [**createAdCatalogProduct**](ProductCatalogsApi.md#createAdCatalogProduct) | **POST** /v1/ads/catalogs/{catalogId}/products | Add a product to a catalog |
| [**createAdCatalogProductWithHttpInfo**](ProductCatalogsApi.md#createAdCatalogProductWithHttpInfo) | **POST** /v1/ads/catalogs/{catalogId}/products | Add a product to a catalog |
| [**createAdCatalogProductSet**](ProductCatalogsApi.md#createAdCatalogProductSet) | **POST** /v1/ads/catalogs/{catalogId}/product-sets | Create a product set |
| [**createAdCatalogProductSetWithHttpInfo**](ProductCatalogsApi.md#createAdCatalogProductSetWithHttpInfo) | **POST** /v1/ads/catalogs/{catalogId}/product-sets | Create a product set |
| [**deleteAdCatalog**](ProductCatalogsApi.md#deleteAdCatalog) | **DELETE** /v1/ads/catalogs/{catalogId} | Delete a product catalog |
| [**deleteAdCatalogWithHttpInfo**](ProductCatalogsApi.md#deleteAdCatalogWithHttpInfo) | **DELETE** /v1/ads/catalogs/{catalogId} | Delete a product catalog |
| [**deleteAdCatalogProduct**](ProductCatalogsApi.md#deleteAdCatalogProduct) | **DELETE** /v1/ads/catalogs/{catalogId}/products/{productId} | Delete a product |
| [**deleteAdCatalogProductWithHttpInfo**](ProductCatalogsApi.md#deleteAdCatalogProductWithHttpInfo) | **DELETE** /v1/ads/catalogs/{catalogId}/products/{productId} | Delete a product |
| [**deleteAdCatalogProductSet**](ProductCatalogsApi.md#deleteAdCatalogProductSet) | **DELETE** /v1/ads/catalogs/{catalogId}/product-sets/{productSetId} | Delete a product set |
| [**deleteAdCatalogProductSetWithHttpInfo**](ProductCatalogsApi.md#deleteAdCatalogProductSetWithHttpInfo) | **DELETE** /v1/ads/catalogs/{catalogId}/product-sets/{productSetId} | Delete a product set |
| [**getAdCatalog**](ProductCatalogsApi.md#getAdCatalog) | **GET** /v1/ads/catalogs/{catalogId} | Get a product catalog |
| [**getAdCatalogWithHttpInfo**](ProductCatalogsApi.md#getAdCatalogWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId} | Get a product catalog |
| [**getAdCatalogBatch**](ProductCatalogsApi.md#getAdCatalogBatch) | **GET** /v1/ads/catalogs/{catalogId}/batches/{handle} | Get a bulk request&#39;s status |
| [**getAdCatalogBatchWithHttpInfo**](ProductCatalogsApi.md#getAdCatalogBatchWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/batches/{handle} | Get a bulk request&#39;s status |
| [**getAdCatalogProduct**](ProductCatalogsApi.md#getAdCatalogProduct) | **GET** /v1/ads/catalogs/{catalogId}/products/{productId} | Get a product |
| [**getAdCatalogProductWithHttpInfo**](ProductCatalogsApi.md#getAdCatalogProductWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/products/{productId} | Get a product |
| [**listAdCatalogFeedUploads**](ProductCatalogsApi.md#listAdCatalogFeedUploads) | **GET** /v1/ads/catalogs/{catalogId}/feeds/{feedId}/uploads | List a feed&#39;s uploads |
| [**listAdCatalogFeedUploadsWithHttpInfo**](ProductCatalogsApi.md#listAdCatalogFeedUploadsWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/feeds/{feedId}/uploads | List a feed&#39;s uploads |
| [**listAdCatalogFeeds**](ProductCatalogsApi.md#listAdCatalogFeeds) | **GET** /v1/ads/catalogs/{catalogId}/feeds | List a catalog&#39;s product feeds |
| [**listAdCatalogFeedsWithHttpInfo**](ProductCatalogsApi.md#listAdCatalogFeedsWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/feeds | List a catalog&#39;s product feeds |
| [**listAdCatalogProductSets**](ProductCatalogsApi.md#listAdCatalogProductSets) | **GET** /v1/ads/catalogs/{catalogId}/product-sets | List a catalog&#39;s product sets |
| [**listAdCatalogProductSetsWithHttpInfo**](ProductCatalogsApi.md#listAdCatalogProductSetsWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/product-sets | List a catalog&#39;s product sets |
| [**listAdCatalogProducts**](ProductCatalogsApi.md#listAdCatalogProducts) | **GET** /v1/ads/catalogs/{catalogId}/products | List a catalog&#39;s products |
| [**listAdCatalogProductsWithHttpInfo**](ProductCatalogsApi.md#listAdCatalogProductsWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/products | List a catalog&#39;s products |
| [**listAdCatalogs**](ProductCatalogsApi.md#listAdCatalogs) | **GET** /v1/ads/catalogs | List Meta product catalogs |
| [**listAdCatalogsWithHttpInfo**](ProductCatalogsApi.md#listAdCatalogsWithHttpInfo) | **GET** /v1/ads/catalogs | List Meta product catalogs |
| [**updateAdCatalogProduct**](ProductCatalogsApi.md#updateAdCatalogProduct) | **PUT** /v1/ads/catalogs/{catalogId}/products/{productId} | Update a product |
| [**updateAdCatalogProductWithHttpInfo**](ProductCatalogsApi.md#updateAdCatalogProductWithHttpInfo) | **PUT** /v1/ads/catalogs/{catalogId}/products/{productId} | Update a product |
| [**updateAdCatalogProductSet**](ProductCatalogsApi.md#updateAdCatalogProductSet) | **PUT** /v1/ads/catalogs/{catalogId}/product-sets/{productSetId} | Update a product set |
| [**updateAdCatalogProductSetWithHttpInfo**](ProductCatalogsApi.md#updateAdCatalogProductSetWithHttpInfo) | **PUT** /v1/ads/catalogs/{catalogId}/product-sets/{productSetId} | Update a product set |



## batchAdCatalogProducts

> BatchAdCatalogProducts202Response batchAdCatalogProducts(catalogId, batchAdCatalogProductsRequest)

Create, update or delete products in bulk

Up to 5000 CREATE / UPDATE / DELETE requests keyed by &#x60;retailerId&#x60;, processed asynchronously by Meta. Returns handles; poll GET /v1/ads/catalogs/{catalogId}/batches/{handle} for the outcome and per-item errors. CREATE requests need name, url, imageUrl, price and currency.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        BatchAdCatalogProductsRequest batchAdCatalogProductsRequest = new BatchAdCatalogProductsRequest(); // BatchAdCatalogProductsRequest | 
        try {
            BatchAdCatalogProducts202Response result = apiInstance.batchAdCatalogProducts(catalogId, batchAdCatalogProductsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#batchAdCatalogProducts");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **batchAdCatalogProductsRequest** | [**BatchAdCatalogProductsRequest**](BatchAdCatalogProductsRequest.md)|  | |

### Return type

[**BatchAdCatalogProducts202Response**](BatchAdCatalogProducts202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted by Meta |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## batchAdCatalogProductsWithHttpInfo

> ApiResponse<BatchAdCatalogProducts202Response> batchAdCatalogProducts batchAdCatalogProductsWithHttpInfo(catalogId, batchAdCatalogProductsRequest)

Create, update or delete products in bulk

Up to 5000 CREATE / UPDATE / DELETE requests keyed by &#x60;retailerId&#x60;, processed asynchronously by Meta. Returns handles; poll GET /v1/ads/catalogs/{catalogId}/batches/{handle} for the outcome and per-item errors. CREATE requests need name, url, imageUrl, price and currency.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        BatchAdCatalogProductsRequest batchAdCatalogProductsRequest = new BatchAdCatalogProductsRequest(); // BatchAdCatalogProductsRequest | 
        try {
            ApiResponse<BatchAdCatalogProducts202Response> response = apiInstance.batchAdCatalogProductsWithHttpInfo(catalogId, batchAdCatalogProductsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#batchAdCatalogProducts");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **batchAdCatalogProductsRequest** | [**BatchAdCatalogProductsRequest**](BatchAdCatalogProductsRequest.md)|  | |

### Return type

ApiResponse<[**BatchAdCatalogProducts202Response**](BatchAdCatalogProducts202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted by Meta |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## createAdCatalog

> CreateAdCatalog201Response createAdCatalog(createAdCatalogRequest)

Create a Meta product catalog

Creates a Meta Commerce catalog in the business portfolio (resolved like GET). The same catalog serves Advantage+ catalog ads, Instagram/Facebook Shops and the WhatsApp Business catalog: link it to a WhatsApp number with POST /v1/whatsapp/catalogs. Needs catalog_management on the Meta login.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        CreateAdCatalogRequest createAdCatalogRequest = new CreateAdCatalogRequest(); // CreateAdCatalogRequest | 
        try {
            CreateAdCatalog201Response result = apiInstance.createAdCatalog(createAdCatalogRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalog");
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
| **createAdCatalogRequest** | [**CreateAdCatalogRequest**](CreateAdCatalogRequest.md)|  | |

### Return type

[**CreateAdCatalog201Response**](CreateAdCatalog201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Catalog created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |

## createAdCatalogWithHttpInfo

> ApiResponse<CreateAdCatalog201Response> createAdCatalog createAdCatalogWithHttpInfo(createAdCatalogRequest)

Create a Meta product catalog

Creates a Meta Commerce catalog in the business portfolio (resolved like GET). The same catalog serves Advantage+ catalog ads, Instagram/Facebook Shops and the WhatsApp Business catalog: link it to a WhatsApp number with POST /v1/whatsapp/catalogs. Needs catalog_management on the Meta login.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        CreateAdCatalogRequest createAdCatalogRequest = new CreateAdCatalogRequest(); // CreateAdCatalogRequest | 
        try {
            ApiResponse<CreateAdCatalog201Response> response = apiInstance.createAdCatalogWithHttpInfo(createAdCatalogRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalog");
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
| **createAdCatalogRequest** | [**CreateAdCatalogRequest**](CreateAdCatalogRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCatalog201Response**](CreateAdCatalog201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Catalog created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |


## createAdCatalogFeed

> CreateAdCatalogFeed201Response createAdCatalogFeed(catalogId, createAdCatalogFeedRequest)

Create a product feed

A feed pulls a CSV/TSV/XML product file from a URL. With &#x60;schedule&#x60; Meta fetches it on a cadence; without it, trigger fetches with POST /v1/ads/catalogs/{catalogId}/feeds/{feedId}/uploads.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        CreateAdCatalogFeedRequest createAdCatalogFeedRequest = new CreateAdCatalogFeedRequest(); // CreateAdCatalogFeedRequest | 
        try {
            CreateAdCatalogFeed201Response result = apiInstance.createAdCatalogFeed(catalogId, createAdCatalogFeedRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogFeed");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **createAdCatalogFeedRequest** | [**CreateAdCatalogFeedRequest**](CreateAdCatalogFeedRequest.md)|  | |

### Return type

[**CreateAdCatalogFeed201Response**](CreateAdCatalogFeed201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Feed created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## createAdCatalogFeedWithHttpInfo

> ApiResponse<CreateAdCatalogFeed201Response> createAdCatalogFeed createAdCatalogFeedWithHttpInfo(catalogId, createAdCatalogFeedRequest)

Create a product feed

A feed pulls a CSV/TSV/XML product file from a URL. With &#x60;schedule&#x60; Meta fetches it on a cadence; without it, trigger fetches with POST /v1/ads/catalogs/{catalogId}/feeds/{feedId}/uploads.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        CreateAdCatalogFeedRequest createAdCatalogFeedRequest = new CreateAdCatalogFeedRequest(); // CreateAdCatalogFeedRequest | 
        try {
            ApiResponse<CreateAdCatalogFeed201Response> response = apiInstance.createAdCatalogFeedWithHttpInfo(catalogId, createAdCatalogFeedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogFeed");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **createAdCatalogFeedRequest** | [**CreateAdCatalogFeedRequest**](CreateAdCatalogFeedRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCatalogFeed201Response**](CreateAdCatalogFeed201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Feed created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## createAdCatalogFeedUpload

> CreateAdCatalogFeedUpload202Response createAdCatalogFeedUpload(catalogId, feedId, createAdCatalogFeedUploadRequest)

Fetch a feed file now

Asks Meta to fetch the product file at &#x60;url&#x60; into the feed. Processing is asynchronous: read the outcome with GET uploads.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String feedId = "feedId_example"; // String | 
        CreateAdCatalogFeedUploadRequest createAdCatalogFeedUploadRequest = new CreateAdCatalogFeedUploadRequest(); // CreateAdCatalogFeedUploadRequest | 
        try {
            CreateAdCatalogFeedUpload202Response result = apiInstance.createAdCatalogFeedUpload(catalogId, feedId, createAdCatalogFeedUploadRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogFeedUpload");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **feedId** | **String**|  | |
| **createAdCatalogFeedUploadRequest** | [**CreateAdCatalogFeedUploadRequest**](CreateAdCatalogFeedUploadRequest.md)|  | |

### Return type

[**CreateAdCatalogFeedUpload202Response**](CreateAdCatalogFeedUpload202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Fetch started |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## createAdCatalogFeedUploadWithHttpInfo

> ApiResponse<CreateAdCatalogFeedUpload202Response> createAdCatalogFeedUpload createAdCatalogFeedUploadWithHttpInfo(catalogId, feedId, createAdCatalogFeedUploadRequest)

Fetch a feed file now

Asks Meta to fetch the product file at &#x60;url&#x60; into the feed. Processing is asynchronous: read the outcome with GET uploads.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String feedId = "feedId_example"; // String | 
        CreateAdCatalogFeedUploadRequest createAdCatalogFeedUploadRequest = new CreateAdCatalogFeedUploadRequest(); // CreateAdCatalogFeedUploadRequest | 
        try {
            ApiResponse<CreateAdCatalogFeedUpload202Response> response = apiInstance.createAdCatalogFeedUploadWithHttpInfo(catalogId, feedId, createAdCatalogFeedUploadRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogFeedUpload");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **feedId** | **String**|  | |
| **createAdCatalogFeedUploadRequest** | [**CreateAdCatalogFeedUploadRequest**](CreateAdCatalogFeedUploadRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCatalogFeedUpload202Response**](CreateAdCatalogFeedUpload202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Fetch started |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## createAdCatalogProduct

> CreateAdCatalogProduct201Response createAdCatalogProduct(catalogId, createAdCatalogProductRequest)

Add a product to a catalog

Adds one product. &#x60;retailerId&#x60; is your SKU and stays the handle for later lookups and batch updates. For many products at once use POST /v1/ads/catalogs/{catalogId}/products/batch. Needs catalog_management on the Meta login.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        CreateAdCatalogProductRequest createAdCatalogProductRequest = new CreateAdCatalogProductRequest(); // CreateAdCatalogProductRequest | 
        try {
            CreateAdCatalogProduct201Response result = apiInstance.createAdCatalogProduct(catalogId, createAdCatalogProductRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **createAdCatalogProductRequest** | [**CreateAdCatalogProductRequest**](CreateAdCatalogProductRequest.md)|  | |

### Return type

[**CreateAdCatalogProduct201Response**](CreateAdCatalogProduct201Response.md)


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
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## createAdCatalogProductWithHttpInfo

> ApiResponse<CreateAdCatalogProduct201Response> createAdCatalogProduct createAdCatalogProductWithHttpInfo(catalogId, createAdCatalogProductRequest)

Add a product to a catalog

Adds one product. &#x60;retailerId&#x60; is your SKU and stays the handle for later lookups and batch updates. For many products at once use POST /v1/ads/catalogs/{catalogId}/products/batch. Needs catalog_management on the Meta login.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        CreateAdCatalogProductRequest createAdCatalogProductRequest = new CreateAdCatalogProductRequest(); // CreateAdCatalogProductRequest | 
        try {
            ApiResponse<CreateAdCatalogProduct201Response> response = apiInstance.createAdCatalogProductWithHttpInfo(catalogId, createAdCatalogProductRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **createAdCatalogProductRequest** | [**CreateAdCatalogProductRequest**](CreateAdCatalogProductRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCatalogProduct201Response**](CreateAdCatalogProduct201Response.md)>


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
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## createAdCatalogProductSet

> CreateAdCatalogProductSet201Response createAdCatalogProductSet(catalogId, createAdCatalogProductSetRequest)

Create a product set

A product set is a filter over the catalog, e.g. &#x60;{\&quot;retailer_id\&quot;: {\&quot;is_any\&quot;: [\&quot;sku-1\&quot;, \&quot;sku-2\&quot;]}}&#x60; or &#x60;{\&quot;brand\&quot;: {\&quot;i_contains\&quot;: \&quot;acme\&quot;}}&#x60; (Meta&#39;s product set filter syntax).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        CreateAdCatalogProductSetRequest createAdCatalogProductSetRequest = new CreateAdCatalogProductSetRequest(); // CreateAdCatalogProductSetRequest | 
        try {
            CreateAdCatalogProductSet201Response result = apiInstance.createAdCatalogProductSet(catalogId, createAdCatalogProductSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogProductSet");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **createAdCatalogProductSetRequest** | [**CreateAdCatalogProductSetRequest**](CreateAdCatalogProductSetRequest.md)|  | |

### Return type

[**CreateAdCatalogProductSet201Response**](CreateAdCatalogProductSet201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product set created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## createAdCatalogProductSetWithHttpInfo

> ApiResponse<CreateAdCatalogProductSet201Response> createAdCatalogProductSet createAdCatalogProductSetWithHttpInfo(catalogId, createAdCatalogProductSetRequest)

Create a product set

A product set is a filter over the catalog, e.g. &#x60;{\&quot;retailer_id\&quot;: {\&quot;is_any\&quot;: [\&quot;sku-1\&quot;, \&quot;sku-2\&quot;]}}&#x60; or &#x60;{\&quot;brand\&quot;: {\&quot;i_contains\&quot;: \&quot;acme\&quot;}}&#x60; (Meta&#39;s product set filter syntax).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        CreateAdCatalogProductSetRequest createAdCatalogProductSetRequest = new CreateAdCatalogProductSetRequest(); // CreateAdCatalogProductSetRequest | 
        try {
            ApiResponse<CreateAdCatalogProductSet201Response> response = apiInstance.createAdCatalogProductSetWithHttpInfo(catalogId, createAdCatalogProductSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#createAdCatalogProductSet");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **createAdCatalogProductSetRequest** | [**CreateAdCatalogProductSetRequest**](CreateAdCatalogProductSetRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCatalogProductSet201Response**](CreateAdCatalogProductSet201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product set created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## deleteAdCatalog

> DeleteAdCatalog200Response deleteAdCatalog(catalogId, accountId, catalogAccountId)

Delete a product catalog

Deletes the catalog and every product in it on Meta. Ads and WhatsApp numbers that use it lose their catalog.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            DeleteAdCatalog200Response result = apiInstance.deleteAdCatalog(catalogId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#deleteAdCatalog");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**DeleteAdCatalog200Response**](DeleteAdCatalog200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## deleteAdCatalogWithHttpInfo

> ApiResponse<DeleteAdCatalog200Response> deleteAdCatalog deleteAdCatalogWithHttpInfo(catalogId, accountId, catalogAccountId)

Delete a product catalog

Deletes the catalog and every product in it on Meta. Ads and WhatsApp numbers that use it lose their catalog.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<DeleteAdCatalog200Response> response = apiInstance.deleteAdCatalogWithHttpInfo(catalogId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#deleteAdCatalog");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**DeleteAdCatalog200Response**](DeleteAdCatalog200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## deleteAdCatalogProduct

> DeleteAdCatalogProduct200Response deleteAdCatalogProduct(catalogId, productId, accountId, catalogAccountId)

Delete a product

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productId = "productId_example"; // String | Meta product item ID (from the products list; not the retailer id)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            DeleteAdCatalogProduct200Response result = apiInstance.deleteAdCatalogProduct(catalogId, productId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#deleteAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productId** | **String**| Meta product item ID (from the products list; not the retailer id) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**DeleteAdCatalogProduct200Response**](DeleteAdCatalogProduct200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## deleteAdCatalogProductWithHttpInfo

> ApiResponse<DeleteAdCatalogProduct200Response> deleteAdCatalogProduct deleteAdCatalogProductWithHttpInfo(catalogId, productId, accountId, catalogAccountId)

Delete a product

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productId = "productId_example"; // String | Meta product item ID (from the products list; not the retailer id)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<DeleteAdCatalogProduct200Response> response = apiInstance.deleteAdCatalogProductWithHttpInfo(catalogId, productId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#deleteAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productId** | **String**| Meta product item ID (from the products list; not the retailer id) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**DeleteAdCatalogProduct200Response**](DeleteAdCatalogProduct200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## deleteAdCatalogProductSet

> DeleteAdCatalogProductSet200Response deleteAdCatalogProductSet(catalogId, productSetId, accountId, catalogAccountId)

Delete a product set

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productSetId = "productSetId_example"; // String | 
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            DeleteAdCatalogProductSet200Response result = apiInstance.deleteAdCatalogProductSet(catalogId, productSetId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#deleteAdCatalogProductSet");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productSetId** | **String**|  | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**DeleteAdCatalogProductSet200Response**](DeleteAdCatalogProductSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## deleteAdCatalogProductSetWithHttpInfo

> ApiResponse<DeleteAdCatalogProductSet200Response> deleteAdCatalogProductSet deleteAdCatalogProductSetWithHttpInfo(catalogId, productSetId, accountId, catalogAccountId)

Delete a product set

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productSetId = "productSetId_example"; // String | 
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<DeleteAdCatalogProductSet200Response> response = apiInstance.deleteAdCatalogProductSetWithHttpInfo(catalogId, productSetId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#deleteAdCatalogProductSet");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productSetId** | **String**|  | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**DeleteAdCatalogProductSet200Response**](DeleteAdCatalogProductSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## getAdCatalog

> CreateAdCatalog201Response getAdCatalog(catalogId, accountId, catalogAccountId)

Get a product catalog

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            CreateAdCatalog201Response result = apiInstance.getAdCatalog(catalogId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#getAdCatalog");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**CreateAdCatalog201Response**](CreateAdCatalog201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## getAdCatalogWithHttpInfo

> ApiResponse<CreateAdCatalog201Response> getAdCatalog getAdCatalogWithHttpInfo(catalogId, accountId, catalogAccountId)

Get a product catalog

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<CreateAdCatalog201Response> response = apiInstance.getAdCatalogWithHttpInfo(catalogId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#getAdCatalog");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**CreateAdCatalog201Response**](CreateAdCatalog201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## getAdCatalogBatch

> GetAdCatalogBatch200Response getAdCatalogBatch(catalogId, handle, accountId, catalogAccountId)

Get a bulk request&#39;s status

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String handle = "handle_example"; // String | Handle returned by the batch call
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            GetAdCatalogBatch200Response result = apiInstance.getAdCatalogBatch(catalogId, handle, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#getAdCatalogBatch");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **handle** | **String**| Handle returned by the batch call | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**GetAdCatalogBatch200Response**](GetAdCatalogBatch200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## getAdCatalogBatchWithHttpInfo

> ApiResponse<GetAdCatalogBatch200Response> getAdCatalogBatch getAdCatalogBatchWithHttpInfo(catalogId, handle, accountId, catalogAccountId)

Get a bulk request&#39;s status

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String handle = "handle_example"; // String | Handle returned by the batch call
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<GetAdCatalogBatch200Response> response = apiInstance.getAdCatalogBatchWithHttpInfo(catalogId, handle, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#getAdCatalogBatch");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **handle** | **String**| Handle returned by the batch call | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**GetAdCatalogBatch200Response**](GetAdCatalogBatch200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## getAdCatalogProduct

> CreateAdCatalogProduct201Response getAdCatalogProduct(catalogId, productId, accountId, catalogAccountId)

Get a product

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productId = "productId_example"; // String | Meta product item ID (from the products list; not the retailer id)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            CreateAdCatalogProduct201Response result = apiInstance.getAdCatalogProduct(catalogId, productId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#getAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productId** | **String**| Meta product item ID (from the products list; not the retailer id) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**CreateAdCatalogProduct201Response**](CreateAdCatalogProduct201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## getAdCatalogProductWithHttpInfo

> ApiResponse<CreateAdCatalogProduct201Response> getAdCatalogProduct getAdCatalogProductWithHttpInfo(catalogId, productId, accountId, catalogAccountId)

Get a product

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productId = "productId_example"; // String | Meta product item ID (from the products list; not the retailer id)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<CreateAdCatalogProduct201Response> response = apiInstance.getAdCatalogProductWithHttpInfo(catalogId, productId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#getAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productId** | **String**| Meta product item ID (from the products list; not the retailer id) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**CreateAdCatalogProduct201Response**](CreateAdCatalogProduct201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## listAdCatalogFeedUploads

> ListAdCatalogFeedUploads200Response listAdCatalogFeedUploads(catalogId, feedId, accountId, catalogAccountId)

List a feed&#39;s uploads

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String feedId = "feedId_example"; // String | 
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ListAdCatalogFeedUploads200Response result = apiInstance.listAdCatalogFeedUploads(catalogId, feedId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogFeedUploads");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **feedId** | **String**|  | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**ListAdCatalogFeedUploads200Response**](ListAdCatalogFeedUploads200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Uploads, newest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## listAdCatalogFeedUploadsWithHttpInfo

> ApiResponse<ListAdCatalogFeedUploads200Response> listAdCatalogFeedUploads listAdCatalogFeedUploadsWithHttpInfo(catalogId, feedId, accountId, catalogAccountId)

List a feed&#39;s uploads

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String feedId = "feedId_example"; // String | 
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<ListAdCatalogFeedUploads200Response> response = apiInstance.listAdCatalogFeedUploadsWithHttpInfo(catalogId, feedId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogFeedUploads");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **feedId** | **String**|  | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**ListAdCatalogFeedUploads200Response**](ListAdCatalogFeedUploads200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Uploads, newest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## listAdCatalogFeeds

> ListAdCatalogFeeds200Response listAdCatalogFeeds(catalogId, accountId, catalogAccountId)

List a catalog&#39;s product feeds

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ListAdCatalogFeeds200Response result = apiInstance.listAdCatalogFeeds(catalogId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogFeeds");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**ListAdCatalogFeeds200Response**](ListAdCatalogFeeds200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feeds |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## listAdCatalogFeedsWithHttpInfo

> ApiResponse<ListAdCatalogFeeds200Response> listAdCatalogFeeds listAdCatalogFeedsWithHttpInfo(catalogId, accountId, catalogAccountId)

List a catalog&#39;s product feeds

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<ListAdCatalogFeeds200Response> response = apiInstance.listAdCatalogFeedsWithHttpInfo(catalogId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogFeeds");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**ListAdCatalogFeeds200Response**](ListAdCatalogFeeds200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feeds |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## listAdCatalogProductSets

> ListAdCatalogProductSets200Response listAdCatalogProductSets(catalogId, accountId, catalogAccountId)

List a catalog&#39;s product sets

Lists a Meta product catalog&#39;s product sets, the unit a catalog ad promotes. Pass the chosen set id, not the parent catalog id, as &#x60;promotedObject.productSetId&#x60; on POST /v1/ads/create with &#x60;goal: catalog_sales&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ListAdCatalogProductSets200Response result = apiInstance.listAdCatalogProductSets(catalogId, accountId, catalogAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogProductSets");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

[**ListAdCatalogProductSets200Response**](ListAdCatalogProductSets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## listAdCatalogProductSetsWithHttpInfo

> ApiResponse<ListAdCatalogProductSets200Response> listAdCatalogProductSets listAdCatalogProductSetsWithHttpInfo(catalogId, accountId, catalogAccountId)

List a catalog&#39;s product sets

Lists a Meta product catalog&#39;s product sets, the unit a catalog ad promotes. Pass the chosen set id, not the parent catalog id, as &#x60;promotedObject.productSetId&#x60; on POST /v1/ads/create with &#x60;goal: catalog_sales&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        try {
            ApiResponse<ListAdCatalogProductSets200Response> response = apiInstance.listAdCatalogProductSetsWithHttpInfo(catalogId, accountId, catalogAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogProductSets");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |

### Return type

ApiResponse<[**ListAdCatalogProductSets200Response**](ListAdCatalogProductSets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## listAdCatalogProducts

> ListAdCatalogProducts200Response listAdCatalogProducts(catalogId, accountId, catalogAccountId, limit, after, retailerId)

List a catalog&#39;s products

Pages through the catalog&#39;s products. Filter by your own &#x60;retailerId&#x60; to look one up. &#x60;price&#x60; and &#x60;salePrice&#x60; come back formatted by Meta (for example \&quot;€49.90\&quot;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | Cursor from the previous page's `nextCursor`
        String retailerId = "retailerId_example"; // String | Only the product with this retailer id (your SKU)
        try {
            ListAdCatalogProducts200Response result = apiInstance.listAdCatalogProducts(catalogId, accountId, catalogAccountId, limit, after, retailerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogProducts");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**| Cursor from the previous page&#39;s &#x60;nextCursor&#x60; | [optional] |
| **retailerId** | **String**| Only the product with this retailer id (your SKU) | [optional] |

### Return type

[**ListAdCatalogProducts200Response**](ListAdCatalogProducts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## listAdCatalogProductsWithHttpInfo

> ApiResponse<ListAdCatalogProducts200Response> listAdCatalogProducts listAdCatalogProductsWithHttpInfo(catalogId, accountId, catalogAccountId, limit, after, retailerId)

List a catalog&#39;s products

Pages through the catalog&#39;s products. Filter by your own &#x60;retailerId&#x60; to look one up. &#x60;price&#x60; and &#x60;salePrice&#x60; come back formatted by Meta (for example \&quot;€49.90\&quot;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account's own
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | Cursor from the previous page's `nextCursor`
        String retailerId = "retailerId_example"; // String | Only the product with this retailer id (your SKU)
        try {
            ApiResponse<ListAdCatalogProducts200Response> response = apiInstance.listAdCatalogProductsWithHttpInfo(catalogId, accountId, catalogAccountId, limit, after, retailerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogProducts");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token performs the call instead of the account&#39;s own | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**| Cursor from the previous page&#39;s &#x60;nextCursor&#x60; | [optional] |
| **retailerId** | **String**| Only the product with this retailer id (your SKU) | [optional] |

### Return type

ApiResponse<[**ListAdCatalogProducts200Response**](ListAdCatalogProducts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## listAdCatalogs

> ListAdCatalogs200Response listAdCatalogs(accountId, catalogAccountId, adAccountId, businessId)

List Meta product catalogs

Lists the Meta Commerce catalogs of a business portfolio (owned + agency-shared). The business comes from &#x60;businessId&#x60;, else the ad account&#39;s owner (&#x60;adAccountId&#x60;), else the WhatsApp Business Account&#39;s owner when &#x60;accountId&#x60; is a WhatsApp connection, else the only business the Meta login can see. Reads work with scopes customers already granted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token is used instead of the account's own (needed for WhatsApp connections, whose token cannot manage catalogs).
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...) whose owner business to list
        String businessId = "businessId_example"; // String | Meta business portfolio ID to list
        try {
            ListAdCatalogs200Response result = apiInstance.listAdCatalogs(accountId, catalogAccountId, adAccountId, businessId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogs");
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
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token is used instead of the account&#39;s own (needed for WhatsApp connections, whose token cannot manage catalogs). | [optional] |
| **adAccountId** | **String**| Meta ad account ID (act_...) whose owner business to list | [optional] |
| **businessId** | **String**| Meta business portfolio ID to list | [optional] |

### Return type

[**ListAdCatalogs200Response**](ListAdCatalogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Catalogs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |

## listAdCatalogsWithHttpInfo

> ApiResponse<ListAdCatalogs200Response> listAdCatalogs listAdCatalogsWithHttpInfo(accountId, catalogAccountId, adAccountId, businessId)

List Meta product catalogs

Lists the Meta Commerce catalogs of a business portfolio (owned + agency-shared). The business comes from &#x60;businessId&#x60;, else the ad account&#39;s owner (&#x60;adAccountId&#x60;), else the WhatsApp Business Account&#39;s owner when &#x60;accountId&#x60; is a WhatsApp connection, else the only business the Meta login can see. Reads work with scopes customers already granted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String accountId = "accountId_example"; // String | A facebook, instagram, metaads or whatsapp account ID
        String catalogAccountId = "catalogAccountId_example"; // String | A facebook, instagram or metaads account whose Meta login carries catalog_management; its token is used instead of the account's own (needed for WhatsApp connections, whose token cannot manage catalogs).
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...) whose owner business to list
        String businessId = "businessId_example"; // String | Meta business portfolio ID to list
        try {
            ApiResponse<ListAdCatalogs200Response> response = apiInstance.listAdCatalogsWithHttpInfo(accountId, catalogAccountId, adAccountId, businessId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#listAdCatalogs");
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
| **accountId** | **String**| A facebook, instagram, metaads or whatsapp account ID | |
| **catalogAccountId** | **String**| A facebook, instagram or metaads account whose Meta login carries catalog_management; its token is used instead of the account&#39;s own (needed for WhatsApp connections, whose token cannot manage catalogs). | [optional] |
| **adAccountId** | **String**| Meta ad account ID (act_...) whose owner business to list | [optional] |
| **businessId** | **String**| Meta business portfolio ID to list | [optional] |

### Return type

ApiResponse<[**ListAdCatalogs200Response**](ListAdCatalogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Catalogs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |


## updateAdCatalogProduct

> CreateAdCatalogProduct201Response updateAdCatalogProduct(catalogId, productId, updateAdCatalogProductRequest)

Update a product

Partial update: only the fields sent change. &#x60;retailerId&#x60; cannot change.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productId = "productId_example"; // String | Meta product item ID (from the products list; not the retailer id)
        UpdateAdCatalogProductRequest updateAdCatalogProductRequest = new UpdateAdCatalogProductRequest(); // UpdateAdCatalogProductRequest | 
        try {
            CreateAdCatalogProduct201Response result = apiInstance.updateAdCatalogProduct(catalogId, productId, updateAdCatalogProductRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#updateAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productId** | **String**| Meta product item ID (from the products list; not the retailer id) | |
| **updateAdCatalogProductRequest** | [**UpdateAdCatalogProductRequest**](UpdateAdCatalogProductRequest.md)|  | |

### Return type

[**CreateAdCatalogProduct201Response**](CreateAdCatalogProduct201Response.md)


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
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## updateAdCatalogProductWithHttpInfo

> ApiResponse<CreateAdCatalogProduct201Response> updateAdCatalogProduct updateAdCatalogProductWithHttpInfo(catalogId, productId, updateAdCatalogProductRequest)

Update a product

Partial update: only the fields sent change. &#x60;retailerId&#x60; cannot change.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productId = "productId_example"; // String | Meta product item ID (from the products list; not the retailer id)
        UpdateAdCatalogProductRequest updateAdCatalogProductRequest = new UpdateAdCatalogProductRequest(); // UpdateAdCatalogProductRequest | 
        try {
            ApiResponse<CreateAdCatalogProduct201Response> response = apiInstance.updateAdCatalogProductWithHttpInfo(catalogId, productId, updateAdCatalogProductRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#updateAdCatalogProduct");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productId** | **String**| Meta product item ID (from the products list; not the retailer id) | |
| **updateAdCatalogProductRequest** | [**UpdateAdCatalogProductRequest**](UpdateAdCatalogProductRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCatalogProduct201Response**](CreateAdCatalogProduct201Response.md)>


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
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |


## updateAdCatalogProductSet

> CreateAdCatalogProductSet201Response updateAdCatalogProductSet(catalogId, productSetId, updateAdCatalogProductSetRequest)

Update a product set

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productSetId = "productSetId_example"; // String | 
        UpdateAdCatalogProductSetRequest updateAdCatalogProductSetRequest = new UpdateAdCatalogProductSetRequest(); // UpdateAdCatalogProductSetRequest | 
        try {
            CreateAdCatalogProductSet201Response result = apiInstance.updateAdCatalogProductSet(catalogId, productSetId, updateAdCatalogProductSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#updateAdCatalogProductSet");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productSetId** | **String**|  | |
| **updateAdCatalogProductSetRequest** | [**UpdateAdCatalogProductSetRequest**](UpdateAdCatalogProductSetRequest.md)|  | |

### Return type

[**CreateAdCatalogProductSet201Response**](CreateAdCatalogProductSet201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product set updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

## updateAdCatalogProductSetWithHttpInfo

> ApiResponse<CreateAdCatalogProductSet201Response> updateAdCatalogProductSet updateAdCatalogProductSetWithHttpInfo(catalogId, productSetId, updateAdCatalogProductSetRequest)

Update a product set

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductCatalogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductCatalogsApi apiInstance = new ProductCatalogsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String productSetId = "productSetId_example"; // String | 
        UpdateAdCatalogProductSetRequest updateAdCatalogProductSetRequest = new UpdateAdCatalogProductSetRequest(); // UpdateAdCatalogProductSetRequest | 
        try {
            ApiResponse<CreateAdCatalogProductSet201Response> response = apiInstance.updateAdCatalogProductSetWithHttpInfo(catalogId, productSetId, updateAdCatalogProductSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductCatalogsApi#updateAdCatalogProductSet");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **productSetId** | **String**|  | |
| **updateAdCatalogProductSetRequest** | [**UpdateAdCatalogProductSetRequest**](UpdateAdCatalogProductSetRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCatalogProductSet201Response**](CreateAdCatalogProductSet201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product set updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The Meta login behind the account lacks catalog_management (code insufficient_permissions). Reconnect granting it, or pass catalogAccountId. |  -  |
| **404** | Resource not found |  -  |

