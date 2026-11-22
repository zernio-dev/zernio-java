# ConversionAuditApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**auditConversionTracking**](ConversionAuditApi.md#auditConversionTracking) | **GET** /v1/conversion-audit | Audit a site&#39;s ad conversion tracking |
| [**auditConversionTrackingWithHttpInfo**](ConversionAuditApi.md#auditConversionTrackingWithHttpInfo) | **GET** /v1/conversion-audit | Audit a site&#39;s ad conversion tracking |
| [**createConversionAuditMonitor**](ConversionAuditApi.md#createConversionAuditMonitor) | **POST** /v1/conversion-audit/monitors | Watch a domain |
| [**createConversionAuditMonitorWithHttpInfo**](ConversionAuditApi.md#createConversionAuditMonitorWithHttpInfo) | **POST** /v1/conversion-audit/monitors | Watch a domain |
| [**deleteConversionAuditMonitor**](ConversionAuditApi.md#deleteConversionAuditMonitor) | **DELETE** /v1/conversion-audit/monitors/{monitorId} | Stop watching a domain |
| [**deleteConversionAuditMonitorWithHttpInfo**](ConversionAuditApi.md#deleteConversionAuditMonitorWithHttpInfo) | **DELETE** /v1/conversion-audit/monitors/{monitorId} | Stop watching a domain |
| [**getLatestConversionAudit**](ConversionAuditApi.md#getLatestConversionAudit) | **GET** /v1/conversion-audit/latest | Get a host&#39;s latest stored conversion audit |
| [**getLatestConversionAuditWithHttpInfo**](ConversionAuditApi.md#getLatestConversionAuditWithHttpInfo) | **GET** /v1/conversion-audit/latest | Get a host&#39;s latest stored conversion audit |
| [**getMetaConversionAudit**](ConversionAuditApi.md#getMetaConversionAudit) | **GET** /v1/conversion-audit/meta-audit | Audit a connected Meta pixel from inside Events Manager |
| [**getMetaConversionAuditWithHttpInfo**](ConversionAuditApi.md#getMetaConversionAuditWithHttpInfo) | **GET** /v1/conversion-audit/meta-audit | Audit a connected Meta pixel from inside Events Manager |
| [**listConversionAuditMonitors**](ConversionAuditApi.md#listConversionAuditMonitors) | **GET** /v1/conversion-audit/monitors | List watched domains |
| [**listConversionAuditMonitorsWithHttpInfo**](ConversionAuditApi.md#listConversionAuditMonitorsWithHttpInfo) | **GET** /v1/conversion-audit/monitors | List watched domains |



## auditConversionTracking

> ConversionAuditAnswer auditConversionTracking(url)

Audit a site&#39;s ad conversion tracking

Scan any public URL for ad-platform conversion tracking, score how much conversion signal it leaks before the ad platforms see it, and get a fix prompt to hand to a coding agent.  The API key is optional. Without one, a caller&#39;s IP address gets 20 scans a minute. The Zernio MCP server always needs a key, because its sign-in covers the whole connection.  The scan fetches the page (SSRF-guarded) and its Google Tag Manager containers, and can render it in a headless browser. It finds every ad platform&#39;s browser pixel, checks for visible server-side (Conversions API) tracking, and estimates the signal lost to ad blockers, browser limits and short cookie windows.  Visitors who decline consent are never counted as lost.  The scan reads the page only and changes nothing on the site. Like the free page, it publishes the result as the host&#39;s public report.  Reading the result:  - &#x60;report.visibility: \&quot;limited\&quot;&#x60; means some pixels load through a tag manager or a store platform, so only part of the setup is visible from outside. It does not mean the tracking failed or is missing. - &#x60;status: \&quot;warn\&quot;&#x60; (browser-only) is the leak: the platform is tracked in the browser but not server-side. - &#x60;status: \&quot;good\&quot;&#x60; (server-side) means conversions reach the platform server-side, which recovers most of that signal. - &#x60;fixPrompt&#x60; is the same fix prompt the Conversion Leak Report page shows: this scan&#39;s findings, then the steps to send conversions server-side with &#x60;POST /v1/events&#x60; and to verify them. - To fix the leak with Zernio, follow https://docs.zernio.com/products/server-side-tracking/fix-with-agent: a tracking site, its tag, a forwarding rule per network to the pixel the page runs, then a rescan. A network turns &#x60;good&#x60; once the site&#39;s events reached that pixel in the last 7 days. - &#x60;publicReport&#x60; links the host&#39;s public page on is-bleeding.com. A homepage scan that could read the site&#39;s pixels becomes that page&#39;s snapshot, the same as a scan on is-bleeding.com. Any other scan links the stored snapshot, taken at &#x60;scannedAt&#x60;, or returns null when the host has none.  Without a key, each IP address also shares one hourly ceiling with every other keyless caller. With a key, a user gets 60 scans a minute. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String url = "example.com"; // String | The website address to audit. A bare domain is accepted and normalized to https.
        try {
            ConversionAuditAnswer result = apiInstance.auditConversionTracking(url);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#auditConversionTracking");
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
| **url** | **String**| The website address to audit. A bare domain is accepted and normalized to https. | |

### Return type

[**ConversionAuditAnswer**](ConversionAuditAnswer.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The scored audit and its fix prompt |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |

## auditConversionTrackingWithHttpInfo

> ApiResponse<ConversionAuditAnswer> auditConversionTracking auditConversionTrackingWithHttpInfo(url)

Audit a site&#39;s ad conversion tracking

Scan any public URL for ad-platform conversion tracking, score how much conversion signal it leaks before the ad platforms see it, and get a fix prompt to hand to a coding agent.  The API key is optional. Without one, a caller&#39;s IP address gets 20 scans a minute. The Zernio MCP server always needs a key, because its sign-in covers the whole connection.  The scan fetches the page (SSRF-guarded) and its Google Tag Manager containers, and can render it in a headless browser. It finds every ad platform&#39;s browser pixel, checks for visible server-side (Conversions API) tracking, and estimates the signal lost to ad blockers, browser limits and short cookie windows.  Visitors who decline consent are never counted as lost.  The scan reads the page only and changes nothing on the site. Like the free page, it publishes the result as the host&#39;s public report.  Reading the result:  - &#x60;report.visibility: \&quot;limited\&quot;&#x60; means some pixels load through a tag manager or a store platform, so only part of the setup is visible from outside. It does not mean the tracking failed or is missing. - &#x60;status: \&quot;warn\&quot;&#x60; (browser-only) is the leak: the platform is tracked in the browser but not server-side. - &#x60;status: \&quot;good\&quot;&#x60; (server-side) means conversions reach the platform server-side, which recovers most of that signal. - &#x60;fixPrompt&#x60; is the same fix prompt the Conversion Leak Report page shows: this scan&#39;s findings, then the steps to send conversions server-side with &#x60;POST /v1/events&#x60; and to verify them. - To fix the leak with Zernio, follow https://docs.zernio.com/products/server-side-tracking/fix-with-agent: a tracking site, its tag, a forwarding rule per network to the pixel the page runs, then a rescan. A network turns &#x60;good&#x60; once the site&#39;s events reached that pixel in the last 7 days. - &#x60;publicReport&#x60; links the host&#39;s public page on is-bleeding.com. A homepage scan that could read the site&#39;s pixels becomes that page&#39;s snapshot, the same as a scan on is-bleeding.com. Any other scan links the stored snapshot, taken at &#x60;scannedAt&#x60;, or returns null when the host has none.  Without a key, each IP address also shares one hourly ceiling with every other keyless caller. With a key, a user gets 60 scans a minute. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String url = "example.com"; // String | The website address to audit. A bare domain is accepted and normalized to https.
        try {
            ApiResponse<ConversionAuditAnswer> response = apiInstance.auditConversionTrackingWithHttpInfo(url);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#auditConversionTracking");
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
| **url** | **String**| The website address to audit. A bare domain is accepted and normalized to https. | |

### Return type

ApiResponse<[**ConversionAuditAnswer**](ConversionAuditAnswer.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The scored audit and its fix prompt |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |


## createConversionAuditMonitor

> ConversionAuditMonitorAnswer createConversionAuditMonitor(createConversionAuditMonitorRequest)

Watch a domain

Watch a domain&#39;s conversion tracking. Zernio rescans its homepage once a day and emails the account&#39;s address when tracking breaks, with what changed and the fix prompt for a coding agent. A break is:  - a score drop of 5 points or more - an ad network that stops tracking or stops firing - a pixel that starts firing before the cookie banner is answered - a server-side path that disappears  A break is confirmed by a second scan before any email goes out. The first check compares against the host&#39;s stored report when it has one, so run &#x60;auditConversionTracking&#x60; first to start from today&#39;s state.  Watching a domain you already watch returns it with &#x60;created: false&#x60; and status &#x60;200&#x60;. An account can watch up to 25 domains. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        CreateConversionAuditMonitorRequest createConversionAuditMonitorRequest = new CreateConversionAuditMonitorRequest(); // CreateConversionAuditMonitorRequest | 
        try {
            ConversionAuditMonitorAnswer result = apiInstance.createConversionAuditMonitor(createConversionAuditMonitorRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#createConversionAuditMonitor");
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
| **createConversionAuditMonitorRequest** | [**CreateConversionAuditMonitorRequest**](CreateConversionAuditMonitorRequest.md)|  | |

### Return type

[**ConversionAuditMonitorAnswer**](ConversionAuditMonitorAnswer.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You already watch this domain |  -  |
| **201** | The domain is now watched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The account already watches 25 domains, or the key&#39;s resource group is disabled |  -  |

## createConversionAuditMonitorWithHttpInfo

> ApiResponse<ConversionAuditMonitorAnswer> createConversionAuditMonitor createConversionAuditMonitorWithHttpInfo(createConversionAuditMonitorRequest)

Watch a domain

Watch a domain&#39;s conversion tracking. Zernio rescans its homepage once a day and emails the account&#39;s address when tracking breaks, with what changed and the fix prompt for a coding agent. A break is:  - a score drop of 5 points or more - an ad network that stops tracking or stops firing - a pixel that starts firing before the cookie banner is answered - a server-side path that disappears  A break is confirmed by a second scan before any email goes out. The first check compares against the host&#39;s stored report when it has one, so run &#x60;auditConversionTracking&#x60; first to start from today&#39;s state.  Watching a domain you already watch returns it with &#x60;created: false&#x60; and status &#x60;200&#x60;. An account can watch up to 25 domains. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        CreateConversionAuditMonitorRequest createConversionAuditMonitorRequest = new CreateConversionAuditMonitorRequest(); // CreateConversionAuditMonitorRequest | 
        try {
            ApiResponse<ConversionAuditMonitorAnswer> response = apiInstance.createConversionAuditMonitorWithHttpInfo(createConversionAuditMonitorRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#createConversionAuditMonitor");
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
| **createConversionAuditMonitorRequest** | [**CreateConversionAuditMonitorRequest**](CreateConversionAuditMonitorRequest.md)|  | |

### Return type

ApiResponse<[**ConversionAuditMonitorAnswer**](ConversionAuditMonitorAnswer.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You already watch this domain |  -  |
| **201** | The domain is now watched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The account already watches 25 domains, or the key&#39;s resource group is disabled |  -  |


## deleteConversionAuditMonitor

> DeleteAutomationTemplate200Response deleteConversionAuditMonitor(monitorId)

Stop watching a domain

Stops the daily checks and alert emails for this domain. The host&#39;s public report stays.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String monitorId = "monitorId_example"; // String | The monitor's `id`, from `listConversionAuditMonitors` or `createConversionAuditMonitor`.
        try {
            DeleteAutomationTemplate200Response result = apiInstance.deleteConversionAuditMonitor(monitorId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#deleteConversionAuditMonitor");
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
| **monitorId** | **String**| The monitor&#39;s &#x60;id&#x60;, from &#x60;listConversionAuditMonitors&#x60; or &#x60;createConversionAuditMonitor&#x60;. | |

### Return type

[**DeleteAutomationTemplate200Response**](DeleteAutomationTemplate200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The domain is no longer watched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |

## deleteConversionAuditMonitorWithHttpInfo

> ApiResponse<DeleteAutomationTemplate200Response> deleteConversionAuditMonitor deleteConversionAuditMonitorWithHttpInfo(monitorId)

Stop watching a domain

Stops the daily checks and alert emails for this domain. The host&#39;s public report stays.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String monitorId = "monitorId_example"; // String | The monitor's `id`, from `listConversionAuditMonitors` or `createConversionAuditMonitor`.
        try {
            ApiResponse<DeleteAutomationTemplate200Response> response = apiInstance.deleteConversionAuditMonitorWithHttpInfo(monitorId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#deleteConversionAuditMonitor");
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
| **monitorId** | **String**| The monitor&#39;s &#x60;id&#x60;, from &#x60;listConversionAuditMonitors&#x60; or &#x60;createConversionAuditMonitor&#x60;. | |

### Return type

ApiResponse<[**DeleteAutomationTemplate200Response**](DeleteAutomationTemplate200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The domain is no longer watched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |


## getLatestConversionAudit

> GetLatestConversionAudit200Response getLatestConversionAudit(host)

Get a host&#39;s latest stored conversion audit

Read the latest stored Conversion Leak Report for a host without running a new scan. Each homepage scan on is-bleeding.com that could read the site&#39;s pixels replaces that host&#39;s stored report. Scans made with &#x60;auditConversionTracking&#x60; are stored the same way.  The API key is optional. Without one, a caller&#39;s IP address gets 60 requests a minute. The Zernio MCP server always needs a key.  Returns &#x60;404&#x60; when the host has no stored report. Run &#x60;auditConversionTracking&#x60; to scan it now. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String host = "example.com"; // String | The host to look up. A full URL is reduced to its host; `www.` and letter case are ignored.
        try {
            GetLatestConversionAudit200Response result = apiInstance.getLatestConversionAudit(host);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#getLatestConversionAudit");
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
| **host** | **String**| The host to look up. A full URL is reduced to its host; &#x60;www.&#x60; and letter case are ignored. | |

### Return type

[**GetLatestConversionAudit200Response**](GetLatestConversionAudit200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored report, its fix prompt and its public page |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |

## getLatestConversionAuditWithHttpInfo

> ApiResponse<GetLatestConversionAudit200Response> getLatestConversionAudit getLatestConversionAuditWithHttpInfo(host)

Get a host&#39;s latest stored conversion audit

Read the latest stored Conversion Leak Report for a host without running a new scan. Each homepage scan on is-bleeding.com that could read the site&#39;s pixels replaces that host&#39;s stored report. Scans made with &#x60;auditConversionTracking&#x60; are stored the same way.  The API key is optional. Without one, a caller&#39;s IP address gets 60 requests a minute. The Zernio MCP server always needs a key.  Returns &#x60;404&#x60; when the host has no stored report. Run &#x60;auditConversionTracking&#x60; to scan it now. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String host = "example.com"; // String | The host to look up. A full URL is reduced to its host; `www.` and letter case are ignored.
        try {
            ApiResponse<GetLatestConversionAudit200Response> response = apiInstance.getLatestConversionAuditWithHttpInfo(host);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#getLatestConversionAudit");
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
| **host** | **String**| The host to look up. A full URL is reduced to its host; &#x60;www.&#x60; and letter case are ignored. | |

### Return type

ApiResponse<[**GetLatestConversionAudit200Response**](GetLatestConversionAudit200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stored report, its fix prompt and its public page |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |


## getMetaConversionAudit

> MetaDatasetAudit getMetaConversionAudit(accountId, adAccountId, pixelId)

Audit a connected Meta pixel from inside Events Manager

The connected follow-up to the Conversion Leak Report. A page scan only sees the browser; this reads what Meta itself recorded for the ad account&#39;s pixel (dataset) with the connection&#39;s own token, over the last 7 days.  ### What it reads  - each event&#39;s volume per day, its last 24 hours and the last hour Meta counted it in - the share of each event that arrived through the Conversions API (server) rather than the browser pixel - Event Match Quality per event, with the coverage of every customer-information key Meta matched on (email, phone, external id, IP address, user agent, &#x60;fbp&#x60;, &#x60;fbc&#x60;, name and address fields) - the event_id, external_id and fbp deduplication coverage of browser and server copies, where an event has both - Meta&#39;s diagnostics for the dataset and its failed dataset checks - whether automatic advanced matching and first-party cookies are on  Each &#x60;findings&#x60; entry is a problem one of those numbers shows, with its fix and who makes it (&#x60;fix.by&#x60;):  - &#x60;zernio&#x60;: turning on Zernio server-side events or the Zernio site tag fixes it - &#x60;you&#x60;: a change in your site or API call - &#x60;meta&#x60;: a setting only Events Manager has  Meta does not return a business&#39;s verified domains or an Aggregated Event Measurement setup to this API, so both are listed under &#x60;unavailable&#x60;, with any read Meta refused.  &#x60;accountId&#x60; is a Meta ads connection (or the Facebook account it belongs to). Without &#x60;adAccountId&#x60;, the first selected ad account that has a pixel is audited; without &#x60;pixelId&#x60;, its most recently active pixel. The result is cached for 10 minutes per pixel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String accountId = "6a10b66d520992756da032cb"; // String | The Meta ads connection to read with.
        String adAccountId = "act_757082720485182"; // String | The ad account whose pixel is audited. Must be selected on the connection.
        String pixelId = "1729525464415281"; // String | One of the ad account's pixels (`datasets[].id`).
        try {
            MetaDatasetAudit result = apiInstance.getMetaConversionAudit(accountId, adAccountId, pixelId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#getMetaConversionAudit");
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
| **accountId** | **String**| The Meta ads connection to read with. | |
| **adAccountId** | **String**| The ad account whose pixel is audited. Must be selected on the connection. | [optional] |
| **pixelId** | **String**| One of the ad account&#39;s pixels (&#x60;datasets[].id&#x60;). | [optional] |

### Return type

[**MetaDatasetAudit**](MetaDatasetAudit.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pixel&#39;s events, findings and what Meta did not expose |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The ad account is not selected on the connection, or the key cannot use ads |  -  |
| **404** | Resource not found |  -  |
| **501** | The connection is not a Meta connection |  -  |
| **502** | Meta refused to list the ad account&#39;s pixels |  -  |

## getMetaConversionAuditWithHttpInfo

> ApiResponse<MetaDatasetAudit> getMetaConversionAudit getMetaConversionAuditWithHttpInfo(accountId, adAccountId, pixelId)

Audit a connected Meta pixel from inside Events Manager

The connected follow-up to the Conversion Leak Report. A page scan only sees the browser; this reads what Meta itself recorded for the ad account&#39;s pixel (dataset) with the connection&#39;s own token, over the last 7 days.  ### What it reads  - each event&#39;s volume per day, its last 24 hours and the last hour Meta counted it in - the share of each event that arrived through the Conversions API (server) rather than the browser pixel - Event Match Quality per event, with the coverage of every customer-information key Meta matched on (email, phone, external id, IP address, user agent, &#x60;fbp&#x60;, &#x60;fbc&#x60;, name and address fields) - the event_id, external_id and fbp deduplication coverage of browser and server copies, where an event has both - Meta&#39;s diagnostics for the dataset and its failed dataset checks - whether automatic advanced matching and first-party cookies are on  Each &#x60;findings&#x60; entry is a problem one of those numbers shows, with its fix and who makes it (&#x60;fix.by&#x60;):  - &#x60;zernio&#x60;: turning on Zernio server-side events or the Zernio site tag fixes it - &#x60;you&#x60;: a change in your site or API call - &#x60;meta&#x60;: a setting only Events Manager has  Meta does not return a business&#39;s verified domains or an Aggregated Event Measurement setup to this API, so both are listed under &#x60;unavailable&#x60;, with any read Meta refused.  &#x60;accountId&#x60; is a Meta ads connection (or the Facebook account it belongs to). Without &#x60;adAccountId&#x60;, the first selected ad account that has a pixel is audited; without &#x60;pixelId&#x60;, its most recently active pixel. The result is cached for 10 minutes per pixel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        String accountId = "6a10b66d520992756da032cb"; // String | The Meta ads connection to read with.
        String adAccountId = "act_757082720485182"; // String | The ad account whose pixel is audited. Must be selected on the connection.
        String pixelId = "1729525464415281"; // String | One of the ad account's pixels (`datasets[].id`).
        try {
            ApiResponse<MetaDatasetAudit> response = apiInstance.getMetaConversionAuditWithHttpInfo(accountId, adAccountId, pixelId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#getMetaConversionAudit");
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
| **accountId** | **String**| The Meta ads connection to read with. | |
| **adAccountId** | **String**| The ad account whose pixel is audited. Must be selected on the connection. | [optional] |
| **pixelId** | **String**| One of the ad account&#39;s pixels (&#x60;datasets[].id&#x60;). | [optional] |

### Return type

ApiResponse<[**MetaDatasetAudit**](MetaDatasetAudit.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pixel&#39;s events, findings and what Meta did not expose |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The ad account is not selected on the connection, or the key cannot use ads |  -  |
| **404** | Resource not found |  -  |
| **501** | The connection is not a Meta connection |  -  |
| **502** | Meta refused to list the ad account&#39;s pixels |  -  |


## listConversionAuditMonitors

> ListConversionAuditMonitors200Response listConversionAuditMonitors()

List watched domains

The domains you watch with the Conversion Leak Report, each with its last score and the score of each daily check.  Zernio rescans every watched domain once a day. When tracking breaks, it emails you what changed and the fix prompt. &#x60;createConversionAuditMonitor&#x60; lists what counts as a break. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        try {
            ListConversionAuditMonitors200Response result = apiInstance.listConversionAuditMonitors();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#listConversionAuditMonitors");
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

[**ListConversionAuditMonitors200Response**](ListConversionAuditMonitors200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your watched domains, sorted by host |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

## listConversionAuditMonitorsWithHttpInfo

> ApiResponse<ListConversionAuditMonitors200Response> listConversionAuditMonitors listConversionAuditMonitorsWithHttpInfo()

List watched domains

The domains you watch with the Conversion Leak Report, each with its last score and the score of each daily check.  Zernio rescans every watched domain once a day. When tracking breaks, it emails you what changed and the fix prompt. &#x60;createConversionAuditMonitor&#x60; lists what counts as a break. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionAuditApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionAuditApi apiInstance = new ConversionAuditApi(defaultClient);
        try {
            ApiResponse<ListConversionAuditMonitors200Response> response = apiInstance.listConversionAuditMonitorsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionAuditApi#listConversionAuditMonitors");
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

ApiResponse<[**ListConversionAuditMonitors200Response**](ListConversionAuditMonitors200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your watched domains, sorted by host |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

