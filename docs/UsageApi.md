# UsageApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUsageStats**](UsageApi.md#getUsageStats) | **GET** /v1/usage-stats | Get plan and usage stats |
| [**getUsageStatsWithHttpInfo**](UsageApi.md#getUsageStatsWithHttpInfo) | **GET** /v1/usage-stats | Get plan and usage stats |
| [**getXApiPricing**](UsageApi.md#getXApiPricing) | **GET** /v1/billing/x-pricing | Get X/Twitter API pricing table |
| [**getXApiPricingWithHttpInfo**](UsageApi.md#getXApiPricingWithHttpInfo) | **GET** /v1/billing/x-pricing | Get X/Twitter API pricing table |



## getUsageStats

> UsageStats getUsageStats()

Get plan and usage stats

Returns the current plan name, billing period, plan limits, and usage counts.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCalls&#x60; (aggregated by tier), &#x60;usage.xApiCallsByOperation&#x60;     (per-operation map — resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;),     plus a &#x60;spend&#x60; block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsageApi apiInstance = new UsageApi(defaultClient);
        try {
            UsageStats result = apiInstance.getUsageStats();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getUsageStats");
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

[**UsageStats**](UsageStats.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Usage stats |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getUsageStatsWithHttpInfo

> ApiResponse<UsageStats> getUsageStats getUsageStatsWithHttpInfo()

Get plan and usage stats

Returns the current plan name, billing period, plan limits, and usage counts.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCalls&#x60; (aggregated by tier), &#x60;usage.xApiCallsByOperation&#x60;     (per-operation map — resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;),     plus a &#x60;spend&#x60; block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsageApi apiInstance = new UsageApi(defaultClient);
        try {
            ApiResponse<UsageStats> response = apiInstance.getUsageStatsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getUsageStats");
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

ApiResponse<[**UsageStats**](UsageStats.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Usage stats |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getXApiPricing

> XApiPricing getXApiPricing()

Get X/Twitter API pricing table

Returns Zernio&#39;s canonical X/Twitter API pricing table. Each X action has its own Metronome product and its own rate, and Zernio passes X API costs through at exact rates with zero markup.  The response is identical for every authenticated user (pricing is universal), so it is safe to cache on the client for the duration of a billing period.  To compute your own per-operation spend, pair this endpoint with &#x60;GET /v1/usage-stats&#x60; — that endpoint returns &#x60;usage.xApiCallsByOperation&#x60; keyed by the same &#x60;operation&#x60; field you get here. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsageApi apiInstance = new UsageApi(defaultClient);
        try {
            XApiPricing result = apiInstance.getXApiPricing();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getXApiPricing");
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

[**XApiPricing**](XApiPricing.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | X pricing table |  -  |
| **401** | Unauthorized |  -  |

## getXApiPricingWithHttpInfo

> ApiResponse<XApiPricing> getXApiPricing getXApiPricingWithHttpInfo()

Get X/Twitter API pricing table

Returns Zernio&#39;s canonical X/Twitter API pricing table. Each X action has its own Metronome product and its own rate, and Zernio passes X API costs through at exact rates with zero markup.  The response is identical for every authenticated user (pricing is universal), so it is safe to cache on the client for the duration of a billing period.  To compute your own per-operation spend, pair this endpoint with &#x60;GET /v1/usage-stats&#x60; — that endpoint returns &#x60;usage.xApiCallsByOperation&#x60; keyed by the same &#x60;operation&#x60; field you get here. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.UsageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        UsageApi apiInstance = new UsageApi(defaultClient);
        try {
            ApiResponse<XApiPricing> response = apiInstance.getXApiPricingWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getXApiPricing");
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

ApiResponse<[**XApiPricing**](XApiPricing.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | X pricing table |  -  |
| **401** | Unauthorized |  -  |

