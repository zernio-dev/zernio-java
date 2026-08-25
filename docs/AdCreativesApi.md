# AdCreativesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdCreative**](AdCreativesApi.md#createAdCreative) | **POST** /v1/ads/creatives | Create a standalone creative |
| [**createAdCreativeWithHttpInfo**](AdCreativesApi.md#createAdCreativeWithHttpInfo) | **POST** /v1/ads/creatives | Create a standalone creative |
| [**deleteAdCreative**](AdCreativesApi.md#deleteAdCreative) | **DELETE** /v1/ads/creatives/{creativeId} | Delete a creative |
| [**deleteAdCreativeWithHttpInfo**](AdCreativesApi.md#deleteAdCreativeWithHttpInfo) | **DELETE** /v1/ads/creatives/{creativeId} | Delete a creative |
| [**deleteAdVideo**](AdCreativesApi.md#deleteAdVideo) | **DELETE** /v1/ads/videos/{videoId} | Delete an ad video |
| [**deleteAdVideoWithHttpInfo**](AdCreativesApi.md#deleteAdVideoWithHttpInfo) | **DELETE** /v1/ads/videos/{videoId} | Delete an ad video |
| [**generateAdPreviews**](AdCreativesApi.md#generateAdPreviews) | **POST** /v1/ads/preview | Render pre-create ad previews |
| [**generateAdPreviewsWithHttpInfo**](AdCreativesApi.md#generateAdPreviewsWithHttpInfo) | **POST** /v1/ads/preview | Render pre-create ad previews |
| [**getAdCreative**](AdCreativesApi.md#getAdCreative) | **GET** /v1/ads/creatives/{creativeId} | Creative details |
| [**getAdCreativeWithHttpInfo**](AdCreativesApi.md#getAdCreativeWithHttpInfo) | **GET** /v1/ads/creatives/{creativeId} | Creative details |
| [**getAdMedia**](AdCreativesApi.md#getAdMedia) | **GET** /v1/ads/{adId}/media | Direct video and image URLs for an ad |
| [**getAdMediaWithHttpInfo**](AdCreativesApi.md#getAdMediaWithHttpInfo) | **GET** /v1/ads/{adId}/media | Direct video and image URLs for an ad |
| [**getAdPreviews**](AdCreativesApi.md#getAdPreviews) | **GET** /v1/ads/{adId}/preview | Render previews of an existing ad |
| [**getAdPreviewsWithHttpInfo**](AdCreativesApi.md#getAdPreviewsWithHttpInfo) | **GET** /v1/ads/{adId}/preview | Render previews of an existing ad |
| [**listAdCatalogProductSets**](AdCreativesApi.md#listAdCatalogProductSets) | **GET** /v1/ads/catalogs/{catalogId}/product-sets | List a catalog&#39;s product sets |
| [**listAdCatalogProductSetsWithHttpInfo**](AdCreativesApi.md#listAdCatalogProductSetsWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/product-sets | List a catalog&#39;s product sets |
| [**listAdCatalogs**](AdCreativesApi.md#listAdCatalogs) | **GET** /v1/ads/catalogs | List Meta product catalogs |
| [**listAdCatalogsWithHttpInfo**](AdCreativesApi.md#listAdCatalogsWithHttpInfo) | **GET** /v1/ads/catalogs | List Meta product catalogs |
| [**listAdCreatives**](AdCreativesApi.md#listAdCreatives) | **GET** /v1/ads/creatives | Creative library |
| [**listAdCreativesWithHttpInfo**](AdCreativesApi.md#listAdCreativesWithHttpInfo) | **GET** /v1/ads/creatives | Creative library |
| [**listAdImages**](AdCreativesApi.md#listAdImages) | **GET** /v1/ads/images | Ad image library |
| [**listAdImagesWithHttpInfo**](AdCreativesApi.md#listAdImagesWithHttpInfo) | **GET** /v1/ads/images | Ad image library |
| [**listAdVideos**](AdCreativesApi.md#listAdVideos) | **GET** /v1/ads/videos | Ad video library |
| [**listAdVideosWithHttpInfo**](AdCreativesApi.md#listAdVideosWithHttpInfo) | **GET** /v1/ads/videos | Ad video library |
| [**updateAdCreative**](AdCreativesApi.md#updateAdCreative) | **PUT** /v1/ads/creatives/{creativeId} | Rename a creative |
| [**updateAdCreativeWithHttpInfo**](AdCreativesApi.md#updateAdCreativeWithHttpInfo) | **PUT** /v1/ads/creatives/{creativeId} | Rename a creative |
| [**uploadAdImage**](AdCreativesApi.md#uploadAdImage) | **POST** /v1/ads/images | Upload an ad image from base64 |
| [**uploadAdImageWithHttpInfo**](AdCreativesApi.md#uploadAdImageWithHttpInfo) | **POST** /v1/ads/images | Upload an ad image from base64 |
| [**uploadAdVideo**](AdCreativesApi.md#uploadAdVideo) | **POST** /v1/ads/videos | Upload an ad video |
| [**uploadAdVideoWithHttpInfo**](AdCreativesApi.md#uploadAdVideoWithHttpInfo) | **POST** /v1/ads/videos | Upload an ad video |



## createAdCreative

> CreateAdCreative201Response createAdCreative(createAdCreativeRequest)

Create a standalone creative

Creates a creative in the library WITHOUT an ad, reusable on the create endpoints via &#x60;existingCreativeId&#x60;. Provide exactly one of &#x60;imageUrl&#x60; (uploaded server-side), &#x60;imageHash&#x60; (from POST /v1/ads/images or the library list), or &#x60;carouselCards&#x60; (2-10 hand-built cards). The Page (and linked Instagram account, when present) is resolved from &#x60;accountId&#x60; as the story actor.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        CreateAdCreativeRequest createAdCreativeRequest = new CreateAdCreativeRequest(); // CreateAdCreativeRequest | 
        try {
            CreateAdCreative201Response result = apiInstance.createAdCreative(createAdCreativeRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#createAdCreative");
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
| **createAdCreativeRequest** | [**CreateAdCreativeRequest**](CreateAdCreativeRequest.md)|  | |

### Return type

[**CreateAdCreative201Response**](CreateAdCreative201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Creative created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page found to act as the story actor |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |

## createAdCreativeWithHttpInfo

> ApiResponse<CreateAdCreative201Response> createAdCreative createAdCreativeWithHttpInfo(createAdCreativeRequest)

Create a standalone creative

Creates a creative in the library WITHOUT an ad, reusable on the create endpoints via &#x60;existingCreativeId&#x60;. Provide exactly one of &#x60;imageUrl&#x60; (uploaded server-side), &#x60;imageHash&#x60; (from POST /v1/ads/images or the library list), or &#x60;carouselCards&#x60; (2-10 hand-built cards). The Page (and linked Instagram account, when present) is resolved from &#x60;accountId&#x60; as the story actor.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        CreateAdCreativeRequest createAdCreativeRequest = new CreateAdCreativeRequest(); // CreateAdCreativeRequest | 
        try {
            ApiResponse<CreateAdCreative201Response> response = apiInstance.createAdCreativeWithHttpInfo(createAdCreativeRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#createAdCreative");
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
| **createAdCreativeRequest** | [**CreateAdCreativeRequest**](CreateAdCreativeRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCreative201Response**](CreateAdCreative201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Creative created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page found to act as the story actor |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |


## deleteAdCreative

> DeleteAdCreative200Response deleteAdCreative(creativeId, accountId)

Delete a creative

Deletes a creative from the library. Meta only allows deleting creatives not referenced by any ad — otherwise its 400 surfaces verbatim.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            DeleteAdCreative200Response result = apiInstance.deleteAdCreative(creativeId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#deleteAdCreative");
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
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

[**DeleteAdCreative200Response**](DeleteAdCreative200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative deleted |  -  |
| **400** | Invalid input, the creative is in use, or Meta rejected the delete |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## deleteAdCreativeWithHttpInfo

> ApiResponse<DeleteAdCreative200Response> deleteAdCreative deleteAdCreativeWithHttpInfo(creativeId, accountId)

Delete a creative

Deletes a creative from the library. Meta only allows deleting creatives not referenced by any ad — otherwise its 400 surfaces verbatim.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            ApiResponse<DeleteAdCreative200Response> response = apiInstance.deleteAdCreativeWithHttpInfo(creativeId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#deleteAdCreative");
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
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

ApiResponse<[**DeleteAdCreative200Response**](DeleteAdCreative200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative deleted |  -  |
| **400** | Invalid input, the creative is in use, or Meta rejected the delete |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## deleteAdVideo

> DeleteAdVideo200Response deleteAdVideo(videoId, accountId, adAccountId)

Delete an ad video

Removes a video from the ad account&#39;s video library. Meta&#39;s canonical &#x60;DELETE /{video_id}&#x60; fails with code 10 / subcode 1363055 for videos uploaded via &#x60;/act_X/advideos&#x60; even with &#x60;ads_management&#x60;; this endpoint uses the working account-scoped shape &#x60;DELETE /act_X/advideos?video_id&#x3D;&lt;id&gt;&#x60; and returns Meta&#39;s &#x60;{success: true}&#x60; verbatim. Deleting a video that lives in a different ad account, or that Meta has already removed, returns Meta&#39;s error verbatim as a 4xx.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String videoId = "videoId_example"; // String | Meta ad video id (numeric).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>) that owns the video.
        try {
            DeleteAdVideo200Response result = apiInstance.deleteAdVideo(videoId, accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#deleteAdVideo");
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
| **videoId** | **String**| Meta ad video id (numeric). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;) that owns the video. | |

### Return type

[**DeleteAdVideo200Response**](DeleteAdVideo200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Video deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## deleteAdVideoWithHttpInfo

> ApiResponse<DeleteAdVideo200Response> deleteAdVideo deleteAdVideoWithHttpInfo(videoId, accountId, adAccountId)

Delete an ad video

Removes a video from the ad account&#39;s video library. Meta&#39;s canonical &#x60;DELETE /{video_id}&#x60; fails with code 10 / subcode 1363055 for videos uploaded via &#x60;/act_X/advideos&#x60; even with &#x60;ads_management&#x60;; this endpoint uses the working account-scoped shape &#x60;DELETE /act_X/advideos?video_id&#x3D;&lt;id&gt;&#x60; and returns Meta&#39;s &#x60;{success: true}&#x60; verbatim. Deleting a video that lives in a different ad account, or that Meta has already removed, returns Meta&#39;s error verbatim as a 4xx.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String videoId = "videoId_example"; // String | Meta ad video id (numeric).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>) that owns the video.
        try {
            ApiResponse<DeleteAdVideo200Response> response = apiInstance.deleteAdVideoWithHttpInfo(videoId, accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#deleteAdVideo");
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
| **videoId** | **String**| Meta ad video id (numeric). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;) that owns the video. | |

### Return type

ApiResponse<[**DeleteAdVideo200Response**](DeleteAdVideo200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Video deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## generateAdPreviews

> GenerateAdPreviews200Response generateAdPreviews(generateAdPreviewsRequest)

Render pre-create ad previews

Renders how a creative would look per placement BEFORE any ad exists, via Meta&#39;s &#x60;/generatepreviews&#x60;. Provide exactly one creative source: &#x60;existingCreativeId&#x60; or &#x60;creativeSpec&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        GenerateAdPreviewsRequest generateAdPreviewsRequest = new GenerateAdPreviewsRequest(); // GenerateAdPreviewsRequest | 
        try {
            GenerateAdPreviews200Response result = apiInstance.generateAdPreviews(generateAdPreviewsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#generateAdPreviews");
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
| **generateAdPreviewsRequest** | [**GenerateAdPreviewsRequest**](GenerateAdPreviewsRequest.md)|  | |

### Return type

[**GenerateAdPreviews200Response**](GenerateAdPreviews200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the creative spec / ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## generateAdPreviewsWithHttpInfo

> ApiResponse<GenerateAdPreviews200Response> generateAdPreviews generateAdPreviewsWithHttpInfo(generateAdPreviewsRequest)

Render pre-create ad previews

Renders how a creative would look per placement BEFORE any ad exists, via Meta&#39;s &#x60;/generatepreviews&#x60;. Provide exactly one creative source: &#x60;existingCreativeId&#x60; or &#x60;creativeSpec&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        GenerateAdPreviewsRequest generateAdPreviewsRequest = new GenerateAdPreviewsRequest(); // GenerateAdPreviewsRequest | 
        try {
            ApiResponse<GenerateAdPreviews200Response> response = apiInstance.generateAdPreviewsWithHttpInfo(generateAdPreviewsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#generateAdPreviews");
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
| **generateAdPreviewsRequest** | [**GenerateAdPreviewsRequest**](GenerateAdPreviewsRequest.md)|  | |

### Return type

ApiResponse<[**GenerateAdPreviews200Response**](GenerateAdPreviews200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the creative spec / ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdCreative

> GetAdCreative200Response getAdCreative(creativeId, accountId, fields)

Creative details

One creative&#39;s details, verbatim from Meta. &#x60;fields&#x60; is a raw-passthrough override of the default projection.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            GetAdCreative200Response result = apiInstance.getAdCreative(creativeId, accountId, fields);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#getAdCreative");
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
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

[**GetAdCreative200Response**](GetAdCreative200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative details |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdCreativeWithHttpInfo

> ApiResponse<GetAdCreative200Response> getAdCreative getAdCreativeWithHttpInfo(creativeId, accountId, fields)

Creative details

One creative&#39;s details, verbatim from Meta. &#x60;fields&#x60; is a raw-passthrough override of the default projection.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            ApiResponse<GetAdCreative200Response> response = apiInstance.getAdCreativeWithHttpInfo(creativeId, accountId, fields);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#getAdCreative");
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
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

ApiResponse<[**GetAdCreative200Response**](GetAdCreative200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative details |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdMedia

> GetAdMedia200Response getAdMedia(adId)

Direct video and image URLs for an ad

Returns the direct signed URLs for every video and image asset used by an ad&#39;s live creative, normalised across shapes: single image/video, carousel, Reels/Story (&#x60;object_story_spec.video_data&#x60;) and dynamic creative (&#x60;asset_feed_spec&#x60;). Video items include Meta&#39;s poster thumbnail and the video&#39;s Meta id when available.  Reads Meta live rather than the stored creative blob because Meta&#39;s signed fbcdn URLs carry an &#x60;oe&#x3D;&lt;hex&gt;&#x60; expiration (image_url ~24 h, video source ~12 d). Treat URLs as short-lived — re-fetch this endpoint before serving or downloading assets instead of caching URLs beyond that window.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex) or platform ad id.
        try {
            GetAdMedia200Response result = apiInstance.getAdMedia(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#getAdMedia");
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
| **adId** | **String**| Zernio ad id (24-char hex) or platform ad id. | |

### Return type

[**GetAdMedia200Response**](GetAdMedia200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Media assets |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **422** | No active Meta connection for this ad. Reconnect the account. |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdMediaWithHttpInfo

> ApiResponse<GetAdMedia200Response> getAdMedia getAdMediaWithHttpInfo(adId)

Direct video and image URLs for an ad

Returns the direct signed URLs for every video and image asset used by an ad&#39;s live creative, normalised across shapes: single image/video, carousel, Reels/Story (&#x60;object_story_spec.video_data&#x60;) and dynamic creative (&#x60;asset_feed_spec&#x60;). Video items include Meta&#39;s poster thumbnail and the video&#39;s Meta id when available.  Reads Meta live rather than the stored creative blob because Meta&#39;s signed fbcdn URLs carry an &#x60;oe&#x3D;&lt;hex&gt;&#x60; expiration (image_url ~24 h, video source ~12 d). Treat URLs as short-lived — re-fetch this endpoint before serving or downloading assets instead of caching URLs beyond that window.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex) or platform ad id.
        try {
            ApiResponse<GetAdMedia200Response> response = apiInstance.getAdMediaWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#getAdMedia");
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
| **adId** | **String**| Zernio ad id (24-char hex) or platform ad id. | |

### Return type

ApiResponse<[**GetAdMedia200Response**](GetAdMedia200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Media assets |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **422** | No active Meta connection for this ad. Reconnect the account. |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdPreviews

> GetAdPreviews200Response getAdPreviews(adId, formats)

Render previews of an existing ad

Renders an EXISTING ad per placement via Meta&#39;s &#x60;/{ad_id}/previews&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex).
        String formats = "formats_example"; // String | Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD.
        try {
            GetAdPreviews200Response result = apiInstance.getAdPreviews(adId, formats);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#getAdPreviews");
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
| **adId** | **String**| Zernio ad id (24-char hex). | |
| **formats** | **String**| Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD. | [optional] |

### Return type

[**GetAdPreviews200Response**](GetAdPreviews200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdPreviewsWithHttpInfo

> ApiResponse<GetAdPreviews200Response> getAdPreviews getAdPreviewsWithHttpInfo(adId, formats)

Render previews of an existing ad

Renders an EXISTING ad per placement via Meta&#39;s &#x60;/{ad_id}/previews&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex).
        String formats = "formats_example"; // String | Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD.
        try {
            ApiResponse<GetAdPreviews200Response> response = apiInstance.getAdPreviewsWithHttpInfo(adId, formats);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#getAdPreviews");
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
| **adId** | **String**| Zernio ad id (24-char hex). | |
| **formats** | **String**| Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD. | [optional] |

### Return type

ApiResponse<[**GetAdPreviews200Response**](GetAdPreviews200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdCatalogProductSets

> ListAdCatalogProductSets200Response listAdCatalogProductSets(catalogId, accountId)

List a catalog&#39;s product sets

Lists a Meta product catalog&#39;s product sets — the unit a catalog ad promotes. Pass the chosen set as &#x60;promotedObject.productSetId&#x60; on POST /v1/ads/create with &#x60;goal: catalog_sales&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        try {
            ListAdCatalogProductSets200Response result = apiInstance.listAdCatalogProductSets(catalogId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdCatalogProductSets");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |

### Return type

[**ListAdCatalogProductSets200Response**](ListAdCatalogProductSets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdCatalogProductSetsWithHttpInfo

> ApiResponse<ListAdCatalogProductSets200Response> listAdCatalogProductSets listAdCatalogProductSetsWithHttpInfo(catalogId, accountId)

List a catalog&#39;s product sets

Lists a Meta product catalog&#39;s product sets — the unit a catalog ad promotes. Pass the chosen set as &#x60;promotedObject.productSetId&#x60; on POST /v1/ads/create with &#x60;goal: catalog_sales&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        try {
            ApiResponse<ListAdCatalogProductSets200Response> response = apiInstance.listAdCatalogProductSetsWithHttpInfo(catalogId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdCatalogProductSets");
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
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |

### Return type

ApiResponse<[**ListAdCatalogProductSets200Response**](ListAdCatalogProductSets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdCatalogs

> ListAdCatalogs200Response listAdCatalogs(accountId, adAccountId)

List Meta product catalogs

Lists the Meta product catalogs reachable from an ad account (owned + agency-shared catalogs of the ad account&#39;s business), for Advantage+ catalog ads (&#x60;goal: catalog_sales&#x60; on POST /v1/ads/create — e.g. vehicle inventory catalogs). Read-only; uses scopes customers already granted (no reconnect needed). Catalog contents (items, feeds) are managed in Meta Commerce Manager, not through this API.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ListAdCatalogs200Response result = apiInstance.listAdCatalogs(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdCatalogs");
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
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

[**ListAdCatalogs200Response**](ListAdCatalogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalogs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdCatalogsWithHttpInfo

> ApiResponse<ListAdCatalogs200Response> listAdCatalogs listAdCatalogsWithHttpInfo(accountId, adAccountId)

List Meta product catalogs

Lists the Meta product catalogs reachable from an ad account (owned + agency-shared catalogs of the ad account&#39;s business), for Advantage+ catalog ads (&#x60;goal: catalog_sales&#x60; on POST /v1/ads/create — e.g. vehicle inventory catalogs). Read-only; uses scopes customers already granted (no reconnect needed). Catalog contents (items, feeds) are managed in Meta Commerce Manager, not through this API.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ApiResponse<ListAdCatalogs200Response> response = apiInstance.listAdCatalogsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdCatalogs");
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
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

ApiResponse<[**ListAdCatalogs200Response**](ListAdCatalogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalogs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdCreatives

> ListAdCreatives200Response listAdCreatives(accountId, adAccountId, fields, limit, after)

Creative library

Lists the ad account&#39;s creative library (Meta&#39;s &#x60;/act_X/adcreatives&#x60;), rows returned verbatim. The default projection covers id, name, status, object type, thumbnail, object_story_spec / asset_feed_spec and url_tags; &#x60;fields&#x60; is a raw-passthrough override. Any creative id here is reusable on the create endpoints via &#x60;existingCreativeId&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdCreatives200Response result = apiInstance.listAdCreatives(accountId, adAccountId, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdCreatives");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdCreatives200Response**](ListAdCreatives200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdCreativesWithHttpInfo

> ApiResponse<ListAdCreatives200Response> listAdCreatives listAdCreativesWithHttpInfo(accountId, adAccountId, fields, limit, after)

Creative library

Lists the ad account&#39;s creative library (Meta&#39;s &#x60;/act_X/adcreatives&#x60;), rows returned verbatim. The default projection covers id, name, status, object type, thumbnail, object_story_spec / asset_feed_spec and url_tags; &#x60;fields&#x60; is a raw-passthrough override. Any creative id here is reusable on the create endpoints via &#x60;existingCreativeId&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdCreatives200Response> response = apiInstance.listAdCreativesWithHttpInfo(accountId, adAccountId, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdCreatives");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdCreatives200Response**](ListAdCreatives200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdImages

> ListAdImages200Response listAdImages(accountId, adAccountId, fields, limit, after)

Ad image library

Lists the ad account&#39;s image library (Meta&#39;s &#x60;/act_X/adimages&#x60;), rows returned verbatim. The default projection covers hash, url, name, dimensions and status; &#x60;fields&#x60; is a raw-passthrough override. Any &#x60;hash&#x60; here is reusable wherever Meta accepts &#x60;image_hash&#x60; (e.g. &#x60;imageHash&#x60; on POST /v1/ads/creatives).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdImages200Response result = apiInstance.listAdImages(accountId, adAccountId, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdImages");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdImages200Response**](ListAdImages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad images (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdImagesWithHttpInfo

> ApiResponse<ListAdImages200Response> listAdImages listAdImagesWithHttpInfo(accountId, adAccountId, fields, limit, after)

Ad image library

Lists the ad account&#39;s image library (Meta&#39;s &#x60;/act_X/adimages&#x60;), rows returned verbatim. The default projection covers hash, url, name, dimensions and status; &#x60;fields&#x60; is a raw-passthrough override. Any &#x60;hash&#x60; here is reusable wherever Meta accepts &#x60;image_hash&#x60; (e.g. &#x60;imageHash&#x60; on POST /v1/ads/creatives).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdImages200Response> response = apiInstance.listAdImagesWithHttpInfo(accountId, adAccountId, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdImages");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdImages200Response**](ListAdImages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad images (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdVideos

> ListAdVideos200Response listAdVideos(accountId, adAccountId, fields, limit, after)

Ad video library

Lists the ad account&#39;s video library (Meta&#39;s &#x60;/act_X/advideos&#x60;), rows returned verbatim. The default projection covers id, title, status, poster frames and length; &#x60;fields&#x60; is a raw-passthrough override. Any &#x60;id&#x60; here is reusable as &#x60;video.id&#x60; on the create endpoints, so N ads that differ only in copy share one upload.  This is the only way to reach a video uploaded OUTSIDE Zernio (Ads Manager, another tool); videos we uploaded also come back as &#x60;creative.videoId&#x60; on GET /v1/ads.  Meta transcodes asynchronously, so a row is only usable once &#x60;status.video_status&#x60; reads &#x60;ready&#x60;. Upload a new video via POST /v1/ads/videos, or inline via &#x60;video.url&#x60; on POST /v1/ads/create.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdVideos200Response result = apiInstance.listAdVideos(accountId, adAccountId, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdVideos");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdVideos200Response**](ListAdVideos200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad videos (raw Meta shape) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdVideosWithHttpInfo

> ApiResponse<ListAdVideos200Response> listAdVideos listAdVideosWithHttpInfo(accountId, adAccountId, fields, limit, after)

Ad video library

Lists the ad account&#39;s video library (Meta&#39;s &#x60;/act_X/advideos&#x60;), rows returned verbatim. The default projection covers id, title, status, poster frames and length; &#x60;fields&#x60; is a raw-passthrough override. Any &#x60;id&#x60; here is reusable as &#x60;video.id&#x60; on the create endpoints, so N ads that differ only in copy share one upload.  This is the only way to reach a video uploaded OUTSIDE Zernio (Ads Manager, another tool); videos we uploaded also come back as &#x60;creative.videoId&#x60; on GET /v1/ads.  Meta transcodes asynchronously, so a row is only usable once &#x60;status.video_status&#x60; reads &#x60;ready&#x60;. Upload a new video via POST /v1/ads/videos, or inline via &#x60;video.url&#x60; on POST /v1/ads/create.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdVideos200Response> response = apiInstance.listAdVideosWithHttpInfo(accountId, adAccountId, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#listAdVideos");
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
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdVideos200Response**](ListAdVideos200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad videos (raw Meta shape) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## updateAdCreative

> UpdateAdCreative200Response updateAdCreative(creativeId, updateAdCreativeRequest)

Rename a creative

Renames a creative. Creatives are immutable on Meta beyond &#x60;name&#x60; — for content changes create a new creative (POST /v1/ads/creatives) and swap it onto the ad (PUT /v1/ads/{adId} with &#x60;creative&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        UpdateAdCreativeRequest updateAdCreativeRequest = new UpdateAdCreativeRequest(); // UpdateAdCreativeRequest | 
        try {
            UpdateAdCreative200Response result = apiInstance.updateAdCreative(creativeId, updateAdCreativeRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#updateAdCreative");
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
| **creativeId** | **String**| Platform creative id | |
| **updateAdCreativeRequest** | [**UpdateAdCreativeRequest**](UpdateAdCreativeRequest.md)|  | |

### Return type

[**UpdateAdCreative200Response**](UpdateAdCreative200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative renamed |  -  |
| **400** | Invalid input, or Meta rejected the update |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## updateAdCreativeWithHttpInfo

> ApiResponse<UpdateAdCreative200Response> updateAdCreative updateAdCreativeWithHttpInfo(creativeId, updateAdCreativeRequest)

Rename a creative

Renames a creative. Creatives are immutable on Meta beyond &#x60;name&#x60; — for content changes create a new creative (POST /v1/ads/creatives) and swap it onto the ad (PUT /v1/ads/{adId} with &#x60;creative&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        UpdateAdCreativeRequest updateAdCreativeRequest = new UpdateAdCreativeRequest(); // UpdateAdCreativeRequest | 
        try {
            ApiResponse<UpdateAdCreative200Response> response = apiInstance.updateAdCreativeWithHttpInfo(creativeId, updateAdCreativeRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#updateAdCreative");
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
| **creativeId** | **String**| Platform creative id | |
| **updateAdCreativeRequest** | [**UpdateAdCreativeRequest**](UpdateAdCreativeRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCreative200Response**](UpdateAdCreative200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative renamed |  -  |
| **400** | Invalid input, or Meta rejected the update |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## uploadAdImage

> UploadAdImage201Response uploadAdImage(uploadAdImageRequest)

Upload an ad image from base64

Uploads raw image bytes to the Meta ad account&#39;s image library — for callers whose creatives aren&#39;t hosted at a public URL. Returns the image &#x60;hash&#x60; (Meta&#39;s identifier for the asset) and the Meta-hosted &#x60;url&#x60;, which can be used directly as &#x60;imageUrl&#x60; on the create endpoints. Max 30 MB decoded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        UploadAdImageRequest uploadAdImageRequest = new UploadAdImageRequest(); // UploadAdImageRequest | 
        try {
            UploadAdImage201Response result = apiInstance.uploadAdImage(uploadAdImageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#uploadAdImage");
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
| **uploadAdImageRequest** | [**UploadAdImageRequest**](UploadAdImageRequest.md)|  | |

### Return type

[**UploadAdImage201Response**](UploadAdImage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Image uploaded |  -  |
| **400** | Invalid input, or Meta rejected the image |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |

## uploadAdImageWithHttpInfo

> ApiResponse<UploadAdImage201Response> uploadAdImage uploadAdImageWithHttpInfo(uploadAdImageRequest)

Upload an ad image from base64

Uploads raw image bytes to the Meta ad account&#39;s image library — for callers whose creatives aren&#39;t hosted at a public URL. Returns the image &#x60;hash&#x60; (Meta&#39;s identifier for the asset) and the Meta-hosted &#x60;url&#x60;, which can be used directly as &#x60;imageUrl&#x60; on the create endpoints. Max 30 MB decoded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        UploadAdImageRequest uploadAdImageRequest = new UploadAdImageRequest(); // UploadAdImageRequest | 
        try {
            ApiResponse<UploadAdImage201Response> response = apiInstance.uploadAdImageWithHttpInfo(uploadAdImageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#uploadAdImage");
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
| **uploadAdImageRequest** | [**UploadAdImageRequest**](UploadAdImageRequest.md)|  | |

### Return type

ApiResponse<[**UploadAdImage201Response**](UploadAdImage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Image uploaded |  -  |
| **400** | Invalid input, or Meta rejected the image |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |


## uploadAdVideo

> UploadAdVideo201Response uploadAdVideo(uploadAdVideoRequest)

Upload an ad video

Standalone ad-video upload (parallel to POST /v1/ads/images), so a video creative can be rendered via POST /v1/ads/preview or attached via &#x60;video.id&#x60; on POST /v1/ads/create before an ad exists.  Accepts either an https &#x60;videoUrl&#x60; we download server-side (SSRF-guarded) or raw &#x60;videoBase64&#x60; bytes; exactly one is required. &#x60;videoBase64&#x60; is capped by Vercel&#39;s body limit — around 4.5 MB payload in practice, so larger videos must come via &#x60;videoUrl&#x60;.  Returns the Meta &#x60;video.id&#x60; (reusable wherever &#x60;video.id&#x60; is accepted) plus Meta&#39;s auto-generated poster URL when available. The endpoint waits until Meta reports the video ready (chunked upload + transcode can take minutes; the handler runs up to 800 s).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        UploadAdVideoRequest uploadAdVideoRequest = new UploadAdVideoRequest(); // UploadAdVideoRequest | 
        try {
            UploadAdVideo201Response result = apiInstance.uploadAdVideo(uploadAdVideoRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#uploadAdVideo");
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
| **uploadAdVideoRequest** | [**UploadAdVideoRequest**](UploadAdVideoRequest.md)|  | |

### Return type

[**UploadAdVideo201Response**](UploadAdVideo201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Video uploaded and ready |  -  |
| **400** | Invalid input, or Meta rejected the upload |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no video id). Inspect &#x60;platformError.reason&#x60;. |  -  |

## uploadAdVideoWithHttpInfo

> ApiResponse<UploadAdVideo201Response> uploadAdVideo uploadAdVideoWithHttpInfo(uploadAdVideoRequest)

Upload an ad video

Standalone ad-video upload (parallel to POST /v1/ads/images), so a video creative can be rendered via POST /v1/ads/preview or attached via &#x60;video.id&#x60; on POST /v1/ads/create before an ad exists.  Accepts either an https &#x60;videoUrl&#x60; we download server-side (SSRF-guarded) or raw &#x60;videoBase64&#x60; bytes; exactly one is required. &#x60;videoBase64&#x60; is capped by Vercel&#39;s body limit — around 4.5 MB payload in practice, so larger videos must come via &#x60;videoUrl&#x60;.  Returns the Meta &#x60;video.id&#x60; (reusable wherever &#x60;video.id&#x60; is accepted) plus Meta&#39;s auto-generated poster URL when available. The endpoint waits until Meta reports the video ready (chunked upload + transcode can take minutes; the handler runs up to 800 s).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCreativesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCreativesApi apiInstance = new AdCreativesApi(defaultClient);
        UploadAdVideoRequest uploadAdVideoRequest = new UploadAdVideoRequest(); // UploadAdVideoRequest | 
        try {
            ApiResponse<UploadAdVideo201Response> response = apiInstance.uploadAdVideoWithHttpInfo(uploadAdVideoRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCreativesApi#uploadAdVideo");
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
| **uploadAdVideoRequest** | [**UploadAdVideoRequest**](UploadAdVideoRequest.md)|  | |

### Return type

ApiResponse<[**UploadAdVideo201Response**](UploadAdVideo201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Video uploaded and ready |  -  |
| **400** | Invalid input, or Meta rejected the upload |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no video id). Inspect &#x60;platformError.reason&#x60;. |  -  |

