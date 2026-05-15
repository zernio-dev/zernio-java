# PostsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkUploadPosts**](PostsApi.md#bulkUploadPosts) | **POST** /v1/posts/bulk-upload | Bulk upload from CSV |
| [**bulkUploadPostsWithHttpInfo**](PostsApi.md#bulkUploadPostsWithHttpInfo) | **POST** /v1/posts/bulk-upload | Bulk upload from CSV |
| [**createPost**](PostsApi.md#createPost) | **POST** /v1/posts | Create post |
| [**createPostWithHttpInfo**](PostsApi.md#createPostWithHttpInfo) | **POST** /v1/posts | Create post |
| [**deletePost**](PostsApi.md#deletePost) | **DELETE** /v1/posts/{postId} | Delete post |
| [**deletePostWithHttpInfo**](PostsApi.md#deletePostWithHttpInfo) | **DELETE** /v1/posts/{postId} | Delete post |
| [**editPost**](PostsApi.md#editPost) | **POST** /v1/posts/{postId}/edit | Edit published post |
| [**editPostWithHttpInfo**](PostsApi.md#editPostWithHttpInfo) | **POST** /v1/posts/{postId}/edit | Edit published post |
| [**getPost**](PostsApi.md#getPost) | **GET** /v1/posts/{postId} | Get post |
| [**getPostWithHttpInfo**](PostsApi.md#getPostWithHttpInfo) | **GET** /v1/posts/{postId} | Get post |
| [**listPosts**](PostsApi.md#listPosts) | **GET** /v1/posts | List posts |
| [**listPostsWithHttpInfo**](PostsApi.md#listPostsWithHttpInfo) | **GET** /v1/posts | List posts |
| [**retryPost**](PostsApi.md#retryPost) | **POST** /v1/posts/{postId}/retry | Retry failed post |
| [**retryPostWithHttpInfo**](PostsApi.md#retryPostWithHttpInfo) | **POST** /v1/posts/{postId}/retry | Retry failed post |
| [**unpublishPost**](PostsApi.md#unpublishPost) | **POST** /v1/posts/{postId}/unpublish | Unpublish post |
| [**unpublishPostWithHttpInfo**](PostsApi.md#unpublishPostWithHttpInfo) | **POST** /v1/posts/{postId}/unpublish | Unpublish post |
| [**updatePost**](PostsApi.md#updatePost) | **PUT** /v1/posts/{postId} | Update post |
| [**updatePostWithHttpInfo**](PostsApi.md#updatePostWithHttpInfo) | **PUT** /v1/posts/{postId} | Update post |
| [**updatePostMetadata**](PostsApi.md#updatePostMetadata) | **POST** /v1/posts/{postId}/update-metadata | Update post metadata |
| [**updatePostMetadataWithHttpInfo**](PostsApi.md#updatePostMetadataWithHttpInfo) | **POST** /v1/posts/{postId}/update-metadata | Update post metadata |



## bulkUploadPosts

> BulkUploadPosts200Response bulkUploadPosts(dryRun, _file)

Bulk upload from CSV

Create multiple posts by uploading a CSV file. Use dryRun&#x3D;true to validate without creating posts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        Boolean dryRun = false; // Boolean | 
        File _file = new File("/path/to/file"); // File | 
        try {
            BulkUploadPosts200Response result = apiInstance.bulkUploadPosts(dryRun, _file);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#bulkUploadPosts");
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
| **dryRun** | **Boolean**|  | [optional] [default to false] |
| **_file** | **File**|  | [optional] |

### Return type

[**BulkUploadPosts200Response**](BulkUploadPosts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bulk upload results |  -  |
| **207** | Partial success |  -  |
| **400** | Invalid CSV or validation errors |  -  |
| **401** | Unauthorized |  -  |
| **429** | Rate limit exceeded. Possible causes: API rate limit (requests per minute) or account cooldown (one or more accounts for platforms specified in the CSV are temporarily rate-limited).  |  -  |

## bulkUploadPostsWithHttpInfo

> ApiResponse<BulkUploadPosts200Response> bulkUploadPosts bulkUploadPostsWithHttpInfo(dryRun, _file)

Bulk upload from CSV

Create multiple posts by uploading a CSV file. Use dryRun&#x3D;true to validate without creating posts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        Boolean dryRun = false; // Boolean | 
        File _file = new File("/path/to/file"); // File | 
        try {
            ApiResponse<BulkUploadPosts200Response> response = apiInstance.bulkUploadPostsWithHttpInfo(dryRun, _file);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#bulkUploadPosts");
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
| **dryRun** | **Boolean**|  | [optional] [default to false] |
| **_file** | **File**|  | [optional] |

### Return type

ApiResponse<[**BulkUploadPosts200Response**](BulkUploadPosts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bulk upload results |  -  |
| **207** | Partial success |  -  |
| **400** | Invalid CSV or validation errors |  -  |
| **401** | Unauthorized |  -  |
| **429** | Rate limit exceeded. Possible causes: API rate limit (requests per minute) or account cooldown (one or more accounts for platforms specified in the CSV are temporarily rate-limited).  |  -  |


## createPost

> PostCreateResponse createPost(createPostRequest, xRequestId)

Create post

Create and optionally publish a post. Immediate posts (&#x60;publishNow: true&#x60;) include &#x60;platformPostUrl&#x60; in the response. Content is optional when media is attached or all platforms have &#x60;customContent&#x60;. See each platform&#39;s schema for media constraints.  ## Idempotency  Two layers of duplicate-protection apply, so safe-to-retry callers (network blips, n8n / Zapier retries, etc.) don&#39;t accidentally double-post.  **1. Same-request idempotency (5-minute window).** Pass an &#x60;x-request-id&#x60; header to mark a logical request. If a second request arrives with the same &#x60;x-request-id&#x60; while the first is in-flight (or within ~5 minutes of completion), we return **HTTP 200** with the original post in the &#x60;existingPost&#x60; field — no new post is created. The official Zernio SDKs auto-generate a unique &#x60;x-request-id&#x60; per call. If you&#39;re using a generic HTTP client (curl, n8n&#39;s HTTP node, Zapier, custom code), either: - Set a unique &#x60;x-request-id&#x60; per logical call (recommended — UUIDv4 is fine) - Or simply omit the header — we&#39;ll treat each request as new  **Common pitfall**: if your workflow tool uses a single execution-level request ID and reuses it across multiple HTTP nodes (e.g. one ID for the whole run, shared across 6 different platform calls), every call after the first will look like a retry of the first and return its post. Generate a fresh ID per node.  **2. Content-hash dedup (24-hour window).** Independently, we hash &#x60;(platform, accountId, content + media URLs)&#x60; and reject duplicates within 24 hours with **HTTP 409**. This catches genuine \&quot;same content posted twice to the same account\&quot; cases regardless of &#x60;x-request-id&#x60;. Returns &#x60;error&#x60;, &#x60;accountId&#x60;, &#x60;platform&#x60;, and &#x60;existingPostId&#x60; so you can find the original. To intentionally re-post identical content within 24h, change something (the caption, the media, the account) — the dedup is keyed on the full content fingerprint.  Order: same-&#x60;x-request-id&#x60; retries (200) are checked first; if no idempotency match, the content-hash dedup (409) runs. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        CreatePostRequest createPostRequest = new CreatePostRequest(); // CreatePostRequest | 
        UUID xRequestId = UUID.randomUUID(); // UUID | Optional client-generated request identifier for safe retry (idempotency). When two requests carry the same value, the second is treated as a retry of the first and returns the original post (HTTP 200) instead of creating a duplicate. Window is ~5 minutes from the first request. Generate a UUID per logical call. SDKs do this automatically; HTTP clients should set it themselves or omit it. See the operation description for the full idempotency contract. 
        try {
            PostCreateResponse result = apiInstance.createPost(createPostRequest, xRequestId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#createPost");
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
| **createPostRequest** | [**CreatePostRequest**](CreatePostRequest.md)|  | |
| **xRequestId** | **UUID**| Optional client-generated request identifier for safe retry (idempotency). When two requests carry the same value, the second is treated as a retry of the first and returns the original post (HTTP 200) instead of creating a duplicate. Window is ~5 minutes from the first request. Generate a UUID per logical call. SDKs do this automatically; HTTP clients should set it themselves or omit it. See the operation description for the full idempotency contract.  | [optional] |

### Return type

[**PostCreateResponse**](PostCreateResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Post created |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Duplicate content detected. Returned when the requested post matches an existing one on &#x60;(platform, accountId, content-hash)&#x60; within the last 24 hours, AND the request was NOT an &#x60;x-request-id&#x60; retry of an in-flight call. Distinct from same-&#x60;x-request-id&#x60; retries (which return HTTP 200 with the original post — see operation description for the idempotency contract).  Body fields: - &#x60;error&#x60; — human-readable message - &#x60;details.accountId&#x60; — the account that already has this content - &#x60;details.platform&#x60; — the platform that already has this content - &#x60;details.existingPostId&#x60; — Zernio &#x60;_id&#x60; of the original post  To intentionally re-post identical content within 24h, vary the content fingerprint (change the caption, swap a media item, or use a different account). To avoid 409s caused by retry loops, set a unique &#x60;x-request-id&#x60; per logical request — see &#x60;parameters.x-request-id&#x60; above.  |  -  |
| **429** | Rate limit exceeded. Possible causes: API rate limit, velocity limit (15 posts/hour per account), account cooldown, or daily platform limits. |  * Retry-After - Seconds until the rate limit resets (for API rate limits) <br>  * X-RateLimit-Limit - The rate limit ceiling <br>  * X-RateLimit-Remaining - Requests remaining in current window <br>  |

## createPostWithHttpInfo

> ApiResponse<PostCreateResponse> createPost createPostWithHttpInfo(createPostRequest, xRequestId)

Create post

Create and optionally publish a post. Immediate posts (&#x60;publishNow: true&#x60;) include &#x60;platformPostUrl&#x60; in the response. Content is optional when media is attached or all platforms have &#x60;customContent&#x60;. See each platform&#39;s schema for media constraints.  ## Idempotency  Two layers of duplicate-protection apply, so safe-to-retry callers (network blips, n8n / Zapier retries, etc.) don&#39;t accidentally double-post.  **1. Same-request idempotency (5-minute window).** Pass an &#x60;x-request-id&#x60; header to mark a logical request. If a second request arrives with the same &#x60;x-request-id&#x60; while the first is in-flight (or within ~5 minutes of completion), we return **HTTP 200** with the original post in the &#x60;existingPost&#x60; field — no new post is created. The official Zernio SDKs auto-generate a unique &#x60;x-request-id&#x60; per call. If you&#39;re using a generic HTTP client (curl, n8n&#39;s HTTP node, Zapier, custom code), either: - Set a unique &#x60;x-request-id&#x60; per logical call (recommended — UUIDv4 is fine) - Or simply omit the header — we&#39;ll treat each request as new  **Common pitfall**: if your workflow tool uses a single execution-level request ID and reuses it across multiple HTTP nodes (e.g. one ID for the whole run, shared across 6 different platform calls), every call after the first will look like a retry of the first and return its post. Generate a fresh ID per node.  **2. Content-hash dedup (24-hour window).** Independently, we hash &#x60;(platform, accountId, content + media URLs)&#x60; and reject duplicates within 24 hours with **HTTP 409**. This catches genuine \&quot;same content posted twice to the same account\&quot; cases regardless of &#x60;x-request-id&#x60;. Returns &#x60;error&#x60;, &#x60;accountId&#x60;, &#x60;platform&#x60;, and &#x60;existingPostId&#x60; so you can find the original. To intentionally re-post identical content within 24h, change something (the caption, the media, the account) — the dedup is keyed on the full content fingerprint.  Order: same-&#x60;x-request-id&#x60; retries (200) are checked first; if no idempotency match, the content-hash dedup (409) runs. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        CreatePostRequest createPostRequest = new CreatePostRequest(); // CreatePostRequest | 
        UUID xRequestId = UUID.randomUUID(); // UUID | Optional client-generated request identifier for safe retry (idempotency). When two requests carry the same value, the second is treated as a retry of the first and returns the original post (HTTP 200) instead of creating a duplicate. Window is ~5 minutes from the first request. Generate a UUID per logical call. SDKs do this automatically; HTTP clients should set it themselves or omit it. See the operation description for the full idempotency contract. 
        try {
            ApiResponse<PostCreateResponse> response = apiInstance.createPostWithHttpInfo(createPostRequest, xRequestId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#createPost");
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
| **createPostRequest** | [**CreatePostRequest**](CreatePostRequest.md)|  | |
| **xRequestId** | **UUID**| Optional client-generated request identifier for safe retry (idempotency). When two requests carry the same value, the second is treated as a retry of the first and returns the original post (HTTP 200) instead of creating a duplicate. Window is ~5 minutes from the first request. Generate a UUID per logical call. SDKs do this automatically; HTTP clients should set it themselves or omit it. See the operation description for the full idempotency contract.  | [optional] |

### Return type

ApiResponse<[**PostCreateResponse**](PostCreateResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Post created |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Duplicate content detected. Returned when the requested post matches an existing one on &#x60;(platform, accountId, content-hash)&#x60; within the last 24 hours, AND the request was NOT an &#x60;x-request-id&#x60; retry of an in-flight call. Distinct from same-&#x60;x-request-id&#x60; retries (which return HTTP 200 with the original post — see operation description for the idempotency contract).  Body fields: - &#x60;error&#x60; — human-readable message - &#x60;details.accountId&#x60; — the account that already has this content - &#x60;details.platform&#x60; — the platform that already has this content - &#x60;details.existingPostId&#x60; — Zernio &#x60;_id&#x60; of the original post  To intentionally re-post identical content within 24h, vary the content fingerprint (change the caption, swap a media item, or use a different account). To avoid 409s caused by retry loops, set a unique &#x60;x-request-id&#x60; per logical request — see &#x60;parameters.x-request-id&#x60; above.  |  -  |
| **429** | Rate limit exceeded. Possible causes: API rate limit, velocity limit (15 posts/hour per account), account cooldown, or daily platform limits. |  * Retry-After - Seconds until the rate limit resets (for API rate limits) <br>  * X-RateLimit-Limit - The rate limit ceiling <br>  * X-RateLimit-Remaining - Requests remaining in current window <br>  |


## deletePost

> PostDeleteResponse deletePost(postId)

Delete post

Delete a draft or scheduled post from Zernio. Published posts cannot be deleted; use the Unpublish endpoint instead. Upload quota is automatically refunded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        try {
            PostDeleteResponse result = apiInstance.deletePost(postId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#deletePost");
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

### Return type

[**PostDeleteResponse**](PostDeleteResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Cannot delete published posts |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

## deletePostWithHttpInfo

> ApiResponse<PostDeleteResponse> deletePost deletePostWithHttpInfo(postId)

Delete post

Delete a draft or scheduled post from Zernio. Published posts cannot be deleted; use the Unpublish endpoint instead. Upload quota is automatically refunded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        try {
            ApiResponse<PostDeleteResponse> response = apiInstance.deletePostWithHttpInfo(postId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#deletePost");
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

### Return type

ApiResponse<[**PostDeleteResponse**](PostDeleteResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Cannot delete published posts |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |


## editPost

> EditPost200Response editPost(postId, editPostRequest)

Edit published post

Edit a published post on a social media platform. Currently only supported for X (Twitter).  Requirements: - Connected X account must have an active X Premium subscription - Must be within 1 hour of original publish time - Maximum 5 edits per tweet (enforced by X) - Text-only edits (media changes are not supported)  The post record in Zernio is updated with the new content and edit history. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        EditPostRequest editPostRequest = new EditPostRequest(); // EditPostRequest | 
        try {
            EditPost200Response result = apiInstance.editPost(postId, editPostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#editPost");
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
| **editPostRequest** | [**EditPostRequest**](EditPostRequest.md)|  | |

### Return type

[**EditPost200Response**](EditPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post edited successfully |  -  |
| **400** | Invalid request: platform not supported, post not published, edit window expired, not Premium, or missing content. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **500** | Platform API edit failed |  -  |

## editPostWithHttpInfo

> ApiResponse<EditPost200Response> editPost editPostWithHttpInfo(postId, editPostRequest)

Edit published post

Edit a published post on a social media platform. Currently only supported for X (Twitter).  Requirements: - Connected X account must have an active X Premium subscription - Must be within 1 hour of original publish time - Maximum 5 edits per tweet (enforced by X) - Text-only edits (media changes are not supported)  The post record in Zernio is updated with the new content and edit history. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        EditPostRequest editPostRequest = new EditPostRequest(); // EditPostRequest | 
        try {
            ApiResponse<EditPost200Response> response = apiInstance.editPostWithHttpInfo(postId, editPostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#editPost");
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
| **editPostRequest** | [**EditPostRequest**](EditPostRequest.md)|  | |

### Return type

ApiResponse<[**EditPost200Response**](EditPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post edited successfully |  -  |
| **400** | Invalid request: platform not supported, post not published, edit window expired, not Premium, or missing content. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **500** | Platform API edit failed |  -  |


## getPost

> PostGetResponse getPost(postId)

Get post

Fetch a single post by ID. For published posts, this returns platformPostUrl for each platform. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        try {
            PostGetResponse result = apiInstance.getPost(postId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#getPost");
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

### Return type

[**PostGetResponse**](PostGetResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

## getPostWithHttpInfo

> ApiResponse<PostGetResponse> getPost getPostWithHttpInfo(postId)

Get post

Fetch a single post by ID. For published posts, this returns platformPostUrl for each platform. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        try {
            ApiResponse<PostGetResponse> response = apiInstance.getPostWithHttpInfo(postId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#getPost");
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

### Return type

ApiResponse<[**PostGetResponse**](PostGetResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |


## listPosts

> PostsListResponse listPosts(page, limit, status, platform, profileId, createdBy, dateFrom, dateTo, includeHidden, search, sortBy, accountId)

List posts

Returns a paginated list of posts. Published posts include platformPostUrl with the public URL on each platform.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 10; // Integer | Page size
        String status = "draft"; // String | 
        String platform = "twitter"; // String | 
        String profileId = "profileId_example"; // String | 
        String createdBy = "createdBy_example"; // String | 
        LocalDate dateFrom = LocalDate.now(); // LocalDate | 
        LocalDate dateTo = LocalDate.now(); // LocalDate | 
        Boolean includeHidden = false; // Boolean | 
        String search = "search_example"; // String | Search posts by text content.
        String sortBy = "scheduled-desc"; // String | Sort order for results.
        String accountId = "accountId_example"; // String | Filter posts to those published via a specific social account (24-char hex ObjectId).
        try {
            PostsListResponse result = apiInstance.listPosts(page, limit, status, platform, profileId, createdBy, dateFrom, dateTo, includeHidden, search, sortBy, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#listPosts");
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
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**| Page size | [optional] [default to 10] |
| **status** | **String**|  | [optional] [enum: draft, scheduled, published, failed] |
| **platform** | **String**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **createdBy** | **String**|  | [optional] |
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **includeHidden** | **Boolean**|  | [optional] [default to false] |
| **search** | **String**| Search posts by text content. | [optional] |
| **sortBy** | **String**| Sort order for results. | [optional] [default to scheduled-desc] [enum: scheduled-desc, scheduled-asc, created-desc, created-asc, status, platform] |
| **accountId** | **String**| Filter posts to those published via a specific social account (24-char hex ObjectId). | [optional] |

### Return type

[**PostsListResponse**](PostsListResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated posts |  -  |
| **401** | Unauthorized |  -  |

## listPostsWithHttpInfo

> ApiResponse<PostsListResponse> listPosts listPostsWithHttpInfo(page, limit, status, platform, profileId, createdBy, dateFrom, dateTo, includeHidden, search, sortBy, accountId)

List posts

Returns a paginated list of posts. Published posts include platformPostUrl with the public URL on each platform.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 10; // Integer | Page size
        String status = "draft"; // String | 
        String platform = "twitter"; // String | 
        String profileId = "profileId_example"; // String | 
        String createdBy = "createdBy_example"; // String | 
        LocalDate dateFrom = LocalDate.now(); // LocalDate | 
        LocalDate dateTo = LocalDate.now(); // LocalDate | 
        Boolean includeHidden = false; // Boolean | 
        String search = "search_example"; // String | Search posts by text content.
        String sortBy = "scheduled-desc"; // String | Sort order for results.
        String accountId = "accountId_example"; // String | Filter posts to those published via a specific social account (24-char hex ObjectId).
        try {
            ApiResponse<PostsListResponse> response = apiInstance.listPostsWithHttpInfo(page, limit, status, platform, profileId, createdBy, dateFrom, dateTo, includeHidden, search, sortBy, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#listPosts");
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
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**| Page size | [optional] [default to 10] |
| **status** | **String**|  | [optional] [enum: draft, scheduled, published, failed] |
| **platform** | **String**|  | [optional] |
| **profileId** | **String**|  | [optional] |
| **createdBy** | **String**|  | [optional] |
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |
| **includeHidden** | **Boolean**|  | [optional] [default to false] |
| **search** | **String**| Search posts by text content. | [optional] |
| **sortBy** | **String**| Sort order for results. | [optional] [default to scheduled-desc] [enum: scheduled-desc, scheduled-asc, created-desc, created-asc, status, platform] |
| **accountId** | **String**| Filter posts to those published via a specific social account (24-char hex ObjectId). | [optional] |

### Return type

ApiResponse<[**PostsListResponse**](PostsListResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated posts |  -  |
| **401** | Unauthorized |  -  |


## retryPost

> PostRetryResponse retryPost(postId)

Retry failed post

Immediately retries publishing a failed post. Returns the updated post with its new status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        try {
            PostRetryResponse result = apiInstance.retryPost(postId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#retryPost");
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

### Return type

[**PostRetryResponse**](PostRetryResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retry successful |  -  |
| **207** | Partial success |  -  |
| **400** | Invalid state |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **409** | Post is currently publishing |  -  |
| **429** | Rate limit exceeded. Possible causes: API rate limit (requests per minute), velocity limit (15 posts/hour per account), or account cooldown (temporarily rate-limited due to repeated errors).  |  -  |

## retryPostWithHttpInfo

> ApiResponse<PostRetryResponse> retryPost retryPostWithHttpInfo(postId)

Retry failed post

Immediately retries publishing a failed post. Returns the updated post with its new status.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        try {
            ApiResponse<PostRetryResponse> response = apiInstance.retryPostWithHttpInfo(postId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#retryPost");
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

### Return type

ApiResponse<[**PostRetryResponse**](PostRetryResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retry successful |  -  |
| **207** | Partial success |  -  |
| **400** | Invalid state |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **409** | Post is currently publishing |  -  |
| **429** | Rate limit exceeded. Possible causes: API rate limit (requests per minute), velocity limit (15 posts/hour per account), or account cooldown (temporarily rate-limited due to repeated errors).  |  -  |


## unpublishPost

> UnpublishPost200Response unpublishPost(postId, unpublishPostRequest)

Unpublish post

Deletes a published post from the specified platform. The post record in Zernio is kept but its status is updated to cancelled. Not supported on Instagram, TikTok, or Snapchat. Threaded posts delete all items. YouTube deletion is permanent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        UnpublishPostRequest unpublishPostRequest = new UnpublishPostRequest(); // UnpublishPostRequest | 
        try {
            UnpublishPost200Response result = apiInstance.unpublishPost(postId, unpublishPostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#unpublishPost");
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
| **unpublishPostRequest** | [**UnpublishPostRequest**](UnpublishPostRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post deleted from platform |  -  |
| **400** | Invalid request: platform not supported for deletion, post not on that platform, not published, no platform post ID, or no access token. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **500** | Platform API deletion failed |  -  |

## unpublishPostWithHttpInfo

> ApiResponse<UnpublishPost200Response> unpublishPost unpublishPostWithHttpInfo(postId, unpublishPostRequest)

Unpublish post

Deletes a published post from the specified platform. The post record in Zernio is kept but its status is updated to cancelled. Not supported on Instagram, TikTok, or Snapchat. Threaded posts delete all items. YouTube deletion is permanent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        UnpublishPostRequest unpublishPostRequest = new UnpublishPostRequest(); // UnpublishPostRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.unpublishPostWithHttpInfo(postId, unpublishPostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#unpublishPost");
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
| **unpublishPostRequest** | [**UnpublishPostRequest**](UnpublishPostRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post deleted from platform |  -  |
| **400** | Invalid request: platform not supported for deletion, post not on that platform, not published, no platform post ID, or no access token. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **500** | Platform API deletion failed |  -  |


## updatePost

> PostUpdateResponse updatePost(postId, updatePostRequest)

Update post

Update an existing post. Only draft, scheduled, failed, and partial posts can be edited. Published, publishing, and cancelled posts cannot be modified. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        UpdatePostRequest updatePostRequest = new UpdatePostRequest(); // UpdatePostRequest | 
        try {
            PostUpdateResponse result = apiInstance.updatePost(postId, updatePostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#updatePost");
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
| **updatePostRequest** | [**UpdatePostRequest**](UpdatePostRequest.md)|  | |

### Return type

[**PostUpdateResponse**](PostUpdateResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post updated |  -  |
| **207** | Partial publish success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

## updatePostWithHttpInfo

> ApiResponse<PostUpdateResponse> updatePost updatePostWithHttpInfo(postId, updatePostRequest)

Update post

Update an existing post. Only draft, scheduled, failed, and partial posts can be edited. Published, publishing, and cancelled posts cannot be modified. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | 
        UpdatePostRequest updatePostRequest = new UpdatePostRequest(); // UpdatePostRequest | 
        try {
            ApiResponse<PostUpdateResponse> response = apiInstance.updatePostWithHttpInfo(postId, updatePostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#updatePost");
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
| **updatePostRequest** | [**UpdatePostRequest**](UpdatePostRequest.md)|  | |

### Return type

ApiResponse<[**PostUpdateResponse**](PostUpdateResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Post updated |  -  |
| **207** | Partial publish success |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |


## updatePostMetadata

> UpdatePostMetadata200Response updatePostMetadata(postId, updatePostMetadataRequest)

Update post metadata

Updates metadata of a published video on the specified platform without re-uploading. Currently only supported for YouTube. At least one updatable field is required.  Two modes:  1. Post-based (video published through Zernio): pass the Zernio postId in the URL and platform in the body. 2. Direct video ID (video uploaded outside Zernio, e.g. directly to YouTube): use _ as the postId,    and pass videoId + accountId + platform in the body. The accountId is the Zernio social account ID    for the connected YouTube channel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID, or \"_\" when using direct video ID mode
        UpdatePostMetadataRequest updatePostMetadataRequest = new UpdatePostMetadataRequest(); // UpdatePostMetadataRequest | 
        try {
            UpdatePostMetadata200Response result = apiInstance.updatePostMetadata(postId, updatePostMetadataRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#updatePostMetadata");
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
| **postId** | **String**| Zernio post ID, or \&quot;_\&quot; when using direct video ID mode | |
| **updatePostMetadataRequest** | [**UpdatePostMetadataRequest**](UpdatePostMetadataRequest.md)|  | |

### Return type

[**UpdatePostMetadata200Response**](UpdatePostMetadata200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadata updated successfully |  -  |
| **400** | Invalid request: unsupported platform, post not published, missing fields, or validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **500** | Platform API update failed |  -  |

## updatePostMetadataWithHttpInfo

> ApiResponse<UpdatePostMetadata200Response> updatePostMetadata updatePostMetadataWithHttpInfo(postId, updatePostMetadataRequest)

Update post metadata

Updates metadata of a published video on the specified platform without re-uploading. Currently only supported for YouTube. At least one updatable field is required.  Two modes:  1. Post-based (video published through Zernio): pass the Zernio postId in the URL and platform in the body. 2. Direct video ID (video uploaded outside Zernio, e.g. directly to YouTube): use _ as the postId,    and pass videoId + accountId + platform in the body. The accountId is the Zernio social account ID    for the connected YouTube channel. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PostsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PostsApi apiInstance = new PostsApi(defaultClient);
        String postId = "postId_example"; // String | Zernio post ID, or \"_\" when using direct video ID mode
        UpdatePostMetadataRequest updatePostMetadataRequest = new UpdatePostMetadataRequest(); // UpdatePostMetadataRequest | 
        try {
            ApiResponse<UpdatePostMetadata200Response> response = apiInstance.updatePostMetadataWithHttpInfo(postId, updatePostMetadataRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PostsApi#updatePostMetadata");
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
| **postId** | **String**| Zernio post ID, or \&quot;_\&quot; when using direct video ID mode | |
| **updatePostMetadataRequest** | [**UpdatePostMetadataRequest**](UpdatePostMetadataRequest.md)|  | |

### Return type

ApiResponse<[**UpdatePostMetadata200Response**](UpdatePostMetadata200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metadata updated successfully |  -  |
| **400** | Invalid request: unsupported platform, post not published, missing fields, or validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **500** | Platform API update failed |  -  |

