# ChangelogApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listChangelog**](ChangelogApi.md#listChangelog) | **GET** /v1/changelog | List API changelog entries |
| [**listChangelogWithHttpInfo**](ChangelogApi.md#listChangelogWithHttpInfo) | **GET** /v1/changelog | List API changelog entries |



## listChangelog

> ListChangelog200Response listChangelog(type, impact, platform, before, limit)

List API changelog entries

The API changelog, newest first. No API key needed; one address may make 120 requests a minute. Each entry is what the &#x60;api.changelog.published&#x60; webhook delivered: the announcement in &#x60;message&#x60;, its &#x60;impact&#x60; on existing integrations, and in &#x60;changes&#x60; the deterministic diff of the OpenAPI spec (operations and schemas added, removed and modified) for automation to act on. Page with &#x60;before&#x60; set to the previous page&#39;s &#x60;nextCursor&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.ChangelogApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        ChangelogApi apiInstance = new ChangelogApi(defaultClient);
        String type = "new_feature"; // String | Only entries of this type.
        String impact = "none"; // String | Only entries with this impact. `action_required` lists the changes an integration may need to act on.
        String platform = "whatsapp"; // String | Only entries tagged with this platform or area slug (see `platforms` on the entry). One slug per request.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Only entries published strictly before this instant. Pass the previous page's `nextCursor`.
        Integer limit = 20; // Integer | 
        try {
            ListChangelog200Response result = apiInstance.listChangelog(type, impact, platform, before, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ChangelogApi#listChangelog");
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
| **type** | **String**| Only entries of this type. | [optional] [enum: new_feature, breaking_change, improvement, deprecation, minor] |
| **impact** | **String**| Only entries with this impact. &#x60;action_required&#x60; lists the changes an integration may need to act on. | [optional] [enum: none, additive, action_required] |
| **platform** | **String**| Only entries tagged with this platform or area slug (see &#x60;platforms&#x60; on the entry). One slug per request. | [optional] |
| **before** | **OffsetDateTime**| Only entries published strictly before this instant. Pass the previous page&#39;s &#x60;nextCursor&#x60;. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**ListChangelog200Response**](ListChangelog200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Changelog entries |  -  |
| **400** | Invalid request |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  YouTube Analytics: reads (channel-insights, demographics, daily-views, video-retention) run on the \&quot;Queries per day\&quot; quota of the Google Cloud project the YouTube account is connected through, shared with other Zernio customers, so a 429 there is not your own volume. It resets at midnight Pacific Time. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  Pinterest ads: Pinterest rate-limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when it sends one, otherwise 60 seconds.  TikTok ads: TikTok limits requests per app and per endpoint (per second, per minute and per day) and answers overage with code 40100 or with code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (for example one ad at a time per advertiser) instead of retrying at once. The Smart+ review read (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has a stricter quota of its own on TikTok: after an overage Zernio answers 429 for that advertiser and connection, without calling TikTok, for about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, each with up to 10% of random jitter. A successful call holds nothing back, and the next overage after it pauses about 60 seconds again; &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## listChangelogWithHttpInfo

> ApiResponse<ListChangelog200Response> listChangelog listChangelogWithHttpInfo(type, impact, platform, before, limit)

List API changelog entries

The API changelog, newest first. No API key needed; one address may make 120 requests a minute. Each entry is what the &#x60;api.changelog.published&#x60; webhook delivered: the announcement in &#x60;message&#x60;, its &#x60;impact&#x60; on existing integrations, and in &#x60;changes&#x60; the deterministic diff of the OpenAPI spec (operations and schemas added, removed and modified) for automation to act on. Page with &#x60;before&#x60; set to the previous page&#39;s &#x60;nextCursor&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.ChangelogApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        ChangelogApi apiInstance = new ChangelogApi(defaultClient);
        String type = "new_feature"; // String | Only entries of this type.
        String impact = "none"; // String | Only entries with this impact. `action_required` lists the changes an integration may need to act on.
        String platform = "whatsapp"; // String | Only entries tagged with this platform or area slug (see `platforms` on the entry). One slug per request.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Only entries published strictly before this instant. Pass the previous page's `nextCursor`.
        Integer limit = 20; // Integer | 
        try {
            ApiResponse<ListChangelog200Response> response = apiInstance.listChangelogWithHttpInfo(type, impact, platform, before, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ChangelogApi#listChangelog");
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
| **type** | **String**| Only entries of this type. | [optional] [enum: new_feature, breaking_change, improvement, deprecation, minor] |
| **impact** | **String**| Only entries with this impact. &#x60;action_required&#x60; lists the changes an integration may need to act on. | [optional] [enum: none, additive, action_required] |
| **platform** | **String**| Only entries tagged with this platform or area slug (see &#x60;platforms&#x60; on the entry). One slug per request. | [optional] |
| **before** | **OffsetDateTime**| Only entries published strictly before this instant. Pass the previous page&#39;s &#x60;nextCursor&#x60;. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

ApiResponse<[**ListChangelog200Response**](ListChangelog200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Changelog entries |  -  |
| **400** | Invalid request |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  YouTube Analytics: reads (channel-insights, demographics, daily-views, video-retention) run on the \&quot;Queries per day\&quot; quota of the Google Cloud project the YouTube account is connected through, shared with other Zernio customers, so a 429 there is not your own volume. It resets at midnight Pacific Time. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  Pinterest ads: Pinterest rate-limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when it sends one, otherwise 60 seconds.  TikTok ads: TikTok limits requests per app and per endpoint (per second, per minute and per day) and answers overage with code 40100 or with code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (for example one ad at a time per advertiser) instead of retrying at once. The Smart+ review read (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has a stricter quota of its own on TikTok: after an overage Zernio answers 429 for that advertiser and connection, without calling TikTok, for about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, each with up to 10% of random jitter. A successful call holds nothing back, and the next overage after it pauses about 60 seconds again; &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

