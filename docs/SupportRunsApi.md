# SupportRunsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSupportRun**](SupportRunsApi.md#createSupportRun) | **POST** /v1/support/runs | Start a support run (private beta) |
| [**createSupportRunWithHttpInfo**](SupportRunsApi.md#createSupportRunWithHttpInfo) | **POST** /v1/support/runs | Start a support run (private beta) |
| [**getSupportRun**](SupportRunsApi.md#getSupportRun) | **GET** /v1/support/runs/{runId} | Get a support run (private beta) |
| [**getSupportRunWithHttpInfo**](SupportRunsApi.md#getSupportRunWithHttpInfo) | **GET** /v1/support/runs/{runId} | Get a support run (private beta) |



## createSupportRun

> CreateSupportRun202Response createSupportRun(createSupportRunRequest, idempotencyKey)

Start a support run (private beta)

Private beta: returns 403 &#x60;feature_not_available&#x60; unless enabled for your account. Asks Ana, the Zernio support agent, a question about your workspace. The run is asynchronous: this returns 202 with a &#x60;runId&#x60;, and the answer arrives through the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks. &#x60;GET /v1/support/runs/{runId}&#x60; is the fallback. Pass &#x60;threadId&#x60; to continue an earlier conversation, and &#x60;context&#x60; to point Ana at a post, account or profile. Billed when the run finishes at the model cost plus 20%, never above &#x60;maxCostUsd&#x60;; failed runs are free. Requires an unrestricted API key, usage-based billing and a card on file. Limits per account: 3 active runs and $100 of runs per UTC month. Send an Idempotency-Key header to make retries safe.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportRunsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportRunsApi apiInstance = new SupportRunsApi(defaultClient);
        CreateSupportRunRequest createSupportRunRequest = new CreateSupportRunRequest(); // CreateSupportRunRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            CreateSupportRun202Response result = apiInstance.createSupportRun(createSupportRunRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportRunsApi#createSupportRun");
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
| **createSupportRunRequest** | [**CreateSupportRunRequest**](CreateSupportRunRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**CreateSupportRun202Response**](CreateSupportRun202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | A card is required (code &#x60;payment_method_required&#x60;) or the last payment failed (code &#x60;payment_required&#x60;). Add or update the card in Billing. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60;: the credential is not an unrestricted API key, or the user is read-only, restricted or profile-scoped. Code &#x60;feature_not_available&#x60;: the private beta is not enabled for your account. |  -  |
| **404** | Code &#x60;support_thread_not_found&#x60; (&#x60;threadId&#x60;), &#x60;post_not_found&#x60;, &#x60;account_not_found&#x60; or &#x60;profile_not_found&#x60; (&#x60;context.*&#x60;). |  -  |
| **409** | Code &#x60;support_run_in_progress&#x60;: the thread already has a run queued or running, so poll it first. Code &#x60;billing_setup_incomplete&#x60;: no billing customer to attach a card to, contact support. Also returned while a request with the same Idempotency-Key is still processing. |  -  |
| **422** | Code &#x60;usage_billing_required&#x60;: support runs need a usage-based plan. Also returned when an Idempotency-Key is reused with a different request. |  -  |
| **429** | Code &#x60;support_active_runs_limit&#x60;: 3 runs are already active, retry when one finishes. Code &#x60;support_monthly_cap_exceeded&#x60;: this run could take the account past $100 for the UTC month; &#x60;Retry-After&#x60; runs until the next month starts, which can be weeks. |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## createSupportRunWithHttpInfo

> ApiResponse<CreateSupportRun202Response> createSupportRun createSupportRunWithHttpInfo(createSupportRunRequest, idempotencyKey)

Start a support run (private beta)

Private beta: returns 403 &#x60;feature_not_available&#x60; unless enabled for your account. Asks Ana, the Zernio support agent, a question about your workspace. The run is asynchronous: this returns 202 with a &#x60;runId&#x60;, and the answer arrives through the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks. &#x60;GET /v1/support/runs/{runId}&#x60; is the fallback. Pass &#x60;threadId&#x60; to continue an earlier conversation, and &#x60;context&#x60; to point Ana at a post, account or profile. Billed when the run finishes at the model cost plus 20%, never above &#x60;maxCostUsd&#x60;; failed runs are free. Requires an unrestricted API key, usage-based billing and a card on file. Limits per account: 3 active runs and $100 of runs per UTC month. Send an Idempotency-Key header to make retries safe.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportRunsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportRunsApi apiInstance = new SupportRunsApi(defaultClient);
        CreateSupportRunRequest createSupportRunRequest = new CreateSupportRunRequest(); // CreateSupportRunRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<CreateSupportRun202Response> response = apiInstance.createSupportRunWithHttpInfo(createSupportRunRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportRunsApi#createSupportRun");
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
| **createSupportRunRequest** | [**CreateSupportRunRequest**](CreateSupportRunRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**CreateSupportRun202Response**](CreateSupportRun202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | A card is required (code &#x60;payment_method_required&#x60;) or the last payment failed (code &#x60;payment_required&#x60;). Add or update the card in Billing. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60;: the credential is not an unrestricted API key, or the user is read-only, restricted or profile-scoped. Code &#x60;feature_not_available&#x60;: the private beta is not enabled for your account. |  -  |
| **404** | Code &#x60;support_thread_not_found&#x60; (&#x60;threadId&#x60;), &#x60;post_not_found&#x60;, &#x60;account_not_found&#x60; or &#x60;profile_not_found&#x60; (&#x60;context.*&#x60;). |  -  |
| **409** | Code &#x60;support_run_in_progress&#x60;: the thread already has a run queued or running, so poll it first. Code &#x60;billing_setup_incomplete&#x60;: no billing customer to attach a card to, contact support. Also returned while a request with the same Idempotency-Key is still processing. |  -  |
| **422** | Code &#x60;usage_billing_required&#x60;: support runs need a usage-based plan. Also returned when an Idempotency-Key is reused with a different request. |  -  |
| **429** | Code &#x60;support_active_runs_limit&#x60;: 3 runs are already active, retry when one finishes. Code &#x60;support_monthly_cap_exceeded&#x60;: this run could take the account past $100 for the UTC month; &#x60;Retry-After&#x60; runs until the next month starts, which can be weeks. |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## getSupportRun

> SupportRun getSupportRun(runId)

Get a support run (private beta)

Private beta: returns 403 &#x60;feature_not_available&#x60; unless enabled for your account. Returns a run started by your team. Prefer the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks; use this as the fallback, waiting &#x60;pollAfterSeconds&#x60; between polls. &#x60;costUsd&#x60; is the amount billed: the model cost plus 20%, never above &#x60;maxCostUsd&#x60;, and 0 for a failed run.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportRunsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportRunsApi apiInstance = new SupportRunsApi(defaultClient);
        String runId = "runId_example"; // String | 
        try {
            SupportRun result = apiInstance.getSupportRun(runId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportRunsApi#getSupportRun");
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
| **runId** | **String**|  | |

### Return type

[**SupportRun**](SupportRun.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The run |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | A card is required (code &#x60;payment_method_required&#x60;) or the last payment failed (code &#x60;payment_required&#x60;). |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60; (not an unrestricted API key, or a read-only, restricted or profile-scoped user) or &#x60;feature_not_available&#x60; (private beta not enabled). |  -  |
| **404** | Code &#x60;support_run_not_found&#x60;: no such run, or it was not started by your team. |  -  |

## getSupportRunWithHttpInfo

> ApiResponse<SupportRun> getSupportRun getSupportRunWithHttpInfo(runId)

Get a support run (private beta)

Private beta: returns 403 &#x60;feature_not_available&#x60; unless enabled for your account. Returns a run started by your team. Prefer the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks; use this as the fallback, waiting &#x60;pollAfterSeconds&#x60; between polls. &#x60;costUsd&#x60; is the amount billed: the model cost plus 20%, never above &#x60;maxCostUsd&#x60;, and 0 for a failed run.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportRunsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportRunsApi apiInstance = new SupportRunsApi(defaultClient);
        String runId = "runId_example"; // String | 
        try {
            ApiResponse<SupportRun> response = apiInstance.getSupportRunWithHttpInfo(runId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportRunsApi#getSupportRun");
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
| **runId** | **String**|  | |

### Return type

ApiResponse<[**SupportRun**](SupportRun.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The run |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | A card is required (code &#x60;payment_method_required&#x60;) or the last payment failed (code &#x60;payment_required&#x60;). |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60; (not an unrestricted API key, or a read-only, restricted or profile-scoped user) or &#x60;feature_not_available&#x60; (private beta not enabled). |  -  |
| **404** | Code &#x60;support_run_not_found&#x60;: no such run, or it was not started by your team. |  -  |

