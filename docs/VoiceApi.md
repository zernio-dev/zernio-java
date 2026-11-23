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
| [**createVoiceWebInboundSession**](VoiceApi.md#createVoiceWebInboundSession) | **POST** /v1/voice/calls/web/inbound | Register a browser to receive calls |
| [**createVoiceWebInboundSessionWithHttpInfo**](VoiceApi.md#createVoiceWebInboundSessionWithHttpInfo) | **POST** /v1/voice/calls/web/inbound | Register a browser to receive calls |
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

Routes the number&#39;s calls to the trunk. The external platform receives its inbound directly and can present it as outbound caller ID.  While attached, Zernio-side voice features are off for this number: call forwarding, IVR, voicemail, recording, the softphone, and WhatsApp calling. So the number must have Calls and WhatsApp calling disabled before attaching.  SMS and WhatsApp messaging are unaffected. 

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **200** | Number attached (idempotent for the same trunk). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The team is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). Move to usage-based billing to use SIP trunking. Also returned when the API key is scoped to profiles that do not include this number. |  -  |
| **404** | Number or trunk not found |  -  |
| **409** | The number still has Calls or WhatsApp calling enabled, is mid WhatsApp verification, is not active, or is attached to another trunk (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so it cannot be trunked. |  -  |

## attachNumberToSipTrunkWithHttpInfo

> ApiResponse<AttachNumberToSipTrunk200Response> attachNumberToSipTrunk attachNumberToSipTrunkWithHttpInfo(id, attachNumberToSipTrunkRequest)

Attach a number to a SIP trunk

Routes the number&#39;s calls to the trunk. The external platform receives its inbound directly and can present it as outbound caller ID.  While attached, Zernio-side voice features are off for this number: call forwarding, IVR, voicemail, recording, the softphone, and WhatsApp calling. So the number must have Calls and WhatsApp calling disabled before attaching.  SMS and WhatsApp messaging are unaffected. 

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **200** | Number attached (idempotent for the same trunk). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The team is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). Move to usage-based billing to use SIP trunking. Also returned when the API key is scoped to profiles that do not include this number. |  -  |
| **404** | Number or trunk not found |  -  |
| **409** | The number still has Calls or WhatsApp calling enabled, is mid WhatsApp verification, is not active, or is attached to another trunk (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so it cannot be trunked. |  -  |


## createSipTrunk

> CreateSipTrunk201Response createSipTrunk(createSipTrunkRequest)

Create a SIP trunk

Creates a SIP trunk an external voice platform (Retell, ElevenLabs, Vapi, or any SIP endpoint) can import your Zernio numbers into. The trunk carries both directions: inbound calls on attached numbers are delivered to &#x60;sipHost&#x60;, and the platform originates outbound calls through &#x60;termination.uri&#x60; with the digest credentials.  The &#x60;digestPassword&#x60; is returned only by this call (and by rotate-credentials); store it immediately. Attach any number of numbers to a trunk. Several trunks may point at the same host. Each carries its own credentials and spend cap, so separate destinations (e.g. an agency&#39;s clients) stay isolated. 

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **201** | Trunk created. The digest password is shown only here and on rotate. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The team is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). Move to usage-based billing to use SIP trunking. |  -  |
| **409** | The team trunk limit was reached (code invalid_resource_state). |  -  |
| **422** | The host cannot be used as a trunk destination (e.g. a Zernio or carrier host). |  -  |

## createSipTrunkWithHttpInfo

> ApiResponse<CreateSipTrunk201Response> createSipTrunk createSipTrunkWithHttpInfo(createSipTrunkRequest)

Create a SIP trunk

Creates a SIP trunk an external voice platform (Retell, ElevenLabs, Vapi, or any SIP endpoint) can import your Zernio numbers into. The trunk carries both directions: inbound calls on attached numbers are delivered to &#x60;sipHost&#x60;, and the platform originates outbound calls through &#x60;termination.uri&#x60; with the digest credentials.  The &#x60;digestPassword&#x60; is returned only by this call (and by rotate-credentials); store it immediately. Attach any number of numbers to a trunk. Several trunks may point at the same host. Each carries its own credentials and spend cap, so separate destinations (e.g. an agency&#39;s clients) stay isolated. 

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **201** | Trunk created. The digest password is shown only here and on rotate. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The team is on legacy (non-usage-based) billing, which cannot invoice trunk call costs (code feature_not_available). Move to usage-based billing to use SIP trunking. |  -  |
| **409** | The team trunk limit was reached (code invalid_resource_state). |  -  |
| **422** | The host cannot be used as a trunk destination (e.g. a Zernio or carrier host). |  -  |


## createVoiceCall

> CreateVoiceCall200Response createVoiceCall(createVoiceCallRequest, idempotencyKey)

Place an outbound phone call

Dials &#x60;to&#x60; FROM one of your voice-enabled numbers and, on answer, bridges the callee to the number&#39;s stored forward destination, or to the per-call &#x60;forwardTo&#x60; override.  Destinations can be your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. An optional &#x60;greeting&#x60; is spoken to the callee before the bridge.  ### Response and limits  The 200 response means the call is dialing. The lifecycle continues asynchronously: track it via &#x60;GET /v1/voice/calls/{id}&#x60; or the &#x60;call.*&#x60; webhooks.  Calls are not capped by count. Each team runs at most 10 calls at once (outbound calls plus calls forwarded to a phone) and has a daily safety limit on calling spend over the last 24 hours.  The profile of the calling number can set tighter limits of its own (&#x60;maxOutboundCallsPerHour&#x60;, &#x60;maxDailyCallSpendUsd&#x60; on the profile; see &#x60;GET /v1/profiles/{profileId}/limits&#x60;).  Past a limit the call is refused with 429 &#x60;call_limit_reached&#x60;, and &#x60;details.limit&#x60; names it.  ### Balance time limit  On balance billing a call runs only as long as the balance, plus what auto top-up can still add this month, funds at its per-minute price, minus calls already in progress. Then it ends with &#x60;hangup_cause: time_limit&#x60;. Under one minute is refused with 402.  ### Idempotency  Send an &#x60;Idempotency-Key&#x60; header to make retries safe. Same key + same body replays the original response instead of dialing (and billing) a second call. 

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **200** | Call originated; lifecycle continues asynchronously. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **422** | No voice-enabled number matches &#x60;fromNumber&#x60;, or no forward destination configured (set the number&#39;s forward or pass &#x60;forwardTo&#x60;). |  -  |
| **429** | A team or profile call limit was reached (&#x60;call_limit_reached&#x60;). &#x60;details.limit&#x60; names it: &#x60;team_concurrent_calls&#x60;, &#x60;team_daily_cost&#x60;, &#x60;profile_outbound_calls_per_hour&#x60;, &#x60;profile_daily_call_spend&#x60;, or &#x60;outbound_paused&#x60;. |  -  |
| **502** | Carrier-side originate failed; the call has been marked failed. |  -  |

## createVoiceCallWithHttpInfo

> ApiResponse<CreateVoiceCall200Response> createVoiceCall createVoiceCallWithHttpInfo(createVoiceCallRequest, idempotencyKey)

Place an outbound phone call

Dials &#x60;to&#x60; FROM one of your voice-enabled numbers and, on answer, bridges the callee to the number&#39;s stored forward destination, or to the per-call &#x60;forwardTo&#x60; override.  Destinations can be your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. An optional &#x60;greeting&#x60; is spoken to the callee before the bridge.  ### Response and limits  The 200 response means the call is dialing. The lifecycle continues asynchronously: track it via &#x60;GET /v1/voice/calls/{id}&#x60; or the &#x60;call.*&#x60; webhooks.  Calls are not capped by count. Each team runs at most 10 calls at once (outbound calls plus calls forwarded to a phone) and has a daily safety limit on calling spend over the last 24 hours.  The profile of the calling number can set tighter limits of its own (&#x60;maxOutboundCallsPerHour&#x60;, &#x60;maxDailyCallSpendUsd&#x60; on the profile; see &#x60;GET /v1/profiles/{profileId}/limits&#x60;).  Past a limit the call is refused with 429 &#x60;call_limit_reached&#x60;, and &#x60;details.limit&#x60; names it.  ### Balance time limit  On balance billing a call runs only as long as the balance, plus what auto top-up can still add this month, funds at its per-minute price, minus calls already in progress. Then it ends with &#x60;hangup_cause: time_limit&#x60;. Under one minute is refused with 402.  ### Idempotency  Send an &#x60;Idempotency-Key&#x60; header to make retries safe. Same key + same body replays the original response instead of dialing (and billing) a second call. 

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **200** | Call originated; lifecycle continues asynchronously. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **422** | No voice-enabled number matches &#x60;fromNumber&#x60;, or no forward destination configured (set the number&#39;s forward or pass &#x60;forwardTo&#x60;). |  -  |
| **429** | A team or profile call limit was reached (&#x60;call_limit_reached&#x60;). &#x60;details.limit&#x60; names it: &#x60;team_concurrent_calls&#x60;, &#x60;team_daily_cost&#x60;, &#x60;profile_outbound_calls_per_hour&#x60;, &#x60;profile_daily_call_spend&#x60;, or &#x60;outbound_paused&#x60;. |  -  |
| **502** | Carrier-side originate failed; the call has been marked failed. |  -  |


## createVoiceWebInboundSession

> CreateVoiceWebInboundSession200Response createVoiceWebInboundSession()

Register a browser to receive calls

Mints a login token for the &#x60;@telnyx/webrtc&#x60; SDK so a browser can receive inbound calls to numbers with &#x60;ringInBrowser&#x60; on.  The token belongs to one long-lived credential per number owner, so every registered tab (including teammates&#39; with calls access) rings together. Tokens last about 24 hours; request a new one to re-register.  Dashboard sessions only: API keys and connector tokens get &#x60;403&#x60;. Returns &#x60;{ enabled: false }&#x60; when none of the owner&#39;s numbers ring in the browser. 

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
            CreateVoiceWebInboundSession200Response result = apiInstance.createVoiceWebInboundSession();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createVoiceWebInboundSession");
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

[**CreateVoiceWebInboundSession200Response**](CreateVoiceWebInboundSession200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token minted, or browser ringing is off. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Not a dashboard session, or calls are turned off for this team member |  -  |
| **502** | Failed to mint the WebRTC token |  -  |

## createVoiceWebInboundSessionWithHttpInfo

> ApiResponse<CreateVoiceWebInboundSession200Response> createVoiceWebInboundSession createVoiceWebInboundSessionWithHttpInfo()

Register a browser to receive calls

Mints a login token for the &#x60;@telnyx/webrtc&#x60; SDK so a browser can receive inbound calls to numbers with &#x60;ringInBrowser&#x60; on.  The token belongs to one long-lived credential per number owner, so every registered tab (including teammates&#39; with calls access) rings together. Tokens last about 24 hours; request a new one to re-register.  Dashboard sessions only: API keys and connector tokens get &#x60;403&#x60;. Returns &#x60;{ enabled: false }&#x60; when none of the owner&#39;s numbers ring in the browser. 

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
            ApiResponse<CreateVoiceWebInboundSession200Response> response = apiInstance.createVoiceWebInboundSessionWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VoiceApi#createVoiceWebInboundSession");
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

ApiResponse<[**CreateVoiceWebInboundSession200Response**](CreateVoiceWebInboundSession200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token minted, or browser ringing is off. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Not a dashboard session, or calls are turned off for this team member |  -  |
| **502** | Failed to mint the WebRTC token |  -  |


## createVoiceWebSession

> CreateVoiceWebSession200Response createVoiceWebSession()

Mint a browser softphone session

Step 1 of the two-step browser softphone handshake. Mints a WebRTC session (token + credential) the browser registers with the &#x60;@telnyx/webrtc&#x60; SDK.  1. Call this endpoint and register the browser with the returned session. 2. Once registered, call &#x60;POST /v1/voice/calls/web/dial&#x60; with the returned &#x60;credentialId&#x60; to place the call.  The split avoids bridging to a browser that has not finished registering. The token lives ~1 hour (it must outlive the whole call, not only the handshake). 

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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **502** | Failed to mint the WebRTC session |  -  |

## createVoiceWebSessionWithHttpInfo

> ApiResponse<CreateVoiceWebSession200Response> createVoiceWebSession createVoiceWebSessionWithHttpInfo()

Mint a browser softphone session

Step 1 of the two-step browser softphone handshake. Mints a WebRTC session (token + credential) the browser registers with the &#x60;@telnyx/webrtc&#x60; SDK.  1. Call this endpoint and register the browser with the returned session. 2. Once registered, call &#x60;POST /v1/voice/calls/web/dial&#x60; with the returned &#x60;credentialId&#x60; to place the call.  The split avoids bridging to a browser that has not finished registering. The token lives ~1 hour (it must outlive the whole call, not only the handshake). 

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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **502** | Failed to mint the WebRTC session |  -  |


## deleteSipTrunk

> DeleteSipTrunk200Response deleteSipTrunk(id)

Delete a SIP trunk

Detaches every number still attached to the trunk (their inbound calls go back to Zernio calling), then tears down the trunk and its carrier-side objects. Its credentials stop working immediately. 

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
            DeleteSipTrunk200Response result = apiInstance.deleteSipTrunk(id);
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

[**DeleteSipTrunk200Response**](DeleteSipTrunk200Response.md)


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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | SIP trunk not found |  -  |

## deleteSipTrunkWithHttpInfo

> ApiResponse<DeleteSipTrunk200Response> deleteSipTrunk deleteSipTrunkWithHttpInfo(id)

Delete a SIP trunk

Detaches every number still attached to the trunk (their inbound calls go back to Zernio calling), then tears down the trunk and its carrier-side objects. Its credentials stop working immediately. 

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
            ApiResponse<DeleteSipTrunk200Response> response = apiInstance.deleteSipTrunkWithHttpInfo(id);
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

ApiResponse<[**DeleteSipTrunk200Response**](DeleteSipTrunk200Response.md)>


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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | SIP trunk not found |  -  |


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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is scoped to profiles that do not include this number. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is scoped to profiles that do not include this number. |  -  |
| **404** | Number not found |  -  |


## dialVoiceWebCall

> DialVoiceWebCall200Response dialVoiceWebCall(dialVoiceWebCallRequest)

Dial from the browser softphone

Step 2 of the browser softphone handshake: rings the browser registered with the credential from &#x60;POST /v1/voice/calls/web&#x60; first, and dials the target only once the browser answers.  The callee&#39;s pickup then connects immediately, with no ringing after they answer.  - The call is logged as outbound (from &#x3D; your number, to &#x3D; target) and recorded per the number&#39;s settings. - &#x60;ringTimeoutSeconds&#x60; applies to the target&#39;s phone, not to the browser. - On balance billing the call gets the same time limit as &#x60;POST /v1/voice/calls&#x60;. 

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **200** | Call originated; answer/bridge continue asynchronously. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **422** | Invalid or unknown WebRTC credential, or no voice-enabled number matches &#x60;fromNumber&#x60; |  -  |
| **429** | A team or profile call limit was reached (&#x60;call_limit_reached&#x60;). &#x60;details.limit&#x60; names it: &#x60;team_concurrent_calls&#x60;, &#x60;team_daily_cost&#x60;, &#x60;profile_outbound_calls_per_hour&#x60;, &#x60;profile_daily_call_spend&#x60;, or &#x60;outbound_paused&#x60;. |  -  |
| **502** | Carrier-side originate failed |  -  |

## dialVoiceWebCallWithHttpInfo

> ApiResponse<DialVoiceWebCall200Response> dialVoiceWebCall dialVoiceWebCallWithHttpInfo(dialVoiceWebCallRequest)

Dial from the browser softphone

Step 2 of the browser softphone handshake: rings the browser registered with the credential from &#x60;POST /v1/voice/calls/web&#x60; first, and dials the target only once the browser answers.  The callee&#39;s pickup then connects immediately, with no ringing after they answer.  - The call is logged as outbound (from &#x3D; your number, to &#x3D; target) and recorded per the number&#39;s settings. - &#x60;ringTimeoutSeconds&#x60; applies to the target&#39;s phone, not to the browser. - On balance billing the call gets the same time limit as &#x60;POST /v1/voice/calls&#x60;. 

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
| **402** | Balance billing only. The balance is at or below $0 and auto top-up could not lift it, so new pay-per-use is refused.  - &#x60;insufficient_balance&#x60;: the balance is empty, or it cannot hold an order&#39;s fees billed later plus those still owed by orders awaiting approval, while auto top-up cannot refill it (off, no card, or past its monthly limit). - The message says how much to add; &#x60;required_cents&#x60; is what the balance must hold. Later fees: a number&#39;s first month, an RCS agent&#39;s fees up to launch, an iMessage sender&#39;s or caller identity&#39;s first month, 10DLC fees. - &#x60;usage_limit_reached&#x60;: the monthly limit kept it there. - On a call start, &#x60;insufficient_balance&#x60; also means the balance, plus what auto top-up can still add this month, cannot fund one minute of the call; &#x60;required_cents&#x60; is what the balance must hold.  &#x60;funding_url&#x60; opens Billing with the Add funds drawer (the add-card drawer first when there is no card). Inbound traffic and connected calls are never refused.  |  -  |
| **200** | Call originated; answer/bridge continue asynchronously. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **422** | Invalid or unknown WebRTC credential, or no voice-enabled number matches &#x60;fromNumber&#x60; |  -  |
| **429** | A team or profile call limit was reached (&#x60;call_limit_reached&#x60;). &#x60;details.limit&#x60; names it: &#x60;team_concurrent_calls&#x60;, &#x60;team_daily_cost&#x60;, &#x60;profile_outbound_calls_per_hour&#x60;, &#x60;profile_daily_call_spend&#x60;, or &#x60;outbound_paused&#x60;. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is scoped to profiles that do not include this number. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is scoped to profiles that do not include this number. |  -  |
| **404** | Number not found |  -  |


## enableVoiceOnNumber

> EnableVoiceOnNumber200Response enableVoiceOnNumber(id, enableVoiceOnNumberRequest)

Enable phone calling on a number

Turns on regular phone (PSTN) calling for one of your numbers and configures how inbound calls are handled.  Inbound calls route to &#x60;forwardTo&#x60;: your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. A number can also be voice-enabled with no forward (outbound-only).  Optional extras: voicemail, business-hours windows, an IVR menu, a caller blocklist, recording, and transcription.  ### Updating settings  Idempotent, and doubles as the settings update: only fields present in the body are written.  - Omitting &#x60;forwardTo&#x60; preserves the current destination. - Sending an empty string clears it. 

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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is scoped to profiles that do not include this number. |  -  |
| **404** | Number not found |  -  |
| **409** | This number is attached to a SIP trunk (detach it first), or it is a Zernio number that is not active yet or was released (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so calls can&#39;t be enabled on it. |  -  |

## enableVoiceOnNumberWithHttpInfo

> ApiResponse<EnableVoiceOnNumber200Response> enableVoiceOnNumber enableVoiceOnNumberWithHttpInfo(id, enableVoiceOnNumberRequest)

Enable phone calling on a number

Turns on regular phone (PSTN) calling for one of your numbers and configures how inbound calls are handled.  Inbound calls route to &#x60;forwardTo&#x60;: your own AI voice agent (Vapi/Retell), a phone, or a SIP endpoint. A number can also be voice-enabled with no forward (outbound-only).  Optional extras: voicemail, business-hours windows, an IVR menu, a caller blocklist, recording, and transcription.  ### Updating settings  Idempotent, and doubles as the settings update: only fields present in the body are written.  - Omitting &#x60;forwardTo&#x60; preserves the current destination. - Sending an empty string clears it. 

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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is scoped to profiles that do not include this number. |  -  |
| **404** | Number not found |  -  |
| **409** | This number is attached to a SIP trunk (detach it first), or it is a Zernio number that is not active yet or was released (code invalid_resource_state). |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so calls can&#39;t be enabled on it. |  -  |


## endVoiceCall

> EndVoiceCall200Response endVoiceCall(id)

Hang up a live call

Hangs up a live call on demand, including an outbound call that is still ringing and has not been answered yet (the callee stops ringing immediately).  ### Supported calls  - PSTN calls. - WhatsApp calls: the &#x60;callId&#x60; returned by &#x60;POST /v1/whatsapp/calls&#x60;, or an inbound WhatsApp call id.  A WhatsApp call forwarded to a &#x60;wss://&#x60; destination also ends automatically when that WebSocket closes.  ### Idempotency and timing  Idempotent: ending a call that already ended (or never connected) returns success with the call&#39;s current status.  Final duration/cost are written asynchronously when the hangup event lands, so the call doc may briefly still show its prior status. 

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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Call not found |  -  |
| **502** | Carrier-side hangup failed |  -  |

## endVoiceCallWithHttpInfo

> ApiResponse<EndVoiceCall200Response> endVoiceCall endVoiceCallWithHttpInfo(id)

Hang up a live call

Hangs up a live call on demand, including an outbound call that is still ringing and has not been answered yet (the callee stops ringing immediately).  ### Supported calls  - PSTN calls. - WhatsApp calls: the &#x60;callId&#x60; returned by &#x60;POST /v1/whatsapp/calls&#x60;, or an inbound WhatsApp call id.  A WhatsApp call forwarded to a &#x60;wss://&#x60; destination also ends automatically when that WebSocket closes.  ### Idempotency and timing  Idempotent: ending a call that already ended (or never connected) returns success with the call&#39;s current status.  Final duration/cost are written asynchronously when the hangup event lands, so the call doc may briefly still show its prior status. 

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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Call not found |  -  |


## getVoiceCallEstimate

> GetVoiceCallEstimate200Response getVoiceCallEstimate(to, from, fromNumberId, trunkId, via, forwardTo, minutes, recording, transcription)

Estimate call cost

Pre-call cost estimate for an outbound phone call, placed through the Voice API or through a [SIP trunk](/platforms/voice/integrations/elevenlabs).  Rates come from the carrier&#39;s live price list. The carrier prices a route by the caller ID, so pass the number you will call from (&#x60;from&#x60; or &#x60;fromNumberId&#x60;).  - **Caller-ID rates.** A caller in the destination country gets local rates. EEA callers get cheaper rates to EEA destinations, and some caller prefixes pay a surcharge. &#x60;rates.*.origination&#x60; names the band used. - **Mobile and landline.** &#x60;rates.mobile&#x60; and &#x60;rates.landline&#x60; are quoted separately, with every network the carrier lists. &#x60;lineType&#x60; says which one &#x60;to&#x60; is, and &#x60;perMinuteUsd&#x60; follows it. - **Trunk or Voice API.** Trunk calls bill twice the carrier rate. Voice API calls add a $0.002/min call-control fee before the markup, plus optional forward, recording and transcription legs.  &#x60;via&#x60; defaults to &#x60;trunk&#x60; when the caller number is attached to a SIP trunk (or &#x60;trunkId&#x60; is passed), and to &#x60;voice&#x60; otherwise. For trunk calls, &#x60;trunk&#x60; reports whether the trunk&#39;s limits would refuse the call.  &#x60;trunk.maxDestinationRateUsd&#x60; is compared with the carrier&#39;s rate for the route, which is half the billed rate. Isle of Man, Jersey and Guernsey numbers on +44 count as their own countries for the whitelist.  The dialed network cannot be known from the number, so the invoice can differ within the &#x60;minPerMinuteUsd&#x60; to &#x60;maxPerMinuteUsd&#x60; range. The real cost comes from the settled carrier record after the call.  PSTN calls have no separate Meta bill, so &#x60;totalCostUSD&#x60; equals &#x60;billableCostUSD&#x60;. 

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
        String from = "from_example"; // String | Caller ID the call would present, E.164. Picks the carrier's caller-ID rates, and prices a trunk call when the number is attached to a SIP trunk. A verified Branded Calling number calling the US adds the per-call surcharge.
        String fromNumberId = "fromNumberId_example"; // String | Id of one of your numbers to use as the caller ID, instead of `from`.
        String trunkId = "trunkId_example"; // String | SIP trunk the call goes through. Prices it as a trunk call and checks that trunk's limits. Without `from`, a number attached to the trunk is the caller ID.
        String via = "trunk"; // String | Force trunk or Voice API pricing. Defaults from the caller number, see above. `trunk` without a caller ID quotes the dearest caller band.
        String forwardTo = "forwardTo_example"; // String | Voice API only. Destination the call bridges to: `tel:+E164`, `sip:...` or `wss://...`. Defaults to the dialing number's configured forward. A `tel:` destination adds a second carrier leg to the quote. Encode the `+` as `%2B`.
        Integer minutes = 1; // Integer | 
        Boolean recording = true; // Boolean | Voice API only.
        Boolean transcription = true; // Boolean | Voice API only.
        try {
            GetVoiceCallEstimate200Response result = apiInstance.getVoiceCallEstimate(to, from, fromNumberId, trunkId, via, forwardTo, minutes, recording, transcription);
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
| **from** | **String**| Caller ID the call would present, E.164. Picks the carrier&#39;s caller-ID rates, and prices a trunk call when the number is attached to a SIP trunk. A verified Branded Calling number calling the US adds the per-call surcharge. | [optional] |
| **fromNumberId** | **String**| Id of one of your numbers to use as the caller ID, instead of &#x60;from&#x60;. | [optional] |
| **trunkId** | **String**| SIP trunk the call goes through. Prices it as a trunk call and checks that trunk&#39;s limits. Without &#x60;from&#x60;, a number attached to the trunk is the caller ID. | [optional] |
| **via** | **String**| Force trunk or Voice API pricing. Defaults from the caller number, see above. &#x60;trunk&#x60; without a caller ID quotes the dearest caller band. | [optional] [enum: trunk, voice] |
| **forwardTo** | **String**| Voice API only. Destination the call bridges to: &#x60;tel:+E164&#x60;, &#x60;sip:...&#x60; or &#x60;wss://...&#x60;. Defaults to the dialing number&#39;s configured forward. A &#x60;tel:&#x60; destination adds a second carrier leg to the quote. Encode the &#x60;+&#x60; as &#x60;%2B&#x60;. | [optional] |
| **minutes** | **Integer**|  | [optional] [default to 1] |
| **recording** | **Boolean**| Voice API only. | [optional] |
| **transcription** | **Boolean**| Voice API only. | [optional] |

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
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **503** | The carrier price list is unavailable. Retry shortly. |  -  |

## getVoiceCallEstimateWithHttpInfo

> ApiResponse<GetVoiceCallEstimate200Response> getVoiceCallEstimate getVoiceCallEstimateWithHttpInfo(to, from, fromNumberId, trunkId, via, forwardTo, minutes, recording, transcription)

Estimate call cost

Pre-call cost estimate for an outbound phone call, placed through the Voice API or through a [SIP trunk](/platforms/voice/integrations/elevenlabs).  Rates come from the carrier&#39;s live price list. The carrier prices a route by the caller ID, so pass the number you will call from (&#x60;from&#x60; or &#x60;fromNumberId&#x60;).  - **Caller-ID rates.** A caller in the destination country gets local rates. EEA callers get cheaper rates to EEA destinations, and some caller prefixes pay a surcharge. &#x60;rates.*.origination&#x60; names the band used. - **Mobile and landline.** &#x60;rates.mobile&#x60; and &#x60;rates.landline&#x60; are quoted separately, with every network the carrier lists. &#x60;lineType&#x60; says which one &#x60;to&#x60; is, and &#x60;perMinuteUsd&#x60; follows it. - **Trunk or Voice API.** Trunk calls bill twice the carrier rate. Voice API calls add a $0.002/min call-control fee before the markup, plus optional forward, recording and transcription legs.  &#x60;via&#x60; defaults to &#x60;trunk&#x60; when the caller number is attached to a SIP trunk (or &#x60;trunkId&#x60; is passed), and to &#x60;voice&#x60; otherwise. For trunk calls, &#x60;trunk&#x60; reports whether the trunk&#39;s limits would refuse the call.  &#x60;trunk.maxDestinationRateUsd&#x60; is compared with the carrier&#39;s rate for the route, which is half the billed rate. Isle of Man, Jersey and Guernsey numbers on +44 count as their own countries for the whitelist.  The dialed network cannot be known from the number, so the invoice can differ within the &#x60;minPerMinuteUsd&#x60; to &#x60;maxPerMinuteUsd&#x60; range. The real cost comes from the settled carrier record after the call.  PSTN calls have no separate Meta bill, so &#x60;totalCostUSD&#x60; equals &#x60;billableCostUSD&#x60;. 

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
        String from = "from_example"; // String | Caller ID the call would present, E.164. Picks the carrier's caller-ID rates, and prices a trunk call when the number is attached to a SIP trunk. A verified Branded Calling number calling the US adds the per-call surcharge.
        String fromNumberId = "fromNumberId_example"; // String | Id of one of your numbers to use as the caller ID, instead of `from`.
        String trunkId = "trunkId_example"; // String | SIP trunk the call goes through. Prices it as a trunk call and checks that trunk's limits. Without `from`, a number attached to the trunk is the caller ID.
        String via = "trunk"; // String | Force trunk or Voice API pricing. Defaults from the caller number, see above. `trunk` without a caller ID quotes the dearest caller band.
        String forwardTo = "forwardTo_example"; // String | Voice API only. Destination the call bridges to: `tel:+E164`, `sip:...` or `wss://...`. Defaults to the dialing number's configured forward. A `tel:` destination adds a second carrier leg to the quote. Encode the `+` as `%2B`.
        Integer minutes = 1; // Integer | 
        Boolean recording = true; // Boolean | Voice API only.
        Boolean transcription = true; // Boolean | Voice API only.
        try {
            ApiResponse<GetVoiceCallEstimate200Response> response = apiInstance.getVoiceCallEstimateWithHttpInfo(to, from, fromNumberId, trunkId, via, forwardTo, minutes, recording, transcription);
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
| **from** | **String**| Caller ID the call would present, E.164. Picks the carrier&#39;s caller-ID rates, and prices a trunk call when the number is attached to a SIP trunk. A verified Branded Calling number calling the US adds the per-call surcharge. | [optional] |
| **fromNumberId** | **String**| Id of one of your numbers to use as the caller ID, instead of &#x60;from&#x60;. | [optional] |
| **trunkId** | **String**| SIP trunk the call goes through. Prices it as a trunk call and checks that trunk&#39;s limits. Without &#x60;from&#x60;, a number attached to the trunk is the caller ID. | [optional] |
| **via** | **String**| Force trunk or Voice API pricing. Defaults from the caller number, see above. &#x60;trunk&#x60; without a caller ID quotes the dearest caller band. | [optional] [enum: trunk, voice] |
| **forwardTo** | **String**| Voice API only. Destination the call bridges to: &#x60;tel:+E164&#x60;, &#x60;sip:...&#x60; or &#x60;wss://...&#x60;. Defaults to the dialing number&#39;s configured forward. A &#x60;tel:&#x60; destination adds a second carrier leg to the quote. Encode the &#x60;+&#x60; as &#x60;%2B&#x60;. | [optional] |
| **minutes** | **Integer**|  | [optional] [default to 1] |
| **recording** | **Boolean**| Voice API only. | [optional] |
| **transcription** | **Boolean**| Voice API only. | [optional] |

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
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **503** | The carrier price list is unavailable. Retry shortly. |  -  |


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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Call not found, or no recording is available for this call. A team that does not retain content gets 404 on the redirect form and &#x60;{ url: null, contentNotRetained: true }&#x60; with JSON. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Call not found, or no recording is available for this call. A team that does not retain content gets 404 on the redirect form and &#x60;{ url: null, contentNotRetained: true }&#x60; with JSON. |  -  |
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
| **200** | The team&#39;s trunks. Passwords are never included. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

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
| **200** | The team&#39;s trunks. Passwords are never included. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## listVoiceCalls

> ListVoiceCalls200Response listVoiceCalls(status, direction, number, before, limit, profileId, externalId)

List phone calls

Your PSTN voice calls (inbound + outbound), newest first. Cursor pagination: pass the returned &#x60;nextCursor&#x60; as &#x60;before&#x60; for the next page. For a history that also includes WhatsApp calls, use &#x60;GET /v1/calls&#x60;.  &#x60;profileId&#x60; or &#x60;externalId&#x60; lists one profile&#39;s calls: a call belongs to the profile of the account (number) it was placed on.  A profile-scoped API key or member only ever lists its own profiles&#39; calls, with or without a filter (since 1.630.0). Full-access keys and sessions list the whole team&#39;s. 

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
        String profileId = "profileId_example"; // String | Only calls of this profile. Mutually exclusive with `externalId`. 404 when the profile is not in your team or outside a scoped key's profiles.
        String externalId = "externalId_example"; // String | Same as `profileId`, naming the profile by the `externalId` you set on it. 404 when none of your visible profiles carries it; 400 when two of them do.
        try {
            ListVoiceCalls200Response result = apiInstance.listVoiceCalls(status, direction, number, before, limit, profileId, externalId);
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
| **profileId** | **String**| Only calls of this profile. Mutually exclusive with &#x60;externalId&#x60;. 404 when the profile is not in your team or outside a scoped key&#39;s profiles. | [optional] |
| **externalId** | **String**| Same as &#x60;profileId&#x60;, naming the profile by the &#x60;externalId&#x60; you set on it. 404 when none of your visible profiles carries it; 400 when two of them do. | [optional] |

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
| **400** | Invalid query parameter, &#x60;profileId&#x60; together with &#x60;externalId&#x60;, or an &#x60;externalId&#x60; shared by two of your profiles. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The profile named by &#x60;profileId&#x60; / &#x60;externalId&#x60; is not visible to the caller. |  -  |

## listVoiceCallsWithHttpInfo

> ApiResponse<ListVoiceCalls200Response> listVoiceCalls listVoiceCallsWithHttpInfo(status, direction, number, before, limit, profileId, externalId)

List phone calls

Your PSTN voice calls (inbound + outbound), newest first. Cursor pagination: pass the returned &#x60;nextCursor&#x60; as &#x60;before&#x60; for the next page. For a history that also includes WhatsApp calls, use &#x60;GET /v1/calls&#x60;.  &#x60;profileId&#x60; or &#x60;externalId&#x60; lists one profile&#39;s calls: a call belongs to the profile of the account (number) it was placed on.  A profile-scoped API key or member only ever lists its own profiles&#39; calls, with or without a filter (since 1.630.0). Full-access keys and sessions list the whole team&#39;s. 

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
        String profileId = "profileId_example"; // String | Only calls of this profile. Mutually exclusive with `externalId`. 404 when the profile is not in your team or outside a scoped key's profiles.
        String externalId = "externalId_example"; // String | Same as `profileId`, naming the profile by the `externalId` you set on it. 404 when none of your visible profiles carries it; 400 when two of them do.
        try {
            ApiResponse<ListVoiceCalls200Response> response = apiInstance.listVoiceCallsWithHttpInfo(status, direction, number, before, limit, profileId, externalId);
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
| **profileId** | **String**| Only calls of this profile. Mutually exclusive with &#x60;externalId&#x60;. 404 when the profile is not in your team or outside a scoped key&#39;s profiles. | [optional] |
| **externalId** | **String**| Same as &#x60;profileId&#x60;, naming the profile by the &#x60;externalId&#x60; you set on it. 404 when none of your visible profiles carries it; 400 when two of them do. | [optional] |

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
| **400** | Invalid query parameter, &#x60;profileId&#x60; together with &#x60;externalId&#x60;, or an &#x60;externalId&#x60; shared by two of your profiles. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The profile named by &#x60;profileId&#x60; / &#x60;externalId&#x60; is not visible to the caller. |  -  |


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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
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
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | SIP trunk not found |  -  |


## transferVoiceCall

> TransferVoiceCall200Response transferVoiceCall(id, transferVoiceCallRequest)

Blind-transfer a live call

Moves the call&#39;s current leg to a new destination (a phone number or a SIP endpoint).  This is a BLIND transfer: control of the leg is handed off and the call ends normally when the transferred leg hangs up. The caller ID presented on the transfer leg is your own number unless you pass &#x60;callerId: \&quot;caller\&quot;&#x60; on an inbound call, which presents the original caller&#39;s number. 

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
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Call not found |  -  |
| **409** | Call is not connected yet, or has already ended |  -  |
| **422** | The carrier refused presenting the caller&#39;s number on this route. Retry with callerId business. |  -  |

## transferVoiceCallWithHttpInfo

> ApiResponse<TransferVoiceCall200Response> transferVoiceCall transferVoiceCallWithHttpInfo(id, transferVoiceCallRequest)

Blind-transfer a live call

Moves the call&#39;s current leg to a new destination (a phone number or a SIP endpoint).  This is a BLIND transfer: control of the leg is handed off and the call ends normally when the transferred leg hangs up. The caller ID presented on the transfer leg is your own number unless you pass &#x60;callerId: \&quot;caller\&quot;&#x60; on an inbound call, which presents the original caller&#39;s number. 

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
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Call not found |  -  |
| **409** | Call is not connected yet, or has already ended |  -  |
| **422** | The carrier refused presenting the caller&#39;s number on this route. Retry with callerId business. |  -  |

