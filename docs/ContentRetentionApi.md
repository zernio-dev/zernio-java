# ContentRetentionApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getContentRetention**](ContentRetentionApi.md#getContentRetention) | **GET** /v1/content-retention | Get content retention mode |
| [**getContentRetentionWithHttpInfo**](ContentRetentionApi.md#getContentRetentionWithHttpInfo) | **GET** /v1/content-retention | Get content retention mode |
| [**updateContentRetention**](ContentRetentionApi.md#updateContentRetention) | **PUT** /v1/content-retention | Turn zero content retention on or off |
| [**updateContentRetentionWithHttpInfo**](ContentRetentionApi.md#updateContentRetentionWithHttpInfo) | **PUT** /v1/content-retention | Turn zero content retention on or off |



## getContentRetention

> ContentRetentionResponse getContentRetention()

Get content retention mode

Returns whether your team stores content. &#x60;none&#x60; is zero content retention: Zernio keeps identifiers and metadata only, and content fields come back as &#x60;null&#x60; with &#x60;contentNotRetained: true&#x60;. See the zero content retention guide for what changes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContentRetentionApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContentRetentionApi apiInstance = new ContentRetentionApi(defaultClient);
        try {
            ContentRetentionResponse result = apiInstance.getContentRetention();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContentRetentionApi#getContentRetention");
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

[**ContentRetentionResponse**](ContentRetentionResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The team&#39;s content retention mode |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

## getContentRetentionWithHttpInfo

> ApiResponse<ContentRetentionResponse> getContentRetention getContentRetentionWithHttpInfo()

Get content retention mode

Returns whether your team stores content. &#x60;none&#x60; is zero content retention: Zernio keeps identifiers and metadata only, and content fields come back as &#x60;null&#x60; with &#x60;contentNotRetained: true&#x60;. See the zero content retention guide for what changes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContentRetentionApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContentRetentionApi apiInstance = new ContentRetentionApi(defaultClient);
        try {
            ApiResponse<ContentRetentionResponse> response = apiInstance.getContentRetentionWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContentRetentionApi#getContentRetention");
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

ApiResponse<[**ContentRetentionResponse**](ContentRetentionResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The team&#39;s content retention mode |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |


## updateContentRetention

> ContentRetentionResponse updateContentRetention(updateContentRetentionRequest)

Turn zero content retention on or off

Sets your team&#39;s content retention mode for every member. Only the team owner can change it, with a signed-in session or a full-access API key.  - &#x60;none&#x60; turns on zero content retention: from then on Zernio stores no message text, comments, lead answers, mentions, post text after publishing, call transcripts or recordings. Webhooks become the only copy, so store each event when it arrives. - &#x60;standard&#x60; stores content again for new data. Content that was not stored cannot come back. - The change applies to new data within about 5 minutes. Content stored before it stays until it is deleted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContentRetentionApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContentRetentionApi apiInstance = new ContentRetentionApi(defaultClient);
        UpdateContentRetentionRequest updateContentRetentionRequest = new UpdateContentRetentionRequest(); // UpdateContentRetentionRequest | 
        try {
            ContentRetentionResponse result = apiInstance.updateContentRetention(updateContentRetentionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContentRetentionApi#updateContentRetention");
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
| **updateContentRetentionRequest** | [**UpdateContentRetentionRequest**](UpdateContentRetentionRequest.md)|  | |

### Return type

[**ContentRetentionResponse**](ContentRetentionResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The mode now set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Only the team owner can change the mode, on a signed-in session or a full-access API key (&#x60;insufficient_permissions&#x60;). Read-only, profile-scoped and restricted API keys and third-party OAuth tokens get 403 too. |  -  |
| **409** | Invalid resource state (&#x60;invalid_resource_state&#x60;): a Zernio phone number of the team has a WhatsApp verification in progress. Teams with zero content retention cannot receive the verification code, so finish or cancel it first. |  -  |

## updateContentRetentionWithHttpInfo

> ApiResponse<ContentRetentionResponse> updateContentRetention updateContentRetentionWithHttpInfo(updateContentRetentionRequest)

Turn zero content retention on or off

Sets your team&#39;s content retention mode for every member. Only the team owner can change it, with a signed-in session or a full-access API key.  - &#x60;none&#x60; turns on zero content retention: from then on Zernio stores no message text, comments, lead answers, mentions, post text after publishing, call transcripts or recordings. Webhooks become the only copy, so store each event when it arrives. - &#x60;standard&#x60; stores content again for new data. Content that was not stored cannot come back. - The change applies to new data within about 5 minutes. Content stored before it stays until it is deleted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContentRetentionApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContentRetentionApi apiInstance = new ContentRetentionApi(defaultClient);
        UpdateContentRetentionRequest updateContentRetentionRequest = new UpdateContentRetentionRequest(); // UpdateContentRetentionRequest | 
        try {
            ApiResponse<ContentRetentionResponse> response = apiInstance.updateContentRetentionWithHttpInfo(updateContentRetentionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContentRetentionApi#updateContentRetention");
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
| **updateContentRetentionRequest** | [**UpdateContentRetentionRequest**](UpdateContentRetentionRequest.md)|  | |

### Return type

ApiResponse<[**ContentRetentionResponse**](ContentRetentionResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The mode now set |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Only the team owner can change the mode, on a signed-in session or a full-access API key (&#x60;insufficient_permissions&#x60;). Read-only, profile-scoped and restricted API keys and third-party OAuth tokens get 403 too. |  -  |
| **409** | Invalid resource state (&#x60;invalid_resource_state&#x60;): a Zernio phone number of the team has a WhatsApp verification in progress. Teams with zero content retention cannot receive the verification code, so finish or cancel it first. |  -  |

