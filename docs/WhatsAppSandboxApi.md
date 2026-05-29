# WhatsAppSandboxApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWhatsAppSandboxSession**](WhatsAppSandboxApi.md#createWhatsAppSandboxSession) | **POST** /v1/whatsapp/sandbox/sessions | Start a sandbox activation for a phone |
| [**createWhatsAppSandboxSessionWithHttpInfo**](WhatsAppSandboxApi.md#createWhatsAppSandboxSessionWithHttpInfo) | **POST** /v1/whatsapp/sandbox/sessions | Start a sandbox activation for a phone |
| [**deleteWhatsAppSandboxSession**](WhatsAppSandboxApi.md#deleteWhatsAppSandboxSession) | **DELETE** /v1/whatsapp/sandbox/sessions/{sessionId} | Revoke a sandbox session |
| [**deleteWhatsAppSandboxSessionWithHttpInfo**](WhatsAppSandboxApi.md#deleteWhatsAppSandboxSessionWithHttpInfo) | **DELETE** /v1/whatsapp/sandbox/sessions/{sessionId} | Revoke a sandbox session |
| [**listWhatsAppSandboxSessions**](WhatsAppSandboxApi.md#listWhatsAppSandboxSessions) | **GET** /v1/whatsapp/sandbox/sessions | List your sandbox sessions |
| [**listWhatsAppSandboxSessionsWithHttpInfo**](WhatsAppSandboxApi.md#listWhatsAppSandboxSessionsWithHttpInfo) | **GET** /v1/whatsapp/sandbox/sessions | List your sandbox sessions |



## createWhatsAppSandboxSession

> CreateWhatsAppSandboxSession200Response createWhatsAppSandboxSession(createWhatsAppSandboxSessionRequest)

Start a sandbox activation for a phone

Creates (or refreshes) a pending sandbox session for the given phone and immediately fires the verified sandbox template from the shared sandbox number to that phone. The session activates when the phone owner replies to that WhatsApp message — the reply itself is proof of ownership.  One phone per user: if the caller already has a non-expired session for a DIFFERENT phone, the request is rejected with &#x60;invalid_field_value&#x60; (the message names the existing phone so it can be revoked first). Re-creating a session for the SAME phone is idempotent and refreshes the verification template.  If Meta rejects the template send (not a WhatsApp number, paused WABA, token issue), the pending row is rolled back and the Meta error message is returned in &#x60;error&#x60; so the caller knows why. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppSandboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppSandboxApi apiInstance = new WhatsAppSandboxApi(defaultClient);
        CreateWhatsAppSandboxSessionRequest createWhatsAppSandboxSessionRequest = new CreateWhatsAppSandboxSessionRequest(); // CreateWhatsAppSandboxSessionRequest | 
        try {
            CreateWhatsAppSandboxSession200Response result = apiInstance.createWhatsAppSandboxSession(createWhatsAppSandboxSessionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppSandboxApi#createWhatsAppSandboxSession");
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
| **createWhatsAppSandboxSessionRequest** | [**CreateWhatsAppSandboxSessionRequest**](CreateWhatsAppSandboxSessionRequest.md)|  | |

### Return type

[**CreateWhatsAppSandboxSession200Response**](CreateWhatsAppSandboxSession200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session created or refreshed; verification template sent |  -  |
| **400** | Returned when (a) phone format is invalid, (b) phone equals the sandbox number itself, (c) the user already has a session for a different phone, or (d) Meta rejected the template send. The &#x60;error&#x60; field contains the specific reason; &#x60;param&#x60; is set when a field is at fault.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## createWhatsAppSandboxSessionWithHttpInfo

> ApiResponse<CreateWhatsAppSandboxSession200Response> createWhatsAppSandboxSession createWhatsAppSandboxSessionWithHttpInfo(createWhatsAppSandboxSessionRequest)

Start a sandbox activation for a phone

Creates (or refreshes) a pending sandbox session for the given phone and immediately fires the verified sandbox template from the shared sandbox number to that phone. The session activates when the phone owner replies to that WhatsApp message — the reply itself is proof of ownership.  One phone per user: if the caller already has a non-expired session for a DIFFERENT phone, the request is rejected with &#x60;invalid_field_value&#x60; (the message names the existing phone so it can be revoked first). Re-creating a session for the SAME phone is idempotent and refreshes the verification template.  If Meta rejects the template send (not a WhatsApp number, paused WABA, token issue), the pending row is rolled back and the Meta error message is returned in &#x60;error&#x60; so the caller knows why. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppSandboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppSandboxApi apiInstance = new WhatsAppSandboxApi(defaultClient);
        CreateWhatsAppSandboxSessionRequest createWhatsAppSandboxSessionRequest = new CreateWhatsAppSandboxSessionRequest(); // CreateWhatsAppSandboxSessionRequest | 
        try {
            ApiResponse<CreateWhatsAppSandboxSession200Response> response = apiInstance.createWhatsAppSandboxSessionWithHttpInfo(createWhatsAppSandboxSessionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppSandboxApi#createWhatsAppSandboxSession");
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
| **createWhatsAppSandboxSessionRequest** | [**CreateWhatsAppSandboxSessionRequest**](CreateWhatsAppSandboxSessionRequest.md)|  | |

### Return type

ApiResponse<[**CreateWhatsAppSandboxSession200Response**](CreateWhatsAppSandboxSession200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session created or refreshed; verification template sent |  -  |
| **400** | Returned when (a) phone format is invalid, (b) phone equals the sandbox number itself, (c) the user already has a session for a different phone, or (d) Meta rejected the template send. The &#x60;error&#x60; field contains the specific reason; &#x60;param&#x60; is set when a field is at fault.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## deleteWhatsAppSandboxSession

> DeleteWhatsAppSandboxSession200Response deleteWhatsAppSandboxSession(sessionId)

Revoke a sandbox session

Hard-deletes the session. The user loses the ability to send to that phone via the sandbox until they re-activate it. Existing conversations and messages already exchanged with that phone are untouched — revocation only blocks FUTURE sends.  Sessions belonging to other users cannot be revoked; the response is the same 400 as \&quot;session not found\&quot; so existence isn&#39;t leaked. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppSandboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppSandboxApi apiInstance = new WhatsAppSandboxApi(defaultClient);
        String sessionId = "sessionId_example"; // String | The session id returned by POST /v1/whatsapp/sandbox/sessions.
        try {
            DeleteWhatsAppSandboxSession200Response result = apiInstance.deleteWhatsAppSandboxSession(sessionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppSandboxApi#deleteWhatsAppSandboxSession");
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
| **sessionId** | **String**| The session id returned by POST /v1/whatsapp/sandbox/sessions. | |

### Return type

[**DeleteWhatsAppSandboxSession200Response**](DeleteWhatsAppSandboxSession200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session revoked |  -  |
| **400** | Invalid or unknown session id |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## deleteWhatsAppSandboxSessionWithHttpInfo

> ApiResponse<DeleteWhatsAppSandboxSession200Response> deleteWhatsAppSandboxSession deleteWhatsAppSandboxSessionWithHttpInfo(sessionId)

Revoke a sandbox session

Hard-deletes the session. The user loses the ability to send to that phone via the sandbox until they re-activate it. Existing conversations and messages already exchanged with that phone are untouched — revocation only blocks FUTURE sends.  Sessions belonging to other users cannot be revoked; the response is the same 400 as \&quot;session not found\&quot; so existence isn&#39;t leaked. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppSandboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppSandboxApi apiInstance = new WhatsAppSandboxApi(defaultClient);
        String sessionId = "sessionId_example"; // String | The session id returned by POST /v1/whatsapp/sandbox/sessions.
        try {
            ApiResponse<DeleteWhatsAppSandboxSession200Response> response = apiInstance.deleteWhatsAppSandboxSessionWithHttpInfo(sessionId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppSandboxApi#deleteWhatsAppSandboxSession");
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
| **sessionId** | **String**| The session id returned by POST /v1/whatsapp/sandbox/sessions. | |

### Return type

ApiResponse<[**DeleteWhatsAppSandboxSession200Response**](DeleteWhatsAppSandboxSession200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session revoked |  -  |
| **400** | Invalid or unknown session id |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## listWhatsAppSandboxSessions

> ListWhatsAppSandboxSessions200Response listWhatsAppSandboxSessions()

List your sandbox sessions

Returns all of the authenticated user&#39;s non-expired sandbox sessions (pending + active) plus the sandbox phone number. In practice there is at most one session per user since the sandbox is one-phone-per-user; the array shape is preserved for forward compatibility. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppSandboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppSandboxApi apiInstance = new WhatsAppSandboxApi(defaultClient);
        try {
            ListWhatsAppSandboxSessions200Response result = apiInstance.listWhatsAppSandboxSessions();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppSandboxApi#listWhatsAppSandboxSessions");
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

[**ListWhatsAppSandboxSessions200Response**](ListWhatsAppSandboxSessions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sessions retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## listWhatsAppSandboxSessionsWithHttpInfo

> ApiResponse<ListWhatsAppSandboxSessions200Response> listWhatsAppSandboxSessions listWhatsAppSandboxSessionsWithHttpInfo()

List your sandbox sessions

Returns all of the authenticated user&#39;s non-expired sandbox sessions (pending + active) plus the sandbox phone number. In practice there is at most one session per user since the sandbox is one-phone-per-user; the array shape is preserved for forward compatibility. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppSandboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppSandboxApi apiInstance = new WhatsAppSandboxApi(defaultClient);
        try {
            ApiResponse<ListWhatsAppSandboxSessions200Response> response = apiInstance.listWhatsAppSandboxSessionsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppSandboxApi#listWhatsAppSandboxSessions");
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

ApiResponse<[**ListWhatsAppSandboxSessions200Response**](ListWhatsAppSandboxSessions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sessions retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

