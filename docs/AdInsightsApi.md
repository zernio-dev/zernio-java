# AdInsightsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdInsightsReport**](AdInsightsApi.md#createAdInsightsReport) | **POST** /v1/ads/insights/reports | Submit an async insights report run |
| [**createAdInsightsReportWithHttpInfo**](AdInsightsApi.md#createAdInsightsReportWithHttpInfo) | **POST** /v1/ads/insights/reports | Submit an async insights report run |
| [**generateKeywordHistoricalMetrics**](AdInsightsApi.md#generateKeywordHistoricalMetrics) | **POST** /v1/ads/keywords/historical-metrics | Historical keyword metrics (Google Keyword Planner) |
| [**generateKeywordHistoricalMetricsWithHttpInfo**](AdInsightsApi.md#generateKeywordHistoricalMetricsWithHttpInfo) | **POST** /v1/ads/keywords/historical-metrics | Historical keyword metrics (Google Keyword Planner) |
| [**generateKeywordIdeas**](AdInsightsApi.md#generateKeywordIdeas) | **POST** /v1/ads/keywords/ideas | Generate keyword ideas (Google Keyword Planner) |
| [**generateKeywordIdeasWithHttpInfo**](AdInsightsApi.md#generateKeywordIdeasWithHttpInfo) | **POST** /v1/ads/keywords/ideas | Generate keyword ideas (Google Keyword Planner) |
| [**getAdAnalytics**](AdInsightsApi.md#getAdAnalytics) | **GET** /v1/ads/{adId}/analytics | Get ad analytics |
| [**getAdAnalyticsWithHttpInfo**](AdInsightsApi.md#getAdAnalyticsWithHttpInfo) | **GET** /v1/ads/{adId}/analytics | Get ad analytics |
| [**getAdInsightsReport**](AdInsightsApi.md#getAdInsightsReport) | **GET** /v1/ads/insights/reports/{reportRunId} | Poll an async insights report run |
| [**getAdInsightsReportWithHttpInfo**](AdInsightsApi.md#getAdInsightsReportWithHttpInfo) | **GET** /v1/ads/insights/reports/{reportRunId} | Poll an async insights report run |
| [**getAdsSearchTerms**](AdInsightsApi.md#getAdsSearchTerms) | **GET** /v1/ads/search-terms | Google Ads search terms report |
| [**getAdsSearchTermsWithHttpInfo**](AdInsightsApi.md#getAdsSearchTermsWithHttpInfo) | **GET** /v1/ads/search-terms | Google Ads search terms report |
| [**getCampaignAnalytics**](AdInsightsApi.md#getCampaignAnalytics) | **GET** /v1/ads/campaigns/{campaignId}/analytics | Get campaign analytics |
| [**getCampaignAnalyticsWithHttpInfo**](AdInsightsApi.md#getCampaignAnalyticsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/analytics | Get campaign analytics |
| [**queryAdInsights**](AdInsightsApi.md#queryAdInsights) | **GET** /v1/ads/insights | Flexible live insights query |
| [**queryAdInsightsWithHttpInfo**](AdInsightsApi.md#queryAdInsightsWithHttpInfo) | **GET** /v1/ads/insights | Flexible live insights query |



## createAdInsightsReport

> CreateAdInsightsReport202Response createAdInsightsReport(createAdInsightsReportRequest)

Submit an async insights report run

Submits an asynchronous Meta insights report. Same query surface as GET /v1/ads/insights, but in the JSON body; Meta processes the report server-side, which is the right choice for long ranges or large accounts where the sync query is slow or rate-limited. Returns a &#x60;reportRunId&#x60; to poll via GET /v1/ads/insights/reports/{reportRunId}. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        CreateAdInsightsReportRequest createAdInsightsReportRequest = new CreateAdInsightsReportRequest(); // CreateAdInsightsReportRequest | 
        try {
            CreateAdInsightsReport202Response result = apiInstance.createAdInsightsReport(createAdInsightsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#createAdInsightsReport");
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
| **createAdInsightsReportRequest** | [**CreateAdInsightsReportRequest**](CreateAdInsightsReportRequest.md)|  | |

### Return type

[**CreateAdInsightsReport202Response**](CreateAdInsightsReport202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Report run submitted |  -  |
| **400** | Invalid input, or Meta rejected the report parameters |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createAdInsightsReportWithHttpInfo

> ApiResponse<CreateAdInsightsReport202Response> createAdInsightsReport createAdInsightsReportWithHttpInfo(createAdInsightsReportRequest)

Submit an async insights report run

Submits an asynchronous Meta insights report. Same query surface as GET /v1/ads/insights, but in the JSON body; Meta processes the report server-side, which is the right choice for long ranges or large accounts where the sync query is slow or rate-limited. Returns a &#x60;reportRunId&#x60; to poll via GET /v1/ads/insights/reports/{reportRunId}. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        CreateAdInsightsReportRequest createAdInsightsReportRequest = new CreateAdInsightsReportRequest(); // CreateAdInsightsReportRequest | 
        try {
            ApiResponse<CreateAdInsightsReport202Response> response = apiInstance.createAdInsightsReportWithHttpInfo(createAdInsightsReportRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#createAdInsightsReport");
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
| **createAdInsightsReportRequest** | [**CreateAdInsightsReportRequest**](CreateAdInsightsReportRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdInsightsReport202Response**](CreateAdInsightsReport202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Report run submitted |  -  |
| **400** | Invalid input, or Meta rejected the report parameters |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## generateKeywordHistoricalMetrics

> GenerateKeywordHistoricalMetrics200Response generateKeywordHistoricalMetrics(generateKeywordHistoricalMetricsRequest)

Historical keyword metrics (Google Keyword Planner)

Google Ads only. Runs Keyword Planner&#39;s generateKeywordHistoricalMetrics for up to 1,000 exact keywords: historical search volume, competition and top-of-page bid ranges, plus averageCpcMicros when includeAverageCpc is set. Rows come back verbatim; counters are int64s encoded as strings, bid/CPC values are micros of the account currency. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        GenerateKeywordHistoricalMetricsRequest generateKeywordHistoricalMetricsRequest = new GenerateKeywordHistoricalMetricsRequest(); // GenerateKeywordHistoricalMetricsRequest | 
        try {
            GenerateKeywordHistoricalMetrics200Response result = apiInstance.generateKeywordHistoricalMetrics(generateKeywordHistoricalMetricsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#generateKeywordHistoricalMetrics");
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
| **generateKeywordHistoricalMetricsRequest** | [**GenerateKeywordHistoricalMetricsRequest**](GenerateKeywordHistoricalMetricsRequest.md)|  | |

### Return type

[**GenerateKeywordHistoricalMetrics200Response**](GenerateKeywordHistoricalMetrics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Historical metric rows (raw Keyword Planner shape) |  -  |
| **400** | Invalid input, or Google rejected the request — message carries Google&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Per-user Google Ads operations budget or the shared Google quota reached; the message says which and when it resets. |  -  |
| **501** | Only supported on Google Ads |  -  |

## generateKeywordHistoricalMetricsWithHttpInfo

> ApiResponse<GenerateKeywordHistoricalMetrics200Response> generateKeywordHistoricalMetrics generateKeywordHistoricalMetricsWithHttpInfo(generateKeywordHistoricalMetricsRequest)

Historical keyword metrics (Google Keyword Planner)

Google Ads only. Runs Keyword Planner&#39;s generateKeywordHistoricalMetrics for up to 1,000 exact keywords: historical search volume, competition and top-of-page bid ranges, plus averageCpcMicros when includeAverageCpc is set. Rows come back verbatim; counters are int64s encoded as strings, bid/CPC values are micros of the account currency. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        GenerateKeywordHistoricalMetricsRequest generateKeywordHistoricalMetricsRequest = new GenerateKeywordHistoricalMetricsRequest(); // GenerateKeywordHistoricalMetricsRequest | 
        try {
            ApiResponse<GenerateKeywordHistoricalMetrics200Response> response = apiInstance.generateKeywordHistoricalMetricsWithHttpInfo(generateKeywordHistoricalMetricsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#generateKeywordHistoricalMetrics");
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
| **generateKeywordHistoricalMetricsRequest** | [**GenerateKeywordHistoricalMetricsRequest**](GenerateKeywordHistoricalMetricsRequest.md)|  | |

### Return type

ApiResponse<[**GenerateKeywordHistoricalMetrics200Response**](GenerateKeywordHistoricalMetrics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Historical metric rows (raw Keyword Planner shape) |  -  |
| **400** | Invalid input, or Google rejected the request — message carries Google&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Per-user Google Ads operations budget or the shared Google quota reached; the message says which and when it resets. |  -  |
| **501** | Only supported on Google Ads |  -  |


## generateKeywordIdeas

> GenerateKeywordIdeas200Response generateKeywordIdeas(generateKeywordIdeasRequest)

Generate keyword ideas (Google Keyword Planner)

Google Ads only. Runs Keyword Planner&#39;s generateKeywordIdeas from seed keywords, a seed URL, or both, returning idea rows verbatim (avgMonthlySearches, competition, competitionIndex, top-of-page bid micros, monthlySearchVolumes). Counters are int64s encoded as strings; bid values are micros of the account currency. Omitting &#x60;countries&#x60; targets worldwide. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        GenerateKeywordIdeasRequest generateKeywordIdeasRequest = new GenerateKeywordIdeasRequest(); // GenerateKeywordIdeasRequest | 
        try {
            GenerateKeywordIdeas200Response result = apiInstance.generateKeywordIdeas(generateKeywordIdeasRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#generateKeywordIdeas");
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
| **generateKeywordIdeasRequest** | [**GenerateKeywordIdeasRequest**](GenerateKeywordIdeasRequest.md)|  | |

### Return type

[**GenerateKeywordIdeas200Response**](GenerateKeywordIdeas200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keyword idea rows (raw Keyword Planner shape) |  -  |
| **400** | Invalid input, or Google rejected the request — message carries Google&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Per-user Google Ads operations budget or the shared Google quota reached; the message says which and when it resets. |  -  |
| **501** | Only supported on Google Ads |  -  |

## generateKeywordIdeasWithHttpInfo

> ApiResponse<GenerateKeywordIdeas200Response> generateKeywordIdeas generateKeywordIdeasWithHttpInfo(generateKeywordIdeasRequest)

Generate keyword ideas (Google Keyword Planner)

Google Ads only. Runs Keyword Planner&#39;s generateKeywordIdeas from seed keywords, a seed URL, or both, returning idea rows verbatim (avgMonthlySearches, competition, competitionIndex, top-of-page bid micros, monthlySearchVolumes). Counters are int64s encoded as strings; bid values are micros of the account currency. Omitting &#x60;countries&#x60; targets worldwide. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        GenerateKeywordIdeasRequest generateKeywordIdeasRequest = new GenerateKeywordIdeasRequest(); // GenerateKeywordIdeasRequest | 
        try {
            ApiResponse<GenerateKeywordIdeas200Response> response = apiInstance.generateKeywordIdeasWithHttpInfo(generateKeywordIdeasRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#generateKeywordIdeas");
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
| **generateKeywordIdeasRequest** | [**GenerateKeywordIdeasRequest**](GenerateKeywordIdeasRequest.md)|  | |

### Return type

ApiResponse<[**GenerateKeywordIdeas200Response**](GenerateKeywordIdeas200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keyword idea rows (raw Keyword Planner shape) |  -  |
| **400** | Invalid input, or Google rejected the request — message carries Google&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Per-user Google Ads operations budget or the shared Google quota reached; the message says which and when it resets. |  -  |
| **501** | Only supported on Google Ads |  -  |


## getAdAnalytics

> GetAdAnalytics200Response getAdAnalytics(adId, fromDate, toDate, breakdowns)

Get ad analytics

Returns detailed performance analytics for an ad. Includes summary metrics, a daily timeline over the requested date range, and optional demographic breakdowns (Meta and TikTok only). If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String adId = "adId_example"; // String | 
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            GetAdAnalytics200Response result = apiInstance.getAdAnalytics(adId, fromDate, toDate, breakdowns);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getAdAnalytics");
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
| **adId** | **String**|  | |
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

[**GetAdAnalytics200Response**](GetAdAnalytics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## getAdAnalyticsWithHttpInfo

> ApiResponse<GetAdAnalytics200Response> getAdAnalytics getAdAnalyticsWithHttpInfo(adId, fromDate, toDate, breakdowns)

Get ad analytics

Returns detailed performance analytics for an ad. Includes summary metrics, a daily timeline over the requested date range, and optional demographic breakdowns (Meta and TikTok only). If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String adId = "adId_example"; // String | 
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            ApiResponse<GetAdAnalytics200Response> response = apiInstance.getAdAnalyticsWithHttpInfo(adId, fromDate, toDate, breakdowns);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getAdAnalytics");
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
| **adId** | **String**|  | |
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

ApiResponse<[**GetAdAnalytics200Response**](GetAdAnalytics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## getAdInsightsReport

> GetAdInsightsReport200Response getAdInsightsReport(reportRunId, accountId, limit, after)

Poll an async insights report run

Status and results for a report run created via POST /v1/ads/insights/reports. While the job runs, returns &#x60;status&#x60; and &#x60;percentCompletion&#x60;. Once &#x60;status&#x60; is \&quot;Job Completed\&quot; the response also carries a &#x60;data&#x60; page, cursor-paginated via &#x60;limit&#x60; / &#x60;after&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String reportRunId = "reportRunId_example"; // String | 
        String accountId = "accountId_example"; // String | Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run).
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        try {
            GetAdInsightsReport200Response result = apiInstance.getAdInsightsReport(reportRunId, accountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getAdInsightsReport");
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
| **reportRunId** | **String**|  | |
| **accountId** | **String**| Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run). | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |

### Return type

[**GetAdInsightsReport200Response**](GetAdInsightsReport200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Report run status (plus results when completed) |  -  |
| **400** | Invalid input, or the report run is not readable with this account&#39;s token |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdInsightsReportWithHttpInfo

> ApiResponse<GetAdInsightsReport200Response> getAdInsightsReport getAdInsightsReportWithHttpInfo(reportRunId, accountId, limit, after)

Poll an async insights report run

Status and results for a report run created via POST /v1/ads/insights/reports. While the job runs, returns &#x60;status&#x60; and &#x60;percentCompletion&#x60;. Once &#x60;status&#x60; is \&quot;Job Completed\&quot; the response also carries a &#x60;data&#x60; page, cursor-paginated via &#x60;limit&#x60; / &#x60;after&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String reportRunId = "reportRunId_example"; // String | 
        String accountId = "accountId_example"; // String | Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run).
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        try {
            ApiResponse<GetAdInsightsReport200Response> response = apiInstance.getAdInsightsReportWithHttpInfo(reportRunId, accountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getAdInsightsReport");
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
| **reportRunId** | **String**|  | |
| **accountId** | **String**| Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run). | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |

### Return type

ApiResponse<[**GetAdInsightsReport200Response**](GetAdInsightsReport200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Report run status (plus results when completed) |  -  |
| **400** | Invalid input, or the report run is not readable with this account&#39;s token |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdsSearchTerms

> GetAdsSearchTerms200Response getAdsSearchTerms(accountId, customerId, fromDate, toDate, campaignId, adGroupId, pageToken)

Google Ads search terms report

The actual search queries that triggered your ads, with matched-keyword status and spend metrics — the raw material for wasted-spend analysis and negative-keyword lists. Reads Google&#39;s &#x60;search_term_view&#x60; live; defaults to the last 30 days. Rows are ordered by cost, descending. Draws on the shared Google Ads operations budget.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String customerId = "customerId_example"; // String | Numeric Google Ads customer id (no dashes). Defaults to the account's connected customer.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Defaults to 30 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Defaults to today.
        String campaignId = "campaignId_example"; // String | Numeric Google campaign id filter.
        String adGroupId = "adGroupId_example"; // String | Numeric Google ad group id filter.
        String pageToken = "pageToken_example"; // String | Cursor from paging.nextPageToken of the previous page.
        try {
            GetAdsSearchTerms200Response result = apiInstance.getAdsSearchTerms(accountId, customerId, fromDate, toDate, campaignId, adGroupId, pageToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getAdsSearchTerms");
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
| **accountId** | **String**| Google ads SocialAccount id. | |
| **customerId** | **String**| Numeric Google Ads customer id (no dashes). Defaults to the account&#39;s connected customer. | [optional] |
| **fromDate** | **LocalDate**| Defaults to 30 days ago. | [optional] |
| **toDate** | **LocalDate**| Defaults to today. | [optional] |
| **campaignId** | **String**| Numeric Google campaign id filter. | [optional] |
| **adGroupId** | **String**| Numeric Google ad group id filter. | [optional] |
| **pageToken** | **String**| Cursor from paging.nextPageToken of the previous page. | [optional] |

### Return type

[**GetAdsSearchTerms200Response**](GetAdsSearchTerms200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search terms |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## getAdsSearchTermsWithHttpInfo

> ApiResponse<GetAdsSearchTerms200Response> getAdsSearchTerms getAdsSearchTermsWithHttpInfo(accountId, customerId, fromDate, toDate, campaignId, adGroupId, pageToken)

Google Ads search terms report

The actual search queries that triggered your ads, with matched-keyword status and spend metrics — the raw material for wasted-spend analysis and negative-keyword lists. Reads Google&#39;s &#x60;search_term_view&#x60; live; defaults to the last 30 days. Rows are ordered by cost, descending. Draws on the shared Google Ads operations budget.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String customerId = "customerId_example"; // String | Numeric Google Ads customer id (no dashes). Defaults to the account's connected customer.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Defaults to 30 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Defaults to today.
        String campaignId = "campaignId_example"; // String | Numeric Google campaign id filter.
        String adGroupId = "adGroupId_example"; // String | Numeric Google ad group id filter.
        String pageToken = "pageToken_example"; // String | Cursor from paging.nextPageToken of the previous page.
        try {
            ApiResponse<GetAdsSearchTerms200Response> response = apiInstance.getAdsSearchTermsWithHttpInfo(accountId, customerId, fromDate, toDate, campaignId, adGroupId, pageToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getAdsSearchTerms");
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
| **accountId** | **String**| Google ads SocialAccount id. | |
| **customerId** | **String**| Numeric Google Ads customer id (no dashes). Defaults to the account&#39;s connected customer. | [optional] |
| **fromDate** | **LocalDate**| Defaults to 30 days ago. | [optional] |
| **toDate** | **LocalDate**| Defaults to today. | [optional] |
| **campaignId** | **String**| Numeric Google campaign id filter. | [optional] |
| **adGroupId** | **String**| Numeric Google ad group id filter. | [optional] |
| **pageToken** | **String**| Cursor from paging.nextPageToken of the previous page. | [optional] |

### Return type

ApiResponse<[**GetAdsSearchTerms200Response**](GetAdsSearchTerms200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search terms |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## getCampaignAnalytics

> GetCampaignAnalytics200Response getCampaignAnalytics(campaignId, platform, fromDate, toDate, breakdowns)

Get campaign analytics

Returns performance analytics for a whole campaign in one call: summary metrics, a daily timeline over the requested date range (summed across the campaign&#39;s ads), and optional demographic breakdowns. Breakdowns are fetched live from Meta at the campaign level (one call per dimension, no per-ad fan-out), so an agency dashboard gets campaign-level age/gender/etc. without summing thousands of per-ad reads. &#x60;campaignId&#x60; is the platform campaign id; pass &#x60;platform&#x60; when a campaign id could be ambiguous across platforms. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign id (platformCampaignId).
        String platform = "platform_example"; // String | Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram).
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            GetCampaignAnalytics200Response result = apiInstance.getCampaignAnalytics(campaignId, platform, fromDate, toDate, breakdowns);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getCampaignAnalytics");
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
| **campaignId** | **String**| Platform campaign id (platformCampaignId). | |
| **platform** | **String**| Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram). | [optional] |
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

[**GetCampaignAnalytics200Response**](GetCampaignAnalytics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## getCampaignAnalyticsWithHttpInfo

> ApiResponse<GetCampaignAnalytics200Response> getCampaignAnalytics getCampaignAnalyticsWithHttpInfo(campaignId, platform, fromDate, toDate, breakdowns)

Get campaign analytics

Returns performance analytics for a whole campaign in one call: summary metrics, a daily timeline over the requested date range (summed across the campaign&#39;s ads), and optional demographic breakdowns. Breakdowns are fetched live from Meta at the campaign level (one call per dimension, no per-ad fan-out), so an agency dashboard gets campaign-level age/gender/etc. without summing thousands of per-ad reads. &#x60;campaignId&#x60; is the platform campaign id; pass &#x60;platform&#x60; when a campaign id could be ambiguous across platforms. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign id (platformCampaignId).
        String platform = "platform_example"; // String | Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram).
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            ApiResponse<GetCampaignAnalytics200Response> response = apiInstance.getCampaignAnalyticsWithHttpInfo(campaignId, platform, fromDate, toDate, breakdowns);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#getCampaignAnalytics");
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
| **campaignId** | **String**| Platform campaign id (platformCampaignId). | |
| **platform** | **String**| Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram). | [optional] |
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

ApiResponse<[**GetCampaignAnalytics200Response**](GetCampaignAnalytics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## queryAdInsights

> QueryAdInsights200Response queryAdInsights(accountId, objectId, query, customerId, pageToken, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after)

Flexible live insights query

Live, flexible insights query. The account&#39;s platform picks the contract:  **Meta (facebook/instagram)**: forwards caller-chosen &#x60;fields&#x60;, &#x60;breakdowns&#x60; and &#x60;filtering&#x60; to any Meta insights node and returns Meta&#39;s rows verbatim. &#x60;objectId&#x60; (required) selects the node; &#x60;level&#x60; sets row granularity. Semantic validation is Meta&#39;s: an unknown field or invalid breakdown combination returns a 400 carrying Meta&#39;s message. For long ranges or agency-scale accounts prefer the async variant (POST /v1/ads/insights/reports).  **Google Ads (googleads)**: raw GAQL passthrough. Send any read-only GAQL SELECT via &#x60;query&#x60; (campaign/keyword/search-term/geo/demographic/asset/shopping resources, &#x60;change_event&#x60;, any &#x60;segments.*&#x60;) and rows come back verbatim (camelCase, counters as strings). Results are paged at a fixed 10,000 rows; follow &#x60;paging.nextPageToken&#x60; with &#x60;pageToken&#x60;. &#x60;customerId&#x60; is only needed when the connection has several Google Ads accounts. Semantic validation is Google&#39;s: an invalid query returns a 400 carrying Google&#39;s message (note: selecting &#x60;segments.date&#x60; requires a finite date filter). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant); its platform selects the Meta or Google contract.
        String objectId = "objectId_example"; // String | Meta only (required there): insights node — act_<n>, campaign id, ad set id or ad id.
        String query = "query_example"; // String | Google only (required there): the GAQL SELECT statement to run.
        String customerId = "customerId_example"; // String | Google only: numeric customer id (no dashes) when the connection has several Google Ads accounts.
        String pageToken = "pageToken_example"; // String | Google only: cursor from paging.nextPageToken of the previous page.
        String level = "ad"; // String | Row granularity
        String fields = "fields_example"; // String | Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted = Meta's default set.
        String breakdowns = "breakdowns_example"; // String | Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform).
        String actionBreakdowns = "actionBreakdowns_example"; // String | Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row.
        String actionAttributionWindows = "actionAttributionWindows_example"; // String | Comma-separated Meta attribution windows. Action values are returned keyed per window.
        String actionReportTime = "actionReportTime_example"; // String | When actions are counted: impression, conversion or mixed.
        Boolean useUnifiedAttributionSetting = true; // Boolean | Use the ad sets' own attribution settings for action counting.
        String filtering = "filtering_example"; // String | JSON array of Meta filter objects: [{\"field\", \"operator\", \"value\"}]. Applied server-side by Meta.
        String datePreset = "datePreset_example"; // String | Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD); requires toDate.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD); requires fromDate.
        String timeIncrement = "timeIncrement_example"; // String | Days per row (1-90), monthly, or all_days.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            QueryAdInsights200Response result = apiInstance.queryAdInsights(accountId, objectId, query, customerId, pageToken, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#queryAdInsights");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant); its platform selects the Meta or Google contract. | |
| **objectId** | **String**| Meta only (required there): insights node — act_&lt;n&gt;, campaign id, ad set id or ad id. | [optional] |
| **query** | **String**| Google only (required there): the GAQL SELECT statement to run. | [optional] |
| **customerId** | **String**| Google only: numeric customer id (no dashes) when the connection has several Google Ads accounts. | [optional] |
| **pageToken** | **String**| Google only: cursor from paging.nextPageToken of the previous page. | [optional] |
| **level** | **String**| Row granularity | [optional] [enum: ad, adset, campaign, account] |
| **fields** | **String**| Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted &#x3D; Meta&#39;s default set. | [optional] |
| **breakdowns** | **String**| Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform). | [optional] |
| **actionBreakdowns** | **String**| Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row. | [optional] |
| **actionAttributionWindows** | **String**| Comma-separated Meta attribution windows. Action values are returned keyed per window. | [optional] |
| **actionReportTime** | **String**| When actions are counted: impression, conversion or mixed. | [optional] |
| **useUnifiedAttributionSetting** | **Boolean**| Use the ad sets&#39; own attribution settings for action counting. | [optional] |
| **filtering** | **String**| JSON array of Meta filter objects: [{\&quot;field\&quot;, \&quot;operator\&quot;, \&quot;value\&quot;}]. Applied server-side by Meta. | [optional] |
| **datePreset** | **String**| Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate. | [optional] |
| **fromDate** | **LocalDate**| Start of range (YYYY-MM-DD); requires toDate. | [optional] |
| **toDate** | **LocalDate**| End of range (YYYY-MM-DD); requires fromDate. | [optional] |
| **timeIncrement** | **String**| Days per row (1-90), monthly, or all_days. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**QueryAdInsights200Response**](QueryAdInsights200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Insight rows (raw platform shape) |  -  |
| **400** | Invalid input, or the platform rejected the query (unknown field, invalid breakdown combo, malformed GAQL) — message carries the platform&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Platform rate limit reached. For Google this is the per-user operations budget or the shared quota; the message says which and when it resets. |  -  |
| **501** | Only supported on Meta (facebook/instagram) and Google Ads |  -  |

## queryAdInsightsWithHttpInfo

> ApiResponse<QueryAdInsights200Response> queryAdInsights queryAdInsightsWithHttpInfo(accountId, objectId, query, customerId, pageToken, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after)

Flexible live insights query

Live, flexible insights query. The account&#39;s platform picks the contract:  **Meta (facebook/instagram)**: forwards caller-chosen &#x60;fields&#x60;, &#x60;breakdowns&#x60; and &#x60;filtering&#x60; to any Meta insights node and returns Meta&#39;s rows verbatim. &#x60;objectId&#x60; (required) selects the node; &#x60;level&#x60; sets row granularity. Semantic validation is Meta&#39;s: an unknown field or invalid breakdown combination returns a 400 carrying Meta&#39;s message. For long ranges or agency-scale accounts prefer the async variant (POST /v1/ads/insights/reports).  **Google Ads (googleads)**: raw GAQL passthrough. Send any read-only GAQL SELECT via &#x60;query&#x60; (campaign/keyword/search-term/geo/demographic/asset/shopping resources, &#x60;change_event&#x60;, any &#x60;segments.*&#x60;) and rows come back verbatim (camelCase, counters as strings). Results are paged at a fixed 10,000 rows; follow &#x60;paging.nextPageToken&#x60; with &#x60;pageToken&#x60;. &#x60;customerId&#x60; is only needed when the connection has several Google Ads accounts. Semantic validation is Google&#39;s: an invalid query returns a 400 carrying Google&#39;s message (note: selecting &#x60;segments.date&#x60; requires a finite date filter). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdInsightsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdInsightsApi apiInstance = new AdInsightsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant); its platform selects the Meta or Google contract.
        String objectId = "objectId_example"; // String | Meta only (required there): insights node — act_<n>, campaign id, ad set id or ad id.
        String query = "query_example"; // String | Google only (required there): the GAQL SELECT statement to run.
        String customerId = "customerId_example"; // String | Google only: numeric customer id (no dashes) when the connection has several Google Ads accounts.
        String pageToken = "pageToken_example"; // String | Google only: cursor from paging.nextPageToken of the previous page.
        String level = "ad"; // String | Row granularity
        String fields = "fields_example"; // String | Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted = Meta's default set.
        String breakdowns = "breakdowns_example"; // String | Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform).
        String actionBreakdowns = "actionBreakdowns_example"; // String | Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row.
        String actionAttributionWindows = "actionAttributionWindows_example"; // String | Comma-separated Meta attribution windows. Action values are returned keyed per window.
        String actionReportTime = "actionReportTime_example"; // String | When actions are counted: impression, conversion or mixed.
        Boolean useUnifiedAttributionSetting = true; // Boolean | Use the ad sets' own attribution settings for action counting.
        String filtering = "filtering_example"; // String | JSON array of Meta filter objects: [{\"field\", \"operator\", \"value\"}]. Applied server-side by Meta.
        String datePreset = "datePreset_example"; // String | Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD); requires toDate.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD); requires fromDate.
        String timeIncrement = "timeIncrement_example"; // String | Days per row (1-90), monthly, or all_days.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<QueryAdInsights200Response> response = apiInstance.queryAdInsightsWithHttpInfo(accountId, objectId, query, customerId, pageToken, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdInsightsApi#queryAdInsights");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant); its platform selects the Meta or Google contract. | |
| **objectId** | **String**| Meta only (required there): insights node — act_&lt;n&gt;, campaign id, ad set id or ad id. | [optional] |
| **query** | **String**| Google only (required there): the GAQL SELECT statement to run. | [optional] |
| **customerId** | **String**| Google only: numeric customer id (no dashes) when the connection has several Google Ads accounts. | [optional] |
| **pageToken** | **String**| Google only: cursor from paging.nextPageToken of the previous page. | [optional] |
| **level** | **String**| Row granularity | [optional] [enum: ad, adset, campaign, account] |
| **fields** | **String**| Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted &#x3D; Meta&#39;s default set. | [optional] |
| **breakdowns** | **String**| Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform). | [optional] |
| **actionBreakdowns** | **String**| Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row. | [optional] |
| **actionAttributionWindows** | **String**| Comma-separated Meta attribution windows. Action values are returned keyed per window. | [optional] |
| **actionReportTime** | **String**| When actions are counted: impression, conversion or mixed. | [optional] |
| **useUnifiedAttributionSetting** | **Boolean**| Use the ad sets&#39; own attribution settings for action counting. | [optional] |
| **filtering** | **String**| JSON array of Meta filter objects: [{\&quot;field\&quot;, \&quot;operator\&quot;, \&quot;value\&quot;}]. Applied server-side by Meta. | [optional] |
| **datePreset** | **String**| Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate. | [optional] |
| **fromDate** | **LocalDate**| Start of range (YYYY-MM-DD); requires toDate. | [optional] |
| **toDate** | **LocalDate**| End of range (YYYY-MM-DD); requires fromDate. | [optional] |
| **timeIncrement** | **String**| Days per row (1-90), monthly, or all_days. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**QueryAdInsights200Response**](QueryAdInsights200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Insight rows (raw platform shape) |  -  |
| **400** | Invalid input, or the platform rejected the query (unknown field, invalid breakdown combo, malformed GAQL) — message carries the platform&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Platform rate limit reached. For Google this is the per-user operations budget or the shared quota; the message says which and when it resets. |  -  |
| **501** | Only supported on Meta (facebook/instagram) and Google Ads |  -  |

