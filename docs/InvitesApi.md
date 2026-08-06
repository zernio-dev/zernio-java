# InvitesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInviteToken**](InvitesApi.md#createInviteToken) | **POST** /v1/invite/tokens | Create invite token |
| [**createInviteTokenWithHttpInfo**](InvitesApi.md#createInviteTokenWithHttpInfo) | **POST** /v1/invite/tokens | Create invite token |



## createInviteToken

> CreateInviteToken201Response createInviteToken(createInviteTokenRequest)

Create invite token

Generate a secure invite link to grant team members access to your profiles. Invites expire after 7 days and are single-use.  Returns 403 when a requested profile is not found or not owned, or when called with a restricted (zrk_) API key: invite management is admin-plane. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InvitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InvitesApi apiInstance = new InvitesApi(defaultClient);
        CreateInviteTokenRequest createInviteTokenRequest = new CreateInviteTokenRequest(); // CreateInviteTokenRequest | 
        try {
            CreateInviteToken201Response result = apiInstance.createInviteToken(createInviteTokenRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitesApi#createInviteToken");
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
| **createInviteTokenRequest** | [**CreateInviteTokenRequest**](CreateInviteTokenRequest.md)|  | |

### Return type

[**CreateInviteToken201Response**](CreateInviteToken201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invite token created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## createInviteTokenWithHttpInfo

> ApiResponse<CreateInviteToken201Response> createInviteToken createInviteTokenWithHttpInfo(createInviteTokenRequest)

Create invite token

Generate a secure invite link to grant team members access to your profiles. Invites expire after 7 days and are single-use.  Returns 403 when a requested profile is not found or not owned, or when called with a restricted (zrk_) API key: invite management is admin-plane. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InvitesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InvitesApi apiInstance = new InvitesApi(defaultClient);
        CreateInviteTokenRequest createInviteTokenRequest = new CreateInviteTokenRequest(); // CreateInviteTokenRequest | 
        try {
            ApiResponse<CreateInviteToken201Response> response = apiInstance.createInviteTokenWithHttpInfo(createInviteTokenRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InvitesApi#createInviteToken");
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
| **createInviteTokenRequest** | [**CreateInviteTokenRequest**](CreateInviteTokenRequest.md)|  | |

### Return type

ApiResponse<[**CreateInviteToken201Response**](CreateInviteToken201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invite token created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

