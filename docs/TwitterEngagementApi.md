# TwitterEngagementApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bookmarkPost**](TwitterEngagementApi.md#bookmarkPost) | **POST** /v1/twitter/bookmark | Bookmark a tweet |
| [**bookmarkPostWithHttpInfo**](TwitterEngagementApi.md#bookmarkPostWithHttpInfo) | **POST** /v1/twitter/bookmark | Bookmark a tweet |
| [**followUser**](TwitterEngagementApi.md#followUser) | **POST** /v1/twitter/follow | Follow a user |
| [**followUserWithHttpInfo**](TwitterEngagementApi.md#followUserWithHttpInfo) | **POST** /v1/twitter/follow | Follow a user |
| [**getTweet**](TwitterEngagementApi.md#getTweet) | **GET** /v1/twitter/tweet | Look up a tweet |
| [**getTweetWithHttpInfo**](TwitterEngagementApi.md#getTweetWithHttpInfo) | **GET** /v1/twitter/tweet | Look up a tweet |
| [**removeBookmark**](TwitterEngagementApi.md#removeBookmark) | **DELETE** /v1/twitter/bookmark | Remove bookmark |
| [**removeBookmarkWithHttpInfo**](TwitterEngagementApi.md#removeBookmarkWithHttpInfo) | **DELETE** /v1/twitter/bookmark | Remove bookmark |
| [**retweetPost**](TwitterEngagementApi.md#retweetPost) | **POST** /v1/twitter/retweet | Retweet a post |
| [**retweetPostWithHttpInfo**](TwitterEngagementApi.md#retweetPostWithHttpInfo) | **POST** /v1/twitter/retweet | Retweet a post |
| [**searchTweets**](TwitterEngagementApi.md#searchTweets) | **GET** /v1/twitter/search | Search recent tweets |
| [**searchTweetsWithHttpInfo**](TwitterEngagementApi.md#searchTweetsWithHttpInfo) | **GET** /v1/twitter/search | Search recent tweets |
| [**undoRetweet**](TwitterEngagementApi.md#undoRetweet) | **DELETE** /v1/twitter/retweet | Undo retweet |
| [**undoRetweetWithHttpInfo**](TwitterEngagementApi.md#undoRetweetWithHttpInfo) | **DELETE** /v1/twitter/retweet | Undo retweet |
| [**unfollowUser**](TwitterEngagementApi.md#unfollowUser) | **DELETE** /v1/twitter/follow | Unfollow a user |
| [**unfollowUserWithHttpInfo**](TwitterEngagementApi.md#unfollowUserWithHttpInfo) | **DELETE** /v1/twitter/follow | Unfollow a user |



## bookmarkPost

> BookmarkPost200Response bookmarkPost(bookmarkPostRequest)

Bookmark a tweet

Bookmark a tweet by ID. Requires the bookmark.write OAuth scope. Rate limit: 50 requests per 15-min window. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        BookmarkPostRequest bookmarkPostRequest = new BookmarkPostRequest(); // BookmarkPostRequest | 
        try {
            BookmarkPost200Response result = apiInstance.bookmarkPost(bookmarkPostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#bookmarkPost");
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
| **bookmarkPostRequest** | [**BookmarkPostRequest**](BookmarkPostRequest.md)|  | |

### Return type

[**BookmarkPost200Response**](BookmarkPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tweet bookmarked |  -  |
| **400** | Bad request or platform limitation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## bookmarkPostWithHttpInfo

> ApiResponse<BookmarkPost200Response> bookmarkPost bookmarkPostWithHttpInfo(bookmarkPostRequest)

Bookmark a tweet

Bookmark a tweet by ID. Requires the bookmark.write OAuth scope. Rate limit: 50 requests per 15-min window. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        BookmarkPostRequest bookmarkPostRequest = new BookmarkPostRequest(); // BookmarkPostRequest | 
        try {
            ApiResponse<BookmarkPost200Response> response = apiInstance.bookmarkPostWithHttpInfo(bookmarkPostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#bookmarkPost");
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
| **bookmarkPostRequest** | [**BookmarkPostRequest**](BookmarkPostRequest.md)|  | |

### Return type

ApiResponse<[**BookmarkPost200Response**](BookmarkPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tweet bookmarked |  -  |
| **400** | Bad request or platform limitation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## followUser

> FollowUser200Response followUser(followUserRequest)

Follow a user

Follow a user on X/Twitter. Requires the follows.write OAuth scope. For protected accounts, a follow request is sent instead (pending_follow will be true). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        FollowUserRequest followUserRequest = new FollowUserRequest(); // FollowUserRequest | 
        try {
            FollowUser200Response result = apiInstance.followUser(followUserRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#followUser");
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
| **followUserRequest** | [**FollowUserRequest**](FollowUserRequest.md)|  | |

### Return type

[**FollowUser200Response**](FollowUser200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User followed or follow request sent |  -  |
| **400** | Bad request or platform limitation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## followUserWithHttpInfo

> ApiResponse<FollowUser200Response> followUser followUserWithHttpInfo(followUserRequest)

Follow a user

Follow a user on X/Twitter. Requires the follows.write OAuth scope. For protected accounts, a follow request is sent instead (pending_follow will be true). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        FollowUserRequest followUserRequest = new FollowUserRequest(); // FollowUserRequest | 
        try {
            ApiResponse<FollowUser200Response> response = apiInstance.followUserWithHttpInfo(followUserRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#followUser");
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
| **followUserRequest** | [**FollowUserRequest**](FollowUserRequest.md)|  | |

### Return type

ApiResponse<[**FollowUser200Response**](FollowUser200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User followed or follow request sent |  -  |
| **400** | Bad request or platform limitation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## getTweet

> GetTweet200Response getTweet(accountId, id)

Look up a tweet

Resolve a single tweet by ID or URL into its text, author and public metrics.  Use this to render a post you are referencing, e.g. the tweet quoted by a quote-style post. Unlike &#x60;/v1/twitter/search&#x60; this is not limited to the last 7 days and works for any tweet visible to the connected account.  Billed as an X posts read ($0.005). Repeat lookups of the same tweet within the same UTC day are charged once. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | The social account ID whose X token is used for the lookup
        String id = "id_example"; // String | Numeric tweet ID or a tweet URL (e.g. https://x.com/user/status/123...)
        try {
            GetTweet200Response result = apiInstance.getTweet(accountId, id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#getTweet");
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
| **accountId** | **String**| The social account ID whose X token is used for the lookup | |
| **id** | **String**| Numeric tweet ID or a tweet URL (e.g. https://x.com/user/status/123...) | |

### Return type

[**GetTweet200Response**](GetTweet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resolved tweet |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | X API spend cap reached for this billing period |  -  |
| **403** | X analytics capability not enabled for this account (code X_ANALYTICS_NOT_ENABLED), or the tweet author is protected or suspended |  -  |
| **404** | Account not found, or the tweet was deleted or never existed |  -  |
| **429** | X rate limit exceeded |  -  |

## getTweetWithHttpInfo

> ApiResponse<GetTweet200Response> getTweet getTweetWithHttpInfo(accountId, id)

Look up a tweet

Resolve a single tweet by ID or URL into its text, author and public metrics.  Use this to render a post you are referencing, e.g. the tweet quoted by a quote-style post. Unlike &#x60;/v1/twitter/search&#x60; this is not limited to the last 7 days and works for any tweet visible to the connected account.  Billed as an X posts read ($0.005). Repeat lookups of the same tweet within the same UTC day are charged once. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | The social account ID whose X token is used for the lookup
        String id = "id_example"; // String | Numeric tweet ID or a tweet URL (e.g. https://x.com/user/status/123...)
        try {
            ApiResponse<GetTweet200Response> response = apiInstance.getTweetWithHttpInfo(accountId, id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#getTweet");
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
| **accountId** | **String**| The social account ID whose X token is used for the lookup | |
| **id** | **String**| Numeric tweet ID or a tweet URL (e.g. https://x.com/user/status/123...) | |

### Return type

ApiResponse<[**GetTweet200Response**](GetTweet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resolved tweet |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | X API spend cap reached for this billing period |  -  |
| **403** | X analytics capability not enabled for this account (code X_ANALYTICS_NOT_ENABLED), or the tweet author is protected or suspended |  -  |
| **404** | Account not found, or the tweet was deleted or never existed |  -  |
| **429** | X rate limit exceeded |  -  |


## removeBookmark

> RemoveBookmark200Response removeBookmark(accountId, tweetId)

Remove bookmark

Remove a bookmark from a tweet. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tweetId = "tweetId_example"; // String | The ID of the tweet to unbookmark
        try {
            RemoveBookmark200Response result = apiInstance.removeBookmark(accountId, tweetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#removeBookmark");
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
| **tweetId** | **String**| The ID of the tweet to unbookmark | |

### Return type

[**RemoveBookmark200Response**](RemoveBookmark200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bookmark removed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## removeBookmarkWithHttpInfo

> ApiResponse<RemoveBookmark200Response> removeBookmark removeBookmarkWithHttpInfo(accountId, tweetId)

Remove bookmark

Remove a bookmark from a tweet. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tweetId = "tweetId_example"; // String | The ID of the tweet to unbookmark
        try {
            ApiResponse<RemoveBookmark200Response> response = apiInstance.removeBookmarkWithHttpInfo(accountId, tweetId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#removeBookmark");
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
| **tweetId** | **String**| The ID of the tweet to unbookmark | |

### Return type

ApiResponse<[**RemoveBookmark200Response**](RemoveBookmark200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bookmark removed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## retweetPost

> RetweetPost200Response retweetPost(retweetPostRequest)

Retweet a post

Retweet (repost) a tweet by ID. Rate limit: 50 requests per 15-min window. Shares the 300/3hr creation limit with tweet creation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        RetweetPostRequest retweetPostRequest = new RetweetPostRequest(); // RetweetPostRequest | 
        try {
            RetweetPost200Response result = apiInstance.retweetPost(retweetPostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#retweetPost");
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
| **retweetPostRequest** | [**RetweetPostRequest**](RetweetPostRequest.md)|  | |

### Return type

[**RetweetPost200Response**](RetweetPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tweet retweeted |  -  |
| **400** | Bad request or platform limitation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## retweetPostWithHttpInfo

> ApiResponse<RetweetPost200Response> retweetPost retweetPostWithHttpInfo(retweetPostRequest)

Retweet a post

Retweet (repost) a tweet by ID. Rate limit: 50 requests per 15-min window. Shares the 300/3hr creation limit with tweet creation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        RetweetPostRequest retweetPostRequest = new RetweetPostRequest(); // RetweetPostRequest | 
        try {
            ApiResponse<RetweetPost200Response> response = apiInstance.retweetPostWithHttpInfo(retweetPostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#retweetPost");
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
| **retweetPostRequest** | [**RetweetPostRequest**](RetweetPostRequest.md)|  | |

### Return type

ApiResponse<[**RetweetPost200Response**](RetweetPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tweet retweeted |  -  |
| **400** | Bad request or platform limitation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## searchTweets

> SearchTweets200Response searchTweets(accountId, query, limit, sinceId, untilId, startTime, endTime, cursor, sortOrder)

Search recent tweets

Search public tweets from the last 7 days matching an X search query, e.g. to discover tweets to reply to. The query string is passed through to X unchanged and supports X&#39;s search operators (&#x60;from:user&#x60;, &#x60;-is:retweet&#x60;, &#x60;is:reply&#x60;, &#x60;lang:en&#x60;, &#x60;\&quot;exact phrase\&quot;&#x60;, &#x60;conversation_id:123&#x60;, boolean &#x60;OR&#x60;, ...). Note that standalone operators like &#x60;is:&#x60; / &#x60;has:&#x60; / &#x60;lang:&#x60; must be combined with a keyword or &#x60;from:&#x60; clause.  To reply to a found tweet, pass its &#x60;id&#x60; as the twitter platform entry&#39;s &#x60;platformSpecificData.replyToTweetId&#x60; when creating a post.  Rate limit: 300 requests per 15-min window per connected account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | The social account ID
        String query = "query_example"; // String | X search query, max 512 characters. Operators are passed through unchanged; X rejects malformed queries with a 400.
        Integer limit = 10; // Integer | Results per page. X requires a minimum of 10; values below 10 are rejected.
        String sinceId = "sinceId_example"; // String | Only return tweets with an ID greater than (more recent than) this numeric tweet ID. Non-numeric values are rejected with 400.
        String untilId = "untilId_example"; // String | Only return tweets with an ID less than (older than) this numeric tweet ID. Non-numeric values are rejected with 400.
        OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Oldest UTC timestamp (ISO 8601, inclusive), within the last 7 days
        OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | Newest UTC timestamp (ISO 8601, exclusive), within the last 7 days
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response
        String sortOrder = "recency"; // String | 
        try {
            SearchTweets200Response result = apiInstance.searchTweets(accountId, query, limit, sinceId, untilId, startTime, endTime, cursor, sortOrder);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#searchTweets");
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
| **accountId** | **String**| The social account ID | |
| **query** | **String**| X search query, max 512 characters. Operators are passed through unchanged; X rejects malformed queries with a 400. | |
| **limit** | **Integer**| Results per page. X requires a minimum of 10; values below 10 are rejected. | [optional] [default to 10] |
| **sinceId** | **String**| Only return tweets with an ID greater than (more recent than) this numeric tweet ID. Non-numeric values are rejected with 400. | [optional] |
| **untilId** | **String**| Only return tweets with an ID less than (older than) this numeric tweet ID. Non-numeric values are rejected with 400. | [optional] |
| **startTime** | **OffsetDateTime**| Oldest UTC timestamp (ISO 8601, inclusive), within the last 7 days | [optional] |
| **endTime** | **OffsetDateTime**| Newest UTC timestamp (ISO 8601, exclusive), within the last 7 days | [optional] |
| **cursor** | **String**| Pagination cursor from a previous response | [optional] |
| **sortOrder** | **String**|  | [optional] [default to recency] [enum: recency, relevancy] |

### Return type

[**SearchTweets200Response**](SearchTweets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching tweets |  -  |
| **400** | Bad request (invalid params, or X rejected the query as malformed) |  -  |
| **401** | Unauthorized |  -  |
| **402** | X API spend cap reached for this billing period |  -  |
| **403** | X analytics capability not enabled for this account (code X_ANALYTICS_NOT_ENABLED) |  -  |
| **404** | Account not found |  -  |
| **429** | X search rate limit exceeded (300 requests per 15 minutes) |  -  |

## searchTweetsWithHttpInfo

> ApiResponse<SearchTweets200Response> searchTweets searchTweetsWithHttpInfo(accountId, query, limit, sinceId, untilId, startTime, endTime, cursor, sortOrder)

Search recent tweets

Search public tweets from the last 7 days matching an X search query, e.g. to discover tweets to reply to. The query string is passed through to X unchanged and supports X&#39;s search operators (&#x60;from:user&#x60;, &#x60;-is:retweet&#x60;, &#x60;is:reply&#x60;, &#x60;lang:en&#x60;, &#x60;\&quot;exact phrase\&quot;&#x60;, &#x60;conversation_id:123&#x60;, boolean &#x60;OR&#x60;, ...). Note that standalone operators like &#x60;is:&#x60; / &#x60;has:&#x60; / &#x60;lang:&#x60; must be combined with a keyword or &#x60;from:&#x60; clause.  To reply to a found tweet, pass its &#x60;id&#x60; as the twitter platform entry&#39;s &#x60;platformSpecificData.replyToTweetId&#x60; when creating a post.  Rate limit: 300 requests per 15-min window per connected account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | The social account ID
        String query = "query_example"; // String | X search query, max 512 characters. Operators are passed through unchanged; X rejects malformed queries with a 400.
        Integer limit = 10; // Integer | Results per page. X requires a minimum of 10; values below 10 are rejected.
        String sinceId = "sinceId_example"; // String | Only return tweets with an ID greater than (more recent than) this numeric tweet ID. Non-numeric values are rejected with 400.
        String untilId = "untilId_example"; // String | Only return tweets with an ID less than (older than) this numeric tweet ID. Non-numeric values are rejected with 400.
        OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | Oldest UTC timestamp (ISO 8601, inclusive), within the last 7 days
        OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | Newest UTC timestamp (ISO 8601, exclusive), within the last 7 days
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response
        String sortOrder = "recency"; // String | 
        try {
            ApiResponse<SearchTweets200Response> response = apiInstance.searchTweetsWithHttpInfo(accountId, query, limit, sinceId, untilId, startTime, endTime, cursor, sortOrder);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#searchTweets");
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
| **accountId** | **String**| The social account ID | |
| **query** | **String**| X search query, max 512 characters. Operators are passed through unchanged; X rejects malformed queries with a 400. | |
| **limit** | **Integer**| Results per page. X requires a minimum of 10; values below 10 are rejected. | [optional] [default to 10] |
| **sinceId** | **String**| Only return tweets with an ID greater than (more recent than) this numeric tweet ID. Non-numeric values are rejected with 400. | [optional] |
| **untilId** | **String**| Only return tweets with an ID less than (older than) this numeric tweet ID. Non-numeric values are rejected with 400. | [optional] |
| **startTime** | **OffsetDateTime**| Oldest UTC timestamp (ISO 8601, inclusive), within the last 7 days | [optional] |
| **endTime** | **OffsetDateTime**| Newest UTC timestamp (ISO 8601, exclusive), within the last 7 days | [optional] |
| **cursor** | **String**| Pagination cursor from a previous response | [optional] |
| **sortOrder** | **String**|  | [optional] [default to recency] [enum: recency, relevancy] |

### Return type

ApiResponse<[**SearchTweets200Response**](SearchTweets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching tweets |  -  |
| **400** | Bad request (invalid params, or X rejected the query as malformed) |  -  |
| **401** | Unauthorized |  -  |
| **402** | X API spend cap reached for this billing period |  -  |
| **403** | X analytics capability not enabled for this account (code X_ANALYTICS_NOT_ENABLED) |  -  |
| **404** | Account not found |  -  |
| **429** | X search rate limit exceeded (300 requests per 15 minutes) |  -  |


## undoRetweet

> UndoRetweet200Response undoRetweet(accountId, tweetId)

Undo retweet

Undo a retweet (un-repost a tweet). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tweetId = "tweetId_example"; // String | The ID of the original tweet to un-retweet
        try {
            UndoRetweet200Response result = apiInstance.undoRetweet(accountId, tweetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#undoRetweet");
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
| **tweetId** | **String**| The ID of the original tweet to un-retweet | |

### Return type

[**UndoRetweet200Response**](UndoRetweet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retweet undone |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## undoRetweetWithHttpInfo

> ApiResponse<UndoRetweet200Response> undoRetweet undoRetweetWithHttpInfo(accountId, tweetId)

Undo retweet

Undo a retweet (un-repost a tweet). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tweetId = "tweetId_example"; // String | The ID of the original tweet to un-retweet
        try {
            ApiResponse<UndoRetweet200Response> response = apiInstance.undoRetweetWithHttpInfo(accountId, tweetId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#undoRetweet");
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
| **tweetId** | **String**| The ID of the original tweet to un-retweet | |

### Return type

ApiResponse<[**UndoRetweet200Response**](UndoRetweet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retweet undone |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |


## unfollowUser

> UnfollowUser200Response unfollowUser(accountId, targetUserId)

Unfollow a user

Unfollow a user on X/Twitter. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String targetUserId = "targetUserId_example"; // String | The Twitter ID of the user to unfollow
        try {
            UnfollowUser200Response result = apiInstance.unfollowUser(accountId, targetUserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#unfollowUser");
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
| **targetUserId** | **String**| The Twitter ID of the user to unfollow | |

### Return type

[**UnfollowUser200Response**](UnfollowUser200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User unfollowed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

## unfollowUserWithHttpInfo

> ApiResponse<UnfollowUser200Response> unfollowUser unfollowUserWithHttpInfo(accountId, targetUserId)

Unfollow a user

Unfollow a user on X/Twitter. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TwitterEngagementApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TwitterEngagementApi apiInstance = new TwitterEngagementApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String targetUserId = "targetUserId_example"; // String | The Twitter ID of the user to unfollow
        try {
            ApiResponse<UnfollowUser200Response> response = apiInstance.unfollowUserWithHttpInfo(accountId, targetUserId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TwitterEngagementApi#unfollowUser");
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
| **targetUserId** | **String**| The Twitter ID of the user to unfollow | |

### Return type

ApiResponse<[**UnfollowUser200Response**](UnfollowUser200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User unfollowed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |

