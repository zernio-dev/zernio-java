# TrackingTagsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTrackingTagSharedAccount**](TrackingTagsApi.md#addTrackingTagSharedAccount) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Share with an ad account |
| [**addTrackingTagSharedAccountWithHttpInfo**](TrackingTagsApi.md#addTrackingTagSharedAccountWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Share with an ad account |
| [**createTrackingTag**](TrackingTagsApi.md#createTrackingTag) | **POST** /v1/accounts/{accountId}/tracking-tags | Create a tracking tag |
| [**createTrackingTagWithHttpInfo**](TrackingTagsApi.md#createTrackingTagWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags | Create a tracking tag |
| [**createTrackingTagEvent**](TrackingTagsApi.md#createTrackingTagEvent) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/events | Create a conversion event |
| [**createTrackingTagEventWithHttpInfo**](TrackingTagsApi.md#createTrackingTagEventWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/events | Create a conversion event |
| [**deleteTrackingTagEvent**](TrackingTagsApi.md#deleteTrackingTagEvent) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/events/{eventId} | Delete a conversion event |
| [**deleteTrackingTagEventWithHttpInfo**](TrackingTagsApi.md#deleteTrackingTagEventWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/events/{eventId} | Delete a conversion event |
| [**getAdTrackingTags**](TrackingTagsApi.md#getAdTrackingTags) | **GET** /v1/ads/{adId}/tracking-tags | Get ad tracking tags |
| [**getAdTrackingTagsWithHttpInfo**](TrackingTagsApi.md#getAdTrackingTagsWithHttpInfo) | **GET** /v1/ads/{adId}/tracking-tags | Get ad tracking tags |
| [**getTrackingTag**](TrackingTagsApi.md#getTrackingTag) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId} | Get a tracking tag |
| [**getTrackingTagWithHttpInfo**](TrackingTagsApi.md#getTrackingTagWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId} | Get a tracking tag |
| [**getTrackingTagStats**](TrackingTagsApi.md#getTrackingTagStats) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/stats | Get aggregated event stats |
| [**getTrackingTagStatsWithHttpInfo**](TrackingTagsApi.md#getTrackingTagStatsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/stats | Get aggregated event stats |
| [**getTrackingTagStoreInstall**](TrackingTagsApi.md#getTrackingTagStoreInstall) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Get store install status |
| [**getTrackingTagStoreInstallWithHttpInfo**](TrackingTagsApi.md#getTrackingTagStoreInstallWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Get store install status |
| [**installTrackingTagOnStore**](TrackingTagsApi.md#installTrackingTagOnStore) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Install on a Shopify store or WordPress site |
| [**installTrackingTagOnStoreWithHttpInfo**](TrackingTagsApi.md#installTrackingTagOnStoreWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Install on a Shopify store or WordPress site |
| [**listTrackingTagEvents**](TrackingTagsApi.md#listTrackingTagEvents) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/events | List conversion events |
| [**listTrackingTagEventsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagEventsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/events | List conversion events |
| [**listTrackingTagSharedAccounts**](TrackingTagsApi.md#listTrackingTagSharedAccounts) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | List accounts it is shared with |
| [**listTrackingTagSharedAccountsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagSharedAccountsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | List accounts it is shared with |
| [**listTrackingTags**](TrackingTagsApi.md#listTrackingTags) | **GET** /v1/accounts/{accountId}/tracking-tags | List tracking tags |
| [**listTrackingTagsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags | List tracking tags |
| [**removeTrackingTagFromStore**](TrackingTagsApi.md#removeTrackingTagFromStore) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Remove from a Shopify store or WordPress site |
| [**removeTrackingTagFromStoreWithHttpInfo**](TrackingTagsApi.md#removeTrackingTagFromStoreWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Remove from a Shopify store or WordPress site |
| [**removeTrackingTagSharedAccount**](TrackingTagsApi.md#removeTrackingTagSharedAccount) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Stop sharing with an account |
| [**removeTrackingTagSharedAccountWithHttpInfo**](TrackingTagsApi.md#removeTrackingTagSharedAccountWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Stop sharing with an account |
| [**updateAdTrackingTags**](TrackingTagsApi.md#updateAdTrackingTags) | **PATCH** /v1/ads/{adId}/tracking-tags | Set ad tracking tags |
| [**updateAdTrackingTagsWithHttpInfo**](TrackingTagsApi.md#updateAdTrackingTagsWithHttpInfo) | **PATCH** /v1/ads/{adId}/tracking-tags | Set ad tracking tags |
| [**updateTrackingTag**](TrackingTagsApi.md#updateTrackingTag) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId} | Update a tracking tag |
| [**updateTrackingTagWithHttpInfo**](TrackingTagsApi.md#updateTrackingTagWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId} | Update a tracking tag |
| [**updateTrackingTagEvent**](TrackingTagsApi.md#updateTrackingTagEvent) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId}/events/{eventId} | Update a conversion event |
| [**updateTrackingTagEventWithHttpInfo**](TrackingTagsApi.md#updateTrackingTagEventWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId}/events/{eventId} | Update a conversion event |



## addTrackingTagSharedAccount

> AddTrackingTagSharedAccount201Response addTrackingTagSharedAccount(accountId, tagId, addTrackingTagSharedAccountRequest)

Share with an ad account

Shares the pixel with another ad account so campaigns/audiences in that account can use it. Requires that you administer both the pixel&#39;s owning Business Manager and the target ad account; a pixel on a personal (non-BM) ad account can&#39;t be shared (Meta will reject the call). Meta only (platform &#x60;metaads&#x60;); other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        AddTrackingTagSharedAccountRequest addTrackingTagSharedAccountRequest = new AddTrackingTagSharedAccountRequest(); // AddTrackingTagSharedAccountRequest | 
        try {
            AddTrackingTagSharedAccount201Response result = apiInstance.addTrackingTagSharedAccount(accountId, tagId, addTrackingTagSharedAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#addTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **addTrackingTagSharedAccountRequest** | [**AddTrackingTagSharedAccountRequest**](AddTrackingTagSharedAccountRequest.md)|  | |

### Return type

[**AddTrackingTagSharedAccount201Response**](AddTrackingTagSharedAccount201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Tracking tag shared with the ad account |  -  |
| **400** | Invalid body / &#x60;adAccountId&#x60;, or Meta rejected the share (e.g. personal ad account). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## addTrackingTagSharedAccountWithHttpInfo

> ApiResponse<AddTrackingTagSharedAccount201Response> addTrackingTagSharedAccount addTrackingTagSharedAccountWithHttpInfo(accountId, tagId, addTrackingTagSharedAccountRequest)

Share with an ad account

Shares the pixel with another ad account so campaigns/audiences in that account can use it. Requires that you administer both the pixel&#39;s owning Business Manager and the target ad account; a pixel on a personal (non-BM) ad account can&#39;t be shared (Meta will reject the call). Meta only (platform &#x60;metaads&#x60;); other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        AddTrackingTagSharedAccountRequest addTrackingTagSharedAccountRequest = new AddTrackingTagSharedAccountRequest(); // AddTrackingTagSharedAccountRequest | 
        try {
            ApiResponse<AddTrackingTagSharedAccount201Response> response = apiInstance.addTrackingTagSharedAccountWithHttpInfo(accountId, tagId, addTrackingTagSharedAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#addTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **addTrackingTagSharedAccountRequest** | [**AddTrackingTagSharedAccountRequest**](AddTrackingTagSharedAccountRequest.md)|  | |

### Return type

ApiResponse<[**AddTrackingTagSharedAccount201Response**](AddTrackingTagSharedAccount201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Tracking tag shared with the ad account |  -  |
| **400** | Invalid body / &#x60;adAccountId&#x60;, or Meta rejected the share (e.g. personal ad account). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |


## createTrackingTag

> CreateTrackingTag201Response createTrackingTag(accountId, createTrackingTagRequest)

Create a tracking tag

Meta: creates a Meta Pixel on the given ad account (&#x60;POST /act_{id}/adspixels&#x60;, where &#x60;name&#x60; is the only input). Returns the created tag including its install &#x60;code&#x60;. The pixel is owned by the Business Manager that owns the ad account; a pixel created on a personal (non-BM) ad account ends up with &#x60;ownerBusinessId: null&#x60; and can&#39;t be shared with other ad accounts.  Creating a Meta pixel does NOT install it. Install the returned &#x60;code&#x60; snippet on the site, or send events server-side via &#x60;POST /v1/ads/conversions&#x60;. The check &#x60;installed&#x60; is derived from &#x60;lastFiredTime&#x60;.  OpenAI Ads: creates an OpenAI pixel AND provisions a Conversions API key for it in the same call (&#x60;adAccountId&#x60; is required by this endpoint but ignored: one API key maps to exactly one ad account, so there&#39;s nothing to select). Returns 422 (&#x60;FEATURE_NOT_AVAILABLE&#x60;) if the ad account isn&#39;t enabled for pixel management; contact your OpenAI partner representative to enable it. There is no delete API for OpenAI pixels. If the pixel is created but the Conversions API key provisioning then fails, the pixel is left live on OpenAI (it cannot be cleaned up) and the error message names the surviving pixel id and warns against retrying, since a retry would create a second, orphaned pixel.  NOT idempotent on either platform: each call creates a new pixel (and, for OpenAI, a new Conversions API key plus, with &#x60;defaultEventType&#x60;, a new conversion event setting). Do not retry blindly on timeout. Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Ads SocialAccount id (platform `metaads` or `openaiads`).
        CreateTrackingTagRequest createTrackingTagRequest = new CreateTrackingTagRequest(); // CreateTrackingTagRequest | 
        try {
            CreateTrackingTag201Response result = apiInstance.createTrackingTag(accountId, createTrackingTagRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#createTrackingTag");
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
| **accountId** | **String**| Ads SocialAccount id (platform &#x60;metaads&#x60; or &#x60;openaiads&#x60;). | |
| **createTrackingTagRequest** | [**CreateTrackingTagRequest**](CreateTrackingTagRequest.md)|  | |

### Return type

[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Tracking tag created |  -  |
| **400** | Invalid body, invalid &#x60;adAccountId&#x60;, over the per-business pixel cap, or ad account not in a Business Manager. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **422** | OpenAI Ads only: the ad account is not enabled for pixel management. Contact your OpenAI partner representative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Creating a pixel is NOT idempotent, so before retrying confirm with GET /v1/accounts/{accountId}/tracking-tags that no pixel was created. |  -  |

## createTrackingTagWithHttpInfo

> ApiResponse<CreateTrackingTag201Response> createTrackingTag createTrackingTagWithHttpInfo(accountId, createTrackingTagRequest)

Create a tracking tag

Meta: creates a Meta Pixel on the given ad account (&#x60;POST /act_{id}/adspixels&#x60;, where &#x60;name&#x60; is the only input). Returns the created tag including its install &#x60;code&#x60;. The pixel is owned by the Business Manager that owns the ad account; a pixel created on a personal (non-BM) ad account ends up with &#x60;ownerBusinessId: null&#x60; and can&#39;t be shared with other ad accounts.  Creating a Meta pixel does NOT install it. Install the returned &#x60;code&#x60; snippet on the site, or send events server-side via &#x60;POST /v1/ads/conversions&#x60;. The check &#x60;installed&#x60; is derived from &#x60;lastFiredTime&#x60;.  OpenAI Ads: creates an OpenAI pixel AND provisions a Conversions API key for it in the same call (&#x60;adAccountId&#x60; is required by this endpoint but ignored: one API key maps to exactly one ad account, so there&#39;s nothing to select). Returns 422 (&#x60;FEATURE_NOT_AVAILABLE&#x60;) if the ad account isn&#39;t enabled for pixel management; contact your OpenAI partner representative to enable it. There is no delete API for OpenAI pixels. If the pixel is created but the Conversions API key provisioning then fails, the pixel is left live on OpenAI (it cannot be cleaned up) and the error message names the surviving pixel id and warns against retrying, since a retry would create a second, orphaned pixel.  NOT idempotent on either platform: each call creates a new pixel (and, for OpenAI, a new Conversions API key plus, with &#x60;defaultEventType&#x60;, a new conversion event setting). Do not retry blindly on timeout. Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Ads SocialAccount id (platform `metaads` or `openaiads`).
        CreateTrackingTagRequest createTrackingTagRequest = new CreateTrackingTagRequest(); // CreateTrackingTagRequest | 
        try {
            ApiResponse<CreateTrackingTag201Response> response = apiInstance.createTrackingTagWithHttpInfo(accountId, createTrackingTagRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#createTrackingTag");
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
| **accountId** | **String**| Ads SocialAccount id (platform &#x60;metaads&#x60; or &#x60;openaiads&#x60;). | |
| **createTrackingTagRequest** | [**CreateTrackingTagRequest**](CreateTrackingTagRequest.md)|  | |

### Return type

ApiResponse<[**CreateTrackingTag201Response**](CreateTrackingTag201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Tracking tag created |  -  |
| **400** | Invalid body, invalid &#x60;adAccountId&#x60;, over the per-business pixel cap, or ad account not in a Business Manager. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **422** | OpenAI Ads only: the ad account is not enabled for pixel management. Contact your OpenAI partner representative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Creating a pixel is NOT idempotent, so before retrying confirm with GET /v1/accounts/{accountId}/tracking-tags that no pixel was created. |  -  |


## createTrackingTagEvent

> CreateTrackingTagEvent201Response createTrackingTagEvent(accountId, tagId, createTrackingTagEventRequest)

Create a conversion event

Creates a conversion event tied to the tag. Pass the platform&#39;s own event type in &#x60;type&#x60; (e.g. Google &#x60;PURCHASE&#x60;, LinkedIn &#x60;ADD_TO_CART&#x60;, X &#x60;CHECKOUT_INITIATED&#x60;) or a neutral &#x60;siteEvent&#x60; the platform maps to its closest type. Each platform stores a subset of the optional fields; sending one it does not store answers 400 naming the supported fields. NOT idempotent unless noted per platform: do not retry blindly. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        CreateTrackingTagEventRequest createTrackingTagEventRequest = new CreateTrackingTagEventRequest(); // CreateTrackingTagEventRequest | 
        try {
            CreateTrackingTagEvent201Response result = apiInstance.createTrackingTagEvent(accountId, tagId, createTrackingTagEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#createTrackingTagEvent");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **createTrackingTagEventRequest** | [**CreateTrackingTagEventRequest**](CreateTrackingTagEventRequest.md)|  | |

### Return type

[**CreateTrackingTagEvent201Response**](CreateTrackingTagEvent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Conversion event created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot create conversion events through its API (code &#x60;platform_not_supported&#x60;). |  -  |

## createTrackingTagEventWithHttpInfo

> ApiResponse<CreateTrackingTagEvent201Response> createTrackingTagEvent createTrackingTagEventWithHttpInfo(accountId, tagId, createTrackingTagEventRequest)

Create a conversion event

Creates a conversion event tied to the tag. Pass the platform&#39;s own event type in &#x60;type&#x60; (e.g. Google &#x60;PURCHASE&#x60;, LinkedIn &#x60;ADD_TO_CART&#x60;, X &#x60;CHECKOUT_INITIATED&#x60;) or a neutral &#x60;siteEvent&#x60; the platform maps to its closest type. Each platform stores a subset of the optional fields; sending one it does not store answers 400 naming the supported fields. NOT idempotent unless noted per platform: do not retry blindly. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        CreateTrackingTagEventRequest createTrackingTagEventRequest = new CreateTrackingTagEventRequest(); // CreateTrackingTagEventRequest | 
        try {
            ApiResponse<CreateTrackingTagEvent201Response> response = apiInstance.createTrackingTagEventWithHttpInfo(accountId, tagId, createTrackingTagEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#createTrackingTagEvent");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **createTrackingTagEventRequest** | [**CreateTrackingTagEventRequest**](CreateTrackingTagEventRequest.md)|  | |

### Return type

ApiResponse<[**CreateTrackingTagEvent201Response**](CreateTrackingTagEvent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Conversion event created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot create conversion events through its API (code &#x60;platform_not_supported&#x60;). |  -  |


## deleteTrackingTagEvent

> DeleteTrackingTagEvent200Response deleteTrackingTagEvent(accountId, tagId, eventId, adAccountId)

Delete a conversion event

Removes the conversion event. Platforms without a hard delete archive or disable it instead; &#x60;state&#x60; in the response says which (&#x60;deleted&#x60;, &#x60;archived&#x60;, &#x60;disabled&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | 
        String eventId = "eventId_example"; // String | Event id (`TrackingTagEvent.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account.
        try {
            DeleteTrackingTagEvent200Response result = apiInstance.deleteTrackingTagEvent(accountId, tagId, eventId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#deleteTrackingTagEvent");
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
| **tagId** | **String**|  | |
| **eventId** | **String**| Event id (&#x60;TrackingTagEvent.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

[**DeleteTrackingTagEvent200Response**](DeleteTrackingTagEvent200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversion event removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot remove conversion events through its API (code &#x60;platform_not_supported&#x60;). |  -  |

## deleteTrackingTagEventWithHttpInfo

> ApiResponse<DeleteTrackingTagEvent200Response> deleteTrackingTagEvent deleteTrackingTagEventWithHttpInfo(accountId, tagId, eventId, adAccountId)

Delete a conversion event

Removes the conversion event. Platforms without a hard delete archive or disable it instead; &#x60;state&#x60; in the response says which (&#x60;deleted&#x60;, &#x60;archived&#x60;, &#x60;disabled&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | 
        String eventId = "eventId_example"; // String | Event id (`TrackingTagEvent.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account.
        try {
            ApiResponse<DeleteTrackingTagEvent200Response> response = apiInstance.deleteTrackingTagEventWithHttpInfo(accountId, tagId, eventId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#deleteTrackingTagEvent");
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
| **tagId** | **String**|  | |
| **eventId** | **String**| Event id (&#x60;TrackingTagEvent.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

ApiResponse<[**DeleteTrackingTagEvent200Response**](DeleteTrackingTagEvent200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversion event removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot remove conversion events through its API (code &#x60;platform_not_supported&#x60;). |  -  |


## getAdTrackingTags

> GetAdTrackingTags200Response getAdTrackingTags(adId)

Get ad tracking tags

Unified read of the platform&#39;s native click-URL tracking params. - Meta (facebook/instagram): the creative&#39;s &#x60;url_tags&#x60; (and template_url_spec). - Google (googleads): the campaign&#39;s &#x60;trackingUrlTemplate&#x60; + &#x60;finalUrlSuffix&#x60;. - LinkedIn (linkedinads): the campaign&#39;s Dynamic UTM &#x60;dynamicValueParameters&#x60; + &#x60;customValueParameters&#x60;. Returns 405 for platforms without a click-URL tracking surface (TikTok, X, Pinterest).  **Not pixels.** Despite the shared path segment, this endpoint has nothing to do with measurement tags. For an ad account&#39;s pixels use &#x60;GET /v1/accounts/{accountId}/tracking-tags?adAccountId&#x3D;act_...&#x60; (Meta Pixels, with &#x60;kind&#x60; and &#x60;ownerAdAccountId&#x60;) or &#x60;GET /v1/accounts/{accountId}/conversion-destinations&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String adId = "adId_example"; // String | Ad id (hex _id, platformAdId, or effective story/media id).
        try {
            GetAdTrackingTags200Response result = apiInstance.getAdTrackingTags(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getAdTrackingTags");
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
| **adId** | **String**| Ad id (hex _id, platformAdId, or effective story/media id). | |

### Return type

[**GetAdTrackingTags200Response**](GetAdTrackingTags200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tags for the ad&#39;s platform (shape varies by platform). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |

## getAdTrackingTagsWithHttpInfo

> ApiResponse<GetAdTrackingTags200Response> getAdTrackingTags getAdTrackingTagsWithHttpInfo(adId)

Get ad tracking tags

Unified read of the platform&#39;s native click-URL tracking params. - Meta (facebook/instagram): the creative&#39;s &#x60;url_tags&#x60; (and template_url_spec). - Google (googleads): the campaign&#39;s &#x60;trackingUrlTemplate&#x60; + &#x60;finalUrlSuffix&#x60;. - LinkedIn (linkedinads): the campaign&#39;s Dynamic UTM &#x60;dynamicValueParameters&#x60; + &#x60;customValueParameters&#x60;. Returns 405 for platforms without a click-URL tracking surface (TikTok, X, Pinterest).  **Not pixels.** Despite the shared path segment, this endpoint has nothing to do with measurement tags. For an ad account&#39;s pixels use &#x60;GET /v1/accounts/{accountId}/tracking-tags?adAccountId&#x3D;act_...&#x60; (Meta Pixels, with &#x60;kind&#x60; and &#x60;ownerAdAccountId&#x60;) or &#x60;GET /v1/accounts/{accountId}/conversion-destinations&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String adId = "adId_example"; // String | Ad id (hex _id, platformAdId, or effective story/media id).
        try {
            ApiResponse<GetAdTrackingTags200Response> response = apiInstance.getAdTrackingTagsWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getAdTrackingTags");
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
| **adId** | **String**| Ad id (hex _id, platformAdId, or effective story/media id). | |

### Return type

ApiResponse<[**GetAdTrackingTags200Response**](GetAdTrackingTags200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tags for the ad&#39;s platform (shape varies by platform). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |


## getTrackingTag

> GetTrackingTag200Response getTrackingTag(accountId, tagId, adAccountId)

Get a tracking tag

Returns the full tag record including the base-code &#x60;code&#x60; snippet, &#x60;lastFiredTime&#x60;, &#x60;ownerBusinessId&#x60;, &#x60;isUnavailable&#x60;, etc. Meta only (platform &#x60;metaads&#x60;); other platforms return 501. OpenAI Ads has no get-by-id endpoint, so it answers 501 here too. Use &#x60;GET /v1/accounts/{accountId}/tracking-tags&#x60; (list) instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere.
        try {
            GetTrackingTag200Response result = apiInstance.getTrackingTag(accountId, tagId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTag");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere. | [optional] |

### Return type

[**GetTrackingTag200Response**](GetTrackingTag200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **400** | Invalid request |  -  |
| **200** | Tracking tag fetched |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## getTrackingTagWithHttpInfo

> ApiResponse<GetTrackingTag200Response> getTrackingTag getTrackingTagWithHttpInfo(accountId, tagId, adAccountId)

Get a tracking tag

Returns the full tag record including the base-code &#x60;code&#x60; snippet, &#x60;lastFiredTime&#x60;, &#x60;ownerBusinessId&#x60;, &#x60;isUnavailable&#x60;, etc. Meta only (platform &#x60;metaads&#x60;); other platforms return 501. OpenAI Ads has no get-by-id endpoint, so it answers 501 here too. Use &#x60;GET /v1/accounts/{accountId}/tracking-tags&#x60; (list) instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere.
        try {
            ApiResponse<GetTrackingTag200Response> response = apiInstance.getTrackingTagWithHttpInfo(accountId, tagId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTag");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere. | [optional] |

### Return type

ApiResponse<[**GetTrackingTag200Response**](GetTrackingTag200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **400** | Invalid request |  -  |
| **200** | Tracking tag fetched |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |


## getTrackingTagStats

> GetTrackingTagStats200Response getTrackingTagStats(accountId, tagId, adAccountId, aggregation, startTime, endTime)

Get aggregated event stats

Returns event counts / health for the tag, where the platform exposes them. Meta: aggregated counts (&#x60;GET /{pixel_id}/stats&#x60;), rows passed through as-is; their shape depends on the &#x60;aggregation&#x60; requested. Platforms without a stats API answer 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere.
        String aggregation = "event"; // String | Meta only (400 on other platforms): aggregation dimension. Defaults to `event`.
        Integer startTime = 56; // Integer | Unix seconds lower bound.
        Integer endTime = 56; // Integer | Unix seconds upper bound.
        try {
            GetTrackingTagStats200Response result = apiInstance.getTrackingTagStats(accountId, tagId, adAccountId, aggregation, startTime, endTime);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagStats");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere. | [optional] |
| **aggregation** | **String**| Meta only (400 on other platforms): aggregation dimension. Defaults to &#x60;event&#x60;. | [optional] [default to event] [enum: event, host, url, url_by_rule, pixel_fire, device_type, device_os, browser_type, had_pii, custom_data_field, match_keys, event_source, event_detection_method, event_processing_results, event_total_counts, event_value_count] |
| **startTime** | **Integer**| Unix seconds lower bound. | [optional] |
| **endTime** | **Integer**| Unix seconds upper bound. | [optional] |

### Return type

[**GetTrackingTagStats200Response**](GetTrackingTagStats200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Stats fetched |  -  |
| **400** | Invalid query parameter. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## getTrackingTagStatsWithHttpInfo

> ApiResponse<GetTrackingTagStats200Response> getTrackingTagStats getTrackingTagStatsWithHttpInfo(accountId, tagId, adAccountId, aggregation, startTime, endTime)

Get aggregated event stats

Returns event counts / health for the tag, where the platform exposes them. Meta: aggregated counts (&#x60;GET /{pixel_id}/stats&#x60;), rows passed through as-is; their shape depends on the &#x60;aggregation&#x60; requested. Platforms without a stats API answer 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere.
        String aggregation = "event"; // String | Meta only (400 on other platforms): aggregation dimension. Defaults to `event`.
        Integer startTime = 56; // Integer | Unix seconds lower bound.
        Integer endTime = 56; // Integer | Unix seconds upper bound.
        try {
            ApiResponse<GetTrackingTagStats200Response> response = apiInstance.getTrackingTagStatsWithHttpInfo(accountId, tagId, adAccountId, aggregation, startTime, endTime);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagStats");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. Ignored elsewhere. | [optional] |
| **aggregation** | **String**| Meta only (400 on other platforms): aggregation dimension. Defaults to &#x60;event&#x60;. | [optional] [default to event] [enum: event, host, url, url_by_rule, pixel_fire, device_type, device_os, browser_type, had_pii, custom_data_field, match_keys, event_source, event_detection_method, event_processing_results, event_total_counts, event_value_count] |
| **startTime** | **Integer**| Unix seconds lower bound. | [optional] |
| **endTime** | **Integer**| Unix seconds upper bound. | [optional] |

### Return type

ApiResponse<[**GetTrackingTagStats200Response**](GetTrackingTagStats200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Stats fetched |  -  |
| **400** | Invalid query parameter. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |


## getTrackingTagStoreInstall

> GetTrackingTagStoreInstall200Response getTrackingTagStoreInstall(accountId, tagId, storeAccountId, adAccountId)

Get store install status

Whether this tag is the one the Shopify store fires for its platform. &#x60;installedTagId&#x60; names the tag of that platform the store currently fires, which can be a different tag, and &#x60;tags&#x60; lists every Zernio tag on the store (all platforms).  WordPress: whether the Zernio widget for this pixel is live (in an active widget area, script intact), plus a read-only &#x60;preflight&#x60; with the theme&#39;s widget areas and, when an install would be blocked, the &#x60;reason&#x60; POST would return. The preflight reads capabilities only, so &#x60;ready: true&#x60; is not a guarantee: &#x60;DISALLOW_UNFILTERED_HTML&#x60; or a multisite admin who is not a Super Admin still strips the script, which POST detects. &#x60;tags&#x60; lists every Zernio widget on the site (all platforms, with &#x60;active&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String storeAccountId = "storeAccountId_example"; // String | The connected Shopify or WordPress account id.
        String adAccountId = "adAccountId_example"; // String | Scopes the tag lookup on platforms whose tag ids live inside an ad account.
        try {
            GetTrackingTagStoreInstall200Response result = apiInstance.getTrackingTagStoreInstall(accountId, tagId, storeAccountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagStoreInstall");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **storeAccountId** | **String**| The connected Shopify or WordPress account id. | |
| **adAccountId** | **String**| Scopes the tag lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

[**GetTrackingTagStoreInstall200Response**](GetTrackingTagStoreInstall200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Install status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **409** | The store must re-approve the Zernio Shopify app to grant pixel access (code &#x60;reconnect_required&#x60;). Send the merchant to &#x60;details.authUrl&#x60;; the Shopify account id stays the same. Also returned while the store account itself needs reconnection (code &#x60;ads_connection_required&#x60;). |  -  |

## getTrackingTagStoreInstallWithHttpInfo

> ApiResponse<GetTrackingTagStoreInstall200Response> getTrackingTagStoreInstall getTrackingTagStoreInstallWithHttpInfo(accountId, tagId, storeAccountId, adAccountId)

Get store install status

Whether this tag is the one the Shopify store fires for its platform. &#x60;installedTagId&#x60; names the tag of that platform the store currently fires, which can be a different tag, and &#x60;tags&#x60; lists every Zernio tag on the store (all platforms).  WordPress: whether the Zernio widget for this pixel is live (in an active widget area, script intact), plus a read-only &#x60;preflight&#x60; with the theme&#39;s widget areas and, when an install would be blocked, the &#x60;reason&#x60; POST would return. The preflight reads capabilities only, so &#x60;ready: true&#x60; is not a guarantee: &#x60;DISALLOW_UNFILTERED_HTML&#x60; or a multisite admin who is not a Super Admin still strips the script, which POST detects. &#x60;tags&#x60; lists every Zernio widget on the site (all platforms, with &#x60;active&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String storeAccountId = "storeAccountId_example"; // String | The connected Shopify or WordPress account id.
        String adAccountId = "adAccountId_example"; // String | Scopes the tag lookup on platforms whose tag ids live inside an ad account.
        try {
            ApiResponse<GetTrackingTagStoreInstall200Response> response = apiInstance.getTrackingTagStoreInstallWithHttpInfo(accountId, tagId, storeAccountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagStoreInstall");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **storeAccountId** | **String**| The connected Shopify or WordPress account id. | |
| **adAccountId** | **String**| Scopes the tag lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

ApiResponse<[**GetTrackingTagStoreInstall200Response**](GetTrackingTagStoreInstall200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Install status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **409** | The store must re-approve the Zernio Shopify app to grant pixel access (code &#x60;reconnect_required&#x60;). Send the merchant to &#x60;details.authUrl&#x60;; the Shopify account id stays the same. Also returned while the store account itself needs reconnection (code &#x60;ads_connection_required&#x60;). |  -  |


## installTrackingTagOnStore

> InstallTrackingTagOnStore200Response installTrackingTagOnStore(accountId, tagId, installTrackingTagOnStoreRequest)

Install on a Shopify store or WordPress site

Puts the Meta pixel on a connected Shopify store&#39;s storefront and checkout through Zernio&#39;s Shopify web pixel (a Shopify app pixel, no theme edits). The store then sends PageView, ViewContent, AddToCart, Search, InitiateCheckout, AddPaymentInfo and Purchase (with value, currency, content_ids and contents) to the pixel, each with an event id. Purchase uses &#x60;shopify_order_{orderId}&#x60; as its event id, so a Conversions API Purchase you send for the same order with that &#x60;eventId&#x60; is deduplicated by Meta.  Idempotent: a store runs one Zernio web pixel holding one tag per platform, so calling it again updates the install, installing a different tag of the same platform replaces the previous one (reported in &#x60;replacedTagId&#x60;), and other platforms&#39; tags are kept. Events respect the store&#39;s customer privacy settings (marketing consent).  &#x60;accountId&#x60; is the Meta ads account that owns the pixel (&#x60;tagId&#x60;); &#x60;storeAccountId&#x60; is the Shopify account. Stores connected before pixel support must re-approve the Zernio app: the call then answers 409 &#x60;reconnect_required&#x60; with &#x60;details.authUrl&#x60; to send the merchant to (the Shopify account id stays the same). Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  **WordPress** (&#x60;storeAccountId&#x60; is a connected WordPress.com or self-hosted site): Zernio adds a Custom HTML widget with the Meta pixel base code (fbevents.js, &#x60;init&#x60;, &#x60;PageView&#x60;) to a widget area of the active theme (a footer area when there is one, else the first active area; pass &#x60;sidebarId&#x60; to choose), then reads the widget back to confirm WordPress kept the &#x60;&lt;script&gt;&#x60; tag. The widget carries a Zernio marker, so the call is idempotent per pixel: repeating it updates or moves the same widget, and pixel code the site owner pasted by hand is never touched. Several pixels can run side by side (one widget each). When the site cannot run the pixel, nothing is left behind and the call answers 422 &#x60;tracking_tag_install_blocked&#x60; with &#x60;details.reason&#x60;: - &#x60;insufficient_permissions&#x60;: the connected user lacks &#x60;edit_theme_options&#x60; (needs Administrator). - &#x60;scripts_stripped&#x60;: WordPress removed the script (the user lacks &#x60;unfiltered_html&#x60;, e.g. a multisite admin who is not a Super Admin, or &#x60;DISALLOW_UNFILTERED_HTML&#x60; is set). - &#x60;wordpress_com_plan&#x60;: a WordPress.com plan that strips scripts (plans without plugins). - &#x60;no_widget_areas&#x60;: the theme has no widget areas (block themes such as Twenty Twenty-Five). - &#x60;widgets_api_unavailable&#x60;: no widgets REST API (WordPress older than 5.8, or disabled). The &#x60;error&#x60; message names the manual alternative (Meta&#39;s official WordPress plugin). With &#x60;verifyHomepage&#x60; (default true) the homepage is fetched afterwards and &#x60;homepageCheck&#x60; says whether the pixel is visible; &#x60;not_found&#x60; can be a stale page cache, the widget read-back is authoritative. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        InstallTrackingTagOnStoreRequest installTrackingTagOnStoreRequest = new InstallTrackingTagOnStoreRequest(); // InstallTrackingTagOnStoreRequest | 
        try {
            InstallTrackingTagOnStore200Response result = apiInstance.installTrackingTagOnStore(accountId, tagId, installTrackingTagOnStoreRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#installTrackingTagOnStore");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **installTrackingTagOnStoreRequest** | [**InstallTrackingTagOnStoreRequest**](InstallTrackingTagOnStoreRequest.md)|  | |

### Return type

[**InstallTrackingTagOnStore200Response**](InstallTrackingTagOnStore200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pixel installed on the store |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **409** | The store must re-approve the Zernio Shopify app to grant pixel access (code &#x60;reconnect_required&#x60;). Send the merchant to &#x60;details.authUrl&#x60;; the Shopify account id stays the same. Also returned while the store account itself needs reconnection (code &#x60;ads_connection_required&#x60;). |  -  |
| **422** | WordPress only: the site cannot run the pixel and nothing was left on it. Code &#x60;tracking_tag_install_blocked&#x60;; the reason is in &#x60;details.reason&#x60;. |  -  |
| **502** | Meta, Shopify or the WordPress site was unreachable or returned an unclassified error. On WordPress a write may have completed; call GET before retrying. |  -  |

## installTrackingTagOnStoreWithHttpInfo

> ApiResponse<InstallTrackingTagOnStore200Response> installTrackingTagOnStore installTrackingTagOnStoreWithHttpInfo(accountId, tagId, installTrackingTagOnStoreRequest)

Install on a Shopify store or WordPress site

Puts the Meta pixel on a connected Shopify store&#39;s storefront and checkout through Zernio&#39;s Shopify web pixel (a Shopify app pixel, no theme edits). The store then sends PageView, ViewContent, AddToCart, Search, InitiateCheckout, AddPaymentInfo and Purchase (with value, currency, content_ids and contents) to the pixel, each with an event id. Purchase uses &#x60;shopify_order_{orderId}&#x60; as its event id, so a Conversions API Purchase you send for the same order with that &#x60;eventId&#x60; is deduplicated by Meta.  Idempotent: a store runs one Zernio web pixel holding one tag per platform, so calling it again updates the install, installing a different tag of the same platform replaces the previous one (reported in &#x60;replacedTagId&#x60;), and other platforms&#39; tags are kept. Events respect the store&#39;s customer privacy settings (marketing consent).  &#x60;accountId&#x60; is the Meta ads account that owns the pixel (&#x60;tagId&#x60;); &#x60;storeAccountId&#x60; is the Shopify account. Stores connected before pixel support must re-approve the Zernio app: the call then answers 409 &#x60;reconnect_required&#x60; with &#x60;details.authUrl&#x60; to send the merchant to (the Shopify account id stays the same). Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  **WordPress** (&#x60;storeAccountId&#x60; is a connected WordPress.com or self-hosted site): Zernio adds a Custom HTML widget with the Meta pixel base code (fbevents.js, &#x60;init&#x60;, &#x60;PageView&#x60;) to a widget area of the active theme (a footer area when there is one, else the first active area; pass &#x60;sidebarId&#x60; to choose), then reads the widget back to confirm WordPress kept the &#x60;&lt;script&gt;&#x60; tag. The widget carries a Zernio marker, so the call is idempotent per pixel: repeating it updates or moves the same widget, and pixel code the site owner pasted by hand is never touched. Several pixels can run side by side (one widget each). When the site cannot run the pixel, nothing is left behind and the call answers 422 &#x60;tracking_tag_install_blocked&#x60; with &#x60;details.reason&#x60;: - &#x60;insufficient_permissions&#x60;: the connected user lacks &#x60;edit_theme_options&#x60; (needs Administrator). - &#x60;scripts_stripped&#x60;: WordPress removed the script (the user lacks &#x60;unfiltered_html&#x60;, e.g. a multisite admin who is not a Super Admin, or &#x60;DISALLOW_UNFILTERED_HTML&#x60; is set). - &#x60;wordpress_com_plan&#x60;: a WordPress.com plan that strips scripts (plans without plugins). - &#x60;no_widget_areas&#x60;: the theme has no widget areas (block themes such as Twenty Twenty-Five). - &#x60;widgets_api_unavailable&#x60;: no widgets REST API (WordPress older than 5.8, or disabled). The &#x60;error&#x60; message names the manual alternative (Meta&#39;s official WordPress plugin). With &#x60;verifyHomepage&#x60; (default true) the homepage is fetched afterwards and &#x60;homepageCheck&#x60; says whether the pixel is visible; &#x60;not_found&#x60; can be a stale page cache, the widget read-back is authoritative. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        InstallTrackingTagOnStoreRequest installTrackingTagOnStoreRequest = new InstallTrackingTagOnStoreRequest(); // InstallTrackingTagOnStoreRequest | 
        try {
            ApiResponse<InstallTrackingTagOnStore200Response> response = apiInstance.installTrackingTagOnStoreWithHttpInfo(accountId, tagId, installTrackingTagOnStoreRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#installTrackingTagOnStore");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **installTrackingTagOnStoreRequest** | [**InstallTrackingTagOnStoreRequest**](InstallTrackingTagOnStoreRequest.md)|  | |

### Return type

ApiResponse<[**InstallTrackingTagOnStore200Response**](InstallTrackingTagOnStore200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pixel installed on the store |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **409** | The store must re-approve the Zernio Shopify app to grant pixel access (code &#x60;reconnect_required&#x60;). Send the merchant to &#x60;details.authUrl&#x60;; the Shopify account id stays the same. Also returned while the store account itself needs reconnection (code &#x60;ads_connection_required&#x60;). |  -  |
| **422** | WordPress only: the site cannot run the pixel and nothing was left on it. Code &#x60;tracking_tag_install_blocked&#x60;; the reason is in &#x60;details.reason&#x60;. |  -  |
| **502** | Meta, Shopify or the WordPress site was unreachable or returned an unclassified error. On WordPress a write may have completed; call GET before retrying. |  -  |


## listTrackingTagEvents

> ListTrackingTagEvents200Response listTrackingTagEvents(accountId, tagId, adAccountId)

List conversion events

The tag&#39;s conversion events, on platforms where each conversion is its own object: Google conversion actions, LinkedIn conversion rules, X web event tags, OpenAI event settings, TikTok pixel events, Meta custom conversions. Platforms where events are just names the site sends (Pinterest) answer 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account.
        try {
            ListTrackingTagEvents200Response result = apiInstance.listTrackingTagEvents(accountId, tagId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagEvents");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

[**ListTrackingTagEvents200Response**](ListTrackingTagEvents200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversion events listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no conversion-event objects (code &#x60;platform_not_supported&#x60;); the message names the alternative. |  -  |

## listTrackingTagEventsWithHttpInfo

> ApiResponse<ListTrackingTagEvents200Response> listTrackingTagEvents listTrackingTagEventsWithHttpInfo(accountId, tagId, adAccountId)

List conversion events

The tag&#39;s conversion events, on platforms where each conversion is its own object: Google conversion actions, LinkedIn conversion rules, X web event tags, OpenAI event settings, TikTok pixel events, Meta custom conversions. Platforms where events are just names the site sends (Pinterest) answer 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String adAccountId = "adAccountId_example"; // String | Scopes the lookup on platforms whose tag ids live inside an ad account.
        try {
            ApiResponse<ListTrackingTagEvents200Response> response = apiInstance.listTrackingTagEventsWithHttpInfo(accountId, tagId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagEvents");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **adAccountId** | **String**| Scopes the lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

ApiResponse<[**ListTrackingTagEvents200Response**](ListTrackingTagEvents200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversion events listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no conversion-event objects (code &#x60;platform_not_supported&#x60;); the message names the alternative. |  -  |


## listTrackingTagSharedAccounts

> ListTrackingTagSharedAccounts200Response listTrackingTagSharedAccounts(accountId, tagId)

List accounts it is shared with

Meta only (platform &#x60;metaads&#x60;); other platforms return 501.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        try {
            ListTrackingTagSharedAccounts200Response result = apiInstance.listTrackingTagSharedAccounts(accountId, tagId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagSharedAccounts");
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
| **tagId** | **String**| Pixel id. | |

### Return type

[**ListTrackingTagSharedAccounts200Response**](ListTrackingTagSharedAccounts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **400** | Invalid request |  -  |
| **200** | Shared ad accounts listed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## listTrackingTagSharedAccountsWithHttpInfo

> ApiResponse<ListTrackingTagSharedAccounts200Response> listTrackingTagSharedAccounts listTrackingTagSharedAccountsWithHttpInfo(accountId, tagId)

List accounts it is shared with

Meta only (platform &#x60;metaads&#x60;); other platforms return 501.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        try {
            ApiResponse<ListTrackingTagSharedAccounts200Response> response = apiInstance.listTrackingTagSharedAccountsWithHttpInfo(accountId, tagId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagSharedAccounts");
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
| **tagId** | **String**| Pixel id. | |

### Return type

ApiResponse<[**ListTrackingTagSharedAccounts200Response**](ListTrackingTagSharedAccounts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **400** | Invalid request |  -  |
| **200** | Shared ad accounts listed |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |


## listTrackingTags

> ListTrackingTags200Response listTrackingTags(accountId, adAccountId)

List tracking tags

Returns the tracking tags (Meta Pixels, or OpenAI Ads pixels) the connected ads account can see. Pass &#x60;?adAccountId&#x3D;act_...&#x60; (Meta only) to scope the list to a single ad account; omit it to list every pixel reachable by the token (the name is then suffixed with the ad account it was discovered on, for disambiguation). The list view omits &#x60;code&#x60;. Call &#x60;getTrackingTag&#x60; for the install snippet and full detail (Meta only; OpenAI Ads has no get-by-id endpoint).  Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501. The &#x60;accountId&#x60; must be the ads SocialAccount created by the Ads add-on connect flow (Meta) or the OpenAI Ads connect flow, not a Facebook/Instagram posting account. Get your Meta &#x60;act_...&#x60; ids from &#x60;GET /v1/ads/accounts&#x60;; &#x60;adAccountId&#x60; is ignored for OpenAI Ads (one API key maps to exactly one ad account). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Ads SocialAccount id (platform `metaads` or `openaiads`).
        String adAccountId = "adAccountId_example"; // String | Optional, Meta only. Scope to one ad account, e.g. `act_123456789`. Ignored for OpenAI Ads.
        try {
            ListTrackingTags200Response result = apiInstance.listTrackingTags(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTags");
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
| **accountId** | **String**| Ads SocialAccount id (platform &#x60;metaads&#x60; or &#x60;openaiads&#x60;). | |
| **adAccountId** | **String**| Optional, Meta only. Scope to one ad account, e.g. &#x60;act_123456789&#x60;. Ignored for OpenAI Ads. | [optional] |

### Return type

[**ListTrackingTags200Response**](ListTrackingTags200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Tracking tags listed |  -  |
| **400** | Account platform not supported, or invalid &#x60;adAccountId&#x60;. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## listTrackingTagsWithHttpInfo

> ApiResponse<ListTrackingTags200Response> listTrackingTags listTrackingTagsWithHttpInfo(accountId, adAccountId)

List tracking tags

Returns the tracking tags (Meta Pixels, or OpenAI Ads pixels) the connected ads account can see. Pass &#x60;?adAccountId&#x3D;act_...&#x60; (Meta only) to scope the list to a single ad account; omit it to list every pixel reachable by the token (the name is then suffixed with the ad account it was discovered on, for disambiguation). The list view omits &#x60;code&#x60;. Call &#x60;getTrackingTag&#x60; for the install snippet and full detail (Meta only; OpenAI Ads has no get-by-id endpoint).  Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501. The &#x60;accountId&#x60; must be the ads SocialAccount created by the Ads add-on connect flow (Meta) or the OpenAI Ads connect flow, not a Facebook/Instagram posting account. Get your Meta &#x60;act_...&#x60; ids from &#x60;GET /v1/ads/accounts&#x60;; &#x60;adAccountId&#x60; is ignored for OpenAI Ads (one API key maps to exactly one ad account). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | Ads SocialAccount id (platform `metaads` or `openaiads`).
        String adAccountId = "adAccountId_example"; // String | Optional, Meta only. Scope to one ad account, e.g. `act_123456789`. Ignored for OpenAI Ads.
        try {
            ApiResponse<ListTrackingTags200Response> response = apiInstance.listTrackingTagsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTags");
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
| **accountId** | **String**| Ads SocialAccount id (platform &#x60;metaads&#x60; or &#x60;openaiads&#x60;). | |
| **adAccountId** | **String**| Optional, Meta only. Scope to one ad account, e.g. &#x60;act_123456789&#x60;. Ignored for OpenAI Ads. | [optional] |

### Return type

ApiResponse<[**ListTrackingTags200Response**](ListTrackingTags200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Tracking tags listed |  -  |
| **400** | Account platform not supported, or invalid &#x60;adAccountId&#x60;. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |


## removeTrackingTagFromStore

> RemoveTrackingTagFromStore200Response removeTrackingTagFromStore(accountId, tagId, storeAccountId, adAccountId)

Remove from a Shopify store or WordPress site

Removes the tag from the store. Idempotent: nothing installed returns 200 with &#x60;installed: false&#x60;. If the store fires a different tag of the same platform, nothing is removed and the call answers 409 &#x60;invalid_resource_state&#x60;. Shopify: other platforms&#39; tags stay; the web pixel itself is deleted once no tag remains.  WordPress: deletes every widget Zernio created for this pixel and reports how many in &#x60;removed&#x60; (0 when nothing was installed). Pixel code added by hand is left alone. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String storeAccountId = "storeAccountId_example"; // String | The connected Shopify or WordPress account id.
        String adAccountId = "adAccountId_example"; // String | Scopes the tag lookup on platforms whose tag ids live inside an ad account.
        try {
            RemoveTrackingTagFromStore200Response result = apiInstance.removeTrackingTagFromStore(accountId, tagId, storeAccountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagFromStore");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **storeAccountId** | **String**| The connected Shopify or WordPress account id. | |
| **adAccountId** | **String**| Scopes the tag lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

[**RemoveTrackingTagFromStore200Response**](RemoveTrackingTagFromStore200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pixel removed (or was not installed) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **409** | The store fires a different pixel (code &#x60;invalid_resource_state&#x60;), or the store must re-approve the Zernio app (code &#x60;reconnect_required&#x60;, see &#x60;details.authUrl&#x60;). |  -  |

## removeTrackingTagFromStoreWithHttpInfo

> ApiResponse<RemoveTrackingTagFromStore200Response> removeTrackingTagFromStore removeTrackingTagFromStoreWithHttpInfo(accountId, tagId, storeAccountId, adAccountId)

Remove from a Shopify store or WordPress site

Removes the tag from the store. Idempotent: nothing installed returns 200 with &#x60;installed: false&#x60;. If the store fires a different tag of the same platform, nothing is removed and the call answers 409 &#x60;invalid_resource_state&#x60;. Shopify: other platforms&#39; tags stay; the web pixel itself is deleted once no tag remains.  WordPress: deletes every widget Zernio created for this pixel and reports how many in &#x60;removed&#x60; (0 when nothing was installed). Pixel code added by hand is left alone. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Tag id (`TrackingTag.id`).
        String storeAccountId = "storeAccountId_example"; // String | The connected Shopify or WordPress account id.
        String adAccountId = "adAccountId_example"; // String | Scopes the tag lookup on platforms whose tag ids live inside an ad account.
        try {
            ApiResponse<RemoveTrackingTagFromStore200Response> response = apiInstance.removeTrackingTagFromStoreWithHttpInfo(accountId, tagId, storeAccountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagFromStore");
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
| **tagId** | **String**| Tag id (&#x60;TrackingTag.id&#x60;). | |
| **storeAccountId** | **String**| The connected Shopify or WordPress account id. | |
| **adAccountId** | **String**| Scopes the tag lookup on platforms whose tag ids live inside an ad account. | [optional] |

### Return type

ApiResponse<[**RemoveTrackingTagFromStore200Response**](RemoveTrackingTagFromStore200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pixel removed (or was not installed) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **409** | The store fires a different pixel (code &#x60;invalid_resource_state&#x60;), or the store must re-approve the Zernio app (code &#x60;reconnect_required&#x60;, see &#x60;details.authUrl&#x60;). |  -  |


## removeTrackingTagSharedAccount

> void removeTrackingTagSharedAccount(accountId, tagId, adAccountId)

Stop sharing with an account

&#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. Meta only (platform &#x60;metaads&#x60;); other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        String adAccountId = "adAccountId_example"; // String | Ad account to unshare, e.g. `act_123456789`. May also be sent in the JSON body.
        try {
            apiInstance.removeTrackingTagSharedAccount(accountId, tagId, adAccountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **adAccountId** | **String**| Ad account to unshare, e.g. &#x60;act_123456789&#x60;. May also be sent in the JSON body. | [optional] |

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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **204** | Ad account unshared (no content). |  -  |
| **400** | &#x60;adAccountId&#x60; missing (neither query nor body), or Meta rejected the unshare. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## removeTrackingTagSharedAccountWithHttpInfo

> ApiResponse<Void> removeTrackingTagSharedAccount removeTrackingTagSharedAccountWithHttpInfo(accountId, tagId, adAccountId)

Stop sharing with an account

&#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. Meta only (platform &#x60;metaads&#x60;); other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        String adAccountId = "adAccountId_example"; // String | Ad account to unshare, e.g. `act_123456789`. May also be sent in the JSON body.
        try {
            ApiResponse<Void> response = apiInstance.removeTrackingTagSharedAccountWithHttpInfo(accountId, tagId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagSharedAccount");
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
| **tagId** | **String**| Pixel id. | |
| **adAccountId** | **String**| Ad account to unshare, e.g. &#x60;act_123456789&#x60;. May also be sent in the JSON body. | [optional] |

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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **204** | Ad account unshared (no content). |  -  |
| **400** | &#x60;adAccountId&#x60; missing (neither query nor body), or Meta rejected the unshare. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |


## updateAdTrackingTags

> UpdateAdTrackingTags200Response updateAdTrackingTags(adId, updateAdTrackingTagsRequest)

Set ad tracking tags

Unified update. Send only the fields for the ad&#39;s platform: - Meta: &#x60;urlTags&#x60; (array of {key,value}). Meta creatives are immutable, so this rebuilds the   creative and repoints the ad. By DEFAULT we PRESERVE the existing creative verbatim   (re-post its object_story_spec + the new url_tags, reusing the image), so you send &#x60;urlTags&#x60;   ALONE, with no need to read back headline/body/CTA. &#x60;creative&#x60; (headline, body, callToAction,   linkUrl, imageUrl) is OPTIONAL and only needed to rebuild explicitly, or for SHARE / page-post   / dark / asset_feed creatives whose object_story_spec Meta strips (those return 422 asking for   &#x60;creative&#x60;). - Google: &#x60;trackingUrlTemplate&#x60; and/or &#x60;finalUrlSuffix&#x60; (full template strings; account quota applies). - LinkedIn: &#x60;dynamicValueParameters&#x60; and/or &#x60;customValueParameters&#x60; (campaign-level Dynamic UTM). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdTrackingTagsRequest updateAdTrackingTagsRequest = new UpdateAdTrackingTagsRequest(); // UpdateAdTrackingTagsRequest | 
        try {
            UpdateAdTrackingTags200Response result = apiInstance.updateAdTrackingTags(adId, updateAdTrackingTagsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateAdTrackingTags");
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
| **adId** | **String**|  | |
| **updateAdTrackingTagsRequest** | [**UpdateAdTrackingTagsRequest**](UpdateAdTrackingTagsRequest.md)|  | |

### Return type

[**UpdateAdTrackingTags200Response**](UpdateAdTrackingTags200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tags as they now stand, in the same shape the GET on this path returns: &#x60;platform&#x60; plus the fields that platform supports. Meta returns &#x60;level&#x60;, &#x60;urlTags&#x60; and &#x60;templateUrlSpec&#x60;; Google returns &#x60;trackingUrlTemplate&#x60; and &#x60;finalUrlSuffix&#x60;. A field the platform does not support is absent.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |
| **422** | Meta creative cannot be rebuilt (e.g. placement-customized/asset-feed/dark creative) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |

## updateAdTrackingTagsWithHttpInfo

> ApiResponse<UpdateAdTrackingTags200Response> updateAdTrackingTags updateAdTrackingTagsWithHttpInfo(adId, updateAdTrackingTagsRequest)

Set ad tracking tags

Unified update. Send only the fields for the ad&#39;s platform: - Meta: &#x60;urlTags&#x60; (array of {key,value}). Meta creatives are immutable, so this rebuilds the   creative and repoints the ad. By DEFAULT we PRESERVE the existing creative verbatim   (re-post its object_story_spec + the new url_tags, reusing the image), so you send &#x60;urlTags&#x60;   ALONE, with no need to read back headline/body/CTA. &#x60;creative&#x60; (headline, body, callToAction,   linkUrl, imageUrl) is OPTIONAL and only needed to rebuild explicitly, or for SHARE / page-post   / dark / asset_feed creatives whose object_story_spec Meta strips (those return 422 asking for   &#x60;creative&#x60;). - Google: &#x60;trackingUrlTemplate&#x60; and/or &#x60;finalUrlSuffix&#x60; (full template strings; account quota applies). - LinkedIn: &#x60;dynamicValueParameters&#x60; and/or &#x60;customValueParameters&#x60; (campaign-level Dynamic UTM). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdTrackingTagsRequest updateAdTrackingTagsRequest = new UpdateAdTrackingTagsRequest(); // UpdateAdTrackingTagsRequest | 
        try {
            ApiResponse<UpdateAdTrackingTags200Response> response = apiInstance.updateAdTrackingTagsWithHttpInfo(adId, updateAdTrackingTagsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateAdTrackingTags");
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
| **adId** | **String**|  | |
| **updateAdTrackingTagsRequest** | [**UpdateAdTrackingTagsRequest**](UpdateAdTrackingTagsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdTrackingTags200Response**](UpdateAdTrackingTags200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tags as they now stand, in the same shape the GET on this path returns: &#x60;platform&#x60; plus the fields that platform supports. Meta returns &#x60;level&#x60;, &#x60;urlTags&#x60; and &#x60;templateUrlSpec&#x60;; Google returns &#x60;trackingUrlTemplate&#x60; and &#x60;finalUrlSuffix&#x60;. A field the platform does not support is absent.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |
| **422** | Meta creative cannot be rebuilt (e.g. placement-customized/asset-feed/dark creative) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |


## updateTrackingTag

> GetTrackingTag200Response updateTrackingTag(accountId, tagId, updateTrackingTagRequest)

Update a tracking tag

Partial-update a pixel. Whitelisted fields: &#x60;name&#x60; (rename), &#x60;enableAutomaticMatching&#x60;, &#x60;automaticMatchingFields&#x60;, &#x60;firstPartyCookieStatus&#x60;, &#x60;dataUseSetting&#x60;. At least one is required. Returns the re-fetched canonical tag. Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  There is no DELETE: Meta has no API to delete a pixel. To stop using one, unshare it from your ad accounts (&#x60;DELETE .../tracking-tags/{tagId}/shared-accounts&#x60;) or disable it in Events Manager. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        UpdateTrackingTagRequest updateTrackingTagRequest = new UpdateTrackingTagRequest(); // UpdateTrackingTagRequest | 
        try {
            GetTrackingTag200Response result = apiInstance.updateTrackingTag(accountId, tagId, updateTrackingTagRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateTrackingTag");
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
| **tagId** | **String**| Pixel id. | |
| **updateTrackingTagRequest** | [**UpdateTrackingTagRequest**](UpdateTrackingTagRequest.md)|  | |

### Return type

[**GetTrackingTag200Response**](GetTrackingTag200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Tracking tag updated (re-fetched canonical state) |  -  |
| **400** | Invalid body (e.g. no fields supplied) or Meta validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## updateTrackingTagWithHttpInfo

> ApiResponse<GetTrackingTag200Response> updateTrackingTag updateTrackingTagWithHttpInfo(accountId, tagId, updateTrackingTagRequest)

Update a tracking tag

Partial-update a pixel. Whitelisted fields: &#x60;name&#x60; (rename), &#x60;enableAutomaticMatching&#x60;, &#x60;automaticMatchingFields&#x60;, &#x60;firstPartyCookieStatus&#x60;, &#x60;dataUseSetting&#x60;. At least one is required. Returns the re-fetched canonical tag. Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  There is no DELETE: Meta has no API to delete a pixel. To stop using one, unshare it from your ad accounts (&#x60;DELETE .../tracking-tags/{tagId}/shared-accounts&#x60;) or disable it in Events Manager. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | Pixel id.
        UpdateTrackingTagRequest updateTrackingTagRequest = new UpdateTrackingTagRequest(); // UpdateTrackingTagRequest | 
        try {
            ApiResponse<GetTrackingTag200Response> response = apiInstance.updateTrackingTagWithHttpInfo(accountId, tagId, updateTrackingTagRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateTrackingTag");
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
| **tagId** | **String**| Pixel id. | |
| **updateTrackingTagRequest** | [**UpdateTrackingTagRequest**](UpdateTrackingTagRequest.md)|  | |

### Return type

ApiResponse<[**GetTrackingTag200Response**](GetTrackingTag200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Tracking tag updated (re-fetched canonical state) |  -  |
| **400** | Invalid body (e.g. no fields supplied) or Meta validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |


## updateTrackingTagEvent

> CreateTrackingTagEvent201Response updateTrackingTagEvent(accountId, tagId, eventId, trackingTagEventInput)

Update a conversion event

Partial update; at least one field. A field the platform does not store answers 400.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | 
        String eventId = "eventId_example"; // String | Event id (`TrackingTagEvent.id`).
        TrackingTagEventInput trackingTagEventInput = new TrackingTagEventInput(); // TrackingTagEventInput | 
        try {
            CreateTrackingTagEvent201Response result = apiInstance.updateTrackingTagEvent(accountId, tagId, eventId, trackingTagEventInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateTrackingTagEvent");
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
| **tagId** | **String**|  | |
| **eventId** | **String**| Event id (&#x60;TrackingTagEvent.id&#x60;). | |
| **trackingTagEventInput** | [**TrackingTagEventInput**](TrackingTagEventInput.md)|  | |

### Return type

[**CreateTrackingTagEvent201Response**](CreateTrackingTagEvent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversion event updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot update conversion events through its API (code &#x60;platform_not_supported&#x60;). |  -  |

## updateTrackingTagEventWithHttpInfo

> ApiResponse<CreateTrackingTagEvent201Response> updateTrackingTagEvent updateTrackingTagEventWithHttpInfo(accountId, tagId, eventId, trackingTagEventInput)

Update a conversion event

Partial update; at least one field. A field the platform does not store answers 400.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TrackingTagsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TrackingTagsApi apiInstance = new TrackingTagsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String tagId = "tagId_example"; // String | 
        String eventId = "eventId_example"; // String | Event id (`TrackingTagEvent.id`).
        TrackingTagEventInput trackingTagEventInput = new TrackingTagEventInput(); // TrackingTagEventInput | 
        try {
            ApiResponse<CreateTrackingTagEvent201Response> response = apiInstance.updateTrackingTagEventWithHttpInfo(accountId, tagId, eventId, trackingTagEventInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#updateTrackingTagEvent");
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
| **tagId** | **String**|  | |
| **eventId** | **String**| Event id (&#x60;TrackingTagEvent.id&#x60;). | |
| **trackingTagEventInput** | [**TrackingTagEventInput**](TrackingTagEventInput.md)|  | |

### Return type

ApiResponse<[**CreateTrackingTagEvent201Response**](CreateTrackingTagEvent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversion event updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot update conversion events through its API (code &#x60;platform_not_supported&#x60;). |  -  |

