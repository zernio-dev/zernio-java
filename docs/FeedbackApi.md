# FeedbackApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**submitFeedback**](FeedbackApi.md#submitFeedback) | **POST** /v1/feedback | Submit feedback |
| [**submitFeedbackWithHttpInfo**](FeedbackApi.md#submitFeedbackWithHttpInfo) | **POST** /v1/feedback | Submit feedback |



## submitFeedback

> FeedbackReceipt submitFeedback(submitFeedbackRequest)

Submit feedback

Report a bug, a missing feature or a documentation gap. Every submission is read by the Zernio team. Designed for AI agents: when a call fails in a way that looks like our bug, or the API lacks something you need, send one structured report here.  Include &#x60;endpoint&#x60; and &#x60;requestId&#x60; (the &#x60;x-request-id&#x60; response header of the failing call) when you have them; they let us find the exact request.  Submitting the same &#x60;summary&#x60; again within 24 hours is idempotent: it returns the original &#x60;id&#x60; with &#x60;duplicate: true&#x60; and a &#x60;200&#x60;. Each API user can file at most 20 submissions per 24 hours. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FeedbackApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FeedbackApi apiInstance = new FeedbackApi(defaultClient);
        SubmitFeedbackRequest submitFeedbackRequest = new SubmitFeedbackRequest(); // SubmitFeedbackRequest | 
        try {
            FeedbackReceipt result = apiInstance.submitFeedback(submitFeedbackRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FeedbackApi#submitFeedback");
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
| **submitFeedbackRequest** | [**SubmitFeedbackRequest**](SubmitFeedbackRequest.md)|  | |

### Return type

[**FeedbackReceipt**](FeedbackReceipt.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Feedback received |  -  |
| **200** | Duplicate of a submission made in the last 24 hours. Returns the original id. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **429** | More than 20 submissions in the last 24 hours. |  -  |

## submitFeedbackWithHttpInfo

> ApiResponse<FeedbackReceipt> submitFeedback submitFeedbackWithHttpInfo(submitFeedbackRequest)

Submit feedback

Report a bug, a missing feature or a documentation gap. Every submission is read by the Zernio team. Designed for AI agents: when a call fails in a way that looks like our bug, or the API lacks something you need, send one structured report here.  Include &#x60;endpoint&#x60; and &#x60;requestId&#x60; (the &#x60;x-request-id&#x60; response header of the failing call) when you have them; they let us find the exact request.  Submitting the same &#x60;summary&#x60; again within 24 hours is idempotent: it returns the original &#x60;id&#x60; with &#x60;duplicate: true&#x60; and a &#x60;200&#x60;. Each API user can file at most 20 submissions per 24 hours. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FeedbackApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FeedbackApi apiInstance = new FeedbackApi(defaultClient);
        SubmitFeedbackRequest submitFeedbackRequest = new SubmitFeedbackRequest(); // SubmitFeedbackRequest | 
        try {
            ApiResponse<FeedbackReceipt> response = apiInstance.submitFeedbackWithHttpInfo(submitFeedbackRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FeedbackApi#submitFeedback");
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
| **submitFeedbackRequest** | [**SubmitFeedbackRequest**](SubmitFeedbackRequest.md)|  | |

### Return type

ApiResponse<[**FeedbackReceipt**](FeedbackReceipt.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Feedback received |  -  |
| **200** | Duplicate of a submission made in the last 24 hours. Returns the original id. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **429** | More than 20 submissions in the last 24 hours. |  -  |

