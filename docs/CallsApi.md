# CallsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCall**](CallsApi.md#getCall) | **GET** /v1/calls/{id} | Get a call (any channel) |
| [**getCallWithHttpInfo**](CallsApi.md#getCallWithHttpInfo) | **GET** /v1/calls/{id} | Get a call (any channel) |
| [**getCallRecording**](CallsApi.md#getCallRecording) | **GET** /v1/calls/{id}/recording | Get a call recording (any channel) |
| [**getCallRecordingWithHttpInfo**](CallsApi.md#getCallRecordingWithHttpInfo) | **GET** /v1/calls/{id}/recording | Get a call recording (any channel) |
| [**listCalls**](CallsApi.md#listCalls) | **GET** /v1/calls | List all calls (unified history) |
| [**listCallsWithHttpInfo**](CallsApi.md#listCallsWithHttpInfo) | **GET** /v1/calls | List all calls (unified history) |



## getCall

> GetCall200Response getCall(id)

Get a call (any channel)

Channel-agnostic call detail: works for both WhatsApp and regular phone (PSTN) calls, so any row from &#x60;GET /v1/calls&#x60; can be opened without branching on &#x60;channel&#x60;. Returns the full call including transcript segments, with &#x60;contactId&#x60;/&#x60;contactName&#x60; set when the counterparty matches a CRM contact. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CallsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CallsApi apiInstance = new CallsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            GetCall200Response result = apiInstance.getCall(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CallsApi#getCall");
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

### Return type

[**GetCall200Response**](GetCall200Response.md)


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
| **403** | Not enrolled in the calling beta |  -  |
| **404** | Call not found |  -  |

## getCallWithHttpInfo

> ApiResponse<GetCall200Response> getCall getCallWithHttpInfo(id)

Get a call (any channel)

Channel-agnostic call detail: works for both WhatsApp and regular phone (PSTN) calls, so any row from &#x60;GET /v1/calls&#x60; can be opened without branching on &#x60;channel&#x60;. Returns the full call including transcript segments, with &#x60;contactId&#x60;/&#x60;contactName&#x60; set when the counterparty matches a CRM contact. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CallsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CallsApi apiInstance = new CallsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<GetCall200Response> response = apiInstance.getCallWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CallsApi#getCall");
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

### Return type

ApiResponse<[**GetCall200Response**](GetCall200Response.md)>


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
| **403** | Not enrolled in the calling beta |  -  |
| **404** | Call not found |  -  |


## getCallRecording

> GetWhatsAppCallRecording200Response getCallRecording(id, as)

Get a call recording (any channel)

Channel-agnostic recording fetch: resolves a fresh, playable MP3 URL for any call regardless of channel (provider-signed URLs expire ~10 minutes after signing, so this re-signs on demand). Default responds &#x60;302 Found&#x60; redirecting to the fresh URL; pass &#x60;as&#x3D;json&#x60; to receive &#x60;{ url }&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CallsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CallsApi apiInstance = new CallsApi(defaultClient);
        String id = "id_example"; // String | 
        String as = "json"; // String | `json` returns `{ url }` instead of a 302 redirect.
        try {
            GetWhatsAppCallRecording200Response result = apiInstance.getCallRecording(id, as);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CallsApi#getCallRecording");
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
| **as** | **String**| &#x60;json&#x60; returns &#x60;{ url }&#x60; instead of a 302 redirect. | [optional] [enum: json] |

### Return type

[**GetWhatsAppCallRecording200Response**](GetWhatsAppCallRecording200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to a freshly-signed recording URL. |  -  |
| **200** | Recording URL (&#x60;as&#x3D;json&#x60; only). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Not enrolled in the calling beta |  -  |
| **404** | Call not found, or no recording is available for this call |  -  |
| **502** | Recording provider lookup failed |  -  |

## getCallRecordingWithHttpInfo

> ApiResponse<GetWhatsAppCallRecording200Response> getCallRecording getCallRecordingWithHttpInfo(id, as)

Get a call recording (any channel)

Channel-agnostic recording fetch: resolves a fresh, playable MP3 URL for any call regardless of channel (provider-signed URLs expire ~10 minutes after signing, so this re-signs on demand). Default responds &#x60;302 Found&#x60; redirecting to the fresh URL; pass &#x60;as&#x3D;json&#x60; to receive &#x60;{ url }&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CallsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CallsApi apiInstance = new CallsApi(defaultClient);
        String id = "id_example"; // String | 
        String as = "json"; // String | `json` returns `{ url }` instead of a 302 redirect.
        try {
            ApiResponse<GetWhatsAppCallRecording200Response> response = apiInstance.getCallRecordingWithHttpInfo(id, as);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CallsApi#getCallRecording");
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
| **as** | **String**| &#x60;json&#x60; returns &#x60;{ url }&#x60; instead of a 302 redirect. | [optional] [enum: json] |

### Return type

ApiResponse<[**GetWhatsAppCallRecording200Response**](GetWhatsAppCallRecording200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to a freshly-signed recording URL. |  -  |
| **200** | Recording URL (&#x60;as&#x3D;json&#x60; only). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Not enrolled in the calling beta |  -  |
| **404** | Call not found, or no recording is available for this call |  -  |
| **502** | Recording provider lookup failed |  -  |


## listCalls

> ListCalls200Response listCalls(channel, status, direction, number, search, before, limit)

List all calls (unified history)

Unified call history across ALL of your numbers: both channels (WhatsApp Business Calling + regular phone/PSTN), inbound and outbound, newest first. Unlike &#x60;GET /v1/voice/calls&#x60; (PSTN-only) and &#x60;GET /v1/whatsapp/calls&#x60; (one account at a time), this endpoint needs no &#x60;accountId&#x60; and never requires fanning out one request per number.  Any row can be opened channel-agnostically via &#x60;GET /v1/calls/{id}&#x60; and &#x60;GET /v1/calls/{id}/recording&#x60;; no branching on &#x60;channel&#x60; needed. When the counterparty number matches a CRM contact, &#x60;contactId&#x60; and &#x60;contactName&#x60; are set.  Cursor pagination: pass the returned &#x60;nextCursor&#x60; as &#x60;before&#x60; to fetch the next page. &#x60;nextCursor&#x60; is null on the last page. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CallsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CallsApi apiInstance = new CallsApi(defaultClient);
        String channel = "whatsapp"; // String | 
        String status = "ringing"; // String | 
        String direction = "inbound"; // String | 
        String number = "number_example"; // String | Exact filter: calls involving this number (typically one of YOUR numbers, to scope history to a single line). E.164, leading + optional.
        String search = "search_example"; // String | Free-text match on the from/to numbers. Non-digits are stripped, so partial queries like `302` or `+1 302` work.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Return calls with startedAt strictly before this instant (use the previous page's nextCursor).
        Integer limit = 50; // Integer | 
        try {
            ListCalls200Response result = apiInstance.listCalls(channel, status, direction, number, search, before, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CallsApi#listCalls");
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
| **channel** | **String**|  | [optional] [enum: whatsapp, pstn] |
| **status** | **String**|  | [optional] [enum: ringing, answered, ended, failed] |
| **direction** | **String**|  | [optional] [enum: inbound, outbound] |
| **number** | **String**| Exact filter: calls involving this number (typically one of YOUR numbers, to scope history to a single line). E.164, leading + optional. | [optional] |
| **search** | **String**| Free-text match on the from/to numbers. Non-digits are stripped, so partial queries like &#x60;302&#x60; or &#x60;+1 302&#x60; work. | [optional] |
| **before** | **OffsetDateTime**| Return calls with startedAt strictly before this instant (use the previous page&#39;s nextCursor). | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**ListCalls200Response**](ListCalls200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calls, newest first |  -  |
| **401** | Unauthorized |  -  |
| **403** | Not enrolled in the calling beta |  -  |

## listCallsWithHttpInfo

> ApiResponse<ListCalls200Response> listCalls listCallsWithHttpInfo(channel, status, direction, number, search, before, limit)

List all calls (unified history)

Unified call history across ALL of your numbers: both channels (WhatsApp Business Calling + regular phone/PSTN), inbound and outbound, newest first. Unlike &#x60;GET /v1/voice/calls&#x60; (PSTN-only) and &#x60;GET /v1/whatsapp/calls&#x60; (one account at a time), this endpoint needs no &#x60;accountId&#x60; and never requires fanning out one request per number.  Any row can be opened channel-agnostically via &#x60;GET /v1/calls/{id}&#x60; and &#x60;GET /v1/calls/{id}/recording&#x60;; no branching on &#x60;channel&#x60; needed. When the counterparty number matches a CRM contact, &#x60;contactId&#x60; and &#x60;contactName&#x60; are set.  Cursor pagination: pass the returned &#x60;nextCursor&#x60; as &#x60;before&#x60; to fetch the next page. &#x60;nextCursor&#x60; is null on the last page. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CallsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CallsApi apiInstance = new CallsApi(defaultClient);
        String channel = "whatsapp"; // String | 
        String status = "ringing"; // String | 
        String direction = "inbound"; // String | 
        String number = "number_example"; // String | Exact filter: calls involving this number (typically one of YOUR numbers, to scope history to a single line). E.164, leading + optional.
        String search = "search_example"; // String | Free-text match on the from/to numbers. Non-digits are stripped, so partial queries like `302` or `+1 302` work.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Return calls with startedAt strictly before this instant (use the previous page's nextCursor).
        Integer limit = 50; // Integer | 
        try {
            ApiResponse<ListCalls200Response> response = apiInstance.listCallsWithHttpInfo(channel, status, direction, number, search, before, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CallsApi#listCalls");
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
| **channel** | **String**|  | [optional] [enum: whatsapp, pstn] |
| **status** | **String**|  | [optional] [enum: ringing, answered, ended, failed] |
| **direction** | **String**|  | [optional] [enum: inbound, outbound] |
| **number** | **String**| Exact filter: calls involving this number (typically one of YOUR numbers, to scope history to a single line). E.164, leading + optional. | [optional] |
| **search** | **String**| Free-text match on the from/to numbers. Non-digits are stripped, so partial queries like &#x60;302&#x60; or &#x60;+1 302&#x60; work. | [optional] |
| **before** | **OffsetDateTime**| Return calls with startedAt strictly before this instant (use the previous page&#39;s nextCursor). | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

ApiResponse<[**ListCalls200Response**](ListCalls200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Calls, newest first |  -  |
| **401** | Unauthorized |  -  |
| **403** | Not enrolled in the calling beta |  -  |

