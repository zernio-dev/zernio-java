# MediaApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMediaPresignedUrl**](MediaApi.md#getMediaPresignedUrl) | **POST** /v1/media/presign | Get upload URL |
| [**getMediaPresignedUrlWithHttpInfo**](MediaApi.md#getMediaPresignedUrlWithHttpInfo) | **POST** /v1/media/presign | Get upload URL |
| [**prepareMedia**](MediaApi.md#prepareMedia) | **POST** /v1/media/prepare | Prepare media for a platform |
| [**prepareMediaWithHttpInfo**](MediaApi.md#prepareMediaWithHttpInfo) | **POST** /v1/media/prepare | Prepare media for a platform |



## getMediaPresignedUrl

> GetMediaPresignedUrl200Response getMediaPresignedUrl(getMediaPresignedUrlRequest)

Get upload URL

Get a presigned URL to upload files directly to cloud storage (up to 5GB). Returns an uploadUrl and publicUrl. PUT your file to the uploadUrl, then use the publicUrl in your posts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MediaApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MediaApi apiInstance = new MediaApi(defaultClient);
        GetMediaPresignedUrlRequest getMediaPresignedUrlRequest = new GetMediaPresignedUrlRequest(); // GetMediaPresignedUrlRequest | 
        try {
            GetMediaPresignedUrl200Response result = apiInstance.getMediaPresignedUrl(getMediaPresignedUrlRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MediaApi#getMediaPresignedUrl");
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
| **getMediaPresignedUrlRequest** | [**GetMediaPresignedUrlRequest**](GetMediaPresignedUrlRequest.md)|  | |

### Return type

[**GetMediaPresignedUrl200Response**](GetMediaPresignedUrl200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Presigned URL generated successfully |  -  |
| **400** | Invalid request (missing filename, unsupported contentType, or size out of range) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## getMediaPresignedUrlWithHttpInfo

> ApiResponse<GetMediaPresignedUrl200Response> getMediaPresignedUrl getMediaPresignedUrlWithHttpInfo(getMediaPresignedUrlRequest)

Get upload URL

Get a presigned URL to upload files directly to cloud storage (up to 5GB). Returns an uploadUrl and publicUrl. PUT your file to the uploadUrl, then use the publicUrl in your posts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MediaApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MediaApi apiInstance = new MediaApi(defaultClient);
        GetMediaPresignedUrlRequest getMediaPresignedUrlRequest = new GetMediaPresignedUrlRequest(); // GetMediaPresignedUrlRequest | 
        try {
            ApiResponse<GetMediaPresignedUrl200Response> response = apiInstance.getMediaPresignedUrlWithHttpInfo(getMediaPresignedUrlRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MediaApi#getMediaPresignedUrl");
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
| **getMediaPresignedUrlRequest** | [**GetMediaPresignedUrlRequest**](GetMediaPresignedUrlRequest.md)|  | |

### Return type

ApiResponse<[**GetMediaPresignedUrl200Response**](GetMediaPresignedUrl200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Presigned URL generated successfully |  -  |
| **400** | Invalid request (missing filename, unsupported contentType, or size out of range) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## prepareMedia

> PrepareMedia200Response prepareMedia(prepareMediaRequest)

Prepare media for a platform

Turn any image or video into a version the target platform accepts, using the same per-platform processing Zernio runs before publishing. Each team can prepare up to 60 files per hour; past that the endpoint answers 429 with &#x60;retryAfterSeconds&#x60;.  What each target does to a video: &#x60;instagram&#x60;, &#x60;facebook_reel&#x60; re-encode to H.264 Main 4.1, 30 fps, 1080 wide (HDR sources only get the size step, so they are not flattened to SDR). &#x60;instagram_story&#x60; re-encodes a video over 100MB to fit 60 seconds and 100MB. &#x60;facebook_story&#x60; reframes anything wider than 9:16 onto a 1080x1920 canvas with a blurred background (Facebook otherwise publishes such stories with 0 seconds of video and no error). &#x60;threads&#x60; re-encodes to the conservative H.264 Baseline profile Threads processes reliably. &#x60;bluesky&#x60; re-encodes to 1080 wide and at most 180 seconds, then compresses under 50MB if the result is still larger. &#x60;telegram&#x60; compresses to 50MB and moves the index to the start of the file. The other targets compress only when the file is over the platform limit.  Images are converted to a format the platform ingests (Instagram takes only JPEG, LinkedIn and Google Business reject WebP and AVIF) and compressed under its size limit; &#x60;telegram&#x60; also fits the width plus height limit and &#x60;googlebusiness&#x60; enlarges images under its minimum size.  When the file already complies, &#x60;changed&#x60; is false and &#x60;url&#x60; is the input URL (after redirects). Otherwise &#x60;url&#x60; points to the prepared file in Zernio storage, kept under the same retention as uploaded media. The request is synchronous: a long video can take a few minutes. Videos over 200MB are refused with 413, and a video URL whose host sends no Content-Length is refused with 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MediaApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MediaApi apiInstance = new MediaApi(defaultClient);
        PrepareMediaRequest prepareMediaRequest = new PrepareMediaRequest(); // PrepareMediaRequest | 
        try {
            PrepareMedia200Response result = apiInstance.prepareMedia(prepareMediaRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MediaApi#prepareMedia");
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
| **prepareMediaRequest** | [**PrepareMediaRequest**](PrepareMediaRequest.md)|  | |

### Return type

[**PrepareMedia200Response**](PrepareMedia200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prepared media |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **413** | The video is over the 200MB this endpoint prepares. |  -  |
| **422** | The media could not be processed (for example a corrupt file). |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  YouTube Analytics: reads (channel-insights, demographics, daily-views, video-retention) run on the \&quot;Queries per day\&quot; quota of the Google Cloud project the YouTube account is connected through, shared with other Zernio customers, so a 429 there is not your own volume. It resets at midnight Pacific Time. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  Pinterest ads: Pinterest rate-limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when it sends one, otherwise 60 seconds.  TikTok ads: TikTok limits requests per app and per endpoint (per second, per minute and per day) and answers overage with code 40100 or with code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (for example one ad at a time per advertiser) instead of retrying at once. The Smart+ review read (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has a stricter quota of its own on TikTok: after an overage Zernio answers 429 for that advertiser and connection, without calling TikTok, for about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, each with up to 10% of random jitter. A successful call holds nothing back, and the next overage after it pauses about 60 seconds again; &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## prepareMediaWithHttpInfo

> ApiResponse<PrepareMedia200Response> prepareMedia prepareMediaWithHttpInfo(prepareMediaRequest)

Prepare media for a platform

Turn any image or video into a version the target platform accepts, using the same per-platform processing Zernio runs before publishing. Each team can prepare up to 60 files per hour; past that the endpoint answers 429 with &#x60;retryAfterSeconds&#x60;.  What each target does to a video: &#x60;instagram&#x60;, &#x60;facebook_reel&#x60; re-encode to H.264 Main 4.1, 30 fps, 1080 wide (HDR sources only get the size step, so they are not flattened to SDR). &#x60;instagram_story&#x60; re-encodes a video over 100MB to fit 60 seconds and 100MB. &#x60;facebook_story&#x60; reframes anything wider than 9:16 onto a 1080x1920 canvas with a blurred background (Facebook otherwise publishes such stories with 0 seconds of video and no error). &#x60;threads&#x60; re-encodes to the conservative H.264 Baseline profile Threads processes reliably. &#x60;bluesky&#x60; re-encodes to 1080 wide and at most 180 seconds, then compresses under 50MB if the result is still larger. &#x60;telegram&#x60; compresses to 50MB and moves the index to the start of the file. The other targets compress only when the file is over the platform limit.  Images are converted to a format the platform ingests (Instagram takes only JPEG, LinkedIn and Google Business reject WebP and AVIF) and compressed under its size limit; &#x60;telegram&#x60; also fits the width plus height limit and &#x60;googlebusiness&#x60; enlarges images under its minimum size.  When the file already complies, &#x60;changed&#x60; is false and &#x60;url&#x60; is the input URL (after redirects). Otherwise &#x60;url&#x60; points to the prepared file in Zernio storage, kept under the same retention as uploaded media. The request is synchronous: a long video can take a few minutes. Videos over 200MB are refused with 413, and a video URL whose host sends no Content-Length is refused with 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MediaApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MediaApi apiInstance = new MediaApi(defaultClient);
        PrepareMediaRequest prepareMediaRequest = new PrepareMediaRequest(); // PrepareMediaRequest | 
        try {
            ApiResponse<PrepareMedia200Response> response = apiInstance.prepareMediaWithHttpInfo(prepareMediaRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MediaApi#prepareMedia");
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
| **prepareMediaRequest** | [**PrepareMediaRequest**](PrepareMediaRequest.md)|  | |

### Return type

ApiResponse<[**PrepareMedia200Response**](PrepareMedia200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prepared media |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **413** | The video is over the 200MB this endpoint prepares. |  -  |
| **422** | The media could not be processed (for example a corrupt file). |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  YouTube Analytics: reads (channel-insights, demographics, daily-views, video-retention) run on the \&quot;Queries per day\&quot; quota of the Google Cloud project the YouTube account is connected through, shared with other Zernio customers, so a 429 there is not your own volume. It resets at midnight Pacific Time. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  Pinterest ads: Pinterest rate-limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when it sends one, otherwise 60 seconds.  TikTok ads: TikTok limits requests per app and per endpoint (per second, per minute and per day) and answers overage with code 40100 or with code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (for example one ad at a time per advertiser) instead of retrying at once. The Smart+ review read (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has a stricter quota of its own on TikTok: after an overage Zernio answers 429 for that advertiser and connection, without calling TikTok, for about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, each with up to 10% of random jitter. A successful call holds nothing back, and the next overage after it pauses about 60 seconds again; &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

