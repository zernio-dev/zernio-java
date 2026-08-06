# ConnectedAppsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listConnectedApps**](ConnectedAppsApi.md#listConnectedApps) | **GET** /v1/me/connected-apps | List connected apps |
| [**listConnectedAppsWithHttpInfo**](ConnectedAppsApi.md#listConnectedAppsWithHttpInfo) | **GET** /v1/me/connected-apps | List connected apps |
| [**revokeConnectedApp**](ConnectedAppsApi.md#revokeConnectedApp) | **DELETE** /v1/me/connected-apps/{clientId} | Revoke connected app |
| [**revokeConnectedAppWithHttpInfo**](ConnectedAppsApi.md#revokeConnectedAppWithHttpInfo) | **DELETE** /v1/me/connected-apps/{clientId} | Revoke connected app |



## listConnectedApps

> ListConnectedApps200Response listConnectedApps()

List connected apps

Returns the OAuth clients (AI assistants and MCP connectors) the authenticated user has authorized and that still hold a live token.  Requires a session or a full-access API key. A profile-scoped API key, a restricted (zrk_) API key, or an OAuth access token is rejected with 403: an app must not be able to enumerate its sibling authorizations, and connected-app management is admin-plane. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectedAppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectedAppsApi apiInstance = new ConnectedAppsApi(defaultClient);
        try {
            ListConnectedApps200Response result = apiInstance.listConnectedApps();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectedAppsApi#listConnectedApps");
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

[**ListConnectedApps200Response**](ListConnectedApps200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connected apps |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes and delivery-log reads, a named event maps to a resource group the key does not hold (a no-messages key cannot subscribe to or replay message.* events). |  -  |

## listConnectedAppsWithHttpInfo

> ApiResponse<ListConnectedApps200Response> listConnectedApps listConnectedAppsWithHttpInfo()

List connected apps

Returns the OAuth clients (AI assistants and MCP connectors) the authenticated user has authorized and that still hold a live token.  Requires a session or a full-access API key. A profile-scoped API key, a restricted (zrk_) API key, or an OAuth access token is rejected with 403: an app must not be able to enumerate its sibling authorizations, and connected-app management is admin-plane. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectedAppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectedAppsApi apiInstance = new ConnectedAppsApi(defaultClient);
        try {
            ApiResponse<ListConnectedApps200Response> response = apiInstance.listConnectedAppsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectedAppsApi#listConnectedApps");
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

ApiResponse<[**ListConnectedApps200Response**](ListConnectedApps200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connected apps |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes and delivery-log reads, a named event maps to a resource group the key does not hold (a no-messages key cannot subscribe to or replay message.* events). |  -  |


## revokeConnectedApp

> RevokeConnectedApp200Response revokeConnectedApp(clientId)

Revoke connected app

Ends an app&#39;s access: invalidates the client&#39;s pending authorization codes and revokes every live token it holds for the authenticated user. Takes effect on the app&#39;s next request.  Idempotent while the authorization is still on record: revoking an app that was already revoked returns 200 with &#x60;revokedTokens: 0&#x60;.  Requires a session or a full-access API key. A profile-scoped API key, a restricted (zrk_) API key, or an OAuth access token is rejected with 403. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectedAppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectedAppsApi apiInstance = new ConnectedAppsApi(defaultClient);
        String clientId = "clientId_example"; // String | OAuth client id, as returned by GET /v1/me/connected-apps.
        try {
            RevokeConnectedApp200Response result = apiInstance.revokeConnectedApp(clientId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectedAppsApi#revokeConnectedApp");
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
| **clientId** | **String**| OAuth client id, as returned by GET /v1/me/connected-apps. | |

### Return type

[**RevokeConnectedApp200Response**](RevokeConnectedApp200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Revoked |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes and delivery-log reads, a named event maps to a resource group the key does not hold (a no-messages key cannot subscribe to or replay message.* events). |  -  |
| **404** | The authenticated user has never authorized this client. Error code: oauth_client_not_found. |  -  |

## revokeConnectedAppWithHttpInfo

> ApiResponse<RevokeConnectedApp200Response> revokeConnectedApp revokeConnectedAppWithHttpInfo(clientId)

Revoke connected app

Ends an app&#39;s access: invalidates the client&#39;s pending authorization codes and revokes every live token it holds for the authenticated user. Takes effect on the app&#39;s next request.  Idempotent while the authorization is still on record: revoking an app that was already revoked returns 200 with &#x60;revokedTokens: 0&#x60;.  Requires a session or a full-access API key. A profile-scoped API key, a restricted (zrk_) API key, or an OAuth access token is rejected with 403. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConnectedAppsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConnectedAppsApi apiInstance = new ConnectedAppsApi(defaultClient);
        String clientId = "clientId_example"; // String | OAuth client id, as returned by GET /v1/me/connected-apps.
        try {
            ApiResponse<RevokeConnectedApp200Response> response = apiInstance.revokeConnectedAppWithHttpInfo(clientId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConnectedAppsApi#revokeConnectedApp");
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
| **clientId** | **String**| OAuth client id, as returned by GET /v1/me/connected-apps. | |

### Return type

ApiResponse<[**RevokeConnectedApp200Response**](RevokeConnectedApp200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Revoked |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes and delivery-log reads, a named event maps to a resource group the key does not hold (a no-messages key cannot subscribe to or replay message.* events). |  -  |
| **404** | The authenticated user has never authorized this client. Error code: oauth_client_not_found. |  -  |

