# ReachAndFrequencyApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelRfReservation**](ReachAndFrequencyApi.md#cancelRfReservation) | **DELETE** /v1/ads/rf-predictions/{predictionId} | Cancel a Reach &amp; Frequency reservation |
| [**cancelRfReservationWithHttpInfo**](ReachAndFrequencyApi.md#cancelRfReservationWithHttpInfo) | **DELETE** /v1/ads/rf-predictions/{predictionId} | Cancel a Reach &amp; Frequency reservation |
| [**createRfPrediction**](ReachAndFrequencyApi.md#createRfPrediction) | **POST** /v1/ads/rf-predictions | Create a Reach &amp; Frequency prediction |
| [**createRfPredictionWithHttpInfo**](ReachAndFrequencyApi.md#createRfPredictionWithHttpInfo) | **POST** /v1/ads/rf-predictions | Create a Reach &amp; Frequency prediction |
| [**getRfPrediction**](ReachAndFrequencyApi.md#getRfPrediction) | **GET** /v1/ads/rf-predictions/{predictionId} | Read a Reach &amp; Frequency prediction |
| [**getRfPredictionWithHttpInfo**](ReachAndFrequencyApi.md#getRfPredictionWithHttpInfo) | **GET** /v1/ads/rf-predictions/{predictionId} | Read a Reach &amp; Frequency prediction |
| [**reserveRfPrediction**](ReachAndFrequencyApi.md#reserveRfPrediction) | **POST** /v1/ads/rf-predictions/{predictionId}/reserve | Reserve a Reach &amp; Frequency prediction |
| [**reserveRfPredictionWithHttpInfo**](ReachAndFrequencyApi.md#reserveRfPredictionWithHttpInfo) | **POST** /v1/ads/rf-predictions/{predictionId}/reserve | Reserve a Reach &amp; Frequency prediction |



## cancelRfReservation

> void cancelRfReservation(predictionId, accountId, adAccountId)

Cancel a Reach &amp; Frequency reservation

Releases a RESERVATION&#39;s locked price and inventory. Unreserved predictions expire on their own.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            apiInstance.cancelRfReservation(predictionId, accountId, adAccountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#cancelRfReservation");
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
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

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
| **200** | Reservation cancelled |  -  |
| **400** | Invalid input, or Meta rejected the cancel |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## cancelRfReservationWithHttpInfo

> ApiResponse<Void> cancelRfReservation cancelRfReservationWithHttpInfo(predictionId, accountId, adAccountId)

Cancel a Reach &amp; Frequency reservation

Releases a RESERVATION&#39;s locked price and inventory. Unreserved predictions expire on their own.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.cancelRfReservationWithHttpInfo(predictionId, accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#cancelRfReservation");
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
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

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
| **200** | Reservation cancelled |  -  |
| **400** | Invalid input, or Meta rejected the cancel |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## createRfPrediction

> CreateRfPrediction201Response createRfPrediction(createRfPredictionRequest)

Create a Reach &amp; Frequency prediction

Creates an R&amp;F prediction — a QUOTE, nothing is bought and no ad entities are created. Provide a date range plus exactly one of &#x60;budgetAmount&#x60; (Meta predicts reach) or &#x60;reach&#x60; (Meta predicts the budget). The response carries the estimate and its allowed bounds (min/max budget and reach). Predictions expire on their own; to buy, reserve one via POST /v1/ads/rf-predictions/{predictionId}/reserve and pass the RESERVED id to POST /v1/ads/create with &#x60;buyingType: \&quot;RESERVED\&quot;&#x60;.  Reservation campaigns reject automatic placements, so omitted &#x60;placements&#x60; default to Facebook feed (+ Instagram stream when a linked IG professional account resolves); Instagram placements require that IG account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        CreateRfPredictionRequest createRfPredictionRequest = new CreateRfPredictionRequest(); // CreateRfPredictionRequest | 
        try {
            CreateRfPrediction201Response result = apiInstance.createRfPrediction(createRfPredictionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#createRfPrediction");
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
| **createRfPredictionRequest** | [**CreateRfPredictionRequest**](CreateRfPredictionRequest.md)|  | |

### Return type

[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Prediction created (usually ready within seconds) |  -  |
| **400** | Invalid input, or Meta rejected the prediction — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page resolved for the account |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createRfPredictionWithHttpInfo

> ApiResponse<CreateRfPrediction201Response> createRfPrediction createRfPredictionWithHttpInfo(createRfPredictionRequest)

Create a Reach &amp; Frequency prediction

Creates an R&amp;F prediction — a QUOTE, nothing is bought and no ad entities are created. Provide a date range plus exactly one of &#x60;budgetAmount&#x60; (Meta predicts reach) or &#x60;reach&#x60; (Meta predicts the budget). The response carries the estimate and its allowed bounds (min/max budget and reach). Predictions expire on their own; to buy, reserve one via POST /v1/ads/rf-predictions/{predictionId}/reserve and pass the RESERVED id to POST /v1/ads/create with &#x60;buyingType: \&quot;RESERVED\&quot;&#x60;.  Reservation campaigns reject automatic placements, so omitted &#x60;placements&#x60; default to Facebook feed (+ Instagram stream when a linked IG professional account resolves); Instagram placements require that IG account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        CreateRfPredictionRequest createRfPredictionRequest = new CreateRfPredictionRequest(); // CreateRfPredictionRequest | 
        try {
            ApiResponse<CreateRfPrediction201Response> response = apiInstance.createRfPredictionWithHttpInfo(createRfPredictionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#createRfPrediction");
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
| **createRfPredictionRequest** | [**CreateRfPredictionRequest**](CreateRfPredictionRequest.md)|  | |

### Return type

ApiResponse<[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Prediction created (usually ready within seconds) |  -  |
| **400** | Invalid input, or Meta rejected the prediction — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page resolved for the account |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getRfPrediction

> CreateRfPrediction201Response getRfPrediction(predictionId, accountId, adAccountId)

Read a Reach &amp; Frequency prediction

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            CreateRfPrediction201Response result = apiInstance.getRfPrediction(predictionId, accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#getRfPrediction");
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
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction status and estimates |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getRfPredictionWithHttpInfo

> ApiResponse<CreateRfPrediction201Response> getRfPrediction getRfPredictionWithHttpInfo(predictionId, accountId, adAccountId)

Read a Reach &amp; Frequency prediction

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ApiResponse<CreateRfPrediction201Response> response = apiInstance.getRfPredictionWithHttpInfo(predictionId, accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#getRfPrediction");
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
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

ApiResponse<[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction status and estimates |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## reserveRfPrediction

> ReserveRfPrediction201Response reserveRfPrediction(predictionId, reserveRfPredictionRequest)

Reserve a Reach &amp; Frequency prediction

Locks the quoted price + inventory until the returned &#x60;expiresAt&#x60; and mints a NEW prediction id — pass that RESERVED id (not the original) as &#x60;rfPredictionId&#x60; on POST /v1/ads/create. Release an unused reservation via DELETE.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        ReserveRfPredictionRequest reserveRfPredictionRequest = new ReserveRfPredictionRequest(); // ReserveRfPredictionRequest | 
        try {
            ReserveRfPrediction201Response result = apiInstance.reserveRfPrediction(predictionId, reserveRfPredictionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#reserveRfPrediction");
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
| **predictionId** | **String**|  | |
| **reserveRfPredictionRequest** | [**ReserveRfPredictionRequest**](ReserveRfPredictionRequest.md)|  | |

### Return type

[**ReserveRfPrediction201Response**](ReserveRfPrediction201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reserved; &#x60;prediction.predictionId&#x60; is the new RESERVED id |  -  |
| **400** | Invalid input, or Meta rejected the reserve |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## reserveRfPredictionWithHttpInfo

> ApiResponse<ReserveRfPrediction201Response> reserveRfPrediction reserveRfPredictionWithHttpInfo(predictionId, reserveRfPredictionRequest)

Reserve a Reach &amp; Frequency prediction

Locks the quoted price + inventory until the returned &#x60;expiresAt&#x60; and mints a NEW prediction id — pass that RESERVED id (not the original) as &#x60;rfPredictionId&#x60; on POST /v1/ads/create. Release an unused reservation via DELETE.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ReachAndFrequencyApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ReachAndFrequencyApi apiInstance = new ReachAndFrequencyApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        ReserveRfPredictionRequest reserveRfPredictionRequest = new ReserveRfPredictionRequest(); // ReserveRfPredictionRequest | 
        try {
            ApiResponse<ReserveRfPrediction201Response> response = apiInstance.reserveRfPredictionWithHttpInfo(predictionId, reserveRfPredictionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ReachAndFrequencyApi#reserveRfPrediction");
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
| **predictionId** | **String**|  | |
| **reserveRfPredictionRequest** | [**ReserveRfPredictionRequest**](ReserveRfPredictionRequest.md)|  | |

### Return type

ApiResponse<[**ReserveRfPrediction201Response**](ReserveRfPrediction201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reserved; &#x60;prediction.predictionId&#x60; is the new RESERVED id |  -  |
| **400** | Invalid input, or Meta rejected the reserve |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

