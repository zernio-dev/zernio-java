# AdTargetingApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**estimateAdReach**](AdTargetingApi.md#estimateAdReach) | **POST** /v1/ads/targeting/reach-estimate | Estimate audience reach |
| [**estimateAdReachWithHttpInfo**](AdTargetingApi.md#estimateAdReachWithHttpInfo) | **POST** /v1/ads/targeting/reach-estimate | Estimate audience reach |
| [**getLinkedInBidPricing**](AdTargetingApi.md#getLinkedInBidPricing) | **POST** /v1/ads/targeting/bid-pricing | Suggested bid and budget bounds |
| [**getLinkedInBidPricingWithHttpInfo**](AdTargetingApi.md#getLinkedInBidPricingWithHttpInfo) | **POST** /v1/ads/targeting/bid-pricing | Suggested bid and budget bounds |
| [**getLinkedInSupplyForecast**](AdTargetingApi.md#getLinkedInSupplyForecast) | **POST** /v1/ads/targeting/supply-forecast | Impressions, clicks and spend forecast |
| [**getLinkedInSupplyForecastWithHttpInfo**](AdTargetingApi.md#getLinkedInSupplyForecastWithHttpInfo) | **POST** /v1/ads/targeting/supply-forecast | Impressions, clicks and spend forecast |
| [**searchAdInterests**](AdTargetingApi.md#searchAdInterests) | **GET** /v1/ads/interests | Search targeting interests |
| [**searchAdInterestsWithHttpInfo**](AdTargetingApi.md#searchAdInterestsWithHttpInfo) | **GET** /v1/ads/interests | Search targeting interests |
| [**searchAdTargeting**](AdTargetingApi.md#searchAdTargeting) | **GET** /v1/ads/targeting/search | Search targeting options |
| [**searchAdTargetingWithHttpInfo**](AdTargetingApi.md#searchAdTargetingWithHttpInfo) | **GET** /v1/ads/targeting/search | Search targeting options |



## estimateAdReach

> EstimateAdReach200Response estimateAdReach(estimateAdReachRequest)

Estimate audience reach

Returns a normalized pre-flight audience-size estimate for a targeting spec, before any campaign is created. Backed by each platform&#39;s native reach API (Meta &#x60;delivery_estimate&#x60;, LinkedIn &#x60;audienceCounts&#x60;, X &#x60;audience_summary&#x60;, Pinterest &#x60;audience_sizing&#x60;).  Platforms without a usable pre-flight reach API (Google Search/Display, TikTok) return &#x60;available: false&#x60; with no bounds, so clients can hide or grey out the estimate rather than treat the absence as an error. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        EstimateAdReachRequest estimateAdReachRequest = new EstimateAdReachRequest(); // EstimateAdReachRequest | 
        try {
            EstimateAdReach200Response result = apiInstance.estimateAdReach(estimateAdReachRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#estimateAdReach");
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
| **estimateAdReachRequest** | [**EstimateAdReachRequest**](EstimateAdReachRequest.md)|  | |

### Return type

[**EstimateAdReach200Response**](EstimateAdReach200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normalized reach estimate |  -  |
| **400** | Missing required fields or a targeting field the platform cannot honour |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## estimateAdReachWithHttpInfo

> ApiResponse<EstimateAdReach200Response> estimateAdReach estimateAdReachWithHttpInfo(estimateAdReachRequest)

Estimate audience reach

Returns a normalized pre-flight audience-size estimate for a targeting spec, before any campaign is created. Backed by each platform&#39;s native reach API (Meta &#x60;delivery_estimate&#x60;, LinkedIn &#x60;audienceCounts&#x60;, X &#x60;audience_summary&#x60;, Pinterest &#x60;audience_sizing&#x60;).  Platforms without a usable pre-flight reach API (Google Search/Display, TikTok) return &#x60;available: false&#x60; with no bounds, so clients can hide or grey out the estimate rather than treat the absence as an error. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        EstimateAdReachRequest estimateAdReachRequest = new EstimateAdReachRequest(); // EstimateAdReachRequest | 
        try {
            ApiResponse<EstimateAdReach200Response> response = apiInstance.estimateAdReachWithHttpInfo(estimateAdReachRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#estimateAdReach");
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
| **estimateAdReachRequest** | [**EstimateAdReachRequest**](EstimateAdReachRequest.md)|  | |

### Return type

ApiResponse<[**EstimateAdReach200Response**](EstimateAdReach200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normalized reach estimate |  -  |
| **400** | Missing required fields or a targeting field the platform cannot honour |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## getLinkedInBidPricing

> GetLinkedInBidPricing200Response getLinkedInBidPricing(getLinkedInBidPricingRequest)

Suggested bid and budget bounds

LinkedIn-only. Returns the suggested bid and bid limits for a targeting spec, plus the daily-budget bounds LinkedIn will accept. Use it before creating a campaign to pick a bid inside the allowed range and warn the user if their daily budget is below the minimum. Wraps LinkedIn&#39;s &#x60;adBudgetPricing&#x60; finder.  Non-LinkedIn accounts return &#x60;available: false&#x60; so clients can hide the pricing UI without treating it as a failure. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        GetLinkedInBidPricingRequest getLinkedInBidPricingRequest = new GetLinkedInBidPricingRequest(); // GetLinkedInBidPricingRequest | 
        try {
            GetLinkedInBidPricing200Response result = apiInstance.getLinkedInBidPricing(getLinkedInBidPricingRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#getLinkedInBidPricing");
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
| **getLinkedInBidPricingRequest** | [**GetLinkedInBidPricingRequest**](GetLinkedInBidPricingRequest.md)|  | |

### Return type

[**GetLinkedInBidPricing200Response**](GetLinkedInBidPricing200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pricing insights |  -  |
| **400** | Invalid targeting or unsupported objective/optimization/bid combination. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |

## getLinkedInBidPricingWithHttpInfo

> ApiResponse<GetLinkedInBidPricing200Response> getLinkedInBidPricing getLinkedInBidPricingWithHttpInfo(getLinkedInBidPricingRequest)

Suggested bid and budget bounds

LinkedIn-only. Returns the suggested bid and bid limits for a targeting spec, plus the daily-budget bounds LinkedIn will accept. Use it before creating a campaign to pick a bid inside the allowed range and warn the user if their daily budget is below the minimum. Wraps LinkedIn&#39;s &#x60;adBudgetPricing&#x60; finder.  Non-LinkedIn accounts return &#x60;available: false&#x60; so clients can hide the pricing UI without treating it as a failure. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        GetLinkedInBidPricingRequest getLinkedInBidPricingRequest = new GetLinkedInBidPricingRequest(); // GetLinkedInBidPricingRequest | 
        try {
            ApiResponse<GetLinkedInBidPricing200Response> response = apiInstance.getLinkedInBidPricingWithHttpInfo(getLinkedInBidPricingRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#getLinkedInBidPricing");
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
| **getLinkedInBidPricingRequest** | [**GetLinkedInBidPricingRequest**](GetLinkedInBidPricingRequest.md)|  | |

### Return type

ApiResponse<[**GetLinkedInBidPricing200Response**](GetLinkedInBidPricing200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pricing insights |  -  |
| **400** | Invalid targeting or unsupported objective/optimization/bid combination. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |


## getLinkedInSupplyForecast

> GetLinkedInSupplyForecast200Response getLinkedInSupplyForecast(getLinkedInSupplyForecastRequest)

Impressions, clicks and spend forecast

LinkedIn-only. Forecasted impressions, clicks, spend and ~20 other metrics for a targeting spec over a time range. Wraps LinkedIn&#39;s &#x60;adSupplyForecasts&#x60; finder.  Each returned series carries a &#x60;metricType&#x60; (IMPRESSION, CLICK, SPENDING, MAX_POTENTIAL_BUDGET, COST_PER_MILLION_IMPRESSIONS, ...) and a &#x60;granularity&#x60; (DAILY, SEVEN_DAY, THIRTY_DAY, CUSTOM). LinkedIn caps the daily spending forecast at 1.2x the daily budget and returns 0 once the total budget is exhausted.  Non-LinkedIn accounts return &#x60;available: false&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        GetLinkedInSupplyForecastRequest getLinkedInSupplyForecastRequest = new GetLinkedInSupplyForecastRequest(); // GetLinkedInSupplyForecastRequest | 
        try {
            GetLinkedInSupplyForecast200Response result = apiInstance.getLinkedInSupplyForecast(getLinkedInSupplyForecastRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#getLinkedInSupplyForecast");
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
| **getLinkedInSupplyForecastRequest** | [**GetLinkedInSupplyForecastRequest**](GetLinkedInSupplyForecastRequest.md)|  | |

### Return type

[**GetLinkedInSupplyForecast200Response**](GetLinkedInSupplyForecast200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forecast series |  -  |
| **400** | Invalid targeting, missing budget, or LinkedIn forecast validation error (e.g. END_DATE_MAX_HORIZON_FOR_FORECAST). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |

## getLinkedInSupplyForecastWithHttpInfo

> ApiResponse<GetLinkedInSupplyForecast200Response> getLinkedInSupplyForecast getLinkedInSupplyForecastWithHttpInfo(getLinkedInSupplyForecastRequest)

Impressions, clicks and spend forecast

LinkedIn-only. Forecasted impressions, clicks, spend and ~20 other metrics for a targeting spec over a time range. Wraps LinkedIn&#39;s &#x60;adSupplyForecasts&#x60; finder.  Each returned series carries a &#x60;metricType&#x60; (IMPRESSION, CLICK, SPENDING, MAX_POTENTIAL_BUDGET, COST_PER_MILLION_IMPRESSIONS, ...) and a &#x60;granularity&#x60; (DAILY, SEVEN_DAY, THIRTY_DAY, CUSTOM). LinkedIn caps the daily spending forecast at 1.2x the daily budget and returns 0 once the total budget is exhausted.  Non-LinkedIn accounts return &#x60;available: false&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        GetLinkedInSupplyForecastRequest getLinkedInSupplyForecastRequest = new GetLinkedInSupplyForecastRequest(); // GetLinkedInSupplyForecastRequest | 
        try {
            ApiResponse<GetLinkedInSupplyForecast200Response> response = apiInstance.getLinkedInSupplyForecastWithHttpInfo(getLinkedInSupplyForecastRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#getLinkedInSupplyForecast");
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
| **getLinkedInSupplyForecastRequest** | [**GetLinkedInSupplyForecastRequest**](GetLinkedInSupplyForecastRequest.md)|  | |

### Return type

ApiResponse<[**GetLinkedInSupplyForecast200Response**](GetLinkedInSupplyForecast200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forecast series |  -  |
| **400** | Invalid targeting, missing budget, or LinkedIn forecast validation error (e.g. END_DATE_MAX_HORIZON_FOR_FORECAST). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |


## searchAdInterests

> SearchAdInterests200Response searchAdInterests(q, accountId)

Search targeting interests

Deprecated alias for &#x60;GET /v1/ads/targeting/search?dimension&#x3D;interest&#x60;. Kept for backward compatibility, it returns the legacy &#x60;{ interests: [...] }&#x60; shape rather than the normalized &#x60;{ results: [...] }&#x60;. New integrations should use &#x60;GET /v1/ads/targeting/search&#x60; with &#x60;dimension&#x3D;interest&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        String q = "q_example"; // String | Search query
        String accountId = "accountId_example"; // String | Social account ID
        try {
            SearchAdInterests200Response result = apiInstance.searchAdInterests(q, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#searchAdInterests");
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
| **q** | **String**| Search query | |
| **accountId** | **String**| Social account ID | |

### Return type

[**SearchAdInterests200Response**](SearchAdInterests200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching interests |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## searchAdInterestsWithHttpInfo

> ApiResponse<SearchAdInterests200Response> searchAdInterests searchAdInterestsWithHttpInfo(q, accountId)

Search targeting interests

Deprecated alias for &#x60;GET /v1/ads/targeting/search?dimension&#x3D;interest&#x60;. Kept for backward compatibility, it returns the legacy &#x60;{ interests: [...] }&#x60; shape rather than the normalized &#x60;{ results: [...] }&#x60;. New integrations should use &#x60;GET /v1/ads/targeting/search&#x60; with &#x60;dimension&#x3D;interest&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        String q = "q_example"; // String | Search query
        String accountId = "accountId_example"; // String | Social account ID
        try {
            ApiResponse<SearchAdInterests200Response> response = apiInstance.searchAdInterestsWithHttpInfo(q, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#searchAdInterests");
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
| **q** | **String**| Search query | |
| **accountId** | **String**| Social account ID | |

### Return type

ApiResponse<[**SearchAdInterests200Response**](SearchAdInterests200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching interests |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## searchAdTargeting

> SearchAdTargeting200Response searchAdTargeting(accountId, q, dimension, geoType, countryCode, limit)

Search targeting options

Resolve a human-readable query into the platform&#39;s opaque targeting ids used in the &#x60;TargetingSpec&#x60; (&#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; geo keys, and &#x60;interests&#x60;/&#x60;behaviors&#x60; entity ids) on &#x60;POST /v1/ads/create&#x60;, &#x60;POST /v1/ads/targeting/reach-estimate&#x60;, and &#x60;saved_targeting&#x60; audiences.  The &#x60;dimension&#x60; param selects what is searched, &#x60;geo&#x60; (locations, further scoped by &#x60;geoType&#x60;), &#x60;interest&#x60;, &#x60;behavior&#x60;, or &#x60;income&#x60;. Availability of each dimension varies by platform (e.g. behaviours are Meta/TikTok only). Results are normalized across platforms into a single shape, so the same client code consumes Meta, TikTok, LinkedIn, X, Pinterest, and Google results.  TikTok geo searches return every matching level in one list (&#x60;type&#x60; is &#x60;country&#x60;, &#x60;region&#x60;, &#x60;city&#x60;, &#x60;district&#x60;, or &#x60;metro&#x60; for DMA areas) — &#x60;geoType&#x60; is not applied. Results are scoped to the advertiser&#39;s targetable markets, and every id is usable in &#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;metros&#x60; keys on &#x60;POST /v1/ads/create&#x60;.  For geo queries, &#x60;q&#x60; should contain only the locality name (e.g. &#x60;\&quot;Amsterdam\&quot;&#x60;, not &#x60;\&quot;Amsterdam, NL\&quot;&#x60;). Use &#x60;countryCode&#x60; to disambiguate. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (a connected account on the target ad platform).
        String q = "q_example"; // String | Search query. For geo, the locality name only (no region/country suffix).
        String dimension = "geo"; // String | What to search. `geo` resolves locations (scope further with `geoType`), `interest`/`behavior` resolve audience entities, `income` resolves income-tier options. Defaults to `interest` for backward compatibility with the deprecated /v1/ads/interests alias.
        String geoType = "country"; // String | Only used when `dimension=geo`. The kind of location to resolve. Defaults to `city`.
        String countryCode = "countryCode_example"; // String | ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search.
        Integer limit = 25; // Integer | Maximum results to return.
        try {
            SearchAdTargeting200Response result = apiInstance.searchAdTargeting(accountId, q, dimension, geoType, countryCode, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#searchAdTargeting");
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
| **accountId** | **String**| Social account ID (a connected account on the target ad platform). | |
| **q** | **String**| Search query. For geo, the locality name only (no region/country suffix). | |
| **dimension** | **String**| What to search. &#x60;geo&#x60; resolves locations (scope further with &#x60;geoType&#x60;), &#x60;interest&#x60;/&#x60;behavior&#x60; resolve audience entities, &#x60;income&#x60; resolves income-tier options. Defaults to &#x60;interest&#x60; for backward compatibility with the deprecated /v1/ads/interests alias. | [optional] [default to interest] [enum: geo, interest, behavior, income] |
| **geoType** | **String**| Only used when &#x60;dimension&#x3D;geo&#x60;. The kind of location to resolve. Defaults to &#x60;city&#x60;. | [optional] [default to city] [enum: country, region, city, zip, metro] |
| **countryCode** | **String**| ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search. | [optional] |
| **limit** | **Integer**| Maximum results to return. | [optional] [default to 25] |

### Return type

[**SearchAdTargeting200Response**](SearchAdTargeting200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching targeting options (normalized) |  -  |
| **400** | Missing or invalid query parameters |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Account not found, or the platform does not support the requested dimension |  -  |

## searchAdTargetingWithHttpInfo

> ApiResponse<SearchAdTargeting200Response> searchAdTargeting searchAdTargetingWithHttpInfo(accountId, q, dimension, geoType, countryCode, limit)

Search targeting options

Resolve a human-readable query into the platform&#39;s opaque targeting ids used in the &#x60;TargetingSpec&#x60; (&#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; geo keys, and &#x60;interests&#x60;/&#x60;behaviors&#x60; entity ids) on &#x60;POST /v1/ads/create&#x60;, &#x60;POST /v1/ads/targeting/reach-estimate&#x60;, and &#x60;saved_targeting&#x60; audiences.  The &#x60;dimension&#x60; param selects what is searched, &#x60;geo&#x60; (locations, further scoped by &#x60;geoType&#x60;), &#x60;interest&#x60;, &#x60;behavior&#x60;, or &#x60;income&#x60;. Availability of each dimension varies by platform (e.g. behaviours are Meta/TikTok only). Results are normalized across platforms into a single shape, so the same client code consumes Meta, TikTok, LinkedIn, X, Pinterest, and Google results.  TikTok geo searches return every matching level in one list (&#x60;type&#x60; is &#x60;country&#x60;, &#x60;region&#x60;, &#x60;city&#x60;, &#x60;district&#x60;, or &#x60;metro&#x60; for DMA areas) — &#x60;geoType&#x60; is not applied. Results are scoped to the advertiser&#39;s targetable markets, and every id is usable in &#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;metros&#x60; keys on &#x60;POST /v1/ads/create&#x60;.  For geo queries, &#x60;q&#x60; should contain only the locality name (e.g. &#x60;\&quot;Amsterdam\&quot;&#x60;, not &#x60;\&quot;Amsterdam, NL\&quot;&#x60;). Use &#x60;countryCode&#x60; to disambiguate. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdTargetingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdTargetingApi apiInstance = new AdTargetingApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (a connected account on the target ad platform).
        String q = "q_example"; // String | Search query. For geo, the locality name only (no region/country suffix).
        String dimension = "geo"; // String | What to search. `geo` resolves locations (scope further with `geoType`), `interest`/`behavior` resolve audience entities, `income` resolves income-tier options. Defaults to `interest` for backward compatibility with the deprecated /v1/ads/interests alias.
        String geoType = "country"; // String | Only used when `dimension=geo`. The kind of location to resolve. Defaults to `city`.
        String countryCode = "countryCode_example"; // String | ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search.
        Integer limit = 25; // Integer | Maximum results to return.
        try {
            ApiResponse<SearchAdTargeting200Response> response = apiInstance.searchAdTargetingWithHttpInfo(accountId, q, dimension, geoType, countryCode, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdTargetingApi#searchAdTargeting");
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
| **accountId** | **String**| Social account ID (a connected account on the target ad platform). | |
| **q** | **String**| Search query. For geo, the locality name only (no region/country suffix). | |
| **dimension** | **String**| What to search. &#x60;geo&#x60; resolves locations (scope further with &#x60;geoType&#x60;), &#x60;interest&#x60;/&#x60;behavior&#x60; resolve audience entities, &#x60;income&#x60; resolves income-tier options. Defaults to &#x60;interest&#x60; for backward compatibility with the deprecated /v1/ads/interests alias. | [optional] [default to interest] [enum: geo, interest, behavior, income] |
| **geoType** | **String**| Only used when &#x60;dimension&#x3D;geo&#x60;. The kind of location to resolve. Defaults to &#x60;city&#x60;. | [optional] [default to city] [enum: country, region, city, zip, metro] |
| **countryCode** | **String**| ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search. | [optional] |
| **limit** | **Integer**| Maximum results to return. | [optional] [default to 25] |

### Return type

ApiResponse<[**SearchAdTargeting200Response**](SearchAdTargeting200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching targeting options (normalized) |  -  |
| **400** | Missing or invalid query parameters |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Account not found, or the platform does not support the requested dimension |  -  |

