# GmbFoodMenusApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGoogleBusinessFoodMenus**](GmbFoodMenusApi.md#getGoogleBusinessFoodMenus) | **GET** /v1/accounts/{accountId}/gmb-food-menus | Get food menus |
| [**getGoogleBusinessFoodMenusWithHttpInfo**](GmbFoodMenusApi.md#getGoogleBusinessFoodMenusWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-food-menus | Get food menus |
| [**updateGoogleBusinessFoodMenus**](GmbFoodMenusApi.md#updateGoogleBusinessFoodMenus) | **PUT** /v1/accounts/{accountId}/gmb-food-menus | Update food menus |
| [**updateGoogleBusinessFoodMenusWithHttpInfo**](GmbFoodMenusApi.md#updateGoogleBusinessFoodMenusWithHttpInfo) | **PUT** /v1/accounts/{accountId}/gmb-food-menus | Update food menus |



## getGoogleBusinessFoodMenus

> GetGoogleBusinessFoodMenus200Response getGoogleBusinessFoodMenus(accountId, locationId)

Get food menus

Returns food menus for a GBP location including sections, items, pricing, and dietary info. Only for locations with food menu support.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbFoodMenusApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbFoodMenusApi apiInstance = new GmbFoodMenusApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            GetGoogleBusinessFoodMenus200Response result = apiInstance.getGoogleBusinessFoodMenus(accountId, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbFoodMenusApi#getGoogleBusinessFoodMenus");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

[**GetGoogleBusinessFoodMenus200Response**](GetGoogleBusinessFoodMenus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Food menus fetched successfully |  -  |
| **400** | Invalid request - not a Google Business account or missing location |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **403** | Permission denied for this location |  -  |
| **404** | Resource not found |  -  |
| **500** | Failed to fetch food menus |  -  |

## getGoogleBusinessFoodMenusWithHttpInfo

> ApiResponse<GetGoogleBusinessFoodMenus200Response> getGoogleBusinessFoodMenus getGoogleBusinessFoodMenusWithHttpInfo(accountId, locationId)

Get food menus

Returns food menus for a GBP location including sections, items, pricing, and dietary info. Only for locations with food menu support.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbFoodMenusApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbFoodMenusApi apiInstance = new GmbFoodMenusApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            ApiResponse<GetGoogleBusinessFoodMenus200Response> response = apiInstance.getGoogleBusinessFoodMenusWithHttpInfo(accountId, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbFoodMenusApi#getGoogleBusinessFoodMenus");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

ApiResponse<[**GetGoogleBusinessFoodMenus200Response**](GetGoogleBusinessFoodMenus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Food menus fetched successfully |  -  |
| **400** | Invalid request - not a Google Business account or missing location |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **403** | Permission denied for this location |  -  |
| **404** | Resource not found |  -  |
| **500** | Failed to fetch food menus |  -  |


## updateGoogleBusinessFoodMenus

> UpdateGoogleBusinessFoodMenus200Response updateGoogleBusinessFoodMenus(accountId, updateGoogleBusinessFoodMenusRequest, locationId)

Update food menus

Updates food menus for a GBP location. Send the full menus array. Use updateMask for partial updates.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbFoodMenusApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbFoodMenusApi apiInstance = new GmbFoodMenusApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        UpdateGoogleBusinessFoodMenusRequest updateGoogleBusinessFoodMenusRequest = new UpdateGoogleBusinessFoodMenusRequest(); // UpdateGoogleBusinessFoodMenusRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            UpdateGoogleBusinessFoodMenus200Response result = apiInstance.updateGoogleBusinessFoodMenus(accountId, updateGoogleBusinessFoodMenusRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbFoodMenusApi#updateGoogleBusinessFoodMenus");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **updateGoogleBusinessFoodMenusRequest** | [**UpdateGoogleBusinessFoodMenusRequest**](UpdateGoogleBusinessFoodMenusRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

[**UpdateGoogleBusinessFoodMenus200Response**](UpdateGoogleBusinessFoodMenus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Food menus updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized or token expired |  -  |
| **403** | Permission denied for this location |  -  |
| **404** | Resource not found |  -  |
| **500** | Failed to update food menus |  -  |

## updateGoogleBusinessFoodMenusWithHttpInfo

> ApiResponse<UpdateGoogleBusinessFoodMenus200Response> updateGoogleBusinessFoodMenus updateGoogleBusinessFoodMenusWithHttpInfo(accountId, updateGoogleBusinessFoodMenusRequest, locationId)

Update food menus

Updates food menus for a GBP location. Send the full menus array. Use updateMask for partial updates.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbFoodMenusApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbFoodMenusApi apiInstance = new GmbFoodMenusApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        UpdateGoogleBusinessFoodMenusRequest updateGoogleBusinessFoodMenusRequest = new UpdateGoogleBusinessFoodMenusRequest(); // UpdateGoogleBusinessFoodMenusRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            ApiResponse<UpdateGoogleBusinessFoodMenus200Response> response = apiInstance.updateGoogleBusinessFoodMenusWithHttpInfo(accountId, updateGoogleBusinessFoodMenusRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbFoodMenusApi#updateGoogleBusinessFoodMenus");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **updateGoogleBusinessFoodMenusRequest** | [**UpdateGoogleBusinessFoodMenusRequest**](UpdateGoogleBusinessFoodMenusRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

ApiResponse<[**UpdateGoogleBusinessFoodMenus200Response**](UpdateGoogleBusinessFoodMenus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Food menus updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized or token expired |  -  |
| **403** | Permission denied for this location |  -  |
| **404** | Resource not found |  -  |
| **500** | Failed to update food menus |  -  |

