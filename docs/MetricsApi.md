# MetricsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccountMetrics**](MetricsApi.md#getAccountMetrics) | **GET** /v1/metrics/accounts | Read follower and post totals per account, platform or scope over time |
| [**getAccountMetricsWithHttpInfo**](MetricsApi.md#getAccountMetricsWithHttpInfo) | **GET** /v1/metrics/accounts | Read follower and post totals per account, platform or scope over time |
| [**getAdAccountMetrics**](MetricsApi.md#getAdAccountMetrics) | **GET** /v1/metrics/ad-accounts | Read the uploaded results summed across ad accounts |
| [**getAdAccountMetricsWithHttpInfo**](MetricsApi.md#getAdAccountMetricsWithHttpInfo) | **GET** /v1/metrics/ad-accounts | Read the uploaded results summed across ad accounts |
| [**getAdMetrics**](MetricsApi.md#getAdMetrics) | **GET** /v1/metrics/ads | Read ad metrics by id, or one ad day by day with breakdowns |
| [**getAdMetricsWithHttpInfo**](MetricsApi.md#getAdMetricsWithHttpInfo) | **GET** /v1/metrics/ads | Read ad metrics by id, or one ad day by day with breakdowns |
| [**getCampaignMetrics**](MetricsApi.md#getCampaignMetrics) | **GET** /v1/metrics/campaigns | Read the uploaded results of each campaign over a window |
| [**getCampaignMetricsWithHttpInfo**](MetricsApi.md#getCampaignMetricsWithHttpInfo) | **GET** /v1/metrics/campaigns | Read the uploaded results of each campaign over a window |
| [**getInboxMetrics**](MetricsApi.md#getInboxMetrics) | **GET** /v1/metrics/inbox | Read message volume and response times |
| [**getInboxMetricsWithHttpInfo**](MetricsApi.md#getInboxMetricsWithHttpInfo) | **GET** /v1/metrics/inbox | Read message volume and response times |
| [**getInsightMetrics**](MetricsApi.md#getInsightMetrics) | **GET** /v1/metrics/insights | Read live account or post insights from the platform |
| [**getInsightMetricsWithHttpInfo**](MetricsApi.md#getInsightMetricsWithHttpInfo) | **GET** /v1/metrics/insights | Read live account or post insights from the platform |
| [**getMetricsCatalog**](MetricsApi.md#getMetricsCatalog) | **GET** /v1/metrics/catalog | List the metrics, groupings and limits of each metrics endpoint |
| [**getMetricsCatalogWithHttpInfo**](MetricsApi.md#getMetricsCatalogWithHttpInfo) | **GET** /v1/metrics/catalog | List the metrics, groupings and limits of each metrics endpoint |
| [**getPostMetrics**](MetricsApi.md#getPostMetrics) | **GET** /v1/metrics/posts | Read post metrics by id, day by day, as a list, or grouped |
| [**getPostMetricsWithHttpInfo**](MetricsApi.md#getPostMetricsWithHttpInfo) | **GET** /v1/metrics/posts | Read post metrics by id, day by day, as a list, or grouped |
| [**queryGoogleAds**](MetricsApi.md#queryGoogleAds) | **POST** /v1/metrics/platform-queries/google-ads | Run a Google Ads Query Language search on one customer |
| [**queryGoogleAdsWithHttpInfo**](MetricsApi.md#queryGoogleAdsWithHttpInfo) | **POST** /v1/metrics/platform-queries/google-ads | Run a Google Ads Query Language search on one customer |
| [**queryGoogleAnalytics**](MetricsApi.md#queryGoogleAnalytics) | **POST** /v1/metrics/platform-queries/google-analytics | Run a GA4 standard or realtime report on one property |
| [**queryGoogleAnalyticsWithHttpInfo**](MetricsApi.md#queryGoogleAnalyticsWithHttpInfo) | **POST** /v1/metrics/platform-queries/google-analytics | Run a GA4 standard or realtime report on one property |
| [**queryMetaAds**](MetricsApi.md#queryMetaAds) | **POST** /v1/metrics/platform-queries/meta-ads | Run a Meta Marketing API insights query on one ad account |
| [**queryMetaAdsWithHttpInfo**](MetricsApi.md#queryMetaAdsWithHttpInfo) | **POST** /v1/metrics/platform-queries/meta-ads | Run a Meta Marketing API insights query on one ad account |
| [**queryTikTokAds**](MetricsApi.md#queryTikTokAds) | **POST** /v1/metrics/platform-queries/tiktok-ads | Run a TikTok Marketing API report on one advertiser |
| [**queryTikTokAdsWithHttpInfo**](MetricsApi.md#queryTikTokAdsWithHttpInfo) | **POST** /v1/metrics/platform-queries/tiktok-ads | Run a TikTok Marketing API report on one advertiser |



## getAccountMetrics

> AccountMetricsResponse getAccountMetrics(accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, attribution, limit, cursor)

Read follower and post totals per account, platform or scope over time

Reads followers, the account counters the platform reports (media count, video count...) and the totals of the posts each account published, per account, per platform or for the whole scope, for the whole window or by day, week or month.  - Scope: exactly one of &#x60;accountId&#x60; (up to 25) or &#x60;profileId&#x60; (one, with an optional &#x60;platform&#x60;). - &#x60;groupBy&#x60;: &#x60;account&#x60; (the default, one row per account and period), &#x60;platform&#x60; or &#x60;none&#x60;. - &#x60;granularity&#x60;: &#x60;total&#x60; (the default), &#x60;day&#x60;, &#x60;week&#x60; (rows start on Monday) or &#x60;month&#x60;. A row&#39;s &#x60;date&#x60; is the start of its period, never before &#x60;fromDate&#x60;. - &#x60;attribution&#x60;: &#x60;publish&#x60; (the default) counts each post on the day it was published; &#x60;received&#x60; counts each interaction on the day it arrived, for windows up to 92 days. - &#x60;granularity&#x3D;week&amp;groupBy&#x3D;platform&amp;metrics&#x3D;postCount,engagementRate&#x60;: how many posts each platform got per week and their pooled engagement rate. The newer way to read &#x60;GET /v1/analytics/posting-frequency&#x60;.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 90 days; the window is at most 366 days. Followers are one value per day, taken at 02:00 UTC. &#x60;GET /v1/metrics/catalog?entity&#x3D;accounts&#x60; lists every metric with the platforms that report it.  Each team has an analytics compute budget of 24 seconds per 30-second window across these reads: a request that would pass it is refused with 429 &#x60;details.scope: team_budget&#x60; before it runs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String accountId = "accountId_example"; // String | Comma-separated account ids, up to 25.
        String profileId = "profileId_example"; // String | One profile id.
        String metrics = "metrics_example"; // String | Comma-separated metric names from the catalog. Defaults to every metric.
        String groupBy = "groupBy_example"; // String | Comma-separated groupings from the catalog, at most 2.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC).
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC).
        String platform = "tiktok"; // String | Only with profileId.
        String granularity = "total"; // String | 
        String attribution = "publish"; // String | 
        Integer limit = 50; // Integer | Rows per page, 50 by default, 100 at most.
        String cursor = "cursor_example"; // String | pagination.nextCursor of the previous page, sent with the same query.
        try {
            AccountMetricsResponse result = apiInstance.getAccountMetrics(accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, attribution, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getAccountMetrics");
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
| **accountId** | **String**| Comma-separated account ids, up to 25. | [optional] |
| **profileId** | **String**| One profile id. | [optional] |
| **metrics** | **String**| Comma-separated metric names from the catalog. Defaults to every metric. | [optional] |
| **groupBy** | **String**| Comma-separated groupings from the catalog, at most 2. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **platform** | **String**| Only with profileId. | [optional] [enum: tiktok, instagram, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, whatsapp, discord, slack] |
| **granularity** | **String**|  | [optional] [default to total] [enum: total, day, week, month] |
| **attribution** | **String**|  | [optional] [default to publish] [enum: publish, received] |
| **limit** | **Integer**| Rows per page, 50 by default, 100 at most. | [optional] [default to 50] |
| **cursor** | **String**| pagination.nextCursor of the previous page, sent with the same query. | [optional] |

### Return type

[**AccountMetricsResponse**](AccountMetricsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per account, platform or scope, and period. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## getAccountMetricsWithHttpInfo

> ApiResponse<AccountMetricsResponse> getAccountMetrics getAccountMetricsWithHttpInfo(accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, attribution, limit, cursor)

Read follower and post totals per account, platform or scope over time

Reads followers, the account counters the platform reports (media count, video count...) and the totals of the posts each account published, per account, per platform or for the whole scope, for the whole window or by day, week or month.  - Scope: exactly one of &#x60;accountId&#x60; (up to 25) or &#x60;profileId&#x60; (one, with an optional &#x60;platform&#x60;). - &#x60;groupBy&#x60;: &#x60;account&#x60; (the default, one row per account and period), &#x60;platform&#x60; or &#x60;none&#x60;. - &#x60;granularity&#x60;: &#x60;total&#x60; (the default), &#x60;day&#x60;, &#x60;week&#x60; (rows start on Monday) or &#x60;month&#x60;. A row&#39;s &#x60;date&#x60; is the start of its period, never before &#x60;fromDate&#x60;. - &#x60;attribution&#x60;: &#x60;publish&#x60; (the default) counts each post on the day it was published; &#x60;received&#x60; counts each interaction on the day it arrived, for windows up to 92 days. - &#x60;granularity&#x3D;week&amp;groupBy&#x3D;platform&amp;metrics&#x3D;postCount,engagementRate&#x60;: how many posts each platform got per week and their pooled engagement rate. The newer way to read &#x60;GET /v1/analytics/posting-frequency&#x60;.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 90 days; the window is at most 366 days. Followers are one value per day, taken at 02:00 UTC. &#x60;GET /v1/metrics/catalog?entity&#x3D;accounts&#x60; lists every metric with the platforms that report it.  Each team has an analytics compute budget of 24 seconds per 30-second window across these reads: a request that would pass it is refused with 429 &#x60;details.scope: team_budget&#x60; before it runs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String accountId = "accountId_example"; // String | Comma-separated account ids, up to 25.
        String profileId = "profileId_example"; // String | One profile id.
        String metrics = "metrics_example"; // String | Comma-separated metric names from the catalog. Defaults to every metric.
        String groupBy = "groupBy_example"; // String | Comma-separated groupings from the catalog, at most 2.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC).
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC).
        String platform = "tiktok"; // String | Only with profileId.
        String granularity = "total"; // String | 
        String attribution = "publish"; // String | 
        Integer limit = 50; // Integer | Rows per page, 50 by default, 100 at most.
        String cursor = "cursor_example"; // String | pagination.nextCursor of the previous page, sent with the same query.
        try {
            ApiResponse<AccountMetricsResponse> response = apiInstance.getAccountMetricsWithHttpInfo(accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, attribution, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getAccountMetrics");
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
| **accountId** | **String**| Comma-separated account ids, up to 25. | [optional] |
| **profileId** | **String**| One profile id. | [optional] |
| **metrics** | **String**| Comma-separated metric names from the catalog. Defaults to every metric. | [optional] |
| **groupBy** | **String**| Comma-separated groupings from the catalog, at most 2. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **platform** | **String**| Only with profileId. | [optional] [enum: tiktok, instagram, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, whatsapp, discord, slack] |
| **granularity** | **String**|  | [optional] [default to total] [enum: total, day, week, month] |
| **attribution** | **String**|  | [optional] [default to publish] [enum: publish, received] |
| **limit** | **Integer**| Rows per page, 50 by default, 100 at most. | [optional] [default to 50] |
| **cursor** | **String**| pagination.nextCursor of the previous page, sent with the same query. | [optional] |

### Return type

ApiResponse<[**AccountMetricsResponse**](AccountMetricsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per account, platform or scope, and period. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## getAdAccountMetrics

> AdAccountMetricsResponse getAdAccountMetrics(fromDate, toDate, adAccountId)

Read the uploaded results summed across ad accounts

Sums each result metric you uploaded across ad accounts (every ad account the key can read, or the platform ids in &#x60;adAccountId&#x60;) over &#x60;fromDate&#x60; to &#x60;toDate&#x60; (both required, at most 400 days), with the same metrics as &#x60;GET /v1/metrics/campaigns&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive. The range is at most 400 days.
        String adAccountId = "adAccountId_example"; // String | Comma-separated platform ad account ids. Defaults to every ad account the key sees.
        try {
            AdAccountMetricsResponse result = apiInstance.getAdAccountMetrics(fromDate, toDate, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getAdAccountMetrics");
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
| **fromDate** | **LocalDate**| First day, inclusive. | |
| **toDate** | **LocalDate**| Last day, inclusive. The range is at most 400 days. | |
| **adAccountId** | **String**| Comma-separated platform ad account ids. Defaults to every ad account the key sees. | [optional] |

### Return type

[**AdAccountMetricsResponse**](AdAccountMetricsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The results summed over the window. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## getAdAccountMetricsWithHttpInfo

> ApiResponse<AdAccountMetricsResponse> getAdAccountMetrics getAdAccountMetricsWithHttpInfo(fromDate, toDate, adAccountId)

Read the uploaded results summed across ad accounts

Sums each result metric you uploaded across ad accounts (every ad account the key can read, or the platform ids in &#x60;adAccountId&#x60;) over &#x60;fromDate&#x60; to &#x60;toDate&#x60; (both required, at most 400 days), with the same metrics as &#x60;GET /v1/metrics/campaigns&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive. The range is at most 400 days.
        String adAccountId = "adAccountId_example"; // String | Comma-separated platform ad account ids. Defaults to every ad account the key sees.
        try {
            ApiResponse<AdAccountMetricsResponse> response = apiInstance.getAdAccountMetricsWithHttpInfo(fromDate, toDate, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getAdAccountMetrics");
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
| **fromDate** | **LocalDate**| First day, inclusive. | |
| **toDate** | **LocalDate**| Last day, inclusive. The range is at most 400 days. | |
| **adAccountId** | **String**| Comma-separated platform ad account ids. Defaults to every ad account the key sees. | [optional] |

### Return type

ApiResponse<[**AdAccountMetricsResponse**](AdAccountMetricsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The results summed over the window. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## getAdMetrics

> AdMetricsResponse getAdMetrics(adId, granularity, fromDate, toDate, breakdowns, attributionWindows)

Read ad metrics by id, or one ad day by day with breakdowns

Reads the delivery and conversion metrics Zernio synced from the ad networks for up to 100 Zernio ad ids (&#x60;adId&#x60;, as &#x60;GET /v1/ads&#x60; returns them). Ids you cannot read come back in &#x60;meta.missingIds&#x60;.  - &#x60;granularity&#x3D;day&#x60; with one ad: one point per day. - &#x60;breakdowns&#x60; with one ad: read live from the network (age, gender, country, placement...), with &#x60;attributionWindows&#x60; for Meta.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 90 days; the window is at most 730 days. &#x60;meta.backfillPending&#x60; is true while older days are still being fetched. Money is in the ad account currency (&#x60;currency&#x60;). &#x60;GET /v1/metrics/catalog?entity&#x3D;ads&#x60; lists every metric with the networks that report it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String adId = "adId_example"; // String | Comma-separated Zernio ad ids, up to 100.
        String granularity = "total"; // String | day reads one ad, one point per day.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Without fromDate and toDate, the last 90 days.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC).
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdowns, read live from the platform. One ad only.
        String attributionWindows = "attributionWindows_example"; // String | Meta attribution windows for the breakdowns, comma-separated.
        try {
            AdMetricsResponse result = apiInstance.getAdMetrics(adId, granularity, fromDate, toDate, breakdowns, attributionWindows);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getAdMetrics");
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
| **adId** | **String**| Comma-separated Zernio ad ids, up to 100. | |
| **granularity** | **String**| day reads one ad, one point per day. | [optional] [default to total] [enum: total, day] |
| **fromDate** | **LocalDate**| Without fromDate and toDate, the last 90 days. | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **breakdowns** | **String**| Comma-separated breakdowns, read live from the platform. One ad only. | [optional] |
| **attributionWindows** | **String**| Meta attribution windows for the breakdowns, comma-separated. | [optional] |

### Return type

[**AdMetricsResponse**](AdMetricsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per ad. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## getAdMetricsWithHttpInfo

> ApiResponse<AdMetricsResponse> getAdMetrics getAdMetricsWithHttpInfo(adId, granularity, fromDate, toDate, breakdowns, attributionWindows)

Read ad metrics by id, or one ad day by day with breakdowns

Reads the delivery and conversion metrics Zernio synced from the ad networks for up to 100 Zernio ad ids (&#x60;adId&#x60;, as &#x60;GET /v1/ads&#x60; returns them). Ids you cannot read come back in &#x60;meta.missingIds&#x60;.  - &#x60;granularity&#x3D;day&#x60; with one ad: one point per day. - &#x60;breakdowns&#x60; with one ad: read live from the network (age, gender, country, placement...), with &#x60;attributionWindows&#x60; for Meta.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 90 days; the window is at most 730 days. &#x60;meta.backfillPending&#x60; is true while older days are still being fetched. Money is in the ad account currency (&#x60;currency&#x60;). &#x60;GET /v1/metrics/catalog?entity&#x3D;ads&#x60; lists every metric with the networks that report it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String adId = "adId_example"; // String | Comma-separated Zernio ad ids, up to 100.
        String granularity = "total"; // String | day reads one ad, one point per day.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Without fromDate and toDate, the last 90 days.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC).
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdowns, read live from the platform. One ad only.
        String attributionWindows = "attributionWindows_example"; // String | Meta attribution windows for the breakdowns, comma-separated.
        try {
            ApiResponse<AdMetricsResponse> response = apiInstance.getAdMetricsWithHttpInfo(adId, granularity, fromDate, toDate, breakdowns, attributionWindows);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getAdMetrics");
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
| **adId** | **String**| Comma-separated Zernio ad ids, up to 100. | |
| **granularity** | **String**| day reads one ad, one point per day. | [optional] [default to total] [enum: total, day] |
| **fromDate** | **LocalDate**| Without fromDate and toDate, the last 90 days. | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **breakdowns** | **String**| Comma-separated breakdowns, read live from the platform. One ad only. | [optional] |
| **attributionWindows** | **String**| Meta attribution windows for the breakdowns, comma-separated. | [optional] |

### Return type

ApiResponse<[**AdMetricsResponse**](AdMetricsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per ad. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## getCampaignMetrics

> CampaignMetricsResponse getCampaignMetrics(fromDate, toDate, limit, cursor, campaignId)

Read the uploaded results of each campaign over a window

Sums, per campaign, each result metric you uploaded (one key per metric, as &#x60;GET /v1/ads/campaign-results/metrics&#x60; lists them), with &#x60;cac_percent&#x60;, &#x60;cost_per_sale&#x60;, &#x60;cost_per_qualified_lead&#x60;, &#x60;lead_to_sale&#x60; and &#x60;qualified_rate&#x60; next to them, over &#x60;fromDate&#x60; to &#x60;toDate&#x60; (both required, at most 400 days).  Filter with &#x60;campaignId&#x60; (platform campaign ids); pages with &#x60;cursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive. The range is at most 400 days.
        Integer limit = 50; // Integer | Rows per page, 50 by default, 100 at most.
        String cursor = "cursor_example"; // String | pagination.nextCursor of the previous page, sent with the same query.
        String campaignId = "campaignId_example"; // String | Comma-separated platform campaign ids.
        try {
            CampaignMetricsResponse result = apiInstance.getCampaignMetrics(fromDate, toDate, limit, cursor, campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getCampaignMetrics");
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
| **fromDate** | **LocalDate**| First day, inclusive. | |
| **toDate** | **LocalDate**| Last day, inclusive. The range is at most 400 days. | |
| **limit** | **Integer**| Rows per page, 50 by default, 100 at most. | [optional] [default to 50] |
| **cursor** | **String**| pagination.nextCursor of the previous page, sent with the same query. | [optional] |
| **campaignId** | **String**| Comma-separated platform campaign ids. | [optional] |

### Return type

[**CampaignMetricsResponse**](CampaignMetricsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per campaign with results in the window. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## getCampaignMetricsWithHttpInfo

> ApiResponse<CampaignMetricsResponse> getCampaignMetrics getCampaignMetricsWithHttpInfo(fromDate, toDate, limit, cursor, campaignId)

Read the uploaded results of each campaign over a window

Sums, per campaign, each result metric you uploaded (one key per metric, as &#x60;GET /v1/ads/campaign-results/metrics&#x60; lists them), with &#x60;cac_percent&#x60;, &#x60;cost_per_sale&#x60;, &#x60;cost_per_qualified_lead&#x60;, &#x60;lead_to_sale&#x60; and &#x60;qualified_rate&#x60; next to them, over &#x60;fromDate&#x60; to &#x60;toDate&#x60; (both required, at most 400 days).  Filter with &#x60;campaignId&#x60; (platform campaign ids); pages with &#x60;cursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive. The range is at most 400 days.
        Integer limit = 50; // Integer | Rows per page, 50 by default, 100 at most.
        String cursor = "cursor_example"; // String | pagination.nextCursor of the previous page, sent with the same query.
        String campaignId = "campaignId_example"; // String | Comma-separated platform campaign ids.
        try {
            ApiResponse<CampaignMetricsResponse> response = apiInstance.getCampaignMetricsWithHttpInfo(fromDate, toDate, limit, cursor, campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getCampaignMetrics");
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
| **fromDate** | **LocalDate**| First day, inclusive. | |
| **toDate** | **LocalDate**| Last day, inclusive. The range is at most 400 days. | |
| **limit** | **Integer**| Rows per page, 50 by default, 100 at most. | [optional] [default to 50] |
| **cursor** | **String**| pagination.nextCursor of the previous page, sent with the same query. | [optional] |
| **campaignId** | **String**| Comma-separated platform campaign ids. | [optional] |

### Return type

ApiResponse<[**CampaignMetricsResponse**](CampaignMetricsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per campaign with results in the window. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## getInboxMetrics

> InboxMetricsResponse getInboxMetrics(conversationId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, source, granularity, sort, include, limit, cursor)

Read message volume and response times

Counts messages received, sent, read and failed, conversations and replies, and response times (median, p90, p99, mean, min, max) across the inbox, from the messages Zernio logged.  - Scope: &#x60;conversationId&#x60; (up to 25, one row per conversation), &#x60;accountId&#x60; (up to 25) or one &#x60;profileId&#x60;. Without a scope, every account the key can read. - &#x60;groupBy&#x60; (at most 2): &#x60;account&#x60;, &#x60;platform&#x60;, &#x60;source&#x60;, &#x60;hourOfWeek&#x60; (one row per UTC weekday and hour), &#x60;responseTimeBucket&#x60; (with &#x60;metrics&#x3D;replied&#x60;) or &#x60;conversation&#x60; (paged with &#x60;cursor&#x60;, &#x60;include&#x3D;total&#x60; counts up to 100,000). - &#x60;granularity&#x60;: &#x60;total&#x60; (the default), &#x60;day&#x60; or &#x60;week&#x60;. - &#x60;include&#x3D;account&#x60; adds usernames to account rows; &#x60;include&#x3D;conversation&#x60; adds the participant and last message to conversation rows.  Response time metrics are returned only when named in &#x60;metrics&#x60;. Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 30 days; the window is at most 90 days. &#x60;GET /v1/metrics/catalog?entity&#x3D;inbox&#x60; lists every metric, sort and groupBy.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String conversationId = "conversationId_example"; // String | Comma-separated conversation ids (Zernio or platform), up to 25: one row per conversation.
        String accountId = "accountId_example"; // String | Comma-separated account ids, up to 25.
        String profileId = "profileId_example"; // String | One profile id.
        String metrics = "metrics_example"; // String | Comma-separated metric names from the catalog. Defaults to the counts; response times only when named.
        String groupBy = "groupBy_example"; // String | Comma-separated groupings from the catalog, at most 2: account, conversation, platform, source, hourOfWeek, responseTimeBucket.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 90 days.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today.
        String platform = "platform_example"; // String | A messaging platform, such as instagram or whatsapp.
        String source = "source_example"; // String | Only messages sent from this source, such as api or broadcast. Not with response time metrics.
        String granularity = "total"; // String | 
        String sort = "sort_example"; // String | A sort from the catalog, such as messages-desc. With granularity=total.
        String include = "include_example"; // String | Comma-separated includes from the catalog: account, conversation, total.
        Integer limit = 56; // Integer | Rows returned with groupBy=account (10 by default, 100 at most) or groupBy=conversation (50 by default, 1,000 at most).
        String cursor = "cursor_example"; // String | With groupBy=conversation: pagination.nextCursor of the previous page.
        try {
            InboxMetricsResponse result = apiInstance.getInboxMetrics(conversationId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, source, granularity, sort, include, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getInboxMetrics");
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
| **conversationId** | **String**| Comma-separated conversation ids (Zernio or platform), up to 25: one row per conversation. | [optional] |
| **accountId** | **String**| Comma-separated account ids, up to 25. | [optional] |
| **profileId** | **String**| One profile id. | [optional] |
| **metrics** | **String**| Comma-separated metric names from the catalog. Defaults to the counts; response times only when named. | [optional] |
| **groupBy** | **String**| Comma-separated groupings from the catalog, at most 2: account, conversation, platform, source, hourOfWeek, responseTimeBucket. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 90 days. | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today. | [optional] |
| **platform** | **String**| A messaging platform, such as instagram or whatsapp. | [optional] |
| **source** | **String**| Only messages sent from this source, such as api or broadcast. Not with response time metrics. | [optional] |
| **granularity** | **String**|  | [optional] [default to total] [enum: total, day, week] |
| **sort** | **String**| A sort from the catalog, such as messages-desc. With granularity&#x3D;total. | [optional] |
| **include** | **String**| Comma-separated includes from the catalog: account, conversation, total. | [optional] |
| **limit** | **Integer**| Rows returned with groupBy&#x3D;account (10 by default, 100 at most) or groupBy&#x3D;conversation (50 by default, 1,000 at most). | [optional] |
| **cursor** | **String**| With groupBy&#x3D;conversation: pagination.nextCursor of the previous page. | [optional] |

### Return type

[**InboxMetricsResponse**](InboxMetricsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per period and group. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## getInboxMetricsWithHttpInfo

> ApiResponse<InboxMetricsResponse> getInboxMetrics getInboxMetricsWithHttpInfo(conversationId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, source, granularity, sort, include, limit, cursor)

Read message volume and response times

Counts messages received, sent, read and failed, conversations and replies, and response times (median, p90, p99, mean, min, max) across the inbox, from the messages Zernio logged.  - Scope: &#x60;conversationId&#x60; (up to 25, one row per conversation), &#x60;accountId&#x60; (up to 25) or one &#x60;profileId&#x60;. Without a scope, every account the key can read. - &#x60;groupBy&#x60; (at most 2): &#x60;account&#x60;, &#x60;platform&#x60;, &#x60;source&#x60;, &#x60;hourOfWeek&#x60; (one row per UTC weekday and hour), &#x60;responseTimeBucket&#x60; (with &#x60;metrics&#x3D;replied&#x60;) or &#x60;conversation&#x60; (paged with &#x60;cursor&#x60;, &#x60;include&#x3D;total&#x60; counts up to 100,000). - &#x60;granularity&#x60;: &#x60;total&#x60; (the default), &#x60;day&#x60; or &#x60;week&#x60;. - &#x60;include&#x3D;account&#x60; adds usernames to account rows; &#x60;include&#x3D;conversation&#x60; adds the participant and last message to conversation rows.  Response time metrics are returned only when named in &#x60;metrics&#x60;. Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 30 days; the window is at most 90 days. &#x60;GET /v1/metrics/catalog?entity&#x3D;inbox&#x60; lists every metric, sort and groupBy.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String conversationId = "conversationId_example"; // String | Comma-separated conversation ids (Zernio or platform), up to 25: one row per conversation.
        String accountId = "accountId_example"; // String | Comma-separated account ids, up to 25.
        String profileId = "profileId_example"; // String | One profile id.
        String metrics = "metrics_example"; // String | Comma-separated metric names from the catalog. Defaults to the counts; response times only when named.
        String groupBy = "groupBy_example"; // String | Comma-separated groupings from the catalog, at most 2: account, conversation, platform, source, hourOfWeek, responseTimeBucket.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 90 days.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today.
        String platform = "platform_example"; // String | A messaging platform, such as instagram or whatsapp.
        String source = "source_example"; // String | Only messages sent from this source, such as api or broadcast. Not with response time metrics.
        String granularity = "total"; // String | 
        String sort = "sort_example"; // String | A sort from the catalog, such as messages-desc. With granularity=total.
        String include = "include_example"; // String | Comma-separated includes from the catalog: account, conversation, total.
        Integer limit = 56; // Integer | Rows returned with groupBy=account (10 by default, 100 at most) or groupBy=conversation (50 by default, 1,000 at most).
        String cursor = "cursor_example"; // String | With groupBy=conversation: pagination.nextCursor of the previous page.
        try {
            ApiResponse<InboxMetricsResponse> response = apiInstance.getInboxMetricsWithHttpInfo(conversationId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, source, granularity, sort, include, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getInboxMetrics");
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
| **conversationId** | **String**| Comma-separated conversation ids (Zernio or platform), up to 25: one row per conversation. | [optional] |
| **accountId** | **String**| Comma-separated account ids, up to 25. | [optional] |
| **profileId** | **String**| One profile id. | [optional] |
| **metrics** | **String**| Comma-separated metric names from the catalog. Defaults to the counts; response times only when named. | [optional] |
| **groupBy** | **String**| Comma-separated groupings from the catalog, at most 2: account, conversation, platform, source, hourOfWeek, responseTimeBucket. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 90 days. | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today. | [optional] |
| **platform** | **String**| A messaging platform, such as instagram or whatsapp. | [optional] |
| **source** | **String**| Only messages sent from this source, such as api or broadcast. Not with response time metrics. | [optional] |
| **granularity** | **String**|  | [optional] [default to total] [enum: total, day, week] |
| **sort** | **String**| A sort from the catalog, such as messages-desc. With granularity&#x3D;total. | [optional] |
| **include** | **String**| Comma-separated includes from the catalog: account, conversation, total. | [optional] |
| **limit** | **Integer**| Rows returned with groupBy&#x3D;account (10 by default, 100 at most) or groupBy&#x3D;conversation (50 by default, 1,000 at most). | [optional] |
| **cursor** | **String**| With groupBy&#x3D;conversation: pagination.nextCursor of the previous page. | [optional] |

### Return type

ApiResponse<[**InboxMetricsResponse**](InboxMetricsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per period and group. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## getInsightMetrics

> InsightMetricsResponse getInsightMetrics(accountId, metrics, platformPostId, granularity, groupBy, breakdown, timeframe, cursor, limit, include, fromDate, toDate)

Read live account or post insights from the platform

Reads insights the platform computes and Zernio does not store (page views, profile visits, watch time, audience demographics...), live from the platform, for one account or one of its posts (&#x60;platformPostId&#x60;).  Platforms: Facebook, Instagram, LinkedIn, TikTok, YouTube, Pinterest, Google Business and Google Search Console. Another platform answers 400 on &#x60;accountId&#x60;, a disconnected account 401 &#x60;account_disconnected&#x60;, and a platform error the platform&#39;s own code under &#x60;platformError&#x60;.  - &#x60;granularity&#x60;: &#x60;total&#x60; (the default) or &#x60;day&#x60;. - &#x60;groupBy&#x3D;demographic&#x60; with one metric and &#x60;breakdown&#x60; (age, gender, country, city...): one row per audience segment. LinkedIn: organizations only. - &#x60;groupBy&#x3D;hour&#x60;: Instagram followers online per day and hour of the last 30 days. - &#x60;groupBy&#x3D;keyword&#x60;: Google Business search keywords, one row per keyword, paged with &#x60;cursor&#x60;.  Google Search Console answers clicks, impressions, ctr (0 to 1) and position (1 is the top), final days only:  - Without groupBy: the site totals. &#x60;granularity&#x3D;day&#x60; adds the date. - &#x60;groupBy&#x60; combines any of &#x60;query&#x60;, &#x60;page&#x60;, &#x60;country&#x60; and &#x60;device&#x60; (&#x60;groupBy&#x3D;query,country&#x60;): one row per combination, most clicks first, with each value in &#x60;dimensions&#x60;. - Pages with &#x60;limit&#x60; (up to 25,000, 1,000 by default) and &#x60;cursor&#x60;. - &#x60;include&#x3D;retentionCurve&#x60; with a YouTube &#x60;platformPostId&#x60;: the audience retention curve.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 30 days; the window is at most 541 days. &#x60;GET /v1/metrics/catalog?entity&#x3D;insights&amp;platform&#x3D;...&#x60; lists each platform&#39;s metrics. Metrics the platform cannot answer for this account are listed in &#x60;meta.unavailableMetrics&#x60; instead of failing the request.  Each request calls the platform: read each account every few minutes at most. These reads share the &#x60;account-insights&#x60; cap and the 120 reads per hour of one account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String accountId = "accountId_example"; // String | One account id.
        String metrics = "metrics_example"; // String | Comma-separated metric names (up to 25). Defaults to the platform's default metrics. `GET /v1/metrics/catalog?entity=insights&platform=...` lists them.
        String platformPostId = "platformPostId_example"; // String | One post of the account, by its platform id: answers the post's live insights instead of the account's.
        String granularity = "total"; // String | Defaults to total; groupBy=hour answers per day.
        String groupBy = "groupBy_example"; // String | demographic: audience segments (age, gender, country...). hour: Instagram followers online per day and hour, last 30 days. keyword: Google Business search keywords per month. query, page, country, device: Google Search Console, combined with commas (groupBy=query,country).
        String breakdown = "breakdown_example"; // String | With groupBy=demographic: comma-separated segments. Defaults to the platform's default segments.
        String timeframe = "this_week"; // String | Instagram demographics only. Defaults to this_month.
        String cursor = "cursor_example"; // String | With groupBy=keyword or a Search Console account: pagination.nextCursor of the previous page, sent with the same query.
        Integer limit = 56; // Integer | Search Console accounts only: rows per page. Defaults to 1,000.
        String include = "include_example"; // String | With platformPostId on YouTube: retentionCurve adds the audience retention curve.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 541 days.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today.
        try {
            InsightMetricsResponse result = apiInstance.getInsightMetrics(accountId, metrics, platformPostId, granularity, groupBy, breakdown, timeframe, cursor, limit, include, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getInsightMetrics");
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
| **accountId** | **String**| One account id. | |
| **metrics** | **String**| Comma-separated metric names (up to 25). Defaults to the platform&#39;s default metrics. &#x60;GET /v1/metrics/catalog?entity&#x3D;insights&amp;platform&#x3D;...&#x60; lists them. | [optional] |
| **platformPostId** | **String**| One post of the account, by its platform id: answers the post&#39;s live insights instead of the account&#39;s. | [optional] |
| **granularity** | **String**| Defaults to total; groupBy&#x3D;hour answers per day. | [optional] [enum: total, day] |
| **groupBy** | **String**| demographic: audience segments (age, gender, country...). hour: Instagram followers online per day and hour, last 30 days. keyword: Google Business search keywords per month. query, page, country, device: Google Search Console, combined with commas (groupBy&#x3D;query,country). | [optional] |
| **breakdown** | **String**| With groupBy&#x3D;demographic: comma-separated segments. Defaults to the platform&#39;s default segments. | [optional] |
| **timeframe** | **String**| Instagram demographics only. Defaults to this_month. | [optional] [enum: this_week, this_month] |
| **cursor** | **String**| With groupBy&#x3D;keyword or a Search Console account: pagination.nextCursor of the previous page, sent with the same query. | [optional] |
| **limit** | **Integer**| Search Console accounts only: rows per page. Defaults to 1,000. | [optional] |
| **include** | **String**| With platformPostId on YouTube: retentionCurve adds the audience retention curve. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 541 days. | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today. | [optional] |

### Return type

[**InsightMetricsResponse**](InsightMetricsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per period, or per segment with groupBy. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key, or the account is disconnected (&#x60;code: account_disconnected&#x60;, &#x60;action: reconnect&#x60;). |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## getInsightMetricsWithHttpInfo

> ApiResponse<InsightMetricsResponse> getInsightMetrics getInsightMetricsWithHttpInfo(accountId, metrics, platformPostId, granularity, groupBy, breakdown, timeframe, cursor, limit, include, fromDate, toDate)

Read live account or post insights from the platform

Reads insights the platform computes and Zernio does not store (page views, profile visits, watch time, audience demographics...), live from the platform, for one account or one of its posts (&#x60;platformPostId&#x60;).  Platforms: Facebook, Instagram, LinkedIn, TikTok, YouTube, Pinterest, Google Business and Google Search Console. Another platform answers 400 on &#x60;accountId&#x60;, a disconnected account 401 &#x60;account_disconnected&#x60;, and a platform error the platform&#39;s own code under &#x60;platformError&#x60;.  - &#x60;granularity&#x60;: &#x60;total&#x60; (the default) or &#x60;day&#x60;. - &#x60;groupBy&#x3D;demographic&#x60; with one metric and &#x60;breakdown&#x60; (age, gender, country, city...): one row per audience segment. LinkedIn: organizations only. - &#x60;groupBy&#x3D;hour&#x60;: Instagram followers online per day and hour of the last 30 days. - &#x60;groupBy&#x3D;keyword&#x60;: Google Business search keywords, one row per keyword, paged with &#x60;cursor&#x60;.  Google Search Console answers clicks, impressions, ctr (0 to 1) and position (1 is the top), final days only:  - Without groupBy: the site totals. &#x60;granularity&#x3D;day&#x60; adds the date. - &#x60;groupBy&#x60; combines any of &#x60;query&#x60;, &#x60;page&#x60;, &#x60;country&#x60; and &#x60;device&#x60; (&#x60;groupBy&#x3D;query,country&#x60;): one row per combination, most clicks first, with each value in &#x60;dimensions&#x60;. - Pages with &#x60;limit&#x60; (up to 25,000, 1,000 by default) and &#x60;cursor&#x60;. - &#x60;include&#x3D;retentionCurve&#x60; with a YouTube &#x60;platformPostId&#x60;: the audience retention curve.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; it reads the last 30 days; the window is at most 541 days. &#x60;GET /v1/metrics/catalog?entity&#x3D;insights&amp;platform&#x3D;...&#x60; lists each platform&#39;s metrics. Metrics the platform cannot answer for this account are listed in &#x60;meta.unavailableMetrics&#x60; instead of failing the request.  Each request calls the platform: read each account every few minutes at most. These reads share the &#x60;account-insights&#x60; cap and the 120 reads per hour of one account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String accountId = "accountId_example"; // String | One account id.
        String metrics = "metrics_example"; // String | Comma-separated metric names (up to 25). Defaults to the platform's default metrics. `GET /v1/metrics/catalog?entity=insights&platform=...` lists them.
        String platformPostId = "platformPostId_example"; // String | One post of the account, by its platform id: answers the post's live insights instead of the account's.
        String granularity = "total"; // String | Defaults to total; groupBy=hour answers per day.
        String groupBy = "groupBy_example"; // String | demographic: audience segments (age, gender, country...). hour: Instagram followers online per day and hour, last 30 days. keyword: Google Business search keywords per month. query, page, country, device: Google Search Console, combined with commas (groupBy=query,country).
        String breakdown = "breakdown_example"; // String | With groupBy=demographic: comma-separated segments. Defaults to the platform's default segments.
        String timeframe = "this_week"; // String | Instagram demographics only. Defaults to this_month.
        String cursor = "cursor_example"; // String | With groupBy=keyword or a Search Console account: pagination.nextCursor of the previous page, sent with the same query.
        Integer limit = 56; // Integer | Search Console accounts only: rows per page. Defaults to 1,000.
        String include = "include_example"; // String | With platformPostId on YouTube: retentionCurve adds the audience retention curve.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 541 days.
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today.
        try {
            ApiResponse<InsightMetricsResponse> response = apiInstance.getInsightMetricsWithHttpInfo(accountId, metrics, platformPostId, granularity, groupBy, breakdown, timeframe, cursor, limit, include, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getInsightMetrics");
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
| **accountId** | **String**| One account id. | |
| **metrics** | **String**| Comma-separated metric names (up to 25). Defaults to the platform&#39;s default metrics. &#x60;GET /v1/metrics/catalog?entity&#x3D;insights&amp;platform&#x3D;...&#x60; lists them. | [optional] |
| **platformPostId** | **String**| One post of the account, by its platform id: answers the post&#39;s live insights instead of the account&#39;s. | [optional] |
| **granularity** | **String**| Defaults to total; groupBy&#x3D;hour answers per day. | [optional] [enum: total, day] |
| **groupBy** | **String**| demographic: audience segments (age, gender, country...). hour: Instagram followers online per day and hour, last 30 days. keyword: Google Business search keywords per month. query, page, country, device: Google Search Console, combined with commas (groupBy&#x3D;query,country). | [optional] |
| **breakdown** | **String**| With groupBy&#x3D;demographic: comma-separated segments. Defaults to the platform&#39;s default segments. | [optional] |
| **timeframe** | **String**| Instagram demographics only. Defaults to this_month. | [optional] [enum: this_week, this_month] |
| **cursor** | **String**| With groupBy&#x3D;keyword or a Search Console account: pagination.nextCursor of the previous page, sent with the same query. | [optional] |
| **limit** | **Integer**| Search Console accounts only: rows per page. Defaults to 1,000. | [optional] |
| **include** | **String**| With platformPostId on YouTube: retentionCurve adds the audience retention curve. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). Defaults to 30 days before toDate. The window is at most 541 days. | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). Defaults to today. | [optional] |

### Return type

ApiResponse<[**InsightMetricsResponse**](InsightMetricsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One row per period, or per segment with groupBy. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key, or the account is disconnected (&#x60;code: account_disconnected&#x60;, &#x60;action: reconnect&#x60;). |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## getMetricsCatalog

> MetricsCatalogResponse getMetricsCatalog(entity, platform)

List the metrics, groupings and limits of each metrics endpoint

Describes each metrics endpoint (&#x60;GET /v1/metrics/posts&#x60;, &#x60;/accounts&#x60;, &#x60;/insights&#x60;, &#x60;/inbox&#x60;, &#x60;/ads&#x60;, &#x60;/campaigns&#x60; and &#x60;/ad-accounts&#x60;): the scope it needs, the most ids per scope, the longest and default date window, the granularities, sorts, includes, groupBy values, attributions and every metric with its unit, platforms and freshness.  Read it once and cache it: it changes only when Zernio adds a metric or a grouping. Filter with &#x60;entity&#x60; and &#x60;platform&#x60; to get only what one screen needs. No analytics add-on is needed to read it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String entity = "posts"; // String | Only this entity.
        String platform = "tiktok"; // String | Only the metrics, sorts, includes and groupBy values this platform has. Every entity is still listed.
        try {
            MetricsCatalogResponse result = apiInstance.getMetricsCatalog(entity, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getMetricsCatalog");
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
| **entity** | **String**| Only this entity. | [optional] [enum: posts, accounts, inbox, insights, ads, campaigns, ad-accounts] |
| **platform** | **String**| Only the metrics, sorts, includes and groupBy values this platform has. Every entity is still listed. | [optional] [enum: tiktok, instagram, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, whatsapp, discord, slack, google, microsoft, openai] |

### Return type

[**MetricsCatalogResponse**](MetricsCatalogResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One entry per entity. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;campaign-analytics&#x60;, &#x60;ad-analytics&#x60;, &#x60;ads-listings&#x60;, &#x60;post-analytics&#x60; or &#x60;account-insights&#x60;: the team&#39;s analytics read cap for that group, on a 30-second sliding window. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level analytics endpoint.  |  * Retry-After - Seconds until card payments are tried again. <br>  * X-RateLimit-Limit - The ceiling of the limit that was reached. <br>  * X-RateLimit-Remaining - Requests remaining in the window. <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the next slot frees up. <br>  |

## getMetricsCatalogWithHttpInfo

> ApiResponse<MetricsCatalogResponse> getMetricsCatalog getMetricsCatalogWithHttpInfo(entity, platform)

List the metrics, groupings and limits of each metrics endpoint

Describes each metrics endpoint (&#x60;GET /v1/metrics/posts&#x60;, &#x60;/accounts&#x60;, &#x60;/insights&#x60;, &#x60;/inbox&#x60;, &#x60;/ads&#x60;, &#x60;/campaigns&#x60; and &#x60;/ad-accounts&#x60;): the scope it needs, the most ids per scope, the longest and default date window, the granularities, sorts, includes, groupBy values, attributions and every metric with its unit, platforms and freshness.  Read it once and cache it: it changes only when Zernio adds a metric or a grouping. Filter with &#x60;entity&#x60; and &#x60;platform&#x60; to get only what one screen needs. No analytics add-on is needed to read it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String entity = "posts"; // String | Only this entity.
        String platform = "tiktok"; // String | Only the metrics, sorts, includes and groupBy values this platform has. Every entity is still listed.
        try {
            ApiResponse<MetricsCatalogResponse> response = apiInstance.getMetricsCatalogWithHttpInfo(entity, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getMetricsCatalog");
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
| **entity** | **String**| Only this entity. | [optional] [enum: posts, accounts, inbox, insights, ads, campaigns, ad-accounts] |
| **platform** | **String**| Only the metrics, sorts, includes and groupBy values this platform has. Every entity is still listed. | [optional] [enum: tiktok, instagram, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, whatsapp, discord, slack, google, microsoft, openai] |

### Return type

ApiResponse<[**MetricsCatalogResponse**](MetricsCatalogResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One entry per entity. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;campaign-analytics&#x60;, &#x60;ad-analytics&#x60;, &#x60;ads-listings&#x60;, &#x60;post-analytics&#x60; or &#x60;account-insights&#x60;: the team&#39;s analytics read cap for that group, on a 30-second sliding window. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level analytics endpoint.  |  * Retry-After - Seconds until card payments are tried again. <br>  * X-RateLimit-Limit - The ceiling of the limit that was reached. <br>  * X-RateLimit-Remaining - Requests remaining in the window. <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the next slot frees up. <br>  |


## getPostMetrics

> PostMetricsResponse getPostMetrics(postId, platformPostId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, origin, sort, include, changedSince, limit, cursor)

Read post metrics by id, day by day, as a list, or grouped

Reads the metrics Zernio synced for published posts, Zernio posts and posts published outside Zernio alike. Send exactly one scope: &#x60;postId&#x60;, &#x60;platformPostId&#x60;, &#x60;accountId&#x60; or &#x60;profileId&#x60;, or read the change feed with &#x60;changedSince&#x60;.  - **By id** (&#x60;postId&#x60; or &#x60;platformPostId&#x60;, up to 100): one row per publication. Ids that match no post you can read come back in &#x60;meta.missingIds&#x60;. - **One post day by day**: one id with &#x60;granularity&#x3D;day&#x60;. - **A list** (&#x60;accountId&#x60; up to 25, or one &#x60;profileId&#x60; with an optional &#x60;platform&#x60;): posts published in the window, newest first, paged with &#x60;cursor&#x60;. &#x60;sort&#x60; orders it by a metric (&#x60;likes-desc&#x60;, &#x60;engagement-desc&#x60;...), up to the 1,000 best posts. &#x60;include&#x3D;total&#x60; counts the list on the first page (windows up to 92 days).  Grouped with &#x60;groupBy&#x60;:  - &#x60;post&#x60;: sums the platforms each post id was published to into one row (by id, &#x60;granularity&#x3D;total&#x60;). - &#x60;dayOfWeek,hour&#x60;: one row per UTC weekday and hour the posts were published, summing each post&#39;s latest metrics. The newer way to read &#x60;GET /v1/analytics/best-time&#x60;. - &#x60;postAge&#x60;: the share of its final engagement a post had reached at each age (0-6h to 30d+), &#x60;engagementShareOfFinal&#x60;. The newer way to read &#x60;GET /v1/analytics/content-decay&#x60;. Defaults to the last 60 days. - &#x60;format&#x60;: one row per format (image, video, carousel, text). The newer way to read &#x60;GET /v1/analytics/format-breakdown&#x60;.  &#x60;dayOfWeek,hour&#x60;, &#x60;postAge&#x60; and &#x60;format&#x60; take a list scope (&#x60;accountId&#x60; or &#x60;profileId&#x60;), &#x60;granularity&#x3D;total&#x60;, windows up to 92 days, and answer in one page.  Includes on rows read by id or in a list (&#x60;include&#x60;, comma-separated):  - &#x60;post&#x60;: content, media and publishing details. - &#x60;samples&#x60;: one reading per analytics sync, oldest first, the newest 500 per post, narrowed by &#x60;fromDate&#x60; and &#x60;toDate&#x60; on the sync time. Posts read by &#x60;postId&#x60; or &#x60;platformPostId&#x60; only, up to 10, with &#x60;granularity&#x3D;total&#x60; and no &#x60;groupBy&#x60;. The newer way to read &#x60;GET /v1/analytics/samples&#x60;. - &#x60;authenticity&#x60;: the stored authenticity score with its confidence, reasons, model version, sample count and when it was computed; null until the post has been scored. The &#x60;authenticityScore&#x60; metric carries the score alone (0 to 100). - &#x60;impressionSources&#x60;, &#x60;audienceTypes&#x60;, &#x60;audienceCountries&#x60;, &#x60;retentionCurve&#x60;: breakdowns on the platforms that report them.  Change feed with &#x60;changedSince&#x60;:  - &#x60;changedSince&#x3D;now&#x60; answers no rows and a starting cursor; send each &#x60;pagination.nextCursor&#x60; back as &#x60;changedSince&#x60; to get one &#x60;PostMetricChange&#x60; row per post whose metrics changed since then, oldest change first. - It reads every account the key can read, narrowed with one &#x60;profileId&#x60; and &#x60;platform&#x60;. It takes &#x60;metrics&#x60; from the feed&#39;s list and the breakdown includes, nothing else. - Changes are kept 7 days and a cursor older than 6 days is refused. The feed and its cursors are the same as &#x60;GET /v1/analytics/delta&#x60;, of which it is the newer way to read.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; a list reads the last 90 days; the window is at most 366 days. &#x60;GET /v1/metrics/catalog?entity&#x3D;posts&#x60; lists every metric, sort, include and groupBy, with the platforms that report each. A metric is &#x60;null&#x60; when the platform does not report it or the post has no snapshot yet.  Each team has an analytics compute budget of 24 seconds per 30-second window across these reads, on top of the per-group cap: a request that would pass it is refused with 429 &#x60;details.scope: team_budget&#x60; before it runs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String postId = "postId_example"; // String | Comma-separated post ids (Zernio or external), up to 100.
        String platformPostId = "platformPostId_example"; // String | Comma-separated ids the platform gave the posts (a TikTok video id, a tweet id), up to 100.
        String accountId = "accountId_example"; // String | Comma-separated account ids, up to 25.
        String profileId = "profileId_example"; // String | One profile id.
        String metrics = "metrics_example"; // String | Comma-separated metric names from the catalog. Defaults to every metric.
        String groupBy = "groupBy_example"; // String | Comma-separated groupings from the catalog, at most 2.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC).
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC).
        String platform = "tiktok"; // String | Only with profileId.
        String granularity = "total"; // String | day reads one post.
        String origin = "all"; // String | Lists only. Defaults to all.
        String sort = "sort_example"; // String | A sort from the catalog, such as published-desc or likes-desc.
        String include = "include_example"; // String | Comma-separated includes from the catalog.
        String changedSince = "changedSince_example"; // String | now (no rows, the starting cursor) or the previous pagination.nextCursor: one row per post whose metrics changed since, oldest first, across every account the key reads. Narrow with profileId and platform. Changes are kept 7 days; cursors older than 6 days are refused.
        Integer limit = 50; // Integer | Rows per page, 50 by default, 100 at most.
        String cursor = "cursor_example"; // String | pagination.nextCursor of the previous page, sent with the same query.
        try {
            PostMetricsResponse result = apiInstance.getPostMetrics(postId, platformPostId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, origin, sort, include, changedSince, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getPostMetrics");
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
| **postId** | **String**| Comma-separated post ids (Zernio or external), up to 100. | [optional] |
| **platformPostId** | **String**| Comma-separated ids the platform gave the posts (a TikTok video id, a tweet id), up to 100. | [optional] |
| **accountId** | **String**| Comma-separated account ids, up to 25. | [optional] |
| **profileId** | **String**| One profile id. | [optional] |
| **metrics** | **String**| Comma-separated metric names from the catalog. Defaults to every metric. | [optional] |
| **groupBy** | **String**| Comma-separated groupings from the catalog, at most 2. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **platform** | **String**| Only with profileId. | [optional] [enum: tiktok, instagram, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, whatsapp, discord, slack] |
| **granularity** | **String**| day reads one post. | [optional] [default to total] [enum: total, day] |
| **origin** | **String**| Lists only. Defaults to all. | [optional] [enum: all, zernio, external] |
| **sort** | **String**| A sort from the catalog, such as published-desc or likes-desc. | [optional] |
| **include** | **String**| Comma-separated includes from the catalog. | [optional] |
| **changedSince** | **String**| now (no rows, the starting cursor) or the previous pagination.nextCursor: one row per post whose metrics changed since, oldest first, across every account the key reads. Narrow with profileId and platform. Changes are kept 7 days; cursors older than 6 days are refused. | [optional] |
| **limit** | **Integer**| Rows per page, 50 by default, 100 at most. | [optional] [default to 50] |
| **cursor** | **String**| pagination.nextCursor of the previous page, sent with the same query. | [optional] |

### Return type

[**PostMetricsResponse**](PostMetricsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rows of the shape the query asks for: &#x60;PostMetricRow&#x60; by id and in lists, &#x60;PostMetricGroup&#x60; with groupBy&#x3D;post, &#x60;PostMetricSlot&#x60; with groupBy&#x3D;dayOfWeek,hour, &#x60;PostMetricAge&#x60; with groupBy&#x3D;postAge, &#x60;PostMetricFormat&#x60; with groupBy&#x3D;format, &#x60;PostMetricChange&#x60; with changedSince. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## getPostMetricsWithHttpInfo

> ApiResponse<PostMetricsResponse> getPostMetrics getPostMetricsWithHttpInfo(postId, platformPostId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, origin, sort, include, changedSince, limit, cursor)

Read post metrics by id, day by day, as a list, or grouped

Reads the metrics Zernio synced for published posts, Zernio posts and posts published outside Zernio alike. Send exactly one scope: &#x60;postId&#x60;, &#x60;platformPostId&#x60;, &#x60;accountId&#x60; or &#x60;profileId&#x60;, or read the change feed with &#x60;changedSince&#x60;.  - **By id** (&#x60;postId&#x60; or &#x60;platformPostId&#x60;, up to 100): one row per publication. Ids that match no post you can read come back in &#x60;meta.missingIds&#x60;. - **One post day by day**: one id with &#x60;granularity&#x3D;day&#x60;. - **A list** (&#x60;accountId&#x60; up to 25, or one &#x60;profileId&#x60; with an optional &#x60;platform&#x60;): posts published in the window, newest first, paged with &#x60;cursor&#x60;. &#x60;sort&#x60; orders it by a metric (&#x60;likes-desc&#x60;, &#x60;engagement-desc&#x60;...), up to the 1,000 best posts. &#x60;include&#x3D;total&#x60; counts the list on the first page (windows up to 92 days).  Grouped with &#x60;groupBy&#x60;:  - &#x60;post&#x60;: sums the platforms each post id was published to into one row (by id, &#x60;granularity&#x3D;total&#x60;). - &#x60;dayOfWeek,hour&#x60;: one row per UTC weekday and hour the posts were published, summing each post&#39;s latest metrics. The newer way to read &#x60;GET /v1/analytics/best-time&#x60;. - &#x60;postAge&#x60;: the share of its final engagement a post had reached at each age (0-6h to 30d+), &#x60;engagementShareOfFinal&#x60;. The newer way to read &#x60;GET /v1/analytics/content-decay&#x60;. Defaults to the last 60 days. - &#x60;format&#x60;: one row per format (image, video, carousel, text). The newer way to read &#x60;GET /v1/analytics/format-breakdown&#x60;.  &#x60;dayOfWeek,hour&#x60;, &#x60;postAge&#x60; and &#x60;format&#x60; take a list scope (&#x60;accountId&#x60; or &#x60;profileId&#x60;), &#x60;granularity&#x3D;total&#x60;, windows up to 92 days, and answer in one page.  Includes on rows read by id or in a list (&#x60;include&#x60;, comma-separated):  - &#x60;post&#x60;: content, media and publishing details. - &#x60;samples&#x60;: one reading per analytics sync, oldest first, the newest 500 per post, narrowed by &#x60;fromDate&#x60; and &#x60;toDate&#x60; on the sync time. Posts read by &#x60;postId&#x60; or &#x60;platformPostId&#x60; only, up to 10, with &#x60;granularity&#x3D;total&#x60; and no &#x60;groupBy&#x60;. The newer way to read &#x60;GET /v1/analytics/samples&#x60;. - &#x60;authenticity&#x60;: the stored authenticity score with its confidence, reasons, model version, sample count and when it was computed; null until the post has been scored. The &#x60;authenticityScore&#x60; metric carries the score alone (0 to 100). - &#x60;impressionSources&#x60;, &#x60;audienceTypes&#x60;, &#x60;audienceCountries&#x60;, &#x60;retentionCurve&#x60;: breakdowns on the platforms that report them.  Change feed with &#x60;changedSince&#x60;:  - &#x60;changedSince&#x3D;now&#x60; answers no rows and a starting cursor; send each &#x60;pagination.nextCursor&#x60; back as &#x60;changedSince&#x60; to get one &#x60;PostMetricChange&#x60; row per post whose metrics changed since then, oldest change first. - It reads every account the key can read, narrowed with one &#x60;profileId&#x60; and &#x60;platform&#x60;. It takes &#x60;metrics&#x60; from the feed&#39;s list and the breakdown includes, nothing else. - Changes are kept 7 days and a cursor older than 6 days is refused. The feed and its cursors are the same as &#x60;GET /v1/analytics/delta&#x60;, of which it is the newer way to read.  Without &#x60;fromDate&#x60; and &#x60;toDate&#x60; a list reads the last 90 days; the window is at most 366 days. &#x60;GET /v1/metrics/catalog?entity&#x3D;posts&#x60; lists every metric, sort, include and groupBy, with the platforms that report each. A metric is &#x60;null&#x60; when the platform does not report it or the post has no snapshot yet.  Each team has an analytics compute budget of 24 seconds per 30-second window across these reads, on top of the per-group cap: a request that would pass it is refused with 429 &#x60;details.scope: team_budget&#x60; before it runs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        String postId = "postId_example"; // String | Comma-separated post ids (Zernio or external), up to 100.
        String platformPostId = "platformPostId_example"; // String | Comma-separated ids the platform gave the posts (a TikTok video id, a tweet id), up to 100.
        String accountId = "accountId_example"; // String | Comma-separated account ids, up to 25.
        String profileId = "profileId_example"; // String | One profile id.
        String metrics = "metrics_example"; // String | Comma-separated metric names from the catalog. Defaults to every metric.
        String groupBy = "groupBy_example"; // String | Comma-separated groupings from the catalog, at most 2.
        LocalDate fromDate = LocalDate.now(); // LocalDate | First day, inclusive (YYYY-MM-DD, UTC).
        LocalDate toDate = LocalDate.now(); // LocalDate | Last day, inclusive (YYYY-MM-DD, UTC).
        String platform = "tiktok"; // String | Only with profileId.
        String granularity = "total"; // String | day reads one post.
        String origin = "all"; // String | Lists only. Defaults to all.
        String sort = "sort_example"; // String | A sort from the catalog, such as published-desc or likes-desc.
        String include = "include_example"; // String | Comma-separated includes from the catalog.
        String changedSince = "changedSince_example"; // String | now (no rows, the starting cursor) or the previous pagination.nextCursor: one row per post whose metrics changed since, oldest first, across every account the key reads. Narrow with profileId and platform. Changes are kept 7 days; cursors older than 6 days are refused.
        Integer limit = 50; // Integer | Rows per page, 50 by default, 100 at most.
        String cursor = "cursor_example"; // String | pagination.nextCursor of the previous page, sent with the same query.
        try {
            ApiResponse<PostMetricsResponse> response = apiInstance.getPostMetricsWithHttpInfo(postId, platformPostId, accountId, profileId, metrics, groupBy, fromDate, toDate, platform, granularity, origin, sort, include, changedSince, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#getPostMetrics");
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
| **postId** | **String**| Comma-separated post ids (Zernio or external), up to 100. | [optional] |
| **platformPostId** | **String**| Comma-separated ids the platform gave the posts (a TikTok video id, a tweet id), up to 100. | [optional] |
| **accountId** | **String**| Comma-separated account ids, up to 25. | [optional] |
| **profileId** | **String**| One profile id. | [optional] |
| **metrics** | **String**| Comma-separated metric names from the catalog. Defaults to every metric. | [optional] |
| **groupBy** | **String**| Comma-separated groupings from the catalog, at most 2. | [optional] |
| **fromDate** | **LocalDate**| First day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **toDate** | **LocalDate**| Last day, inclusive (YYYY-MM-DD, UTC). | [optional] |
| **platform** | **String**| Only with profileId. | [optional] [enum: tiktok, instagram, facebook, youtube, linkedin, twitter, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, whatsapp, discord, slack] |
| **granularity** | **String**| day reads one post. | [optional] [default to total] [enum: total, day] |
| **origin** | **String**| Lists only. Defaults to all. | [optional] [enum: all, zernio, external] |
| **sort** | **String**| A sort from the catalog, such as published-desc or likes-desc. | [optional] |
| **include** | **String**| Comma-separated includes from the catalog. | [optional] |
| **changedSince** | **String**| now (no rows, the starting cursor) or the previous pagination.nextCursor: one row per post whose metrics changed since, oldest first, across every account the key reads. Narrow with profileId and platform. Changes are kept 7 days; cursors older than 6 days are refused. | [optional] |
| **limit** | **Integer**| Rows per page, 50 by default, 100 at most. | [optional] [default to 50] |
| **cursor** | **String**| pagination.nextCursor of the previous page, sent with the same query. | [optional] |

### Return type

ApiResponse<[**PostMetricsResponse**](PostMetricsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rows of the shape the query asks for: &#x60;PostMetricRow&#x60; by id and in lists, &#x60;PostMetricGroup&#x60; with groupBy&#x3D;post, &#x60;PostMetricSlot&#x60; with groupBy&#x3D;dayOfWeek,hour, &#x60;PostMetricAge&#x60; with groupBy&#x3D;postAge, &#x60;PostMetricFormat&#x60; with groupBy&#x3D;format, &#x60;PostMetricChange&#x60; with changedSince. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## queryGoogleAds

> PlatformQueryPage queryGoogleAds(googleAdsPlatformQueryBody)

Run a Google Ads Query Language search on one customer

Runs a GAQL &#x60;SELECT&#x60; on one Google Ads customer, read only. Without &#x60;adAccountId&#x60; it reads the connection&#39;s own customer.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        GoogleAdsPlatformQueryBody googleAdsPlatformQueryBody = new GoogleAdsPlatformQueryBody(); // GoogleAdsPlatformQueryBody | 
        try {
            PlatformQueryPage result = apiInstance.queryGoogleAds(googleAdsPlatformQueryBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryGoogleAds");
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
| **googleAdsPlatformQueryBody** | [**GoogleAdsPlatformQueryBody**](GoogleAdsPlatformQueryBody.md)|  | |

### Return type

[**PlatformQueryPage**](PlatformQueryPage.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## queryGoogleAdsWithHttpInfo

> ApiResponse<PlatformQueryPage> queryGoogleAds queryGoogleAdsWithHttpInfo(googleAdsPlatformQueryBody)

Run a Google Ads Query Language search on one customer

Runs a GAQL &#x60;SELECT&#x60; on one Google Ads customer, read only. Without &#x60;adAccountId&#x60; it reads the connection&#39;s own customer.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        GoogleAdsPlatformQueryBody googleAdsPlatformQueryBody = new GoogleAdsPlatformQueryBody(); // GoogleAdsPlatformQueryBody | 
        try {
            ApiResponse<PlatformQueryPage> response = apiInstance.queryGoogleAdsWithHttpInfo(googleAdsPlatformQueryBody);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryGoogleAds");
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
| **googleAdsPlatformQueryBody** | [**GoogleAdsPlatformQueryBody**](GoogleAdsPlatformQueryBody.md)|  | |

### Return type

ApiResponse<[**PlatformQueryPage**](PlatformQueryPage.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## queryGoogleAnalytics

> PlatformQueryPage queryGoogleAnalytics(googleAnalyticsPlatformQueryBody)

Run a GA4 standard or realtime report on one property

Runs a GA4 &#x60;standard&#x60; report over up to 4 date ranges, paged, or a &#x60;realtime&#x60; report on the last 30 minutes. Needs the Analytics add-on.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        GoogleAnalyticsPlatformQueryBody googleAnalyticsPlatformQueryBody = new GoogleAnalyticsPlatformQueryBody(); // GoogleAnalyticsPlatformQueryBody | 
        try {
            PlatformQueryPage result = apiInstance.queryGoogleAnalytics(googleAnalyticsPlatformQueryBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryGoogleAnalytics");
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
| **googleAnalyticsPlatformQueryBody** | [**GoogleAnalyticsPlatformQueryBody**](GoogleAnalyticsPlatformQueryBody.md)|  | |

### Return type

[**PlatformQueryPage**](PlatformQueryPage.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## queryGoogleAnalyticsWithHttpInfo

> ApiResponse<PlatformQueryPage> queryGoogleAnalytics queryGoogleAnalyticsWithHttpInfo(googleAnalyticsPlatformQueryBody)

Run a GA4 standard or realtime report on one property

Runs a GA4 &#x60;standard&#x60; report over up to 4 date ranges, paged, or a &#x60;realtime&#x60; report on the last 30 minutes. Needs the Analytics add-on.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        GoogleAnalyticsPlatformQueryBody googleAnalyticsPlatformQueryBody = new GoogleAnalyticsPlatformQueryBody(); // GoogleAnalyticsPlatformQueryBody | 
        try {
            ApiResponse<PlatformQueryPage> response = apiInstance.queryGoogleAnalyticsWithHttpInfo(googleAnalyticsPlatformQueryBody);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryGoogleAnalytics");
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
| **googleAnalyticsPlatformQueryBody** | [**GoogleAnalyticsPlatformQueryBody**](GoogleAnalyticsPlatformQueryBody.md)|  | |

### Return type

ApiResponse<[**PlatformQueryPage**](PlatformQueryPage.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## queryMetaAds

> PlatformQueryPage queryMetaAds(metaAdsPlatformQueryBody)

Run a Meta Marketing API insights query on one ad account

Reads Meta&#39;s insights for one ad account (&#x60;act_&lt;n&gt;&#x60;). Read its campaigns, ad sets or ads with &#x60;level&#x60; and &#x60;filtering&#x60; on the same ad account.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        MetaAdsPlatformQueryBody metaAdsPlatformQueryBody = new MetaAdsPlatformQueryBody(); // MetaAdsPlatformQueryBody | 
        try {
            PlatformQueryPage result = apiInstance.queryMetaAds(metaAdsPlatformQueryBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryMetaAds");
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
| **metaAdsPlatformQueryBody** | [**MetaAdsPlatformQueryBody**](MetaAdsPlatformQueryBody.md)|  | |

### Return type

[**PlatformQueryPage**](PlatformQueryPage.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## queryMetaAdsWithHttpInfo

> ApiResponse<PlatformQueryPage> queryMetaAds queryMetaAdsWithHttpInfo(metaAdsPlatformQueryBody)

Run a Meta Marketing API insights query on one ad account

Reads Meta&#39;s insights for one ad account (&#x60;act_&lt;n&gt;&#x60;). Read its campaigns, ad sets or ads with &#x60;level&#x60; and &#x60;filtering&#x60; on the same ad account.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        MetaAdsPlatformQueryBody metaAdsPlatformQueryBody = new MetaAdsPlatformQueryBody(); // MetaAdsPlatformQueryBody | 
        try {
            ApiResponse<PlatformQueryPage> response = apiInstance.queryMetaAdsWithHttpInfo(metaAdsPlatformQueryBody);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryMetaAds");
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
| **metaAdsPlatformQueryBody** | [**MetaAdsPlatformQueryBody**](MetaAdsPlatformQueryBody.md)|  | |

### Return type

ApiResponse<[**PlatformQueryPage**](PlatformQueryPage.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## queryTikTokAds

> PlatformQueryPage queryTikTokAds(tikTokAdsPlatformQueryBody)

Run a TikTok Marketing API report on one advertiser

Runs a synchronous TikTok report (&#x60;BASIC&#x60; or &#x60;AUDIENCE&#x60;) for one advertiser at the data level asked.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        TikTokAdsPlatformQueryBody tikTokAdsPlatformQueryBody = new TikTokAdsPlatformQueryBody(); // TikTokAdsPlatformQueryBody | 
        try {
            PlatformQueryPage result = apiInstance.queryTikTokAds(tikTokAdsPlatformQueryBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryTikTokAds");
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
| **tikTokAdsPlatformQueryBody** | [**TikTokAdsPlatformQueryBody**](TikTokAdsPlatformQueryBody.md)|  | |

### Return type

[**PlatformQueryPage**](PlatformQueryPage.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## queryTikTokAdsWithHttpInfo

> ApiResponse<PlatformQueryPage> queryTikTokAds queryTikTokAdsWithHttpInfo(tikTokAdsPlatformQueryBody)

Run a TikTok Marketing API report on one advertiser

Runs a synchronous TikTok report (&#x60;BASIC&#x60; or &#x60;AUDIENCE&#x60;) for one advertiser at the data level asked.  Runs a native query on the platform with the account&#39;s own token and answers the platform&#39;s rows unchanged, with its own field names, plus its headers, counts and quota in &#x60;meta&#x60;. Use it for what &#x60;/v1/metrics/_*&#x60; does not store; the stored metrics stay cheaper and faster.  - Up to 120 reads per hour per platform target (the Zernio account plus the ad account or property); past it, 429 with &#x60;details.scope&#x60; &#x60;platform_query_target&#x60;.  - Up to 10 queries in flight per team.  - A query must answer within 25 seconds.  - An account of another source answers 400 on &#x60;accountId&#x60; with the route it belongs to.  - The next page goes in &#x60;cursor&#x60;, from &#x60;pagination.nextCursor&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MetricsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MetricsApi apiInstance = new MetricsApi(defaultClient);
        TikTokAdsPlatformQueryBody tikTokAdsPlatformQueryBody = new TikTokAdsPlatformQueryBody(); // TikTokAdsPlatformQueryBody | 
        try {
            ApiResponse<PlatformQueryPage> response = apiInstance.queryTikTokAdsWithHttpInfo(tikTokAdsPlatformQueryBody);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MetricsApi#queryTikTokAds");
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
| **tikTokAdsPlatformQueryBody** | [**TikTokAdsPlatformQueryBody**](TikTokAdsPlatformQueryBody.md)|  | |

### Return type

ApiResponse<[**PlatformQueryPage**](PlatformQueryPage.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The platform&#39;s rows for the query. |  -  |
| **400** | The query is invalid: an unknown or repeated parameter, a missing or second scope, a metric, groupBy, include or sort the entity does not have, or a window past its limit. &#x60;param&#x60; names the field. &#x60;GET /v1/metrics/catalog&#x60; lists what each entity accepts. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;ads_addon_required&#x60;: the account has no ads access (included on usage-based plans). &#x60;insufficient_permissions&#x60;: the API key can read no profile. Also returned for a restricted key without the &#x60;ads&#x60; resource group. |  -  |
| **429** | A limit on your request rate was reached. &#x60;details.scope&#x60; says which one:  - absent: your plan&#39;s API limit. - &#x60;post-analytics&#x60;, &#x60;account-insights&#x60;, &#x60;ad-analytics&#x60; or &#x60;campaign-analytics&#x60;: the team&#39;s cap of 300 reads per 30 seconds for that group. - &#x60;account_route&#x60;: 120 reads per hour of one account on one account-level endpoint. - &#x60;team_budget&#x60;: the team spent its analytics compute budget of 24 seconds per 30-second window. &#x60;Retry-After&#x60; counts to the end of the window. - &#x60;in_flight&#x60;: too many of the team&#39;s analytics reads are running at once.  &#x60;team_budget&#x60; and &#x60;in_flight&#x60; apply to posts, accounts, ads, campaigns and ad accounts reads. |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

