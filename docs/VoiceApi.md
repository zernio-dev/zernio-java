# VoiceApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attachNumberToSipTrunk**](VoiceApi.md#attachNumberToSipTrunk) | **POST** /v1/phone-numbers/{id}/sip-trunk | Attach a number to a SIP trunk |
| [**attachNumberToSipTrunkWithHttpInfo**](VoiceApi.md#attachNumberToSipTrunkWithHttpInfo) | **POST** /v1/phone-numbers/{id}/sip-trunk | Attach a number to a SIP trunk |
| [**createSipTrunk**](VoiceApi.md#createSipTrunk) | **POST** /v1/phone-numbers/sip-trunks | Create a SIP trunk |
| [**createSipTrunkWithHttpInfo**](VoiceApi.md#createSipTrunkWithHttpInfo) | **POST** /v1/phone-numbers/sip-trunks | Create a SIP trunk |
| [**createVoiceCall**](VoiceApi.md#createVoiceCall) | **POST** /v1/voice/calls | Place an outbound phone call |
| [**createVoiceCallWithHttpInfo**](VoiceApi.md#createVoiceCallWithHttpInfo) | **POST** /v1/voice/calls | Place an outbound phone call |
| [**createVoiceWebSession**](VoiceApi.md#createVoiceWebSession) | **POST** /v1/voice/calls/web | Mint a browser softphone session |
| [**createVoiceWebSessionWithHttpInfo**](VoiceApi.md#createVoiceWebSessionWithHttpInfo) | **POST** /v1/voice/calls/web | Mint a browser softphone session |
| [**deleteSipTrunk**](VoiceApi.md#deleteSipTrunk) | **DELETE** /v1/phone-numbers/sip-trunks/{id} | Delete a SIP trunk |
| [**deleteSipTrunkWithHttpInfo**](VoiceApi.md#deleteSipTrunkWithHttpInfo) | **DELETE** /v1/phone-numbers/sip-trunks/{id} | Delete a SIP trunk |
| [**detachNumberFromSipTrunk**](VoiceApi.md#detachNumberFromSipTrunk) | **DELETE** /v1/phone-numbers/{id}/sip-trunk | Detach a number from its SIP trunk |
| [**detachNumberFromSipTrunkWithHttpInfo**](VoiceApi.md#detachNumberFromSipTrunkWithHttpInfo) | **DELETE** /v1/phone-numbers/{id}/sip-trunk | Detach a number from its SIP trunk |
| [**dialVoiceWebCall**](VoiceApi.md#dialVoiceWebCall) | **POST** /v1/voice/calls/web/dial | Dial from the browser softphone |
| [**dialVoiceWebCallWithHttpInfo**](VoiceApi.md#dialVoiceWebCallWithHttpInfo) | **POST** /v1/voice/calls/web/dial | Dial from the browser softphone |
| [**disableVoiceOnNumber**](VoiceApi.md#disableVoiceOnNumber) | **DELETE** /v1/phone-numbers/{id}/voice | Disable phone calling on a number |
| [**disableVoiceOnNumberWithHttpInfo**](VoiceApi.md#disableVoiceOnNumberWithHttpInfo) | **DELETE** /v1/phone-numbers/{id}/voice | Disable phone calling on a number |
| [**enableVoiceOnNumber**](VoiceApi.md#enableVoiceOnNumber) | **POST** /v1/phone-numbers/{id}/voice | Enable phone calling on a number |
| [**enableVoiceOnNumberWithHttpInfo**](VoiceApi.md#enableVoiceOnNumberWithHttpInfo) | **POST** /v1/phone-numbers/{id}/voice | Enable phone calling on a number |
| [**endVoiceCall**](VoiceApi.md#endVoiceCall) | **POST** /v1/voice/calls/{id}/end | Hang up a live call |
| [**endVoiceCallWithHttpInfo**](VoiceApi.md#endVoiceCallWithHttpInfo) | **POST** /v1/voice/calls/{id}/end | Hang up a live call |
| [**getSipTrunk**](VoiceApi.md#getSipTrunk) | **GET** /v1/phone-numbers/sip-trunks/{id} | Get a SIP trunk |
| [**getSipTrunkWithHttpInfo**](VoiceApi.md#getSipTrunkWithHttpInfo) | **GET** /v1/phone-numbers/sip-trunks/{id} | Get a SIP trunk |
| [**getVoiceCall**](VoiceApi.md#getVoiceCall) | **GET** /v1/voice/calls/{id} | Get a phone call |
| [**getVoiceCallWithHttpInfo**](VoiceApi.md#getVoiceCallWithHttpInfo) | **GET** /v1/voice/calls/{id} | Get a phone call |
| [**getVoiceCallEstimate**](VoiceApi.md#getVoiceCallEstimate) | **GET** /v1/voice/calls/estimate | Estimate call cost |
| [**getVoiceCallEstimateWithHttpInfo**](VoiceApi.md#getVoiceCallEstimateWithHttpInfo) | **GET** /v1/voice/calls/estimate | Estimate call cost |
| [**getVoiceCallRecording**](VoiceApi.md#getVoiceCallRecording) | **GET** /v1/voice/calls/{id}/recording | Get a call recording |
| [**getVoiceCallRecordingWithHttpInfo**](VoiceApi.md#getVoiceCallRecordingWithHttpInfo) | **GET** /v1/voice/calls/{id}/recording | Get a call recording |
| [**listSipTrunks**](VoiceApi.md#listSipTrunks) | **GET** /v1/phone-numbers/sip-trunks | List SIP trunks |
| [**listSipTrunksWithHttpInfo**](VoiceApi.md#listSipTrunksWithHttpInfo) | **GET** /v1/phone-numbers/sip-trunks | List SIP trunks |
| [**listVoiceCalls**](VoiceApi.md#listVoiceCalls) | **GET** /v1/voice/calls | List phone calls |
| [**listVoiceCallsWithHttpInfo**](VoiceApi.md#listVoiceCallsWithHttpInfo) | **GET** /v1/voice/calls | List phone calls |
| [**rotateSipTrunkCredentials**](VoiceApi.md#rotateSipTrunkCredentials) | **POST** /v1/phone-numbers/sip-trunks/{id}/rotate-credentials | Rotate a SIP trunk&#39;s password |
| [**rotateSipTrunkCredentialsWithHttpInfo**](VoiceApi.md#rotateSipTrunkCredentialsWithHttpInfo) | **POST** /v1/phone-numbers/sip-trunks/{id}/rotate-credentials | Rotate a SIP trunk&#39;s password |
| [**transferVoiceCall**](VoiceApi.md#transferVoiceCall) | **POST** /v1/voice/calls/{id}/transfer | Blind-transfer a live call |
| [**transferVoiceCallWithHttpInfo**](VoiceApi.md#transferVoiceCallWithHttpInfo) | **POST** /v1/voice/calls/{id}/transfer | Blind-transfer a live call |



## attachNumberToSipTrunk

> AttachNumberToSipTrunk200Response attachNumberToSipTrunk(id, attachNumberToSipTrunkRequest)

Attach a number to a SIP trunk

Routes the number&#39;s calls to the trunk: the external platform receives its inbound directly and can present it as outbound caller ID. While attached, Zernio-side voice features are off for this number (call forwarding, IVR, voicemail, recording, the softphone, and WhatsApp calling), so the number must have Calls and WhatsApp calling disabled before attaching. SMS and WhatsApp messaging are unaffected. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID (from GET /v1/phone-numbers).
        AttachNumberToSipTrunkRequest attachNumberToSipTrunkRequest = new AttachNumberToSipTrunkRequest(); // AttachNumberToSipTrunkRequest | 
        try {
            AttachNumberToSipTrunk200Response result = apiInstance.attachNumberToSipTrunk(id, attachNumberToSipTrunkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#attachNumberToSipTrunk");
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
| **id** | **String**| Phone number record ID (from GET /v1/phone-numbers). | |
| **attachNumberToSipTrunkRequest** | [**AttachNumberToSipTrunkRequest**](AttachNumberToSipTrunkRequest.md)|  | |

### Return type

[**AttachNumberToSipTrunk200Response**](AttachNumberToSipTrunk200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number attached (idempotent for the same trunk). |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | SIP trunking is not enabled for this workspace, or the workspace is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). |  -  |
| **404** | Number or trunk not found |  -  |
| **409** | The number still has Calls or WhatsApp calling enabled, is mid WhatsApp verification, is not active, or is attached to another trunk (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so it cannot be trunked. |  -  |

## attachNumberToSipTrunkWithHttpInfo

> ApiResponse<AttachNumberToSipTrunk200Response> attachNumberToSipTrunk attachNumberToSipTrunkWithHttpInfo(id, attachNumberToSipTrunkRequest)

Attach a number to a SIP trunk

Routes the number&#39;s calls to the trunk: the external platform receives its inbound directly and can present it as outbound caller ID. While attached, Zernio-side voice features are off for this number (call forwarding, IVR, voicemail, recording, the softphone, and WhatsApp calling), so the number must have Calls and WhatsApp calling disabled before attaching. SMS and WhatsApp messaging are unaffected. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID (from GET /v1/phone-numbers).
        AttachNumberToSipTrunkRequest attachNumberToSipTrunkRequest = new AttachNumberToSipTrunkRequest(); // AttachNumberToSipTrunkRequest | 
        try {
            ApiResponse<AttachNumberToSipTrunk200Response> response = apiInstance.attachNumberToSipTrunkWithHttpInfo(id, attachNumberToSipTrunkRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#attachNumberToSipTrunk");
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
| **id** | **String**| Phone number record ID (from GET /v1/phone-numbers). | |
| **attachNumberToSipTrunkRequest** | [**AttachNumberToSipTrunkRequest**](AttachNumberToSipTrunkRequest.md)|  | |

### Return type

ApiResponse<[**AttachNumberToSipTrunk200Response**](AttachNumberToSipTrunk200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number attached (idempotent for the same trunk). |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | SIP trunking is not enabled for this workspace, or the workspace is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). |  -  |
| **404** | Number or trunk not found |  -  |
| **409** | The number still has Calls or WhatsApp calling enabled, is mid WhatsApp verification, is not active, or is attached to another trunk (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so it cannot be trunked. |  -  |


## createSipTrunk

> CreateSipTrunk201Response createSipTrunk(createSipTrunkRequest)

Create a SIP trunk

Creates a SIP trunk an external voice platform (Retell, ElevenLabs, Vapi, or any SIP endpoint) can import your Zernio numbers into. The trunk carries both directions: inbound calls on attached numbers are delivered to &#x60;sipHost&#x60;, and the platform originates outbound calls through &#x60;termination.uri&#x60; with the digest credentials.  The &#x60;digestPassword&#x60; is returned only by this call (and by rotate-credentials); store it immediately. Attach any number of numbers to a trunk. Several trunks may point at the same host — each carries its own credentials and spend cap, so separate destination workspaces (e.g. an agency&#39;s clients) stay isolated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        CreateSipTrunkRequest createSipTrunkRequest = new CreateSipTrunkRequest(); // CreateSipTrunkRequest | 
        try {
            CreateSipTrunk201Response result = apiInstance.createSipTrunk(createSipTrunkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createSipTrunk");
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
| **createSipTrunkRequest** | [**CreateSipTrunkRequest**](CreateSipTrunkRequest.md)|  | |

### Return type

[**CreateSipTrunk201Response**](CreateSipTrunk201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Trunk created. The digest password is shown only here and on rotate. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | SIP trunking is not enabled for this workspace, or the workspace is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). |  -  |
| **409** | The workspace trunk limit was reached (code invalid_resource_state). |  -  |
| **422** | The host cannot be used as a trunk destination (e.g. a Zernio or carrier host). |  -  |

## createSipTrunkWithHttpInfo

> ApiResponse<CreateSipTrunk201Response> createSipTrunk createSipTrunkWithHttpInfo(createSipTrunkRequest)

Create a SIP trunk

Creates a SIP trunk an external voice platform (Retell, ElevenLabs, Vapi, or any SIP endpoint) can import your Zernio numbers into. The trunk carries both directions: inbound calls on attached numbers are delivered to &#x60;sipHost&#x60;, and the platform originates outbound calls through &#x60;termination.uri&#x60; with the digest credentials.  The &#x60;digestPassword&#x60; is returned only by this call (and by rotate-credentials); store it immediately. Attach any number of numbers to a trunk. Several trunks may point at the same host — each carries its own credentials and spend cap, so separate destination workspaces (e.g. an agency&#39;s clients) stay isolated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        CreateSipTrunkRequest createSipTrunkRequest = new CreateSipTrunkRequest(); // CreateSipTrunkRequest | 
        try {
            ApiResponse<CreateSipTrunk201Response> response = apiInstance.createSipTrunkWithHttpInfo(createSipTrunkRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createSipTrunk");
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
| **createSipTrunkRequest** | [**CreateSipTrunkRequest**](CreateSipTrunkRequest.md)|  | |

### Return type

ApiResponse<[**CreateSipTrunk201Response**](CreateSipTrunk201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Trunk created. The digest password is shown only here and on rotate. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | SIP trunking is not enabled for this workspace, or the workspace is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). |  -  |
| **409** | The workspace trunk limit was reached (code invalid_resource_state). |  -  |
| **422** | The host cannot be used as a trunk destination (e.g. a Zernio or carrier host). |  -  |


## createVoiceCall

> CreateVoiceCall200Response createVoiceCall(createVoiceCallRequest, idempotencyKey)

Place an outbound phone call

Dials &#x60;to&#x60; FROM one of your voice-enabled numbers and, on answer, bridges the callee to the number&#39;s stored forward destination, or to the per-call &#x60;forwardTo&#x60; override. Destinations can be your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. An optional &#x60;greeting&#x60; is spoken to the callee before the bridge.  The 200 response means the call is dialing; the lifecycle continues asynchronously (track it via &#x60;GET /v1/voice/calls/{id}&#x60; or the &#x60;call.*&#x60; webhooks). Outbound calls are capped per rolling hour (429 when hit).  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe; same key + same body replays the original response instead of dialing (and billing) a second call. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        CreateVoiceCallRequest createVoiceCallRequest = new CreateVoiceCallRequest(); // CreateVoiceCallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            CreateVoiceCall200Response result = apiInstance.createVoiceCall(createVoiceCallRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createVoiceCall");
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
| **createVoiceCallRequest** | [**CreateVoiceCallRequest**](CreateVoiceCallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**CreateVoiceCall200Response**](CreateVoiceCall200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call originated; lifecycle continues asynchronously. |  -  |
| **401** | Unauthorized |  -  |
| **422** | No voice-enabled number matches &#x60;fromNumber&#x60;, or no forward destination configured (set the number&#39;s forward or pass &#x60;forwardTo&#x60;). |  -  |
| **429** | Outbound call limit reached (per rolling hour). |  -  |
| **502** | Carrier-side originate failed; the call has been marked failed. |  -  |

## createVoiceCallWithHttpInfo

> ApiResponse<CreateVoiceCall200Response> createVoiceCall createVoiceCallWithHttpInfo(createVoiceCallRequest, idempotencyKey)

Place an outbound phone call

Dials &#x60;to&#x60; FROM one of your voice-enabled numbers and, on answer, bridges the callee to the number&#39;s stored forward destination, or to the per-call &#x60;forwardTo&#x60; override. Destinations can be your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. An optional &#x60;greeting&#x60; is spoken to the callee before the bridge.  The 200 response means the call is dialing; the lifecycle continues asynchronously (track it via &#x60;GET /v1/voice/calls/{id}&#x60; or the &#x60;call.*&#x60; webhooks). Outbound calls are capped per rolling hour (429 when hit).  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe; same key + same body replays the original response instead of dialing (and billing) a second call. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        CreateVoiceCallRequest createVoiceCallRequest = new CreateVoiceCallRequest(); // CreateVoiceCallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<CreateVoiceCall200Response> response = apiInstance.createVoiceCallWithHttpInfo(createVoiceCallRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createVoiceCall");
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
| **createVoiceCallRequest** | [**CreateVoiceCallRequest**](CreateVoiceCallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**CreateVoiceCall200Response**](CreateVoiceCall200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call originated; lifecycle continues asynchronously. |  -  |
| **401** | Unauthorized |  -  |
| **422** | No voice-enabled number matches &#x60;fromNumber&#x60;, or no forward destination configured (set the number&#39;s forward or pass &#x60;forwardTo&#x60;). |  -  |
| **429** | Outbound call limit reached (per rolling hour). |  -  |
| **502** | Carrier-side originate failed; the call has been marked failed. |  -  |


## createVoiceWebSession

> CreateVoiceWebSession200Response createVoiceWebSession()

Mint a browser softphone session

Step 1 of the two-step browser softphone handshake. Mints a WebRTC session (token + credential) the browser registers with the &#x60;@telnyx/webrtc&#x60; SDK. Once registered, call &#x60;POST /v1/voice/calls/web/dial&#x60; with the returned &#x60;credentialId&#x60; to place the call. The split avoids bridging to a browser that has not finished registering. The token lives ~1 hour (it must outlive the whole call, not just the handshake). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        try {
            CreateVoiceWebSession200Response result = apiInstance.createVoiceWebSession();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createVoiceWebSession");
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

[**CreateVoiceWebSession200Response**](CreateVoiceWebSession200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WebRTC session minted. |  -  |
| **401** | Unauthorized |  -  |
| **502** | Failed to mint the WebRTC session |  -  |

## createVoiceWebSessionWithHttpInfo

> ApiResponse<CreateVoiceWebSession200Response> createVoiceWebSession createVoiceWebSessionWithHttpInfo()

Mint a browser softphone session

Step 1 of the two-step browser softphone handshake. Mints a WebRTC session (token + credential) the browser registers with the &#x60;@telnyx/webrtc&#x60; SDK. Once registered, call &#x60;POST /v1/voice/calls/web/dial&#x60; with the returned &#x60;credentialId&#x60; to place the call. The split avoids bridging to a browser that has not finished registering. The token lives ~1 hour (it must outlive the whole call, not just the handshake). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        try {
            ApiResponse<CreateVoiceWebSession200Response> response = apiInstance.createVoiceWebSessionWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createVoiceWebSession");
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

ApiResponse<[**CreateVoiceWebSession200Response**](CreateVoiceWebSession200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WebRTC session minted. |  -  |
| **401** | Unauthorized |  -  |
| **502** | Failed to mint the WebRTC session |  -  |


## deleteSipTrunk

> DeleteSmsSenderId200Response deleteSipTrunk(id)

Delete a SIP trunk

Tears down the trunk and its carrier-side objects. Refused while any number is still attached: detach them first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            DeleteSmsSenderId200Response result = apiInstance.deleteSipTrunk(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#deleteSipTrunk");
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

[**DeleteSmsSenderId200Response**](DeleteSmsSenderId200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trunk deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | SIP trunk not found |  -  |
| **409** | Numbers are still attached to this trunk (code invalid_resource_state). |  -  |

## deleteSipTrunkWithHttpInfo

> ApiResponse<DeleteSmsSenderId200Response> deleteSipTrunk deleteSipTrunkWithHttpInfo(id)

Delete a SIP trunk

Tears down the trunk and its carrier-side objects. Refused while any number is still attached: detach them first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<DeleteSmsSenderId200Response> response = apiInstance.deleteSipTrunkWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#deleteSipTrunk");
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

ApiResponse<[**DeleteSmsSenderId200Response**](DeleteSmsSenderId200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trunk deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | SIP trunk not found |  -  |
| **409** | Numbers are still attached to this trunk (code invalid_resource_state). |  -  |


## detachNumberFromSipTrunk

> DetachNumberFromSipTrunk200Response detachNumberFromSipTrunk(id)

Detach a number from its SIP trunk

Returns the number&#39;s calls to Zernio routing. Idempotent when the number is not attached to any trunk. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            DetachNumberFromSipTrunk200Response result = apiInstance.detachNumberFromSipTrunk(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#detachNumberFromSipTrunk");
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

[**DetachNumberFromSipTrunk200Response**](DetachNumberFromSipTrunk200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number detached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |

## detachNumberFromSipTrunkWithHttpInfo

> ApiResponse<DetachNumberFromSipTrunk200Response> detachNumberFromSipTrunk detachNumberFromSipTrunkWithHttpInfo(id)

Detach a number from its SIP trunk

Returns the number&#39;s calls to Zernio routing. Idempotent when the number is not attached to any trunk. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<DetachNumberFromSipTrunk200Response> response = apiInstance.detachNumberFromSipTrunkWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#detachNumberFromSipTrunk");
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

ApiResponse<[**DetachNumberFromSipTrunk200Response**](DetachNumberFromSipTrunk200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number detached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |


## dialVoiceWebCall

> DialVoiceWebCall200Response dialVoiceWebCall(dialVoiceWebCallRequest)

Dial from the browser softphone

Step 2 of the browser softphone handshake: places an outbound call whose answered leg is bridged to the browser registered with the credential from &#x60;POST /v1/voice/calls/web&#x60;. The call runs through the normal outbound lane, so it is logged as outbound (from &#x3D; your number, to &#x3D; target) and recorded per the number&#39;s settings. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        DialVoiceWebCallRequest dialVoiceWebCallRequest = new DialVoiceWebCallRequest(); // DialVoiceWebCallRequest | 
        try {
            DialVoiceWebCall200Response result = apiInstance.dialVoiceWebCall(dialVoiceWebCallRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#dialVoiceWebCall");
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
| **dialVoiceWebCallRequest** | [**DialVoiceWebCallRequest**](DialVoiceWebCallRequest.md)|  | |

### Return type

[**DialVoiceWebCall200Response**](DialVoiceWebCall200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call originated; answer/bridge continue asynchronously. |  -  |
| **401** | Unauthorized |  -  |
| **422** | Invalid or unknown WebRTC credential, or no voice-enabled number matches &#x60;fromNumber&#x60; |  -  |
| **429** | Outbound call limit reached (per rolling hour). |  -  |
| **502** | Carrier-side originate failed |  -  |

## dialVoiceWebCallWithHttpInfo

> ApiResponse<DialVoiceWebCall200Response> dialVoiceWebCall dialVoiceWebCallWithHttpInfo(dialVoiceWebCallRequest)

Dial from the browser softphone

Step 2 of the browser softphone handshake: places an outbound call whose answered leg is bridged to the browser registered with the credential from &#x60;POST /v1/voice/calls/web&#x60;. The call runs through the normal outbound lane, so it is logged as outbound (from &#x3D; your number, to &#x3D; target) and recorded per the number&#39;s settings. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        DialVoiceWebCallRequest dialVoiceWebCallRequest = new DialVoiceWebCallRequest(); // DialVoiceWebCallRequest | 
        try {
            ApiResponse<DialVoiceWebCall200Response> response = apiInstance.dialVoiceWebCallWithHttpInfo(dialVoiceWebCallRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#dialVoiceWebCall");
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
| **dialVoiceWebCallRequest** | [**DialVoiceWebCallRequest**](DialVoiceWebCallRequest.md)|  | |

### Return type

ApiResponse<[**DialVoiceWebCall200Response**](DialVoiceWebCall200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Call originated; answer/bridge continue asynchronously. |  -  |
| **401** | Unauthorized |  -  |
| **422** | Invalid or unknown WebRTC credential, or no voice-enabled number matches &#x60;fromNumber&#x60; |  -  |
| **429** | Outbound call limit reached (per rolling hour). |  -  |
| **502** | Carrier-side originate failed |  -  |


## disableVoiceOnNumber

> DisableVoiceOnNumber200Response disableVoiceOnNumber(id)

Disable phone calling on a number

Turns off PSTN calling for the number. The stored forward destination and settings are preserved, so re-enabling restores the prior config. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            DisableVoiceOnNumber200Response result = apiInstance.disableVoiceOnNumber(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#disableVoiceOnNumber");
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

[**DisableVoiceOnNumber200Response**](DisableVoiceOnNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Voice disabled. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |

## disableVoiceOnNumberWithHttpInfo

> ApiResponse<DisableVoiceOnNumber200Response> disableVoiceOnNumber disableVoiceOnNumberWithHttpInfo(id)

Disable phone calling on a number

Turns off PSTN calling for the number. The stored forward destination and settings are preserved, so re-enabling restores the prior config. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<DisableVoiceOnNumber200Response> response = apiInstance.disableVoiceOnNumberWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#disableVoiceOnNumber");
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

ApiResponse<[**DisableVoiceOnNumber200Response**](DisableVoiceOnNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Voice disabled. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |


## enableVoiceOnNumber

> EnableVoiceOnNumber200Response enableVoiceOnNumber(id, enableVoiceOnNumberRequest)

Enable phone calling on a number

Turns on regular phone (PSTN) calling for one of your numbers and configures how inbound calls are handled. Inbound calls route to &#x60;forwardTo&#x60;: your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. Optional extras: voicemail, business-hours windows, an IVR menu, a caller blocklist, recording, and transcription. A number can also be voice-enabled with no forward (outbound-only).  Idempotent, and doubles as the settings update: only fields present in the body are written. Omitting &#x60;forwardTo&#x60; preserves the current destination; sending an empty string clears it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID (from GET /v1/phone-numbers).
        EnableVoiceOnNumberRequest enableVoiceOnNumberRequest = new EnableVoiceOnNumberRequest(); // EnableVoiceOnNumberRequest | 
        try {
            EnableVoiceOnNumber200Response result = apiInstance.enableVoiceOnNumber(id, enableVoiceOnNumberRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#enableVoiceOnNumber");
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
| **id** | **String**| Phone number record ID (from GET /v1/phone-numbers). | |
| **enableVoiceOnNumberRequest** | [**EnableVoiceOnNumberRequest**](EnableVoiceOnNumberRequest.md)|  | [optional] |

### Return type

[**EnableVoiceOnNumber200Response**](EnableVoiceOnNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Voice enabled; the full effective voice config is echoed back. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |
| **409** | This number is attached to a SIP trunk; detach it first (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so calls can&#39;t be enabled on it. |  -  |

## enableVoiceOnNumberWithHttpInfo

> ApiResponse<EnableVoiceOnNumber200Response> enableVoiceOnNumber enableVoiceOnNumberWithHttpInfo(id, enableVoiceOnNumberRequest)

Enable phone calling on a number

Turns on regular phone (PSTN) calling for one of your numbers and configures how inbound calls are handled. Inbound calls route to &#x60;forwardTo&#x60;: your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. Optional extras: voicemail, business-hours windows, an IVR menu, a caller blocklist, recording, and transcription. A number can also be voice-enabled with no forward (outbound-only).  Idempotent, and doubles as the settings update: only fields present in the body are written. Omitting &#x60;forwardTo&#x60; preserves the current destination; sending an empty string clears it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID (from GET /v1/phone-numbers).
        EnableVoiceOnNumberRequest enableVoiceOnNumberRequest = new EnableVoiceOnNumberRequest(); // EnableVoiceOnNumberRequest | 
        try {
            ApiResponse<EnableVoiceOnNumber200Response> response = apiInstance.enableVoiceOnNumberWithHttpInfo(id, enableVoiceOnNumberRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#enableVoiceOnNumber");
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
| **id** | **String**| Phone number record ID (from GET /v1/phone-numbers). | |
| **enableVoiceOnNumberRequest** | [**EnableVoiceOnNumberRequest**](EnableVoiceOnNumberRequest.md)|  | [optional] |

### Return type

ApiResponse<[**EnableVoiceOnNumber200Response**](EnableVoiceOnNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Voice enabled; the full effective voice config is echoed back. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |
| **409** | This number is attached to a SIP trunk; detach it first (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so calls can&#39;t be enabled on it. |  -  |


## endVoiceCall

> EndVoiceCall200Response endVoiceCall(id)

Hang up a live call

Hangs up a live call on demand. Idempotent: ending a call that already ended (or never connected) returns success with the call&#39;s current status. Final duration/cost are written asynchronously when the hangup event lands, so the call doc may briefly still show its prior status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            EndVoiceCall200Response result = apiInstance.endVoiceCall(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#endVoiceCall");
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

[**EndVoiceCall200Response**](EndVoiceCall200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hangup issued (or the call was already over). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Call not found |  -  |
| **502** | Carrier-side hangup failed |  -  |

## endVoiceCallWithHttpInfo

> ApiResponse<EndVoiceCall200Response> endVoiceCall endVoiceCallWithHttpInfo(id)

Hang up a live call

Hangs up a live call on demand. Idempotent: ending a call that already ended (or never connected) returns success with the call&#39;s current status. Final duration/cost are written asynchronously when the hangup event lands, so the call doc may briefly still show its prior status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<EndVoiceCall200Response> response = apiInstance.endVoiceCallWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#endVoiceCall");
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

ApiResponse<[**EndVoiceCall200Response**](EndVoiceCall200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hangup issued (or the call was already over). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Call not found |  -  |
| **502** | Carrier-side hangup failed |  -  |


## getSipTrunk

> GetSipTrunk200Response getSipTrunk(id)

Get a SIP trunk

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            GetSipTrunk200Response result = apiInstance.getSipTrunk(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getSipTrunk");
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

[**GetSipTrunk200Response**](GetSipTrunk200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trunk detail, including the attached numbers. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | SIP trunk not found |  -  |

## getSipTrunkWithHttpInfo

> ApiResponse<GetSipTrunk200Response> getSipTrunk getSipTrunkWithHttpInfo(id)

Get a SIP trunk

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<GetSipTrunk200Response> response = apiInstance.getSipTrunkWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getSipTrunk");
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

ApiResponse<[**GetSipTrunk200Response**](GetSipTrunk200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trunk detail, including the attached numbers. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | SIP trunk not found |  -  |


## getVoiceCall

> GetVoiceCall200Response getVoiceCall(id)

Get a phone call

Full call detail, including the transcript segments when transcription was on.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            GetVoiceCall200Response result = apiInstance.getVoiceCall(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getVoiceCall");
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

[**GetVoiceCall200Response**](GetVoiceCall200Response.md)


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

## getVoiceCallWithHttpInfo

> ApiResponse<GetVoiceCall200Response> getVoiceCall getVoiceCallWithHttpInfo(id)

Get a phone call

Full call detail, including the transcript segments when transcription was on.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<GetVoiceCall200Response> response = apiInstance.getVoiceCallWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getVoiceCall");
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

ApiResponse<[**GetVoiceCall200Response**](GetVoiceCall200Response.md)>


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


## getVoiceCallEstimate

> GetVoiceCallEstimate200Response getVoiceCallEstimate(to, minutes, recording, transcription)

Estimate call cost

Pre-call cost estimate for a PSTN call: the carrier leg plus optional recording and transcription add-ons. Same billing formula as the post-call invoice, so the quote and the final charge can&#39;t disagree. The per-minute figure is deliberately conservative (the real cost comes from the settled carrier record after the call), so estimates trend slightly over the actual invoice. Parity endpoint of &#x60;GET /v1/whatsapp/calls/estimate&#x60;, minus the Meta line (PSTN calls have no separate Meta bill, so &#x60;totalCostUSD&#x60; equals &#x60;billableCostUSD&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String to = "to_example"; // String | Destination number, E.164 (leading + optional).
        Integer minutes = 1; // Integer | 
        Boolean recording = true; // Boolean | 
        Boolean transcription = true; // Boolean | 
        try {
            GetVoiceCallEstimate200Response result = apiInstance.getVoiceCallEstimate(to, minutes, recording, transcription);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getVoiceCallEstimate");
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
| **to** | **String**| Destination number, E.164 (leading + optional). | |
| **minutes** | **Integer**|  | [optional] [default to 1] |
| **recording** | **Boolean**|  | [optional] |
| **transcription** | **Boolean**|  | [optional] |

### Return type

[**GetVoiceCallEstimate200Response**](GetVoiceCallEstimate200Response.md)


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

## getVoiceCallEstimateWithHttpInfo

> ApiResponse<GetVoiceCallEstimate200Response> getVoiceCallEstimate getVoiceCallEstimateWithHttpInfo(to, minutes, recording, transcription)

Estimate call cost

Pre-call cost estimate for a PSTN call: the carrier leg plus optional recording and transcription add-ons. Same billing formula as the post-call invoice, so the quote and the final charge can&#39;t disagree. The per-minute figure is deliberately conservative (the real cost comes from the settled carrier record after the call), so estimates trend slightly over the actual invoice. Parity endpoint of &#x60;GET /v1/whatsapp/calls/estimate&#x60;, minus the Meta line (PSTN calls have no separate Meta bill, so &#x60;totalCostUSD&#x60; equals &#x60;billableCostUSD&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String to = "to_example"; // String | Destination number, E.164 (leading + optional).
        Integer minutes = 1; // Integer | 
        Boolean recording = true; // Boolean | 
        Boolean transcription = true; // Boolean | 
        try {
            ApiResponse<GetVoiceCallEstimate200Response> response = apiInstance.getVoiceCallEstimateWithHttpInfo(to, minutes, recording, transcription);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getVoiceCallEstimate");
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
| **to** | **String**| Destination number, E.164 (leading + optional). | |
| **minutes** | **Integer**|  | [optional] [default to 1] |
| **recording** | **Boolean**|  | [optional] |
| **transcription** | **Boolean**|  | [optional] |

### Return type

ApiResponse<[**GetVoiceCallEstimate200Response**](GetVoiceCallEstimate200Response.md)>


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


## getVoiceCallRecording

> GetWhatsAppCallRecording200Response getVoiceCallRecording(id, as)

Get a call recording

Resolves a fresh, playable MP3 URL for the call&#39;s recording (provider-signed URLs expire ~10 minutes after signing, so this endpoint re-signs on demand). Default responds &#x60;302 Found&#x60; redirecting to the fresh URL; pass &#x60;as&#x3D;json&#x60; to receive &#x60;{ url }&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        String as = "json"; // String | `json` returns `{ url }` instead of a 302 redirect.
        try {
            GetWhatsAppCallRecording200Response result = apiInstance.getVoiceCallRecording(id, as);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getVoiceCallRecording");
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
| **404** | Call not found, or no recording is available for this call |  -  |
| **502** | Recording provider lookup failed |  -  |

## getVoiceCallRecordingWithHttpInfo

> ApiResponse<GetWhatsAppCallRecording200Response> getVoiceCallRecording getVoiceCallRecordingWithHttpInfo(id, as)

Get a call recording

Resolves a fresh, playable MP3 URL for the call&#39;s recording (provider-signed URLs expire ~10 minutes after signing, so this endpoint re-signs on demand). Default responds &#x60;302 Found&#x60; redirecting to the fresh URL; pass &#x60;as&#x3D;json&#x60; to receive &#x60;{ url }&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        String as = "json"; // String | `json` returns `{ url }` instead of a 302 redirect.
        try {
            ApiResponse<GetWhatsAppCallRecording200Response> response = apiInstance.getVoiceCallRecordingWithHttpInfo(id, as);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#getVoiceCallRecording");
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
| **404** | Call not found, or no recording is available for this call |  -  |
| **502** | Recording provider lookup failed |  -  |


## listSipTrunks

> ListSipTrunks200Response listSipTrunks()

List SIP trunks

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        try {
            ListSipTrunks200Response result = apiInstance.listSipTrunks();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#listSipTrunks");
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

[**ListSipTrunks200Response**](ListSipTrunks200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workspace&#39;s trunks. Passwords are never included. |  -  |
| **401** | Unauthorized |  -  |

## listSipTrunksWithHttpInfo

> ApiResponse<ListSipTrunks200Response> listSipTrunks listSipTrunksWithHttpInfo()

List SIP trunks

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        try {
            ApiResponse<ListSipTrunks200Response> response = apiInstance.listSipTrunksWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#listSipTrunks");
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

ApiResponse<[**ListSipTrunks200Response**](ListSipTrunks200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workspace&#39;s trunks. Passwords are never included. |  -  |
| **401** | Unauthorized |  -  |


## listVoiceCalls

> ListVoiceCalls200Response listVoiceCalls(status, direction, number, before, limit)

List phone calls

Your PSTN voice calls (inbound + outbound), newest first. Cursor pagination: pass the returned &#x60;nextCursor&#x60; as &#x60;before&#x60; for the next page. For a history that also includes WhatsApp calls, use &#x60;GET /v1/calls&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String status = "ringing"; // String | 
        String direction = "inbound"; // String | 
        String number = "number_example"; // String | Exact filter: calls involving this number (typically one of your DIDs). E.164, leading + optional.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
        Integer limit = 50; // Integer | 
        try {
            ListVoiceCalls200Response result = apiInstance.listVoiceCalls(status, direction, number, before, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#listVoiceCalls");
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
| **status** | **String**|  | [optional] [enum: ringing, answered, ended, failed] |
| **direction** | **String**|  | [optional] [enum: inbound, outbound] |
| **number** | **String**| Exact filter: calls involving this number (typically one of your DIDs). E.164, leading + optional. | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**ListVoiceCalls200Response**](ListVoiceCalls200Response.md)


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

## listVoiceCallsWithHttpInfo

> ApiResponse<ListVoiceCalls200Response> listVoiceCalls listVoiceCallsWithHttpInfo(status, direction, number, before, limit)

List phone calls

Your PSTN voice calls (inbound + outbound), newest first. Cursor pagination: pass the returned &#x60;nextCursor&#x60; as &#x60;before&#x60; for the next page. For a history that also includes WhatsApp calls, use &#x60;GET /v1/calls&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String status = "ringing"; // String | 
        String direction = "inbound"; // String | 
        String number = "number_example"; // String | Exact filter: calls involving this number (typically one of your DIDs). E.164, leading + optional.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
        Integer limit = 50; // Integer | 
        try {
            ApiResponse<ListVoiceCalls200Response> response = apiInstance.listVoiceCallsWithHttpInfo(status, direction, number, before, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#listVoiceCalls");
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
| **status** | **String**|  | [optional] [enum: ringing, answered, ended, failed] |
| **direction** | **String**|  | [optional] [enum: inbound, outbound] |
| **number** | **String**| Exact filter: calls involving this number (typically one of your DIDs). E.164, leading + optional. | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

ApiResponse<[**ListVoiceCalls200Response**](ListVoiceCalls200Response.md)>


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


## rotateSipTrunkCredentials

> RotateSipTrunkCredentials200Response rotateSipTrunkCredentials(id)

Rotate a SIP trunk&#39;s password

Mints a new digest password on the trunk. The old password stops working immediately, so update the destination platform right away. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            RotateSipTrunkCredentials200Response result = apiInstance.rotateSipTrunkCredentials(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#rotateSipTrunkCredentials");
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

[**RotateSipTrunkCredentials200Response**](RotateSipTrunkCredentials200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New credentials. The password is shown only here. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | SIP trunk not found |  -  |

## rotateSipTrunkCredentialsWithHttpInfo

> ApiResponse<RotateSipTrunkCredentials200Response> rotateSipTrunkCredentials rotateSipTrunkCredentialsWithHttpInfo(id)

Rotate a SIP trunk&#39;s password

Mints a new digest password on the trunk. The old password stops working immediately, so update the destination platform right away. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<RotateSipTrunkCredentials200Response> response = apiInstance.rotateSipTrunkCredentialsWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#rotateSipTrunkCredentials");
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

ApiResponse<[**RotateSipTrunkCredentials200Response**](RotateSipTrunkCredentials200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New credentials. The password is shown only here. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | SIP trunk not found |  -  |


## transferVoiceCall

> TransferVoiceCall200Response transferVoiceCall(id, transferVoiceCallRequest)

Blind-transfer a live call

Moves the call&#39;s current leg to a new destination (a phone number or a SIP endpoint). This is a BLIND transfer: control of the leg is handed off and the call ends normally when the transferred leg hangs up. The caller ID presented on the transfer leg is always your own number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        TransferVoiceCallRequest transferVoiceCallRequest = new TransferVoiceCallRequest(); // TransferVoiceCallRequest | 
        try {
            TransferVoiceCall200Response result = apiInstance.transferVoiceCall(id, transferVoiceCallRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#transferVoiceCall");
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
| **transferVoiceCallRequest** | [**TransferVoiceCallRequest**](TransferVoiceCallRequest.md)|  | |

### Return type

[**TransferVoiceCall200Response**](TransferVoiceCall200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transfer issued. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Call not found |  -  |
| **409** | Call is not connected yet, or has already ended |  -  |

## transferVoiceCallWithHttpInfo

> ApiResponse<TransferVoiceCall200Response> transferVoiceCall transferVoiceCallWithHttpInfo(id, transferVoiceCallRequest)

Blind-transfer a live call

Moves the call&#39;s current leg to a new destination (a phone number or a SIP endpoint). This is a BLIND transfer: control of the leg is handed off and the call ends normally when the transferred leg hangs up. The caller ID presented on the transfer leg is always your own number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VoiceApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VoiceApi apiInstance = new VoiceApi(defaultClient);
        String id = "id_example"; // String | 
        TransferVoiceCallRequest transferVoiceCallRequest = new TransferVoiceCallRequest(); // TransferVoiceCallRequest | 
        try {
            ApiResponse<TransferVoiceCall200Response> response = apiInstance.transferVoiceCallWithHttpInfo(id, transferVoiceCallRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#transferVoiceCall");
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
| **transferVoiceCallRequest** | [**TransferVoiceCallRequest**](TransferVoiceCallRequest.md)|  | |

### Return type

ApiResponse<[**TransferVoiceCall200Response**](TransferVoiceCall200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transfer issued. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Call not found |  -  |
| **409** | Call is not connected yet, or has already ended |  -  |

