# GmbServicesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGoogleBusinessServices**](GmbServicesApi.md#getGoogleBusinessServices) | **GET** /v1/accounts/{accountId}/gmb-services | Get services |
| [**getGoogleBusinessServicesWithHttpInfo**](GmbServicesApi.md#getGoogleBusinessServicesWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-services | Get services |
| [**updateGoogleBusinessServices**](GmbServicesApi.md#updateGoogleBusinessServices) | **PUT** /v1/accounts/{accountId}/gmb-services | Replace services |
| [**updateGoogleBusinessServicesWithHttpInfo**](GmbServicesApi.md#updateGoogleBusinessServicesWithHttpInfo) | **PUT** /v1/accounts/{accountId}/gmb-services | Replace services |



## getGoogleBusinessServices

> GetGoogleBusinessServices200Response getGoogleBusinessServices(accountId, locationId)

Get services

Gets the services offered by a Google Business Profile location. Returns an array of service items (structured or free-form with optional price). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbServicesApi apiInstance = new GmbServicesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location.
        try {
            GetGoogleBusinessServices200Response result = apiInstance.getGoogleBusinessServices(accountId, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbServicesApi#getGoogleBusinessServices");
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
| **accountId** | **String**|  | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

[**GetGoogleBusinessServices200Response**](GetGoogleBusinessServices200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Services fetched successfully |  -  |
| **401** | Unauthorized |  -  |

## getGoogleBusinessServicesWithHttpInfo

> ApiResponse<GetGoogleBusinessServices200Response> getGoogleBusinessServices getGoogleBusinessServicesWithHttpInfo(accountId, locationId)

Get services

Gets the services offered by a Google Business Profile location. Returns an array of service items (structured or free-form with optional price). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbServicesApi apiInstance = new GmbServicesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location.
        try {
            ApiResponse<GetGoogleBusinessServices200Response> response = apiInstance.getGoogleBusinessServicesWithHttpInfo(accountId, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbServicesApi#getGoogleBusinessServices");
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
| **accountId** | **String**|  | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

ApiResponse<[**GetGoogleBusinessServices200Response**](GetGoogleBusinessServices200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Services fetched successfully |  -  |
| **401** | Unauthorized |  -  |


## updateGoogleBusinessServices

> UpdateGoogleBusinessServices200Response updateGoogleBusinessServices(accountId, updateGoogleBusinessServicesRequest, locationId)

Replace services

Replaces the entire service list for a location. Google&#39;s API requires full replacement; individual item updates are not supported. Each service can be structured (using a predefined serviceTypeId) or free-form (custom label). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbServicesApi apiInstance = new GmbServicesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGoogleBusinessServicesRequest updateGoogleBusinessServicesRequest = new UpdateGoogleBusinessServicesRequest(); // UpdateGoogleBusinessServicesRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            UpdateGoogleBusinessServices200Response result = apiInstance.updateGoogleBusinessServices(accountId, updateGoogleBusinessServicesRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbServicesApi#updateGoogleBusinessServices");
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
| **accountId** | **String**|  | |
| **updateGoogleBusinessServicesRequest** | [**UpdateGoogleBusinessServicesRequest**](UpdateGoogleBusinessServicesRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

[**UpdateGoogleBusinessServices200Response**](UpdateGoogleBusinessServices200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Services updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## updateGoogleBusinessServicesWithHttpInfo

> ApiResponse<UpdateGoogleBusinessServices200Response> updateGoogleBusinessServices updateGoogleBusinessServicesWithHttpInfo(accountId, updateGoogleBusinessServicesRequest, locationId)

Replace services

Replaces the entire service list for a location. Google&#39;s API requires full replacement; individual item updates are not supported. Each service can be structured (using a predefined serviceTypeId) or free-form (custom label). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbServicesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbServicesApi apiInstance = new GmbServicesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGoogleBusinessServicesRequest updateGoogleBusinessServicesRequest = new UpdateGoogleBusinessServicesRequest(); // UpdateGoogleBusinessServicesRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            ApiResponse<UpdateGoogleBusinessServices200Response> response = apiInstance.updateGoogleBusinessServicesWithHttpInfo(accountId, updateGoogleBusinessServicesRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbServicesApi#updateGoogleBusinessServices");
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
| **accountId** | **String**|  | |
| **updateGoogleBusinessServicesRequest** | [**UpdateGoogleBusinessServicesRequest**](UpdateGoogleBusinessServicesRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

ApiResponse<[**UpdateGoogleBusinessServices200Response**](UpdateGoogleBusinessServices200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Services updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

