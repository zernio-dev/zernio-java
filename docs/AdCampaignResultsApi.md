# AdCampaignResultsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCampaignResultsTotals**](AdCampaignResultsApi.md#getCampaignResultsTotals) | **GET** /v1/ads/campaign-results/totals | Get your results totals |
| [**getCampaignResultsTotalsWithHttpInfo**](AdCampaignResultsApi.md#getCampaignResultsTotalsWithHttpInfo) | **GET** /v1/ads/campaign-results/totals | Get your results totals |
| [**getCampaignResultsUpload**](AdCampaignResultsApi.md#getCampaignResultsUpload) | **GET** /v1/ads/campaign-results/uploads/{uploadId} | Check a results upload |
| [**getCampaignResultsUploadWithHttpInfo**](AdCampaignResultsApi.md#getCampaignResultsUploadWithHttpInfo) | **GET** /v1/ads/campaign-results/uploads/{uploadId} | Check a results upload |
| [**listCampaignResultMetrics**](AdCampaignResultsApi.md#listCampaignResultMetrics) | **GET** /v1/ads/campaign-results/metrics | List your result metrics |
| [**listCampaignResultMetricsWithHttpInfo**](AdCampaignResultsApi.md#listCampaignResultMetricsWithHttpInfo) | **GET** /v1/ads/campaign-results/metrics | List your result metrics |
| [**listCampaignResults**](AdCampaignResultsApi.md#listCampaignResults) | **GET** /v1/ads/campaign-results | List your results per campaign |
| [**listCampaignResultsWithHttpInfo**](AdCampaignResultsApi.md#listCampaignResultsWithHttpInfo) | **GET** /v1/ads/campaign-results | List your results per campaign |
| [**setCampaignResultMetric**](AdCampaignResultsApi.md#setCampaignResultMetric) | **PUT** /v1/ads/campaign-results/metrics/{key} | Name a result metric or define a formula |
| [**setCampaignResultMetricWithHttpInfo**](AdCampaignResultsApi.md#setCampaignResultMetricWithHttpInfo) | **PUT** /v1/ads/campaign-results/metrics/{key} | Name a result metric or define a formula |
| [**uploadCampaignResults**](AdCampaignResultsApi.md#uploadCampaignResults) | **POST** /v1/ads/campaign-results | Upload your results per campaign |
| [**uploadCampaignResultsWithHttpInfo**](AdCampaignResultsApi.md#uploadCampaignResultsWithHttpInfo) | **POST** /v1/ads/campaign-results | Upload your results per campaign |



## getCampaignResultsTotals

> GetCampaignResultsTotals200Response getCampaignResultsTotals(fromDate, toDate, adAccountIds)

Get your results totals

Each metric you send summed over a date range across every campaign of the ad accounts your key can see, or of the ones you name. Each day counts its newest value only.  Formulas are not computed here, since they also read the platform&#39;s numbers: apply one to these totals and the account&#39;s spend for the same range, or read it per campaign from &#x60;GET /v1/ads/tree?results&#x3D;true&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive. At most 400 days after `fromDate`.
        String adAccountIds = "adAccountIds_example"; // String | Comma-separated platform ad account ids, at most 100. Omit for every ad account your key can see.
        try {
            GetCampaignResultsTotals200Response result = apiInstance.getCampaignResultsTotals(fromDate, toDate, adAccountIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#getCampaignResultsTotals");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**| Inclusive. At most 400 days after &#x60;fromDate&#x60;. | |
| **adAccountIds** | **String**| Comma-separated platform ad account ids, at most 100. Omit for every ad account your key can see. | [optional] |

### Return type

[**GetCampaignResultsTotals200Response**](GetCampaignResultsTotals200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The totals by metric key. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## getCampaignResultsTotalsWithHttpInfo

> ApiResponse<GetCampaignResultsTotals200Response> getCampaignResultsTotals getCampaignResultsTotalsWithHttpInfo(fromDate, toDate, adAccountIds)

Get your results totals

Each metric you send summed over a date range across every campaign of the ad accounts your key can see, or of the ones you name. Each day counts its newest value only.  Formulas are not computed here, since they also read the platform&#39;s numbers: apply one to these totals and the account&#39;s spend for the same range, or read it per campaign from &#x60;GET /v1/ads/tree?results&#x3D;true&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive. At most 400 days after `fromDate`.
        String adAccountIds = "adAccountIds_example"; // String | Comma-separated platform ad account ids, at most 100. Omit for every ad account your key can see.
        try {
            ApiResponse<GetCampaignResultsTotals200Response> response = apiInstance.getCampaignResultsTotalsWithHttpInfo(fromDate, toDate, adAccountIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#getCampaignResultsTotals");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**| Inclusive. At most 400 days after &#x60;fromDate&#x60;. | |
| **adAccountIds** | **String**| Comma-separated platform ad account ids, at most 100. Omit for every ad account your key can see. | [optional] |

### Return type

ApiResponse<[**GetCampaignResultsTotals200Response**](GetCampaignResultsTotals200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The totals by metric key. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## getCampaignResultsUpload

> GetCampaignResultsUpload200Response getCampaignResultsUpload(uploadId)

Check a results upload

How an upload was matched: rows matched and unmatched, and up to 100 unmatched rows with why (&#x60;no_campaign&#x60; or &#x60;ambiguous&#x60;).  &#x60;status&#x60; turns &#x60;done&#x60; once every row is processed, usually within seconds. Uploads are kept for 30 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        String uploadId = "uploadId_example"; // String | 
        try {
            GetCampaignResultsUpload200Response result = apiInstance.getCampaignResultsUpload(uploadId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#getCampaignResultsUpload");
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
| **uploadId** | **String**|  | |

### Return type

[**GetCampaignResultsUpload200Response**](GetCampaignResultsUpload200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The upload&#39;s outcome. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getCampaignResultsUploadWithHttpInfo

> ApiResponse<GetCampaignResultsUpload200Response> getCampaignResultsUpload getCampaignResultsUploadWithHttpInfo(uploadId)

Check a results upload

How an upload was matched: rows matched and unmatched, and up to 100 unmatched rows with why (&#x60;no_campaign&#x60; or &#x60;ambiguous&#x60;).  &#x60;status&#x60; turns &#x60;done&#x60; once every row is processed, usually within seconds. Uploads are kept for 30 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        String uploadId = "uploadId_example"; // String | 
        try {
            ApiResponse<GetCampaignResultsUpload200Response> response = apiInstance.getCampaignResultsUploadWithHttpInfo(uploadId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#getCampaignResultsUpload");
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
| **uploadId** | **String**|  | |

### Return type

ApiResponse<[**GetCampaignResultsUpload200Response**](GetCampaignResultsUpload200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The upload&#39;s outcome. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## listCampaignResultMetrics

> ListCampaignResultMetrics200Response listCampaignResultMetrics()

List your result metrics

The metric keys your team has sent, with their label and kind, then the formulas: your own and the built-in ones (&#x60;cac_percent&#x60;, &#x60;cost_per_sale&#x60;, &#x60;cost_per_qualified_lead&#x60;, &#x60;lead_to_sale&#x60;). A new key appears as a &#x60;count&#x60; labelled from the key; name it, or define a formula, with &#x60;PUT /v1/ads/campaign-results/metrics/{key}&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        try {
            ListCampaignResultMetrics200Response result = apiInstance.listCampaignResultMetrics();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#listCampaignResultMetrics");
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

[**ListCampaignResultMetrics200Response**](ListCampaignResultMetrics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metrics. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listCampaignResultMetricsWithHttpInfo

> ApiResponse<ListCampaignResultMetrics200Response> listCampaignResultMetrics listCampaignResultMetricsWithHttpInfo()

List your result metrics

The metric keys your team has sent, with their label and kind, then the formulas: your own and the built-in ones (&#x60;cac_percent&#x60;, &#x60;cost_per_sale&#x60;, &#x60;cost_per_qualified_lead&#x60;, &#x60;lead_to_sale&#x60;). A new key appears as a &#x60;count&#x60; labelled from the key; name it, or define a formula, with &#x60;PUT /v1/ads/campaign-results/metrics/{key}&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        try {
            ApiResponse<ListCampaignResultMetrics200Response> response = apiInstance.listCampaignResultMetricsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#listCampaignResultMetrics");
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

ApiResponse<[**ListCampaignResultMetrics200Response**](ListCampaignResultMetrics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metrics. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## listCampaignResults

> ListCampaignResults200Response listCampaignResults(fromDate, toDate, campaignIds, limit, cursor)

List your results per campaign

Your results summed per campaign over a date range, one entry per campaign with every metric it has, for the ad accounts your key can see. Each day counts its newest value only.  Paginated by campaign: pass &#x60;nextCursor&#x60; back as &#x60;cursor&#x60; until it is null. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive. At most 400 days after `fromDate`.
        String campaignIds = "campaignIds_example"; // String | Comma-separated platform campaign ids, at most 500. Omit for all campaigns.
        Integer limit = 100; // Integer | Campaigns per page.
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ListCampaignResults200Response result = apiInstance.listCampaignResults(fromDate, toDate, campaignIds, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#listCampaignResults");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**| Inclusive. At most 400 days after &#x60;fromDate&#x60;. | |
| **campaignIds** | **String**| Comma-separated platform campaign ids, at most 500. Omit for all campaigns. | [optional] |
| **limit** | **Integer**| Campaigns per page. | [optional] [default to 100] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

[**ListCampaignResults200Response**](ListCampaignResults200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of campaigns. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listCampaignResultsWithHttpInfo

> ApiResponse<ListCampaignResults200Response> listCampaignResults listCampaignResultsWithHttpInfo(fromDate, toDate, campaignIds, limit, cursor)

List your results per campaign

Your results summed per campaign over a date range, one entry per campaign with every metric it has, for the ad accounts your key can see. Each day counts its newest value only.  Paginated by campaign: pass &#x60;nextCursor&#x60; back as &#x60;cursor&#x60; until it is null. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | 
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive. At most 400 days after `fromDate`.
        String campaignIds = "campaignIds_example"; // String | Comma-separated platform campaign ids, at most 500. Omit for all campaigns.
        Integer limit = 100; // Integer | Campaigns per page.
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ApiResponse<ListCampaignResults200Response> response = apiInstance.listCampaignResultsWithHttpInfo(fromDate, toDate, campaignIds, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#listCampaignResults");
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
| **fromDate** | **LocalDate**|  | |
| **toDate** | **LocalDate**| Inclusive. At most 400 days after &#x60;fromDate&#x60;. | |
| **campaignIds** | **String**| Comma-separated platform campaign ids, at most 500. Omit for all campaigns. | [optional] |
| **limit** | **Integer**| Campaigns per page. | [optional] [default to 100] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

ApiResponse<[**ListCampaignResults200Response**](ListCampaignResults200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of campaigns. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## setCampaignResultMetric

> SetCampaignResultMetric200Response setCampaignResultMetric(key, setCampaignResultMetricRequest)

Name a result metric or define a formula

Sets a metric key&#39;s label and kind: &#x60;count&#x60; for things you count (leads, sales), &#x60;money&#x60; with its currency (revenue), &#x60;percent&#x60; or &#x60;ratio&#x60;.  Send &#x60;formula&#x60; to make it a computed metric: &#x60;+ - * /&#x60; and parentheses over &#x60;spend&#x60;, &#x60;impressions&#x60;, &#x60;clicks&#x60;, &#x60;conversions&#x60;, &#x60;purchase_value&#x60; and the metrics you send, at most 200 characters. A formula cannot read another formula.  It is computed per campaign over the summed values of the range, and has no value when an input is missing or a division is by zero. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        String key = "key_example"; // String | 
        SetCampaignResultMetricRequest setCampaignResultMetricRequest = new SetCampaignResultMetricRequest(); // SetCampaignResultMetricRequest | 
        try {
            SetCampaignResultMetric200Response result = apiInstance.setCampaignResultMetric(key, setCampaignResultMetricRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#setCampaignResultMetric");
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
| **key** | **String**|  | |
| **setCampaignResultMetricRequest** | [**SetCampaignResultMetricRequest**](SetCampaignResultMetricRequest.md)|  | |

### Return type

[**SetCampaignResultMetric200Response**](SetCampaignResultMetric200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## setCampaignResultMetricWithHttpInfo

> ApiResponse<SetCampaignResultMetric200Response> setCampaignResultMetric setCampaignResultMetricWithHttpInfo(key, setCampaignResultMetricRequest)

Name a result metric or define a formula

Sets a metric key&#39;s label and kind: &#x60;count&#x60; for things you count (leads, sales), &#x60;money&#x60; with its currency (revenue), &#x60;percent&#x60; or &#x60;ratio&#x60;.  Send &#x60;formula&#x60; to make it a computed metric: &#x60;+ - * /&#x60; and parentheses over &#x60;spend&#x60;, &#x60;impressions&#x60;, &#x60;clicks&#x60;, &#x60;conversions&#x60;, &#x60;purchase_value&#x60; and the metrics you send, at most 200 characters. A formula cannot read another formula.  It is computed per campaign over the summed values of the range, and has no value when an input is missing or a division is by zero. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        String key = "key_example"; // String | 
        SetCampaignResultMetricRequest setCampaignResultMetricRequest = new SetCampaignResultMetricRequest(); // SetCampaignResultMetricRequest | 
        try {
            ApiResponse<SetCampaignResultMetric200Response> response = apiInstance.setCampaignResultMetricWithHttpInfo(key, setCampaignResultMetricRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#setCampaignResultMetric");
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
| **key** | **String**|  | |
| **setCampaignResultMetricRequest** | [**SetCampaignResultMetricRequest**](SetCampaignResultMetricRequest.md)|  | |

### Return type

ApiResponse<[**SetCampaignResultMetric200Response**](SetCampaignResultMetric200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## uploadCampaignResults

> UploadCampaignResults202Response uploadCampaignResults(uploadCampaignResultsRequest, idempotencyKey)

Upload your results per campaign

Sends your own daily numbers per campaign (qualified leads, sales, revenue...) so rules and reports can use them next to spend.  Name each row&#39;s campaign by &#x60;campaignId&#x60;, &#x60;utmCampaign&#x60; or &#x60;campaignName&#x60;. Rows are matched in the background: the &#x60;202&#x60; returns an &#x60;uploadId&#x60;, and &#x60;Location&#x60; points to &#x60;GET /v1/ads/campaign-results/uploads/{uploadId}&#x60;.  Re-sending a day replaces it. Send an &#x60;Idempotency-Key&#x60; to retry safely. Limits per team: 60 requests and 20,000 rows per hour, 512 KB per request. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        UploadCampaignResultsRequest uploadCampaignResultsRequest = new UploadCampaignResultsRequest(); // UploadCampaignResultsRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | A retry with the same key and body replays the first response instead of uploading twice.
        try {
            UploadCampaignResults202Response result = apiInstance.uploadCampaignResults(uploadCampaignResultsRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#uploadCampaignResults");
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
| **uploadCampaignResultsRequest** | [**UploadCampaignResultsRequest**](UploadCampaignResultsRequest.md)|  | |
| **idempotencyKey** | **String**| A retry with the same key and body replays the first response instead of uploading twice. | [optional] |

### Return type

[**UploadCampaignResults202Response**](UploadCampaignResults202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Queued for matching. |  * Location - The upload, to check how its rows were matched. <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the team has no ads access. |  -  |
| **409** | The same &#x60;Idempotency-Key&#x60; is still being processed. Retry shortly. |  -  |
| **413** | Code &#x60;payload_too_large&#x60;: the body is over 512 KB. |  -  |
| **422** | The &#x60;Idempotency-Key&#x60; was used with a different body. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## uploadCampaignResultsWithHttpInfo

> ApiResponse<UploadCampaignResults202Response> uploadCampaignResults uploadCampaignResultsWithHttpInfo(uploadCampaignResultsRequest, idempotencyKey)

Upload your results per campaign

Sends your own daily numbers per campaign (qualified leads, sales, revenue...) so rules and reports can use them next to spend.  Name each row&#39;s campaign by &#x60;campaignId&#x60;, &#x60;utmCampaign&#x60; or &#x60;campaignName&#x60;. Rows are matched in the background: the &#x60;202&#x60; returns an &#x60;uploadId&#x60;, and &#x60;Location&#x60; points to &#x60;GET /v1/ads/campaign-results/uploads/{uploadId}&#x60;.  Re-sending a day replaces it. Send an &#x60;Idempotency-Key&#x60; to retry safely. Limits per team: 60 requests and 20,000 rows per hour, 512 KB per request. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignResultsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignResultsApi apiInstance = new AdCampaignResultsApi(defaultClient);
        UploadCampaignResultsRequest uploadCampaignResultsRequest = new UploadCampaignResultsRequest(); // UploadCampaignResultsRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | A retry with the same key and body replays the first response instead of uploading twice.
        try {
            ApiResponse<UploadCampaignResults202Response> response = apiInstance.uploadCampaignResultsWithHttpInfo(uploadCampaignResultsRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignResultsApi#uploadCampaignResults");
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
| **uploadCampaignResultsRequest** | [**UploadCampaignResultsRequest**](UploadCampaignResultsRequest.md)|  | |
| **idempotencyKey** | **String**| A retry with the same key and body replays the first response instead of uploading twice. | [optional] |

### Return type

ApiResponse<[**UploadCampaignResults202Response**](UploadCampaignResults202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Queued for matching. |  * Location - The upload, to check how its rows were matched. <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the team has no ads access. |  -  |
| **409** | The same &#x60;Idempotency-Key&#x60; is still being processed. Retry shortly. |  -  |
| **413** | Code &#x60;payload_too_large&#x60;: the body is over 512 KB. |  -  |
| **422** | The &#x60;Idempotency-Key&#x60; was used with a different body. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

