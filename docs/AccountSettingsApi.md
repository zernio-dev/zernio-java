# AccountSettingsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteInstagramIceBreakers**](AccountSettingsApi.md#deleteInstagramIceBreakers) | **DELETE** /v1/accounts/{accountId}/instagram-ice-breakers | Delete IG ice breakers |
| [**deleteInstagramIceBreakersWithHttpInfo**](AccountSettingsApi.md#deleteInstagramIceBreakersWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/instagram-ice-breakers | Delete IG ice breakers |
| [**deleteMessengerGetStarted**](AccountSettingsApi.md#deleteMessengerGetStarted) | **DELETE** /v1/accounts/{accountId}/messenger-get-started | Delete FB Get Started button |
| [**deleteMessengerGetStartedWithHttpInfo**](AccountSettingsApi.md#deleteMessengerGetStartedWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/messenger-get-started | Delete FB Get Started button |
| [**deleteMessengerMenu**](AccountSettingsApi.md#deleteMessengerMenu) | **DELETE** /v1/accounts/{accountId}/messenger-menu | Delete FB persistent menu |
| [**deleteMessengerMenuWithHttpInfo**](AccountSettingsApi.md#deleteMessengerMenuWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/messenger-menu | Delete FB persistent menu |
| [**deleteTelegramCommands**](AccountSettingsApi.md#deleteTelegramCommands) | **DELETE** /v1/accounts/{accountId}/telegram-commands | Delete TG bot commands |
| [**deleteTelegramCommandsWithHttpInfo**](AccountSettingsApi.md#deleteTelegramCommandsWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/telegram-commands | Delete TG bot commands |
| [**getInstagramIceBreakers**](AccountSettingsApi.md#getInstagramIceBreakers) | **GET** /v1/accounts/{accountId}/instagram-ice-breakers | Get IG ice breakers |
| [**getInstagramIceBreakersWithHttpInfo**](AccountSettingsApi.md#getInstagramIceBreakersWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram-ice-breakers | Get IG ice breakers |
| [**getMessengerGetStarted**](AccountSettingsApi.md#getMessengerGetStarted) | **GET** /v1/accounts/{accountId}/messenger-get-started | Get FB Get Started button |
| [**getMessengerGetStartedWithHttpInfo**](AccountSettingsApi.md#getMessengerGetStartedWithHttpInfo) | **GET** /v1/accounts/{accountId}/messenger-get-started | Get FB Get Started button |
| [**getMessengerMenu**](AccountSettingsApi.md#getMessengerMenu) | **GET** /v1/accounts/{accountId}/messenger-menu | Get FB persistent menu |
| [**getMessengerMenuWithHttpInfo**](AccountSettingsApi.md#getMessengerMenuWithHttpInfo) | **GET** /v1/accounts/{accountId}/messenger-menu | Get FB persistent menu |
| [**getTelegramCommands**](AccountSettingsApi.md#getTelegramCommands) | **GET** /v1/accounts/{accountId}/telegram-commands | Get TG bot commands |
| [**getTelegramCommandsWithHttpInfo**](AccountSettingsApi.md#getTelegramCommandsWithHttpInfo) | **GET** /v1/accounts/{accountId}/telegram-commands | Get TG bot commands |
| [**setInstagramIceBreakers**](AccountSettingsApi.md#setInstagramIceBreakers) | **PUT** /v1/accounts/{accountId}/instagram-ice-breakers | Set IG ice breakers |
| [**setInstagramIceBreakersWithHttpInfo**](AccountSettingsApi.md#setInstagramIceBreakersWithHttpInfo) | **PUT** /v1/accounts/{accountId}/instagram-ice-breakers | Set IG ice breakers |
| [**setMessengerGetStarted**](AccountSettingsApi.md#setMessengerGetStarted) | **PUT** /v1/accounts/{accountId}/messenger-get-started | Set FB Get Started button |
| [**setMessengerGetStartedWithHttpInfo**](AccountSettingsApi.md#setMessengerGetStartedWithHttpInfo) | **PUT** /v1/accounts/{accountId}/messenger-get-started | Set FB Get Started button |
| [**setMessengerMenu**](AccountSettingsApi.md#setMessengerMenu) | **PUT** /v1/accounts/{accountId}/messenger-menu | Set FB persistent menu |
| [**setMessengerMenuWithHttpInfo**](AccountSettingsApi.md#setMessengerMenuWithHttpInfo) | **PUT** /v1/accounts/{accountId}/messenger-menu | Set FB persistent menu |
| [**setTelegramCommands**](AccountSettingsApi.md#setTelegramCommands) | **PUT** /v1/accounts/{accountId}/telegram-commands | Set TG bot commands |
| [**setTelegramCommandsWithHttpInfo**](AccountSettingsApi.md#setTelegramCommandsWithHttpInfo) | **PUT** /v1/accounts/{accountId}/telegram-commands | Set TG bot commands |



## deleteInstagramIceBreakers

> void deleteInstagramIceBreakers(accountId)

Delete IG ice breakers

Removes the ice breaker questions from an Instagram account&#39;s Messenger experience.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            apiInstance.deleteInstagramIceBreakers(accountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteInstagramIceBreakers");
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


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ice breakers deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## deleteInstagramIceBreakersWithHttpInfo

> ApiResponse<Void> deleteInstagramIceBreakers deleteInstagramIceBreakersWithHttpInfo(accountId)

Delete IG ice breakers

Removes the ice breaker questions from an Instagram account&#39;s Messenger experience.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.deleteInstagramIceBreakersWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteInstagramIceBreakers");
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


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ice breakers deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## deleteMessengerGetStarted

> UpdateYoutubeDefaultPlaylist200Response deleteMessengerGetStarted(accountId)

Delete FB Get Started button

Remove the Get Started button. Meta refuses while a persistent menu is set, so delete the menu first.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteMessengerGetStarted(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteMessengerGetStarted");
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

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Started button deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **409** | A persistent menu is still set. Delete it with DELETE /v1/accounts/{accountId}/messenger-menu first. |  -  |

## deleteMessengerGetStartedWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteMessengerGetStarted deleteMessengerGetStartedWithHttpInfo(accountId)

Delete FB Get Started button

Remove the Get Started button. Meta refuses while a persistent menu is set, so delete the menu first.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteMessengerGetStartedWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteMessengerGetStarted");
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

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Started button deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **409** | A persistent menu is still set. Delete it with DELETE /v1/accounts/{accountId}/messenger-menu first. |  -  |


## deleteMessengerMenu

> void deleteMessengerMenu(accountId)

Delete FB persistent menu

Removes the persistent menu from Facebook Messenger conversations for this account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            apiInstance.deleteMessengerMenu(accountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteMessengerMenu");
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


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## deleteMessengerMenuWithHttpInfo

> ApiResponse<Void> deleteMessengerMenu deleteMessengerMenuWithHttpInfo(accountId)

Delete FB persistent menu

Removes the persistent menu from Facebook Messenger conversations for this account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.deleteMessengerMenuWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteMessengerMenu");
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


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## deleteTelegramCommands

> void deleteTelegramCommands(accountId)

Delete TG bot commands

Clears all bot commands configured for a Telegram bot account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            apiInstance.deleteTelegramCommands(accountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteTelegramCommands");
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


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Commands deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## deleteTelegramCommandsWithHttpInfo

> ApiResponse<Void> deleteTelegramCommands deleteTelegramCommandsWithHttpInfo(accountId)

Delete TG bot commands

Clears all bot commands configured for a Telegram bot account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.deleteTelegramCommandsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#deleteTelegramCommands");
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


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Commands deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## getInstagramIceBreakers

> GetMessengerMenu200Response getInstagramIceBreakers(accountId)

Get IG ice breakers

Get the ice breaker configuration for an Instagram account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetMessengerMenu200Response result = apiInstance.getInstagramIceBreakers(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getInstagramIceBreakers");
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

[**GetMessengerMenu200Response**](GetMessengerMenu200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ice breaker configuration |  -  |
| **400** | Not an Instagram account |  -  |
| **401** | Unauthorized |  -  |

## getInstagramIceBreakersWithHttpInfo

> ApiResponse<GetMessengerMenu200Response> getInstagramIceBreakers getInstagramIceBreakersWithHttpInfo(accountId)

Get IG ice breakers

Get the ice breaker configuration for an Instagram account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetMessengerMenu200Response> response = apiInstance.getInstagramIceBreakersWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getInstagramIceBreakers");
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

ApiResponse<[**GetMessengerMenu200Response**](GetMessengerMenu200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ice breaker configuration |  -  |
| **400** | Not an Instagram account |  -  |
| **401** | Unauthorized |  -  |


## getMessengerGetStarted

> GetMessengerGetStarted200Response getMessengerGetStarted(accountId)

Get FB Get Started button

Get the Get Started button payload for a Facebook Messenger account. &#x60;data&#x60; is null when the page has none.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetMessengerGetStarted200Response result = apiInstance.getMessengerGetStarted(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getMessengerGetStarted");
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

[**GetMessengerGetStarted200Response**](GetMessengerGetStarted200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Started button configuration |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getMessengerGetStartedWithHttpInfo

> ApiResponse<GetMessengerGetStarted200Response> getMessengerGetStarted getMessengerGetStartedWithHttpInfo(accountId)

Get FB Get Started button

Get the Get Started button payload for a Facebook Messenger account. &#x60;data&#x60; is null when the page has none.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetMessengerGetStarted200Response> response = apiInstance.getMessengerGetStartedWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getMessengerGetStarted");
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

ApiResponse<[**GetMessengerGetStarted200Response**](GetMessengerGetStarted200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Started button configuration |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getMessengerMenu

> GetMessengerMenu200Response getMessengerMenu(accountId)

Get FB persistent menu

Get the persistent menu configuration for a Facebook Messenger account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetMessengerMenu200Response result = apiInstance.getMessengerMenu(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getMessengerMenu");
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

[**GetMessengerMenu200Response**](GetMessengerMenu200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Persistent menu configuration |  -  |
| **400** | Not a Facebook account |  -  |
| **401** | Unauthorized |  -  |

## getMessengerMenuWithHttpInfo

> ApiResponse<GetMessengerMenu200Response> getMessengerMenu getMessengerMenuWithHttpInfo(accountId)

Get FB persistent menu

Get the persistent menu configuration for a Facebook Messenger account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetMessengerMenu200Response> response = apiInstance.getMessengerMenuWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getMessengerMenu");
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

ApiResponse<[**GetMessengerMenu200Response**](GetMessengerMenu200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Persistent menu configuration |  -  |
| **400** | Not a Facebook account |  -  |
| **401** | Unauthorized |  -  |


## getTelegramCommands

> GetTelegramCommands200Response getTelegramCommands(accountId)

Get TG bot commands

Get the bot commands configuration for a Telegram account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetTelegramCommands200Response result = apiInstance.getTelegramCommands(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getTelegramCommands");
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

[**GetTelegramCommands200Response**](GetTelegramCommands200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bot commands list |  -  |
| **400** | Not a Telegram account |  -  |
| **401** | Unauthorized |  -  |

## getTelegramCommandsWithHttpInfo

> ApiResponse<GetTelegramCommands200Response> getTelegramCommands getTelegramCommandsWithHttpInfo(accountId)

Get TG bot commands

Get the bot commands configuration for a Telegram account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetTelegramCommands200Response> response = apiInstance.getTelegramCommandsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#getTelegramCommands");
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

ApiResponse<[**GetTelegramCommands200Response**](GetTelegramCommands200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bot commands list |  -  |
| **400** | Not a Telegram account |  -  |
| **401** | Unauthorized |  -  |


## setInstagramIceBreakers

> void setInstagramIceBreakers(accountId, setInstagramIceBreakersRequest)

Set IG ice breakers

Set ice breakers for an Instagram account. Max 4 ice breakers, question max 80 chars.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetInstagramIceBreakersRequest setInstagramIceBreakersRequest = new SetInstagramIceBreakersRequest(); // SetInstagramIceBreakersRequest | 
        try {
            apiInstance.setInstagramIceBreakers(accountId, setInstagramIceBreakersRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setInstagramIceBreakers");
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
| **setInstagramIceBreakersRequest** | [**SetInstagramIceBreakersRequest**](SetInstagramIceBreakersRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ice breakers set successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## setInstagramIceBreakersWithHttpInfo

> ApiResponse<Void> setInstagramIceBreakers setInstagramIceBreakersWithHttpInfo(accountId, setInstagramIceBreakersRequest)

Set IG ice breakers

Set ice breakers for an Instagram account. Max 4 ice breakers, question max 80 chars.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetInstagramIceBreakersRequest setInstagramIceBreakersRequest = new SetInstagramIceBreakersRequest(); // SetInstagramIceBreakersRequest | 
        try {
            ApiResponse<Void> response = apiInstance.setInstagramIceBreakersWithHttpInfo(accountId, setInstagramIceBreakersRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setInstagramIceBreakers");
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
| **setInstagramIceBreakersRequest** | [**SetInstagramIceBreakersRequest**](SetInstagramIceBreakersRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ice breakers set successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## setMessengerGetStarted

> UpdateYoutubeDefaultPlaylist200Response setMessengerGetStarted(accountId, setMessengerGetStartedRequest)

Set FB Get Started button

Set the Get Started button shown on a Facebook page&#39;s Messenger welcome screen. Meta requires it before a persistent menu can be set. Tapping it sends a postback with &#x60;payload&#x60;, which arrives as a &#x60;message.received&#x60; webhook carrying it in &#x60;metadata.postbackPayload&#x60;. Use &#x60;zernio:workflow:&lt;workflowId&gt;&#x60; to start a workflow on the tap; the workflow must be active on this account and profile.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetMessengerGetStartedRequest setMessengerGetStartedRequest = new SetMessengerGetStartedRequest(); // SetMessengerGetStartedRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.setMessengerGetStarted(accountId, setMessengerGetStartedRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setMessengerGetStarted");
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
| **setMessengerGetStartedRequest** | [**SetMessengerGetStartedRequest**](SetMessengerGetStartedRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Started button set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## setMessengerGetStartedWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> setMessengerGetStarted setMessengerGetStartedWithHttpInfo(accountId, setMessengerGetStartedRequest)

Set FB Get Started button

Set the Get Started button shown on a Facebook page&#39;s Messenger welcome screen. Meta requires it before a persistent menu can be set. Tapping it sends a postback with &#x60;payload&#x60;, which arrives as a &#x60;message.received&#x60; webhook carrying it in &#x60;metadata.postbackPayload&#x60;. Use &#x60;zernio:workflow:&lt;workflowId&gt;&#x60; to start a workflow on the tap; the workflow must be active on this account and profile.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetMessengerGetStartedRequest setMessengerGetStartedRequest = new SetMessengerGetStartedRequest(); // SetMessengerGetStartedRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.setMessengerGetStartedWithHttpInfo(accountId, setMessengerGetStartedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setMessengerGetStarted");
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
| **setMessengerGetStartedRequest** | [**SetMessengerGetStartedRequest**](SetMessengerGetStartedRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Started button set |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## setMessengerMenu

> void setMessengerMenu(accountId, setMessengerMenuRequest)

Set FB persistent menu

Set the persistent menu for a Facebook Messenger account. Max 3 top-level items, max 5 nested items. Meta only shows a persistent menu on a page that has a Get Started button, so set one first with PUT /v1/accounts/{accountId}/messenger-get-started. A postback button whose payload is &#x60;zernio:workflow:&lt;workflowId&gt;&#x60; starts that workflow when tapped; the workflow must be active on this account and profile.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetMessengerMenuRequest setMessengerMenuRequest = new SetMessengerMenuRequest(); // SetMessengerMenuRequest | 
        try {
            apiInstance.setMessengerMenu(accountId, setMessengerMenuRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setMessengerMenu");
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
| **setMessengerMenuRequest** | [**SetMessengerMenuRequest**](SetMessengerMenuRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu set successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **409** | The page has no Get Started button. Set one with PUT /v1/accounts/{accountId}/messenger-get-started and retry. |  -  |

## setMessengerMenuWithHttpInfo

> ApiResponse<Void> setMessengerMenu setMessengerMenuWithHttpInfo(accountId, setMessengerMenuRequest)

Set FB persistent menu

Set the persistent menu for a Facebook Messenger account. Max 3 top-level items, max 5 nested items. Meta only shows a persistent menu on a page that has a Get Started button, so set one first with PUT /v1/accounts/{accountId}/messenger-get-started. A postback button whose payload is &#x60;zernio:workflow:&lt;workflowId&gt;&#x60; starts that workflow when tapped; the workflow must be active on this account and profile.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetMessengerMenuRequest setMessengerMenuRequest = new SetMessengerMenuRequest(); // SetMessengerMenuRequest | 
        try {
            ApiResponse<Void> response = apiInstance.setMessengerMenuWithHttpInfo(accountId, setMessengerMenuRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setMessengerMenu");
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
| **setMessengerMenuRequest** | [**SetMessengerMenuRequest**](SetMessengerMenuRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Menu set successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **409** | The page has no Get Started button. Set one with PUT /v1/accounts/{accountId}/messenger-get-started and retry. |  -  |


## setTelegramCommands

> void setTelegramCommands(accountId, setTelegramCommandsRequest)

Set TG bot commands

Set bot commands for a Telegram account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetTelegramCommandsRequest setTelegramCommandsRequest = new SetTelegramCommandsRequest(); // SetTelegramCommandsRequest | 
        try {
            apiInstance.setTelegramCommands(accountId, setTelegramCommandsRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setTelegramCommands");
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
| **setTelegramCommandsRequest** | [**SetTelegramCommandsRequest**](SetTelegramCommandsRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Commands set successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## setTelegramCommandsWithHttpInfo

> ApiResponse<Void> setTelegramCommands setTelegramCommandsWithHttpInfo(accountId, setTelegramCommandsRequest)

Set TG bot commands

Set bot commands for a Telegram account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountSettingsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountSettingsApi apiInstance = new AccountSettingsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        SetTelegramCommandsRequest setTelegramCommandsRequest = new SetTelegramCommandsRequest(); // SetTelegramCommandsRequest | 
        try {
            ApiResponse<Void> response = apiInstance.setTelegramCommandsWithHttpInfo(accountId, setTelegramCommandsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountSettingsApi#setTelegramCommands");
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
| **setTelegramCommandsRequest** | [**SetTelegramCommandsRequest**](SetTelegramCommandsRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Commands set successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

