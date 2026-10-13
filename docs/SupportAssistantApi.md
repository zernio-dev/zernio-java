# SupportAssistantApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**askSupportQuestion**](SupportAssistantApi.md#askSupportQuestion) | **POST** /v1/support/runs | Ask a support question |
| [**askSupportQuestionWithHttpInfo**](SupportAssistantApi.md#askSupportQuestionWithHttpInfo) | **POST** /v1/support/runs | Ask a support question |
| [**getSupportAnswer**](SupportAssistantApi.md#getSupportAnswer) | **GET** /v1/support/runs/{runId} | Get a support answer |
| [**getSupportAnswerWithHttpInfo**](SupportAssistantApi.md#getSupportAnswerWithHttpInfo) | **GET** /v1/support/runs/{runId} | Get a support answer |
| [**listSupportAnswers**](SupportAssistantApi.md#listSupportAnswers) | **GET** /v1/support/runs | List a thread&#39;s support answers |
| [**listSupportAnswersWithHttpInfo**](SupportAssistantApi.md#listSupportAnswersWithHttpInfo) | **GET** /v1/support/runs | List a thread&#39;s support answers |



## askSupportQuestion

> AskSupportQuestion202Response askSupportQuestion(askSupportQuestionRequest, idempotencyKey)

Ask a support question

Asks the Zernio Support Assistant a question about your workspace. Each question starts a run that answers asynchronously: this returns 202 with a &#x60;runId&#x60;, and the answer arrives through the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks. &#x60;GET /v1/support/runs/{runId}&#x60; is the fallback. Pass &#x60;threadId&#x60; to continue an earlier conversation, and &#x60;context&#x60; to point the assistant at a post, account, profile or a failed request (its &#x60;X-Request-Id&#x60;). When the assistant finds a problem on Zernio&#39;s side it opens a support ticket with the team (see &#x60;supportTicket&#x60; on the run) and the run ends as &#x60;needs_human&#x60;.  **Pricing.** You pay per question, once it finishes. The exact amount charged is the run&#39;s &#x60;costUsd&#x60;.  | Question | You pay | | --- | --- | | Typical question | $0.10 to $0.50 | | Most one question can cost | Its &#x60;maxCostUsd&#x60;: $0.50 to $3, $3 by default | | Handed to the Zernio team (&#x60;needs_human&#x60;) | Charged like an answered question | | Failed or expired | $0 | | All questions in a UTC month | At most $100 per account |  Near its &#x60;maxCostUsd&#x60; a run stops investigating and answers with what it found so far, so it never charges more than the cap; with nothing to answer yet it fails and costs nothing. Charges appear as \&quot;Support API\&quot; on your invoice.  Requires an unrestricted API key, usage-based billing and a card on file. Limits per account: 3 active runs and $100 of runs per UTC month. Send an Idempotency-Key header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportAssistantApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportAssistantApi apiInstance = new SupportAssistantApi(defaultClient);
        AskSupportQuestionRequest askSupportQuestionRequest = new AskSupportQuestionRequest(); // AskSupportQuestionRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            AskSupportQuestion202Response result = apiInstance.askSupportQuestion(askSupportQuestionRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportAssistantApi#askSupportQuestion");
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
| **askSupportQuestionRequest** | [**AskSupportQuestionRequest**](AskSupportQuestionRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**AskSupportQuestion202Response**](AskSupportQuestion202Response.md)


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
| **403** | Code &#x60;insufficient_permissions&#x60;: the credential is not an unrestricted API key, or the user is read-only, restricted or profile-scoped. |  -  |
| **404** | Code &#x60;support_thread_not_found&#x60; (&#x60;threadId&#x60;), &#x60;post_not_found&#x60;, &#x60;account_not_found&#x60; or &#x60;profile_not_found&#x60; (&#x60;context.*&#x60;). |  -  |
| **409** | Code &#x60;support_run_in_progress&#x60;: the thread already has a run queued or running, so poll it first. Code &#x60;billing_setup_incomplete&#x60;: no billing customer to attach a card to, contact support. Also returned while a request with the same Idempotency-Key is still processing. |  -  |
| **422** | Code &#x60;usage_billing_required&#x60;: the Support Assistant needs a usage-based plan. Also returned when an Idempotency-Key is reused with a different request. |  -  |
| **429** | Code &#x60;support_active_runs_limit&#x60;: 3 runs are already active, retry when one finishes. Code &#x60;support_monthly_cap_exceeded&#x60;: this run could take the account past $100 for the UTC month; &#x60;Retry-After&#x60; runs until the next month starts, which can be weeks. |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## askSupportQuestionWithHttpInfo

> ApiResponse<AskSupportQuestion202Response> askSupportQuestion askSupportQuestionWithHttpInfo(askSupportQuestionRequest, idempotencyKey)

Ask a support question

Asks the Zernio Support Assistant a question about your workspace. Each question starts a run that answers asynchronously: this returns 202 with a &#x60;runId&#x60;, and the answer arrives through the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks. &#x60;GET /v1/support/runs/{runId}&#x60; is the fallback. Pass &#x60;threadId&#x60; to continue an earlier conversation, and &#x60;context&#x60; to point the assistant at a post, account, profile or a failed request (its &#x60;X-Request-Id&#x60;). When the assistant finds a problem on Zernio&#39;s side it opens a support ticket with the team (see &#x60;supportTicket&#x60; on the run) and the run ends as &#x60;needs_human&#x60;.  **Pricing.** You pay per question, once it finishes. The exact amount charged is the run&#39;s &#x60;costUsd&#x60;.  | Question | You pay | | --- | --- | | Typical question | $0.10 to $0.50 | | Most one question can cost | Its &#x60;maxCostUsd&#x60;: $0.50 to $3, $3 by default | | Handed to the Zernio team (&#x60;needs_human&#x60;) | Charged like an answered question | | Failed or expired | $0 | | All questions in a UTC month | At most $100 per account |  Near its &#x60;maxCostUsd&#x60; a run stops investigating and answers with what it found so far, so it never charges more than the cap; with nothing to answer yet it fails and costs nothing. Charges appear as \&quot;Support API\&quot; on your invoice.  Requires an unrestricted API key, usage-based billing and a card on file. Limits per account: 3 active runs and $100 of runs per UTC month. Send an Idempotency-Key header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportAssistantApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportAssistantApi apiInstance = new SupportAssistantApi(defaultClient);
        AskSupportQuestionRequest askSupportQuestionRequest = new AskSupportQuestionRequest(); // AskSupportQuestionRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<AskSupportQuestion202Response> response = apiInstance.askSupportQuestionWithHttpInfo(askSupportQuestionRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportAssistantApi#askSupportQuestion");
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
| **askSupportQuestionRequest** | [**AskSupportQuestionRequest**](AskSupportQuestionRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**AskSupportQuestion202Response**](AskSupportQuestion202Response.md)>


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
| **403** | Code &#x60;insufficient_permissions&#x60;: the credential is not an unrestricted API key, or the user is read-only, restricted or profile-scoped. |  -  |
| **404** | Code &#x60;support_thread_not_found&#x60; (&#x60;threadId&#x60;), &#x60;post_not_found&#x60;, &#x60;account_not_found&#x60; or &#x60;profile_not_found&#x60; (&#x60;context.*&#x60;). |  -  |
| **409** | Code &#x60;support_run_in_progress&#x60;: the thread already has a run queued or running, so poll it first. Code &#x60;billing_setup_incomplete&#x60;: no billing customer to attach a card to, contact support. Also returned while a request with the same Idempotency-Key is still processing. |  -  |
| **422** | Code &#x60;usage_billing_required&#x60;: the Support Assistant needs a usage-based plan. Also returned when an Idempotency-Key is reused with a different request. |  -  |
| **429** | Code &#x60;support_active_runs_limit&#x60;: 3 runs are already active, retry when one finishes. Code &#x60;support_monthly_cap_exceeded&#x60;: this run could take the account past $100 for the UTC month; &#x60;Retry-After&#x60; runs until the next month starts, which can be weeks. |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## getSupportAnswer

> SupportRun getSupportAnswer(runId)

Get a support answer

Returns a run started by your team, with the answer once it is ready. Prefer the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks; use this as the fallback, waiting &#x60;pollAfterSeconds&#x60; between polls. &#x60;costUsd&#x60; is the amount billed for the question, never above &#x60;maxCostUsd&#x60;, and 0 for a failed run (pricing on Ask a support question).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportAssistantApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportAssistantApi apiInstance = new SupportAssistantApi(defaultClient);
        String runId = "runId_example"; // String | 
        try {
            SupportRun result = apiInstance.getSupportAnswer(runId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportAssistantApi#getSupportAnswer");
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
| **403** | Code &#x60;insufficient_permissions&#x60;: not an unrestricted API key, or a read-only, restricted or profile-scoped user. |  -  |
| **404** | Code &#x60;support_run_not_found&#x60;: no such run, or it was not started by your team. |  -  |

## getSupportAnswerWithHttpInfo

> ApiResponse<SupportRun> getSupportAnswer getSupportAnswerWithHttpInfo(runId)

Get a support answer

Returns a run started by your team, with the answer once it is ready. Prefer the &#x60;support.run.completed&#x60; and &#x60;support.run.failed&#x60; webhooks; use this as the fallback, waiting &#x60;pollAfterSeconds&#x60; between polls. &#x60;costUsd&#x60; is the amount billed for the question, never above &#x60;maxCostUsd&#x60;, and 0 for a failed run (pricing on Ask a support question).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportAssistantApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportAssistantApi apiInstance = new SupportAssistantApi(defaultClient);
        String runId = "runId_example"; // String | 
        try {
            ApiResponse<SupportRun> response = apiInstance.getSupportAnswerWithHttpInfo(runId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportAssistantApi#getSupportAnswer");
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
| **403** | Code &#x60;insufficient_permissions&#x60;: not an unrestricted API key, or a read-only, restricted or profile-scoped user. |  -  |
| **404** | Code &#x60;support_run_not_found&#x60;: no such run, or it was not started by your team. |  -  |


## listSupportAnswers

> ListSupportAnswers200Response listSupportAnswers(threadId, limit, cursor)

List a thread&#39;s support answers

Lists the runs of one thread that your team started, with each question and its answer, oldest first. Replies from the Zernio team after a support ticket arrive by email and are not included. Runs are kept for 90 days. Page through a long thread with &#x60;limit&#x60; and &#x60;cursor&#x60;: pass &#x60;nextCursor&#x60; as &#x60;cursor&#x60; until it is null.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportAssistantApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportAssistantApi apiInstance = new SupportAssistantApi(defaultClient);
        String threadId = "threadId_example"; // String | The thread to list, as returned by `POST /v1/support/runs`.
        Integer limit = 20; // Integer | Runs per page.
        String cursor = "cursor_example"; // String | Pass `nextCursor` from the previous page.
        try {
            ListSupportAnswers200Response result = apiInstance.listSupportAnswers(threadId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportAssistantApi#listSupportAnswers");
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
| **threadId** | **String**| The thread to list, as returned by &#x60;POST /v1/support/runs&#x60;. | |
| **limit** | **Integer**| Runs per page. | [optional] [default to 20] |
| **cursor** | **String**| Pass &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

[**ListSupportAnswers200Response**](ListSupportAnswers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thread&#39;s runs, oldest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | A card is required (code &#x60;payment_method_required&#x60;) or the last payment failed (code &#x60;payment_required&#x60;). |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60;: not an unrestricted API key, or a read-only, restricted or profile-scoped user. |  -  |
| **404** | Code &#x60;support_thread_not_found&#x60;: no run in this thread was started by your team, or its runs are older than 90 days. |  -  |

## listSupportAnswersWithHttpInfo

> ApiResponse<ListSupportAnswers200Response> listSupportAnswers listSupportAnswersWithHttpInfo(threadId, limit, cursor)

List a thread&#39;s support answers

Lists the runs of one thread that your team started, with each question and its answer, oldest first. Replies from the Zernio team after a support ticket arrive by email and are not included. Runs are kept for 90 days. Page through a long thread with &#x60;limit&#x60; and &#x60;cursor&#x60;: pass &#x60;nextCursor&#x60; as &#x60;cursor&#x60; until it is null.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SupportAssistantApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SupportAssistantApi apiInstance = new SupportAssistantApi(defaultClient);
        String threadId = "threadId_example"; // String | The thread to list, as returned by `POST /v1/support/runs`.
        Integer limit = 20; // Integer | Runs per page.
        String cursor = "cursor_example"; // String | Pass `nextCursor` from the previous page.
        try {
            ApiResponse<ListSupportAnswers200Response> response = apiInstance.listSupportAnswersWithHttpInfo(threadId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SupportAssistantApi#listSupportAnswers");
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
| **threadId** | **String**| The thread to list, as returned by &#x60;POST /v1/support/runs&#x60;. | |
| **limit** | **Integer**| Runs per page. | [optional] [default to 20] |
| **cursor** | **String**| Pass &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

ApiResponse<[**ListSupportAnswers200Response**](ListSupportAnswers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thread&#39;s runs, oldest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | A card is required (code &#x60;payment_method_required&#x60;) or the last payment failed (code &#x60;payment_required&#x60;). |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60;: not an unrestricted API key, or a read-only, restricted or profile-scoped user. |  -  |
| **404** | Code &#x60;support_thread_not_found&#x60;: no run in this thread was started by your team, or its runs are older than 90 days. |  -  |

