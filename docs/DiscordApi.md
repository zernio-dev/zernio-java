# DiscordApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDiscordChannels**](DiscordApi.md#getDiscordChannels) | **GET** /v1/accounts/{accountId}/discord-channels | List Discord guild channels |
| [**getDiscordChannelsWithHttpInfo**](DiscordApi.md#getDiscordChannelsWithHttpInfo) | **GET** /v1/accounts/{accountId}/discord-channels | List Discord guild channels |
| [**getDiscordSettings**](DiscordApi.md#getDiscordSettings) | **GET** /v1/accounts/{accountId}/discord-settings | Get Discord account settings |
| [**getDiscordSettingsWithHttpInfo**](DiscordApi.md#getDiscordSettingsWithHttpInfo) | **GET** /v1/accounts/{accountId}/discord-settings | Get Discord account settings |
| [**updateDiscordSettings**](DiscordApi.md#updateDiscordSettings) | **PATCH** /v1/accounts/{accountId}/discord-settings | Update Discord settings |
| [**updateDiscordSettingsWithHttpInfo**](DiscordApi.md#updateDiscordSettingsWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/discord-settings | Update Discord settings |



## getDiscordChannels

> GetDiscordChannels200Response getDiscordChannels(accountId)

List Discord guild channels

Returns the text, announcement, and forum channels in the connected Discord guild. Use this to discover available channels when switching the connected channel via PATCH /v1/accounts/{accountId}/discord-settings.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetDiscordChannels200Response result = apiInstance.getDiscordChannels(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordChannels");
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

### Return type

[**GetDiscordChannels200Response**](GetDiscordChannels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel list |  -  |
| **400** | Not a Discord account or missing guild info |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getDiscordChannelsWithHttpInfo

> ApiResponse<GetDiscordChannels200Response> getDiscordChannels getDiscordChannelsWithHttpInfo(accountId)

List Discord guild channels

Returns the text, announcement, and forum channels in the connected Discord guild. Use this to discover available channels when switching the connected channel via PATCH /v1/accounts/{accountId}/discord-settings.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetDiscordChannels200Response> response = apiInstance.getDiscordChannelsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordChannels");
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

### Return type

ApiResponse<[**GetDiscordChannels200Response**](GetDiscordChannels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel list |  -  |
| **400** | Not a Discord account or missing guild info |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getDiscordSettings

> GetDiscordSettings200Response getDiscordSettings(accountId)

Get Discord account settings

Returns the current Discord account settings including webhook identity (display name and avatar), connected channel, and guild information.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetDiscordSettings200Response result = apiInstance.getDiscordSettings(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordSettings");
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

### Return type

[**GetDiscordSettings200Response**](GetDiscordSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discord account settings |  -  |
| **400** | Not a Discord account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## getDiscordSettingsWithHttpInfo

> ApiResponse<GetDiscordSettings200Response> getDiscordSettings getDiscordSettingsWithHttpInfo(accountId)

Get Discord account settings

Returns the current Discord account settings including webhook identity (display name and avatar), connected channel, and guild information.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetDiscordSettings200Response> response = apiInstance.getDiscordSettingsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#getDiscordSettings");
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

### Return type

ApiResponse<[**GetDiscordSettings200Response**](GetDiscordSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Discord account settings |  -  |
| **400** | Not a Discord account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## updateDiscordSettings

> UpdateDiscordSettings200Response updateDiscordSettings(accountId, updateDiscordSettingsRequest)

Update Discord settings

Update Discord account settings. Supports two operations (can be combined):  1. **Webhook identity** - Set the default display name and avatar that appear as the message author on every post. These are account-level defaults; individual posts can override them via platformSpecificData.webhookUsername / webhookAvatarUrl.  2. **Switch channel** - Move the connection to a different channel in the same guild. A new webhook is automatically created in the target channel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateDiscordSettingsRequest updateDiscordSettingsRequest = new UpdateDiscordSettingsRequest(); // UpdateDiscordSettingsRequest | 
        try {
            UpdateDiscordSettings200Response result = apiInstance.updateDiscordSettings(accountId, updateDiscordSettingsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#updateDiscordSettings");
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
| **updateDiscordSettingsRequest** | [**UpdateDiscordSettingsRequest**](UpdateDiscordSettingsRequest.md)|  | |

### Return type

[**UpdateDiscordSettings200Response**](UpdateDiscordSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings updated |  -  |
| **400** | Invalid request (no changes |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found |  -  |

## updateDiscordSettingsWithHttpInfo

> ApiResponse<UpdateDiscordSettings200Response> updateDiscordSettings updateDiscordSettingsWithHttpInfo(accountId, updateDiscordSettingsRequest)

Update Discord settings

Update Discord account settings. Supports two operations (can be combined):  1. **Webhook identity** - Set the default display name and avatar that appear as the message author on every post. These are account-level defaults; individual posts can override them via platformSpecificData.webhookUsername / webhookAvatarUrl.  2. **Switch channel** - Move the connection to a different channel in the same guild. A new webhook is automatically created in the target channel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.DiscordApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        DiscordApi apiInstance = new DiscordApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateDiscordSettingsRequest updateDiscordSettingsRequest = new UpdateDiscordSettingsRequest(); // UpdateDiscordSettingsRequest | 
        try {
            ApiResponse<UpdateDiscordSettings200Response> response = apiInstance.updateDiscordSettingsWithHttpInfo(accountId, updateDiscordSettingsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling DiscordApi#updateDiscordSettings");
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
| **updateDiscordSettingsRequest** | [**UpdateDiscordSettingsRequest**](UpdateDiscordSettingsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateDiscordSettings200Response**](UpdateDiscordSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings updated |  -  |
| **400** | Invalid request (no changes |  -  |
| **401** | Unauthorized |  -  |
| **404** | Discord account not found |  -  |

