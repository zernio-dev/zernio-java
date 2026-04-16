# GmbPlaceActionsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGoogleBusinessPlaceAction**](GmbPlaceActionsApi.md#createGoogleBusinessPlaceAction) | **POST** /v1/accounts/{accountId}/gmb-place-actions | Create action link |
| [**createGoogleBusinessPlaceActionWithHttpInfo**](GmbPlaceActionsApi.md#createGoogleBusinessPlaceActionWithHttpInfo) | **POST** /v1/accounts/{accountId}/gmb-place-actions | Create action link |
| [**deleteGoogleBusinessPlaceAction**](GmbPlaceActionsApi.md#deleteGoogleBusinessPlaceAction) | **DELETE** /v1/accounts/{accountId}/gmb-place-actions | Delete action link |
| [**deleteGoogleBusinessPlaceActionWithHttpInfo**](GmbPlaceActionsApi.md#deleteGoogleBusinessPlaceActionWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/gmb-place-actions | Delete action link |
| [**listGoogleBusinessPlaceActions**](GmbPlaceActionsApi.md#listGoogleBusinessPlaceActions) | **GET** /v1/accounts/{accountId}/gmb-place-actions | List action links |
| [**listGoogleBusinessPlaceActionsWithHttpInfo**](GmbPlaceActionsApi.md#listGoogleBusinessPlaceActionsWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-place-actions | List action links |
| [**updateGoogleBusinessPlaceAction**](GmbPlaceActionsApi.md#updateGoogleBusinessPlaceAction) | **PATCH** /v1/accounts/{accountId}/gmb-place-actions | Update action link |
| [**updateGoogleBusinessPlaceActionWithHttpInfo**](GmbPlaceActionsApi.md#updateGoogleBusinessPlaceActionWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/gmb-place-actions | Update action link |



## createGoogleBusinessPlaceAction

> CreateGoogleBusinessPlaceAction200Response createGoogleBusinessPlaceAction(accountId, createGoogleBusinessPlaceActionRequest, locationId)

Create action link

Creates a place action link for a location.  Available action types: APPOINTMENT, ONLINE_APPOINTMENT, DINING_RESERVATION, FOOD_ORDERING, FOOD_DELIVERY, FOOD_TAKEOUT, SHOP_ONLINE. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        CreateGoogleBusinessPlaceActionRequest createGoogleBusinessPlaceActionRequest = new CreateGoogleBusinessPlaceActionRequest(); // CreateGoogleBusinessPlaceActionRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            CreateGoogleBusinessPlaceAction200Response result = apiInstance.createGoogleBusinessPlaceAction(accountId, createGoogleBusinessPlaceActionRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#createGoogleBusinessPlaceAction");
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
| **createGoogleBusinessPlaceActionRequest** | [**CreateGoogleBusinessPlaceActionRequest**](CreateGoogleBusinessPlaceActionRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

[**CreateGoogleBusinessPlaceAction200Response**](CreateGoogleBusinessPlaceAction200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place action created successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## createGoogleBusinessPlaceActionWithHttpInfo

> ApiResponse<CreateGoogleBusinessPlaceAction200Response> createGoogleBusinessPlaceAction createGoogleBusinessPlaceActionWithHttpInfo(accountId, createGoogleBusinessPlaceActionRequest, locationId)

Create action link

Creates a place action link for a location.  Available action types: APPOINTMENT, ONLINE_APPOINTMENT, DINING_RESERVATION, FOOD_ORDERING, FOOD_DELIVERY, FOOD_TAKEOUT, SHOP_ONLINE. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        CreateGoogleBusinessPlaceActionRequest createGoogleBusinessPlaceActionRequest = new CreateGoogleBusinessPlaceActionRequest(); // CreateGoogleBusinessPlaceActionRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            ApiResponse<CreateGoogleBusinessPlaceAction200Response> response = apiInstance.createGoogleBusinessPlaceActionWithHttpInfo(accountId, createGoogleBusinessPlaceActionRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#createGoogleBusinessPlaceAction");
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
| **createGoogleBusinessPlaceActionRequest** | [**CreateGoogleBusinessPlaceActionRequest**](CreateGoogleBusinessPlaceActionRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

ApiResponse<[**CreateGoogleBusinessPlaceAction200Response**](CreateGoogleBusinessPlaceAction200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place action created successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## deleteGoogleBusinessPlaceAction

> DeleteGoogleBusinessPlaceAction200Response deleteGoogleBusinessPlaceAction(accountId, name, locationId)

Delete action link

Deletes a place action link (e.g. booking or ordering URL) from a GBP location.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String name = "name_example"; // String | The resource name of the place action link (e.g. locations/123/placeActionLinks/456)
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            DeleteGoogleBusinessPlaceAction200Response result = apiInstance.deleteGoogleBusinessPlaceAction(accountId, name, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#deleteGoogleBusinessPlaceAction");
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
| **name** | **String**| The resource name of the place action link (e.g. locations/123/placeActionLinks/456) | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

[**DeleteGoogleBusinessPlaceAction200Response**](DeleteGoogleBusinessPlaceAction200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place action deleted successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## deleteGoogleBusinessPlaceActionWithHttpInfo

> ApiResponse<DeleteGoogleBusinessPlaceAction200Response> deleteGoogleBusinessPlaceAction deleteGoogleBusinessPlaceActionWithHttpInfo(accountId, name, locationId)

Delete action link

Deletes a place action link (e.g. booking or ordering URL) from a GBP location.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String name = "name_example"; // String | The resource name of the place action link (e.g. locations/123/placeActionLinks/456)
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            ApiResponse<DeleteGoogleBusinessPlaceAction200Response> response = apiInstance.deleteGoogleBusinessPlaceActionWithHttpInfo(accountId, name, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#deleteGoogleBusinessPlaceAction");
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
| **name** | **String**| The resource name of the place action link (e.g. locations/123/placeActionLinks/456) | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

ApiResponse<[**DeleteGoogleBusinessPlaceAction200Response**](DeleteGoogleBusinessPlaceAction200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place action deleted successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## listGoogleBusinessPlaceActions

> ListGoogleBusinessPlaceActions200Response listGoogleBusinessPlaceActions(accountId, locationId, pageSize, pageToken)

List action links

Lists place action links for a Google Business Profile location.  Place actions are the booking, ordering, and reservation buttons that appear on your listing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        Integer pageSize = 100; // Integer | 
        String pageToken = "pageToken_example"; // String | 
        try {
            ListGoogleBusinessPlaceActions200Response result = apiInstance.listGoogleBusinessPlaceActions(accountId, locationId, pageSize, pageToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#listGoogleBusinessPlaceActions");
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
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |
| **pageSize** | **Integer**|  | [optional] [default to 100] |
| **pageToken** | **String**|  | [optional] |

### Return type

[**ListGoogleBusinessPlaceActions200Response**](ListGoogleBusinessPlaceActions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place actions fetched successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## listGoogleBusinessPlaceActionsWithHttpInfo

> ApiResponse<ListGoogleBusinessPlaceActions200Response> listGoogleBusinessPlaceActions listGoogleBusinessPlaceActionsWithHttpInfo(accountId, locationId, pageSize, pageToken)

List action links

Lists place action links for a Google Business Profile location.  Place actions are the booking, ordering, and reservation buttons that appear on your listing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        Integer pageSize = 100; // Integer | 
        String pageToken = "pageToken_example"; // String | 
        try {
            ApiResponse<ListGoogleBusinessPlaceActions200Response> response = apiInstance.listGoogleBusinessPlaceActionsWithHttpInfo(accountId, locationId, pageSize, pageToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#listGoogleBusinessPlaceActions");
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
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |
| **pageSize** | **Integer**|  | [optional] [default to 100] |
| **pageToken** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListGoogleBusinessPlaceActions200Response**](ListGoogleBusinessPlaceActions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place actions fetched successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## updateGoogleBusinessPlaceAction

> UpdateGoogleBusinessPlaceAction200Response updateGoogleBusinessPlaceAction(accountId, updateGoogleBusinessPlaceActionRequest, locationId)

Update action link

Updates a place action link (change URL or action type). Only the fields included in the request body will be updated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGoogleBusinessPlaceActionRequest updateGoogleBusinessPlaceActionRequest = new UpdateGoogleBusinessPlaceActionRequest(); // UpdateGoogleBusinessPlaceActionRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            UpdateGoogleBusinessPlaceAction200Response result = apiInstance.updateGoogleBusinessPlaceAction(accountId, updateGoogleBusinessPlaceActionRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#updateGoogleBusinessPlaceAction");
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
| **updateGoogleBusinessPlaceActionRequest** | [**UpdateGoogleBusinessPlaceActionRequest**](UpdateGoogleBusinessPlaceActionRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

[**UpdateGoogleBusinessPlaceAction200Response**](UpdateGoogleBusinessPlaceAction200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place action updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## updateGoogleBusinessPlaceActionWithHttpInfo

> ApiResponse<UpdateGoogleBusinessPlaceAction200Response> updateGoogleBusinessPlaceAction updateGoogleBusinessPlaceActionWithHttpInfo(accountId, updateGoogleBusinessPlaceActionRequest, locationId)

Update action link

Updates a place action link (change URL or action type). Only the fields included in the request body will be updated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbPlaceActionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbPlaceActionsApi apiInstance = new GmbPlaceActionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGoogleBusinessPlaceActionRequest updateGoogleBusinessPlaceActionRequest = new UpdateGoogleBusinessPlaceActionRequest(); // UpdateGoogleBusinessPlaceActionRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            ApiResponse<UpdateGoogleBusinessPlaceAction200Response> response = apiInstance.updateGoogleBusinessPlaceActionWithHttpInfo(accountId, updateGoogleBusinessPlaceActionRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbPlaceActionsApi#updateGoogleBusinessPlaceAction");
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
| **updateGoogleBusinessPlaceActionRequest** | [**UpdateGoogleBusinessPlaceActionRequest**](UpdateGoogleBusinessPlaceActionRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

ApiResponse<[**UpdateGoogleBusinessPlaceAction200Response**](UpdateGoogleBusinessPlaceAction200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place action updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

