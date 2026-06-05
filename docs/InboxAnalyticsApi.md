# InboxAnalyticsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInboxConversationAnalytics**](InboxAnalyticsApi.md#getInboxConversationAnalytics) | **GET** /v1/analytics/inbox/conversations/{conversationId} | Get analytics for a single conversation |
| [**getInboxConversationAnalyticsWithHttpInfo**](InboxAnalyticsApi.md#getInboxConversationAnalyticsWithHttpInfo) | **GET** /v1/analytics/inbox/conversations/{conversationId} | Get analytics for a single conversation |
| [**getInboxHeatmap**](InboxAnalyticsApi.md#getInboxHeatmap) | **GET** /v1/analytics/inbox/heatmap | Get inbox day-of-week × hour-of-day heatmap |
| [**getInboxHeatmapWithHttpInfo**](InboxAnalyticsApi.md#getInboxHeatmapWithHttpInfo) | **GET** /v1/analytics/inbox/heatmap | Get inbox day-of-week × hour-of-day heatmap |
| [**getInboxResponseTime**](InboxAnalyticsApi.md#getInboxResponseTime) | **GET** /v1/analytics/inbox/response-time | Get inbox response-time stats |
| [**getInboxResponseTimeWithHttpInfo**](InboxAnalyticsApi.md#getInboxResponseTimeWithHttpInfo) | **GET** /v1/analytics/inbox/response-time | Get inbox response-time stats |
| [**getInboxSourceBreakdown**](InboxAnalyticsApi.md#getInboxSourceBreakdown) | **GET** /v1/analytics/inbox/source-breakdown | Get inbox source breakdown |
| [**getInboxSourceBreakdownWithHttpInfo**](InboxAnalyticsApi.md#getInboxSourceBreakdownWithHttpInfo) | **GET** /v1/analytics/inbox/source-breakdown | Get inbox source breakdown |
| [**getInboxTopAccounts**](InboxAnalyticsApi.md#getInboxTopAccounts) | **GET** /v1/analytics/inbox/top-accounts | Get top accounts by inbox volume |
| [**getInboxTopAccountsWithHttpInfo**](InboxAnalyticsApi.md#getInboxTopAccountsWithHttpInfo) | **GET** /v1/analytics/inbox/top-accounts | Get top accounts by inbox volume |
| [**getInboxVolume**](InboxAnalyticsApi.md#getInboxVolume) | **GET** /v1/analytics/inbox/volume | Get inbox messaging volume |
| [**getInboxVolumeWithHttpInfo**](InboxAnalyticsApi.md#getInboxVolumeWithHttpInfo) | **GET** /v1/analytics/inbox/volume | Get inbox messaging volume |
| [**listInboxConversationAnalytics**](InboxAnalyticsApi.md#listInboxConversationAnalytics) | **GET** /v1/analytics/inbox/conversations | List conversations with inbox analytics |
| [**listInboxConversationAnalyticsWithHttpInfo**](InboxAnalyticsApi.md#listInboxConversationAnalyticsWithHttpInfo) | **GET** /v1/analytics/inbox/conversations | List conversations with inbox analytics |



## getInboxConversationAnalytics

> GetInboxConversationAnalytics200Response getInboxConversationAnalytics(conversationId, fromDate, toDate)

Get analytics for a single conversation

Per-conversation inbox analytics. The inbox analog of /v1/analytics/post-timeline — one conversation, daily totals, source mix.  The {conversationId} path param accepts EITHER the Mongo &#x60;_id&#x60; of the Conversation document OR its &#x60;platformConversationId&#x60; (the same identity used by metadata.conversationId at ingest time). Ownership is verified in MongoDB against the caller&#39;s team before the Tinybird query fires.  Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        String conversationId = "conversationId_example"; // String | Mongo _id or platformConversationId.
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        try {
            GetInboxConversationAnalytics200Response result = apiInstance.getInboxConversationAnalytics(conversationId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxConversationAnalytics");
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
| **conversationId** | **String**| Mongo _id or platformConversationId. | |
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |

### Return type

[**GetInboxConversationAnalytics200Response**](GetInboxConversationAnalytics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-conversation analytics |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **404** | Conversation not found or not owned by the caller&#39;s team |  -  |
| **500** | Internal server error |  -  |

## getInboxConversationAnalyticsWithHttpInfo

> ApiResponse<GetInboxConversationAnalytics200Response> getInboxConversationAnalytics getInboxConversationAnalyticsWithHttpInfo(conversationId, fromDate, toDate)

Get analytics for a single conversation

Per-conversation inbox analytics. The inbox analog of /v1/analytics/post-timeline — one conversation, daily totals, source mix.  The {conversationId} path param accepts EITHER the Mongo &#x60;_id&#x60; of the Conversation document OR its &#x60;platformConversationId&#x60; (the same identity used by metadata.conversationId at ingest time). Ownership is verified in MongoDB against the caller&#39;s team before the Tinybird query fires.  Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        String conversationId = "conversationId_example"; // String | Mongo _id or platformConversationId.
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        try {
            ApiResponse<GetInboxConversationAnalytics200Response> response = apiInstance.getInboxConversationAnalyticsWithHttpInfo(conversationId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxConversationAnalytics");
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
| **conversationId** | **String**| Mongo _id or platformConversationId. | |
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |

### Return type

ApiResponse<[**GetInboxConversationAnalytics200Response**](GetInboxConversationAnalytics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-conversation analytics |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **404** | Conversation not found or not owned by the caller&#39;s team |  -  |
| **500** | Internal server error |  -  |


## getInboxHeatmap

> GetInboxHeatmap200Response getInboxHeatmap(fromDate, toDate, profileId, platform, accountId, source, action)

Get inbox day-of-week × hour-of-day heatmap

Day-of-week × hour-of-day breakdown of inbox messages. Buckets are sparse — only cells with at least one event are returned; clients zero-fill the rest to render the full 7×24 grid. The &#x60;dow&#x60; field follows ClickHouse&#39;s &#x60;toDayOfWeek&#x60; convention (1 &#x3D; Monday … 7 &#x3D; Sunday). Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String source = "source_example"; // String | 
        String action = "message.received"; // String | Narrow to a single event type. \"all\" or omitted means no filter.
        try {
            GetInboxHeatmap200Response result = apiInstance.getInboxHeatmap(fromDate, toDate, profileId, platform, accountId, source, action);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxHeatmap");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **source** | **String**|  | [optional] |
| **action** | **String**| Narrow to a single event type. \&quot;all\&quot; or omitted means no filter. | [optional] [enum: message.received, message.sent, message.read, all] |

### Return type

[**GetInboxHeatmap200Response**](GetInboxHeatmap200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Heatmap buckets |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |

## getInboxHeatmapWithHttpInfo

> ApiResponse<GetInboxHeatmap200Response> getInboxHeatmap getInboxHeatmapWithHttpInfo(fromDate, toDate, profileId, platform, accountId, source, action)

Get inbox day-of-week × hour-of-day heatmap

Day-of-week × hour-of-day breakdown of inbox messages. Buckets are sparse — only cells with at least one event are returned; clients zero-fill the rest to render the full 7×24 grid. The &#x60;dow&#x60; field follows ClickHouse&#39;s &#x60;toDayOfWeek&#x60; convention (1 &#x3D; Monday … 7 &#x3D; Sunday). Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String source = "source_example"; // String | 
        String action = "message.received"; // String | Narrow to a single event type. \"all\" or omitted means no filter.
        try {
            ApiResponse<GetInboxHeatmap200Response> response = apiInstance.getInboxHeatmapWithHttpInfo(fromDate, toDate, profileId, platform, accountId, source, action);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxHeatmap");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **source** | **String**|  | [optional] |
| **action** | **String**| Narrow to a single event type. \&quot;all\&quot; or omitted means no filter. | [optional] [enum: message.received, message.sent, message.read, all] |

### Return type

ApiResponse<[**GetInboxHeatmap200Response**](GetInboxHeatmap200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Heatmap buckets |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |


## getInboxResponseTime

> GetInboxResponseTime200Response getInboxResponseTime(fromDate, toDate, profileId, platform, accountId)

Get inbox response-time stats

Time-to-first-response stats. Pairs each received message with the next sent message in the same conversation and reports the delta as both summary statistics and a fixed-bucket histogram suited for the analytics page&#39;s TTR chart.  &#x60;sampleSize&#x60; reflects only conversations that received AND got a reply in the window — received-but-never-answered conversations are excluded. Compare against /v1/analytics/inbox/volume&#39;s &#x60;summary.received&#x60; to compute reply rate.  Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            GetInboxResponseTime200Response result = apiInstance.getInboxResponseTime(fromDate, toDate, profileId, platform, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxResponseTime");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |

### Return type

[**GetInboxResponseTime200Response**](GetInboxResponseTime200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response-time summary + histogram |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |

## getInboxResponseTimeWithHttpInfo

> ApiResponse<GetInboxResponseTime200Response> getInboxResponseTime getInboxResponseTimeWithHttpInfo(fromDate, toDate, profileId, platform, accountId)

Get inbox response-time stats

Time-to-first-response stats. Pairs each received message with the next sent message in the same conversation and reports the delta as both summary statistics and a fixed-bucket histogram suited for the analytics page&#39;s TTR chart.  &#x60;sampleSize&#x60; reflects only conversations that received AND got a reply in the window — received-but-never-answered conversations are excluded. Compare against /v1/analytics/inbox/volume&#39;s &#x60;summary.received&#x60; to compute reply rate.  Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetInboxResponseTime200Response> response = apiInstance.getInboxResponseTimeWithHttpInfo(fromDate, toDate, profileId, platform, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxResponseTime");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |

### Return type

ApiResponse<[**GetInboxResponseTime200Response**](GetInboxResponseTime200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response-time summary + histogram |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |


## getInboxSourceBreakdown

> GetInboxSourceBreakdown200Response getInboxSourceBreakdown(fromDate, toDate, profileId, platform, accountId)

Get inbox source breakdown

Breakdown of inbox messages by their lineage source (the &#x60;metadata.source&#x60; field set at ingest time: human / workflow / sequence / broadcast / comment_automation / api / contact / platform). Each source row also carries a per-platform sub-split. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            GetInboxSourceBreakdown200Response result = apiInstance.getInboxSourceBreakdown(fromDate, toDate, profileId, platform, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxSourceBreakdown");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |

### Return type

[**GetInboxSourceBreakdown200Response**](GetInboxSourceBreakdown200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Source breakdown |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |

## getInboxSourceBreakdownWithHttpInfo

> ApiResponse<GetInboxSourceBreakdown200Response> getInboxSourceBreakdown getInboxSourceBreakdownWithHttpInfo(fromDate, toDate, profileId, platform, accountId)

Get inbox source breakdown

Breakdown of inbox messages by their lineage source (the &#x60;metadata.source&#x60; field set at ingest time: human / workflow / sequence / broadcast / comment_automation / api / contact / platform). Each source row also carries a per-platform sub-split. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetInboxSourceBreakdown200Response> response = apiInstance.getInboxSourceBreakdownWithHttpInfo(fromDate, toDate, profileId, platform, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxSourceBreakdown");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |

### Return type

ApiResponse<[**GetInboxSourceBreakdown200Response**](GetInboxSourceBreakdown200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Source breakdown |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |


## getInboxTopAccounts

> GetInboxTopAccounts200Response getInboxTopAccounts(fromDate, toDate, profileId, platform, source, limit)

Get top accounts by inbox volume

Leaderboard of social accounts by inbox message volume. Decorates each row with display labels from the live SocialAccount record (so the UI shows username + displayName, not just an ID). Accounts that no longer map to a SocialAccount surface as \&quot;(disconnected)\&quot; so the row stays visible. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String source = "source_example"; // String | 
        Integer limit = 10; // Integer | Cap on returned rows. Lower than the posting listing's 100 because each row triggers a SocialAccount Mongo lookup.
        try {
            GetInboxTopAccounts200Response result = apiInstance.getInboxTopAccounts(fromDate, toDate, profileId, platform, source, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxTopAccounts");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **source** | **String**|  | [optional] |
| **limit** | **Integer**| Cap on returned rows. Lower than the posting listing&#39;s 100 because each row triggers a SocialAccount Mongo lookup. | [optional] [default to 10] |

### Return type

[**GetInboxTopAccounts200Response**](GetInboxTopAccounts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top accounts leaderboard |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |

## getInboxTopAccountsWithHttpInfo

> ApiResponse<GetInboxTopAccounts200Response> getInboxTopAccounts getInboxTopAccountsWithHttpInfo(fromDate, toDate, profileId, platform, source, limit)

Get top accounts by inbox volume

Leaderboard of social accounts by inbox message volume. Decorates each row with display labels from the live SocialAccount record (so the UI shows username + displayName, not just an ID). Accounts that no longer map to a SocialAccount surface as \&quot;(disconnected)\&quot; so the row stays visible. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String source = "source_example"; // String | 
        Integer limit = 10; // Integer | Cap on returned rows. Lower than the posting listing's 100 because each row triggers a SocialAccount Mongo lookup.
        try {
            ApiResponse<GetInboxTopAccounts200Response> response = apiInstance.getInboxTopAccountsWithHttpInfo(fromDate, toDate, profileId, platform, source, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxTopAccounts");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **source** | **String**|  | [optional] |
| **limit** | **Integer**| Cap on returned rows. Lower than the posting listing&#39;s 100 because each row triggers a SocialAccount Mongo lookup. | [optional] [default to 10] |

### Return type

ApiResponse<[**GetInboxTopAccounts200Response**](GetInboxTopAccounts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top accounts leaderboard |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |


## getInboxVolume

> GetInboxVolume200Response getInboxVolume(fromDate, toDate, profileId, platform, accountId, source)

Get inbox messaging volume

Daily inbox messaging volume + breakdowns. Folds the raw messaging events into three projections so the client can render the volume chart, KPI strip, and per-platform stacked bar from a single call. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive lower bound (YYYY-MM-DD). Required.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive upper bound (YYYY-MM-DD). Defaults to today.
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | Filter by single platform (facebook, instagram, twitter, etc.).
        String accountId = "accountId_example"; // String | 
        String source = "source_example"; // String | Filter by metadata.source lineage (human, workflow, sequence, broadcast, comment_automation, api, contact, platform).
        try {
            GetInboxVolume200Response result = apiInstance.getInboxVolume(fromDate, toDate, profileId, platform, accountId, source);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxVolume");
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
| **fromDate** | **LocalDate**| Inclusive lower bound (YYYY-MM-DD). Required. | |
| **toDate** | **LocalDate**| Inclusive upper bound (YYYY-MM-DD). Defaults to today. | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**| Filter by single platform (facebook, instagram, twitter, etc.). | [optional] |
| **accountId** | **String**|  | [optional] |
| **source** | **String**| Filter by metadata.source lineage (human, workflow, sequence, broadcast, comment_automation, api, contact, platform). | [optional] |

### Return type

[**GetInboxVolume200Response**](GetInboxVolume200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume breakdown |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |

## getInboxVolumeWithHttpInfo

> ApiResponse<GetInboxVolume200Response> getInboxVolume getInboxVolumeWithHttpInfo(fromDate, toDate, profileId, platform, accountId, source)

Get inbox messaging volume

Daily inbox messaging volume + breakdowns. Folds the raw messaging events into three projections so the client can render the volume chart, KPI strip, and per-platform stacked bar from a single call. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive lower bound (YYYY-MM-DD). Required.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive upper bound (YYYY-MM-DD). Defaults to today.
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | Filter by single platform (facebook, instagram, twitter, etc.).
        String accountId = "accountId_example"; // String | 
        String source = "source_example"; // String | Filter by metadata.source lineage (human, workflow, sequence, broadcast, comment_automation, api, contact, platform).
        try {
            ApiResponse<GetInboxVolume200Response> response = apiInstance.getInboxVolumeWithHttpInfo(fromDate, toDate, profileId, platform, accountId, source);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#getInboxVolume");
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
| **fromDate** | **LocalDate**| Inclusive lower bound (YYYY-MM-DD). Required. | |
| **toDate** | **LocalDate**| Inclusive upper bound (YYYY-MM-DD). Defaults to today. | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**| Filter by single platform (facebook, instagram, twitter, etc.). | [optional] |
| **accountId** | **String**|  | [optional] |
| **source** | **String**| Filter by metadata.source lineage (human, workflow, sequence, broadcast, comment_automation, api, contact, platform). | [optional] |

### Return type

ApiResponse<[**GetInboxVolume200Response**](GetInboxVolume200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume breakdown |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |


## listInboxConversationAnalytics

> ListInboxConversationAnalytics200Response listInboxConversationAnalytics(fromDate, toDate, profileId, platform, accountId, source, limit, page, sortBy, order)

List conversations with inbox analytics

Per-conversation listing with per-row totals + first/last message timestamps. The inbox analog of GET /v1/analytics (posts listing) — same filter shape, same pagination, same sort/order semantics. Use as the entry point for the per-conversation analytics drawer at /v1/analytics/inbox/conversations/{conversationId}.  Rows are enriched with the conversation&#39;s participant info (&#x60;participantName&#x60;, &#x60;participantUsername&#x60;, &#x60;participantPicture&#x60;) and last-message preview by joining the Conversation document scoped to the caller&#39;s team. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String source = "source_example"; // String | 
        Integer limit = 50; // Integer | 
        Integer page = 1; // Integer | 
        String sortBy = "lastMessageAt"; // String | 
        String order = "asc"; // String | 
        try {
            ListInboxConversationAnalytics200Response result = apiInstance.listInboxConversationAnalytics(fromDate, toDate, profileId, platform, accountId, source, limit, page, sortBy, order);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#listInboxConversationAnalytics");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **source** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **sortBy** | **String**|  | [optional] [default to lastMessageAt] [enum: lastMessageAt, firstMessageAt, totalMessages, received, sent, read, failed] |
| **order** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

### Return type

[**ListInboxConversationAnalytics200Response**](ListInboxConversationAnalytics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated conversation analytics list |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |

## listInboxConversationAnalyticsWithHttpInfo

> ApiResponse<ListInboxConversationAnalytics200Response> listInboxConversationAnalytics listInboxConversationAnalyticsWithHttpInfo(fromDate, toDate, profileId, platform, accountId, source, limit, page, sortBy, order)

List conversations with inbox analytics

Per-conversation listing with per-row totals + first/last message timestamps. The inbox analog of GET /v1/analytics (posts listing) — same filter shape, same pagination, same sort/order semantics. Use as the entry point for the per-conversation analytics drawer at /v1/analytics/inbox/conversations/{conversationId}.  Rows are enriched with the conversation&#39;s participant info (&#x60;participantName&#x60;, &#x60;participantUsername&#x60;, &#x60;participantPicture&#x60;) and last-message preview by joining the Conversation document scoped to the caller&#39;s team. Max date range is 365 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxAnalyticsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxAnalyticsApi apiInstance = new InboxAnalyticsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | 
        String profileId = "profileId_example"; // String | 
        String platform = "platform_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String source = "source_example"; // String | 
        Integer limit = 50; // Integer | 
        Integer page = 1; // Integer | 
        String sortBy = "lastMessageAt"; // String | 
        String order = "asc"; // String | 
        try {
            ApiResponse<ListInboxConversationAnalytics200Response> response = apiInstance.listInboxConversationAnalyticsWithHttpInfo(fromDate, toDate, profileId, platform, accountId, source, limit, page, sortBy, order);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxAnalyticsApi#listInboxConversationAnalytics");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **source** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **sortBy** | **String**|  | [optional] [default to lastMessageAt] [enum: lastMessageAt, firstMessageAt, totalMessages, received, sent, read, failed] |
| **order** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

### Return type

ApiResponse<[**ListInboxConversationAnalytics200Response**](ListInboxConversationAnalytics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated conversation analytics list |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal server error |  -  |

