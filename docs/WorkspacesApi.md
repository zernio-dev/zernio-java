# WorkspacesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkspace**](WorkspacesApi.md#createWorkspace) | **POST** /v1/workspaces | Create workspace |
| [**createWorkspaceWithHttpInfo**](WorkspacesApi.md#createWorkspaceWithHttpInfo) | **POST** /v1/workspaces | Create workspace |
| [**createWorkspaceApiKey**](WorkspacesApi.md#createWorkspaceApiKey) | **POST** /v1/workspaces/{workspaceId}/api-keys | Create workspace key |
| [**createWorkspaceApiKeyWithHttpInfo**](WorkspacesApi.md#createWorkspaceApiKeyWithHttpInfo) | **POST** /v1/workspaces/{workspaceId}/api-keys | Create workspace key |
| [**deleteWorkspace**](WorkspacesApi.md#deleteWorkspace) | **DELETE** /v1/workspaces/{workspaceId} | Delete workspace |
| [**deleteWorkspaceWithHttpInfo**](WorkspacesApi.md#deleteWorkspaceWithHttpInfo) | **DELETE** /v1/workspaces/{workspaceId} | Delete workspace |
| [**getWorkspace**](WorkspacesApi.md#getWorkspace) | **GET** /v1/workspaces/{workspaceId} | Get workspace |
| [**getWorkspaceWithHttpInfo**](WorkspacesApi.md#getWorkspaceWithHttpInfo) | **GET** /v1/workspaces/{workspaceId} | Get workspace |
| [**listWorkspaces**](WorkspacesApi.md#listWorkspaces) | **GET** /v1/workspaces | List workspaces |
| [**listWorkspacesWithHttpInfo**](WorkspacesApi.md#listWorkspacesWithHttpInfo) | **GET** /v1/workspaces | List workspaces |
| [**updateWorkspace**](WorkspacesApi.md#updateWorkspace) | **PATCH** /v1/workspaces/{workspaceId} | Rename workspace |
| [**updateWorkspaceWithHttpInfo**](WorkspacesApi.md#updateWorkspaceWithHttpInfo) | **PATCH** /v1/workspaces/{workspaceId} | Rename workspace |



## createWorkspace

> CreateWorkspace201Response createWorkspace(createWorkspaceRequest)

Create workspace

Creates a new, empty workspace owned by the key&#39;s owner, for example one per client of your product.  - Send &#x60;apiKey&#x60; to get the new workspace&#39;s first key in the same call. A key only manages its own workspace, so no other key can mint one there later. - The workspace has no billing. Its keys can read, but writes return 402 &#x60;workspace_billing_required&#x60; until billing is set up at &#x60;billing.setupUrl&#x60;. - Needs a full-access key. Creation is capped at 5 a day and 20 owned workspaces without billing (429). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        CreateWorkspaceRequest createWorkspaceRequest = new CreateWorkspaceRequest(); // CreateWorkspaceRequest | 
        try {
            CreateWorkspace201Response result = apiInstance.createWorkspace(createWorkspaceRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#createWorkspace");
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
| **createWorkspaceRequest** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)|  | |

### Return type

[**CreateWorkspace201Response**](CreateWorkspace201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | Creation cap reached. Error code: workspace_daily_limit_reached (5 a day) or workspace_limit_reached (20 owned without billing). |  -  |

## createWorkspaceWithHttpInfo

> ApiResponse<CreateWorkspace201Response> createWorkspace createWorkspaceWithHttpInfo(createWorkspaceRequest)

Create workspace

Creates a new, empty workspace owned by the key&#39;s owner, for example one per client of your product.  - Send &#x60;apiKey&#x60; to get the new workspace&#39;s first key in the same call. A key only manages its own workspace, so no other key can mint one there later. - The workspace has no billing. Its keys can read, but writes return 402 &#x60;workspace_billing_required&#x60; until billing is set up at &#x60;billing.setupUrl&#x60;. - Needs a full-access key. Creation is capped at 5 a day and 20 owned workspaces without billing (429). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        CreateWorkspaceRequest createWorkspaceRequest = new CreateWorkspaceRequest(); // CreateWorkspaceRequest | 
        try {
            ApiResponse<CreateWorkspace201Response> response = apiInstance.createWorkspaceWithHttpInfo(createWorkspaceRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#createWorkspace");
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
| **createWorkspaceRequest** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)|  | |

### Return type

ApiResponse<[**CreateWorkspace201Response**](CreateWorkspace201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | Creation cap reached. Error code: workspace_daily_limit_reached (5 a day) or workspace_limit_reached (20 owned without billing). |  -  |


## createWorkspaceApiKey

> CreateWorkspaceApiKey201Response createWorkspaceApiKey(workspaceId, createWorkspaceApiKeyRequest)

Create workspace key

Creates another API key that acts in this workspace as its creator. It covers every profile, and its full value is returned only once.  - The caller must be owner or admin there. - The calling credential must be a full-access key of this same workspace. Profile-scoped, restricted and handed-over keys, OAuth tokens and keys of other workspaces get 403. - For another workspace, use the dashboard. For a new one, send &#x60;apiKey&#x60; on &#x60;POST /v1/workspaces&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        CreateWorkspaceApiKeyRequest createWorkspaceApiKeyRequest = new CreateWorkspaceApiKeyRequest(); // CreateWorkspaceApiKeyRequest | 
        try {
            CreateWorkspaceApiKey201Response result = apiInstance.createWorkspaceApiKey(workspaceId, createWorkspaceApiKeyRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#createWorkspaceApiKey");
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
| **workspaceId** | **String**|  | |
| **createWorkspaceApiKeyRequest** | [**CreateWorkspaceApiKeyRequest**](CreateWorkspaceApiKeyRequest.md)|  | |

### Return type

[**CreateWorkspaceApiKey201Response**](CreateWorkspaceApiKey201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | The caller is not owner or admin there (workspace_forbidden), or the calling credential is not a full-access key of this workspace (insufficient_permissions). |  -  |
| **404** | Resource not found |  -  |

## createWorkspaceApiKeyWithHttpInfo

> ApiResponse<CreateWorkspaceApiKey201Response> createWorkspaceApiKey createWorkspaceApiKeyWithHttpInfo(workspaceId, createWorkspaceApiKeyRequest)

Create workspace key

Creates another API key that acts in this workspace as its creator. It covers every profile, and its full value is returned only once.  - The caller must be owner or admin there. - The calling credential must be a full-access key of this same workspace. Profile-scoped, restricted and handed-over keys, OAuth tokens and keys of other workspaces get 403. - For another workspace, use the dashboard. For a new one, send &#x60;apiKey&#x60; on &#x60;POST /v1/workspaces&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        CreateWorkspaceApiKeyRequest createWorkspaceApiKeyRequest = new CreateWorkspaceApiKeyRequest(); // CreateWorkspaceApiKeyRequest | 
        try {
            ApiResponse<CreateWorkspaceApiKey201Response> response = apiInstance.createWorkspaceApiKeyWithHttpInfo(workspaceId, createWorkspaceApiKeyRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#createWorkspaceApiKey");
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
| **workspaceId** | **String**|  | |
| **createWorkspaceApiKeyRequest** | [**CreateWorkspaceApiKeyRequest**](CreateWorkspaceApiKeyRequest.md)|  | |

### Return type

ApiResponse<[**CreateWorkspaceApiKey201Response**](CreateWorkspaceApiKey201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | The caller is not owner or admin there (workspace_forbidden), or the calling credential is not a full-access key of this workspace (insufficient_permissions). |  -  |
| **404** | Resource not found |  -  |


## deleteWorkspace

> GetWorkspace200Response deleteWorkspace(workspaceId, moveBalanceTo, forfeitBalance)

Delete workspace

Schedules the workspace for deletion 48 hours ahead, as the dashboard does. Members keep working, publishing is paused, and the owner or an admin can cancel from the dashboard until then. Only this workspace&#39;s data is deleted, never its members&#39; accounts.  - Owner only, with a full-access key of this workspace. A key of another workspace gets 403; delete it from the dashboard. - A Personal workspace is never deleted. - Refused while the workspace owes a payment or holds a phone number or carrier registration (409 &#x60;deletion_blocked&#x60;). - With a balance above $0, send &#x60;moveBalanceTo&#x60; (another billed workspace you own) or &#x60;forfeitBalance&#x3D;true&#x60;. Balances are never refunded. Without either the call returns 422 &#x60;deletion_balance_choice&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        String moveBalanceTo = "moveBalanceTo_example"; // String | A billed workspace you own that receives the remaining balance.
        Boolean forfeitBalance = true; // Boolean | Leave the remaining balance; it is written off when the workspace is deleted.
        try {
            GetWorkspace200Response result = apiInstance.deleteWorkspace(workspaceId, moveBalanceTo, forfeitBalance);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#deleteWorkspace");
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
| **workspaceId** | **String**|  | |
| **moveBalanceTo** | **String**| A billed workspace you own that receives the remaining balance. | [optional] |
| **forfeitBalance** | **Boolean**| Leave the remaining balance; it is written off when the workspace is deleted. | [optional] |

### Return type

[**GetWorkspace200Response**](GetWorkspace200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletion scheduled |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | Only the owner can delete a workspace (workspace_forbidden), with a full-access key of this workspace (insufficient_permissions otherwise). |  -  |
| **404** | Resource not found |  -  |
| **409** | Refused: personal_workspace, deletion_already_scheduled, or deletion_blocked (a payment due, a phone number or a carrier registration; the message names it). |  -  |
| **422** | The workspace has a balance: send moveBalanceTo or forfeitBalance. Error code: deletion_balance_choice. |  -  |

## deleteWorkspaceWithHttpInfo

> ApiResponse<GetWorkspace200Response> deleteWorkspace deleteWorkspaceWithHttpInfo(workspaceId, moveBalanceTo, forfeitBalance)

Delete workspace

Schedules the workspace for deletion 48 hours ahead, as the dashboard does. Members keep working, publishing is paused, and the owner or an admin can cancel from the dashboard until then. Only this workspace&#39;s data is deleted, never its members&#39; accounts.  - Owner only, with a full-access key of this workspace. A key of another workspace gets 403; delete it from the dashboard. - A Personal workspace is never deleted. - Refused while the workspace owes a payment or holds a phone number or carrier registration (409 &#x60;deletion_blocked&#x60;). - With a balance above $0, send &#x60;moveBalanceTo&#x60; (another billed workspace you own) or &#x60;forfeitBalance&#x3D;true&#x60;. Balances are never refunded. Without either the call returns 422 &#x60;deletion_balance_choice&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        String moveBalanceTo = "moveBalanceTo_example"; // String | A billed workspace you own that receives the remaining balance.
        Boolean forfeitBalance = true; // Boolean | Leave the remaining balance; it is written off when the workspace is deleted.
        try {
            ApiResponse<GetWorkspace200Response> response = apiInstance.deleteWorkspaceWithHttpInfo(workspaceId, moveBalanceTo, forfeitBalance);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#deleteWorkspace");
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
| **workspaceId** | **String**|  | |
| **moveBalanceTo** | **String**| A billed workspace you own that receives the remaining balance. | [optional] |
| **forfeitBalance** | **Boolean**| Leave the remaining balance; it is written off when the workspace is deleted. | [optional] |

### Return type

ApiResponse<[**GetWorkspace200Response**](GetWorkspace200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deletion scheduled |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | Only the owner can delete a workspace (workspace_forbidden), with a full-access key of this workspace (insufficient_permissions otherwise). |  -  |
| **404** | Resource not found |  -  |
| **409** | Refused: personal_workspace, deletion_already_scheduled, or deletion_blocked (a payment due, a phone number or a carrier registration; the message names it). |  -  |
| **422** | The workspace has a balance: send moveBalanceTo or forfeitBalance. Error code: deletion_balance_choice. |  -  |


## getWorkspace

> GetWorkspace200Response getWorkspace(workspaceId)

Get workspace

Returns one workspace the key&#39;s owner belongs to, with their role. Owners, admins and billing admins also get &#x60;billing&#x60; (whether it is set up, and where to set it up); members and viewers do not.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        try {
            GetWorkspace200Response result = apiInstance.getWorkspace(workspaceId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#getWorkspace");
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
| **workspaceId** | **String**|  | |

### Return type

[**GetWorkspace200Response**](GetWorkspace200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspace |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |

## getWorkspaceWithHttpInfo

> ApiResponse<GetWorkspace200Response> getWorkspace getWorkspaceWithHttpInfo(workspaceId)

Get workspace

Returns one workspace the key&#39;s owner belongs to, with their role. Owners, admins and billing admins also get &#x60;billing&#x60; (whether it is set up, and where to set it up); members and viewers do not.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        try {
            ApiResponse<GetWorkspace200Response> response = apiInstance.getWorkspaceWithHttpInfo(workspaceId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#getWorkspace");
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
| **workspaceId** | **String**|  | |

### Return type

ApiResponse<[**GetWorkspace200Response**](GetWorkspace200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspace |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |


## listWorkspaces

> ListWorkspaces200Response listWorkspaces(limit, skip)

List workspaces

Lists every workspace the key&#39;s owner belongs to, with their role in each: teams first by name, their Personal workspace last. Any key of the owner lists them all, whatever workspace that key acts in.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        Integer limit = 50; // Integer | Page size.
        Integer skip = 0; // Integer | Number of workspaces to skip.
        try {
            ListWorkspaces200Response result = apiInstance.listWorkspaces(limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#listWorkspaces");
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
| **limit** | **Integer**| Page size. | [optional] [default to 50] |
| **skip** | **Integer**| Number of workspaces to skip. | [optional] [default to 0] |

### Return type

[**ListWorkspaces200Response**](ListWorkspaces200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspaces |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

## listWorkspacesWithHttpInfo

> ApiResponse<ListWorkspaces200Response> listWorkspaces listWorkspacesWithHttpInfo(limit, skip)

List workspaces

Lists every workspace the key&#39;s owner belongs to, with their role in each: teams first by name, their Personal workspace last. Any key of the owner lists them all, whatever workspace that key acts in.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        Integer limit = 50; // Integer | Page size.
        Integer skip = 0; // Integer | Number of workspaces to skip.
        try {
            ApiResponse<ListWorkspaces200Response> response = apiInstance.listWorkspacesWithHttpInfo(limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#listWorkspaces");
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
| **limit** | **Integer**| Page size. | [optional] [default to 50] |
| **skip** | **Integer**| Number of workspaces to skip. | [optional] [default to 0] |

### Return type

ApiResponse<[**ListWorkspaces200Response**](ListWorkspaces200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspaces |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |


## updateWorkspace

> GetWorkspace200Response updateWorkspace(workspaceId, updateWorkspaceRequest)

Rename workspace

Renames a workspace. Owner or admin there, with a full-access key of this workspace (a key of another workspace gets 403: rename it from the dashboard). Only a Personal workspace can be called \&quot;Personal\&quot;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        UpdateWorkspaceRequest updateWorkspaceRequest = new UpdateWorkspaceRequest(); // UpdateWorkspaceRequest | 
        try {
            GetWorkspace200Response result = apiInstance.updateWorkspace(workspaceId, updateWorkspaceRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#updateWorkspace");
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
| **workspaceId** | **String**|  | |
| **updateWorkspaceRequest** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)|  | |

### Return type

[**GetWorkspace200Response**](GetWorkspace200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Renamed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | The role there cannot rename it (workspace_forbidden), the key is not a full-access key, or the key acts in another workspace (insufficient_permissions: use a key of this workspace or the dashboard). |  -  |
| **404** | Resource not found |  -  |

## updateWorkspaceWithHttpInfo

> ApiResponse<GetWorkspace200Response> updateWorkspace updateWorkspaceWithHttpInfo(workspaceId, updateWorkspaceRequest)

Rename workspace

Renames a workspace. Owner or admin there, with a full-access key of this workspace (a key of another workspace gets 403: rename it from the dashboard). Only a Personal workspace can be called \&quot;Personal\&quot;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkspacesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
        String workspaceId = "workspaceId_example"; // String | 
        UpdateWorkspaceRequest updateWorkspaceRequest = new UpdateWorkspaceRequest(); // UpdateWorkspaceRequest | 
        try {
            ApiResponse<GetWorkspace200Response> response = apiInstance.updateWorkspaceWithHttpInfo(workspaceId, updateWorkspaceRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkspacesApi#updateWorkspace");
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
| **workspaceId** | **String**|  | |
| **updateWorkspaceRequest** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)|  | |

### Return type

ApiResponse<[**GetWorkspace200Response**](GetWorkspace200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Renamed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | The calling key acts in a workspace without billing, which cannot make changes through the API. Error code: workspace_billing_required. Set billing up for that workspace in the dashboard. |  -  |
| **403** | The role there cannot rename it (workspace_forbidden), the key is not a full-access key, or the key acts in another workspace (insufficient_permissions: use a key of this workspace or the dashboard). |  -  |
| **404** | Resource not found |  -  |

