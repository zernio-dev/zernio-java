# TrackingTagsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTrackingTagSharedAccount**](TrackingTagsApi.md#addTrackingTagSharedAccount) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Share a tracking tag with an ad account |
| [**addTrackingTagSharedAccountWithHttpInfo**](TrackingTagsApi.md#addTrackingTagSharedAccountWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Share a tracking tag with an ad account |
| [**createTrackingTag**](TrackingTagsApi.md#createTrackingTag) | **POST** /v1/accounts/{accountId}/tracking-tags | Create a tracking tag (Meta Pixel) |
| [**createTrackingTagWithHttpInfo**](TrackingTagsApi.md#createTrackingTagWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags | Create a tracking tag (Meta Pixel) |
| [**getTrackingTag**](TrackingTagsApi.md#getTrackingTag) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId} | Fetch a single tracking tag (Meta Pixel) |
| [**getTrackingTagWithHttpInfo**](TrackingTagsApi.md#getTrackingTagWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId} | Fetch a single tracking tag (Meta Pixel) |
| [**getTrackingTagStats**](TrackingTagsApi.md#getTrackingTagStats) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/stats | Aggregated event stats for a tracking tag (Meta Pixel) |
| [**getTrackingTagStatsWithHttpInfo**](TrackingTagsApi.md#getTrackingTagStatsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/stats | Aggregated event stats for a tracking tag (Meta Pixel) |
| [**listTrackingTagSharedAccounts**](TrackingTagsApi.md#listTrackingTagSharedAccounts) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | List ad accounts a tracking tag is shared with |
| [**listTrackingTagSharedAccountsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagSharedAccountsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | List ad accounts a tracking tag is shared with |
| [**listTrackingTags**](TrackingTagsApi.md#listTrackingTags) | **GET** /v1/accounts/{accountId}/tracking-tags | List tracking tags (Meta Pixels) |
| [**listTrackingTagsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags | List tracking tags (Meta Pixels) |
| [**removeTrackingTagSharedAccount**](TrackingTagsApi.md#removeTrackingTagSharedAccount) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Stop sharing a tracking tag with an ad account |
| [**removeTrackingTagSharedAccountWithHttpInfo**](TrackingTagsApi.md#removeTrackingTagSharedAccountWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Stop sharing a tracking tag with an ad account |
| [**updateTrackingTag**](TrackingTagsApi.md#updateTrackingTag) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId} | Update a tracking tag (Meta Pixel) |
| [**updateTrackingTagWithHttpInfo**](TrackingTagsApi.md#updateTrackingTagWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId} | Update a tracking tag (Meta Pixel) |



## addTrackingTagSharedAccount

> AddTrackingTagSharedAccount201Response addTrackingTagSharedAccount(accountId, tagId, addTrackingTagSharedAccountRequest)

Share a tracking tag with an ad account

Shares the pixel with another ad account so campaigns/audiences in that account can use it. Requires that you administer both the pixel&#39;s owning Business Manager and the target ad account; a pixel on a personal (non-BM) ad account can&#39;t be shared (Meta will reject the call). Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        AddTrackingTagSharedAccountRequest addTrackingTagSharedAccountRequest = new AddTrackingTagSharedAccountRequest(); // AddTrackingTagSharedAccountRequest | 
        try {
            AddTrackingTagSharedAccount201Response result = apiInstance.addTrackingTagSharedAccount(accountId, tagId, addTrackingTagSharedAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#addTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **addTrackingTagSharedAccountRequest** | [**AddTrackingTagSharedAccountRequest**](AddTrackingTagSharedAccountRequest.md)|  | |

### Return type

[**AddTrackingTagSharedAccount201Response**](AddTrackingTagSharedAccount201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tracking tag shared with the ad account |  -  |
| **400** | Invalid body / &#x60;adAccountId&#x60;, or Meta rejected the share (e.g. personal ad account). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support shared accounts. |  -  |

## addTrackingTagSharedAccountWithHttpInfo

> ApiResponse<AddTrackingTagSharedAccount201Response> addTrackingTagSharedAccount addTrackingTagSharedAccountWithHttpInfo(accountId, tagId, addTrackingTagSharedAccountRequest)

Share a tracking tag with an ad account

Shares the pixel with another ad account so campaigns/audiences in that account can use it. Requires that you administer both the pixel&#39;s owning Business Manager and the target ad account; a pixel on a personal (non-BM) ad account can&#39;t be shared (Meta will reject the call). Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        AddTrackingTagSharedAccountRequest addTrackingTagSharedAccountRequest = new AddTrackingTagSharedAccountRequest(); // AddTrackingTagSharedAccountRequest | 
        try {
            ApiResponse<AddTrackingTagSharedAccount201Response> response = apiInstance.addTrackingTagSharedAccountWithHttpInfo(accountId, tagId, addTrackingTagSharedAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#addTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **addTrackingTagSharedAccountRequest** | [**AddTrackingTagSharedAccountRequest**](AddTrackingTagSharedAccountRequest.md)|  | |

### Return type

ApiResponse<[**AddTrackingTagSharedAccount201Response**](AddTrackingTagSharedAccount201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tracking tag shared with the ad account |  -  |
| **400** | Invalid body / &#x60;adAccountId&#x60;, or Meta rejected the share (e.g. personal ad account). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support shared accounts. |  -  |


## createTrackingTag

> CreateTrackingTag201Response createTrackingTag(accountId, createTrackingTagRequest)

Create a tracking tag (Meta Pixel)

Creates a Meta Pixel on the given ad account (&#x60;POST /act_{id}/adspixels&#x60; — &#x60;name&#x60; is the only input). Returns the created tag including its install &#x60;code&#x60;. The pixel is owned by the Business Manager that owns the ad account; a pixel created on a personal (non-BM) ad account ends up with &#x60;ownerBusinessId: null&#x60; and can&#39;t be shared with other ad accounts.  Creating a pixel does NOT install it — install the returned &#x60;code&#x60; snippet on the site, or send events server-side via &#x60;POST /v1/ads/conversions&#x60;. The check &#x60;installed&#x60; is derived from &#x60;lastFiredTime&#x60;.  NOT idempotent: each call creates a new pixel. Do not retry blindly on timeout. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id (platform `metaads`).
        CreateTrackingTagRequest createTrackingTagRequest = new CreateTrackingTagRequest(); // CreateTrackingTagRequest | 
        try {
            CreateTrackingTag201Response result = apiInstance.createTrackingTag(accountId, createTrackingTagRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#createTrackingTag");
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
| **accountId** | **String**| Meta ads SocialAccount id (platform &#x60;metaads&#x60;). | |
| **createTrackingTagRequest** | [**CreateTrackingTagRequest**](CreateTrackingTagRequest.md)|  | |

### Return type

[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tracking tag created |  -  |
| **400** | Invalid body, invalid &#x60;adAccountId&#x60;, over the per-business pixel cap, or ad account not in a Business Manager. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support creating tracking tags. |  -  |

## createTrackingTagWithHttpInfo

> ApiResponse<CreateTrackingTag201Response> createTrackingTag createTrackingTagWithHttpInfo(accountId, createTrackingTagRequest)

Create a tracking tag (Meta Pixel)

Creates a Meta Pixel on the given ad account (&#x60;POST /act_{id}/adspixels&#x60; — &#x60;name&#x60; is the only input). Returns the created tag including its install &#x60;code&#x60;. The pixel is owned by the Business Manager that owns the ad account; a pixel created on a personal (non-BM) ad account ends up with &#x60;ownerBusinessId: null&#x60; and can&#39;t be shared with other ad accounts.  Creating a pixel does NOT install it — install the returned &#x60;code&#x60; snippet on the site, or send events server-side via &#x60;POST /v1/ads/conversions&#x60;. The check &#x60;installed&#x60; is derived from &#x60;lastFiredTime&#x60;.  NOT idempotent: each call creates a new pixel. Do not retry blindly on timeout. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id (platform `metaads`).
        CreateTrackingTagRequest createTrackingTagRequest = new CreateTrackingTagRequest(); // CreateTrackingTagRequest | 
        try {
            ApiResponse<CreateTrackingTag201Response> response = apiInstance.createTrackingTagWithHttpInfo(accountId, createTrackingTagRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#createTrackingTag");
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
| **accountId** | **String**| Meta ads SocialAccount id (platform &#x60;metaads&#x60;). | |
| **createTrackingTagRequest** | [**CreateTrackingTagRequest**](CreateTrackingTagRequest.md)|  | |

### Return type

ApiResponse<[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tracking tag created |  -  |
| **400** | Invalid body, invalid &#x60;adAccountId&#x60;, over the per-business pixel cap, or ad account not in a Business Manager. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support creating tracking tags. |  -  |


## getTrackingTag

> CreateTrackingTag201Response getTrackingTag(accountId, tagId)

Fetch a single tracking tag (Meta Pixel)

Returns the full tag record including the base-code &#x60;code&#x60; snippet, &#x60;lastFiredTime&#x60;, &#x60;ownerBusinessId&#x60;, &#x60;isUnavailable&#x60;, etc. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        try {
            CreateTrackingTag201Response result = apiInstance.getTrackingTag(accountId, tagId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTag");
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
| **tagId** | **String**| Pixel id. | |

### Return type

[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tag fetched |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support fetching a tracking tag. |  -  |

## getTrackingTagWithHttpInfo

> ApiResponse<CreateTrackingTag201Response> getTrackingTag getTrackingTagWithHttpInfo(accountId, tagId)

Fetch a single tracking tag (Meta Pixel)

Returns the full tag record including the base-code &#x60;code&#x60; snippet, &#x60;lastFiredTime&#x60;, &#x60;ownerBusinessId&#x60;, &#x60;isUnavailable&#x60;, etc. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        try {
            ApiResponse<CreateTrackingTag201Response> response = apiInstance.getTrackingTagWithHttpInfo(accountId, tagId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTag");
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
| **tagId** | **String**| Pixel id. | |

### Return type

ApiResponse<[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tag fetched |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support fetching a tracking tag. |  -  |


## getTrackingTagStats

> GetTrackingTagStats200Response getTrackingTagStats(accountId, tagId, aggregation, startTime, endTime)

Aggregated event stats for a tracking tag (Meta Pixel)

Returns aggregated event counts for the pixel (&#x60;GET /{pixel_id}/stats&#x60;). Rows are passed through from Meta as-is — their shape depends on the &#x60;aggregation&#x60; requested. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        String aggregation = "event"; // String | Aggregation dimension. Defaults to `event`.
        Integer startTime = 56; // Integer | Unix seconds lower bound.
        Integer endTime = 56; // Integer | Unix seconds upper bound.
        try {
            GetTrackingTagStats200Response result = apiInstance.getTrackingTagStats(accountId, tagId, aggregation, startTime, endTime);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagStats");
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
| **tagId** | **String**| Pixel id. | |
| **aggregation** | **String**| Aggregation dimension. Defaults to &#x60;event&#x60;. | [optional] [default to event] [enum: event, host, url, url_by_rule, pixel_fire, device_type, device_os, browser_type, had_pii, custom_data_field, match_keys, event_source, event_detection_method, event_processing_results, event_total_counts, event_value_count] |
| **startTime** | **Integer**| Unix seconds lower bound. | [optional] |
| **endTime** | **Integer**| Unix seconds upper bound. | [optional] |

### Return type

[**GetTrackingTagStats200Response**](GetTrackingTagStats200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stats fetched |  -  |
| **400** | Invalid query parameter. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support tracking-tag stats. |  -  |

## getTrackingTagStatsWithHttpInfo

> ApiResponse<GetTrackingTagStats200Response> getTrackingTagStats getTrackingTagStatsWithHttpInfo(accountId, tagId, aggregation, startTime, endTime)

Aggregated event stats for a tracking tag (Meta Pixel)

Returns aggregated event counts for the pixel (&#x60;GET /{pixel_id}/stats&#x60;). Rows are passed through from Meta as-is — their shape depends on the &#x60;aggregation&#x60; requested. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        String aggregation = "event"; // String | Aggregation dimension. Defaults to `event`.
        Integer startTime = 56; // Integer | Unix seconds lower bound.
        Integer endTime = 56; // Integer | Unix seconds upper bound.
        try {
            ApiResponse<GetTrackingTagStats200Response> response = apiInstance.getTrackingTagStatsWithHttpInfo(accountId, tagId, aggregation, startTime, endTime);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagStats");
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
| **tagId** | **String**| Pixel id. | |
| **aggregation** | **String**| Aggregation dimension. Defaults to &#x60;event&#x60;. | [optional] [default to event] [enum: event, host, url, url_by_rule, pixel_fire, device_type, device_os, browser_type, had_pii, custom_data_field, match_keys, event_source, event_detection_method, event_processing_results, event_total_counts, event_value_count] |
| **startTime** | **Integer**| Unix seconds lower bound. | [optional] |
| **endTime** | **Integer**| Unix seconds upper bound. | [optional] |

### Return type

ApiResponse<[**GetTrackingTagStats200Response**](GetTrackingTagStats200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stats fetched |  -  |
| **400** | Invalid query parameter. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support tracking-tag stats. |  -  |


## listTrackingTagSharedAccounts

> ListTrackingTagSharedAccounts200Response listTrackingTagSharedAccounts(accountId, tagId)

List ad accounts a tracking tag is shared with

Meta only (platform &#x60;metaads&#x60;); other platforms return 405.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        try {
            ListTrackingTagSharedAccounts200Response result = apiInstance.listTrackingTagSharedAccounts(accountId, tagId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagSharedAccounts");
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
| **tagId** | **String**| Pixel id. | |

### Return type

[**ListTrackingTagSharedAccounts200Response**](ListTrackingTagSharedAccounts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shared ad accounts listed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support shared accounts. |  -  |

## listTrackingTagSharedAccountsWithHttpInfo

> ApiResponse<ListTrackingTagSharedAccounts200Response> listTrackingTagSharedAccounts listTrackingTagSharedAccountsWithHttpInfo(accountId, tagId)

List ad accounts a tracking tag is shared with

Meta only (platform &#x60;metaads&#x60;); other platforms return 405.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        try {
            ApiResponse<ListTrackingTagSharedAccounts200Response> response = apiInstance.listTrackingTagSharedAccountsWithHttpInfo(accountId, tagId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagSharedAccounts");
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
| **tagId** | **String**| Pixel id. | |

### Return type

ApiResponse<[**ListTrackingTagSharedAccounts200Response**](ListTrackingTagSharedAccounts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shared ad accounts listed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support shared accounts. |  -  |


## listTrackingTags

> ListTrackingTags200Response listTrackingTags(accountId, adAccountId)

List tracking tags (Meta Pixels)

Returns the tracking tags (Meta Pixels) the connected ads account can see. Pass &#x60;?adAccountId&#x3D;act_...&#x60; to scope the list to a single ad account; omit it to list every pixel reachable by the token (the name is then suffixed with the ad account it was discovered on, for disambiguation). The list view omits &#x60;code&#x60; — call &#x60;getTrackingTag&#x60; for the install snippet and full detail.  Meta only today (platform &#x60;metaads&#x60;); other platforms return 405. The &#x60;accountId&#x60; must be the Meta *ads* SocialAccount created by the Ads add-on connect flow, not a Facebook/Instagram posting account. Get your &#x60;act_...&#x60; ids from &#x60;GET /v1/ads/accounts&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id (platform `metaads`).
        String adAccountId = "adAccountId_example"; // String | Optional. Scope to one ad account, e.g. `act_123456789`.
        try {
            ListTrackingTags200Response result = apiInstance.listTrackingTags(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTags");
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
| **accountId** | **String**| Meta ads SocialAccount id (platform &#x60;metaads&#x60;). | |
| **adAccountId** | **String**| Optional. Scope to one ad account, e.g. &#x60;act_123456789&#x60;. | [optional] |

### Return type

[**ListTrackingTags200Response**](ListTrackingTags200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tags listed |  -  |
| **400** | Account platform not supported, or invalid &#x60;adAccountId&#x60;. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support listing tracking tags. |  -  |

## listTrackingTagsWithHttpInfo

> ApiResponse<ListTrackingTags200Response> listTrackingTags listTrackingTagsWithHttpInfo(accountId, adAccountId)

List tracking tags (Meta Pixels)

Returns the tracking tags (Meta Pixels) the connected ads account can see. Pass &#x60;?adAccountId&#x3D;act_...&#x60; to scope the list to a single ad account; omit it to list every pixel reachable by the token (the name is then suffixed with the ad account it was discovered on, for disambiguation). The list view omits &#x60;code&#x60; — call &#x60;getTrackingTag&#x60; for the install snippet and full detail.  Meta only today (platform &#x60;metaads&#x60;); other platforms return 405. The &#x60;accountId&#x60; must be the Meta *ads* SocialAccount created by the Ads add-on connect flow, not a Facebook/Instagram posting account. Get your &#x60;act_...&#x60; ids from &#x60;GET /v1/ads/accounts&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id (platform `metaads`).
        String adAccountId = "adAccountId_example"; // String | Optional. Scope to one ad account, e.g. `act_123456789`.
        try {
            ApiResponse<ListTrackingTags200Response> response = apiInstance.listTrackingTagsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTags");
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
| **accountId** | **String**| Meta ads SocialAccount id (platform &#x60;metaads&#x60;). | |
| **adAccountId** | **String**| Optional. Scope to one ad account, e.g. &#x60;act_123456789&#x60;. | [optional] |

### Return type

ApiResponse<[**ListTrackingTags200Response**](ListTrackingTags200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tags listed |  -  |
| **400** | Account platform not supported, or invalid &#x60;adAccountId&#x60;. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support listing tracking tags. |  -  |


## removeTrackingTagSharedAccount

> void removeTrackingTagSharedAccount(accountId, tagId, adAccountId)

Stop sharing a tracking tag with an ad account

&#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        String adAccountId = "adAccountId_example"; // String | Ad account to unshare, e.g. `act_123456789`. May also be sent in the JSON body.
        try {
            apiInstance.removeTrackingTagSharedAccount(accountId, tagId, adAccountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **adAccountId** | **String**| Ad account to unshare, e.g. &#x60;act_123456789&#x60;. May also be sent in the JSON body. | [optional] |

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
| **204** | Ad account unshared (no content). |  -  |
| **400** | &#x60;adAccountId&#x60; missing (neither query nor body), or Meta rejected the unshare. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support shared accounts. |  -  |

## removeTrackingTagSharedAccountWithHttpInfo

> ApiResponse<Void> removeTrackingTagSharedAccount removeTrackingTagSharedAccountWithHttpInfo(accountId, tagId, adAccountId)

Stop sharing a tracking tag with an ad account

&#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. Meta only (platform &#x60;metaads&#x60;); other platforms return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        String adAccountId = "adAccountId_example"; // String | Ad account to unshare, e.g. `act_123456789`. May also be sent in the JSON body.
        try {
            ApiResponse<Void> response = apiInstance.removeTrackingTagSharedAccountWithHttpInfo(accountId, tagId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **adAccountId** | **String**| Ad account to unshare, e.g. &#x60;act_123456789&#x60;. May also be sent in the JSON body. | [optional] |

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
| **204** | Ad account unshared (no content). |  -  |
| **400** | &#x60;adAccountId&#x60; missing (neither query nor body), or Meta rejected the unshare. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support shared accounts. |  -  |


## updateTrackingTag

> CreateTrackingTag201Response updateTrackingTag(accountId, tagId, updateTrackingTagRequest)

Update a tracking tag (Meta Pixel)

Partial-update a pixel. Whitelisted fields: &#x60;name&#x60; (rename), &#x60;enableAutomaticMatching&#x60;, &#x60;automaticMatchingFields&#x60;, &#x60;firstPartyCookieStatus&#x60;, &#x60;dataUseSetting&#x60;. At least one is required. Returns the re-fetched canonical tag. Meta only (platform &#x60;metaads&#x60;); other platforms return 405.  There is no DELETE — Meta has no API to delete a pixel. To stop using one, unshare it from your ad accounts (&#x60;DELETE .../tracking-tags/{tagId}/shared-accounts&#x60;) or disable it in Events Manager. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        UpdateTrackingTagRequest updateTrackingTagRequest = new UpdateTrackingTagRequest(); // UpdateTrackingTagRequest | 
        try {
            CreateTrackingTag201Response result = apiInstance.updateTrackingTag(accountId, tagId, updateTrackingTagRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateTrackingTag");
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
| **tagId** | **String**| Pixel id. | |
| **updateTrackingTagRequest** | [**UpdateTrackingTagRequest**](UpdateTrackingTagRequest.md)|  | |

### Return type

[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tag updated (re-fetched canonical state) |  -  |
| **400** | Invalid body (e.g. no fields supplied) or Meta validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support updating tracking tags. |  -  |

## updateTrackingTagWithHttpInfo

> ApiResponse<CreateTrackingTag201Response> updateTrackingTag updateTrackingTagWithHttpInfo(accountId, tagId, updateTrackingTagRequest)

Update a tracking tag (Meta Pixel)

Partial-update a pixel. Whitelisted fields: &#x60;name&#x60; (rename), &#x60;enableAutomaticMatching&#x60;, &#x60;automaticMatchingFields&#x60;, &#x60;firstPartyCookieStatus&#x60;, &#x60;dataUseSetting&#x60;. At least one is required. Returns the re-fetched canonical tag. Meta only (platform &#x60;metaads&#x60;); other platforms return 405.  There is no DELETE — Meta has no API to delete a pixel. To stop using one, unshare it from your ad accounts (&#x60;DELETE .../tracking-tags/{tagId}/shared-accounts&#x60;) or disable it in Events Manager. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        UpdateTrackingTagRequest updateTrackingTagRequest = new UpdateTrackingTagRequest(); // UpdateTrackingTagRequest | 
        try {
            ApiResponse<CreateTrackingTag201Response> response = apiInstance.updateTrackingTagWithHttpInfo(accountId, tagId, updateTrackingTagRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateTrackingTag");
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
| **tagId** | **String**| Pixel id. | |
| **updateTrackingTagRequest** | [**UpdateTrackingTagRequest**](UpdateTrackingTagRequest.md)|  | |

### Return type

ApiResponse<[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tag updated (re-fetched canonical state) |  -  |
| **400** | Invalid body (e.g. no fields supplied) or Meta validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required, or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | Account or tracking tag not found. |  -  |
| **405** | Platform does not support updating tracking tags. |  -  |

