# LogsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listLogs**](LogsApi.md#listLogs) | **GET** /v1/logs | List activity logs |
| [**listLogsWithHttpInfo**](LogsApi.md#listLogsWithHttpInfo) | **GET** /v1/logs | List activity logs |



## listLogs

> ListLogs200Response listLogs(type, status, platform, action, search, days, limit, skip, accountId, accountId2, event, requestId, requestId2, from, to, statusCode, statusCode2, apiKeyId, apiKeyId2, includeReadReceipts, includeReadReceipts2)

List activity logs

Unified logs endpoint. Returns logs for publishing, connections, webhooks, and messaging. Filter by type, platform, status, and time range. Logs are retained for 90 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String type = "all"; // String | Log category to query. Use `all` for the unified view across every category, or `api_request` for your API request logs (method, path, status, latency). 
        String status = "success"; // String | Filter by status
        String platform = "tiktok"; // String | Filter by platform
        String action = "action_example"; // String | Filter by action (e.g., post.published, message.sent, account.connected, webhook.delivered)
        String search = "search_example"; // String | Free-text search across log fields
        Integer days = 90; // Integer | Number of days to look back (max 90)
        Integer limit = 50; // Integer | Maximum number of logs to return (max 100)
        Integer skip = 0; // Integer | Number of logs to skip (for pagination)
        String accountId = "accountId_example"; // String | Filter by connected account ID
        String accountId2 = "accountId_example"; // String | Alias of accountId, kept for existing callers
        String event = "event_example"; // String | Filter webhook logs by event (e.g. post.published, message.received)
        String requestId = "requestId_example"; // String | Correlation ID. Returns every log spawned by a single API request
        String requestId2 = "requestId_example"; // String | Alias of requestId, kept for existing callers
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Precise start instant (ISO 8601); narrows within the day range
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Precise end instant (ISO 8601)
        Integer statusCode = 56; // Integer | Filter by exact HTTP status code (api_request logs)
        Integer statusCode2 = 56; // Integer | Alias of statusCode, kept for existing callers
        String apiKeyId = "apiKeyId_example"; // String | Filter by the API key that made the request (api_request logs)
        String apiKeyId2 = "apiKeyId_example"; // String | Alias of apiKeyId, kept for existing callers
        Boolean includeReadReceipts = false; // Boolean | Include message.read / message.delivered events (hidden by default for messaging logs)
        Boolean includeReadReceipts2 = false; // Boolean | Alias of includeReadReceipts, kept for existing callers
        try {
            ListLogs200Response result = apiInstance.listLogs(type, status, platform, action, search, days, limit, skip, accountId, accountId2, event, requestId, requestId2, from, to, statusCode, statusCode2, apiKeyId, apiKeyId2, includeReadReceipts, includeReadReceipts2);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#listLogs");
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
| **type** | **String**| Log category to query. Use &#x60;all&#x60; for the unified view across every category, or &#x60;api_request&#x60; for your API request logs (method, path, status, latency).  | [optional] [default to publishing] [enum: all, publishing, connections, webhooks, messaging, workflow_event, api_request] |
| **status** | **String**| Filter by status | [optional] [enum: success, failed, pending, skipped, all] |
| **platform** | **String**| Filter by platform | [optional] [enum: tiktok, instagram, whatsapp, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, all] |
| **action** | **String**| Filter by action (e.g., post.published, message.sent, account.connected, webhook.delivered) | [optional] |
| **search** | **String**| Free-text search across log fields | [optional] |
| **days** | **Integer**| Number of days to look back (max 90) | [optional] [default to 90] |
| **limit** | **Integer**| Maximum number of logs to return (max 100) | [optional] [default to 50] |
| **skip** | **Integer**| Number of logs to skip (for pagination) | [optional] [default to 0] |
| **accountId** | **String**| Filter by connected account ID | [optional] |
| **accountId2** | **String**| Alias of accountId, kept for existing callers | [optional] |
| **event** | **String**| Filter webhook logs by event (e.g. post.published, message.received) | [optional] |
| **requestId** | **String**| Correlation ID. Returns every log spawned by a single API request | [optional] |
| **requestId2** | **String**| Alias of requestId, kept for existing callers | [optional] |
| **from** | **OffsetDateTime**| Precise start instant (ISO 8601); narrows within the day range | [optional] |
| **to** | **OffsetDateTime**| Precise end instant (ISO 8601) | [optional] |
| **statusCode** | **Integer**| Filter by exact HTTP status code (api_request logs) | [optional] |
| **statusCode2** | **Integer**| Alias of statusCode, kept for existing callers | [optional] |
| **apiKeyId** | **String**| Filter by the API key that made the request (api_request logs) | [optional] |
| **apiKeyId2** | **String**| Alias of apiKeyId, kept for existing callers | [optional] |
| **includeReadReceipts** | **Boolean**| Include message.read / message.delivered events (hidden by default for messaging logs) | [optional] [default to false] |
| **includeReadReceipts2** | **Boolean**| Alias of includeReadReceipts, kept for existing callers | [optional] [default to false] |

### Return type

[**ListLogs200Response**](ListLogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Logs retrieved successfully |  -  |
| **400** | Invalid filter value. Unknown parameters are ignored on this list; the histogram, facets and export routes reject them. |  -  |
| **401** | Unauthorized |  -  |

## listLogsWithHttpInfo

> ApiResponse<ListLogs200Response> listLogs listLogsWithHttpInfo(type, status, platform, action, search, days, limit, skip, accountId, accountId2, event, requestId, requestId2, from, to, statusCode, statusCode2, apiKeyId, apiKeyId2, includeReadReceipts, includeReadReceipts2)

List activity logs

Unified logs endpoint. Returns logs for publishing, connections, webhooks, and messaging. Filter by type, platform, status, and time range. Logs are retained for 90 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LogsApi apiInstance = new LogsApi(defaultClient);
        String type = "all"; // String | Log category to query. Use `all` for the unified view across every category, or `api_request` for your API request logs (method, path, status, latency). 
        String status = "success"; // String | Filter by status
        String platform = "tiktok"; // String | Filter by platform
        String action = "action_example"; // String | Filter by action (e.g., post.published, message.sent, account.connected, webhook.delivered)
        String search = "search_example"; // String | Free-text search across log fields
        Integer days = 90; // Integer | Number of days to look back (max 90)
        Integer limit = 50; // Integer | Maximum number of logs to return (max 100)
        Integer skip = 0; // Integer | Number of logs to skip (for pagination)
        String accountId = "accountId_example"; // String | Filter by connected account ID
        String accountId2 = "accountId_example"; // String | Alias of accountId, kept for existing callers
        String event = "event_example"; // String | Filter webhook logs by event (e.g. post.published, message.received)
        String requestId = "requestId_example"; // String | Correlation ID. Returns every log spawned by a single API request
        String requestId2 = "requestId_example"; // String | Alias of requestId, kept for existing callers
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Precise start instant (ISO 8601); narrows within the day range
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Precise end instant (ISO 8601)
        Integer statusCode = 56; // Integer | Filter by exact HTTP status code (api_request logs)
        Integer statusCode2 = 56; // Integer | Alias of statusCode, kept for existing callers
        String apiKeyId = "apiKeyId_example"; // String | Filter by the API key that made the request (api_request logs)
        String apiKeyId2 = "apiKeyId_example"; // String | Alias of apiKeyId, kept for existing callers
        Boolean includeReadReceipts = false; // Boolean | Include message.read / message.delivered events (hidden by default for messaging logs)
        Boolean includeReadReceipts2 = false; // Boolean | Alias of includeReadReceipts, kept for existing callers
        try {
            ApiResponse<ListLogs200Response> response = apiInstance.listLogsWithHttpInfo(type, status, platform, action, search, days, limit, skip, accountId, accountId2, event, requestId, requestId2, from, to, statusCode, statusCode2, apiKeyId, apiKeyId2, includeReadReceipts, includeReadReceipts2);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LogsApi#listLogs");
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
| **type** | **String**| Log category to query. Use &#x60;all&#x60; for the unified view across every category, or &#x60;api_request&#x60; for your API request logs (method, path, status, latency).  | [optional] [default to publishing] [enum: all, publishing, connections, webhooks, messaging, workflow_event, api_request] |
| **status** | **String**| Filter by status | [optional] [enum: success, failed, pending, skipped, all] |
| **platform** | **String**| Filter by platform | [optional] [enum: tiktok, instagram, whatsapp, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, all] |
| **action** | **String**| Filter by action (e.g., post.published, message.sent, account.connected, webhook.delivered) | [optional] |
| **search** | **String**| Free-text search across log fields | [optional] |
| **days** | **Integer**| Number of days to look back (max 90) | [optional] [default to 90] |
| **limit** | **Integer**| Maximum number of logs to return (max 100) | [optional] [default to 50] |
| **skip** | **Integer**| Number of logs to skip (for pagination) | [optional] [default to 0] |
| **accountId** | **String**| Filter by connected account ID | [optional] |
| **accountId2** | **String**| Alias of accountId, kept for existing callers | [optional] |
| **event** | **String**| Filter webhook logs by event (e.g. post.published, message.received) | [optional] |
| **requestId** | **String**| Correlation ID. Returns every log spawned by a single API request | [optional] |
| **requestId2** | **String**| Alias of requestId, kept for existing callers | [optional] |
| **from** | **OffsetDateTime**| Precise start instant (ISO 8601); narrows within the day range | [optional] |
| **to** | **OffsetDateTime**| Precise end instant (ISO 8601) | [optional] |
| **statusCode** | **Integer**| Filter by exact HTTP status code (api_request logs) | [optional] |
| **statusCode2** | **Integer**| Alias of statusCode, kept for existing callers | [optional] |
| **apiKeyId** | **String**| Filter by the API key that made the request (api_request logs) | [optional] |
| **apiKeyId2** | **String**| Alias of apiKeyId, kept for existing callers | [optional] |
| **includeReadReceipts** | **Boolean**| Include message.read / message.delivered events (hidden by default for messaging logs) | [optional] [default to false] |
| **includeReadReceipts2** | **Boolean**| Alias of includeReadReceipts, kept for existing callers | [optional] [default to false] |

### Return type

ApiResponse<[**ListLogs200Response**](ListLogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Logs retrieved successfully |  -  |
| **400** | Invalid filter value. Unknown parameters are ignored on this list; the histogram, facets and export routes reject them. |  -  |
| **401** | Unauthorized |  -  |

