# InstagramApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInstagramAudio**](InstagramApi.md#getInstagramAudio) | **GET** /v1/accounts/{accountId}/instagram/audio/{audioId} | Get Instagram audio metadata |
| [**getInstagramAudioWithHttpInfo**](InstagramApi.md#getInstagramAudioWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram/audio/{audioId} | Get Instagram audio metadata |
| [**getInstagramPublishingLimit**](InstagramApi.md#getInstagramPublishingLimit) | **GET** /v1/accounts/{accountId}/instagram/publishing-limit | Get Instagram publishing limit |
| [**getInstagramPublishingLimitWithHttpInfo**](InstagramApi.md#getInstagramPublishingLimitWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram/publishing-limit | Get Instagram publishing limit |
| [**getInstagramStoryInsights**](InstagramApi.md#getInstagramStoryInsights) | **GET** /v1/accounts/{accountId}/instagram/stories/{storyId}/insights | Get Instagram story insights |
| [**getInstagramStoryInsightsWithHttpInfo**](InstagramApi.md#getInstagramStoryInsightsWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram/stories/{storyId}/insights | Get Instagram story insights |
| [**listInstagramStories**](InstagramApi.md#listInstagramStories) | **GET** /v1/accounts/{accountId}/instagram/stories | List active Instagram stories |
| [**listInstagramStoriesWithHttpInfo**](InstagramApi.md#listInstagramStoriesWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram/stories | List active Instagram stories |
| [**searchInstagramAudio**](InstagramApi.md#searchInstagramAudio) | **GET** /v1/accounts/{accountId}/instagram/audio | Search Instagram audio |
| [**searchInstagramAudioWithHttpInfo**](InstagramApi.md#searchInstagramAudioWithHttpInfo) | **GET** /v1/accounts/{accountId}/instagram/audio | Search Instagram audio |



## getInstagramAudio

> GetInstagramAudio200Response getInstagramAudio(accountId, audioId)

Get Instagram audio metadata

Fetch one audio asset&#39;s metadata by ID. Use it to re-validate a stored &#x60;audioId&#x60; before a scheduled Reel publishes, or to refresh the preview &#x60;downloadUrl&#x60; (Meta expires preview URLs after roughly 1.5 days).  Same connection requirement as the search endpoint: Facebook-Login Instagram accounts only. 

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
        String accountId = "accountId_example"; // String | The ID of the Instagram account
        String audioId = "audioId_example"; // String | Instagram audio asset ID
        try {
            GetInstagramAudio200Response result = apiInstance.getInstagramAudio(accountId, audioId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#getInstagramAudio");
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
| **accountId** | **String**| The ID of the Instagram account | |
| **audioId** | **String**| Instagram audio asset ID | |

### Return type

[**GetInstagramAudio200Response**](GetInstagramAudio200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The audio asset |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram rejected the request |  -  |

## getInstagramAudioWithHttpInfo

> ApiResponse<GetInstagramAudio200Response> getInstagramAudio getInstagramAudioWithHttpInfo(accountId, audioId)

Get Instagram audio metadata

Fetch one audio asset&#39;s metadata by ID. Use it to re-validate a stored &#x60;audioId&#x60; before a scheduled Reel publishes, or to refresh the preview &#x60;downloadUrl&#x60; (Meta expires preview URLs after roughly 1.5 days).  Same connection requirement as the search endpoint: Facebook-Login Instagram accounts only. 

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
        String accountId = "accountId_example"; // String | The ID of the Instagram account
        String audioId = "audioId_example"; // String | Instagram audio asset ID
        try {
            ApiResponse<GetInstagramAudio200Response> response = apiInstance.getInstagramAudioWithHttpInfo(accountId, audioId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#getInstagramAudio");
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
| **accountId** | **String**| The ID of the Instagram account | |
| **audioId** | **String**| Instagram audio asset ID | |

### Return type

ApiResponse<[**GetInstagramAudio200Response**](GetInstagramAudio200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The audio asset |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram rejected the request |  -  |


## getInstagramPublishingLimit

> GetInstagramPublishingLimit200Response getInstagramPublishingLimit(accountId)

Get Instagram publishing limit

Returns the account&#39;s remaining content-publishing quota for Instagram&#39;s rolling 24-hour window, so you can pace publishing and warn before the cap is reached.  &#x60;quotaUsage&#x60; counts containers published since the start of the window. Always compare against the returned &#x60;quotaTotal&#x60; rather than hardcoding a number: Meta&#39;s prose documentation and the live API disagree on the value, and the live value is authoritative. 

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
        String accountId = "accountId_example"; // String | The ID of the Instagram account
        try {
            GetInstagramPublishingLimit200Response result = apiInstance.getInstagramPublishingLimit(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#getInstagramPublishingLimit");
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
| **accountId** | **String**| The ID of the Instagram account | |

### Return type

[**GetInstagramPublishingLimit200Response**](GetInstagramPublishingLimit200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Remaining publishing quota for the rolling window |  -  |
| **400** | Not an Instagram account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram rejected the request |  -  |

## getInstagramPublishingLimitWithHttpInfo

> ApiResponse<GetInstagramPublishingLimit200Response> getInstagramPublishingLimit getInstagramPublishingLimitWithHttpInfo(accountId)

Get Instagram publishing limit

Returns the account&#39;s remaining content-publishing quota for Instagram&#39;s rolling 24-hour window, so you can pace publishing and warn before the cap is reached.  &#x60;quotaUsage&#x60; counts containers published since the start of the window. Always compare against the returned &#x60;quotaTotal&#x60; rather than hardcoding a number: Meta&#39;s prose documentation and the live API disagree on the value, and the live value is authoritative. 

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
        String accountId = "accountId_example"; // String | The ID of the Instagram account
        try {
            ApiResponse<GetInstagramPublishingLimit200Response> response = apiInstance.getInstagramPublishingLimitWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#getInstagramPublishingLimit");
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
| **accountId** | **String**| The ID of the Instagram account | |

### Return type

ApiResponse<[**GetInstagramPublishingLimit200Response**](GetInstagramPublishingLimit200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Remaining publishing quota for the rolling window |  -  |
| **400** | Not an Instagram account |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram rejected the request |  -  |


## getInstagramStoryInsights

> GetInstagramStoryInsights200Response getInstagramStoryInsights(accountId, storyId)

Get Instagram story insights

Returns metrics for a single story. The &#x60;source&#x60; field discriminates between three states:  - &#x60;live&#x60; — fetched from Meta in real time (story is still active) - &#x60;cached&#x60; — fetched from a persisted &#x60;story_insights&#x60; webhook payload   (story has expired but we received its final-state metrics from Meta) - &#x60;unavailable&#x60; — story has expired and we never received its webhook   payload (for example, the account connected after the story expired)  Meta can report an expired story as an empty successful result rather than an error, so an expired story resolves to &#x60;cached&#x60; or &#x60;unavailable&#x60; even though the upstream request itself succeeded.  Field semantics follow Meta&#39;s API. Counts below 5 may be returned as 0 due to Meta&#39;s privacy floor on small audiences. The &#x60;navigation&#x60; field is the sum of &#x60;tapsForward + tapsBack + exits + swipesForward&#x60;. 

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
| **502** | Instagram rejected the request. |  -  |

## getInstagramStoryInsightsWithHttpInfo

> ApiResponse<GetInstagramStoryInsights200Response> getInstagramStoryInsights getInstagramStoryInsightsWithHttpInfo(accountId, storyId)

Get Instagram story insights

Returns metrics for a single story. The &#x60;source&#x60; field discriminates between three states:  - &#x60;live&#x60; — fetched from Meta in real time (story is still active) - &#x60;cached&#x60; — fetched from a persisted &#x60;story_insights&#x60; webhook payload   (story has expired but we received its final-state metrics from Meta) - &#x60;unavailable&#x60; — story has expired and we never received its webhook   payload (for example, the account connected after the story expired)  Meta can report an expired story as an empty successful result rather than an error, so an expired story resolves to &#x60;cached&#x60; or &#x60;unavailable&#x60; even though the upstream request itself succeeded.  Field semantics follow Meta&#39;s API. Counts below 5 may be returned as 0 due to Meta&#39;s privacy floor on small audiences. The &#x60;navigation&#x60; field is the sum of &#x60;tapsForward + tapsBack + exits + swipesForward&#x60;. 

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
| **502** | Instagram rejected the request. |  -  |


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


## searchInstagramAudio

> SearchInstagramAudio200Response searchInstagramAudio(accountId, audioType, q)

Search Instagram audio

Search Instagram&#39;s audio catalog (licensed music or original sounds), or list what is currently trending by omitting &#x60;q&#x60;. Returns up to ~30 assets; Meta exposes no pagination on this edge.  Pass the returned &#x60;audioId&#x60; as &#x60;platformSpecificData.audioConfiguration.audioId&#x60; when creating a Reel to publish it with that track.  Requires an Instagram account connected via **Facebook Login**. Meta hosts this catalog on graph.facebook.com only, so accounts connected with classic Instagram Login receive a 400 (&#x60;instagram_audio_requires_facebook_login&#x60;) and must be reconnected choosing the Facebook option. 

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
        String accountId = "accountId_example"; // String | The ID of the Instagram account
        String audioType = "music"; // String | Catalog to search: licensed music or original sounds from Reels.
        String q = "q_example"; // String | Search keywords. Omit to get the current trending list.
        try {
            SearchInstagramAudio200Response result = apiInstance.searchInstagramAudio(accountId, audioType, q);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#searchInstagramAudio");
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
| **accountId** | **String**| The ID of the Instagram account | |
| **audioType** | **String**| Catalog to search: licensed music or original sounds from Reels. | [enum: music, original_sound] |
| **q** | **String**| Search keywords. Omit to get the current trending list. | [optional] |

### Return type

[**SearchInstagramAudio200Response**](SearchInstagramAudio200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching audio assets (may be empty) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram rejected the request |  -  |

## searchInstagramAudioWithHttpInfo

> ApiResponse<SearchInstagramAudio200Response> searchInstagramAudio searchInstagramAudioWithHttpInfo(accountId, audioType, q)

Search Instagram audio

Search Instagram&#39;s audio catalog (licensed music or original sounds), or list what is currently trending by omitting &#x60;q&#x60;. Returns up to ~30 assets; Meta exposes no pagination on this edge.  Pass the returned &#x60;audioId&#x60; as &#x60;platformSpecificData.audioConfiguration.audioId&#x60; when creating a Reel to publish it with that track.  Requires an Instagram account connected via **Facebook Login**. Meta hosts this catalog on graph.facebook.com only, so accounts connected with classic Instagram Login receive a 400 (&#x60;instagram_audio_requires_facebook_login&#x60;) and must be reconnected choosing the Facebook option. 

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
        String accountId = "accountId_example"; // String | The ID of the Instagram account
        String audioType = "music"; // String | Catalog to search: licensed music or original sounds from Reels.
        String q = "q_example"; // String | Search keywords. Omit to get the current trending list.
        try {
            ApiResponse<SearchInstagramAudio200Response> response = apiInstance.searchInstagramAudioWithHttpInfo(accountId, audioType, q);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InstagramApi#searchInstagramAudio");
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
| **accountId** | **String**| The ID of the Instagram account | |
| **audioType** | **String**| Catalog to search: licensed music or original sounds from Reels. | [enum: music, original_sound] |
| **q** | **String**| Search keywords. Omit to get the current trending list. | [optional] |

### Return type

ApiResponse<[**SearchInstagramAudio200Response**](SearchInstagramAudio200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching audio assets (may be empty) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram rejected the request |  -  |

