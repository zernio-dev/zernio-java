# RedditSearchApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRedditFeed**](RedditSearchApi.md#getRedditFeed) | **GET** /v1/reddit/feed | Get subreddit feed |
| [**getRedditFeedWithHttpInfo**](RedditSearchApi.md#getRedditFeedWithHttpInfo) | **GET** /v1/reddit/feed | Get subreddit feed |
| [**getRedditPostComments**](RedditSearchApi.md#getRedditPostComments) | **GET** /v1/reddit/comments/{postId} | Get the comments of a Reddit post |
| [**getRedditPostCommentsWithHttpInfo**](RedditSearchApi.md#getRedditPostCommentsWithHttpInfo) | **GET** /v1/reddit/comments/{postId} | Get the comments of a Reddit post |
| [**searchReddit**](RedditSearchApi.md#searchReddit) | **GET** /v1/reddit/search | Search posts |
| [**searchRedditWithHttpInfo**](RedditSearchApi.md#searchRedditWithHttpInfo) | **GET** /v1/reddit/search | Search posts |



## getRedditFeed

> SearchReddit200Response getRedditFeed(accountId, subreddit, sort, limit, after, t)

Get subreddit feed

Fetch posts from a subreddit feed. Supports sorting, time filtering, and cursor-based pagination.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RedditSearchApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RedditSearchApi apiInstance = new RedditSearchApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String subreddit = "subreddit_example"; // String | 
        String sort = "hot"; // String | 
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        String t = "hour"; // String | 
        try {
            SearchReddit200Response result = apiInstance.getRedditFeed(accountId, subreddit, sort, limit, after, t);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RedditSearchApi#getRedditFeed");
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
| **accountId** | **String**|  | |
| **subreddit** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] [default to hot] [enum: hot, new, top, rising] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |
| **t** | **String**|  | [optional] [enum: hour, day, week, month, year, all] |

### Return type

[**SearchReddit200Response**](SearchReddit200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feed items |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No active Reddit account with this ID is available to the API key. It may have been disconnected or deleted, or it belongs to a profile the key cannot access. Re-connecting an account issues a NEW account ID, so an ID stored from before a reconnect will not resolve.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## getRedditFeedWithHttpInfo

> ApiResponse<SearchReddit200Response> getRedditFeed getRedditFeedWithHttpInfo(accountId, subreddit, sort, limit, after, t)

Get subreddit feed

Fetch posts from a subreddit feed. Supports sorting, time filtering, and cursor-based pagination.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RedditSearchApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RedditSearchApi apiInstance = new RedditSearchApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String subreddit = "subreddit_example"; // String | 
        String sort = "hot"; // String | 
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        String t = "hour"; // String | 
        try {
            ApiResponse<SearchReddit200Response> response = apiInstance.getRedditFeedWithHttpInfo(accountId, subreddit, sort, limit, after, t);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RedditSearchApi#getRedditFeed");
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
| **accountId** | **String**|  | |
| **subreddit** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] [default to hot] [enum: hot, new, top, rising] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |
| **t** | **String**|  | [optional] [enum: hour, day, week, month, year, all] |

### Return type

ApiResponse<[**SearchReddit200Response**](SearchReddit200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feed items |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No active Reddit account with this ID is available to the API key. It may have been disconnected or deleted, or it belongs to a profile the key cannot access. Re-connecting an account issues a NEW account ID, so an ID stored from before a reconnect will not resolve.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## getRedditPostComments

> GetRedditPostComments200Response getRedditPostComments(postId, accountId, sort, limit, commentId)

Get the comments of a Reddit post

Reads the comments of any Reddit post the connected account can see, for example one found through &#x60;/v1/reddit/feed&#x60; or &#x60;/v1/reddit/search&#x60;, straight from Reddit on every call. The tree comes flattened in thread order (a reply follows its parent); rebuild it from &#x60;parentId&#x60;, which is &#x60;t3_…&#x60; for a reply to the post and &#x60;t1_…&#x60; for a reply to a comment. Deleted and removed comments are passed through as Reddit sends them (&#x60;[deleted]&#x60; / &#x60;[removed]&#x60;). Where Reddit truncates a thread, the ids it left out are listed in &#x60;more&#x60;; &#x60;commentId&#x60; fetches one such comment with its replies. A post Reddit no longer serves answers 404 and a private subreddit 403, both with &#x60;platform_api_error&#x60;. For comments on posts published through Zernio, &#x60;/v1/inbox/comments/{postId}&#x60; adds caching, moderation and replies. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RedditSearchApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RedditSearchApi apiInstance = new RedditSearchApi(defaultClient);
        String postId = "postId_example"; // String | Reddit post id, with or without the `t3_` prefix (as `id` or `fullname` on RedditPost).
        String accountId = "accountId_example"; // String | An active Reddit account the request is made as.
        String sort = "new"; // String | 
        Integer limit = 25; // Integer | Maximum number of top-level comments.
        String commentId = "commentId_example"; // String | Return only this comment and its replies, with or without the `t1_` prefix; pass an id from `more` to expand it.
        try {
            GetRedditPostComments200Response result = apiInstance.getRedditPostComments(postId, accountId, sort, limit, commentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RedditSearchApi#getRedditPostComments");
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
| **postId** | **String**| Reddit post id, with or without the &#x60;t3_&#x60; prefix (as &#x60;id&#x60; or &#x60;fullname&#x60; on RedditPost). | |
| **accountId** | **String**| An active Reddit account the request is made as. | |
| **sort** | **String**|  | [optional] [default to new] [enum: new, top, best, controversial, old, qa] |
| **limit** | **Integer**| Maximum number of top-level comments. | [optional] [default to 25] |
| **commentId** | **String**| Return only this comment and its replies, with or without the &#x60;t1_&#x60; prefix; pass an id from &#x60;more&#x60; to expand it. | [optional] |

### Return type

[**GetRedditPostComments200Response**](GetRedditPostComments200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The post and its comments |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Reddit refused the thread, typically a private or quarantined subreddit (&#x60;platform_api_error&#x60;). |  -  |
| **404** | Either no active Reddit account with this ID is available to the API key (&#x60;account_not_found&#x60;), or Reddit no longer serves the post, for example because it was deleted (&#x60;platform_api_error&#x60;).  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## getRedditPostCommentsWithHttpInfo

> ApiResponse<GetRedditPostComments200Response> getRedditPostComments getRedditPostCommentsWithHttpInfo(postId, accountId, sort, limit, commentId)

Get the comments of a Reddit post

Reads the comments of any Reddit post the connected account can see, for example one found through &#x60;/v1/reddit/feed&#x60; or &#x60;/v1/reddit/search&#x60;, straight from Reddit on every call. The tree comes flattened in thread order (a reply follows its parent); rebuild it from &#x60;parentId&#x60;, which is &#x60;t3_…&#x60; for a reply to the post and &#x60;t1_…&#x60; for a reply to a comment. Deleted and removed comments are passed through as Reddit sends them (&#x60;[deleted]&#x60; / &#x60;[removed]&#x60;). Where Reddit truncates a thread, the ids it left out are listed in &#x60;more&#x60;; &#x60;commentId&#x60; fetches one such comment with its replies. A post Reddit no longer serves answers 404 and a private subreddit 403, both with &#x60;platform_api_error&#x60;. For comments on posts published through Zernio, &#x60;/v1/inbox/comments/{postId}&#x60; adds caching, moderation and replies. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RedditSearchApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RedditSearchApi apiInstance = new RedditSearchApi(defaultClient);
        String postId = "postId_example"; // String | Reddit post id, with or without the `t3_` prefix (as `id` or `fullname` on RedditPost).
        String accountId = "accountId_example"; // String | An active Reddit account the request is made as.
        String sort = "new"; // String | 
        Integer limit = 25; // Integer | Maximum number of top-level comments.
        String commentId = "commentId_example"; // String | Return only this comment and its replies, with or without the `t1_` prefix; pass an id from `more` to expand it.
        try {
            ApiResponse<GetRedditPostComments200Response> response = apiInstance.getRedditPostCommentsWithHttpInfo(postId, accountId, sort, limit, commentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RedditSearchApi#getRedditPostComments");
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
| **postId** | **String**| Reddit post id, with or without the &#x60;t3_&#x60; prefix (as &#x60;id&#x60; or &#x60;fullname&#x60; on RedditPost). | |
| **accountId** | **String**| An active Reddit account the request is made as. | |
| **sort** | **String**|  | [optional] [default to new] [enum: new, top, best, controversial, old, qa] |
| **limit** | **Integer**| Maximum number of top-level comments. | [optional] [default to 25] |
| **commentId** | **String**| Return only this comment and its replies, with or without the &#x60;t1_&#x60; prefix; pass an id from &#x60;more&#x60; to expand it. | [optional] |

### Return type

ApiResponse<[**GetRedditPostComments200Response**](GetRedditPostComments200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The post and its comments |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Reddit refused the thread, typically a private or quarantined subreddit (&#x60;platform_api_error&#x60;). |  -  |
| **404** | Either no active Reddit account with this ID is available to the API key (&#x60;account_not_found&#x60;), or Reddit no longer serves the post, for example because it was deleted (&#x60;platform_api_error&#x60;).  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## searchReddit

> SearchReddit200Response searchReddit(accountId, q, subreddit, restrictSr, sort, limit, after)

Search posts

Search Reddit posts using a connected account. Optionally scope to a specific subreddit.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RedditSearchApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RedditSearchApi apiInstance = new RedditSearchApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String q = "q_example"; // String | 
        String subreddit = "subreddit_example"; // String | 
        String restrictSr = "0"; // String | 
        String sort = "relevance"; // String | 
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        try {
            SearchReddit200Response result = apiInstance.searchReddit(accountId, q, subreddit, restrictSr, sort, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RedditSearchApi#searchReddit");
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
| **accountId** | **String**|  | |
| **q** | **String**|  | |
| **subreddit** | **String**|  | [optional] |
| **restrictSr** | **String**|  | [optional] [enum: 0, 1] |
| **sort** | **String**|  | [optional] [default to new] [enum: relevance, hot, top, new, comments] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |

### Return type

[**SearchReddit200Response**](SearchReddit200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search results |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No active Reddit account with this ID is available to the API key. It may have been disconnected or deleted, or it belongs to a profile the key cannot access. Re-connecting an account issues a NEW account ID, so an ID stored from before a reconnect will not resolve.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## searchRedditWithHttpInfo

> ApiResponse<SearchReddit200Response> searchReddit searchRedditWithHttpInfo(accountId, q, subreddit, restrictSr, sort, limit, after)

Search posts

Search Reddit posts using a connected account. Optionally scope to a specific subreddit.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.RedditSearchApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        RedditSearchApi apiInstance = new RedditSearchApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String q = "q_example"; // String | 
        String subreddit = "subreddit_example"; // String | 
        String restrictSr = "0"; // String | 
        String sort = "relevance"; // String | 
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        try {
            ApiResponse<SearchReddit200Response> response = apiInstance.searchRedditWithHttpInfo(accountId, q, subreddit, restrictSr, sort, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling RedditSearchApi#searchReddit");
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
| **accountId** | **String**|  | |
| **q** | **String**|  | |
| **subreddit** | **String**|  | [optional] |
| **restrictSr** | **String**|  | [optional] [enum: 0, 1] |
| **sort** | **String**|  | [optional] [default to new] [enum: relevance, hot, top, new, comments] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |

### Return type

ApiResponse<[**SearchReddit200Response**](SearchReddit200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search results |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No active Reddit account with this ID is available to the API key. It may have been disconnected or deleted, or it belongs to a profile the key cannot access. Re-connecting an account issues a NEW account ID, so an ID stored from before a reconnect will not resolve.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

