# WhatsAppCallingApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disableWhatsAppCalling**](WhatsAppCallingApi.md#disableWhatsAppCalling) | **DELETE** /v1/whatsapp/phone-numbers/{id}/calling | Disable calling on a number |
| [**disableWhatsAppCallingWithHttpInfo**](WhatsAppCallingApi.md#disableWhatsAppCallingWithHttpInfo) | **DELETE** /v1/whatsapp/phone-numbers/{id}/calling | Disable calling on a number |
| [**enableWhatsAppCalling**](WhatsAppCallingApi.md#enableWhatsAppCalling) | **POST** /v1/whatsapp/phone-numbers/{id}/calling | Enable calling on a number |
| [**enableWhatsAppCallingWithHttpInfo**](WhatsAppCallingApi.md#enableWhatsAppCallingWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/{id}/calling | Enable calling on a number |
| [**getWhatsAppCall**](WhatsAppCallingApi.md#getWhatsAppCall) | **GET** /v1/whatsapp/calls/{callId} | Get a single call |
| [**getWhatsAppCallWithHttpInfo**](WhatsAppCallingApi.md#getWhatsAppCallWithHttpInfo) | **GET** /v1/whatsapp/calls/{callId} | Get a single call |
| [**getWhatsAppCallEstimate**](WhatsAppCallingApi.md#getWhatsAppCallEstimate) | **GET** /v1/whatsapp/calls/estimate | Estimate per-minute cost for a destination |
| [**getWhatsAppCallEstimateWithHttpInfo**](WhatsAppCallingApi.md#getWhatsAppCallEstimateWithHttpInfo) | **GET** /v1/whatsapp/calls/estimate | Estimate per-minute cost for a destination |
| [**getWhatsAppCallPermissions**](WhatsAppCallingApi.md#getWhatsAppCallPermissions) | **GET** /v1/whatsapp/call-permissions | Check call permission for a consumer |
| [**getWhatsAppCallPermissionsWithHttpInfo**](WhatsAppCallingApi.md#getWhatsAppCallPermissionsWithHttpInfo) | **GET** /v1/whatsapp/call-permissions | Check call permission for a consumer |
| [**getWhatsAppCallingConfig**](WhatsAppCallingApi.md#getWhatsAppCallingConfig) | **GET** /v1/whatsapp/calling | Get calling config for an account |
| [**getWhatsAppCallingConfigWithHttpInfo**](WhatsAppCallingApi.md#getWhatsAppCallingConfigWithHttpInfo) | **GET** /v1/whatsapp/calling | Get calling config for an account |
| [**initiateWhatsAppCall**](WhatsAppCallingApi.md#initiateWhatsAppCall) | **POST** /v1/whatsapp/calls | Initiate outbound call |
| [**initiateWhatsAppCallWithHttpInfo**](WhatsAppCallingApi.md#initiateWhatsAppCallWithHttpInfo) | **POST** /v1/whatsapp/calls | Initiate outbound call |
| [**listWhatsAppCalls**](WhatsAppCallingApi.md#listWhatsAppCalls) | **GET** /v1/whatsapp/calls | List call history for an account |
| [**listWhatsAppCallsWithHttpInfo**](WhatsAppCallingApi.md#listWhatsAppCallsWithHttpInfo) | **GET** /v1/whatsapp/calls | List call history for an account |
| [**updateWhatsAppCalling**](WhatsAppCallingApi.md#updateWhatsAppCalling) | **PATCH** /v1/whatsapp/phone-numbers/{id}/calling | Update calling config |
| [**updateWhatsAppCallingWithHttpInfo**](WhatsAppCallingApi.md#updateWhatsAppCallingWithHttpInfo) | **PATCH** /v1/whatsapp/phone-numbers/{id}/calling | Update calling config |



## disableWhatsAppCalling

> void disableWhatsAppCalling(id, accountId)

Disable calling on a number

Disable calling. Sends calling.status&#x3D;DISABLED to Meta (best-effort) and flips the local &#x60;callingEnabled&#x60; flag off. forwardTo and SIP creds are preserved so a re-enable does not lose the destination. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String id = "id_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            apiInstance.disableWhatsAppCalling(id, accountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#disableWhatsAppCalling");
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
| **id** | **String**|  | |
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
| **200** | Disabled |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found |  -  |

## disableWhatsAppCallingWithHttpInfo

> ApiResponse<Void> disableWhatsAppCalling disableWhatsAppCallingWithHttpInfo(id, accountId)

Disable calling on a number

Disable calling. Sends calling.status&#x3D;DISABLED to Meta (best-effort) and flips the local &#x60;callingEnabled&#x60; flag off. forwardTo and SIP creds are preserved so a re-enable does not lose the destination. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String id = "id_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.disableWhatsAppCallingWithHttpInfo(id, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#disableWhatsAppCalling");
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
| **id** | **String**|  | |
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
| **200** | Disabled |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found |  -  |


## enableWhatsAppCalling

> EnableWhatsAppCalling200Response enableWhatsAppCalling(id, enableWhatsAppCallingRequest)

Enable calling on a number

Enable WhatsApp Business Calling on a connected number. Configures Meta calling.status&#x3D;ENABLED with our Telnyx SIP endpoint, fetches and stores the Meta-issued SIP password (encrypted), and snapshots the customer&#39;s forward-to destination. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String id = "id_example"; // String | WhatsAppPhoneNumber Mongo ID
        EnableWhatsAppCallingRequest enableWhatsAppCallingRequest = new EnableWhatsAppCallingRequest(); // EnableWhatsAppCallingRequest | 
        try {
            EnableWhatsAppCalling200Response result = apiInstance.enableWhatsAppCalling(id, enableWhatsAppCallingRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#enableWhatsAppCalling");
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
| **id** | **String**| WhatsAppPhoneNumber Mongo ID | |
| **enableWhatsAppCallingRequest** | [**EnableWhatsAppCallingRequest**](EnableWhatsAppCallingRequest.md)|  | |

### Return type

[**EnableWhatsAppCalling200Response**](EnableWhatsAppCalling200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calling enabled |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found |  -  |
| **422** | Not eligible to enable calling: not on usage-based billing, or the number&#39;s messaging limit is below Meta&#39;s ~2,000-daily-recipient threshold (TIER_250). Warm the number up to raise the limit. |  -  |

## enableWhatsAppCallingWithHttpInfo

> ApiResponse<EnableWhatsAppCalling200Response> enableWhatsAppCalling enableWhatsAppCallingWithHttpInfo(id, enableWhatsAppCallingRequest)

Enable calling on a number

Enable WhatsApp Business Calling on a connected number. Configures Meta calling.status&#x3D;ENABLED with our Telnyx SIP endpoint, fetches and stores the Meta-issued SIP password (encrypted), and snapshots the customer&#39;s forward-to destination. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String id = "id_example"; // String | WhatsAppPhoneNumber Mongo ID
        EnableWhatsAppCallingRequest enableWhatsAppCallingRequest = new EnableWhatsAppCallingRequest(); // EnableWhatsAppCallingRequest | 
        try {
            ApiResponse<EnableWhatsAppCalling200Response> response = apiInstance.enableWhatsAppCallingWithHttpInfo(id, enableWhatsAppCallingRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#enableWhatsAppCalling");
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
| **id** | **String**| WhatsAppPhoneNumber Mongo ID | |
| **enableWhatsAppCallingRequest** | [**EnableWhatsAppCallingRequest**](EnableWhatsAppCallingRequest.md)|  | |

### Return type

ApiResponse<[**EnableWhatsAppCalling200Response**](EnableWhatsAppCalling200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calling enabled |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found |  -  |
| **422** | Not eligible to enable calling: not on usage-based billing, or the number&#39;s messaging limit is below Meta&#39;s ~2,000-daily-recipient threshold (TIER_250). Warm the number up to raise the limit. |  -  |


## getWhatsAppCall

> GetWhatsAppCall200Response getWhatsAppCall(callId, accountId)

Get a single call

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String callId = "callId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            GetWhatsAppCall200Response result = apiInstance.getWhatsAppCall(callId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCall");
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
| **callId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**GetWhatsAppCall200Response**](GetWhatsAppCall200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call |  -  |
| **401** | Unauthorized |  -  |
| **404** | Call not found |  -  |

## getWhatsAppCallWithHttpInfo

> ApiResponse<GetWhatsAppCall200Response> getWhatsAppCall getWhatsAppCallWithHttpInfo(callId, accountId)

Get a single call

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String callId = "callId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetWhatsAppCall200Response> response = apiInstance.getWhatsAppCallWithHttpInfo(callId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCall");
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
| **callId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**GetWhatsAppCall200Response**](GetWhatsAppCall200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call |  -  |
| **401** | Unauthorized |  -  |
| **404** | Call not found |  -  |


## getWhatsAppCallEstimate

> GetWhatsAppCallEstimate200Response getWhatsAppCallEstimate(accountId, to, minutes, recording)

Estimate per-minute cost for a destination

Returns a zero-markup estimated cost for an outbound call to the given destination, broken down by Meta + Telnyx + recording line items. Costs are pass-through, no margin applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String to = "to_example"; // String | 
        Integer minutes = 56; // Integer | 
        Boolean recording = true; // Boolean | 
        try {
            GetWhatsAppCallEstimate200Response result = apiInstance.getWhatsAppCallEstimate(accountId, to, minutes, recording);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCallEstimate");
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
| **to** | **String**|  | |
| **minutes** | **Integer**|  | [optional] |
| **recording** | **Boolean**|  | [optional] |

### Return type

[**GetWhatsAppCallEstimate200Response**](GetWhatsAppCallEstimate200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Estimate |  -  |
| **401** | Unauthorized |  -  |

## getWhatsAppCallEstimateWithHttpInfo

> ApiResponse<GetWhatsAppCallEstimate200Response> getWhatsAppCallEstimate getWhatsAppCallEstimateWithHttpInfo(accountId, to, minutes, recording)

Estimate per-minute cost for a destination

Returns a zero-markup estimated cost for an outbound call to the given destination, broken down by Meta + Telnyx + recording line items. Costs are pass-through, no margin applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String to = "to_example"; // String | 
        Integer minutes = 56; // Integer | 
        Boolean recording = true; // Boolean | 
        try {
            ApiResponse<GetWhatsAppCallEstimate200Response> response = apiInstance.getWhatsAppCallEstimateWithHttpInfo(accountId, to, minutes, recording);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCallEstimate");
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
| **to** | **String**|  | |
| **minutes** | **Integer**|  | [optional] |
| **recording** | **Boolean**|  | [optional] |

### Return type

ApiResponse<[**GetWhatsAppCallEstimate200Response**](GetWhatsAppCallEstimate200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Estimate |  -  |
| **401** | Unauthorized |  -  |


## getWhatsAppCallPermissions

> GetWhatsAppCallPermissions200Response getWhatsAppCallPermissions(accountId, to)

Check call permission for a consumer

Returns the permission state and the list of available actions for a given consumer wa_id (e.g. &#x60;start_call&#x60;, &#x60;send_call_permission_request&#x60;). Use this before placing a call to decide whether to prompt for consent first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String to = "to_example"; // String | Consumer wa_id (E.164, leading + optional)
        try {
            GetWhatsAppCallPermissions200Response result = apiInstance.getWhatsAppCallPermissions(accountId, to);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCallPermissions");
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
| **to** | **String**| Consumer wa_id (E.164, leading + optional) | |

### Return type

[**GetWhatsAppCallPermissions200Response**](GetWhatsAppCallPermissions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Permission state |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppCallPermissionsWithHttpInfo

> ApiResponse<GetWhatsAppCallPermissions200Response> getWhatsAppCallPermissions getWhatsAppCallPermissionsWithHttpInfo(accountId, to)

Check call permission for a consumer

Returns the permission state and the list of available actions for a given consumer wa_id (e.g. &#x60;start_call&#x60;, &#x60;send_call_permission_request&#x60;). Use this before placing a call to decide whether to prompt for consent first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String to = "to_example"; // String | Consumer wa_id (E.164, leading + optional)
        try {
            ApiResponse<GetWhatsAppCallPermissions200Response> response = apiInstance.getWhatsAppCallPermissionsWithHttpInfo(accountId, to);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCallPermissions");
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
| **to** | **String**| Consumer wa_id (E.164, leading + optional) | |

### Return type

ApiResponse<[**GetWhatsAppCallPermissions200Response**](GetWhatsAppCallPermissions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Permission state |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppCallingConfig

> GetWhatsAppCallingConfig200Response getWhatsAppCallingConfig(accountId)

Get calling config for an account

Returns the local calling configuration snapshot for the connected WhatsApp account: whether calling is enabled, the forward-to destination URI, recording opt-in state, the WhatsAppPhoneNumber doc id (use as &#x60;{id}&#x60; on the calling-config write endpoints) and whether SIP digest credentials are stored (the encrypted password itself is never returned). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppCallingConfig200Response result = apiInstance.getWhatsAppCallingConfig(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCallingConfig");
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
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**GetWhatsAppCallingConfig200Response**](GetWhatsAppCallingConfig200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calling config |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found for this account |  -  |

## getWhatsAppCallingConfigWithHttpInfo

> ApiResponse<GetWhatsAppCallingConfig200Response> getWhatsAppCallingConfig getWhatsAppCallingConfigWithHttpInfo(accountId)

Get calling config for an account

Returns the local calling configuration snapshot for the connected WhatsApp account: whether calling is enabled, the forward-to destination URI, recording opt-in state, the WhatsAppPhoneNumber doc id (use as &#x60;{id}&#x60; on the calling-config write endpoints) and whether SIP digest credentials are stored (the encrypted password itself is never returned). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppCallingConfig200Response> response = apiInstance.getWhatsAppCallingConfigWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#getWhatsAppCallingConfig");
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
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**GetWhatsAppCallingConfig200Response**](GetWhatsAppCallingConfig200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calling config |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found for this account |  -  |


## initiateWhatsAppCall

> InitiateWhatsAppCall200Response initiateWhatsAppCall(initiateWhatsAppCallRequest)

Initiate outbound call

Initiates an outbound Business-Initiated Call. The Telnyx-side SIP leg is originated server-side (Option B: SIP-first). Telnyx INVITEs Meta directly over TLS:5061 with the SIP digest credentials we captured at calling-enablement time). No client-side SDP is required; pass only &#x60;accountId&#x60; and &#x60;to&#x60;.  To send the consumer the call-consent prompt instead of placing a call, pass &#x60;action: \&quot;send_call_permission_request\&quot;&#x60; (+ optional &#x60;bodyText&#x60;). The consumer must tap Allow in WhatsApp before &#x60;start_call&#x60; is permitted; Meta limits the prompt to 1 per consumer per 24h (2 per 7 days) and requires an open 24h service window. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        InitiateWhatsAppCallRequest initiateWhatsAppCallRequest = new InitiateWhatsAppCallRequest(); // InitiateWhatsAppCallRequest | 
        try {
            InitiateWhatsAppCall200Response result = apiInstance.initiateWhatsAppCall(initiateWhatsAppCallRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#initiateWhatsAppCall");
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
| **initiateWhatsAppCallRequest** | [**InitiateWhatsAppCallRequest**](InitiateWhatsAppCallRequest.md)|  | |

### Return type

[**InitiateWhatsAppCall200Response**](InitiateWhatsAppCall200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call originated; lifecycle continues asynchronously via webhooks. |  -  |
| **401** | Unauthorized |  -  |
| **409** | No active call permission — send a permission request first. |  -  |
| **422** | Calling not enabled, BIC country blocked, or missing Meta SIP credentials |  -  |
| **502** | Telnyx-side originate failed; the Call doc has been marked failed. |  -  |

## initiateWhatsAppCallWithHttpInfo

> ApiResponse<InitiateWhatsAppCall200Response> initiateWhatsAppCall initiateWhatsAppCallWithHttpInfo(initiateWhatsAppCallRequest)

Initiate outbound call

Initiates an outbound Business-Initiated Call. The Telnyx-side SIP leg is originated server-side (Option B: SIP-first). Telnyx INVITEs Meta directly over TLS:5061 with the SIP digest credentials we captured at calling-enablement time). No client-side SDP is required; pass only &#x60;accountId&#x60; and &#x60;to&#x60;.  To send the consumer the call-consent prompt instead of placing a call, pass &#x60;action: \&quot;send_call_permission_request\&quot;&#x60; (+ optional &#x60;bodyText&#x60;). The consumer must tap Allow in WhatsApp before &#x60;start_call&#x60; is permitted; Meta limits the prompt to 1 per consumer per 24h (2 per 7 days) and requires an open 24h service window. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        InitiateWhatsAppCallRequest initiateWhatsAppCallRequest = new InitiateWhatsAppCallRequest(); // InitiateWhatsAppCallRequest | 
        try {
            ApiResponse<InitiateWhatsAppCall200Response> response = apiInstance.initiateWhatsAppCallWithHttpInfo(initiateWhatsAppCallRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#initiateWhatsAppCall");
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
| **initiateWhatsAppCallRequest** | [**InitiateWhatsAppCallRequest**](InitiateWhatsAppCallRequest.md)|  | |

### Return type

ApiResponse<[**InitiateWhatsAppCall200Response**](InitiateWhatsAppCall200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call originated; lifecycle continues asynchronously via webhooks. |  -  |
| **401** | Unauthorized |  -  |
| **409** | No active call permission — send a permission request first. |  -  |
| **422** | Calling not enabled, BIC country blocked, or missing Meta SIP credentials |  -  |
| **502** | Telnyx-side originate failed; the Call doc has been marked failed. |  -  |


## listWhatsAppCalls

> ListWhatsAppCalls200Response listWhatsAppCalls(accountId, status, direction, since, until, limit)

List call history for an account

Compact history listing for a single connected account. Results are scoped to the resolved SocialAccount; profile-scoped team members cannot read calls on sibling accounts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String status = "ringing"; // String | 
        String direction = "inbound"; // String | 
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime until = OffsetDateTime.now(); // OffsetDateTime | 
        Integer limit = 56; // Integer | 
        try {
            ListWhatsAppCalls200Response result = apiInstance.listWhatsAppCalls(accountId, status, direction, since, until, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#listWhatsAppCalls");
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
| **status** | **String**|  | [optional] [enum: ringing, answered, ended, failed] |
| **direction** | **String**|  | [optional] [enum: inbound, outbound] |
| **since** | **OffsetDateTime**|  | [optional] |
| **until** | **OffsetDateTime**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**ListWhatsAppCalls200Response**](ListWhatsAppCalls200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calls |  -  |
| **401** | Unauthorized |  -  |

## listWhatsAppCallsWithHttpInfo

> ApiResponse<ListWhatsAppCalls200Response> listWhatsAppCalls listWhatsAppCallsWithHttpInfo(accountId, status, direction, since, until, limit)

List call history for an account

Compact history listing for a single connected account. Results are scoped to the resolved SocialAccount; profile-scoped team members cannot read calls on sibling accounts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String status = "ringing"; // String | 
        String direction = "inbound"; // String | 
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime until = OffsetDateTime.now(); // OffsetDateTime | 
        Integer limit = 56; // Integer | 
        try {
            ApiResponse<ListWhatsAppCalls200Response> response = apiInstance.listWhatsAppCallsWithHttpInfo(accountId, status, direction, since, until, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#listWhatsAppCalls");
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
| **status** | **String**|  | [optional] [enum: ringing, answered, ended, failed] |
| **direction** | **String**|  | [optional] [enum: inbound, outbound] |
| **since** | **OffsetDateTime**|  | [optional] |
| **until** | **OffsetDateTime**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

ApiResponse<[**ListWhatsAppCalls200Response**](ListWhatsAppCalls200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calls |  -  |
| **401** | Unauthorized |  -  |


## updateWhatsAppCalling

> void updateWhatsAppCalling(id, updateWhatsAppCallingRequest)

Update calling config

Update fields on an already-enabled number. Only fields present in the body are written; &#x60;undefined&#x60; leaves the stored value alone, explicit &#x60;null&#x60; clears a nullable field. No Meta side effect, this only changes local routing state consumed by the Telnyx webhook handler. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String id = "id_example"; // String | 
        UpdateWhatsAppCallingRequest updateWhatsAppCallingRequest = new UpdateWhatsAppCallingRequest(); // UpdateWhatsAppCallingRequest | 
        try {
            apiInstance.updateWhatsAppCalling(id, updateWhatsAppCallingRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#updateWhatsAppCalling");
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
| **id** | **String**|  | |
| **updateWhatsAppCallingRequest** | [**UpdateWhatsAppCallingRequest**](UpdateWhatsAppCallingRequest.md)|  | |

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
| **200** | Updated |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found |  -  |
| **422** | Calling must be enabled before settings can be updated |  -  |

## updateWhatsAppCallingWithHttpInfo

> ApiResponse<Void> updateWhatsAppCalling updateWhatsAppCallingWithHttpInfo(id, updateWhatsAppCallingRequest)

Update calling config

Update fields on an already-enabled number. Only fields present in the body are written; &#x60;undefined&#x60; leaves the stored value alone, explicit &#x60;null&#x60; clears a nullable field. No Meta side effect, this only changes local routing state consumed by the Telnyx webhook handler. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppCallingApi apiInstance = new WhatsAppCallingApi(defaultClient);
        String id = "id_example"; // String | 
        UpdateWhatsAppCallingRequest updateWhatsAppCallingRequest = new UpdateWhatsAppCallingRequest(); // UpdateWhatsAppCallingRequest | 
        try {
            ApiResponse<Void> response = apiInstance.updateWhatsAppCallingWithHttpInfo(id, updateWhatsAppCallingRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppCallingApi#updateWhatsAppCalling");
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
| **id** | **String**|  | |
| **updateWhatsAppCallingRequest** | [**UpdateWhatsAppCallingRequest**](UpdateWhatsAppCallingRequest.md)|  | |

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
| **200** | Updated |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp phone number not found |  -  |
| **422** | Calling must be enabled before settings can be updated |  -  |

