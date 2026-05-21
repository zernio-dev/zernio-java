# GmbVerificationsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**completeGoogleBusinessVerification**](GmbVerificationsApi.md#completeGoogleBusinessVerification) | **POST** /v1/accounts/{accountId}/gmb-verifications/{verificationId}/complete | Complete a verification |
| [**completeGoogleBusinessVerificationWithHttpInfo**](GmbVerificationsApi.md#completeGoogleBusinessVerificationWithHttpInfo) | **POST** /v1/accounts/{accountId}/gmb-verifications/{verificationId}/complete | Complete a verification |
| [**fetchGoogleBusinessVerificationOptions**](GmbVerificationsApi.md#fetchGoogleBusinessVerificationOptions) | **POST** /v1/accounts/{accountId}/gmb-verifications/options | Fetch verification options |
| [**fetchGoogleBusinessVerificationOptionsWithHttpInfo**](GmbVerificationsApi.md#fetchGoogleBusinessVerificationOptionsWithHttpInfo) | **POST** /v1/accounts/{accountId}/gmb-verifications/options | Fetch verification options |
| [**getGoogleBusinessVerifications**](GmbVerificationsApi.md#getGoogleBusinessVerifications) | **GET** /v1/accounts/{accountId}/gmb-verifications | Get verification state |
| [**getGoogleBusinessVerificationsWithHttpInfo**](GmbVerificationsApi.md#getGoogleBusinessVerificationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-verifications | Get verification state |
| [**startGoogleBusinessVerification**](GmbVerificationsApi.md#startGoogleBusinessVerification) | **POST** /v1/accounts/{accountId}/gmb-verifications | Start a verification |
| [**startGoogleBusinessVerificationWithHttpInfo**](GmbVerificationsApi.md#startGoogleBusinessVerificationWithHttpInfo) | **POST** /v1/accounts/{accountId}/gmb-verifications | Start a verification |



## completeGoogleBusinessVerification

> StartGoogleBusinessVerification200Response completeGoogleBusinessVerification(accountId, verificationId, completeGoogleBusinessVerificationRequest, locationId)

Complete a verification

Completes a PENDING verification by submitting the PIN/code Google sent the business (postcard code, SMS PIN, etc.). On success the verification moves to COMPLETED.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String verificationId = "verificationId_example"; // String | The last segment of a verification `name` from GET /gmb-verifications.
        CompleteGoogleBusinessVerificationRequest completeGoogleBusinessVerificationRequest = new CompleteGoogleBusinessVerificationRequest(); // CompleteGoogleBusinessVerificationRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            StartGoogleBusinessVerification200Response result = apiInstance.completeGoogleBusinessVerification(accountId, verificationId, completeGoogleBusinessVerificationRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#completeGoogleBusinessVerification");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **verificationId** | **String**| The last segment of a verification &#x60;name&#x60; from GET /gmb-verifications. | |
| **completeGoogleBusinessVerificationRequest** | [**CompleteGoogleBusinessVerificationRequest**](CompleteGoogleBusinessVerificationRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

[**StartGoogleBusinessVerification200Response**](StartGoogleBusinessVerification200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification completed |  -  |
| **400** | Invalid request (e.g. wrong PIN or verification not pending) |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |

## completeGoogleBusinessVerificationWithHttpInfo

> ApiResponse<StartGoogleBusinessVerification200Response> completeGoogleBusinessVerification completeGoogleBusinessVerificationWithHttpInfo(accountId, verificationId, completeGoogleBusinessVerificationRequest, locationId)

Complete a verification

Completes a PENDING verification by submitting the PIN/code Google sent the business (postcard code, SMS PIN, etc.). On success the verification moves to COMPLETED.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String verificationId = "verificationId_example"; // String | The last segment of a verification `name` from GET /gmb-verifications.
        CompleteGoogleBusinessVerificationRequest completeGoogleBusinessVerificationRequest = new CompleteGoogleBusinessVerificationRequest(); // CompleteGoogleBusinessVerificationRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            ApiResponse<StartGoogleBusinessVerification200Response> response = apiInstance.completeGoogleBusinessVerificationWithHttpInfo(accountId, verificationId, completeGoogleBusinessVerificationRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#completeGoogleBusinessVerification");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **verificationId** | **String**| The last segment of a verification &#x60;name&#x60; from GET /gmb-verifications. | |
| **completeGoogleBusinessVerificationRequest** | [**CompleteGoogleBusinessVerificationRequest**](CompleteGoogleBusinessVerificationRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

ApiResponse<[**StartGoogleBusinessVerification200Response**](StartGoogleBusinessVerification200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification completed |  -  |
| **400** | Invalid request (e.g. wrong PIN or verification not pending) |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |


## fetchGoogleBusinessVerificationOptions

> FetchGoogleBusinessVerificationOptions200Response fetchGoogleBusinessVerificationOptions(accountId, fetchGoogleBusinessVerificationOptionsRequest, locationId)

Fetch verification options

Reports the verification methods Google currently offers for the location. Non-mutating (nothing is sent to the business). &#x60;languageCode&#x60; is required; service-area (\&quot;CUSTOMER_LOCATION_ONLY\&quot;) businesses also require &#x60;context.address&#x60;, otherwise Google returns 400.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        FetchGoogleBusinessVerificationOptionsRequest fetchGoogleBusinessVerificationOptionsRequest = new FetchGoogleBusinessVerificationOptionsRequest(); // FetchGoogleBusinessVerificationOptionsRequest | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location.
        try {
            FetchGoogleBusinessVerificationOptions200Response result = apiInstance.fetchGoogleBusinessVerificationOptions(accountId, fetchGoogleBusinessVerificationOptionsRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#fetchGoogleBusinessVerificationOptions");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **fetchGoogleBusinessVerificationOptionsRequest** | [**FetchGoogleBusinessVerificationOptionsRequest**](FetchGoogleBusinessVerificationOptionsRequest.md)|  | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

[**FetchGoogleBusinessVerificationOptions200Response**](FetchGoogleBusinessVerificationOptions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification options fetched |  -  |
| **400** | Invalid request (e.g. missing service business context, or missing languageCode) |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |

## fetchGoogleBusinessVerificationOptionsWithHttpInfo

> ApiResponse<FetchGoogleBusinessVerificationOptions200Response> fetchGoogleBusinessVerificationOptions fetchGoogleBusinessVerificationOptionsWithHttpInfo(accountId, fetchGoogleBusinessVerificationOptionsRequest, locationId)

Fetch verification options

Reports the verification methods Google currently offers for the location. Non-mutating (nothing is sent to the business). &#x60;languageCode&#x60; is required; service-area (\&quot;CUSTOMER_LOCATION_ONLY\&quot;) businesses also require &#x60;context.address&#x60;, otherwise Google returns 400.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        FetchGoogleBusinessVerificationOptionsRequest fetchGoogleBusinessVerificationOptionsRequest = new FetchGoogleBusinessVerificationOptionsRequest(); // FetchGoogleBusinessVerificationOptionsRequest | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location.
        try {
            ApiResponse<FetchGoogleBusinessVerificationOptions200Response> response = apiInstance.fetchGoogleBusinessVerificationOptionsWithHttpInfo(accountId, fetchGoogleBusinessVerificationOptionsRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#fetchGoogleBusinessVerificationOptions");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **fetchGoogleBusinessVerificationOptionsRequest** | [**FetchGoogleBusinessVerificationOptionsRequest**](FetchGoogleBusinessVerificationOptionsRequest.md)|  | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

ApiResponse<[**FetchGoogleBusinessVerificationOptions200Response**](FetchGoogleBusinessVerificationOptions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification options fetched |  -  |
| **400** | Invalid request (e.g. missing service business context, or missing languageCode) |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |


## getGoogleBusinessVerifications

> GetGoogleBusinessVerifications200Response getGoogleBusinessVerifications(accountId, locationId)

Get verification state

Returns the location&#39;s Voice of Merchant state plus its verification history. &#x60;voiceOfMerchantState.hasVoiceOfMerchant&#x60; tells you whether the listing is verified and published; when it is false, &#x60;verify&#x60; reports whether a verification is already pending. Each entry in &#x60;verifications&#x60; has a &#x60;state&#x60; of PENDING, COMPLETED, or FAILED.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            GetGoogleBusinessVerifications200Response result = apiInstance.getGoogleBusinessVerifications(accountId, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#getGoogleBusinessVerifications");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

[**GetGoogleBusinessVerifications200Response**](GetGoogleBusinessVerifications200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification state fetched successfully |  -  |
| **400** | Not a Google Business account or missing location |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |

## getGoogleBusinessVerificationsWithHttpInfo

> ApiResponse<GetGoogleBusinessVerifications200Response> getGoogleBusinessVerifications getGoogleBusinessVerificationsWithHttpInfo(accountId, locationId)

Get verification state

Returns the location&#39;s Voice of Merchant state plus its verification history. &#x60;voiceOfMerchantState.hasVoiceOfMerchant&#x60; tells you whether the listing is verified and published; when it is false, &#x60;verify&#x60; reports whether a verification is already pending. Each entry in &#x60;verifications&#x60; has a &#x60;state&#x60; of PENDING, COMPLETED, or FAILED.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            ApiResponse<GetGoogleBusinessVerifications200Response> response = apiInstance.getGoogleBusinessVerificationsWithHttpInfo(accountId, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#getGoogleBusinessVerifications");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

ApiResponse<[**GetGoogleBusinessVerifications200Response**](GetGoogleBusinessVerifications200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification state fetched successfully |  -  |
| **400** | Not a Google Business account or missing location |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |


## startGoogleBusinessVerification

> StartGoogleBusinessVerification200Response startGoogleBusinessVerification(accountId, startGoogleBusinessVerificationRequest, locationId)

Start a verification

Starts a verification for the location. This is a mutating action: depending on &#x60;method&#x60;, Google mails a postcard, places a call, or sends an SMS/email to the business. Submit the resulting code with POST /gmb-verifications/{verificationId}/complete. Use POST /gmb-verifications/options first to discover which methods are eligible.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        StartGoogleBusinessVerificationRequest startGoogleBusinessVerificationRequest = new StartGoogleBusinessVerificationRequest(); // StartGoogleBusinessVerificationRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            StartGoogleBusinessVerification200Response result = apiInstance.startGoogleBusinessVerification(accountId, startGoogleBusinessVerificationRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#startGoogleBusinessVerification");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **startGoogleBusinessVerificationRequest** | [**StartGoogleBusinessVerificationRequest**](StartGoogleBusinessVerificationRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

[**StartGoogleBusinessVerification200Response**](StartGoogleBusinessVerification200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification started |  -  |
| **400** | Invalid request (e.g. wrong field for the chosen method, or Google rejected it) |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |

## startGoogleBusinessVerificationWithHttpInfo

> ApiResponse<StartGoogleBusinessVerification200Response> startGoogleBusinessVerification startGoogleBusinessVerificationWithHttpInfo(accountId, startGoogleBusinessVerificationRequest, locationId)

Start a verification

Starts a verification for the location. This is a mutating action: depending on &#x60;method&#x60;, Google mails a postcard, places a call, or sends an SMS/email to the business. Submit the resulting code with POST /gmb-verifications/{verificationId}/complete. Use POST /gmb-verifications/options first to discover which methods are eligible.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbVerificationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbVerificationsApi apiInstance = new GmbVerificationsApi(defaultClient);
        String accountId = "accountId_example"; // String | The Zernio account ID (from /v1/accounts)
        StartGoogleBusinessVerificationRequest startGoogleBusinessVerificationRequest = new StartGoogleBusinessVerificationRequest(); // StartGoogleBusinessVerificationRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location.
        try {
            ApiResponse<StartGoogleBusinessVerification200Response> response = apiInstance.startGoogleBusinessVerificationWithHttpInfo(accountId, startGoogleBusinessVerificationRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbVerificationsApi#startGoogleBusinessVerification");
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
| **accountId** | **String**| The Zernio account ID (from /v1/accounts) | |
| **startGoogleBusinessVerificationRequest** | [**StartGoogleBusinessVerificationRequest**](StartGoogleBusinessVerificationRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. | [optional] |

### Return type

ApiResponse<[**StartGoogleBusinessVerification200Response**](StartGoogleBusinessVerification200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Verification started |  -  |
| **400** | Invalid request (e.g. wrong field for the chosen method, or Google rejected it) |  -  |
| **401** | Unauthorized or token invalid |  -  |
| **404** | Resource not found |  -  |

