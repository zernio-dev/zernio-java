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

Creates a blog on the connected store. The platform generates the URL &#x60;handle&#x60; from the title when omitted.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support creating blogs. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## createBlogWithHttpInfo

> ApiResponse<CreateBlog201Response> createBlog createBlogWithHttpInfo(accountId, createBlogRequest)

Create a blog

Creates a blog on the connected store. The platform generates the URL &#x60;handle&#x60; from the title when omitted.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support creating blogs. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## createBlogArticle

> CreateBlogArticle201Response createBlogArticle(accountId, blogId, createBlogArticleRequest)

Create a blog article

Creates an article on the blog. Publishing behavior:  - &#x60;isPublished: false&#x60; keeps the article as a draft. - A future &#x60;publishDate&#x60; schedules publication natively on the   platform; the platform publishes it at that time with no Zernio   queue involved. - &#x60;seo.title&#x60; / &#x60;seo.description&#x60; map to Shopify&#39;s global &#x60;title_tag&#x60;   and &#x60;description_tag&#x60; metafields (the fields Shopify themes read for   the page title and meta description).  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        CreateBlogArticleRequest createBlogArticleRequest = new CreateBlogArticleRequest(); // CreateBlogArticleRequest | 
        try {
            CreateBlogArticle201Response result = apiInstance.createBlogArticle(accountId, blogId, createBlogArticleRequest);
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **createBlogArticleRequest** | [**CreateBlogArticleRequest**](CreateBlogArticleRequest.md)|  | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support creating articles. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## createBlogArticleWithHttpInfo

> ApiResponse<CreateBlogArticle201Response> createBlogArticle createBlogArticleWithHttpInfo(accountId, blogId, createBlogArticleRequest)

Create a blog article

Creates an article on the blog. Publishing behavior:  - &#x60;isPublished: false&#x60; keeps the article as a draft. - A future &#x60;publishDate&#x60; schedules publication natively on the   platform; the platform publishes it at that time with no Zernio   queue involved. - &#x60;seo.title&#x60; / &#x60;seo.description&#x60; map to Shopify&#39;s global &#x60;title_tag&#x60;   and &#x60;description_tag&#x60; metafields (the fields Shopify themes read for   the page title and meta description).  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        CreateBlogArticleRequest createBlogArticleRequest = new CreateBlogArticleRequest(); // CreateBlogArticleRequest | 
        try {
            ApiResponse<CreateBlogArticle201Response> response = apiInstance.createBlogArticleWithHttpInfo(accountId, blogId, createBlogArticleRequest);
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **createBlogArticleRequest** | [**CreateBlogArticleRequest**](CreateBlogArticleRequest.md)|  | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support creating articles. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## deleteBlog

> void deleteBlog(accountId, blogId)

Delete a blog

Deletes the blog AND every article in it. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
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
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support deleting a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## deleteBlogWithHttpInfo

> ApiResponse<Void> deleteBlog deleteBlogWithHttpInfo(accountId, blogId)

Delete a blog

Deletes the blog AND every article in it. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
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
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support deleting a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## deleteBlogArticle

> void deleteBlogArticle(accountId, blogId, articleId)

Delete a blog article

Deletes the article. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        String articleId = "articleId_example"; // String | Platform-native numeric article id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **articleId** | **String**| Platform-native numeric article id. Non-numeric values return 400. | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support deleting an article. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## deleteBlogArticleWithHttpInfo

> ApiResponse<Void> deleteBlogArticle deleteBlogArticleWithHttpInfo(accountId, blogId, articleId)

Delete a blog article

Deletes the article. The delete happens on the platform and is permanent; Zernio stores nothing to restore it from.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        String articleId = "articleId_example"; // String | Platform-native numeric article id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **articleId** | **String**| Platform-native numeric article id. Non-numeric values return 400. | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support deleting an article. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## getBlog

> CreateBlog201Response getBlog(accountId, blogId)

Get a blog

Fetches a single blog. &#x60;blogId&#x60; is the platform&#39;s numeric blog id from &#x60;GET /v1/accounts/{accountId}/blogs&#x60;, not a Zernio id.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        try {
            CreateBlog201Response result = apiInstance.getBlog(accountId, blogId);
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |

### Return type

[**CreateBlog201Response**](CreateBlog201Response.md)


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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support fetching a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## getBlogWithHttpInfo

> ApiResponse<CreateBlog201Response> getBlog getBlogWithHttpInfo(accountId, blogId)

Get a blog

Fetches a single blog. &#x60;blogId&#x60; is the platform&#39;s numeric blog id from &#x60;GET /v1/accounts/{accountId}/blogs&#x60;, not a Zernio id.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        try {
            ApiResponse<CreateBlog201Response> response = apiInstance.getBlogWithHttpInfo(accountId, blogId);
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |

### Return type

ApiResponse<[**CreateBlog201Response**](CreateBlog201Response.md)>


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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support fetching a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## getBlogArticle

> CreateBlogArticle201Response getBlogArticle(accountId, blogId, articleId)

Get a blog article

Fetches a single article. An article addressed through a blog it does not belong to is a 404 (code blog_article_not_found).  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        String articleId = "articleId_example"; // String | Platform-native numeric article id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **articleId** | **String**| Platform-native numeric article id. Non-numeric values return 400. | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support fetching an article. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## getBlogArticleWithHttpInfo

> ApiResponse<CreateBlogArticle201Response> getBlogArticle getBlogArticleWithHttpInfo(accountId, blogId, articleId)

Get a blog article

Fetches a single article. An article addressed through a blog it does not belong to is a 404 (code blog_article_not_found).  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        String articleId = "articleId_example"; // String | Platform-native numeric article id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **articleId** | **String**| Platform-native numeric article id. Non-numeric values return 400. | |

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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support fetching an article. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## listBlogArticles

> ListBlogArticles200Response listBlogArticles(accountId, blogId, limit, cursor)

List blog articles

Lists the articles of a blog. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support listing articles. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## listBlogArticlesWithHttpInfo

> ApiResponse<ListBlogArticles200Response> listBlogArticles listBlogArticlesWithHttpInfo(accountId, blogId, limit, cursor)

List blog articles

Lists the articles of a blog. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support listing articles. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## listBlogs

> ListBlogs200Response listBlogs(accountId, limit, cursor)

List blogs

Lists the blogs on the connected store, newest-first as the platform returns them. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support listing blogs. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## listBlogsWithHttpInfo

> ApiResponse<ListBlogs200Response> listBlogs listBlogsWithHttpInfo(accountId, limit, cursor)

List blogs

Lists the blogs on the connected store, newest-first as the platform returns them. Cursor-paginated: pass &#x60;limit&#x60; (1-50, default 20) and the &#x60;cursor&#x60; from a previous response&#39;s &#x60;nextCursor&#x60;; &#x60;nextCursor&#x60; is null when there are no more pages.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found). |  -  |
| **405** | Platform does not support listing blogs. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## updateBlog

> CreateBlog201Response updateBlog(accountId, blogId, updateBlogRequest)

Update a blog

Partial-updates a blog. Send any subset of &#x60;title&#x60; and &#x60;handle&#x60;; at least one field is required (an empty body returns 400).  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
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
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support updating a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## updateBlogWithHttpInfo

> ApiResponse<CreateBlog201Response> updateBlog updateBlogWithHttpInfo(accountId, blogId, updateBlogRequest)

Update a blog

Partial-updates a blog. Send any subset of &#x60;title&#x60; and &#x60;handle&#x60;; at least one field is required (an empty body returns 400).  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
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
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), or blog not found (code blog_not_found). |  -  |
| **405** | Platform does not support updating a blog. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |


## updateBlogArticle

> CreateBlogArticle201Response updateBlogArticle(accountId, blogId, articleId, updateBlogArticleRequest)

Update a blog article

Partial-updates an article. Send any subset of the create fields (&#x60;title&#x60;, &#x60;bodyHtml&#x60;, &#x60;handle&#x60;, &#x60;tags&#x60;, &#x60;author&#x60;, &#x60;excerpt&#x60;, &#x60;image&#x60;, &#x60;seo&#x60;, &#x60;isPublished&#x60;, &#x60;publishDate&#x60;); at least one field is required (an empty body returns 400). &#x60;isPublished&#x60; and &#x60;publishDate&#x60; behave as on create: &#x60;isPublished: false&#x60; unpublishes back to a draft and a future &#x60;publishDate&#x60; schedules publication natively on the platform.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        String articleId = "articleId_example"; // String | Platform-native numeric article id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **articleId** | **String**| Platform-native numeric article id. Non-numeric values return 400. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support updating an article. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

## updateBlogArticleWithHttpInfo

> ApiResponse<CreateBlogArticle201Response> updateBlogArticle updateBlogArticleWithHttpInfo(accountId, blogId, articleId, updateBlogArticleRequest)

Update a blog article

Partial-updates an article. Send any subset of the create fields (&#x60;title&#x60;, &#x60;bodyHtml&#x60;, &#x60;handle&#x60;, &#x60;tags&#x60;, &#x60;author&#x60;, &#x60;excerpt&#x60;, &#x60;image&#x60;, &#x60;seo&#x60;, &#x60;isPublished&#x60;, &#x60;publishDate&#x60;); at least one field is required (an empty body returns 400). &#x60;isPublished&#x60; and &#x60;publishDate&#x60; behave as on create: &#x60;isPublished: false&#x60; unpublishes back to a draft and a future &#x60;publishDate&#x60; schedules publication natively on the platform.  Supported on Shopify (platform &#x60;shopify&#x60;). Accounts on platforms without blogs support return 400; a blogs-capable platform that lacks this specific operation returns 405. 

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
        String blogId = "blogId_example"; // String | Platform-native numeric blog id. Non-numeric values return 400.
        String articleId = "articleId_example"; // String | Platform-native numeric article id. Non-numeric values return 400.
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
| **accountId** | **String**| Connected Shopify SocialAccount id. | |
| **blogId** | **String**| Platform-native numeric blog id. Non-numeric values return 400. | |
| **articleId** | **String**| Platform-native numeric article id. Non-numeric values return 400. | |
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
| **401** | Unauthorized |  -  |
| **403** | The platform rejected the request (code insufficient_permissions); reconnect the Shopify account to restore access. |  -  |
| **404** | Account not found or not accessible (code account_not_found), blog not found (code blog_not_found), or article not found (code blog_article_not_found). |  -  |
| **405** | Platform does not support updating an article. |  -  |
| **429** | Rate limited, either by Zernio or by Shopify. Retry later. |  -  |

