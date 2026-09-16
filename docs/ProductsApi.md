# ProductsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProduct**](ProductsApi.md#getProduct) | **GET** /v1/accounts/{accountId}/products/{productId} | Get a product |
| [**getProductWithHttpInfo**](ProductsApi.md#getProductWithHttpInfo) | **GET** /v1/accounts/{accountId}/products/{productId} | Get a product |
| [**listProducts**](ProductsApi.md#listProducts) | **GET** /v1/accounts/{accountId}/products | List products |
| [**listProductsWithHttpInfo**](ProductsApi.md#listProductsWithHttpInfo) | **GET** /v1/accounts/{accountId}/products | List products |
| [**updateProduct**](ProductsApi.md#updateProduct) | **PATCH** /v1/accounts/{accountId}/products/{productId} | Update a product |
| [**updateProductWithHttpInfo**](ProductsApi.md#updateProductWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/products/{productId} | Update a product |



## getProduct

> GetProduct200Response getProduct(accountId, productId)

Get a product

Fetches a single product with its variants, options and images. &#x60;productId&#x60; is the platform&#39;s numeric product id from &#x60;GET /v1/accounts/{accountId}/products&#x60;, not a Zernio id.  Supported on Shopify (platform &#x60;shopify&#x60;); accounts on other platforms return 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String productId = "productId_example"; // String | Platform-native numeric product id. Non-numeric values return 400.
        try {
            GetProduct200Response result = apiInstance.getProduct(accountId, productId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#getProduct");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **productId** | **String**| Platform-native numeric product id. Non-numeric values return 400. | |

### Return type

[**GetProduct200Response**](GetProduct200Response.md)


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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). The store lacks the product scopes or the token was revoked; reconnect the Shopify account. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## getProductWithHttpInfo

> ApiResponse<GetProduct200Response> getProduct getProductWithHttpInfo(accountId, productId)

Get a product

Fetches a single product with its variants, options and images. &#x60;productId&#x60; is the platform&#39;s numeric product id from &#x60;GET /v1/accounts/{accountId}/products&#x60;, not a Zernio id.  Supported on Shopify (platform &#x60;shopify&#x60;); accounts on other platforms return 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String productId = "productId_example"; // String | Platform-native numeric product id. Non-numeric values return 400.
        try {
            ApiResponse<GetProduct200Response> response = apiInstance.getProductWithHttpInfo(accountId, productId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#getProduct");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **productId** | **String**| Platform-native numeric product id. Non-numeric values return 400. | |

### Return type

ApiResponse<[**GetProduct200Response**](GetProduct200Response.md)>


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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). The store lacks the product scopes or the token was revoked; reconnect the Shopify account. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## listProducts

> ListProducts200Response listProducts(accountId, limit, cursor, status, query)

List products

Lists the products on the connected store in the platform&#39;s default order, each with its variants, options and images. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages. Filter with &#x60;status&#x60; and/or &#x60;query&#x60; (the platform&#39;s product search syntax, e.g. &#x60;title:*shirt* vendor:Acme tag:summer&#x60;).  Supported on Shopify (platform &#x60;shopify&#x60;); accounts on other platforms return 400. A store connected before product access was added answers 403 insufficient_permissions until the merchant reconnects it through &#x60;GET /v1/connect/shopify&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        Integer limit = 20; // Integer | Page size (1-50).
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        String status = "active"; // String | Only products in this status.
        String query = "query_example"; // String | Platform product search syntax, passed through verbatim (Shopify: title, vendor, product_type, tag, sku, handle, created_at, updated_at, ...).
        try {
            ListProducts200Response result = apiInstance.listProducts(accountId, limit, cursor, status, query);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#listProducts");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **limit** | **Integer**| Page size (1-50). | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |
| **status** | **String**| Only products in this status. | [optional] [enum: active, draft, archived] |
| **query** | **String**| Platform product search syntax, passed through verbatim (Shopify: title, vendor, product_type, tag, sku, handle, created_at, updated_at, ...). | [optional] |

### Return type

[**ListProducts200Response**](ListProducts200Response.md)


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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). The store lacks the product scopes or the token was revoked; reconnect the Shopify account. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## listProductsWithHttpInfo

> ApiResponse<ListProducts200Response> listProducts listProductsWithHttpInfo(accountId, limit, cursor, status, query)

List products

Lists the products on the connected store in the platform&#39;s default order, each with its variants, options and images. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages. Filter with &#x60;status&#x60; and/or &#x60;query&#x60; (the platform&#39;s product search syntax, e.g. &#x60;title:*shirt* vendor:Acme tag:summer&#x60;).  Supported on Shopify (platform &#x60;shopify&#x60;); accounts on other platforms return 400. A store connected before product access was added answers 403 insufficient_permissions until the merchant reconnects it through &#x60;GET /v1/connect/shopify&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        Integer limit = 20; // Integer | Page size (1-50).
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        String status = "active"; // String | Only products in this status.
        String query = "query_example"; // String | Platform product search syntax, passed through verbatim (Shopify: title, vendor, product_type, tag, sku, handle, created_at, updated_at, ...).
        try {
            ApiResponse<ListProducts200Response> response = apiInstance.listProductsWithHttpInfo(accountId, limit, cursor, status, query);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#listProducts");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **limit** | **Integer**| Page size (1-50). | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |
| **status** | **String**| Only products in this status. | [optional] [enum: active, draft, archived] |
| **query** | **String**| Platform product search syntax, passed through verbatim (Shopify: title, vendor, product_type, tag, sku, handle, created_at, updated_at, ...). | [optional] |

### Return type

ApiResponse<[**ListProducts200Response**](ListProducts200Response.md)>


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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions). The store lacks the product scopes or the token was revoked; reconnect the Shopify account. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## updateProduct

> GetProduct200Response updateProduct(accountId, productId, updateProductRequest)

Update a product

Partial-updates a product. Send any subset of &#x60;title&#x60;, &#x60;descriptionHtml&#x60;, &#x60;handle&#x60;, &#x60;vendor&#x60;, &#x60;productType&#x60;, &#x60;tags&#x60;, &#x60;status&#x60;, &#x60;seo&#x60; and &#x60;variants&#x60;; at least one field is required (an empty body returns 400). &#x60;tags&#x60; replaces the full tag list. &#x60;variants&#x60; updates the price and compare-at price of the listed variant ids only; other variants are untouched, and a variant id that does not belong to the product is a 400. Responds with the product as it is after the update.  Supported on Shopify (platform &#x60;shopify&#x60;); accounts on other platforms return 400. A store connected before product access was added answers 403 insufficient_permissions until the merchant reconnects it through &#x60;GET /v1/connect/shopify&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String productId = "productId_example"; // String | Platform-native numeric product id. Non-numeric values return 400.
        UpdateProductRequest updateProductRequest = new UpdateProductRequest(); // UpdateProductRequest | 
        try {
            GetProduct200Response result = apiInstance.updateProduct(accountId, productId, updateProductRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#updateProduct");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **productId** | **String**| Platform-native numeric product id. Non-numeric values return 400. | |
| **updateProductRequest** | [**UpdateProductRequest**](UpdateProductRequest.md)|  | |

### Return type

[**GetProduct200Response**](GetProduct200Response.md)


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
| **403** | The platform rejected the request (code insufficient_permissions). The store lacks the product scopes or the token was revoked; reconnect the Shopify account. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## updateProductWithHttpInfo

> ApiResponse<GetProduct200Response> updateProduct updateProductWithHttpInfo(accountId, productId, updateProductRequest)

Update a product

Partial-updates a product. Send any subset of &#x60;title&#x60;, &#x60;descriptionHtml&#x60;, &#x60;handle&#x60;, &#x60;vendor&#x60;, &#x60;productType&#x60;, &#x60;tags&#x60;, &#x60;status&#x60;, &#x60;seo&#x60; and &#x60;variants&#x60;; at least one field is required (an empty body returns 400). &#x60;tags&#x60; replaces the full tag list. &#x60;variants&#x60; updates the price and compare-at price of the listed variant ids only; other variants are untouched, and a variant id that does not belong to the product is a 400. Responds with the product as it is after the update.  Supported on Shopify (platform &#x60;shopify&#x60;); accounts on other platforms return 400. A store connected before product access was added answers 403 insufficient_permissions until the merchant reconnects it through &#x60;GET /v1/connect/shopify&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ProductsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ProductsApi apiInstance = new ProductsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String productId = "productId_example"; // String | Platform-native numeric product id. Non-numeric values return 400.
        UpdateProductRequest updateProductRequest = new UpdateProductRequest(); // UpdateProductRequest | 
        try {
            ApiResponse<GetProduct200Response> response = apiInstance.updateProductWithHttpInfo(accountId, productId, updateProductRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductsApi#updateProduct");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **productId** | **String**| Platform-native numeric product id. Non-numeric values return 400. | |
| **updateProductRequest** | [**UpdateProductRequest**](UpdateProductRequest.md)|  | |

### Return type

ApiResponse<[**GetProduct200Response**](GetProduct200Response.md)>


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
| **403** | The platform rejected the request (code insufficient_permissions). The store lacks the product scopes or the token was revoked; reconnect the Shopify account. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or product not found (code product_not_found). |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

