# CommentsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteInboxComment**](CommentsApi.md#deleteInboxComment) | **DELETE** /v1/inbox/comments/{postId} | Delete comment |
| [**deleteInboxCommentWithHttpInfo**](CommentsApi.md#deleteInboxCommentWithHttpInfo) | **DELETE** /v1/inbox/comments/{postId} | Delete comment |
| [**editInboxComment**](CommentsApi.md#editInboxComment) | **PATCH** /v1/inbox/comments/{postId}/{commentId} | Edit comment |
| [**editInboxCommentWithHttpInfo**](CommentsApi.md#editInboxCommentWithHttpInfo) | **PATCH** /v1/inbox/comments/{postId}/{commentId} | Edit comment |
| [**getInboxPostComments**](CommentsApi.md#getInboxPostComments) | **GET** /v1/inbox/comments/{postId} | Get post comments |
| [**getInboxPostCommentsWithHttpInfo**](CommentsApi.md#getInboxPostCommentsWithHttpInfo) | **GET** /v1/inbox/comments/{postId} | Get post comments |
| [**hideInboxComment**](CommentsApi.md#hideInboxComment) | **POST** /v1/inbox/comments/{postId}/{commentId}/hide | Hide comment |
| [**hideInboxCommentWithHttpInfo**](CommentsApi.md#hideInboxCommentWithHttpInfo) | **POST** /v1/inbox/comments/{postId}/{commentId}/hide | Hide comment |
| [**likeInboxComment**](CommentsApi.md#likeInboxComment) | **POST** /v1/inbox/comments/{postId}/{commentId}/like | Like comment |
| [**likeInboxCommentWithHttpInfo**](CommentsApi.md#likeInboxCommentWithHttpInfo) | **POST** /v1/inbox/comments/{postId}/{commentId}/like | Like comment |
| [**likePost**](CommentsApi.md#likePost) | **POST** /v1/inbox/posts/{postId}/like | Like post |
| [**likePostWithHttpInfo**](CommentsApi.md#likePostWithHttpInfo) | **POST** /v1/inbox/posts/{postId}/like | Like post |
| [**listInboxComments**](CommentsApi.md#listInboxComments) | **GET** /v1/inbox/comments | List commented posts |
| [**listInboxCommentsWithHttpInfo**](CommentsApi.md#listInboxCommentsWithHttpInfo) | **GET** /v1/inbox/comments | List commented posts |
| [**replyToInboxPost**](CommentsApi.md#replyToInboxPost) | **POST** /v1/inbox/comments/{postId} | Reply to comment |
| [**replyToInboxPostWithHttpInfo**](CommentsApi.md#replyToInboxPostWithHttpInfo) | **POST** /v1/inbox/comments/{postId} | Reply to comment |
| [**sendPrivateReplyToComment**](CommentsApi.md#sendPrivateReplyToComment) | **POST** /v1/inbox/comments/{postId}/{commentId}/private-reply | Send private reply |
| [**sendPrivateReplyToCommentWithHttpInfo**](CommentsApi.md#sendPrivateReplyToCommentWithHttpInfo) | **POST** /v1/inbox/comments/{postId}/{commentId}/private-reply | Send private reply |
| [**setCommentModeration**](CommentsApi.md#setCommentModeration) | **POST** /v1/inbox/comments/{postId}/{commentId}/moderation | Set comment moderation status |
| [**setCommentModerationWithHttpInfo**](CommentsApi.md#setCommentModerationWithHttpInfo) | **POST** /v1/inbox/comments/{postId}/{commentId}/moderation | Set comment moderation status |
| [**unhideInboxComment**](CommentsApi.md#unhideInboxComment) | **DELETE** /v1/inbox/comments/{postId}/{commentId}/hide | Unhide comment |
| [**unhideInboxCommentWithHttpInfo**](CommentsApi.md#unhideInboxCommentWithHttpInfo) | **DELETE** /v1/inbox/comments/{postId}/{commentId}/hide | Unhide comment |
| [**unlikeInboxComment**](CommentsApi.md#unlikeInboxComment) | **DELETE** /v1/inbox/comments/{postId}/{commentId}/like | Unlike comment |
| [**unlikeInboxCommentWithHttpInfo**](CommentsApi.md#unlikeInboxCommentWithHttpInfo) | **DELETE** /v1/inbox/comments/{postId}/{commentId}/like | Unlike comment |
| [**unlikePost**](CommentsApi.md#unlikePost) | **DELETE** /v1/inbox/posts/{postId}/like | Unlike post |
| [**unlikePostWithHttpInfo**](CommentsApi.md#unlikePostWithHttpInfo) | **DELETE** /v1/inbox/posts/{postId}/like | Unlike post |



## deleteInboxComment

> DeleteInboxComment200Response deleteInboxComment(postId, accountId, commentId)

Delete comment

Delete a comment on a post. Supported by Facebook, Instagram, Bluesky, Reddit, YouTube, and LinkedIn. Requires accountId and commentId query parameters. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID.
        String accountId = "accountId_example"; // String | 
        String commentId = "commentId_example"; // String | For LinkedIn, accepts either the numeric comment ID or the composite comment URN returned by the comments listing (e.g. urn:li:comment:(threadUrn,id))
        try {
            DeleteInboxComment200Response result = apiInstance.deleteInboxComment(postId, accountId, commentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#deleteInboxComment");
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
| **postId** | **String**| Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID. | |
| **accountId** | **String**|  | |
| **commentId** | **String**| For LinkedIn, accepts either the numeric comment ID or the composite comment URN returned by the comments listing (e.g. urn:li:comment:(threadUrn,id)) | |

### Return type

[**DeleteInboxComment200Response**](DeleteInboxComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment deleted |  -  |
| **400** | Platform rejected the operation (e.g., comment already deleted) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the connected account is not permitted to delete this comment on the platform (code platform_api_error, type platform_error) |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | Upstream platform error (code platform_api_error, type platform_error) |  -  |

## deleteInboxCommentWithHttpInfo

> ApiResponse<DeleteInboxComment200Response> deleteInboxComment deleteInboxCommentWithHttpInfo(postId, accountId, commentId)

Delete comment

Delete a comment on a post. Supported by Facebook, Instagram, Bluesky, Reddit, YouTube, and LinkedIn. Requires accountId and commentId query parameters. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID.
        String accountId = "accountId_example"; // String | 
        String commentId = "commentId_example"; // String | For LinkedIn, accepts either the numeric comment ID or the composite comment URN returned by the comments listing (e.g. urn:li:comment:(threadUrn,id))
        try {
            ApiResponse<DeleteInboxComment200Response> response = apiInstance.deleteInboxCommentWithHttpInfo(postId, accountId, commentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#deleteInboxComment");
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
| **postId** | **String**| Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID. | |
| **accountId** | **String**|  | |
| **commentId** | **String**| For LinkedIn, accepts either the numeric comment ID or the composite comment URN returned by the comments listing (e.g. urn:li:comment:(threadUrn,id)) | |

### Return type

ApiResponse<[**DeleteInboxComment200Response**](DeleteInboxComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment deleted |  -  |
| **400** | Platform rejected the operation (e.g., comment already deleted) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the connected account is not permitted to delete this comment on the platform (code platform_api_error, type platform_error) |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | Upstream platform error (code platform_api_error, type platform_error) |  -  |


## editInboxComment

> EditInboxComment200Response editInboxComment(postId, commentId, editInboxCommentRequest)

Edit comment

Edit the body of a comment the connected account posted. Supported on Reddit only.  Reddit keeps the same comment id after an edit. Reddit exposes no API to edit a post title, and a link post has no editable body. To edit a published post&#39;s body, use &#x60;POST /v1/posts/{postId}/edit&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        EditInboxCommentRequest editInboxCommentRequest = new EditInboxCommentRequest(); // EditInboxCommentRequest | 
        try {
            EditInboxComment200Response result = apiInstance.editInboxComment(postId, commentId, editInboxCommentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#editInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **editInboxCommentRequest** | [**EditInboxCommentRequest**](EditInboxCommentRequest.md)|  | |

### Return type

[**EditInboxComment200Response**](EditInboxComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment edited |  -  |
| **400** | Platform does not support editing comments (code: platform_not_supported), or content missing. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses are forwarded as-is. |  -  |

## editInboxCommentWithHttpInfo

> ApiResponse<EditInboxComment200Response> editInboxComment editInboxCommentWithHttpInfo(postId, commentId, editInboxCommentRequest)

Edit comment

Edit the body of a comment the connected account posted. Supported on Reddit only.  Reddit keeps the same comment id after an edit. Reddit exposes no API to edit a post title, and a link post has no editable body. To edit a published post&#39;s body, use &#x60;POST /v1/posts/{postId}/edit&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        EditInboxCommentRequest editInboxCommentRequest = new EditInboxCommentRequest(); // EditInboxCommentRequest | 
        try {
            ApiResponse<EditInboxComment200Response> response = apiInstance.editInboxCommentWithHttpInfo(postId, commentId, editInboxCommentRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#editInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **editInboxCommentRequest** | [**EditInboxCommentRequest**](EditInboxCommentRequest.md)|  | |

### Return type

ApiResponse<[**EditInboxComment200Response**](EditInboxComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment edited |  -  |
| **400** | Platform does not support editing comments (code: platform_not_supported), or content missing. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |
| **502** | Reddit was unreachable or returned an unclassified error. Reddit 4xx statuses are forwarded as-is. |  -  |


## getInboxPostComments

> GetInboxPostComments200Response getInboxPostComments(postId, accountId, subreddit, limit, cursor, commentId)

Get post comments

Fetch comments for a specific post. Requires accountId query parameter.  On Facebook and Instagram, passing a COMMENT id as &#x60;postId&#x60; is also supported and returns that comment&#39;s replies instead of the post&#39;s top-level comments. This is not available on YouTube, where &#x60;postId&#x60; must be a video id.  Responses are cached for up to 10 minutes, so a page may lag new comments by that window. Do not poll this endpoint for real-time updates: subscribe to the &#x60;comment.received&#x60; webhook, which delivers new comments as they arrive. Your own writes (creating, replying to, or deleting a comment) refresh the cache immediately. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or platform-specific post ID. Zernio IDs are auto-resolved. LinkedIn third-party posts accept full activity URN or numeric ID. On Facebook and Instagram, a comment ID is also accepted here and returns that comment's replies.
        String accountId = "accountId_example"; // String | 
        String subreddit = "subreddit_example"; // String | (Reddit only) Subreddit name
        Integer limit = 25; // Integer | Maximum number of comments to return
        String cursor = "cursor_example"; // String | Pagination cursor, returned by a previous call as `pagination.cursor`. This is the platform's own opaque paging value passed through verbatim: never construct, decode or validate it client-side.
        String commentId = "commentId_example"; // String | (Reddit only) Get replies to a specific comment
        try {
            GetInboxPostComments200Response result = apiInstance.getInboxPostComments(postId, accountId, subreddit, limit, cursor, commentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#getInboxPostComments");
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
| **postId** | **String**| Zernio post ID or platform-specific post ID. Zernio IDs are auto-resolved. LinkedIn third-party posts accept full activity URN or numeric ID. On Facebook and Instagram, a comment ID is also accepted here and returns that comment&#39;s replies. | |
| **accountId** | **String**|  | |
| **subreddit** | **String**| (Reddit only) Subreddit name | [optional] |
| **limit** | **Integer**| Maximum number of comments to return | [optional] [default to 25] |
| **cursor** | **String**| Pagination cursor, returned by a previous call as &#x60;pagination.cursor&#x60;. This is the platform&#39;s own opaque paging value passed through verbatim: never construct, decode or validate it client-side. | [optional] |
| **commentId** | **String**| (Reddit only) Get replies to a specific comment | [optional] |

### Return type

[**GetInboxPostComments200Response**](GetInboxPostComments200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments for the post |  -  |
| **400** | Invalid request, or the postId belongs to a Meta ad creative / ad ID rather than an organic post (code USE_AD_COMMENTS_ENDPOINT — response includes &#x60;adId&#x60; and &#x60;adCommentsUrl&#x60;).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the connected account is not permitted to read this post on the platform (code platform_api_error, type platform_error) |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | Upstream platform error (code platform_api_error, type platform_error) |  -  |

## getInboxPostCommentsWithHttpInfo

> ApiResponse<GetInboxPostComments200Response> getInboxPostComments getInboxPostCommentsWithHttpInfo(postId, accountId, subreddit, limit, cursor, commentId)

Get post comments

Fetch comments for a specific post. Requires accountId query parameter.  On Facebook and Instagram, passing a COMMENT id as &#x60;postId&#x60; is also supported and returns that comment&#39;s replies instead of the post&#39;s top-level comments. This is not available on YouTube, where &#x60;postId&#x60; must be a video id.  Responses are cached for up to 10 minutes, so a page may lag new comments by that window. Do not poll this endpoint for real-time updates: subscribe to the &#x60;comment.received&#x60; webhook, which delivers new comments as they arrive. Your own writes (creating, replying to, or deleting a comment) refresh the cache immediately. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or platform-specific post ID. Zernio IDs are auto-resolved. LinkedIn third-party posts accept full activity URN or numeric ID. On Facebook and Instagram, a comment ID is also accepted here and returns that comment's replies.
        String accountId = "accountId_example"; // String | 
        String subreddit = "subreddit_example"; // String | (Reddit only) Subreddit name
        Integer limit = 25; // Integer | Maximum number of comments to return
        String cursor = "cursor_example"; // String | Pagination cursor, returned by a previous call as `pagination.cursor`. This is the platform's own opaque paging value passed through verbatim: never construct, decode or validate it client-side.
        String commentId = "commentId_example"; // String | (Reddit only) Get replies to a specific comment
        try {
            ApiResponse<GetInboxPostComments200Response> response = apiInstance.getInboxPostCommentsWithHttpInfo(postId, accountId, subreddit, limit, cursor, commentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#getInboxPostComments");
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
| **postId** | **String**| Zernio post ID or platform-specific post ID. Zernio IDs are auto-resolved. LinkedIn third-party posts accept full activity URN or numeric ID. On Facebook and Instagram, a comment ID is also accepted here and returns that comment&#39;s replies. | |
| **accountId** | **String**|  | |
| **subreddit** | **String**| (Reddit only) Subreddit name | [optional] |
| **limit** | **Integer**| Maximum number of comments to return | [optional] [default to 25] |
| **cursor** | **String**| Pagination cursor, returned by a previous call as &#x60;pagination.cursor&#x60;. This is the platform&#39;s own opaque paging value passed through verbatim: never construct, decode or validate it client-side. | [optional] |
| **commentId** | **String**| (Reddit only) Get replies to a specific comment | [optional] |

### Return type

ApiResponse<[**GetInboxPostComments200Response**](GetInboxPostComments200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments for the post |  -  |
| **400** | Invalid request, or the postId belongs to a Meta ad creative / ad ID rather than an organic post (code USE_AD_COMMENTS_ENDPOINT — response includes &#x60;adId&#x60; and &#x60;adCommentsUrl&#x60;).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the connected account is not permitted to read this post on the platform (code platform_api_error, type platform_error) |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | Upstream platform error (code platform_api_error, type platform_error) |  -  |


## hideInboxComment

> HideInboxComment200Response hideInboxComment(postId, commentId, hideInboxCommentRequest)

Hide comment

Hide a comment on a post. Supported by Facebook, Instagram, Threads, and X/Twitter. Hidden comments are only visible to the commenter and page admin. For X/Twitter, the reply must belong to a conversation started by the authenticated user. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        HideInboxCommentRequest hideInboxCommentRequest = new HideInboxCommentRequest(); // HideInboxCommentRequest | 
        try {
            HideInboxComment200Response result = apiInstance.hideInboxComment(postId, commentId, hideInboxCommentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#hideInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **hideInboxCommentRequest** | [**HideInboxCommentRequest**](HideInboxCommentRequest.md)|  | |

### Return type

[**HideInboxComment200Response**](HideInboxComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment hidden |  -  |
| **400** | Platform does not support hiding comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## hideInboxCommentWithHttpInfo

> ApiResponse<HideInboxComment200Response> hideInboxComment hideInboxCommentWithHttpInfo(postId, commentId, hideInboxCommentRequest)

Hide comment

Hide a comment on a post. Supported by Facebook, Instagram, Threads, and X/Twitter. Hidden comments are only visible to the commenter and page admin. For X/Twitter, the reply must belong to a conversation started by the authenticated user. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        HideInboxCommentRequest hideInboxCommentRequest = new HideInboxCommentRequest(); // HideInboxCommentRequest | 
        try {
            ApiResponse<HideInboxComment200Response> response = apiInstance.hideInboxCommentWithHttpInfo(postId, commentId, hideInboxCommentRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#hideInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **hideInboxCommentRequest** | [**HideInboxCommentRequest**](HideInboxCommentRequest.md)|  | |

### Return type

ApiResponse<[**HideInboxComment200Response**](HideInboxComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment hidden |  -  |
| **400** | Platform does not support hiding comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## likeInboxComment

> LikeInboxComment200Response likeInboxComment(postId, commentId, likeInboxCommentRequest)

Like comment

Like or upvote a comment on a post. Supported platforms: Facebook, Twitter/X, Bluesky, Reddit, LinkedIn, and Instagram in limited release (see below). For Bluesky, the cid (content identifier) is required in the request body. For LinkedIn, pass the composite comment URN returned by the comments endpoints as commentId; an optional reactionType picks the reaction (defaults to LIKE), and accounts connected before the social-feed scopes were requested get a 403 with code &#x60;linkedin_reconnect_required&#x60;.  Instagram is in LIMITED RELEASE and not generally available: the call needs &#x60;instagram_manage_engagement&#x60;, which Meta has so far granted this app only under Standard Access, so it works for app admins, developers and testers of our Meta app and returns a 403 with code &#x60;PLATFORM_BETA_RESTRICTED&#x60; for every other account. That restriction lifts when Meta App Review grants Advanced Access; the constraints below apply once it does.  Instagram covers comments and replies on feed posts, reels and carousels. Only an account connected through Facebook Login can be granted &#x60;instagram_manage_engagement&#x60;: an Instagram Login connection returns a 400 with code &#x60;instagram_likes_require_facebook_login&#x60;, and an account whose token predates the permission returns a 403 with code &#x60;reconnect_required&#x60;. Content from private accounts cannot be liked. Instagram also enforces a burst limit of 50 like or unlike calls per 5 seconds per Instagram account, and exceeding it locks that account out of the like API for an hour, so pace bulk loops. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        LikeInboxCommentRequest likeInboxCommentRequest = new LikeInboxCommentRequest(); // LikeInboxCommentRequest | 
        try {
            LikeInboxComment200Response result = apiInstance.likeInboxComment(postId, commentId, likeInboxCommentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#likeInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **likeInboxCommentRequest** | [**LikeInboxCommentRequest**](LikeInboxCommentRequest.md)|  | |

### Return type

[**LikeInboxComment200Response**](LikeInboxComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment liked |  -  |
| **400** | Platform does not support liking comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform permission |  -  |

## likeInboxCommentWithHttpInfo

> ApiResponse<LikeInboxComment200Response> likeInboxComment likeInboxCommentWithHttpInfo(postId, commentId, likeInboxCommentRequest)

Like comment

Like or upvote a comment on a post. Supported platforms: Facebook, Twitter/X, Bluesky, Reddit, LinkedIn, and Instagram in limited release (see below). For Bluesky, the cid (content identifier) is required in the request body. For LinkedIn, pass the composite comment URN returned by the comments endpoints as commentId; an optional reactionType picks the reaction (defaults to LIKE), and accounts connected before the social-feed scopes were requested get a 403 with code &#x60;linkedin_reconnect_required&#x60;.  Instagram is in LIMITED RELEASE and not generally available: the call needs &#x60;instagram_manage_engagement&#x60;, which Meta has so far granted this app only under Standard Access, so it works for app admins, developers and testers of our Meta app and returns a 403 with code &#x60;PLATFORM_BETA_RESTRICTED&#x60; for every other account. That restriction lifts when Meta App Review grants Advanced Access; the constraints below apply once it does.  Instagram covers comments and replies on feed posts, reels and carousels. Only an account connected through Facebook Login can be granted &#x60;instagram_manage_engagement&#x60;: an Instagram Login connection returns a 400 with code &#x60;instagram_likes_require_facebook_login&#x60;, and an account whose token predates the permission returns a 403 with code &#x60;reconnect_required&#x60;. Content from private accounts cannot be liked. Instagram also enforces a burst limit of 50 like or unlike calls per 5 seconds per Instagram account, and exceeding it locks that account out of the like API for an hour, so pace bulk loops. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        LikeInboxCommentRequest likeInboxCommentRequest = new LikeInboxCommentRequest(); // LikeInboxCommentRequest | 
        try {
            ApiResponse<LikeInboxComment200Response> response = apiInstance.likeInboxCommentWithHttpInfo(postId, commentId, likeInboxCommentRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#likeInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **likeInboxCommentRequest** | [**LikeInboxCommentRequest**](LikeInboxCommentRequest.md)|  | |

### Return type

ApiResponse<[**LikeInboxComment200Response**](LikeInboxComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment liked |  -  |
| **400** | Platform does not support liking comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform permission |  -  |


## likePost

> LikePost200Response likePost(postId, likePostRequest)

Like post

Like (or react to) a post as a connected account. Supported platforms: LinkedIn, Twitter/X, Facebook, YouTube, Bluesky, and Instagram in limited release (see below). Threads, TikTok and Pinterest expose no like endpoint in their APIs and return 400. Reddit returns 400 too, pointing at &#x60;POST /v1/accounts/{accountId}/reddit-vote&#x60;, which covers upvote, downvote and clear on both posts and comments.  The account does not have to be the one that published the post, which is what makes executive engagement possible: pass an exec&#39;s &#x60;accountId&#x60; and the brand post&#39;s ID. &#x60;postId&#x60; accepts either a Zernio post ID or the platform&#39;s native post ID. A Zernio post ID resolves to the entry for &#x60;accountId&#x60;, falling back to the post&#39;s single entry on the same platform (two entries on that platform is a 400, so pass the native ID).  LinkedIn requires the &#x60;w_member_social_feed&#x60; / &#x60;w_organization_social_feed&#x60; scopes, which are not retroactive: accounts connected before those were requested get a 403 with code &#x60;linkedin_reconnect_required&#x60; until the user reconnects the account. YouTube spends 50 quota units per call.  Instagram is in LIMITED RELEASE and not generally available: the call needs &#x60;instagram_manage_engagement&#x60;, which Meta has so far granted this app only under Standard Access, so it works for app admins, developers and testers of our Meta app and returns a 403 with code &#x60;PLATFORM_BETA_RESTRICTED&#x60; for every other account. That restriction lifts when Meta App Review grants Advanced Access; the constraints below apply once it does.  Instagram covers feed images, reels and carousels (stories and private-account media are not likeable). Only an account connected through Facebook Login can be granted &#x60;instagram_manage_engagement&#x60;: an Instagram Login connection returns a 400 with code &#x60;instagram_likes_require_facebook_login&#x60;, and an account whose token predates the permission returns a 403 with code &#x60;reconnect_required&#x60;. Instagram also enforces a burst limit of 50 like or unlike calls per 5 seconds per Instagram account, and exceeding it locks that account out of the like API for an hour, so pace bulk loops. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or the platform's native post ID
        LikePostRequest likePostRequest = new LikePostRequest(); // LikePostRequest | 
        try {
            LikePost200Response result = apiInstance.likePost(postId, likePostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#likePost");
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
| **postId** | **String**| Zernio post ID or the platform&#39;s native post ID | |
| **likePostRequest** | [**LikePostRequest**](LikePostRequest.md)|  | |

### Return type

[**LikePost200Response**](LikePost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post liked |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform scope |  -  |
| **404** | Account or post not found |  -  |

## likePostWithHttpInfo

> ApiResponse<LikePost200Response> likePost likePostWithHttpInfo(postId, likePostRequest)

Like post

Like (or react to) a post as a connected account. Supported platforms: LinkedIn, Twitter/X, Facebook, YouTube, Bluesky, and Instagram in limited release (see below). Threads, TikTok and Pinterest expose no like endpoint in their APIs and return 400. Reddit returns 400 too, pointing at &#x60;POST /v1/accounts/{accountId}/reddit-vote&#x60;, which covers upvote, downvote and clear on both posts and comments.  The account does not have to be the one that published the post, which is what makes executive engagement possible: pass an exec&#39;s &#x60;accountId&#x60; and the brand post&#39;s ID. &#x60;postId&#x60; accepts either a Zernio post ID or the platform&#39;s native post ID. A Zernio post ID resolves to the entry for &#x60;accountId&#x60;, falling back to the post&#39;s single entry on the same platform (two entries on that platform is a 400, so pass the native ID).  LinkedIn requires the &#x60;w_member_social_feed&#x60; / &#x60;w_organization_social_feed&#x60; scopes, which are not retroactive: accounts connected before those were requested get a 403 with code &#x60;linkedin_reconnect_required&#x60; until the user reconnects the account. YouTube spends 50 quota units per call.  Instagram is in LIMITED RELEASE and not generally available: the call needs &#x60;instagram_manage_engagement&#x60;, which Meta has so far granted this app only under Standard Access, so it works for app admins, developers and testers of our Meta app and returns a 403 with code &#x60;PLATFORM_BETA_RESTRICTED&#x60; for every other account. That restriction lifts when Meta App Review grants Advanced Access; the constraints below apply once it does.  Instagram covers feed images, reels and carousels (stories and private-account media are not likeable). Only an account connected through Facebook Login can be granted &#x60;instagram_manage_engagement&#x60;: an Instagram Login connection returns a 400 with code &#x60;instagram_likes_require_facebook_login&#x60;, and an account whose token predates the permission returns a 403 with code &#x60;reconnect_required&#x60;. Instagram also enforces a burst limit of 50 like or unlike calls per 5 seconds per Instagram account, and exceeding it locks that account out of the like API for an hour, so pace bulk loops. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or the platform's native post ID
        LikePostRequest likePostRequest = new LikePostRequest(); // LikePostRequest | 
        try {
            ApiResponse<LikePost200Response> response = apiInstance.likePostWithHttpInfo(postId, likePostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#likePost");
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
| **postId** | **String**| Zernio post ID or the platform&#39;s native post ID | |
| **likePostRequest** | [**LikePostRequest**](LikePostRequest.md)|  | |

### Return type

ApiResponse<[**LikePost200Response**](LikePost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post liked |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform scope |  -  |
| **404** | Account or post not found |  -  |


## listInboxComments

> ListInboxComments200Response listInboxComments(profileId, platform, minComments, since, sortBy, sortOrder, limit, cursor, accountId)

List commented posts

Returns posts with comment counts from all connected accounts. Aggregates data across multiple accounts.  Responses are cached for up to 10 minutes, so the feed may lag new comments by that window. Do not poll this endpoint for real-time updates: subscribe to the &#x60;comment.received&#x60; webhook, which fires for every new comment across your posts and carries the post reference needed to keep this list current.  For users with the Ads add-on (Metronome plans always qualify), the user&#39;s Meta ads (boosted/dark posts) are included too. There&#39;s one row per (ad, placement-with-comments): an ad that runs on both Facebook feed and Instagram feed produces up to two rows (the Page dark post and the IG media have separate comment threads), each flagged &#x60;isAd: true&#x60; with &#x60;adId&#x60; and &#x60;placement&#x60; (&#x60;id&#x60; is &#x60;{adId}:{placement}&#x60;). Use &#x60;?platform&#x3D;metaads&#x60; to return *only* ad rows; passing &#x60;facebook&#x60;/&#x60;instagram&#x60; returns *organic* posts only (no ads); omitting &#x60;platform&#x60; returns both. Fetch a row&#39;s thread from GET /v1/ads/{adId}/comments?placement&#x3D;{placement}. Ad comment counts are read with the Marketing API token (Facebook side) or the connected Instagram account&#39;s token (Instagram side); a row whose count can&#39;t be read is omitted.  Pagination walks each account&#39;s platform listing. Following &#x60;nextCursor&#x60; reaches past the first page on Facebook, Instagram, Threads, LinkedIn and YouTube, since they are the platforms that support a server-side date window; on the others the listing stops at its first page. Cursor pagination is only coherent for the default sort (&#x60;sortBy&#x3D;date&#x60;, &#x60;sortOrder&#x3D;desc&#x60;): with &#x60;sortOrder&#x3D;asc&#x60;, or with &#x60;sortBy&#x3D;comments&#x60;, the cursor filter does not match the sort order and the second page is unreliable.  &#x60;nextCursor&#x60; is opaque: pass it back verbatim, never construct or parse it, its composition may change without notice. Because each page re-queries a live window, results can still shift between requests, so dedupe by &#x60;id&#x60; on the client.  &#x60;commentCount&#x60; semantics differ by platform: YouTube&#39;s includes replies, Facebook&#39;s counts top-level comments only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile ID
        String platform = "facebook"; // String | Filter by platform. `metaads` is a synthetic value meaning the user's ads (boosted/dark posts) only; `facebook`/`instagram` return organic posts only.
        Integer minComments = 56; // Integer | Minimum comment count
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Posts created after this date
        String sortBy = "date"; // String | Sort field
        String sortOrder = "asc"; // String | Sort order
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | 
        String accountId = "accountId_example"; // String | Filter by specific social account ID
        try {
            ListInboxComments200Response result = apiInstance.listInboxComments(profileId, platform, minComments, since, sortBy, sortOrder, limit, cursor, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#listInboxComments");
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
| **profileId** | **String**| Filter by profile ID | [optional] |
| **platform** | **String**| Filter by platform. &#x60;metaads&#x60; is a synthetic value meaning the user&#39;s ads (boosted/dark posts) only; &#x60;facebook&#x60;/&#x60;instagram&#x60; return organic posts only. | [optional] [enum: facebook, instagram, twitter, bluesky, threads, youtube, linkedin, reddit, metaads] |
| **minComments** | **Integer**| Minimum comment count | [optional] |
| **since** | **OffsetDateTime**| Posts created after this date | [optional] |
| **sortBy** | **String**| Sort field | [optional] [default to date] [enum: date, comments] |
| **sortOrder** | **String**| Sort order | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**|  | [optional] |
| **accountId** | **String**| Filter by specific social account ID | [optional] |

### Return type

[**ListInboxComments200Response**](ListInboxComments200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated posts with comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## listInboxCommentsWithHttpInfo

> ApiResponse<ListInboxComments200Response> listInboxComments listInboxCommentsWithHttpInfo(profileId, platform, minComments, since, sortBy, sortOrder, limit, cursor, accountId)

List commented posts

Returns posts with comment counts from all connected accounts. Aggregates data across multiple accounts.  Responses are cached for up to 10 minutes, so the feed may lag new comments by that window. Do not poll this endpoint for real-time updates: subscribe to the &#x60;comment.received&#x60; webhook, which fires for every new comment across your posts and carries the post reference needed to keep this list current.  For users with the Ads add-on (Metronome plans always qualify), the user&#39;s Meta ads (boosted/dark posts) are included too. There&#39;s one row per (ad, placement-with-comments): an ad that runs on both Facebook feed and Instagram feed produces up to two rows (the Page dark post and the IG media have separate comment threads), each flagged &#x60;isAd: true&#x60; with &#x60;adId&#x60; and &#x60;placement&#x60; (&#x60;id&#x60; is &#x60;{adId}:{placement}&#x60;). Use &#x60;?platform&#x3D;metaads&#x60; to return *only* ad rows; passing &#x60;facebook&#x60;/&#x60;instagram&#x60; returns *organic* posts only (no ads); omitting &#x60;platform&#x60; returns both. Fetch a row&#39;s thread from GET /v1/ads/{adId}/comments?placement&#x3D;{placement}. Ad comment counts are read with the Marketing API token (Facebook side) or the connected Instagram account&#39;s token (Instagram side); a row whose count can&#39;t be read is omitted.  Pagination walks each account&#39;s platform listing. Following &#x60;nextCursor&#x60; reaches past the first page on Facebook, Instagram, Threads, LinkedIn and YouTube, since they are the platforms that support a server-side date window; on the others the listing stops at its first page. Cursor pagination is only coherent for the default sort (&#x60;sortBy&#x3D;date&#x60;, &#x60;sortOrder&#x3D;desc&#x60;): with &#x60;sortOrder&#x3D;asc&#x60;, or with &#x60;sortBy&#x3D;comments&#x60;, the cursor filter does not match the sort order and the second page is unreliable.  &#x60;nextCursor&#x60; is opaque: pass it back verbatim, never construct or parse it, its composition may change without notice. Because each page re-queries a live window, results can still shift between requests, so dedupe by &#x60;id&#x60; on the client.  &#x60;commentCount&#x60; semantics differ by platform: YouTube&#39;s includes replies, Facebook&#39;s counts top-level comments only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile ID
        String platform = "facebook"; // String | Filter by platform. `metaads` is a synthetic value meaning the user's ads (boosted/dark posts) only; `facebook`/`instagram` return organic posts only.
        Integer minComments = 56; // Integer | Minimum comment count
        OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Posts created after this date
        String sortBy = "date"; // String | Sort field
        String sortOrder = "asc"; // String | Sort order
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | 
        String accountId = "accountId_example"; // String | Filter by specific social account ID
        try {
            ApiResponse<ListInboxComments200Response> response = apiInstance.listInboxCommentsWithHttpInfo(profileId, platform, minComments, since, sortBy, sortOrder, limit, cursor, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#listInboxComments");
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
| **profileId** | **String**| Filter by profile ID | [optional] |
| **platform** | **String**| Filter by platform. &#x60;metaads&#x60; is a synthetic value meaning the user&#39;s ads (boosted/dark posts) only; &#x60;facebook&#x60;/&#x60;instagram&#x60; return organic posts only. | [optional] [enum: facebook, instagram, twitter, bluesky, threads, youtube, linkedin, reddit, metaads] |
| **minComments** | **Integer**| Minimum comment count | [optional] |
| **since** | **OffsetDateTime**| Posts created after this date | [optional] |
| **sortBy** | **String**| Sort field | [optional] [default to date] [enum: date, comments] |
| **sortOrder** | **String**| Sort order | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**|  | [optional] |
| **accountId** | **String**| Filter by specific social account ID | [optional] |

### Return type

ApiResponse<[**ListInboxComments200Response**](ListInboxComments200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated posts with comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## replyToInboxPost

> ReplyToInboxPost200Response replyToInboxPost(postId, replyToInboxPostRequest, idempotencyKey)

Reply to comment

Post a reply to a post or specific comment. Requires accountId in request body.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe (e.g. after a client-side timeout where delivery is unknown): same key + same body replays the original response (with &#x60;Idempotent-Replayed: true&#x60;) instead of posting the comment a second time; same key + different body returns 422; a key still in flight returns 409. Keys are retained for 24 hours and are scoped to the credential and to this exact path, so reusing a key against a different postId returns 422 rather than replaying the other post&#39;s response.  Only successful (2xx) responses are stored for replay. If the request throws or returns a non-2xx status the key is released, so the header protects the \&quot;request succeeded but the response was lost\&quot; case. After an ambiguous failure (a 5xx or a network timeout) list the post&#39;s comments before retrying with the same key, and treat an empty result as inconclusive rather than as proof nothing was posted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID.
        ReplyToInboxPostRequest replyToInboxPostRequest = new ReplyToInboxPostRequest(); // ReplyToInboxPostRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ReplyToInboxPost200Response result = apiInstance.replyToInboxPost(postId, replyToInboxPostRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#replyToInboxPost");
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
| **postId** | **String**| Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID. | |
| **replyToInboxPostRequest** | [**ReplyToInboxPostRequest**](ReplyToInboxPostRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**ReplyToInboxPost200Response**](ReplyToInboxPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reply posted |  -  |
| **400** | Invalid request (e.g. attachmentUrl on a platform other than Facebook, code PLATFORM_NOT_SUPPORTED) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the connected account is not permitted to comment on this post on the platform (code platform_api_error, type platform_error) |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | Upstream platform error (code platform_api_error, type platform_error) |  -  |

## replyToInboxPostWithHttpInfo

> ApiResponse<ReplyToInboxPost200Response> replyToInboxPost replyToInboxPostWithHttpInfo(postId, replyToInboxPostRequest, idempotencyKey)

Reply to comment

Post a reply to a post or specific comment. Requires accountId in request body.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe (e.g. after a client-side timeout where delivery is unknown): same key + same body replays the original response (with &#x60;Idempotent-Replayed: true&#x60;) instead of posting the comment a second time; same key + different body returns 422; a key still in flight returns 409. Keys are retained for 24 hours and are scoped to the credential and to this exact path, so reusing a key against a different postId returns 422 rather than replaying the other post&#39;s response.  Only successful (2xx) responses are stored for replay. If the request throws or returns a non-2xx status the key is released, so the header protects the \&quot;request succeeded but the response was lost\&quot; case. After an ambiguous failure (a 5xx or a network timeout) list the post&#39;s comments before retrying with the same key, and treat an empty result as inconclusive rather than as proof nothing was posted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID.
        ReplyToInboxPostRequest replyToInboxPostRequest = new ReplyToInboxPostRequest(); // ReplyToInboxPostRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<ReplyToInboxPost200Response> response = apiInstance.replyToInboxPostWithHttpInfo(postId, replyToInboxPostRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#replyToInboxPost");
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
| **postId** | **String**| Zernio post ID or platform-specific post ID. LinkedIn third-party posts accept full activity URN or numeric ID. | |
| **replyToInboxPostRequest** | [**ReplyToInboxPostRequest**](ReplyToInboxPostRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**ReplyToInboxPost200Response**](ReplyToInboxPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reply posted |  -  |
| **400** | Invalid request (e.g. attachmentUrl on a platform other than Facebook, code PLATFORM_NOT_SUPPORTED) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the connected account is not permitted to comment on this post on the platform (code platform_api_error, type platform_error) |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | Upstream platform error (code platform_api_error, type platform_error) |  -  |


## sendPrivateReplyToComment

> SendPrivateReplyToComment200Response sendPrivateReplyToComment(postId, commentId, sendPrivateReplyToCommentRequest)

Send private reply

Send a private message to the author of a comment. Supported on Instagram and Facebook only. One reply per comment, must be sent within 7 days. Optionally attach interactive elements: &#x60;quickReplies&#x60; (chips above the keyboard, max 13) or &#x60;buttons&#x60; (1-3 inline postback/url buttons rendered in the same bubble via Meta&#39;s button_template). Buttons are recommended for cold reach since chips do not render in the Instagram Message Requests folder. &#x60;quickReplies&#x60; and &#x60;buttons&#x60; are mutually exclusive. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | The media/post ID (Instagram media ID or Facebook post ID)
        String commentId = "commentId_example"; // String | The comment ID to send a private reply to
        SendPrivateReplyToCommentRequest sendPrivateReplyToCommentRequest = new SendPrivateReplyToCommentRequest(); // SendPrivateReplyToCommentRequest | 
        try {
            SendPrivateReplyToComment200Response result = apiInstance.sendPrivateReplyToComment(postId, commentId, sendPrivateReplyToCommentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#sendPrivateReplyToComment");
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
| **postId** | **String**| The media/post ID (Instagram media ID or Facebook post ID) | |
| **commentId** | **String**| The comment ID to send a private reply to | |
| **sendPrivateReplyToCommentRequest** | [**SendPrivateReplyToCommentRequest**](SendPrivateReplyToCommentRequest.md)|  | |

### Return type

[**SendPrivateReplyToComment200Response**](SendPrivateReplyToComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Private reply sent successfully |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |

## sendPrivateReplyToCommentWithHttpInfo

> ApiResponse<SendPrivateReplyToComment200Response> sendPrivateReplyToComment sendPrivateReplyToCommentWithHttpInfo(postId, commentId, sendPrivateReplyToCommentRequest)

Send private reply

Send a private message to the author of a comment. Supported on Instagram and Facebook only. One reply per comment, must be sent within 7 days. Optionally attach interactive elements: &#x60;quickReplies&#x60; (chips above the keyboard, max 13) or &#x60;buttons&#x60; (1-3 inline postback/url buttons rendered in the same bubble via Meta&#39;s button_template). Buttons are recommended for cold reach since chips do not render in the Instagram Message Requests folder. &#x60;quickReplies&#x60; and &#x60;buttons&#x60; are mutually exclusive. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | The media/post ID (Instagram media ID or Facebook post ID)
        String commentId = "commentId_example"; // String | The comment ID to send a private reply to
        SendPrivateReplyToCommentRequest sendPrivateReplyToCommentRequest = new SendPrivateReplyToCommentRequest(); // SendPrivateReplyToCommentRequest | 
        try {
            ApiResponse<SendPrivateReplyToComment200Response> response = apiInstance.sendPrivateReplyToCommentWithHttpInfo(postId, commentId, sendPrivateReplyToCommentRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#sendPrivateReplyToComment");
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
| **postId** | **String**| The media/post ID (Instagram media ID or Facebook post ID) | |
| **commentId** | **String**| The comment ID to send a private reply to | |
| **sendPrivateReplyToCommentRequest** | [**SendPrivateReplyToCommentRequest**](SendPrivateReplyToCommentRequest.md)|  | |

### Return type

ApiResponse<[**SendPrivateReplyToComment200Response**](SendPrivateReplyToComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Private reply sent successfully |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |


## setCommentModeration

> UpdateYoutubeDefaultPlaylist200Response setCommentModeration(postId, commentId, setCommentModerationRequest)

Set comment moderation status

Set a comment&#39;s moderation status. Supported on YouTube only.  Use this to work a moderation queue: approve a held comment (&#x60;published&#x60;), reject it (&#x60;rejected&#x60;), or send it back for review (&#x60;heldForReview&#x60;).  The request must be authorized by the owner of the channel or video the comment belongs to. You cannot moderate comments on videos you do not own.  This is distinct from &#x60;POST /v1/inbox/comments/{postId}/{commentId}/hide&#x60;, which covers Facebook, Instagram, Threads, and X/Twitter and does not apply to YouTube. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        SetCommentModerationRequest setCommentModerationRequest = new SetCommentModerationRequest(); // SetCommentModerationRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.setCommentModeration(postId, commentId, setCommentModerationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#setCommentModeration");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **setCommentModerationRequest** | [**SetCommentModerationRequest**](SetCommentModerationRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Moderation status applied |  -  |
| **400** | Platform does not support comment moderation (code: platform_not_supported), or banAuthor was set without moderationStatus&#x3D;rejected. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |
| **502** | YouTube rejected the request (e.g. the account does not own the video). |  -  |

## setCommentModerationWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> setCommentModeration setCommentModerationWithHttpInfo(postId, commentId, setCommentModerationRequest)

Set comment moderation status

Set a comment&#39;s moderation status. Supported on YouTube only.  Use this to work a moderation queue: approve a held comment (&#x60;published&#x60;), reject it (&#x60;rejected&#x60;), or send it back for review (&#x60;heldForReview&#x60;).  The request must be authorized by the owner of the channel or video the comment belongs to. You cannot moderate comments on videos you do not own.  This is distinct from &#x60;POST /v1/inbox/comments/{postId}/{commentId}/hide&#x60;, which covers Facebook, Instagram, Threads, and X/Twitter and does not apply to YouTube. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        SetCommentModerationRequest setCommentModerationRequest = new SetCommentModerationRequest(); // SetCommentModerationRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.setCommentModerationWithHttpInfo(postId, commentId, setCommentModerationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#setCommentModeration");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **setCommentModerationRequest** | [**SetCommentModerationRequest**](SetCommentModerationRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Moderation status applied |  -  |
| **400** | Platform does not support comment moderation (code: platform_not_supported), or banAuthor was set without moderationStatus&#x3D;rejected. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |
| **502** | YouTube rejected the request (e.g. the account does not own the video). |  -  |


## unhideInboxComment

> HideInboxComment200Response unhideInboxComment(postId, commentId, accountId)

Unhide comment

Unhide a previously hidden comment. Supported by Facebook, Instagram, Threads, and X/Twitter. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            HideInboxComment200Response result = apiInstance.unhideInboxComment(postId, commentId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#unhideInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**HideInboxComment200Response**](HideInboxComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment unhidden |  -  |
| **400** | Platform does not support unhiding comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## unhideInboxCommentWithHttpInfo

> ApiResponse<HideInboxComment200Response> unhideInboxComment unhideInboxCommentWithHttpInfo(postId, commentId, accountId)

Unhide comment

Unhide a previously hidden comment. Supported by Facebook, Instagram, Threads, and X/Twitter. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<HideInboxComment200Response> response = apiInstance.unhideInboxCommentWithHttpInfo(postId, commentId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#unhideInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**HideInboxComment200Response**](HideInboxComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment unhidden |  -  |
| **400** | Platform does not support unhiding comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## unlikeInboxComment

> UnlikeInboxComment200Response unlikeInboxComment(postId, commentId, accountId, likeUri)

Unlike comment

Remove a like from a comment. Supported platforms: Facebook, Twitter/X, Bluesky, Reddit, LinkedIn, and Instagram in limited release. For Bluesky, the likeUri query parameter is required. Instagram has the same limited release, Facebook Login, &#x60;instagram_manage_engagement&#x60; and burst-limit constraints as liking. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String likeUri = "likeUri_example"; // String | (Bluesky only) The like URI returned when liking
        try {
            UnlikeInboxComment200Response result = apiInstance.unlikeInboxComment(postId, commentId, accountId, likeUri);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#unlikeInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **accountId** | **String**|  | |
| **likeUri** | **String**| (Bluesky only) The like URI returned when liking | [optional] |

### Return type

[**UnlikeInboxComment200Response**](UnlikeInboxComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment unliked |  -  |
| **400** | Platform does not support unliking comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform permission |  -  |

## unlikeInboxCommentWithHttpInfo

> ApiResponse<UnlikeInboxComment200Response> unlikeInboxComment unlikeInboxCommentWithHttpInfo(postId, commentId, accountId, likeUri)

Unlike comment

Remove a like from a comment. Supported platforms: Facebook, Twitter/X, Bluesky, Reddit, LinkedIn, and Instagram in limited release. For Bluesky, the likeUri query parameter is required. Instagram has the same limited release, Facebook Login, &#x60;instagram_manage_engagement&#x60; and burst-limit constraints as liking. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | 
        String commentId = "commentId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String likeUri = "likeUri_example"; // String | (Bluesky only) The like URI returned when liking
        try {
            ApiResponse<UnlikeInboxComment200Response> response = apiInstance.unlikeInboxCommentWithHttpInfo(postId, commentId, accountId, likeUri);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#unlikeInboxComment");
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
| **postId** | **String**|  | |
| **commentId** | **String**|  | |
| **accountId** | **String**|  | |
| **likeUri** | **String**| (Bluesky only) The like URI returned when liking | [optional] |

### Return type

ApiResponse<[**UnlikeInboxComment200Response**](UnlikeInboxComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment unliked |  -  |
| **400** | Platform does not support unliking comments |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform permission |  -  |


## unlikePost

> UnlikePost200Response unlikePost(postId, accountId, likeUri)

Unlike post

Remove this account&#39;s like from a post. Supported platforms: LinkedIn, Twitter/X, Facebook, YouTube, Bluesky, and Instagram in limited release. On YouTube this clears the rating. Instagram has the same limited release, Facebook Login, &#x60;instagram_manage_engagement&#x60; and burst-limit constraints as liking. For Bluesky, &#x60;likeUri&#x60; (returned when the post was liked) is required. Reddit uses &#x60;POST /v1/accounts/{accountId}/reddit-vote&#x60; with &#x60;direction: 0&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or the platform's native post ID
        String accountId = "accountId_example"; // String | 
        String likeUri = "likeUri_example"; // String | (Bluesky only) The like URI returned when liking
        try {
            UnlikePost200Response result = apiInstance.unlikePost(postId, accountId, likeUri);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#unlikePost");
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
| **postId** | **String**| Zernio post ID or the platform&#39;s native post ID | |
| **accountId** | **String**|  | |
| **likeUri** | **String**| (Bluesky only) The like URI returned when liking | [optional] |

### Return type

[**UnlikePost200Response**](UnlikePost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post unliked |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform scope |  -  |
| **404** | Account or post not found |  -  |

## unlikePostWithHttpInfo

> ApiResponse<UnlikePost200Response> unlikePost unlikePostWithHttpInfo(postId, accountId, likeUri)

Unlike post

Remove this account&#39;s like from a post. Supported platforms: LinkedIn, Twitter/X, Facebook, YouTube, Bluesky, and Instagram in limited release. On YouTube this clears the rating. Instagram has the same limited release, Facebook Login, &#x60;instagram_manage_engagement&#x60; and burst-limit constraints as liking. For Bluesky, &#x60;likeUri&#x60; (returned when the post was liked) is required. Reddit uses &#x60;POST /v1/accounts/{accountId}/reddit-vote&#x60; with &#x60;direction: 0&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentsApi apiInstance = new CommentsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID or the platform's native post ID
        String accountId = "accountId_example"; // String | 
        String likeUri = "likeUri_example"; // String | (Bluesky only) The like URI returned when liking
        try {
            ApiResponse<UnlikePost200Response> response = apiInstance.unlikePostWithHttpInfo(postId, accountId, likeUri);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentsApi#unlikePost");
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
| **postId** | **String**| Zernio post ID or the platform&#39;s native post ID | |
| **accountId** | **String**|  | |
| **likeUri** | **String**| (Bluesky only) The like URI returned when liking | [optional] |

### Return type

ApiResponse<[**UnlikePost200Response**](UnlikePost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post unliked |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required, or the account is missing the platform scope |  -  |
| **404** | Account or post not found |  -  |

