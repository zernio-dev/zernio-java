# WebhooksApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebhookSettings**](WebhooksApi.md#createWebhookSettings) | **POST** /v1/webhooks/settings | Create webhook |
| [**createWebhookSettingsWithHttpInfo**](WebhooksApi.md#createWebhookSettingsWithHttpInfo) | **POST** /v1/webhooks/settings | Create webhook |
| [**deleteWebhookSettings**](WebhooksApi.md#deleteWebhookSettings) | **DELETE** /v1/webhooks/settings | Delete webhook |
| [**deleteWebhookSettingsWithHttpInfo**](WebhooksApi.md#deleteWebhookSettingsWithHttpInfo) | **DELETE** /v1/webhooks/settings | Delete webhook |
| [**getWebhookLogs**](WebhooksApi.md#getWebhookLogs) | **GET** /v1/webhooks/logs | List webhook delivery logs |
| [**getWebhookLogsWithHttpInfo**](WebhooksApi.md#getWebhookLogsWithHttpInfo) | **GET** /v1/webhooks/logs | List webhook delivery logs |
| [**getWebhookSettings**](WebhooksApi.md#getWebhookSettings) | **GET** /v1/webhooks/settings | List webhooks |
| [**getWebhookSettingsWithHttpInfo**](WebhooksApi.md#getWebhookSettingsWithHttpInfo) | **GET** /v1/webhooks/settings | List webhooks |
| [**redeliverWebhookEvent**](WebhooksApi.md#redeliverWebhookEvent) | **POST** /v1/webhooks/logs/redeliver | Redeliver a webhook event |
| [**redeliverWebhookEventWithHttpInfo**](WebhooksApi.md#redeliverWebhookEventWithHttpInfo) | **POST** /v1/webhooks/logs/redeliver | Redeliver a webhook event |
| [**testWebhook**](WebhooksApi.md#testWebhook) | **POST** /v1/webhooks/test | Send test webhook |
| [**testWebhookWithHttpInfo**](WebhooksApi.md#testWebhookWithHttpInfo) | **POST** /v1/webhooks/test | Send test webhook |
| [**updateWebhookSettings**](WebhooksApi.md#updateWebhookSettings) | **PUT** /v1/webhooks/settings | Update webhook |
| [**updateWebhookSettingsWithHttpInfo**](WebhooksApi.md#updateWebhookSettingsWithHttpInfo) | **PUT** /v1/webhooks/settings | Update webhook |



## createWebhookSettings

> UpdateWebhookSettings200Response createWebhookSettings(createWebhookSettingsRequest)

Create webhook

Create a new webhook configuration. Maximum 50 webhooks per user.  &#x60;name&#x60;, &#x60;url&#x60; and &#x60;events&#x60; are required. &#x60;url&#x60; must be a valid URL and &#x60;events&#x60; must contain at least one event. Whitespace is trimmed from &#x60;url&#x60; before validation.  Webhooks are automatically disabled after 10 consecutive delivery failures.  A restricted (zrk_) API key can only subscribe to events whose resource group the key holds; an event outside the key&#39;s groups is rejected with 403, so a restricted key can never create a subscription broader than itself.  &#x60;disabledResourceGroups&#x60; restricts the subscription itself, independently of which key or session later reads it. Events in a disabled group are dropped before delivery to this endpoint, on live delivery and on every replay path (test fire, redelivery, dead-letter requeue), even if they are listed in &#x60;events&#x60;. Omit it to receive everything in &#x60;events&#x60;, which is how existing subscriptions behave. A restricted key&#39;s own disabled groups are always unioned in. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        CreateWebhookSettingsRequest createWebhookSettingsRequest = new CreateWebhookSettingsRequest(); // CreateWebhookSettingsRequest | 
        try {
            UpdateWebhookSettings200Response result = apiInstance.createWebhookSettings(createWebhookSettingsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#createWebhookSettings");
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
| **createWebhookSettingsRequest** | [**CreateWebhookSettingsRequest**](CreateWebhookSettingsRequest.md)|  | |

### Return type

[**UpdateWebhookSettings200Response**](UpdateWebhookSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook created successfully |  -  |
| **400** | Validation error or maximum webhooks reached |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## createWebhookSettingsWithHttpInfo

> ApiResponse<UpdateWebhookSettings200Response> createWebhookSettings createWebhookSettingsWithHttpInfo(createWebhookSettingsRequest)

Create webhook

Create a new webhook configuration. Maximum 50 webhooks per user.  &#x60;name&#x60;, &#x60;url&#x60; and &#x60;events&#x60; are required. &#x60;url&#x60; must be a valid URL and &#x60;events&#x60; must contain at least one event. Whitespace is trimmed from &#x60;url&#x60; before validation.  Webhooks are automatically disabled after 10 consecutive delivery failures.  A restricted (zrk_) API key can only subscribe to events whose resource group the key holds; an event outside the key&#39;s groups is rejected with 403, so a restricted key can never create a subscription broader than itself.  &#x60;disabledResourceGroups&#x60; restricts the subscription itself, independently of which key or session later reads it. Events in a disabled group are dropped before delivery to this endpoint, on live delivery and on every replay path (test fire, redelivery, dead-letter requeue), even if they are listed in &#x60;events&#x60;. Omit it to receive everything in &#x60;events&#x60;, which is how existing subscriptions behave. A restricted key&#39;s own disabled groups are always unioned in. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        CreateWebhookSettingsRequest createWebhookSettingsRequest = new CreateWebhookSettingsRequest(); // CreateWebhookSettingsRequest | 
        try {
            ApiResponse<UpdateWebhookSettings200Response> response = apiInstance.createWebhookSettingsWithHttpInfo(createWebhookSettingsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#createWebhookSettings");
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
| **createWebhookSettingsRequest** | [**CreateWebhookSettingsRequest**](CreateWebhookSettingsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateWebhookSettings200Response**](UpdateWebhookSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook created successfully |  -  |
| **400** | Validation error or maximum webhooks reached |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## deleteWebhookSettings

> UpdateYoutubeDefaultPlaylist200Response deleteWebhookSettings(id)

Delete webhook

Permanently delete a webhook configuration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        String id = "id_example"; // String | Webhook ID to delete
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteWebhookSettings(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#deleteWebhookSettings");
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
| **id** | **String**| Webhook ID to delete | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook deleted successfully |  -  |
| **400** | Webhook ID missing or not a valid ID |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## deleteWebhookSettingsWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteWebhookSettings deleteWebhookSettingsWithHttpInfo(id)

Delete webhook

Permanently delete a webhook configuration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        String id = "id_example"; // String | Webhook ID to delete
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteWebhookSettingsWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#deleteWebhookSettings");
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
| **id** | **String**| Webhook ID to delete | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook deleted successfully |  -  |
| **400** | Webhook ID missing or not a valid ID |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## getWebhookLogs

> GetWebhookLogs200Response getWebhookLogs(limit, skip, status, event, webhookId, eventId)

List webhook delivery logs

Retrieve recorded webhook delivery attempts for the authenticated user, most recent first. Logs are retained for 30 days. Supports filtering by status, event type, webhook ID, and event ID, plus offset-based pagination.  For a restricted (zrk_) API key, rows for events outside the key&#39;s resource groups are omitted (&#x60;pagination.total&#x60; may over-count), and an &#x60;event&#x60; filter naming such an event is rejected with 403. Events blocked by a subscription&#39;s own &#x60;disabledResourceGroups&#x60; are dropped before delivery, so they produce no log rows for anyone; the exception is the five-minute tail after a denylist change, where an already-queued event can still be delivered and logged. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        Integer limit = 50; // Integer | Maximum number of logs to return
        Integer skip = 0; // Integer | Number of logs to skip (offset-based pagination)
        String status = "success"; // String | Filter by delivery outcome
        String event = "event_example"; // String | Filter by event type (e.g. post.published)
        String webhookId = "webhookId_example"; // String | Filter by webhook configuration ID
        String eventId = "eventId_example"; // String | Filter by stable webhook event ID
        try {
            GetWebhookLogs200Response result = apiInstance.getWebhookLogs(limit, skip, status, event, webhookId, eventId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#getWebhookLogs");
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
| **limit** | **Integer**| Maximum number of logs to return | [optional] [default to 50] |
| **skip** | **Integer**| Number of logs to skip (offset-based pagination) | [optional] [default to 0] |
| **status** | **String**| Filter by delivery outcome | [optional] [enum: success, failed] |
| **event** | **String**| Filter by event type (e.g. post.published) | [optional] |
| **webhookId** | **String**| Filter by webhook configuration ID | [optional] |
| **eventId** | **String**| Filter by stable webhook event ID | [optional] |

### Return type

[**GetWebhookLogs200Response**](GetWebhookLogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook logs retrieved successfully |  -  |
| **400** | Invalid query parameter |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## getWebhookLogsWithHttpInfo

> ApiResponse<GetWebhookLogs200Response> getWebhookLogs getWebhookLogsWithHttpInfo(limit, skip, status, event, webhookId, eventId)

List webhook delivery logs

Retrieve recorded webhook delivery attempts for the authenticated user, most recent first. Logs are retained for 30 days. Supports filtering by status, event type, webhook ID, and event ID, plus offset-based pagination.  For a restricted (zrk_) API key, rows for events outside the key&#39;s resource groups are omitted (&#x60;pagination.total&#x60; may over-count), and an &#x60;event&#x60; filter naming such an event is rejected with 403. Events blocked by a subscription&#39;s own &#x60;disabledResourceGroups&#x60; are dropped before delivery, so they produce no log rows for anyone; the exception is the five-minute tail after a denylist change, where an already-queued event can still be delivered and logged. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        Integer limit = 50; // Integer | Maximum number of logs to return
        Integer skip = 0; // Integer | Number of logs to skip (offset-based pagination)
        String status = "success"; // String | Filter by delivery outcome
        String event = "event_example"; // String | Filter by event type (e.g. post.published)
        String webhookId = "webhookId_example"; // String | Filter by webhook configuration ID
        String eventId = "eventId_example"; // String | Filter by stable webhook event ID
        try {
            ApiResponse<GetWebhookLogs200Response> response = apiInstance.getWebhookLogsWithHttpInfo(limit, skip, status, event, webhookId, eventId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#getWebhookLogs");
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
| **limit** | **Integer**| Maximum number of logs to return | [optional] [default to 50] |
| **skip** | **Integer**| Number of logs to skip (offset-based pagination) | [optional] [default to 0] |
| **status** | **String**| Filter by delivery outcome | [optional] [enum: success, failed] |
| **event** | **String**| Filter by event type (e.g. post.published) | [optional] |
| **webhookId** | **String**| Filter by webhook configuration ID | [optional] |
| **eventId** | **String**| Filter by stable webhook event ID | [optional] |

### Return type

ApiResponse<[**GetWebhookLogs200Response**](GetWebhookLogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook logs retrieved successfully |  -  |
| **400** | Invalid query parameter |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## getWebhookSettings

> GetWebhookSettings200Response getWebhookSettings()

List webhooks

Retrieve all configured webhooks for the authenticated user. Supports up to 50 webhooks per user.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        try {
            GetWebhookSettings200Response result = apiInstance.getWebhookSettings();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#getWebhookSettings");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetWebhookSettings200Response**](GetWebhookSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhooks retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## getWebhookSettingsWithHttpInfo

> ApiResponse<GetWebhookSettings200Response> getWebhookSettings getWebhookSettingsWithHttpInfo()

List webhooks

Retrieve all configured webhooks for the authenticated user. Supports up to 50 webhooks per user.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        try {
            ApiResponse<GetWebhookSettings200Response> response = apiInstance.getWebhookSettingsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#getWebhookSettings");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

ApiResponse<[**GetWebhookSettings200Response**](GetWebhookSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhooks retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## redeliverWebhookEvent

> UnpublishPost200Response redeliverWebhookEvent(redeliverWebhookEventRequest)

Redeliver a webhook event

Replay a past delivery: the original payload is re-sent, byte for byte, to the subscription&#39;s current URL. The original event ID is preserved so your endpoint can dedupe, and the replay is recorded as a fresh attempt, so it shows up in &#x60;GET /v1/webhooks/logs&#x60; next to the delivery it replays.  Both &#x60;webhookId&#x60; and &#x60;eventId&#x60; come from a row of &#x60;GET /v1/webhooks/logs&#x60;. Because the stored payload is replayed as-is, a redelivery reflects the event as it was emitted, not the current state of the resource.  Only deliveries inside the 30-day log retention window can be replayed; past that the payload is gone and the request fails with a 500. Replays run the same resource-group checks as live delivery, against both the key&#39;s groups and the subscription&#39;s &#x60;disabledResourceGroups&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        RedeliverWebhookEventRequest redeliverWebhookEventRequest = new RedeliverWebhookEventRequest(); // RedeliverWebhookEventRequest | 
        try {
            UnpublishPost200Response result = apiInstance.redeliverWebhookEvent(redeliverWebhookEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#redeliverWebhookEvent");
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
| **redeliverWebhookEventRequest** | [**RedeliverWebhookEventRequest**](RedeliverWebhookEventRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event re-delivered successfully |  -  |
| **400** | webhookId or eventId missing or empty |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **500** | Webhook no longer exists, has no URL configured, or the original payload is outside the 30-day retention window |  -  |
| **502** | Re-delivery was attempted but your endpoint errored again. The attempt is still logged; &#x60;message&#x60; describes the failure.  |  -  |

## redeliverWebhookEventWithHttpInfo

> ApiResponse<UnpublishPost200Response> redeliverWebhookEvent redeliverWebhookEventWithHttpInfo(redeliverWebhookEventRequest)

Redeliver a webhook event

Replay a past delivery: the original payload is re-sent, byte for byte, to the subscription&#39;s current URL. The original event ID is preserved so your endpoint can dedupe, and the replay is recorded as a fresh attempt, so it shows up in &#x60;GET /v1/webhooks/logs&#x60; next to the delivery it replays.  Both &#x60;webhookId&#x60; and &#x60;eventId&#x60; come from a row of &#x60;GET /v1/webhooks/logs&#x60;. Because the stored payload is replayed as-is, a redelivery reflects the event as it was emitted, not the current state of the resource.  Only deliveries inside the 30-day log retention window can be replayed; past that the payload is gone and the request fails with a 500. Replays run the same resource-group checks as live delivery, against both the key&#39;s groups and the subscription&#39;s &#x60;disabledResourceGroups&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        RedeliverWebhookEventRequest redeliverWebhookEventRequest = new RedeliverWebhookEventRequest(); // RedeliverWebhookEventRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.redeliverWebhookEventWithHttpInfo(redeliverWebhookEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#redeliverWebhookEvent");
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
| **redeliverWebhookEventRequest** | [**RedeliverWebhookEventRequest**](RedeliverWebhookEventRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event re-delivered successfully |  -  |
| **400** | webhookId or eventId missing or empty |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **500** | Webhook no longer exists, has no URL configured, or the original payload is outside the 30-day retention window |  -  |
| **502** | Re-delivery was attempted but your endpoint errored again. The attempt is still logged; &#x60;message&#x60; describes the failure.  |  -  |


## testWebhook

> UnpublishPost200Response testWebhook(testWebhookRequest)

Send test webhook

Send a test webhook to verify your endpoint is configured correctly. The test payload includes event: \&quot;webhook.test\&quot; to distinguish it from real events.  &#x60;webhook.test&#x60; belongs to the &#x60;webhooks&#x60; resource group, so a key with that group disabled is rejected with 403, as is a test fire on a subscription that lists &#x60;webhooks&#x60; in its own &#x60;disabledResourceGroups&#x60; (a 403, not a reported delivery failure). Replays of real events (redelivery, dead-letter requeue) run the same checks as live delivery, against both the key&#39;s groups and the subscription&#39;s. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        TestWebhookRequest testWebhookRequest = new TestWebhookRequest(); // TestWebhookRequest | 
        try {
            UnpublishPost200Response result = apiInstance.testWebhook(testWebhookRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#testWebhook");
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
| **testWebhookRequest** | [**TestWebhookRequest**](TestWebhookRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test webhook sent successfully |  -  |
| **400** | Webhook ID required |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Webhook not found |  -  |
| **500** | Test webhook failed to deliver |  -  |

## testWebhookWithHttpInfo

> ApiResponse<UnpublishPost200Response> testWebhook testWebhookWithHttpInfo(testWebhookRequest)

Send test webhook

Send a test webhook to verify your endpoint is configured correctly. The test payload includes event: \&quot;webhook.test\&quot; to distinguish it from real events.  &#x60;webhook.test&#x60; belongs to the &#x60;webhooks&#x60; resource group, so a key with that group disabled is rejected with 403, as is a test fire on a subscription that lists &#x60;webhooks&#x60; in its own &#x60;disabledResourceGroups&#x60; (a 403, not a reported delivery failure). Replays of real events (redelivery, dead-letter requeue) run the same checks as live delivery, against both the key&#39;s groups and the subscription&#39;s. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        TestWebhookRequest testWebhookRequest = new TestWebhookRequest(); // TestWebhookRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.testWebhookWithHttpInfo(testWebhookRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#testWebhook");
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
| **testWebhookRequest** | [**TestWebhookRequest**](TestWebhookRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test webhook sent successfully |  -  |
| **400** | Webhook ID required |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Webhook not found |  -  |
| **500** | Test webhook failed to deliver |  -  |


## updateWebhookSettings

> UpdateWebhookSettings200Response updateWebhookSettings(updateWebhookSettingsRequest)

Update webhook

Update an existing webhook configuration. All fields except &#x60;_id&#x60; are optional; only provided fields will be updated.  When provided, &#x60;name&#x60; must be 1-50 characters, &#x60;url&#x60; must be a valid URL, and &#x60;events&#x60; must contain at least one event. Whitespace is trimmed from &#x60;url&#x60; before validation.  Webhooks are automatically disabled after 10 consecutive delivery failures.  A restricted (zrk_) API key can only set &#x60;events&#x60; to events whose resource group the key holds; an event outside the key&#39;s groups is rejected with 403. It also cannot widen an existing subscription past its own groups.  &#x60;disabledResourceGroups&#x60; replaces the subscription&#39;s own denylist, which applies to delivery regardless of which key or session created it. Send an empty array to clear it. A restricted key&#39;s own disabled groups are unioned into the stored value on every update, so repointing a legacy unrestricted subscription with a restricted key also narrows it.  Timing: the new denylist applies to every event emitted after the update. Events already queued for delivery when the update landed were filtered against the previous denylist and can still arrive at your endpoint for up to five minutes after they were enqueued, because the delivery worker trusts a five-minute enqueue-time snapshot before re-checking the subscription. Retries beyond that window, dead-letter replays, test fires, and redeliveries are all checked against the current denylist. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UpdateWebhookSettingsRequest updateWebhookSettingsRequest = new UpdateWebhookSettingsRequest(); // UpdateWebhookSettingsRequest | 
        try {
            UpdateWebhookSettings200Response result = apiInstance.updateWebhookSettings(updateWebhookSettingsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#updateWebhookSettings");
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
| **updateWebhookSettingsRequest** | [**UpdateWebhookSettingsRequest**](UpdateWebhookSettingsRequest.md)|  | |

### Return type

[**UpdateWebhookSettings200Response**](UpdateWebhookSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook updated successfully |  -  |
| **400** | Validation error or missing webhook ID |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Webhook not found |  -  |

## updateWebhookSettingsWithHttpInfo

> ApiResponse<UpdateWebhookSettings200Response> updateWebhookSettings updateWebhookSettingsWithHttpInfo(updateWebhookSettingsRequest)

Update webhook

Update an existing webhook configuration. All fields except &#x60;_id&#x60; are optional; only provided fields will be updated.  When provided, &#x60;name&#x60; must be 1-50 characters, &#x60;url&#x60; must be a valid URL, and &#x60;events&#x60; must contain at least one event. Whitespace is trimmed from &#x60;url&#x60; before validation.  Webhooks are automatically disabled after 10 consecutive delivery failures.  A restricted (zrk_) API key can only set &#x60;events&#x60; to events whose resource group the key holds; an event outside the key&#39;s groups is rejected with 403. It also cannot widen an existing subscription past its own groups.  &#x60;disabledResourceGroups&#x60; replaces the subscription&#39;s own denylist, which applies to delivery regardless of which key or session created it. Send an empty array to clear it. A restricted key&#39;s own disabled groups are unioned into the stored value on every update, so repointing a legacy unrestricted subscription with a restricted key also narrows it.  Timing: the new denylist applies to every event emitted after the update. Events already queued for delivery when the update landed were filtered against the previous denylist and can still arrive at your endpoint for up to five minutes after they were enqueued, because the delivery worker trusts a five-minute enqueue-time snapshot before re-checking the subscription. Retries beyond that window, dead-letter replays, test fires, and redeliveries are all checked against the current denylist. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhooksApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhooksApi apiInstance = new WebhooksApi(defaultClient);
        UpdateWebhookSettingsRequest updateWebhookSettingsRequest = new UpdateWebhookSettingsRequest(); // UpdateWebhookSettingsRequest | 
        try {
            ApiResponse<UpdateWebhookSettings200Response> response = apiInstance.updateWebhookSettingsWithHttpInfo(updateWebhookSettingsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhooksApi#updateWebhookSettings");
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
| **updateWebhookSettingsRequest** | [**UpdateWebhookSettingsRequest**](UpdateWebhookSettingsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateWebhookSettings200Response**](UpdateWebhookSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook updated successfully |  -  |
| **400** | Validation error or missing webhook ID |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Webhook not found |  -  |

