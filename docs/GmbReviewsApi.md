# GmbReviewsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchGetGoogleBusinessReviews**](GmbReviewsApi.md#batchGetGoogleBusinessReviews) | **POST** /v1/accounts/{accountId}/gmb-reviews/batch | Batch get reviews |
| [**batchGetGoogleBusinessReviewsWithHttpInfo**](GmbReviewsApi.md#batchGetGoogleBusinessReviewsWithHttpInfo) | **POST** /v1/accounts/{accountId}/gmb-reviews/batch | Batch get reviews |
| [**getGoogleBusinessReviews**](GmbReviewsApi.md#getGoogleBusinessReviews) | **GET** /v1/accounts/{accountId}/gmb-reviews | Get reviews |
| [**getGoogleBusinessReviewsWithHttpInfo**](GmbReviewsApi.md#getGoogleBusinessReviewsWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-reviews | Get reviews |



## batchGetGoogleBusinessReviews

> BatchGetGoogleBusinessReviews200Response batchGetGoogleBusinessReviews(accountId, batchGetGoogleBusinessReviewsRequest)

Batch get reviews

Fetches reviews across multiple locations in a single request. More efficient than calling GET /gmb-reviews per location for multi-location businesses. Reviews are grouped by location in the response. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbReviewsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbReviewsApi apiInstance = new GmbReviewsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        BatchGetGoogleBusinessReviewsRequest batchGetGoogleBusinessReviewsRequest = new BatchGetGoogleBusinessReviewsRequest(); // BatchGetGoogleBusinessReviewsRequest | 
        try {
            BatchGetGoogleBusinessReviews200Response result = apiInstance.batchGetGoogleBusinessReviews(accountId, batchGetGoogleBusinessReviewsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbReviewsApi#batchGetGoogleBusinessReviews");
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
| **batchGetGoogleBusinessReviewsRequest** | [**BatchGetGoogleBusinessReviewsRequest**](BatchGetGoogleBusinessReviewsRequest.md)|  | |

### Return type

[**BatchGetGoogleBusinessReviews200Response**](BatchGetGoogleBusinessReviews200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch reviews fetched successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## batchGetGoogleBusinessReviewsWithHttpInfo

> ApiResponse<BatchGetGoogleBusinessReviews200Response> batchGetGoogleBusinessReviews batchGetGoogleBusinessReviewsWithHttpInfo(accountId, batchGetGoogleBusinessReviewsRequest)

Batch get reviews

Fetches reviews across multiple locations in a single request. More efficient than calling GET /gmb-reviews per location for multi-location businesses. Reviews are grouped by location in the response. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbReviewsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbReviewsApi apiInstance = new GmbReviewsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        BatchGetGoogleBusinessReviewsRequest batchGetGoogleBusinessReviewsRequest = new BatchGetGoogleBusinessReviewsRequest(); // BatchGetGoogleBusinessReviewsRequest | 
        try {
            ApiResponse<BatchGetGoogleBusinessReviews200Response> response = apiInstance.batchGetGoogleBusinessReviewsWithHttpInfo(accountId, batchGetGoogleBusinessReviewsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbReviewsApi#batchGetGoogleBusinessReviews");
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
| **batchGetGoogleBusinessReviewsRequest** | [**BatchGetGoogleBusinessReviewsRequest**](BatchGetGoogleBusinessReviewsRequest.md)|  | |

### Return type

ApiResponse<[**BatchGetGoogleBusinessReviews200Response**](BatchGetGoogleBusinessReviews200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Batch reviews fetched successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## getGoogleBusinessReviews

> GetGoogleBusinessReviews200Response getGoogleBusinessReviews(accountId, locationId, pageSize, pageToken)

Get reviews

Returns reviews for a GBP account including ratings, comments, and owner replies. Use nextPageToken for pagination.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbReviewsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbReviewsApi apiInstance = new GmbReviewsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        Integer pageSize = 50; // Integer | Number of reviews to fetch per page (max 50)
        String pageToken = "pageToken_example"; // String | Pagination token from previous response
        try {
            GetGoogleBusinessReviews200Response result = apiInstance.getGoogleBusinessReviews(accountId, locationId, pageSize, pageToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbReviewsApi#getGoogleBusinessReviews");
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
| **pageSize** | **Integer**| Number of reviews to fetch per page (max 50) | [optional] [default to 50] |
| **pageToken** | **String**| Pagination token from previous response | [optional] |

### Return type

[**GetGoogleBusinessReviews200Response**](GetGoogleBusinessReviews200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reviews fetched successfully |  -  |
| **400** | Invalid request - not a Google Business account or missing location |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **403** | Permission denied for this location |  -  |
| **404** | Resource not found |  -  |
| **500** | Failed to fetch reviews |  -  |

## getGoogleBusinessReviewsWithHttpInfo

> ApiResponse<GetGoogleBusinessReviews200Response> getGoogleBusinessReviews getGoogleBusinessReviewsWithHttpInfo(accountId, locationId, pageSize, pageToken)

Get reviews

Returns reviews for a GBP account including ratings, comments, and owner replies. Use nextPageToken for pagination.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbReviewsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbReviewsApi apiInstance = new GmbReviewsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        Integer pageSize = 50; // Integer | Number of reviews to fetch per page (max 50)
        String pageToken = "pageToken_example"; // String | Pagination token from previous response
        try {
            ApiResponse<GetGoogleBusinessReviews200Response> response = apiInstance.getGoogleBusinessReviewsWithHttpInfo(accountId, locationId, pageSize, pageToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbReviewsApi#getGoogleBusinessReviews");
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
| **pageSize** | **Integer**| Number of reviews to fetch per page (max 50) | [optional] [default to 50] |
| **pageToken** | **String**| Pagination token from previous response | [optional] |

### Return type

ApiResponse<[**GetGoogleBusinessReviews200Response**](GetGoogleBusinessReviews200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reviews fetched successfully |  -  |
| **400** | Invalid request - not a Google Business account or missing location |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **403** | Permission denied for this location |  -  |
| **404** | Resource not found |  -  |
| **500** | Failed to fetch reviews |  -  |

