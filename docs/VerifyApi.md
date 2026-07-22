# VerifyApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkVerification**](VerifyApi.md#checkVerification) | **POST** /v1/verify/verifications/{verificationId}/check | Check a verification code |
| [**checkVerificationWithHttpInfo**](VerifyApi.md#checkVerificationWithHttpInfo) | **POST** /v1/verify/verifications/{verificationId}/check | Check a verification code |
| [**createVerification**](VerifyApi.md#createVerification) | **POST** /v1/verify/verifications | Send a verification code |
| [**createVerificationWithHttpInfo**](VerifyApi.md#createVerificationWithHttpInfo) | **POST** /v1/verify/verifications | Send a verification code |
| [**getVerification**](VerifyApi.md#getVerification) | **GET** /v1/verify/verifications/{verificationId} | Get a verification |
| [**getVerificationWithHttpInfo**](VerifyApi.md#getVerificationWithHttpInfo) | **GET** /v1/verify/verifications/{verificationId} | Get a verification |



## checkVerification

> CheckVerification200Response checkVerification(verificationId, checkVerificationRequest)

Check a verification code

Verify the code the user typed. Wrong, expired, and exhausted codes answer 200 with &#x60;valid: false&#x60; and the settled &#x60;status&#x60; — only an unknown id is a 404. A correct code consumes the verification (single-use, &#x60;status: approved&#x60;) and fires the &#x60;verification.approved&#x60; webhook; the 5th wrong attempt settles it as &#x60;max_attempts_reached&#x60; and fires &#x60;verification.failed&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VerifyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VerifyApi apiInstance = new VerifyApi(defaultClient);
        String verificationId = "verificationId_example"; // String | 
        CheckVerificationRequest checkVerificationRequest = new CheckVerificationRequest(); // CheckVerificationRequest | 
        try {
            CheckVerification200Response result = apiInstance.checkVerification(verificationId, checkVerificationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VerifyApi#checkVerification");
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
| **verificationId** | **String**|  | |
| **checkVerificationRequest** | [**CheckVerificationRequest**](CheckVerificationRequest.md)|  | |

### Return type

[**CheckVerification200Response**](CheckVerification200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check result: the verification plus &#x60;valid&#x60;. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Verification not found (or already reaped). |  -  |

## checkVerificationWithHttpInfo

> ApiResponse<CheckVerification200Response> checkVerification checkVerificationWithHttpInfo(verificationId, checkVerificationRequest)

Check a verification code

Verify the code the user typed. Wrong, expired, and exhausted codes answer 200 with &#x60;valid: false&#x60; and the settled &#x60;status&#x60; — only an unknown id is a 404. A correct code consumes the verification (single-use, &#x60;status: approved&#x60;) and fires the &#x60;verification.approved&#x60; webhook; the 5th wrong attempt settles it as &#x60;max_attempts_reached&#x60; and fires &#x60;verification.failed&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VerifyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VerifyApi apiInstance = new VerifyApi(defaultClient);
        String verificationId = "verificationId_example"; // String | 
        CheckVerificationRequest checkVerificationRequest = new CheckVerificationRequest(); // CheckVerificationRequest | 
        try {
            ApiResponse<CheckVerification200Response> response = apiInstance.checkVerificationWithHttpInfo(verificationId, checkVerificationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VerifyApi#checkVerification");
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
| **verificationId** | **String**|  | |
| **checkVerificationRequest** | [**CheckVerificationRequest**](CheckVerificationRequest.md)|  | |

### Return type

ApiResponse<[**CheckVerification200Response**](CheckVerification200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check result: the verification plus &#x60;valid&#x60;. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Verification not found (or already reaped). |  -  |


## createVerification

> Verification createVerification(createVerificationRequest)

Send a verification code

Generate a one-time code, deliver it to the recipient, and store only its hash. Check the user-typed code with POST /v1/verify/verifications/{verificationId}/check.  Re-POSTing for the same (channel, to) while a verification is active RESENDS a fresh code on the existing verification (200 with &#x60;resend: true&#x60;) instead of creating a new one; resends are limited to one per 60 seconds (429 with &#x60;retryAfterSeconds&#x60; inside the cooldown). The stored brandName/codeLength/ttlMinutes win on a resend.  Codes deliver by SMS from a phone number on your account (&#x60;from&#x60; optional when you own exactly one SMS-enabled number) and the message uses a fixed template. Each accepted send bills one verification fee plus the standard message rate. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VerifyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VerifyApi apiInstance = new VerifyApi(defaultClient);
        CreateVerificationRequest createVerificationRequest = new CreateVerificationRequest(); // CreateVerificationRequest | 
        try {
            Verification result = apiInstance.createVerification(createVerificationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VerifyApi#createVerification");
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
| **createVerificationRequest** | [**CreateVerificationRequest**](CreateVerificationRequest.md)|  | |

### Return type

[**Verification**](Verification.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Verification created and the code sent. |  -  |
| **200** | Active verification found: a fresh code was resent (&#x60;resend: true&#x60;). |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Verifications require usage-based billing. |  -  |
| **404** | The &#39;from&#39; number is not an SMS-enabled number on this account. |  -  |
| **409** | The recipient has opted out of messages from your number. |  -  |
| **422** | Verifications need an SMS-enabled number on your account; add one first. |  -  |
| **429** | Resend cooldown or a send cap was hit; &#x60;retryAfterSeconds&#x60; says when to retry. |  -  |

## createVerificationWithHttpInfo

> ApiResponse<Verification> createVerification createVerificationWithHttpInfo(createVerificationRequest)

Send a verification code

Generate a one-time code, deliver it to the recipient, and store only its hash. Check the user-typed code with POST /v1/verify/verifications/{verificationId}/check.  Re-POSTing for the same (channel, to) while a verification is active RESENDS a fresh code on the existing verification (200 with &#x60;resend: true&#x60;) instead of creating a new one; resends are limited to one per 60 seconds (429 with &#x60;retryAfterSeconds&#x60; inside the cooldown). The stored brandName/codeLength/ttlMinutes win on a resend.  Codes deliver by SMS from a phone number on your account (&#x60;from&#x60; optional when you own exactly one SMS-enabled number) and the message uses a fixed template. Each accepted send bills one verification fee plus the standard message rate. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VerifyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VerifyApi apiInstance = new VerifyApi(defaultClient);
        CreateVerificationRequest createVerificationRequest = new CreateVerificationRequest(); // CreateVerificationRequest | 
        try {
            ApiResponse<Verification> response = apiInstance.createVerificationWithHttpInfo(createVerificationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VerifyApi#createVerification");
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
| **createVerificationRequest** | [**CreateVerificationRequest**](CreateVerificationRequest.md)|  | |

### Return type

ApiResponse<[**Verification**](Verification.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Verification created and the code sent. |  -  |
| **200** | Active verification found: a fresh code was resent (&#x60;resend: true&#x60;). |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Verifications require usage-based billing. |  -  |
| **404** | The &#39;from&#39; number is not an SMS-enabled number on this account. |  -  |
| **409** | The recipient has opted out of messages from your number. |  -  |
| **422** | Verifications need an SMS-enabled number on your account; add one first. |  -  |
| **429** | Resend cooldown or a send cap was hit; &#x60;retryAfterSeconds&#x60; says when to retry. |  -  |


## getVerification

> Verification getVerification(verificationId)

Get a verification

Current state of a verification. &#x60;status&#x60; is effective (a pending code past its expiry reads as &#x60;expired&#x60;). Verification records are deleted 24 hours after creation, after which this returns 404. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VerifyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VerifyApi apiInstance = new VerifyApi(defaultClient);
        String verificationId = "verificationId_example"; // String | 
        try {
            Verification result = apiInstance.getVerification(verificationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling VerifyApi#getVerification");
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
| **verificationId** | **String**|  | |

### Return type

[**Verification**](Verification.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The verification. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Verification not found (or already reaped). |  -  |

## getVerificationWithHttpInfo

> ApiResponse<Verification> getVerification getVerificationWithHttpInfo(verificationId)

Get a verification

Current state of a verification. &#x60;status&#x60; is effective (a pending code past its expiry reads as &#x60;expired&#x60;). Verification records are deleted 24 hours after creation, after which this returns 404. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.VerifyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        VerifyApi apiInstance = new VerifyApi(defaultClient);
        String verificationId = "verificationId_example"; // String | 
        try {
            ApiResponse<Verification> response = apiInstance.getVerificationWithHttpInfo(verificationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling VerifyApi#getVerification");
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
| **verificationId** | **String**|  | |

### Return type

ApiResponse<[**Verification**](Verification.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The verification. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Verification not found (or already reaped). |  -  |

