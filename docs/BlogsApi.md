# BlogsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBlog**](BlogsApi.md#createBlog) | **POST** /v1/accounts/{accountId}/blogs | Create a blog |
| [**createBlogWithHttpInfo**](BlogsApi.md#createBlogWithHttpInfo) | **POST** /v1/accounts/{accountId}/blogs | Create a blog |
| [**createBlogArticle**](BlogsApi.md#createBlogArticle) | **POST** /v1/accounts/{accountId}/blogs/{blogId}/articles | Create a blog article |
| [**createBlogArticleWithHttpInfo**](BlogsApi.md#createBlogArticleWithHttpInfo) | **POST** /v1/accounts/{accountId}/blogs/{blogId}/articles | Create a blog article |
| [**deleteBlog**](BlogsApi.md#deleteBlog) | **DELETE** /v1/accounts/{accountId}/blogs/{blogId} | Delete a blog |
| [**deleteBlogWithHttpInfo**](BlogsApi.md#deleteBlogWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/blogs/{blogId} | Delete a blog |
| [**deleteBlogArticle**](BlogsApi.md#deleteBlogArticle) | **DELETE** /v1/accounts/{accountId}/blogs/{blogId}/articles/{articleId} | Delete a blog article |
| [**deleteBlogArticleWithHttpInfo**](BlogsApi.md#deleteBlogArticleWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/blogs/{blogId}/articles/{articleId} | Delete a blog article |
| [**getBlog**](BlogsApi.md#getBlog) | **GET** /v1/accounts/{accountId}/blogs/{blogId} | Get a blog |
| [**getBlogWithHttpInfo**](BlogsApi.md#getBlogWithHttpInfo) | **GET** /v1/accounts/{accountId}/blogs/{blogId} | Get a blog |
| [**getBlogArticle**](BlogsApi.md#getBlogArticle) | **GET** /v1/accounts/{accountId}/blogs/{blogId}/articles/{articleId} | Get a blog article |
| [**getBlogArticleWithHttpInfo**](BlogsApi.md#getBlogArticleWithHttpInfo) | **GET** /v1/accounts/{accountId}/blogs/{blogId}/articles/{articleId} | Get a blog article |
| [**listBlogArticles**](BlogsApi.md#listBlogArticles) | **GET** /v1/accounts/{accountId}/blogs/{blogId}/articles | List blog articles |
| [**listBlogArticlesWithHttpInfo**](BlogsApi.md#listBlogArticlesWithHttpInfo) | **GET** /v1/accounts/{accountId}/blogs/{blogId}/articles | List blog articles |
| [**listBlogs**](BlogsApi.md#listBlogs) | **GET** /v1/accounts/{accountId}/blogs | List blogs |
| [**listBlogsWithHttpInfo**](BlogsApi.md#listBlogsWithHttpInfo) | **GET** /v1/accounts/{accountId}/blogs | List blogs |
| [**updateBlog**](BlogsApi.md#updateBlog) | **PATCH** /v1/accounts/{accountId}/blogs/{blogId} | Update a blog |
| [**updateBlogWithHttpInfo**](BlogsApi.md#updateBlogWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/blogs/{blogId} | Update a blog |
| [**updateBlogArticle**](BlogsApi.md#updateBlogArticle) | **PATCH** /v1/accounts/{accountId}/blogs/{blogId}/articles/{articleId} | Update a blog article |
| [**updateBlogArticleWithHttpInfo**](BlogsApi.md#updateBlogArticleWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/blogs/{blogId}/articles/{articleId} | Update a blog article |



## createBlog

> CreateBlog201Response createBlog(accountId, createBlogRequest)

Create a blog

Creates a blog on the connected store. The platform generates the URL &#x60;handle&#x60; from the title when omitted.  Supported on Shopify (platform &#x60;shopify&#x60;). A WordPress or Wix connection is its existing site, so both return 405 for blog creation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        CreateBlogRequest createBlogRequest = new CreateBlogRequest(); // CreateBlogRequest | 
        try {
            CreateBlog201Response result = apiInstance.createBlog(accountId, createBlogRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#createBlog");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **createBlogRequest** | [**CreateBlogRequest**](CreateBlogRequest.md)|  | |

### Return type

[**CreateBlog201Response**](CreateBlog201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Blog created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support creating blogs. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## createBlogWithHttpInfo

> ApiResponse<CreateBlog201Response> createBlog createBlogWithHttpInfo(accountId, createBlogRequest)

Create a blog

Creates a blog on the connected store. The platform generates the URL &#x60;handle&#x60; from the title when omitted.  Supported on Shopify (platform &#x60;shopify&#x60;). A WordPress or Wix connection is its existing site, so both return 405 for blog creation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        CreateBlogRequest createBlogRequest = new CreateBlogRequest(); // CreateBlogRequest | 
        try {
            ApiResponse<CreateBlog201Response> response = apiInstance.createBlogWithHttpInfo(accountId, createBlogRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#createBlog");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **createBlogRequest** | [**CreateBlogRequest**](CreateBlogRequest.md)|  | |

### Return type

ApiResponse<[**CreateBlog201Response**](CreateBlog201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Blog created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support creating blogs. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## createBlogArticle

> CreateBlogArticle201Response createBlogArticle(accountId, blogId, createBlogArticleRequest, idempotencyKey)

Create a blog article

Creates an article on the blog. Publishing behavior:  - WordPress, Wix and Webflow default to a draft when both publishing   fields are omitted. - &#x60;isPublished: false&#x60; keeps the article as a draft and takes priority   over a future &#x60;publishDate&#x60;. - A future &#x60;publishDate&#x60; schedules publication natively on the   platform; the platform publishes it at that time with no Zernio   queue involved. - &#x60;isPublished: true&#x60; publishes immediately when there is no future   &#x60;publishDate&#x60;. - &#x60;seo.title&#x60; / &#x60;seo.description&#x60; map to Shopify&#39;s global &#x60;title_tag&#x60;   and &#x60;description_tag&#x60; metafields (the fields Shopify themes read for   the page title and meta description), and on Wix to the post&#39;s SEO   title and meta description. WordPress and Webflow reject &#x60;seo&#x60;; SEO   plugin and custom-field writes are not supported. - Webflow has no scheduling API: a future &#x60;publishDate&#x60; returns 400   unless &#x60;isPublished: false&#x60; keeps a draft. Fields map to the   collection&#39;s own fields by type and slug (the body to its rich text   field, &#x60;excerpt&#x60; to a summary field, &#x60;image&#x60; to an image field, &#x60;tags&#x60;   and &#x60;author&#x60; to tag and author reference fields); sending a field the   collection does not have returns 400, as does a collection that   requires a field the Blogs API cannot fill. - Wix stores rich content: &#x60;bodyHtml&#x60; is converted on write (each   top-level HTML element must fit 30,000 characters), and images in   the body are imported into the site&#39;s Media Manager.  Send an Idempotency-Key header to make retries safe: a retry with the same key and body replays the original 201 instead of creating a second article. A retry while the first request is still running returns 409; retry after a short backoff.  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). WordPress native scheduling depends on the site&#39;s scheduler/WP-Cron. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        CreateBlogArticleRequest createBlogArticleRequest = new CreateBlogArticleRequest(); // CreateBlogArticleRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.
        try {
            CreateBlogArticle201Response result = apiInstance.createBlogArticle(accountId, blogId, createBlogArticleRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#createBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **createBlogArticleRequest** | [**CreateBlogArticleRequest**](CreateBlogArticleRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. | [optional] |

### Return type

[**CreateBlogArticle201Response**](CreateBlogArticle201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Article created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support creating articles. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. Article mutations are not blindly retried. |  -  |

## createBlogArticleWithHttpInfo

> ApiResponse<CreateBlogArticle201Response> createBlogArticle createBlogArticleWithHttpInfo(accountId, blogId, createBlogArticleRequest, idempotencyKey)

Create a blog article

Creates an article on the blog. Publishing behavior:  - WordPress, Wix and Webflow default to a draft when both publishing   fields are omitted. - &#x60;isPublished: false&#x60; keeps the article as a draft and takes priority   over a future &#x60;publishDate&#x60;. - A future &#x60;publishDate&#x60; schedules publication natively on the   platform; the platform publishes it at that time with no Zernio   queue involved. - &#x60;isPublished: true&#x60; publishes immediately when there is no future   &#x60;publishDate&#x60;. - &#x60;seo.title&#x60; / &#x60;seo.description&#x60; map to Shopify&#39;s global &#x60;title_tag&#x60;   and &#x60;description_tag&#x60; metafields (the fields Shopify themes read for   the page title and meta description), and on Wix to the post&#39;s SEO   title and meta description. WordPress and Webflow reject &#x60;seo&#x60;; SEO   plugin and custom-field writes are not supported. - Webflow has no scheduling API: a future &#x60;publishDate&#x60; returns 400   unless &#x60;isPublished: false&#x60; keeps a draft. Fields map to the   collection&#39;s own fields by type and slug (the body to its rich text   field, &#x60;excerpt&#x60; to a summary field, &#x60;image&#x60; to an image field, &#x60;tags&#x60;   and &#x60;author&#x60; to tag and author reference fields); sending a field the   collection does not have returns 400, as does a collection that   requires a field the Blogs API cannot fill. - Wix stores rich content: &#x60;bodyHtml&#x60; is converted on write (each   top-level HTML element must fit 30,000 characters), and images in   the body are imported into the site&#39;s Media Manager.  Send an Idempotency-Key header to make retries safe: a retry with the same key and body replays the original 201 instead of creating a second article. A retry while the first request is still running returns 409; retry after a short backoff.  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). WordPress native scheduling depends on the site&#39;s scheduler/WP-Cron. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        CreateBlogArticleRequest createBlogArticleRequest = new CreateBlogArticleRequest(); // CreateBlogArticleRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.
        try {
            ApiResponse<CreateBlogArticle201Response> response = apiInstance.createBlogArticleWithHttpInfo(accountId, blogId, createBlogArticleRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#createBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **createBlogArticleRequest** | [**CreateBlogArticleRequest**](CreateBlogArticleRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. | [optional] |

### Return type

ApiResponse<[**CreateBlogArticle201Response**](CreateBlogArticle201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Article created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support creating articles. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. Article mutations are not blindly retried. |  -  |


## deleteBlog

> void deleteBlog(accountId, blogId)

Delete a blog

Deletes the blog AND every article in it. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from.  Supported on Shopify (platform &#x60;shopify&#x60;). Disconnect a WordPress or Wix account instead of deleting its site; both return 405 here. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String blogId = "blogId_example"; // String | Platform-native blog id. Shopify blog ids are numeric; other values return 400.
        try {
            apiInstance.deleteBlog(accountId, blogId);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#deleteBlog");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native blog id. Shopify blog ids are numeric; other values return 400. | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Blog deleted (no content). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support deleting a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## deleteBlogWithHttpInfo

> ApiResponse<Void> deleteBlog deleteBlogWithHttpInfo(accountId, blogId)

Delete a blog

Deletes the blog AND every article in it. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from.  Supported on Shopify (platform &#x60;shopify&#x60;). Disconnect a WordPress or Wix account instead of deleting its site; both return 405 here. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String blogId = "blogId_example"; // String | Platform-native blog id. Shopify blog ids are numeric; other values return 400.
        try {
            ApiResponse<Void> response = apiInstance.deleteBlogWithHttpInfo(accountId, blogId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#deleteBlog");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native blog id. Shopify blog ids are numeric; other values return 400. | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Blog deleted (no content). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support deleting a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## deleteBlogArticle

> void deleteBlogArticle(accountId, blogId, articleId)

Delete a blog article

Deletes the article. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from. On WordPress the post is force-deleted, while uploaded attachments and tags remain in the site&#39;s media library and taxonomy. On Webflow the item is unpublished from the live site, then deleted from the collection.  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        String articleId = "articleId_example"; // String | Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400.
        try {
            apiInstance.deleteBlogArticle(accountId, blogId, articleId);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#deleteBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **articleId** | **String**| Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400. | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Article deleted (no content). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support deleting an article. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. Article deletion is not blindly retried. |  -  |

## deleteBlogArticleWithHttpInfo

> ApiResponse<Void> deleteBlogArticle deleteBlogArticleWithHttpInfo(accountId, blogId, articleId)

Delete a blog article

Deletes the article. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from. On WordPress the post is force-deleted, while uploaded attachments and tags remain in the site&#39;s media library and taxonomy. On Webflow the item is unpublished from the live site, then deleted from the collection.  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        String articleId = "articleId_example"; // String | Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400.
        try {
            ApiResponse<Void> response = apiInstance.deleteBlogArticleWithHttpInfo(accountId, blogId, articleId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#deleteBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **articleId** | **String**| Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400. | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Article deleted (no content). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support deleting an article. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. Article deletion is not blindly retried. |  -  |


## getBlog

> GetBlog200Response getBlog(accountId, blogId)

Get a blog

Fetches a single blog. Use the platform-native &#x60;blogId&#x60; returned by &#x60;GET /v1/accounts/{accountId}/blogs&#x60;: a Shopify numeric blog id, the WordPress.com numeric site id, or &#x60;1&#x60; for a self-hosted WordPress or a Wix site. That &#x60;1&#x60; is scoped to its connected account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        try {
            GetBlog200Response result = apiInstance.getBlog(accountId, blogId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#getBlog");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |

### Return type

[**GetBlog200Response**](GetBlog200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blog fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support fetching a blog. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |

## getBlogWithHttpInfo

> ApiResponse<GetBlog200Response> getBlog getBlogWithHttpInfo(accountId, blogId)

Get a blog

Fetches a single blog. Use the platform-native &#x60;blogId&#x60; returned by &#x60;GET /v1/accounts/{accountId}/blogs&#x60;: a Shopify numeric blog id, the WordPress.com numeric site id, or &#x60;1&#x60; for a self-hosted WordPress or a Wix site. That &#x60;1&#x60; is scoped to its connected account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        try {
            ApiResponse<GetBlog200Response> response = apiInstance.getBlogWithHttpInfo(accountId, blogId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#getBlog");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |

### Return type

ApiResponse<[**GetBlog200Response**](GetBlog200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blog fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support fetching a blog. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |


## getBlogArticle

> CreateBlogArticle201Response getBlogArticle(accountId, blogId, articleId)

Get a blog article

Fetches a single article. An article addressed through a blog it does not belong to is a 404 (code blog_article_not_found).  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). WordPress returns its native &#x60;status&#x60;; &#x60;publishedAt&#x60; is present only for a published post and &#x60;publishDate&#x60; only for a scheduled post. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        String articleId = "articleId_example"; // String | Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400.
        try {
            CreateBlogArticle201Response result = apiInstance.getBlogArticle(accountId, blogId, articleId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#getBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **articleId** | **String**| Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400. | |

### Return type

[**CreateBlogArticle201Response**](CreateBlogArticle201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support fetching an article. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |

## getBlogArticleWithHttpInfo

> ApiResponse<CreateBlogArticle201Response> getBlogArticle getBlogArticleWithHttpInfo(accountId, blogId, articleId)

Get a blog article

Fetches a single article. An article addressed through a blog it does not belong to is a 404 (code blog_article_not_found).  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). WordPress returns its native &#x60;status&#x60;; &#x60;publishedAt&#x60; is present only for a published post and &#x60;publishDate&#x60; only for a scheduled post. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        String articleId = "articleId_example"; // String | Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400.
        try {
            ApiResponse<CreateBlogArticle201Response> response = apiInstance.getBlogArticleWithHttpInfo(accountId, blogId, articleId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#getBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **articleId** | **String**| Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400. | |

### Return type

ApiResponse<[**CreateBlogArticle201Response**](CreateBlogArticle201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support fetching an article. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |


## listBlogArticles

> ListBlogArticles200Response listBlogArticles(accountId, blogId, limit, cursor)

List blog articles

Lists the articles of a blog. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages. Treat cursors as opaque and pass them unchanged. Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). WordPress and Wix results include &#x60;status&#x60; and include &#x60;publishDate&#x60; only for scheduled (&#x60;future&#x60;) posts. Wix lists return &#x60;bodyHtml: null&#x60;; get the article for its body. Webflow results report &#x60;status&#x60; as &#x60;publish&#x60; or &#x60;draft&#x60; only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        Integer limit = 20; // Integer | Page size (1-50).
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        try {
            ListBlogArticles200Response result = apiInstance.listBlogArticles(accountId, blogId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#listBlogArticles");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **limit** | **Integer**| Page size (1-50). | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |

### Return type

[**ListBlogArticles200Response**](ListBlogArticles200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Articles listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support listing articles. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |

## listBlogArticlesWithHttpInfo

> ApiResponse<ListBlogArticles200Response> listBlogArticles listBlogArticlesWithHttpInfo(accountId, blogId, limit, cursor)

List blog articles

Lists the articles of a blog. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages. Treat cursors as opaque and pass them unchanged. Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). WordPress and Wix results include &#x60;status&#x60; and include &#x60;publishDate&#x60; only for scheduled (&#x60;future&#x60;) posts. Wix lists return &#x60;bodyHtml: null&#x60;; get the article for its body. Webflow results report &#x60;status&#x60; as &#x60;publish&#x60; or &#x60;draft&#x60; only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        Integer limit = 20; // Integer | Page size (1-50).
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        try {
            ApiResponse<ListBlogArticles200Response> response = apiInstance.listBlogArticlesWithHttpInfo(accountId, blogId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#listBlogArticles");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **limit** | **Integer**| Page size (1-50). | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |

### Return type

ApiResponse<[**ListBlogArticles200Response**](ListBlogArticles200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Articles listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support listing articles. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |


## listBlogs

> ListBlogs200Response listBlogs(accountId, limit, cursor)

List blogs

Lists blogs on the connected account. Shopify returns its store blogs with cursor pagination. A WordPress or Wix account represents one site and always returns exactly that one blog with &#x60;nextCursor: null&#x60;. A Webflow site returns each CMS collection that has a rich text field (its blog id is the collection id), with &#x60;nextCursor: null&#x60;.  &#x60;limit&#x60; is 1-50 (default 20). Treat &#x60;nextCursor&#x60; as opaque; pass it unchanged on the next request. Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        Integer limit = 20; // Integer | Page size (1-50).
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        try {
            ListBlogs200Response result = apiInstance.listBlogs(accountId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#listBlogs");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **limit** | **Integer**| Page size (1-50). | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |

### Return type

[**ListBlogs200Response**](ListBlogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blogs listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support listing blogs. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |

## listBlogsWithHttpInfo

> ApiResponse<ListBlogs200Response> listBlogs listBlogsWithHttpInfo(accountId, limit, cursor)

List blogs

Lists blogs on the connected account. Shopify returns its store blogs with cursor pagination. A WordPress or Wix account represents one site and always returns exactly that one blog with &#x60;nextCursor: null&#x60;. A Webflow site returns each CMS collection that has a rich text field (its blog id is the collection id), with &#x60;nextCursor: null&#x60;.  &#x60;limit&#x60; is 1-50 (default 20). Treat &#x60;nextCursor&#x60; as opaque; pass it unchanged on the next request. Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        Integer limit = 20; // Integer | Page size (1-50).
        String cursor = "cursor_example"; // String | Opaque cursor from a previous response. Omit for the first page.
        try {
            ApiResponse<ListBlogs200Response> response = apiInstance.listBlogsWithHttpInfo(accountId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#listBlogs");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **limit** | **Integer**| Page size (1-50). | [optional] [default to 20] |
| **cursor** | **String**| Opaque cursor from a previous response. Omit for the first page. | [optional] |

### Return type

ApiResponse<[**ListBlogs200Response**](ListBlogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blogs listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support listing blogs. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. |  -  |


## updateBlog

> CreateBlog201Response updateBlog(accountId, blogId, updateBlogRequest)

Update a blog

Partial-updates a blog. Send any subset of &#x60;title&#x60; and &#x60;handle&#x60;; at least one field is required (an empty body returns 400).  Supported on Shopify (platform &#x60;shopify&#x60;). WordPress and Wix site settings are not writable through this API, so both return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String blogId = "blogId_example"; // String | Platform-native blog id. Shopify blog ids are numeric; other values return 400.
        UpdateBlogRequest updateBlogRequest = new UpdateBlogRequest(); // UpdateBlogRequest | 
        try {
            CreateBlog201Response result = apiInstance.updateBlog(accountId, blogId, updateBlogRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#updateBlog");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native blog id. Shopify blog ids are numeric; other values return 400. | |
| **updateBlogRequest** | [**UpdateBlogRequest**](UpdateBlogRequest.md)|  | |

### Return type

[**CreateBlog201Response**](CreateBlog201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blog updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support updating a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## updateBlogWithHttpInfo

> ApiResponse<CreateBlog201Response> updateBlog updateBlogWithHttpInfo(accountId, blogId, updateBlogRequest)

Update a blog

Partial-updates a blog. Send any subset of &#x60;title&#x60; and &#x60;handle&#x60;; at least one field is required (an empty body returns 400).  Supported on Shopify (platform &#x60;shopify&#x60;). WordPress and Wix site settings are not writable through this API, so both return 405. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify SocialAccount id.
        String blogId = "blogId_example"; // String | Platform-native blog id. Shopify blog ids are numeric; other values return 400.
        UpdateBlogRequest updateBlogRequest = new UpdateBlogRequest(); // UpdateBlogRequest | 
        try {
            ApiResponse<CreateBlog201Response> response = apiInstance.updateBlogWithHttpInfo(accountId, blogId, updateBlogRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#updateBlog");
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native blog id. Shopify blog ids are numeric; other values return 400. | |
| **updateBlogRequest** | [**UpdateBlogRequest**](UpdateBlogRequest.md)|  | |

### Return type

ApiResponse<[**CreateBlog201Response**](CreateBlog201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blog updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support updating a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## updateBlogArticle

> CreateBlogArticle201Response updateBlogArticle(accountId, blogId, articleId, updateBlogArticleRequest)

Update a blog article

Partial-updates an article. Send any subset of the create fields (&#x60;title&#x60;, &#x60;bodyHtml&#x60;, &#x60;handle&#x60;, &#x60;tags&#x60;, &#x60;author&#x60;, &#x60;excerpt&#x60;, &#x60;image&#x60;, &#x60;seo&#x60;, &#x60;isPublished&#x60;, &#x60;publishDate&#x60;); at least one field is required (an empty body returns 400). &#x60;isPublished&#x60; and &#x60;publishDate&#x60; behave as on create: &#x60;isPublished: false&#x60; unpublishes back to a draft and a future &#x60;publishDate&#x60; schedules publication natively on the platform. Omitting both fields preserves the current WordPress or Wix status. Omitting &#x60;image&#x60; preserves the current featured image; removal is not supported. WordPress rejects &#x60;seo&#x60; and does not support SEO-plugin/custom-field, category, or custom-post-type writes. On Webflow, an edit to a published item goes live immediately, &#x60;isPublished: false&#x60; unpublishes it, and a future &#x60;publishDate&#x60; returns 400.  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        String articleId = "articleId_example"; // String | Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400.
        UpdateBlogArticleRequest updateBlogArticleRequest = new UpdateBlogArticleRequest(); // UpdateBlogArticleRequest | 
        try {
            CreateBlogArticle201Response result = apiInstance.updateBlogArticle(accountId, blogId, articleId, updateBlogArticleRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#updateBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **articleId** | **String**| Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400. | |
| **updateBlogArticleRequest** | [**UpdateBlogArticleRequest**](UpdateBlogArticleRequest.md)|  | |

### Return type

[**CreateBlogArticle201Response**](CreateBlogArticle201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support updating an article. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. Article mutations are not blindly retried. |  -  |

## updateBlogArticleWithHttpInfo

> ApiResponse<CreateBlogArticle201Response> updateBlogArticle updateBlogArticleWithHttpInfo(accountId, blogId, articleId, updateBlogArticleRequest)

Update a blog article

Partial-updates an article. Send any subset of the create fields (&#x60;title&#x60;, &#x60;bodyHtml&#x60;, &#x60;handle&#x60;, &#x60;tags&#x60;, &#x60;author&#x60;, &#x60;excerpt&#x60;, &#x60;image&#x60;, &#x60;seo&#x60;, &#x60;isPublished&#x60;, &#x60;publishDate&#x60;); at least one field is required (an empty body returns 400). &#x60;isPublished&#x60; and &#x60;publishDate&#x60; behave as on create: &#x60;isPublished: false&#x60; unpublishes back to a draft and a future &#x60;publishDate&#x60; schedules publication natively on the platform. Omitting both fields preserves the current WordPress or Wix status. Omitting &#x60;image&#x60; preserves the current featured image; removal is not supported. WordPress rejects &#x60;seo&#x60; and does not support SEO-plugin/custom-field, category, or custom-post-type writes. On Webflow, an edit to a published item goes live immediately, &#x60;isPublished: false&#x60; unpublishes it, and a future &#x60;publishDate&#x60; returns 400.  Supported on Shopify (&#x60;shopify&#x60;), WordPress (&#x60;wordpress&#x60;), Wix (&#x60;wix&#x60;) and Webflow (&#x60;webflow&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BlogsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BlogsApi apiInstance = new BlogsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected Shopify, WordPress, Wix or Webflow account id.
        String blogId = "blogId_example"; // String | Platform-native blog/site id returned by the list operation.
        String articleId = "articleId_example"; // String | Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400.
        UpdateBlogArticleRequest updateBlogArticleRequest = new UpdateBlogArticleRequest(); // UpdateBlogArticleRequest | 
        try {
            ApiResponse<CreateBlogArticle201Response> response = apiInstance.updateBlogArticleWithHttpInfo(accountId, blogId, articleId, updateBlogArticleRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BlogsApi#updateBlogArticle");
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
| **accountId** | **String**| Connected Shopify, WordPress, Wix or Webflow account id. | |
| **blogId** | **String**| Platform-native blog/site id returned by the list operation. | |
| **articleId** | **String**| Platform-native article id: numeric on Shopify and WordPress, a GUID on Wix, a 24-character hex item id on Webflow. Other formats return 400. | |
| **updateBlogArticleRequest** | [**UpdateBlogArticleRequest**](UpdateBlogArticleRequest.md)|  | |

### Return type

ApiResponse<[**CreateBlogArticle201Response**](CreateBlogArticle201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the account or restore the WordPress user capabilities. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support updating an article. |  -  |
| **429** | Rate limited by Zernio or the connected platform. Retry later. |  -  |
| **502** | The connected platform returned an unclassified upstream error. Article mutations are not blindly retried. |  -  |

