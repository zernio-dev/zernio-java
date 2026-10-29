# LinkedInMentionsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLinkedInMentions**](LinkedInMentionsApi.md#getLinkedInMentions) | **GET** /v1/accounts/{accountId}/linkedin-mentions | Resolve LinkedIn mention |
| [**getLinkedInMentionsWithHttpInfo**](LinkedInMentionsApi.md#getLinkedInMentionsWithHttpInfo) | **GET** /v1/accounts/{accountId}/linkedin-mentions | Resolve LinkedIn mention |



## getLinkedInMentions

> GetLinkedInMentions200Response getLinkedInMentions(accountId, url, displayName)

Resolve LinkedIn mention

Converts a LinkedIn profile or company URL to a URN for @mentions in posts.  You usually do not need this endpoint. Put the profile or company URL inside &#x60;@[...]&#x60; in the post &#x60;content&#x60; (for example &#x60;@[https://www.linkedin.com/in/vincentjong]&#x60;) and the post resolves it for you, using LinkedIn&#39;s own name.  Use this endpoint to preview what a URL resolves to, or to get ready-made &#x60;@[Name](urn)&#x60; markup, which still works in &#x60;content&#x60; and is published exactly as written.  ### Example  1. Resolve: GET /v1/accounts/{id}/linkedin-mentions?url&#x3D;linkedin.com/in/vincentjong 2. Returns: mentionFormat: \&quot;@[Vincent Jong](urn:li:person:xxx)\&quot; 3. Use in post content: \&quot;Great talk with @[Vincent Jong](urn:li:person:xxx) today!\&quot;  Important: the mentions array field in POST /v1/posts is stored for reference only and does NOT trigger @mentions on LinkedIn. Write the mention in the content text.  ### Requirements  - Resolving a profile URL to a person mention requires the LinkedIn account to be admin of at least one organization: both endpoints that resolve a profile URL to a member URN take an organization you administer. - A resolved person mention publishes from any account. Organization mentions (e.g. @Microsoft) have no such requirement. - Person mentions DO work when published from personal profiles (the URN only needs to be valid). The limitation is only in the resolution step (URL to URN), not in publishing.  ### Why a profile can 404  The two resolution endpoints are not scoped alike:  - peopleTypeahead?q&#x3D;organizationFollowers only returns that organization&#39;s followers. - vanityUrl?q&#x3D;vanityUrlAsOrganization does not, and its resolvable set is opaque.  A 404 here does not mean the person is unknown to you or unknown to LinkedIn: a live public profile can 404 with no reason given.  ### Display name  displayName is deprecated and ignored in practice: the endpoint reads the person&#39;s real name from LinkedIn itself. LinkedIn renders a person mention as a link only when the mention text is the person&#39;s first name, last name or full name (case-sensitive). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LinkedInMentionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LinkedInMentionsApi apiInstance = new LinkedInMentionsApi(defaultClient);
        String accountId = "accountId_example"; // String | The LinkedIn account ID
        String url = "miquelpalet"; // String | LinkedIn profile URL, company URL, or vanity name.
        String displayName = "Miquel Palet"; // String | Deprecated: omit it. When omitted, the real name is read from LinkedIn. Ignored for org mentions, which always use the organization's LinkedIn name.  When sent for a person, it overrides the mention text, and LinkedIn renders the mention only if it is exactly the person's first name, last name or full name (case-sensitive). 
        try {
            GetLinkedInMentions200Response result = apiInstance.getLinkedInMentions(accountId, url, displayName);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LinkedInMentionsApi#getLinkedInMentions");
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
| **accountId** | **String**| The LinkedIn account ID | |
| **url** | **String**| LinkedIn profile URL, company URL, or vanity name. | |
| **displayName** | **String**| Deprecated: omit it. When omitted, the real name is read from LinkedIn. Ignored for org mentions, which always use the organization&#39;s LinkedIn name.  When sent for a person, it overrides the mention text, and LinkedIn renders the mention only if it is exactly the person&#39;s first name, last name or full name (case-sensitive).  | [optional] |

### Return type

[**GetLinkedInMentions200Response**](GetLinkedInMentions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | URN resolved successfully |  -  |
| **400** | Invalid request or no organization found (for person mentions) |  -  |
| **401** | Missing or invalid API key (&#x60;missing_credentials&#x60; or &#x60;invalid_credentials&#x60;), or LinkedIn revoked or expired the account&#39;s token (&#x60;reconnect_required&#x60;, reconnect the account). |  -  |
| **403** | The account holds no organization role that can resolve person mentions |  -  |
| **404** | Account, person or organization not found |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## getLinkedInMentionsWithHttpInfo

> ApiResponse<GetLinkedInMentions200Response> getLinkedInMentions getLinkedInMentionsWithHttpInfo(accountId, url, displayName)

Resolve LinkedIn mention

Converts a LinkedIn profile or company URL to a URN for @mentions in posts.  You usually do not need this endpoint. Put the profile or company URL inside &#x60;@[...]&#x60; in the post &#x60;content&#x60; (for example &#x60;@[https://www.linkedin.com/in/vincentjong]&#x60;) and the post resolves it for you, using LinkedIn&#39;s own name.  Use this endpoint to preview what a URL resolves to, or to get ready-made &#x60;@[Name](urn)&#x60; markup, which still works in &#x60;content&#x60; and is published exactly as written.  ### Example  1. Resolve: GET /v1/accounts/{id}/linkedin-mentions?url&#x3D;linkedin.com/in/vincentjong 2. Returns: mentionFormat: \&quot;@[Vincent Jong](urn:li:person:xxx)\&quot; 3. Use in post content: \&quot;Great talk with @[Vincent Jong](urn:li:person:xxx) today!\&quot;  Important: the mentions array field in POST /v1/posts is stored for reference only and does NOT trigger @mentions on LinkedIn. Write the mention in the content text.  ### Requirements  - Resolving a profile URL to a person mention requires the LinkedIn account to be admin of at least one organization: both endpoints that resolve a profile URL to a member URN take an organization you administer. - A resolved person mention publishes from any account. Organization mentions (e.g. @Microsoft) have no such requirement. - Person mentions DO work when published from personal profiles (the URN only needs to be valid). The limitation is only in the resolution step (URL to URN), not in publishing.  ### Why a profile can 404  The two resolution endpoints are not scoped alike:  - peopleTypeahead?q&#x3D;organizationFollowers only returns that organization&#39;s followers. - vanityUrl?q&#x3D;vanityUrlAsOrganization does not, and its resolvable set is opaque.  A 404 here does not mean the person is unknown to you or unknown to LinkedIn: a live public profile can 404 with no reason given.  ### Display name  displayName is deprecated and ignored in practice: the endpoint reads the person&#39;s real name from LinkedIn itself. LinkedIn renders a person mention as a link only when the mention text is the person&#39;s first name, last name or full name (case-sensitive). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LinkedInMentionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LinkedInMentionsApi apiInstance = new LinkedInMentionsApi(defaultClient);
        String accountId = "accountId_example"; // String | The LinkedIn account ID
        String url = "miquelpalet"; // String | LinkedIn profile URL, company URL, or vanity name.
        String displayName = "Miquel Palet"; // String | Deprecated: omit it. When omitted, the real name is read from LinkedIn. Ignored for org mentions, which always use the organization's LinkedIn name.  When sent for a person, it overrides the mention text, and LinkedIn renders the mention only if it is exactly the person's first name, last name or full name (case-sensitive). 
        try {
            ApiResponse<GetLinkedInMentions200Response> response = apiInstance.getLinkedInMentionsWithHttpInfo(accountId, url, displayName);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LinkedInMentionsApi#getLinkedInMentions");
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
| **accountId** | **String**| The LinkedIn account ID | |
| **url** | **String**| LinkedIn profile URL, company URL, or vanity name. | |
| **displayName** | **String**| Deprecated: omit it. When omitted, the real name is read from LinkedIn. Ignored for org mentions, which always use the organization&#39;s LinkedIn name.  When sent for a person, it overrides the mention text, and LinkedIn renders the mention only if it is exactly the person&#39;s first name, last name or full name (case-sensitive).  | [optional] |

### Return type

ApiResponse<[**GetLinkedInMentions200Response**](GetLinkedInMentions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | URN resolved successfully |  -  |
| **400** | Invalid request or no organization found (for person mentions) |  -  |
| **401** | Missing or invalid API key (&#x60;missing_credentials&#x60; or &#x60;invalid_credentials&#x60;), or LinkedIn revoked or expired the account&#39;s token (&#x60;reconnect_required&#x60;, reconnect the account). |  -  |
| **403** | The account holds no organization role that can resolve person mentions |  -  |
| **404** | Account, person or organization not found |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

