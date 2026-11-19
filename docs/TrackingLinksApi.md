# TrackingLinksApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTrackingLink**](TrackingLinksApi.md#createTrackingLink) | **POST** /v1/tracking-links | Create a tracking link |
| [**createTrackingLinkWithHttpInfo**](TrackingLinksApi.md#createTrackingLinkWithHttpInfo) | **POST** /v1/tracking-links | Create a tracking link |
| [**deleteTrackingLink**](TrackingLinksApi.md#deleteTrackingLink) | **DELETE** /v1/tracking-links/{linkId} | Delete a tracking link |
| [**deleteTrackingLinkWithHttpInfo**](TrackingLinksApi.md#deleteTrackingLinkWithHttpInfo) | **DELETE** /v1/tracking-links/{linkId} | Delete a tracking link |
| [**getTrackingLink**](TrackingLinksApi.md#getTrackingLink) | **GET** /v1/tracking-links/{linkId} | Get a tracking link |
| [**getTrackingLinkWithHttpInfo**](TrackingLinksApi.md#getTrackingLinkWithHttpInfo) | **GET** /v1/tracking-links/{linkId} | Get a tracking link |
| [**getTrackingLinkStats**](TrackingLinksApi.md#getTrackingLinkStats) | **GET** /v1/tracking-links/{linkId}/stats | Get a tracking link&#39;s results |
| [**getTrackingLinkStatsWithHttpInfo**](TrackingLinksApi.md#getTrackingLinkStatsWithHttpInfo) | **GET** /v1/tracking-links/{linkId}/stats | Get a tracking link&#39;s results |
| [**listTrackingLinks**](TrackingLinksApi.md#listTrackingLinks) | **GET** /v1/tracking-links | List tracking links |
| [**listTrackingLinksWithHttpInfo**](TrackingLinksApi.md#listTrackingLinksWithHttpInfo) | **GET** /v1/tracking-links | List tracking links |
| [**rotateTrackingLinkPostbackToken**](TrackingLinksApi.md#rotateTrackingLinkPostbackToken) | **POST** /v1/tracking-links/{linkId}/rotate-postback-token | Rotate a tracking link&#39;s postback URL |
| [**rotateTrackingLinkPostbackTokenWithHttpInfo**](TrackingLinksApi.md#rotateTrackingLinkPostbackTokenWithHttpInfo) | **POST** /v1/tracking-links/{linkId}/rotate-postback-token | Rotate a tracking link&#39;s postback URL |
| [**updateTrackingLink**](TrackingLinksApi.md#updateTrackingLink) | **PATCH** /v1/tracking-links/{linkId} | Update a tracking link |
| [**updateTrackingLinkWithHttpInfo**](TrackingLinksApi.md#updateTrackingLinkWithHttpInfo) | **PATCH** /v1/tracking-links/{linkId} | Update a tracking link |



## createTrackingLink

> CreateTrackingLink201Response createTrackingLink(idempotencyKey, createTrackingLinkRequest)

Create a tracking link

Creates a short link on a tracking site. Each click goes to one of &#x60;destinations&#x60;, picked by weight, so the link also split-tests landing pages. Put &#x60;url&#x60; in your ads and give &#x60;postbackUrl&#x60; to the network that reports conversions server to server. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String idempotencyKey = "idempotencyKey_example"; // String | A unique key per link you create, such as a UUID. A retry with the same key and body returns the same link.
        CreateTrackingLinkRequest createTrackingLinkRequest = new CreateTrackingLinkRequest(); // CreateTrackingLinkRequest | 
        try {
            CreateTrackingLink201Response result = apiInstance.createTrackingLink(idempotencyKey, createTrackingLinkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#createTrackingLink");
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
| **idempotencyKey** | **String**| A unique key per link you create, such as a UUID. A retry with the same key and body returns the same link. | |
| **createTrackingLinkRequest** | [**CreateTrackingLinkRequest**](CreateTrackingLinkRequest.md)|  | |

### Return type

[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Link created. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No site with this id in your workspace (code &#x60;tracking_site_not_found&#x60;). |  -  |

## createTrackingLinkWithHttpInfo

> ApiResponse<CreateTrackingLink201Response> createTrackingLink createTrackingLinkWithHttpInfo(idempotencyKey, createTrackingLinkRequest)

Create a tracking link

Creates a short link on a tracking site. Each click goes to one of &#x60;destinations&#x60;, picked by weight, so the link also split-tests landing pages. Put &#x60;url&#x60; in your ads and give &#x60;postbackUrl&#x60; to the network that reports conversions server to server. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String idempotencyKey = "idempotencyKey_example"; // String | A unique key per link you create, such as a UUID. A retry with the same key and body returns the same link.
        CreateTrackingLinkRequest createTrackingLinkRequest = new CreateTrackingLinkRequest(); // CreateTrackingLinkRequest | 
        try {
            ApiResponse<CreateTrackingLink201Response> response = apiInstance.createTrackingLinkWithHttpInfo(idempotencyKey, createTrackingLinkRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#createTrackingLink");
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
| **idempotencyKey** | **String**| A unique key per link you create, such as a UUID. A retry with the same key and body returns the same link. | |
| **createTrackingLinkRequest** | [**CreateTrackingLinkRequest**](CreateTrackingLinkRequest.md)|  | |

### Return type

ApiResponse<[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Link created. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No site with this id in your workspace (code &#x60;tracking_site_not_found&#x60;). |  -  |


## deleteTrackingLink

> void deleteTrackingLink(linkId)

Delete a tracking link

The link and its postback URL stop working at once. Conversions already stored are kept.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        try {
            apiInstance.deleteTrackingLink(linkId);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#deleteTrackingLink");
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
| **linkId** | **String**|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Link deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## deleteTrackingLinkWithHttpInfo

> ApiResponse<Void> deleteTrackingLink deleteTrackingLinkWithHttpInfo(linkId)

Delete a tracking link

The link and its postback URL stop working at once. Conversions already stored are kept.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.deleteTrackingLinkWithHttpInfo(linkId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#deleteTrackingLink");
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
| **linkId** | **String**|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Link deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getTrackingLink

> CreateTrackingLink201Response getTrackingLink(linkId)

Get a tracking link

One link, with its URL and postback URL.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        try {
            CreateTrackingLink201Response result = apiInstance.getTrackingLink(linkId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#getTrackingLink");
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
| **linkId** | **String**|  | |

### Return type

[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No link with this id in your workspace (code &#x60;tracking_link_not_found&#x60;). |  -  |

## getTrackingLinkWithHttpInfo

> ApiResponse<CreateTrackingLink201Response> getTrackingLink getTrackingLinkWithHttpInfo(linkId)

Get a tracking link

One link, with its URL and postback URL.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        try {
            ApiResponse<CreateTrackingLink201Response> response = apiInstance.getTrackingLinkWithHttpInfo(linkId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#getTrackingLink");
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
| **linkId** | **String**|  | |

### Return type

ApiResponse<[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No link with this id in your workspace (code &#x60;tracking_link_not_found&#x60;). |  -  |


## getTrackingLinkStats

> TrackingLinkStats getTrackingLinkStats(linkId, fromDate, toDate)

Get a tracking link&#39;s results

Clicks, conversions and revenue of one link over a range of days (UTC), and its clicks per destination, the result of a split test. Clicks leave out bots.  Conversions are the link&#39;s postbacks plus website conversions carrying the click id of one of its clicks, less any retracted. The range is at most 90 days, the time clicks are kept. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day of the range, `YYYY-MM-DD`.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day of the range, `YYYY-MM-DD`.
        try {
            TrackingLinkStats result = apiInstance.getTrackingLinkStats(linkId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#getTrackingLinkStats");
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
| **linkId** | **String**|  | |
| **fromDate** | **LocalDate**| First day of the range, &#x60;YYYY-MM-DD&#x60;. | |
| **toDate** | **LocalDate**| Last day of the range, &#x60;YYYY-MM-DD&#x60;. | |

### Return type

[**TrackingLinkStats**](TrackingLinkStats.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link&#39;s results. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getTrackingLinkStatsWithHttpInfo

> ApiResponse<TrackingLinkStats> getTrackingLinkStats getTrackingLinkStatsWithHttpInfo(linkId, fromDate, toDate)

Get a tracking link&#39;s results

Clicks, conversions and revenue of one link over a range of days (UTC), and its clicks per destination, the result of a split test. Clicks leave out bots.  Conversions are the link&#39;s postbacks plus website conversions carrying the click id of one of its clicks, less any retracted. The range is at most 90 days, the time clicks are kept. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day of the range, `YYYY-MM-DD`.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day of the range, `YYYY-MM-DD`.
        try {
            ApiResponse<TrackingLinkStats> response = apiInstance.getTrackingLinkStatsWithHttpInfo(linkId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#getTrackingLinkStats");
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
| **linkId** | **String**|  | |
| **fromDate** | **LocalDate**| First day of the range, &#x60;YYYY-MM-DD&#x60;. | |
| **toDate** | **LocalDate**| Last day of the range, &#x60;YYYY-MM-DD&#x60;. | |

### Return type

ApiResponse<[**TrackingLinkStats**](TrackingLinkStats.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link&#39;s results. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## listTrackingLinks

> ListTrackingLinks200Response listTrackingLinks(profileId, siteId, limit, cursor)

List tracking links

The tracking links of your workspace in creation order. Pass &#x60;profileId&#x60; or &#x60;siteId&#x60; to list one profile&#39;s or one site&#39;s links.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        String siteId = "siteId_example"; // String | 
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `pagination.nextCursor` from the previous page.
        try {
            ListTrackingLinks200Response result = apiInstance.listTrackingLinks(profileId, siteId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#listTrackingLinks");
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
| **profileId** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;pagination.nextCursor&#x60; from the previous page. | [optional] |

### Return type

[**ListTrackingLinks200Response**](ListTrackingLinks200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of links. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## listTrackingLinksWithHttpInfo

> ApiResponse<ListTrackingLinks200Response> listTrackingLinks listTrackingLinksWithHttpInfo(profileId, siteId, limit, cursor)

List tracking links

The tracking links of your workspace in creation order. Pass &#x60;profileId&#x60; or &#x60;siteId&#x60; to list one profile&#39;s or one site&#39;s links.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String profileId = "profileId_example"; // String | 
        String siteId = "siteId_example"; // String | 
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `pagination.nextCursor` from the previous page.
        try {
            ApiResponse<ListTrackingLinks200Response> response = apiInstance.listTrackingLinksWithHttpInfo(profileId, siteId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#listTrackingLinks");
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
| **profileId** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;pagination.nextCursor&#x60; from the previous page. | [optional] |

### Return type

ApiResponse<[**ListTrackingLinks200Response**](ListTrackingLinks200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of links. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## rotateTrackingLinkPostbackToken

> CreateTrackingLink201Response rotateTrackingLinkPostbackToken(linkId, idempotencyKey)

Rotate a tracking link&#39;s postback URL

Issues a new &#x60;postbackUrl&#x60;. The old one stops working at once, so update it at the network right after.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        String idempotencyKey = "idempotencyKey_example"; // String | A unique key per rotation, such as a UUID.
        try {
            CreateTrackingLink201Response result = apiInstance.rotateTrackingLinkPostbackToken(linkId, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#rotateTrackingLinkPostbackToken");
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
| **linkId** | **String**|  | |
| **idempotencyKey** | **String**| A unique key per rotation, such as a UUID. | |

### Return type

[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link with its new postback URL. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## rotateTrackingLinkPostbackTokenWithHttpInfo

> ApiResponse<CreateTrackingLink201Response> rotateTrackingLinkPostbackToken rotateTrackingLinkPostbackTokenWithHttpInfo(linkId, idempotencyKey)

Rotate a tracking link&#39;s postback URL

Issues a new &#x60;postbackUrl&#x60;. The old one stops working at once, so update it at the network right after.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        String idempotencyKey = "idempotencyKey_example"; // String | A unique key per rotation, such as a UUID.
        try {
            ApiResponse<CreateTrackingLink201Response> response = apiInstance.rotateTrackingLinkPostbackTokenWithHttpInfo(linkId, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#rotateTrackingLinkPostbackToken");
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
| **linkId** | **String**|  | |
| **idempotencyKey** | **String**| A unique key per rotation, such as a UUID. | |

### Return type

ApiResponse<[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link with its new postback URL. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## updateTrackingLink

> CreateTrackingLink201Response updateTrackingLink(linkId, updateTrackingLinkRequest)

Update a tracking link

Changes the link&#39;s name, destinations, campaign hints or status. Send at least one field. &#x60;status: paused&#x60; turns the link off until it is set back to &#x60;active&#x60;. &#x60;campaign: null&#x60; removes the hints. The code and URL never change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        UpdateTrackingLinkRequest updateTrackingLinkRequest = new UpdateTrackingLinkRequest(); // UpdateTrackingLinkRequest | 
        try {
            CreateTrackingLink201Response result = apiInstance.updateTrackingLink(linkId, updateTrackingLinkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#updateTrackingLink");
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
| **linkId** | **String**|  | |
| **updateTrackingLinkRequest** | [**UpdateTrackingLinkRequest**](UpdateTrackingLinkRequest.md)|  | |

### Return type

[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated link. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## updateTrackingLinkWithHttpInfo

> ApiResponse<CreateTrackingLink201Response> updateTrackingLink updateTrackingLinkWithHttpInfo(linkId, updateTrackingLinkRequest)

Update a tracking link

Changes the link&#39;s name, destinations, campaign hints or status. Send at least one field. &#x60;status: paused&#x60; turns the link off until it is set back to &#x60;active&#x60;. &#x60;campaign: null&#x60; removes the hints. The code and URL never change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingLinksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingLinksApi apiInstance = new TrackingLinksApi(defaultClient);
        String linkId = "linkId_example"; // String | 
        UpdateTrackingLinkRequest updateTrackingLinkRequest = new UpdateTrackingLinkRequest(); // UpdateTrackingLinkRequest | 
        try {
            ApiResponse<CreateTrackingLink201Response> response = apiInstance.updateTrackingLinkWithHttpInfo(linkId, updateTrackingLinkRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingLinksApi#updateTrackingLink");
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
| **linkId** | **String**|  | |
| **updateTrackingLinkRequest** | [**UpdateTrackingLinkRequest**](UpdateTrackingLinkRequest.md)|  | |

### Return type

ApiResponse<[**CreateTrackingLink201Response**](CreateTrackingLink201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated link. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

