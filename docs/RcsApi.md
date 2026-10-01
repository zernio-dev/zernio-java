# RcsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRcsTestDevice**](RcsApi.md#addRcsTestDevice) | **POST** /v1/rcs/agents/{agentId}/test-devices | Invite an RCS test phone |
| [**addRcsTestDeviceWithHttpInfo**](RcsApi.md#addRcsTestDeviceWithHttpInfo) | **POST** /v1/rcs/agents/{agentId}/test-devices | Invite an RCS test phone |
| [**createRcsAgent**](RcsApi.md#createRcsAgent) | **POST** /v1/rcs/agents | Request an RCS agent |
| [**createRcsAgentWithHttpInfo**](RcsApi.md#createRcsAgentWithHttpInfo) | **POST** /v1/rcs/agents | Request an RCS agent |
| [**deactivateRcsAgent**](RcsApi.md#deactivateRcsAgent) | **DELETE** /v1/rcs/agents/{agentId} | Deactivate an RCS agent |
| [**deactivateRcsAgentWithHttpInfo**](RcsApi.md#deactivateRcsAgentWithHttpInfo) | **DELETE** /v1/rcs/agents/{agentId} | Deactivate an RCS agent |
| [**getRcsAgent**](RcsApi.md#getRcsAgent) | **GET** /v1/rcs/agents/{agentId} | Get an RCS agent |
| [**getRcsAgentWithHttpInfo**](RcsApi.md#getRcsAgentWithHttpInfo) | **GET** /v1/rcs/agents/{agentId} | Get an RCS agent |
| [**getRcsCapabilities**](RcsApi.md#getRcsCapabilities) | **GET** /v1/rcs/capabilities | Check RCS capability |
| [**getRcsCapabilitiesWithHttpInfo**](RcsApi.md#getRcsCapabilitiesWithHttpInfo) | **GET** /v1/rcs/capabilities | Check RCS capability |
| [**listRcsAgents**](RcsApi.md#listRcsAgents) | **GET** /v1/rcs/agents | List RCS agents |
| [**listRcsAgentsWithHttpInfo**](RcsApi.md#listRcsAgentsWithHttpInfo) | **GET** /v1/rcs/agents | List RCS agents |
| [**listRcsBrands**](RcsApi.md#listRcsBrands) | **GET** /v1/rcs/brands | List RCS brands |
| [**listRcsBrandsWithHttpInfo**](RcsApi.md#listRcsBrandsWithHttpInfo) | **GET** /v1/rcs/brands | List RCS brands |
| [**listRcsTestDevices**](RcsApi.md#listRcsTestDevices) | **GET** /v1/rcs/agents/{agentId}/test-devices | List RCS test phones |
| [**listRcsTestDevicesWithHttpInfo**](RcsApi.md#listRcsTestDevicesWithHttpInfo) | **GET** /v1/rcs/agents/{agentId}/test-devices | List RCS test phones |
| [**removeRcsTestDevice**](RcsApi.md#removeRcsTestDevice) | **DELETE** /v1/rcs/agents/{agentId}/test-devices/{testDeviceId} | Remove an RCS test phone |
| [**removeRcsTestDeviceWithHttpInfo**](RcsApi.md#removeRcsTestDeviceWithHttpInfo) | **DELETE** /v1/rcs/agents/{agentId}/test-devices/{testDeviceId} | Remove an RCS test phone |
| [**requestRcsAgentLaunch**](RcsApi.md#requestRcsAgentLaunch) | **POST** /v1/rcs/agents/{agentId}/launch-request | Send the launch filing |
| [**requestRcsAgentLaunchWithHttpInfo**](RcsApi.md#requestRcsAgentLaunchWithHttpInfo) | **POST** /v1/rcs/agents/{agentId}/launch-request | Send the launch filing |
| [**sendRcsMessage**](RcsApi.md#sendRcsMessage) | **POST** /v1/rcs/messages | Send an RCS message |
| [**sendRcsMessageWithHttpInfo**](RcsApi.md#sendRcsMessageWithHttpInfo) | **POST** /v1/rcs/messages | Send an RCS message |
| [**updateRcsAgent**](RcsApi.md#updateRcsAgent) | **PATCH** /v1/rcs/agents/{agentId} | Update an RCS agent |
| [**updateRcsAgentWithHttpInfo**](RcsApi.md#updateRcsAgentWithHttpInfo) | **PATCH** /v1/rcs/agents/{agentId} | Update an RCS agent |
| [**uploadRcsAsset**](RcsApi.md#uploadRcsAsset) | **POST** /v1/rcs/assets | Upload an RCS logo or banner |
| [**uploadRcsAssetWithHttpInfo**](RcsApi.md#uploadRcsAssetWithHttpInfo) | **POST** /v1/rcs/assets | Upload an RCS logo or banner |



## addRcsTestDevice

> AddRcsTestDevice201Response addRcsTestDevice(agentId, addRcsTestDeviceRequest)

Invite an RCS test phone

Invites a phone to try the agent before launch. It must accept the invite in its messaging app. Available once the agent exists with the carriers (after brand vetting). T-Mobile and AT&amp;T numbers cannot be test phones. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        AddRcsTestDeviceRequest addRcsTestDeviceRequest = new AddRcsTestDeviceRequest(); // AddRcsTestDeviceRequest | 
        try {
            AddRcsTestDevice201Response result = apiInstance.addRcsTestDevice(agentId, addRcsTestDeviceRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#addRcsTestDevice");
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
| **agentId** | **String**|  | |
| **addRcsTestDeviceRequest** | [**AddRcsTestDeviceRequest**](AddRcsTestDeviceRequest.md)|  | |

### Return type

[**AddRcsTestDevice201Response**](AddRcsTestDevice201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invite sent. |  -  |
| **400** | Invalid phone number, or the carrier refused it as a test phone |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent does not exist with the carriers yet |  -  |

## addRcsTestDeviceWithHttpInfo

> ApiResponse<AddRcsTestDevice201Response> addRcsTestDevice addRcsTestDeviceWithHttpInfo(agentId, addRcsTestDeviceRequest)

Invite an RCS test phone

Invites a phone to try the agent before launch. It must accept the invite in its messaging app. Available once the agent exists with the carriers (after brand vetting). T-Mobile and AT&amp;T numbers cannot be test phones. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        AddRcsTestDeviceRequest addRcsTestDeviceRequest = new AddRcsTestDeviceRequest(); // AddRcsTestDeviceRequest | 
        try {
            ApiResponse<AddRcsTestDevice201Response> response = apiInstance.addRcsTestDeviceWithHttpInfo(agentId, addRcsTestDeviceRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#addRcsTestDevice");
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
| **agentId** | **String**|  | |
| **addRcsTestDeviceRequest** | [**AddRcsTestDeviceRequest**](AddRcsTestDeviceRequest.md)|  | |

### Return type

ApiResponse<[**AddRcsTestDevice201Response**](AddRcsTestDevice201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invite sent. |  -  |
| **400** | Invalid phone number, or the carrier refused it as a test phone |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent does not exist with the carriers yet |  -  |


## createRcsAgent

> CreateRcsAgent201Response createRcsAgent(createRcsAgentRequest, idempotencyKey)

Request an RCS agent

Requests a new agent for a profile, with a new company (&#x60;brand&#x60;) or an existing one (&#x60;brandId&#x60;, skips vetting when it is already verified). The request lands in our review: nothing is filed with the carriers or billed until we submit it. A profile can hold several agents. Requires usage-based billing and a card on file. Send an &#x60;Idempotency-Key&#x60; header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        CreateRcsAgentRequest createRcsAgentRequest = new CreateRcsAgentRequest(); // CreateRcsAgentRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            CreateRcsAgent201Response result = apiInstance.createRcsAgent(createRcsAgentRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#createRcsAgent");
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
| **createRcsAgentRequest** | [**CreateRcsAgentRequest**](CreateRcsAgentRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Agent requested. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | No payment method on file (payment_method_required). Add a card and retry. |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Profile or brand not found |  -  |
| **409** | The brand was rejected, or the Idempotency-Key is still in flight |  -  |
| **422** | Usage-based billing is not enabled for the workspace (USAGE_BILLING_REQUIRED), or the Idempotency-Key was reused with a different body |  -  |

## createRcsAgentWithHttpInfo

> ApiResponse<CreateRcsAgent201Response> createRcsAgent createRcsAgentWithHttpInfo(createRcsAgentRequest, idempotencyKey)

Request an RCS agent

Requests a new agent for a profile, with a new company (&#x60;brand&#x60;) or an existing one (&#x60;brandId&#x60;, skips vetting when it is already verified). The request lands in our review: nothing is filed with the carriers or billed until we submit it. A profile can hold several agents. Requires usage-based billing and a card on file. Send an &#x60;Idempotency-Key&#x60; header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        CreateRcsAgentRequest createRcsAgentRequest = new CreateRcsAgentRequest(); // CreateRcsAgentRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<CreateRcsAgent201Response> response = apiInstance.createRcsAgentWithHttpInfo(createRcsAgentRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#createRcsAgent");
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
| **createRcsAgentRequest** | [**CreateRcsAgentRequest**](CreateRcsAgentRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Agent requested. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | No payment method on file (payment_method_required). Add a card and retry. |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Profile or brand not found |  -  |
| **409** | The brand was rejected, or the Idempotency-Key is still in flight |  -  |
| **422** | Usage-based billing is not enabled for the workspace (USAGE_BILLING_REQUIRED), or the Idempotency-Key was reused with a different body |  -  |


## deactivateRcsAgent

> CreateRcsAgent201Response deactivateRcsAgent(agentId)

Deactivate an RCS agent

Stops sending, disconnects its inbox account and stops monthly billing. Fees already charged are not refunded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        try {
            CreateRcsAgent201Response result = apiInstance.deactivateRcsAgent(agentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#deactivateRcsAgent");
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
| **agentId** | **String**|  | |

### Return type

[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deactivated agent. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent is already rejected or deactivated |  -  |

## deactivateRcsAgentWithHttpInfo

> ApiResponse<CreateRcsAgent201Response> deactivateRcsAgent deactivateRcsAgentWithHttpInfo(agentId)

Deactivate an RCS agent

Stops sending, disconnects its inbox account and stops monthly billing. Fees already charged are not refunded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        try {
            ApiResponse<CreateRcsAgent201Response> response = apiInstance.deactivateRcsAgentWithHttpInfo(agentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#deactivateRcsAgent");
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
| **agentId** | **String**|  | |

### Return type

ApiResponse<[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deactivated agent. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent is already rejected or deactivated |  -  |


## getRcsAgent

> CreateRcsAgent201Response getRcsAgent(agentId)

Get an RCS agent

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        try {
            CreateRcsAgent201Response result = apiInstance.getRcsAgent(agentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#getRcsAgent");
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
| **agentId** | **String**|  | |

### Return type

[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The agent with its brand, carrier approvals and test devices. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |

## getRcsAgentWithHttpInfo

> ApiResponse<CreateRcsAgent201Response> getRcsAgent getRcsAgentWithHttpInfo(agentId)

Get an RCS agent

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        try {
            ApiResponse<CreateRcsAgent201Response> response = apiInstance.getRcsAgentWithHttpInfo(agentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#getRcsAgent");
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
| **agentId** | **String**|  | |

### Return type

ApiResponse<[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The agent with its brand, carrier approvals and test devices. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |


## getRcsCapabilities

> GetRcsCapabilities200Response getRcsCapabilities(agentId, numbers)

Check RCS capability

Which recipients can receive RCS from the agent and which rich features their phones support. Up to 100 numbers.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        String numbers = "numbers_example"; // String | Comma-separated E.164 numbers, max 100.
        try {
            GetRcsCapabilities200Response result = apiInstance.getRcsCapabilities(agentId, numbers);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#getRcsCapabilities");
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
| **agentId** | **String**|  | |
| **numbers** | **String**| Comma-separated E.164 numbers, max 100. | |

### Return type

[**GetRcsCapabilities200Response**](GetRcsCapabilities200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One entry per number, in input order. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent does not exist with the carriers yet |  -  |

## getRcsCapabilitiesWithHttpInfo

> ApiResponse<GetRcsCapabilities200Response> getRcsCapabilities getRcsCapabilitiesWithHttpInfo(agentId, numbers)

Check RCS capability

Which recipients can receive RCS from the agent and which rich features their phones support. Up to 100 numbers.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        String numbers = "numbers_example"; // String | Comma-separated E.164 numbers, max 100.
        try {
            ApiResponse<GetRcsCapabilities200Response> response = apiInstance.getRcsCapabilitiesWithHttpInfo(agentId, numbers);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#getRcsCapabilities");
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
| **agentId** | **String**|  | |
| **numbers** | **String**| Comma-separated E.164 numbers, max 100. | |

### Return type

ApiResponse<[**GetRcsCapabilities200Response**](GetRcsCapabilities200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One entry per number, in input order. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent does not exist with the carriers yet |  -  |


## listRcsAgents

> ListRcsAgents200Response listRcsAgents(includeClosed)

List RCS agents

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        Boolean includeClosed = true; // Boolean | Include rejected and deactivated agents.
        try {
            ListRcsAgents200Response result = apiInstance.listRcsAgents(includeClosed);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#listRcsAgents");
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
| **includeClosed** | **Boolean**| Include rejected and deactivated agents. | [optional] |

### Return type

[**ListRcsAgents200Response**](ListRcsAgents200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Agents, newest first. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |

## listRcsAgentsWithHttpInfo

> ApiResponse<ListRcsAgents200Response> listRcsAgents listRcsAgentsWithHttpInfo(includeClosed)

List RCS agents

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        Boolean includeClosed = true; // Boolean | Include rejected and deactivated agents.
        try {
            ApiResponse<ListRcsAgents200Response> response = apiInstance.listRcsAgentsWithHttpInfo(includeClosed);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#listRcsAgents");
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
| **includeClosed** | **Boolean**| Include rejected and deactivated agents. | [optional] |

### Return type

ApiResponse<[**ListRcsAgents200Response**](ListRcsAgents200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Agents, newest first. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |


## listRcsBrands

> ListRcsBrands200Response listRcsBrands()

List RCS brands

The team&#39;s RCS brands (vetted companies), to reuse one for another agent with &#x60;brandId&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        try {
            ListRcsBrands200Response result = apiInstance.listRcsBrands();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#listRcsBrands");
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

[**ListRcsBrands200Response**](ListRcsBrands200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Brands, newest first. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |

## listRcsBrandsWithHttpInfo

> ApiResponse<ListRcsBrands200Response> listRcsBrands listRcsBrandsWithHttpInfo()

List RCS brands

The team&#39;s RCS brands (vetted companies), to reuse one for another agent with &#x60;brandId&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        try {
            ApiResponse<ListRcsBrands200Response> response = apiInstance.listRcsBrandsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#listRcsBrands");
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

ApiResponse<[**ListRcsBrands200Response**](ListRcsBrands200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Brands, newest first. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |


## listRcsTestDevices

> ListRcsTestDevices200Response listRcsTestDevices(agentId)

List RCS test phones

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        try {
            ListRcsTestDevices200Response result = apiInstance.listRcsTestDevices(agentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#listRcsTestDevices");
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
| **agentId** | **String**|  | |

### Return type

[**ListRcsTestDevices200Response**](ListRcsTestDevices200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invited test phones. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |

## listRcsTestDevicesWithHttpInfo

> ApiResponse<ListRcsTestDevices200Response> listRcsTestDevices listRcsTestDevicesWithHttpInfo(agentId)

List RCS test phones

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        try {
            ApiResponse<ListRcsTestDevices200Response> response = apiInstance.listRcsTestDevicesWithHttpInfo(agentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#listRcsTestDevices");
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
| **agentId** | **String**|  | |

### Return type

ApiResponse<[**ListRcsTestDevices200Response**](ListRcsTestDevices200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invited test phones. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |


## removeRcsTestDevice

> UpdateYoutubeDefaultPlaylist200Response removeRcsTestDevice(agentId, testDeviceId)

Remove an RCS test phone

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        UUID testDeviceId = UUID.randomUUID(); // UUID | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.removeRcsTestDevice(agentId, testDeviceId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#removeRcsTestDevice");
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
| **agentId** | **String**|  | |
| **testDeviceId** | **UUID**|  | |

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
| **200** | Removed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent or test phone not found |  -  |

## removeRcsTestDeviceWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> removeRcsTestDevice removeRcsTestDeviceWithHttpInfo(agentId, testDeviceId)

Remove an RCS test phone

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        UUID testDeviceId = UUID.randomUUID(); // UUID | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.removeRcsTestDeviceWithHttpInfo(agentId, testDeviceId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#removeRcsTestDevice");
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
| **agentId** | **String**|  | |
| **testDeviceId** | **UUID**|  | |

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
| **200** | Removed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent or test phone not found |  -  |


## requestRcsAgentLaunch

> CreateRcsAgent201Response requestRcsAgentLaunch(agentId, rcsLaunchRequest)

Send the launch filing

Sends the launch details the carriers review (campaign, consent and a public test video). US agents send them once they are in &#x60;testing&#x60;; we review them before they reach the carriers. Agents in other markets send them while still in review (&#x60;requested&#x60;, &#x60;changes_requested&#x60; or &#x60;brand_vetting&#x60;), because we file everything with the carriers at once; this saves the details without changing the status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        RcsLaunchRequest rcsLaunchRequest = new RcsLaunchRequest(); // RcsLaunchRequest | 
        try {
            CreateRcsAgent201Response result = apiInstance.requestRcsAgentLaunch(agentId, rcsLaunchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#requestRcsAgentLaunch");
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
| **agentId** | **String**|  | |
| **rcsLaunchRequest** | [**RcsLaunchRequest**](RcsLaunchRequest.md)|  | |

### Return type

[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The agent, now in launch_review. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent is not in testing |  -  |

## requestRcsAgentLaunchWithHttpInfo

> ApiResponse<CreateRcsAgent201Response> requestRcsAgentLaunch requestRcsAgentLaunchWithHttpInfo(agentId, rcsLaunchRequest)

Send the launch filing

Sends the launch details the carriers review (campaign, consent and a public test video). US agents send them once they are in &#x60;testing&#x60;; we review them before they reach the carriers. Agents in other markets send them while still in review (&#x60;requested&#x60;, &#x60;changes_requested&#x60; or &#x60;brand_vetting&#x60;), because we file everything with the carriers at once; this saves the details without changing the status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        RcsLaunchRequest rcsLaunchRequest = new RcsLaunchRequest(); // RcsLaunchRequest | 
        try {
            ApiResponse<CreateRcsAgent201Response> response = apiInstance.requestRcsAgentLaunchWithHttpInfo(agentId, rcsLaunchRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#requestRcsAgentLaunch");
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
| **agentId** | **String**|  | |
| **rcsLaunchRequest** | [**RcsLaunchRequest**](RcsLaunchRequest.md)|  | |

### Return type

ApiResponse<[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The agent, now in launch_review. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent is not in testing |  -  |


## sendRcsMessage

> SendRcsMessage200Response sendRcsMessage(sendRcsMessageRequest, idempotencyKey)

Send an RCS message

Sends from one of your agents. Use &#x60;text&#x60; for a plain message or &#x60;content&#x60; for rich content (card, carousel, media, suggestion chips). Before launch an agent only reaches test phones that accepted the invite. With the agent&#39;s &#x60;smsFallbackFrom&#x60; set, phones without RCS get &#x60;fallbackText&#x60; (default: the message&#39;s readable text) as SMS.  Replies and status arrive as webhooks with &#x60;platform: \&quot;rcs\&quot;&#x60;: &#x60;message.received&#x60; (a tapped chip carries its postback in &#x60;metadata.postbackPayload&#x60;), &#x60;message.delivered&#x60;, &#x60;message.read&#x60; and &#x60;message.failed&#x60;. Send an &#x60;Idempotency-Key&#x60; header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        SendRcsMessageRequest sendRcsMessageRequest = new SendRcsMessageRequest(); // SendRcsMessageRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            SendRcsMessage200Response result = apiInstance.sendRcsMessage(sendRcsMessageRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#sendRcsMessage");
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
| **sendRcsMessageRequest** | [**SendRcsMessageRequest**](SendRcsMessageRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**SendRcsMessage200Response**](SendRcsMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message accepted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The plan does not include the inbox, the recipient is not an accepted test phone before launch, or usage billing is not enabled |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent cannot send yet, the recipient opted out (replied STOP), or the Idempotency-Key is still in flight |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **502** | Carrier-side send failed |  -  |

## sendRcsMessageWithHttpInfo

> ApiResponse<SendRcsMessage200Response> sendRcsMessage sendRcsMessageWithHttpInfo(sendRcsMessageRequest, idempotencyKey)

Send an RCS message

Sends from one of your agents. Use &#x60;text&#x60; for a plain message or &#x60;content&#x60; for rich content (card, carousel, media, suggestion chips). Before launch an agent only reaches test phones that accepted the invite. With the agent&#39;s &#x60;smsFallbackFrom&#x60; set, phones without RCS get &#x60;fallbackText&#x60; (default: the message&#39;s readable text) as SMS.  Replies and status arrive as webhooks with &#x60;platform: \&quot;rcs\&quot;&#x60;: &#x60;message.received&#x60; (a tapped chip carries its postback in &#x60;metadata.postbackPayload&#x60;), &#x60;message.delivered&#x60;, &#x60;message.read&#x60; and &#x60;message.failed&#x60;. Send an &#x60;Idempotency-Key&#x60; header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        SendRcsMessageRequest sendRcsMessageRequest = new SendRcsMessageRequest(); // SendRcsMessageRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<SendRcsMessage200Response> response = apiInstance.sendRcsMessageWithHttpInfo(sendRcsMessageRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#sendRcsMessage");
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
| **sendRcsMessageRequest** | [**SendRcsMessageRequest**](SendRcsMessageRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**SendRcsMessage200Response**](SendRcsMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message accepted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The plan does not include the inbox, the recipient is not an accepted test phone before launch, or usage billing is not enabled |  -  |
| **404** | Agent not found |  -  |
| **409** | The agent cannot send yet, the recipient opted out (replied STOP), or the Idempotency-Key is still in flight |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **502** | Carrier-side send failed |  -  |


## updateRcsAgent

> CreateRcsAgent201Response updateRcsAgent(agentId, updateRcsAgentRequest)

Update an RCS agent

Edits the filing while the agent is &#x60;requested&#x60; or &#x60;changes_requested&#x60;; answering a change request puts it back in our review. The company can only change until it is filed. &#x60;smsFallbackFrom&#x60; stays editable in any status (null removes it). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        UpdateRcsAgentRequest updateRcsAgentRequest = new UpdateRcsAgentRequest(); // UpdateRcsAgentRequest | 
        try {
            CreateRcsAgent201Response result = apiInstance.updateRcsAgent(agentId, updateRcsAgentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#updateRcsAgent");
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
| **agentId** | **String**|  | |
| **updateRcsAgentRequest** | [**UpdateRcsAgentRequest**](UpdateRcsAgentRequest.md)|  | |

### Return type

[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated agent. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The filing is locked because it is already with the carriers |  -  |

## updateRcsAgentWithHttpInfo

> ApiResponse<CreateRcsAgent201Response> updateRcsAgent updateRcsAgentWithHttpInfo(agentId, updateRcsAgentRequest)

Update an RCS agent

Edits the filing while the agent is &#x60;requested&#x60; or &#x60;changes_requested&#x60;; answering a change request puts it back in our review. The company can only change until it is filed. &#x60;smsFallbackFrom&#x60; stays editable in any status (null removes it). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        String agentId = "agentId_example"; // String | 
        UpdateRcsAgentRequest updateRcsAgentRequest = new UpdateRcsAgentRequest(); // UpdateRcsAgentRequest | 
        try {
            ApiResponse<CreateRcsAgent201Response> response = apiInstance.updateRcsAgentWithHttpInfo(agentId, updateRcsAgentRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#updateRcsAgent");
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
| **agentId** | **String**|  | |
| **updateRcsAgentRequest** | [**UpdateRcsAgentRequest**](UpdateRcsAgentRequest.md)|  | |

### Return type

ApiResponse<[**CreateRcsAgent201Response**](CreateRcsAgent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated agent. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **404** | Agent not found |  -  |
| **409** | The filing is locked because it is already with the carriers |  -  |


## uploadRcsAsset

> ListInboxReviews200ResponseDataInnerPhotosInner uploadRcsAsset(_file, kind)

Upload an RCS logo or banner

Uploads an image and returns a public URL for &#x60;profile.logoUrl&#x60; or &#x60;profile.heroUrl&#x60;. The image is cropped and compressed to the carriers&#39; exact rules (logo 224x224 under 50 KB, banner 1440x448 under 200 KB). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        File _file = new File("/path/to/file"); // File | PNG, JPEG or WebP.
        String kind = "logo"; // String | 
        try {
            ListInboxReviews200ResponseDataInnerPhotosInner result = apiInstance.uploadRcsAsset(_file, kind);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#uploadRcsAsset");
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
| **_file** | **File**| PNG, JPEG or WebP. | |
| **kind** | **String**|  | [enum: logo, banner] |

### Return type

[**ListInboxReviews200ResponseDataInnerPhotosInner**](ListInboxReviews200ResponseDataInnerPhotosInner.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hosted URL. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **422** | The image is unreadable, too small, or could not be compressed under the limit |  -  |

## uploadRcsAssetWithHttpInfo

> ApiResponse<ListInboxReviews200ResponseDataInnerPhotosInner> uploadRcsAsset uploadRcsAssetWithHttpInfo(_file, kind)

Upload an RCS logo or banner

Uploads an image and returns a public URL for &#x60;profile.logoUrl&#x60; or &#x60;profile.heroUrl&#x60;. The image is cropped and compressed to the carriers&#39; exact rules (logo 224x224 under 50 KB, banner 1440x448 under 200 KB). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RcsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RcsApi apiInstance = new RcsApi(defaultClient);
        File _file = new File("/path/to/file"); // File | PNG, JPEG or WebP.
        String kind = "logo"; // String | 
        try {
            ApiResponse<ListInboxReviews200ResponseDataInnerPhotosInner> response = apiInstance.uploadRcsAssetWithHttpInfo(_file, kind);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RcsApi#uploadRcsAsset");
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
| **_file** | **File**| PNG, JPEG or WebP. | |
| **kind** | **String**|  | [enum: logo, banner] |

### Return type

ApiResponse<[**ListInboxReviews200ResponseDataInnerPhotosInner**](ListInboxReviews200ResponseDataInnerPhotosInner.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hosted URL. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Your plan does not include the inbox, which RCS requires. |  -  |
| **422** | The image is unreadable, too small, or could not be compressed under the limit |  -  |

