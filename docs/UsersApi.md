# UsersApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCurrentUser**](UsersApi.md#getCurrentUser) | **GET** /v1/users/me | Get the current user |
| [**getCurrentUserWithHttpInfo**](UsersApi.md#getCurrentUserWithHttpInfo) | **GET** /v1/users/me | Get the current user |
| [**getUser**](UsersApi.md#getUser) | **GET** /v1/users/{userId} | Get user |
| [**getUserWithHttpInfo**](UsersApi.md#getUserWithHttpInfo) | **GET** /v1/users/{userId} | Get user |
| [**listUsers**](UsersApi.md#listUsers) | **GET** /v1/users | List users |
| [**listUsersWithHttpInfo**](UsersApi.md#listUsersWithHttpInfo) | **GET** /v1/users | List users |
| [**removeUser**](UsersApi.md#removeUser) | **DELETE** /v1/users/{userId} | Remove member |
| [**removeUserWithHttpInfo**](UsersApi.md#removeUserWithHttpInfo) | **DELETE** /v1/users/{userId} | Remove member |



## getCurrentUser

> GetCurrentUser200Response getCurrentUser()

Get the current user

Returns the user the credential belongs to, in the same shape as one element of &#x60;users&#x60; in GET /v1/users, plus the workspace the credential acts in. Use it to check who an API key belongs to without listing every user.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        try {
            GetCurrentUser200Response result = apiInstance.getCurrentUser();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#getCurrentUser");
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

[**GetCurrentUser200Response**](GetCurrentUser200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current user |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getCurrentUserWithHttpInfo

> ApiResponse<GetCurrentUser200Response> getCurrentUser getCurrentUserWithHttpInfo()

Get the current user

Returns the user the credential belongs to, in the same shape as one element of &#x60;users&#x60; in GET /v1/users, plus the workspace the credential acts in. Use it to check who an API key belongs to without listing every user.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        try {
            ApiResponse<GetCurrentUser200Response> response = apiInstance.getCurrentUserWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#getCurrentUser");
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

ApiResponse<[**GetCurrentUser200Response**](GetCurrentUser200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current user |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getUser

> GetUser200Response getUser(userId)

Get user

Returns a single user&#39;s details by ID, including name, email, and role.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        String userId = "userId_example"; // String | 
        try {
            GetUser200Response result = apiInstance.getUser(userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#getUser");
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
| **userId** | **String**|  | |

### Return type

[**GetUser200Response**](GetUser200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

## getUserWithHttpInfo

> ApiResponse<GetUser200Response> getUser getUserWithHttpInfo(userId)

Get user

Returns a single user&#39;s details by ID, including name, email, and role.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        String userId = "userId_example"; // String | 
        try {
            ApiResponse<GetUser200Response> response = apiInstance.getUserWithHttpInfo(userId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#getUser");
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
| **userId** | **String**|  | |

### Return type

ApiResponse<[**GetUser200Response**](GetUser200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |


## listUsers

> ListUsers200Response listUsers()

List users

Returns all users in the team including roles and profile access. Also returns the currentUserId of the caller.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        try {
            ListUsers200Response result = apiInstance.listUsers();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#listUsers");
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

[**ListUsers200Response**](ListUsers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Users |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listUsersWithHttpInfo

> ApiResponse<ListUsers200Response> listUsers listUsersWithHttpInfo()

List users

Returns all users in the team including roles and profile access. Also returns the currentUserId of the caller.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        try {
            ApiResponse<ListUsers200Response> response = apiInstance.listUsersWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#listUsers");
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

ApiResponse<[**ListUsers200Response**](ListUsers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Users |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## removeUser

> RemoveUser200Response removeUser(userId)

Remove member

Removes a member from your team. The member keeps their own login and what they had before joining. What they added as a member passes to the team owner.  API keys the member used in the last 7 days pass to the owner and expire within 24 hours, and their other keys in the team are revoked.  Requires the owner or an admin, and a key that is not restricted. You cannot remove yourself.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        String userId = "userId_example"; // String | 
        try {
            RemoveUser200Response result = apiInstance.removeUser(userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#removeUser");
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
| **userId** | **String**|  | |

### Return type

[**RemoveUser200Response**](RemoveUser200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Member removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. The caller is not the owner or an admin, is removing themselves, or uses a restricted key.  With code &#x60;only_owner_acts_on_admins&#x60;, an admin tried to remove another admin, which only the owner can do. That code is returned to callers who have the workspaces preview. The dashboard routes that change a member&#39;s role and access return the same code. |  -  |
| **404** | Resource not found |  -  |
| **503** | The member&#39;s data could not be moved yet. Nothing was changed. Retry in a minute. |  -  |

## removeUserWithHttpInfo

> ApiResponse<RemoveUser200Response> removeUser removeUserWithHttpInfo(userId)

Remove member

Removes a member from your team. The member keeps their own login and what they had before joining. What they added as a member passes to the team owner.  API keys the member used in the last 7 days pass to the owner and expire within 24 hours, and their other keys in the team are revoked.  Requires the owner or an admin, and a key that is not restricted. You cannot remove yourself.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsersApi apiInstance = new UsersApi(defaultClient);
        String userId = "userId_example"; // String | 
        try {
            ApiResponse<RemoveUser200Response> response = apiInstance.removeUserWithHttpInfo(userId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsersApi#removeUser");
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
| **userId** | **String**|  | |

### Return type

ApiResponse<[**RemoveUser200Response**](RemoveUser200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Member removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. The caller is not the owner or an admin, is removing themselves, or uses a restricted key.  With code &#x60;only_owner_acts_on_admins&#x60;, an admin tried to remove another admin, which only the owner can do. That code is returned to callers who have the workspaces preview. The dashboard routes that change a member&#39;s role and access return the same code. |  -  |
| **404** | Resource not found |  -  |
| **503** | The member&#39;s data could not be moved yet. Nothing was changed. Retry in a minute. |  -  |

