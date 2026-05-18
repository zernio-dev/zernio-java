# InstagramApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInstagramStoryInsights**](InstagramApi.md#getInstagramStoryInsights) | **GET** /v1/accounts/{accountId}/instagram/stories/{storyId}/insights | Get Instagram story insights |
| [**getInstagramStoryInsightsWithHttpInfo**](InstagramApi.md#getInstagramStoryInsightsWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram/stories/{storyId}/insights | Get Instagram story insights |
| [**listInstagramStories**](InstagramApi.md#listInstagramStories) | **GET** /v1/accounts/{accountId}/instagram/stories | List active Instagram stories |
| [**listInstagramStoriesWithHttpInfo**](InstagramApi.md#listInstagramStoriesWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram/stories | List active Instagram stories |



## getInstagramStoryInsights

> GetInstagramStoryInsights200Response getInstagramStoryInsights(accountId, storyId)

Get Instagram story insights

Returns metrics for a single story. The &#x60;source&#x60; field discriminates between three states:  - &#x60;live&#x60; — fetched from Meta in real time (story is still active) - &#x60;cached&#x60; — fetched from a persisted &#x60;story_insights&#x60; webhook payload   (story has expired but we received its final-state metrics from Meta) - &#x60;unavailable&#x60; — story has expired and we never received its webhook   payload (for example, the account connected after the story expired)  Field semantics follow Meta&#39;s API. Counts below 5 may be returned as 0 due to Meta&#39;s privacy floor on small audiences. The &#x60;navigation&#x60; field is the sum of &#x60;tapsForward + tapsBack + exits + swipesForward&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InstagramApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InstagramApi apiInstance = new InstagramApi(defaultClient);
        String accountId = "accountId_example"; // String | The Instagram account ID
        String storyId = "storyId_example"; // String | The Instagram media ID of the story.
        try {
            GetInstagramStoryInsights200Response result = apiInstance.getInstagramStoryInsights(accountId, storyId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#getInstagramStoryInsights");
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
| **accountId** | **String**| The Instagram account ID | |
| **storyId** | **String**| The Instagram media ID of the story. | |

### Return type

[**GetInstagramStoryInsights200Response**](GetInstagramStoryInsights200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Story insights |  -  |
| **400** | Invalid request. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Instagram account not found. |  -  |

## getInstagramStoryInsightsWithHttpInfo

> ApiResponse<GetInstagramStoryInsights200Response> getInstagramStoryInsights getInstagramStoryInsightsWithHttpInfo(accountId, storyId)

Get Instagram story insights

Returns metrics for a single story. The &#x60;source&#x60; field discriminates between three states:  - &#x60;live&#x60; — fetched from Meta in real time (story is still active) - &#x60;cached&#x60; — fetched from a persisted &#x60;story_insights&#x60; webhook payload   (story has expired but we received its final-state metrics from Meta) - &#x60;unavailable&#x60; — story has expired and we never received its webhook   payload (for example, the account connected after the story expired)  Field semantics follow Meta&#39;s API. Counts below 5 may be returned as 0 due to Meta&#39;s privacy floor on small audiences. The &#x60;navigation&#x60; field is the sum of &#x60;tapsForward + tapsBack + exits + swipesForward&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InstagramApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InstagramApi apiInstance = new InstagramApi(defaultClient);
        String accountId = "accountId_example"; // String | The Instagram account ID
        String storyId = "storyId_example"; // String | The Instagram media ID of the story.
        try {
            ApiResponse<GetInstagramStoryInsights200Response> response = apiInstance.getInstagramStoryInsightsWithHttpInfo(accountId, storyId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#getInstagramStoryInsights");
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
| **accountId** | **String**| The Instagram account ID | |
| **storyId** | **String**| The Instagram media ID of the story. | |

### Return type

ApiResponse<[**GetInstagramStoryInsights200Response**](GetInstagramStoryInsights200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Story insights |  -  |
| **400** | Invalid request. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Instagram account not found. |  -  |


## listInstagramStories

> ListInstagramStories200Response listInstagramStories(accountId)

List active Instagram stories

Returns the IG Business/Creator account&#39;s currently-active stories. Meta keeps stories live for 24h; expired stories are not returned.  Limitations propagated from Meta (these are NOT bugs): - 24h window only - Live videos excluded - Reshared stories not returned - &#x60;mediaUrl&#x60; may be null if Meta flagged the story for copyright - &#x60;caption&#x60;, &#x60;likeCount&#x60;, &#x60;commentsCount&#x60; do not apply to story media 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InstagramApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InstagramApi apiInstance = new InstagramApi(defaultClient);
        String accountId = "accountId_example"; // String | The Instagram account ID
        try {
            ListInstagramStories200Response result = apiInstance.listInstagramStories(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#listInstagramStories");
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
| **accountId** | **String**| The Instagram account ID | |

### Return type

[**ListInstagramStories200Response**](ListInstagramStories200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Active stories |  -  |
| **400** | Invalid request. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Instagram account not found. |  -  |

## listInstagramStoriesWithHttpInfo

> ApiResponse<ListInstagramStories200Response> listInstagramStories listInstagramStoriesWithHttpInfo(accountId)

List active Instagram stories

Returns the IG Business/Creator account&#39;s currently-active stories. Meta keeps stories live for 24h; expired stories are not returned.  Limitations propagated from Meta (these are NOT bugs): - 24h window only - Live videos excluded - Reshared stories not returned - &#x60;mediaUrl&#x60; may be null if Meta flagged the story for copyright - &#x60;caption&#x60;, &#x60;likeCount&#x60;, &#x60;commentsCount&#x60; do not apply to story media 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InstagramApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InstagramApi apiInstance = new InstagramApi(defaultClient);
        String accountId = "accountId_example"; // String | The Instagram account ID
        try {
            ApiResponse<ListInstagramStories200Response> response = apiInstance.listInstagramStoriesWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#listInstagramStories");
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
| **accountId** | **String**| The Instagram account ID | |

### Return type

ApiResponse<[**ListInstagramStories200Response**](ListInstagramStories200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Active stories |  -  |
| **400** | Invalid request. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Instagram account not found. |  -  |

