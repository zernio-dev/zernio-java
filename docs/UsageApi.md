# UsageApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCallsUsage**](UsageApi.md#getCallsUsage) | **GET** /v1/usage/calls | Calling usage and cost |
| [**getCallsUsageWithHttpInfo**](UsageApi.md#getCallsUsageWithHttpInfo) | **GET** /v1/usage/calls | Calling usage and cost |
| [**getSmsUsage**](UsageApi.md#getSmsUsage) | **GET** /v1/usage/sms | SMS usage (volumes) |
| [**getSmsUsageWithHttpInfo**](UsageApi.md#getSmsUsageWithHttpInfo) | **GET** /v1/usage/sms | SMS usage (volumes) |
| [**getUsage**](UsageApi.md#getUsage) | **GET** /v1/usage | Get plan and usage snapshot |
| [**getUsageWithHttpInfo**](UsageApi.md#getUsageWithHttpInfo) | **GET** /v1/usage | Get plan and usage snapshot |
| [**getUsageStats**](UsageApi.md#getUsageStats) | **GET** /v1/usage-stats | Get plan and usage stats |
| [**getUsageStatsWithHttpInfo**](UsageApi.md#getUsageStatsWithHttpInfo) | **GET** /v1/usage-stats | Get plan and usage stats |
| [**getXApiPricing**](UsageApi.md#getXApiPricing) | **GET** /v1/billing/x-pricing | Get X/Twitter API pricing table |
| [**getXApiPricingWithHttpInfo**](UsageApi.md#getXApiPricingWithHttpInfo) | **GET** /v1/billing/x-pricing | Get X/Twitter API pricing table |



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

> UsageStats getUsage(reconcile)

Get plan and usage snapshot

The usage hub: current plan name, billing period, plan limits, and usage counts, in one snapshot. For metered consumption over an arbitrary window with breakdowns (by day, by number), use the domain spokes: &#x60;GET /v1/usage/calls&#x60; and &#x60;GET /v1/usage/sms&#x60;.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCallsByOperation&#x60; (per-operation X API call counts —     resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;), plus a &#x60;spend&#x60;     block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. The legacy &#x60;usage.xApiCalls&#x60; 3-tier     aggregate is still emitted for back-compat but excludes the     $0.200 URL tier and any future tiers — new clients should     consume &#x60;xApiCallsByOperation&#x60; only. 

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
            UsageStats result = apiInstance.getUsage(reconcile);
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
| **200** | Usage snapshot |  -  |
| **400** | Invalid query parameter |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getUsageWithHttpInfo

> ApiResponse<UsageStats> getUsage getUsageWithHttpInfo(reconcile)

Get plan and usage snapshot

The usage hub: current plan name, billing period, plan limits, and usage counts, in one snapshot. For metered consumption over an arbitrary window with breakdowns (by day, by number), use the domain spokes: &#x60;GET /v1/usage/calls&#x60; and &#x60;GET /v1/usage/sms&#x60;.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCallsByOperation&#x60; (per-operation X API call counts —     resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;), plus a &#x60;spend&#x60;     block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. The legacy &#x60;usage.xApiCalls&#x60; 3-tier     aggregate is still emitted for back-compat but excludes the     $0.200 URL tier and any future tiers — new clients should     consume &#x60;xApiCallsByOperation&#x60; only. 

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
            ApiResponse<UsageStats> response = apiInstance.getUsageWithHttpInfo(reconcile);
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
| **200** | Usage snapshot |  -  |
| **400** | Invalid query parameter |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getUsageStats

> UsageStats getUsageStats(reconcile)

Get plan and usage stats

Deprecated alias of &#x60;GET /v1/usage&#x60;; same contract. New integrations should use that path (the usage hub), with &#x60;GET /v1/usage/calls&#x60; and &#x60;GET /v1/usage/sms&#x60; for metered breakdowns.  Returns the current plan name, billing period, plan limits, and usage counts.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCallsByOperation&#x60; (per-operation X API call counts —     resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;), plus a &#x60;spend&#x60;     block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. The legacy &#x60;usage.xApiCalls&#x60; 3-tier     aggregate is still emitted for back-compat but excludes the     $0.200 URL tier and any future tiers — new clients should     consume &#x60;xApiCallsByOperation&#x60; only. 

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

Get plan and usage stats

Deprecated alias of &#x60;GET /v1/usage&#x60;; same contract. New integrations should use that path (the usage hub), with &#x60;GET /v1/usage/calls&#x60; and &#x60;GET /v1/usage/sms&#x60; for metered breakdowns.  Returns the current plan name, billing period, plan limits, and usage counts.  The response shape depends on the account&#39;s &#x60;billingSystem&#x60;:   * Stripe users: per-period &#x60;usage.uploads&#x60; / &#x60;usage.profiles&#x60; counters.   * Metronome (usage-based) users: &#x60;usage.connectedAccounts&#x60;,     &#x60;usage.xApiCallsByOperation&#x60; (per-operation X API call counts —     resolve keys via &#x60;GET /v1/billing/x-pricing&#x60;), plus a &#x60;spend&#x60;     block with &#x60;currentPeriodCents&#x60;, &#x60;xSpendCents&#x60;, and     &#x60;xSpendLimitCents&#x60;. The legacy &#x60;usage.xApiCalls&#x60; 3-tier     aggregate is still emitted for back-compat but excludes the     $0.200 URL tier and any future tiers — new clients should     consume &#x60;xApiCallsByOperation&#x60; only. 

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

