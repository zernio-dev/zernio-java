# UsageApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBilling**](UsageApi.md#getBilling) | **GET** /v1/billing | Account billing snapshot (plan, cycle, balance, caps, status) |
| [**getBillingWithHttpInfo**](UsageApi.md#getBillingWithHttpInfo) | **GET** /v1/billing | Account billing snapshot (plan, cycle, balance, caps, status) |
| [**getCallsUsage**](UsageApi.md#getCallsUsage) | **GET** /v1/usage/calls | Calling usage and cost |
| [**getCallsUsageWithHttpInfo**](UsageApi.md#getCallsUsageWithHttpInfo) | **GET** /v1/usage/calls | Calling usage and cost |
| [**getSmsUsage**](UsageApi.md#getSmsUsage) | **GET** /v1/usage/sms | SMS usage (volumes) |
| [**getSmsUsageWithHttpInfo**](UsageApi.md#getSmsUsageWithHttpInfo) | **GET** /v1/usage/sms | SMS usage (volumes) |
| [**getUsage**](UsageApi.md#getUsage) | **GET** /v1/usage | Usage snapshot (default) or billed-spend metering (with params) |
| [**getUsageWithHttpInfo**](UsageApi.md#getUsageWithHttpInfo) | **GET** /v1/usage | Usage snapshot (default) or billed-spend metering (with params) |
| [**getUsageStats**](UsageApi.md#getUsageStats) | **GET** /v1/usage-stats | Get plan and usage snapshot (plan, limits, payment status) |
| [**getUsageStatsWithHttpInfo**](UsageApi.md#getUsageStatsWithHttpInfo) | **GET** /v1/usage-stats | Get plan and usage snapshot (plan, limits, payment status) |
| [**getXApiPricing**](UsageApi.md#getXApiPricing) | **GET** /v1/billing/x-pricing | Get X/Twitter API pricing table |
| [**getXApiPricingWithHttpInfo**](UsageApi.md#getXApiPricingWithHttpInfo) | **GET** /v1/billing/x-pricing | Get X/Twitter API pricing table |



## getBilling

> BillingSnapshot getBilling()

Account billing snapshot (plan, cycle, balance, caps, status)

The billing \&quot;wallet/statement\&quot; view: current plan, billing cycle, accrued balance + remaining credits this period, spend caps, and payment / access status. This is the billing half of the legacy &#x60;/v1/usage-stats&#x60; snapshot — the per-product consumption half is metering and lives on &#x60;GET /v1/usage&#x60;.  Usage-based (Metronome) accounts get a populated &#x60;balance&#x60;; legacy Stripe accounts get &#x60;balance: null&#x60; plus a deprecated &#x60;legacy.limits&#x60; block and, when payment-blocked, &#x60;status.openInvoiceUrl&#x60; / &#x60;status.declineReason&#x60;. 

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
            BillingSnapshot result = apiInstance.getBilling();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getBilling");
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

[**BillingSnapshot**](BillingSnapshot.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Billing snapshot |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getBillingWithHttpInfo

> ApiResponse<BillingSnapshot> getBilling getBillingWithHttpInfo()

Account billing snapshot (plan, cycle, balance, caps, status)

The billing \&quot;wallet/statement\&quot; view: current plan, billing cycle, accrued balance + remaining credits this period, spend caps, and payment / access status. This is the billing half of the legacy &#x60;/v1/usage-stats&#x60; snapshot — the per-product consumption half is metering and lives on &#x60;GET /v1/usage&#x60;.  Usage-based (Metronome) accounts get a populated &#x60;balance&#x60;; legacy Stripe accounts get &#x60;balance: null&#x60; plus a deprecated &#x60;legacy.limits&#x60; block and, when payment-blocked, &#x60;status.openInvoiceUrl&#x60; / &#x60;status.declineReason&#x60;. 

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
            ApiResponse<BillingSnapshot> response = apiInstance.getBillingWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getBilling");
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

ApiResponse<[**BillingSnapshot**](BillingSnapshot.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Billing snapshot |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getCallsUsage

> GetCallsUsage200Response getCallsUsage(since, until, channel, number, groupBy)

Calling usage and cost

Aggregated calling usage across your numbers, both channels (WhatsApp Business Calling + regular phone/PSTN): call counts, answered counts, minutes, and cost. Use it for cost visibility or to rebill your own customers per number.  Costs come from each call&#39;s billing snapshot, so this endpoint always agrees with the invoice: &#x60;billableUSD&#x60; is what Zernio bills; &#x60;metaUSD&#x60; is the WhatsApp per-minute charge Meta bills directly to your WABA (display only, never billed by Zernio).  Optional &#x60;groupBy&#x60; returns a breakdown by UTC day, by your number, or by channel. Defaults to the last 30 days. 

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
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Start of the window (inclusive). Default 30 days before `until`.
        OffsetDateTime until = OffsetDateTime.now(); // OffsetDateTime | End of the window (exclusive). Default now.
        String channel = "whatsapp"; // String | 
        String number = "number_example"; // String | Scope to calls involving this number (typically one of YOUR numbers). E.164, leading + optional.
        String groupBy = "day"; // String | 
        try {
            GetCallsUsage200Response result = apiInstance.getCallsUsage(since, until, channel, number, groupBy);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getCallsUsage");
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
| **since** | **OffsetDateTime**| Start of the window (inclusive). Default 30 days before &#x60;until&#x60;. | [optional] |
| **until** | **OffsetDateTime**| End of the window (exclusive). Default now. | [optional] |
| **channel** | **String**|  | [optional] [enum: whatsapp, pstn] |
| **number** | **String**| Scope to calls involving this number (typically one of YOUR numbers). E.164, leading + optional. | [optional] |
| **groupBy** | **String**|  | [optional] [enum: day, number, channel] |

### Return type

[**GetCallsUsage200Response**](GetCallsUsage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Usage totals (+ breakdown when groupBy is set). |  -  |
| **400** | since must be before until |  -  |
| **401** | Unauthorized |  -  |

## getCallsUsageWithHttpInfo

> ApiResponse<GetCallsUsage200Response> getCallsUsage getCallsUsageWithHttpInfo(since, until, channel, number, groupBy)

Calling usage and cost

Aggregated calling usage across your numbers, both channels (WhatsApp Business Calling + regular phone/PSTN): call counts, answered counts, minutes, and cost. Use it for cost visibility or to rebill your own customers per number.  Costs come from each call&#39;s billing snapshot, so this endpoint always agrees with the invoice: &#x60;billableUSD&#x60; is what Zernio bills; &#x60;metaUSD&#x60; is the WhatsApp per-minute charge Meta bills directly to your WABA (display only, never billed by Zernio).  Optional &#x60;groupBy&#x60; returns a breakdown by UTC day, by your number, or by channel. Defaults to the last 30 days. 

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
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Start of the window (inclusive). Default 30 days before `until`.
        OffsetDateTime until = OffsetDateTime.now(); // OffsetDateTime | End of the window (exclusive). Default now.
        String channel = "whatsapp"; // String | 
        String number = "number_example"; // String | Scope to calls involving this number (typically one of YOUR numbers). E.164, leading + optional.
        String groupBy = "day"; // String | 
        try {
            ApiResponse<GetCallsUsage200Response> response = apiInstance.getCallsUsageWithHttpInfo(since, until, channel, number, groupBy);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getCallsUsage");
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
| **since** | **OffsetDateTime**| Start of the window (inclusive). Default 30 days before &#x60;until&#x60;. | [optional] |
| **until** | **OffsetDateTime**| End of the window (exclusive). Default now. | [optional] |
| **channel** | **String**|  | [optional] [enum: whatsapp, pstn] |
| **number** | **String**| Scope to calls involving this number (typically one of YOUR numbers). E.164, leading + optional. | [optional] |
| **groupBy** | **String**|  | [optional] [enum: day, number, channel] |

### Return type

ApiResponse<[**GetCallsUsage200Response**](GetCallsUsage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Usage totals (+ breakdown when groupBy is set). |  -  |
| **400** | since must be before until |  -  |
| **401** | Unauthorized |  -  |


## getSmsUsage

> GetSmsUsage200Response getSmsUsage(since, until, number, groupBy)

SMS usage (volumes)

Aggregated SMS/MMS volumes across your numbers: sent, received, and total message counts, with an optional breakdown by UTC day or by number. Defaults to the last 30 days.  Volumes only, deliberately: SMS cost is carrier-rated asynchronously and billed to your invoice, so per-message cost is not available here. Calling usage (GET /v1/usage/calls) does include billable cost. 

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
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Start of the window (inclusive). Default 30 days before `until`.
        OffsetDateTime until = OffsetDateTime.now(); // OffsetDateTime | End of the window (exclusive). Default now.
        String number = "number_example"; // String | Scope to one of YOUR SMS-enabled numbers (E.164, leading + optional).
        String groupBy = "day"; // String | 
        try {
            GetSmsUsage200Response result = apiInstance.getSmsUsage(since, until, number, groupBy);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getSmsUsage");
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
| **since** | **OffsetDateTime**| Start of the window (inclusive). Default 30 days before &#x60;until&#x60;. | [optional] |
| **until** | **OffsetDateTime**| End of the window (exclusive). Default now. | [optional] |
| **number** | **String**| Scope to one of YOUR SMS-enabled numbers (E.164, leading + optional). | [optional] |
| **groupBy** | **String**|  | [optional] [enum: day, number] |

### Return type

[**GetSmsUsage200Response**](GetSmsUsage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume totals (+ breakdown when groupBy is set). |  -  |
| **400** | since must be before until |  -  |
| **401** | Unauthorized |  -  |
| **404** | &#x60;number&#x60; doesn&#39;t match any of your SMS-enabled numbers |  -  |

## getSmsUsageWithHttpInfo

> ApiResponse<GetSmsUsage200Response> getSmsUsage getSmsUsageWithHttpInfo(since, until, number, groupBy)

SMS usage (volumes)

Aggregated SMS/MMS volumes across your numbers: sent, received, and total message counts, with an optional breakdown by UTC day or by number. Defaults to the last 30 days.  Volumes only, deliberately: SMS cost is carrier-rated asynchronously and billed to your invoice, so per-message cost is not available here. Calling usage (GET /v1/usage/calls) does include billable cost. 

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
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Start of the window (inclusive). Default 30 days before `until`.
        OffsetDateTime until = OffsetDateTime.now(); // OffsetDateTime | End of the window (exclusive). Default now.
        String number = "number_example"; // String | Scope to one of YOUR SMS-enabled numbers (E.164, leading + optional).
        String groupBy = "day"; // String | 
        try {
            ApiResponse<GetSmsUsage200Response> response = apiInstance.getSmsUsageWithHttpInfo(since, until, number, groupBy);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getSmsUsage");
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
| **since** | **OffsetDateTime**| Start of the window (inclusive). Default 30 days before &#x60;until&#x60;. | [optional] |
| **until** | **OffsetDateTime**| End of the window (exclusive). Default now. | [optional] |
| **number** | **String**| Scope to one of YOUR SMS-enabled numbers (E.164, leading + optional). | [optional] |
| **groupBy** | **String**|  | [optional] [enum: day, number] |

### Return type

ApiResponse<[**GetSmsUsage200Response**](GetSmsUsage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume totals (+ breakdown when groupBy is set). |  -  |
| **400** | since must be before until |  -  |
| **401** | Unauthorized |  -  |
| **404** | &#x60;number&#x60; doesn&#39;t match any of your SMS-enabled numbers |  -  |


## getUsage

> GetUsage200Response getUsage(reconcile, range, from, to, granularity)

Usage snapshot (default) or billed-spend metering (with params)

Dual-mode endpoint, selected by query params — fully backward compatible:  **Without metering params (the default):** the plan / quota / usage snapshot — plan name, billing period, limits, usage counts, access state. Identical to &#x60;GET /v1/usage-stats&#x60;. Existing integrations keep working unchanged.  **With &#x60;range&#x60;, &#x60;granularity&#x60;, &#x60;from&#x60;, or &#x60;to&#x60;:** usage METERING — billed spend (USD) by product family (&#x60;accounts&#x60;, &#x60;numbers&#x60;, &#x60;calls&#x60;, &#x60;sms&#x60;, &#x60;dlc&#x60;, &#x60;xApi&#x60;, &#x60;credits&#x60;, &#x60;other&#x60;) over the window, at &#x60;day&#x60; / &#x60;month&#x60; / &#x60;total&#x60; granularity, from Metronome&#39;s invoice breakdown (the CHARGE view — always reconciles with what gets billed). Also served at &#x60;GET /v1/usage/daily&#x60;. Usage-based accounts only — legacy Stripe accounts get &#x60;{ \&quot;supported\&quot;: false, \&quot;days\&quot;: [] }&#x60;.  For per-domain consumption *volumes* use &#x60;GET /v1/usage/calls&#x60; and &#x60;GET /v1/usage/sms&#x60;. For the billing statement (balance, credits, caps, payment status) use &#x60;GET /v1/billing&#x60;. 

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
        Boolean reconcile = true; // Boolean | Snapshot mode only. For Stripe subscription users, `true` forces a subscription reconciliation pass even when cached plan data looks complete. 
        String range = "cycle"; // String | Window to report. `cycle` / `prev-cycle` resolve to the customer's real billing-period bounds (falling back to a trailing 30 days when no invoice exists yet); `7d`…`12mo` are trailing windows; `custom` uses `from` / `to`. 
        LocalDate from = LocalDate.now(); // LocalDate | Inclusive start (UTC date). Required when `range=custom`.
        LocalDate to = LocalDate.now(); // LocalDate | Inclusive end (UTC date). Required when `range=custom`. Max span 366 days.
        String granularity = "day"; // String | Bucketing of the `days` series: `day` (one row per UTC day), `month` (one row per calendar month, dated to the 1st), or `total` (no series — read `totals`). Does not affect `totals`. 
        try {
            GetUsage200Response result = apiInstance.getUsage(reconcile, range, from, to, granularity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getUsage");
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
| **reconcile** | **Boolean**| Snapshot mode only. For Stripe subscription users, &#x60;true&#x60; forces a subscription reconciliation pass even when cached plan data looks complete.  | [optional] |
| **range** | **String**| Window to report. &#x60;cycle&#x60; / &#x60;prev-cycle&#x60; resolve to the customer&#39;s real billing-period bounds (falling back to a trailing 30 days when no invoice exists yet); &#x60;7d&#x60;…&#x60;12mo&#x60; are trailing windows; &#x60;custom&#x60; uses &#x60;from&#x60; / &#x60;to&#x60;.  | [optional] [default to cycle] [enum: cycle, prev-cycle, 7d, 14d, 30d, 3mo, 12mo, custom] |
| **from** | **LocalDate**| Inclusive start (UTC date). Required when &#x60;range&#x3D;custom&#x60;. | [optional] |
| **to** | **LocalDate**| Inclusive end (UTC date). Required when &#x60;range&#x3D;custom&#x60;. Max span 366 days. | [optional] |
| **granularity** | **String**| Bucketing of the &#x60;days&#x60; series: &#x60;day&#x60; (one row per UTC day), &#x60;month&#x60; (one row per calendar month, dated to the 1st), or &#x60;total&#x60; (no series — read &#x60;totals&#x60;). Does not affect &#x60;totals&#x60;.  | [optional] [default to day] [enum: day, month, total] |

### Return type

[**GetUsage200Response**](GetUsage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapshot (no metering params) or billed spend by product over the window (with metering params).  |  -  |
| **400** | Invalid query parameter |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getUsageWithHttpInfo

> ApiResponse<GetUsage200Response> getUsage getUsageWithHttpInfo(reconcile, range, from, to, granularity)

Usage snapshot (default) or billed-spend metering (with params)

Dual-mode endpoint, selected by query params — fully backward compatible:  **Without metering params (the default):** the plan / quota / usage snapshot — plan name, billing period, limits, usage counts, access state. Identical to &#x60;GET /v1/usage-stats&#x60;. Existing integrations keep working unchanged.  **With &#x60;range&#x60;, &#x60;granularity&#x60;, &#x60;from&#x60;, or &#x60;to&#x60;:** usage METERING — billed spend (USD) by product family (&#x60;accounts&#x60;, &#x60;numbers&#x60;, &#x60;calls&#x60;, &#x60;sms&#x60;, &#x60;dlc&#x60;, &#x60;xApi&#x60;, &#x60;credits&#x60;, &#x60;other&#x60;) over the window, at &#x60;day&#x60; / &#x60;month&#x60; / &#x60;total&#x60; granularity, from Metronome&#39;s invoice breakdown (the CHARGE view — always reconciles with what gets billed). Also served at &#x60;GET /v1/usage/daily&#x60;. Usage-based accounts only — legacy Stripe accounts get &#x60;{ \&quot;supported\&quot;: false, \&quot;days\&quot;: [] }&#x60;.  For per-domain consumption *volumes* use &#x60;GET /v1/usage/calls&#x60; and &#x60;GET /v1/usage/sms&#x60;. For the billing statement (balance, credits, caps, payment status) use &#x60;GET /v1/billing&#x60;. 

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
        Boolean reconcile = true; // Boolean | Snapshot mode only. For Stripe subscription users, `true` forces a subscription reconciliation pass even when cached plan data looks complete. 
        String range = "cycle"; // String | Window to report. `cycle` / `prev-cycle` resolve to the customer's real billing-period bounds (falling back to a trailing 30 days when no invoice exists yet); `7d`…`12mo` are trailing windows; `custom` uses `from` / `to`. 
        LocalDate from = LocalDate.now(); // LocalDate | Inclusive start (UTC date). Required when `range=custom`.
        LocalDate to = LocalDate.now(); // LocalDate | Inclusive end (UTC date). Required when `range=custom`. Max span 366 days.
        String granularity = "day"; // String | Bucketing of the `days` series: `day` (one row per UTC day), `month` (one row per calendar month, dated to the 1st), or `total` (no series — read `totals`). Does not affect `totals`. 
        try {
            ApiResponse<GetUsage200Response> response = apiInstance.getUsageWithHttpInfo(reconcile, range, from, to, granularity);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling UsageApi#getUsage");
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
| **reconcile** | **Boolean**| Snapshot mode only. For Stripe subscription users, &#x60;true&#x60; forces a subscription reconciliation pass even when cached plan data looks complete.  | [optional] |
| **range** | **String**| Window to report. &#x60;cycle&#x60; / &#x60;prev-cycle&#x60; resolve to the customer&#39;s real billing-period bounds (falling back to a trailing 30 days when no invoice exists yet); &#x60;7d&#x60;…&#x60;12mo&#x60; are trailing windows; &#x60;custom&#x60; uses &#x60;from&#x60; / &#x60;to&#x60;.  | [optional] [default to cycle] [enum: cycle, prev-cycle, 7d, 14d, 30d, 3mo, 12mo, custom] |
| **from** | **LocalDate**| Inclusive start (UTC date). Required when &#x60;range&#x3D;custom&#x60;. | [optional] |
| **to** | **LocalDate**| Inclusive end (UTC date). Required when &#x60;range&#x3D;custom&#x60;. Max span 366 days. | [optional] |
| **granularity** | **String**| Bucketing of the &#x60;days&#x60; series: &#x60;day&#x60; (one row per UTC day), &#x60;month&#x60; (one row per calendar month, dated to the 1st), or &#x60;total&#x60; (no series — read &#x60;totals&#x60;). Does not affect &#x60;totals&#x60;.  | [optional] [default to day] [enum: day, month, total] |

### Return type

ApiResponse<[**GetUsage200Response**](GetUsage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapshot (no metering params) or billed spend by product over the window (with metering params).  |  -  |
| **400** | Invalid query parameter |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getUsageStats

> UsageStats getUsageStats(reconcile)

Get plan and usage snapshot (plan, limits, payment status)

The plan / quota / payment-status snapshot: current plan name, billing period, plan limits, usage counts, and access state. Identical to a bare &#x60;GET /v1/usage&#x60; call (this path is its deprecated alias). For billed spend by product, call &#x60;GET /v1/usage&#x60; with &#x60;range&#x60; / &#x60;granularity&#x60; params. The statement view (balance, credits, caps, payment status) lives at &#x60;GET /v1/billing&#x60;.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCallsByOperation&#x60; (per-operation X API call counts —     resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;), plus a &#x60;spend&#x60;     block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. The legacy &#x60;usage.xApiCalls&#x60; 3-tier     aggregate is still emitted for back-compat but excludes the     $0.200 URL tier and any future tiers — new clients should     consume &#x60;xApiCallsByOperation&#x60; only. 

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
        Boolean reconcile = true; // Boolean | For Stripe subscription users, `true` forces a subscription reconciliation pass even when cached plan data looks complete. Omit the parameter, or pass `false`, to use the default first-time-only reconciliation behavior. Invalid boolean values are rejected. 
        try {
            UsageStats result = apiInstance.getUsageStats(reconcile);
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


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reconcile** | **Boolean**| For Stripe subscription users, &#x60;true&#x60; forces a subscription reconciliation pass even when cached plan data looks complete. Omit the parameter, or pass &#x60;false&#x60;, to use the default first-time-only reconciliation behavior. Invalid boolean values are rejected.  | [optional] |

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
| **400** | Invalid query parameter |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getUsageStatsWithHttpInfo

> ApiResponse<UsageStats> getUsageStats getUsageStatsWithHttpInfo(reconcile)

Get plan and usage snapshot (plan, limits, payment status)

The plan / quota / payment-status snapshot: current plan name, billing period, plan limits, usage counts, and access state. Identical to a bare &#x60;GET /v1/usage&#x60; call (this path is its deprecated alias). For billed spend by product, call &#x60;GET /v1/usage&#x60; with &#x60;range&#x60; / &#x60;granularity&#x60; params. The statement view (balance, credits, caps, payment status) lives at &#x60;GET /v1/billing&#x60;.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCallsByOperation&#x60; (per-operation X API call counts —     resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;), plus a &#x60;spend&#x60;     block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. The legacy &#x60;usage.xApiCalls&#x60; 3-tier     aggregate is still emitted for back-compat but excludes the     $0.200 URL tier and any future tiers — new clients should     consume &#x60;xApiCallsByOperation&#x60; only. 

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
        Boolean reconcile = true; // Boolean | For Stripe subscription users, `true` forces a subscription reconciliation pass even when cached plan data looks complete. Omit the parameter, or pass `false`, to use the default first-time-only reconciliation behavior. Invalid boolean values are rejected. 
        try {
            ApiResponse<UsageStats> response = apiInstance.getUsageStatsWithHttpInfo(reconcile);
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


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reconcile** | **Boolean**| For Stripe subscription users, &#x60;true&#x60; forces a subscription reconciliation pass even when cached plan data looks complete. Omit the parameter, or pass &#x60;false&#x60;, to use the default first-time-only reconciliation behavior. Invalid boolean values are rejected.  | [optional] |

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
| **400** | Invalid query parameter |  -  |
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

