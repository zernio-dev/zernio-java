# TrackingTagsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTrackingTagSharedAccount**](TrackingTagsApi.md#addTrackingTagSharedAccount) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Share with an ad account |
| [**addTrackingTagSharedAccountWithHttpInfo**](TrackingTagsApi.md#addTrackingTagSharedAccountWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Share with an ad account |
| [**assignTrackingTagUser**](TrackingTagsApi.md#assignTrackingTagUser) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/users | Assign a user to a tag |
| [**assignTrackingTagUserWithHttpInfo**](TrackingTagsApi.md#assignTrackingTagUserWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/users | Assign a user to a tag |
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
| [**getTrackingTagDiagnostics**](TrackingTagsApi.md#getTrackingTagDiagnostics) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/diagnostics | Get tag diagnostics |
| [**getTrackingTagDiagnosticsWithHttpInfo**](TrackingTagsApi.md#getTrackingTagDiagnosticsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/diagnostics | Get tag diagnostics |
| [**getTrackingTagStats**](TrackingTagsApi.md#getTrackingTagStats) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/stats | Get aggregated event stats |
| [**getTrackingTagStatsWithHttpInfo**](TrackingTagsApi.md#getTrackingTagStatsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/stats | Get aggregated event stats |
| [**getTrackingTagStoreInstall**](TrackingTagsApi.md#getTrackingTagStoreInstall) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Get store install status |
| [**getTrackingTagStoreInstallWithHttpInfo**](TrackingTagsApi.md#getTrackingTagStoreInstallWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Get store install status |
| [**installTrackingTagOnStore**](TrackingTagsApi.md#installTrackingTagOnStore) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Install on a Shopify store or WordPress site |
| [**installTrackingTagOnStoreWithHttpInfo**](TrackingTagsApi.md#installTrackingTagOnStoreWithHttpInfo) | **POST** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Install on a Shopify store or WordPress site |
| [**listTrackingTagEvents**](TrackingTagsApi.md#listTrackingTagEvents) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/events | List conversion events |
| [**listTrackingTagEventsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagEventsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/events | List conversion events |
| [**listTrackingTagPartners**](TrackingTagsApi.md#listTrackingTagPartners) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/partners | List partner businesses of a tag |
| [**listTrackingTagPartnersWithHttpInfo**](TrackingTagsApi.md#listTrackingTagPartnersWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/partners | List partner businesses of a tag |
| [**listTrackingTagSharedAccounts**](TrackingTagsApi.md#listTrackingTagSharedAccounts) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | List accounts it is shared with |
| [**listTrackingTagSharedAccountsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagSharedAccountsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | List accounts it is shared with |
| [**listTrackingTagUsers**](TrackingTagsApi.md#listTrackingTagUsers) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/users | List tag users |
| [**listTrackingTagUsersWithHttpInfo**](TrackingTagsApi.md#listTrackingTagUsersWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags/{tagId}/users | List tag users |
| [**listTrackingTags**](TrackingTagsApi.md#listTrackingTags) | **GET** /v1/accounts/{accountId}/tracking-tags | List tracking tags |
| [**listTrackingTagsWithHttpInfo**](TrackingTagsApi.md#listTrackingTagsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tracking-tags | List tracking tags |
| [**removeTrackingTagFromStore**](TrackingTagsApi.md#removeTrackingTagFromStore) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Remove from a Shopify store or WordPress site |
| [**removeTrackingTagFromStoreWithHttpInfo**](TrackingTagsApi.md#removeTrackingTagFromStoreWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/install | Remove from a Shopify store or WordPress site |
| [**removeTrackingTagSharedAccount**](TrackingTagsApi.md#removeTrackingTagSharedAccount) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Stop sharing with an account |
| [**removeTrackingTagSharedAccountWithHttpInfo**](TrackingTagsApi.md#removeTrackingTagSharedAccountWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/shared-accounts | Stop sharing with an account |
| [**removeTrackingTagUser**](TrackingTagsApi.md#removeTrackingTagUser) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/users/{userId} | Remove a user from a tag |
| [**removeTrackingTagUserWithHttpInfo**](TrackingTagsApi.md#removeTrackingTagUserWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/tracking-tags/{tagId}/users/{userId} | Remove a user from a tag |
| [**updateAdTrackingTags**](TrackingTagsApi.md#updateAdTrackingTags) | **PATCH** /v1/ads/{adId}/tracking-tags | Set ad tracking tags |
| [**updateAdTrackingTagsWithHttpInfo**](TrackingTagsApi.md#updateAdTrackingTagsWithHttpInfo) | **PATCH** /v1/ads/{adId}/tracking-tags | Set ad tracking tags |
| [**updateTrackingTag**](TrackingTagsApi.md#updateTrackingTag) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId} | Update a tracking tag |
| [**updateTrackingTagWithHttpInfo**](TrackingTagsApi.md#updateTrackingTagWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId} | Update a tracking tag |
| [**updateTrackingTagEvent**](TrackingTagsApi.md#updateTrackingTagEvent) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId}/events/{eventId} | Update a conversion event |
| [**updateTrackingTagEventWithHttpInfo**](TrackingTagsApi.md#updateTrackingTagEventWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/tracking-tags/{tagId}/events/{eventId} | Update a conversion event |



## addTrackingTagSharedAccount

> AddTrackingTagSharedAccount201Response addTrackingTagSharedAccount(accountId, tagId, addTrackingTagSharedAccountRequest)

Share with an ad account

Shares the pixel with another ad account so campaigns/audiences in that account can use it. Requires that you administer both the pixel&#39;s owning Business Manager and the target ad account; a pixel on a personal (non-BM) ad account can&#39;t be shared (Meta will reject the call). Meta and LinkedIn; other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): grants &#x60;USE_ONLY&#x60; access from the ad account that created the tag, so the target can use the tag and its conversions but cannot edit or reshare it. &#x60;adAccountId&#x60; is the numeric LinkedIn ad account id. An ad account uses one Insight Tag at a time, so a target that already has one answers 400.  TikTok: links the pixel to an advertiser through Business Center (&#x60;/bc/pixel/link/update/&#x60;, &#x60;adAccountId&#x60; &#x3D; numeric advertiser_id). Only a pixel that is an asset of a Business Center this connection manages can be shared; otherwise the answer is 400 asking to transfer it to Business Center first. 

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

Shares the pixel with another ad account so campaigns/audiences in that account can use it. Requires that you administer both the pixel&#39;s owning Business Manager and the target ad account; a pixel on a personal (non-BM) ad account can&#39;t be shared (Meta will reject the call). Meta and LinkedIn; other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): grants &#x60;USE_ONLY&#x60; access from the ad account that created the tag, so the target can use the tag and its conversions but cannot edit or reshare it. &#x60;adAccountId&#x60; is the numeric LinkedIn ad account id. An ad account uses one Insight Tag at a time, so a target that already has one answers 400.  TikTok: links the pixel to an advertiser through Business Center (&#x60;/bc/pixel/link/update/&#x60;, &#x60;adAccountId&#x60; &#x3D; numeric advertiser_id). Only a pixel that is an asset of a Business Center this connection manages can be shared; otherwise the answer is 400 asking to transfer it to Business Center first. 

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


## assignTrackingTagUser

> AssignTrackingTagUser200Response assignTrackingTagUser(accountId, tagId, assignTrackingTagUserRequest)

Assign a user to a tag

Gives a user of the owning business access to the tag. Assigning an already assigned user replaces their task set.  Meta: &#x60;tasks&#x60; are &#x60;AA_ANALYZE&#x60;, &#x60;ADVERTISE&#x60;, &#x60;ANALYZE&#x60;, &#x60;EDIT&#x60;, &#x60;UPLOAD&#x60;; &#x60;userId&#x60; is the business-scoped id from &#x60;GET /v1/ads/businesses/users&#x60;. A pixel on a personal ad account answers 400. Needs &#x60;business_management&#x60; like the list. 

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
        AssignTrackingTagUserRequest assignTrackingTagUserRequest = new AssignTrackingTagUserRequest(); // AssignTrackingTagUserRequest | 
        try {
            AssignTrackingTagUser200Response result = apiInstance.assignTrackingTagUser(accountId, tagId, assignTrackingTagUserRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#assignTrackingTagUser");
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
| **assignTrackingTagUserRequest** | [**AssignTrackingTagUserRequest**](AssignTrackingTagUserRequest.md)|  | |

### Return type

[**AssignTrackingTagUser200Response**](AssignTrackingTagUser200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User assigned |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no tag user assignment (code &#x60;platform_not_supported&#x60;). |  -  |

## assignTrackingTagUserWithHttpInfo

> ApiResponse<AssignTrackingTagUser200Response> assignTrackingTagUser assignTrackingTagUserWithHttpInfo(accountId, tagId, assignTrackingTagUserRequest)

Assign a user to a tag

Gives a user of the owning business access to the tag. Assigning an already assigned user replaces their task set.  Meta: &#x60;tasks&#x60; are &#x60;AA_ANALYZE&#x60;, &#x60;ADVERTISE&#x60;, &#x60;ANALYZE&#x60;, &#x60;EDIT&#x60;, &#x60;UPLOAD&#x60;; &#x60;userId&#x60; is the business-scoped id from &#x60;GET /v1/ads/businesses/users&#x60;. A pixel on a personal ad account answers 400. Needs &#x60;business_management&#x60; like the list. 

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
        AssignTrackingTagUserRequest assignTrackingTagUserRequest = new AssignTrackingTagUserRequest(); // AssignTrackingTagUserRequest | 
        try {
            ApiResponse<AssignTrackingTagUser200Response> response = apiInstance.assignTrackingTagUserWithHttpInfo(accountId, tagId, assignTrackingTagUserRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#assignTrackingTagUser");
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
| **assignTrackingTagUserRequest** | [**AssignTrackingTagUserRequest**](AssignTrackingTagUserRequest.md)|  | |

### Return type

ApiResponse<[**AssignTrackingTagUser200Response**](AssignTrackingTagUser200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User assigned |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no tag user assignment (code &#x60;platform_not_supported&#x60;). |  -  |


## createTrackingTag

> CreateTrackingTag201Response createTrackingTag(accountId, createTrackingTagRequest)

Create a tracking tag

Meta: creates a Meta Pixel on the given ad account (&#x60;POST /act_{id}/adspixels&#x60;, where &#x60;name&#x60; is the only input). Returns the created tag including its install &#x60;code&#x60;. The pixel is owned by the Business Manager that owns the ad account; a pixel created on a personal (non-BM) ad account ends up with &#x60;ownerBusinessId: null&#x60; and can&#39;t be shared with other ad accounts.  Creating a Meta pixel does NOT install it. Install the returned &#x60;code&#x60; snippet on the site, or send events server-side via &#x60;POST /v1/ads/conversions&#x60;. The check &#x60;installed&#x60; is derived from &#x60;lastFiredTime&#x60;.  OpenAI Ads: creates an OpenAI pixel AND provisions a Conversions API key for it in the same call (&#x60;adAccountId&#x60; is required by this endpoint but ignored: one API key maps to exactly one ad account, so there&#39;s nothing to select). Returns 422 (&#x60;FEATURE_NOT_AVAILABLE&#x60;) if the ad account isn&#39;t enabled for pixel management; contact your OpenAI partner representative to enable it. There is no delete API for OpenAI pixels. If the pixel is created but the Conversions API key provisioning then fails, the pixel is left live on OpenAI (it cannot be cleaned up) and the error message names the surviving pixel id and warns against retrying, since a retry would create a second, orphaned pixel.  NOT idempotent on either platform: each call creates a new pixel (and, for OpenAI, a new Conversions API key plus, with &#x60;defaultEventType&#x60;, a new conversion event setting). Do not retry blindly on timeout. Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): creates the ad account&#39;s Insight Tag (&#x60;POST /rest/insightTags&#x60;). Idempotent: an ad account holds at most one Insight Tag, so when it already has one that tag is returned and nothing is created. &#x60;name&#x60; is ignored (LinkedIn tags have no name) and there is no API to delete an Insight Tag.  Pinterest (platform &#x60;pinterestads&#x60;): creates a Pinterest tag on the numeric ad account &#x60;adAccountId&#x60; (&#x60;POST /v5/ad_accounts/{id}/conversion_tags&#x60;). Returns the tag with Pinterest&#39;s &#x60;code&#x60; snippet. &#x60;automaticMatchingFields&#x60; switches on automatic enhanced match for those fields. NOT idempotent and Pinterest has no dry-run and no delete for tags (DELETE on &#x60;conversion_tags/{id}&#x60; answers 405), so never retry blindly: list first.  Google Ads (&#x60;googleads&#x60;): every Google Ads account has exactly one Google tag (&#x60;AW-...&#x60;), so this is idempotent. &#x60;adAccountId&#x60; is the 10-digit customer id. When the account already tracks conversions the existing tag is returned (201) and nothing is created. Otherwise a first WEBPAGE conversion action named &#x60;name&#x60; (category DEFAULT) is created, which is what switches Google&#39;s conversion tracking on, and the tag is returned with it as its first event.  TikTok: &#x60;POST /pixel/create/&#x60; on the advertiser in &#x60;adAccountId&#x60; (numeric). Names are at most 40 characters with no emoji and must be unique; TikTok refuses a duplicate name (400), which is its only retry guard. TikTok has no pixel delete API.  Pinterest&#39;s &#x60;code&#x60; snippet. NOT idempotent and Pinterest has no dry-run and no delete for tags, so never retry blindly: list first.  X Ads (platform &#x60;xads&#x60;): creates the ad account&#39;s X Pixel (its UNIVERSAL website tag) with first-party cookies on. &#x60;adAccountId&#x60; is the X ad account id; &#x60;name&#x60; is not stored (X pixels have no name). X allows one pixel per ad account and cannot delete one, so an account that already has a pixel answers 409 without writing anything. 

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

Meta: creates a Meta Pixel on the given ad account (&#x60;POST /act_{id}/adspixels&#x60;, where &#x60;name&#x60; is the only input). Returns the created tag including its install &#x60;code&#x60;. The pixel is owned by the Business Manager that owns the ad account; a pixel created on a personal (non-BM) ad account ends up with &#x60;ownerBusinessId: null&#x60; and can&#39;t be shared with other ad accounts.  Creating a Meta pixel does NOT install it. Install the returned &#x60;code&#x60; snippet on the site, or send events server-side via &#x60;POST /v1/ads/conversions&#x60;. The check &#x60;installed&#x60; is derived from &#x60;lastFiredTime&#x60;.  OpenAI Ads: creates an OpenAI pixel AND provisions a Conversions API key for it in the same call (&#x60;adAccountId&#x60; is required by this endpoint but ignored: one API key maps to exactly one ad account, so there&#39;s nothing to select). Returns 422 (&#x60;FEATURE_NOT_AVAILABLE&#x60;) if the ad account isn&#39;t enabled for pixel management; contact your OpenAI partner representative to enable it. There is no delete API for OpenAI pixels. If the pixel is created but the Conversions API key provisioning then fails, the pixel is left live on OpenAI (it cannot be cleaned up) and the error message names the surviving pixel id and warns against retrying, since a retry would create a second, orphaned pixel.  NOT idempotent on either platform: each call creates a new pixel (and, for OpenAI, a new Conversions API key plus, with &#x60;defaultEventType&#x60;, a new conversion event setting). Do not retry blindly on timeout. Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): creates the ad account&#39;s Insight Tag (&#x60;POST /rest/insightTags&#x60;). Idempotent: an ad account holds at most one Insight Tag, so when it already has one that tag is returned and nothing is created. &#x60;name&#x60; is ignored (LinkedIn tags have no name) and there is no API to delete an Insight Tag.  Pinterest (platform &#x60;pinterestads&#x60;): creates a Pinterest tag on the numeric ad account &#x60;adAccountId&#x60; (&#x60;POST /v5/ad_accounts/{id}/conversion_tags&#x60;). Returns the tag with Pinterest&#39;s &#x60;code&#x60; snippet. &#x60;automaticMatchingFields&#x60; switches on automatic enhanced match for those fields. NOT idempotent and Pinterest has no dry-run and no delete for tags (DELETE on &#x60;conversion_tags/{id}&#x60; answers 405), so never retry blindly: list first.  Google Ads (&#x60;googleads&#x60;): every Google Ads account has exactly one Google tag (&#x60;AW-...&#x60;), so this is idempotent. &#x60;adAccountId&#x60; is the 10-digit customer id. When the account already tracks conversions the existing tag is returned (201) and nothing is created. Otherwise a first WEBPAGE conversion action named &#x60;name&#x60; (category DEFAULT) is created, which is what switches Google&#39;s conversion tracking on, and the tag is returned with it as its first event.  TikTok: &#x60;POST /pixel/create/&#x60; on the advertiser in &#x60;adAccountId&#x60; (numeric). Names are at most 40 characters with no emoji and must be unique; TikTok refuses a duplicate name (400), which is its only retry guard. TikTok has no pixel delete API.  Pinterest&#39;s &#x60;code&#x60; snippet. NOT idempotent and Pinterest has no dry-run and no delete for tags, so never retry blindly: list first.  X Ads (platform &#x60;xads&#x60;): creates the ad account&#39;s X Pixel (its UNIVERSAL website tag) with first-party cookies on. &#x60;adAccountId&#x60; is the X ad account id; &#x60;name&#x60; is not stored (X pixels have no name). X allows one pixel per ad account and cannot delete one, so an account that already has a pixel answers 409 without writing anything. 

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

Creates a conversion event tied to the tag. Pass the platform&#39;s own event type in &#x60;type&#x60; (e.g. Google &#x60;PURCHASE&#x60;, LinkedIn &#x60;ADD_TO_CART&#x60;, X &#x60;CHECKOUT_INITIATED&#x60;) or a neutral &#x60;siteEvent&#x60; the platform maps to its closest type. Each platform stores a subset of the optional fields; sending one it does not store answers 400 naming the supported fields. NOT idempotent unless noted per platform: do not retry blindly.  OpenAI Ads: creates a conversion event setting on the pixel (&#x60;POST /conversions/event_settings&#x60;, source &#x3D; the pixel). Accepts &#x60;name&#x60;, &#x60;type&#x60; and &#x60;siteEvent&#x60; only. &#x60;type&#x60; is a standard event (&#x60;order_created&#x60;, &#x60;lead_created&#x60;, &#x60;items_added&#x60;, &#x60;contents_viewed&#x60;, &#x60;checkout_started&#x60;, &#x60;registration_completed&#x60;, &#x60;subscription_created&#x60;, &#x60;trial_started&#x60;, &#x60;appointment_scheduled&#x60;, &#x60;page_viewed&#x60;, &#x60;app_installed&#x60;, &#x60;app_opened&#x60;) or, for anything else, the custom event name itself (1 to 64 letters, digits, underscores or dashes; stored lowercase). &#x60;siteEvent&#x60; maps &#x60;search&#x60; and &#x60;add_payment_info&#x60; to the custom events &#x60;search&#x60; and &#x60;addpaymentinfo&#x60;, the names Zernio&#39;s Shopify pixel sends. The click attribution window is 30 days, the only value OpenAI documents. Only standard events can be a conversions campaign&#39;s optimization goal.  LinkedIn (&#x60;linkedinads&#x60;): creates an event-specific Insight Tag conversion rule (no URL match rules), the kind a page or the Shopify pixel fires by id. &#x60;type&#x60; is a LinkedIn conversion type (e.g. &#x60;PURCHASE&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;START_CHECKOUT&#x60;, &#x60;LEAD&#x60;); &#x60;siteEvent&#x60; maps to &#x60;KEY_PAGE_VIEW&#x60;, &#x60;VIEW_CONTENT&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;SEARCH&#x60;, &#x60;START_CHECKOUT&#x60;, &#x60;ADD_BILLING_INFO&#x60; or &#x60;PURCHASE&#x60;. &#x60;defaultValue&#x60; needs &#x60;currency&#x60; (the ad account currency) and is a fallback: a value sent with the event wins. Click and view windows are in days (LinkedIn validates them: the docs list 1, 7 and 30, and rules with 90 exist). Stores name, type, siteEvent, enabled, defaultValue, currency, clickWindowDays, viewWindowDays. Not idempotent.  Meta: creates a custom conversion on &#x60;adAccountId&#x60; (default: the pixel&#39;s owner ad account). Accepts &#x60;name&#x60;, &#x60;type&#x60; (Meta &#x60;custom_event_type&#x60;: &#x60;PURCHASE&#x60;, &#x60;LEAD&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;COMPLETE_REGISTRATION&#x60;, &#x60;OTHER&#x60;...), &#x60;siteEvent&#x60;, &#x60;urlContains&#x60; and &#x60;defaultValue&#x60; (in the ad account currency). The rule matches the standard event of &#x60;siteEvent&#x60; (or of &#x60;type&#x60;), plus &#x60;urlContains&#x60; when given; &#x60;urlContains&#x60; alone matches page views on that URL. &#x60;type: OTHER&#x60; needs &#x60;siteEvent&#x60; or &#x60;urlContains&#x60;. Idempotent by name: an active conversion with the same name on this pixel is returned instead of a duplicate. Meta caps custom conversions per ad account; the cap answers 400.  Google Ads (&#x60;googleads&#x60;): creates a WEBPAGE conversion action. &#x60;type&#x60; is a ConversionActionCategory (e.g. &#x60;PURCHASE&#x60;, &#x60;SIGNUP&#x60;, &#x60;DEFAULT&#x60;); &#x60;siteEvent&#x60; maps page_view, add_to_cart, initiate_checkout and purchase, while view_content, search and add_payment_info answer 400 (Google has no category for them). Stored fields: name, type, defaultValue, currency, alwaysUseDefaultValue, clickWindowDays (1 to 90), viewWindowDays (1 to 30), primary, countingType, enabled. Actions are created enabled (&#x60;enabled: false&#x60; answers 400); Google blocks the HIDDEN status on WEBPAGE actions. Names are unique per account, so a replay answers 400 (DUPLICATE_NAME) instead of creating a second one.  Pinterest (platform &#x60;pinterestads&#x60;): creates an advertiser defined event on the tag&#39;s ad account. Fields: &#x60;name&#x60; (1-100 letters, digits, &#x60;_&#x60; or &#x60;-&#x60;, case-insensitive, max 15 per ad account) and &#x60;type&#x60; (one of Pinterest&#39;s optimizable types: SIGNUP, ADD_TO_CART, LEAD, CHECKOUT, SUBSCRIBE, ADD_TO_WISHLIST, ADD_PAYMENT_INFO, INITIATE_CHECKOUT, CONTACT, CUSTOMIZE_PRODUCT, FIND_LOCATION, SCHEDULE, SUBMIT_APPLICATION, START_TRIAL, PAGE_VISIT, VIEW_CATEGORY, VIEW_CONTENT, SEARCH, WATCH_VIDEO) or &#x60;siteEvent&#x60;. A duplicate name answers 400.  TikTok: &#x60;POST /pixel/event/create/&#x60;. &#x60;type&#x60; is a TikTok pixel event type (SHOPPING, ON_WEB_CART, ON_WEB_DETAIL, INITIATE_ORDER, ADD_BILLING, ON_WEB_SEARCH, PAGE_VIEW, ON_WEB_REGISTER, FORM, ...), or pass &#x60;siteEvent&#x60;. Stores &#x60;name&#x60; (at most 40 characters), &#x60;defaultValue&#x60; and &#x60;currency&#x60; (USD, JPY or INR only). TikTok returns no id: the new event is read back from the pixel, and while TikTok&#39;s listing has not refreshed the response carries an empty &#x60;id&#x60; and &#x60;status: pending&#x60;.  X Ads (platform &#x60;xads&#x60;): creates a web event tag. Fields: &#x60;name&#x60;, &#x60;type&#x60; (X enum: ADDED_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, CHECKOUT_INITIATED, CONTENT_VIEW, CUSTOM, DOWNLOAD, INSTALL, LANDING_PAGE_VIEW, LOGIN, PRODUCT_CUSTOMIZATION, PURCHASE, SEARCH, SESSION, SIGN_UP, SITE_VISIT, START_TRIAL, SUBSCRIBE) or &#x60;siteEvent&#x60;, &#x60;clickWindowDays&#x60; (1, 7, 14, 30, 60 or 90; default 30) and &#x60;viewWindowDays&#x60; (0, 1, 7, 14, 30, 60 or 90, at most the click window; default 1). Retargeting is enabled, as in Events Manager. 

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

Creates a conversion event tied to the tag. Pass the platform&#39;s own event type in &#x60;type&#x60; (e.g. Google &#x60;PURCHASE&#x60;, LinkedIn &#x60;ADD_TO_CART&#x60;, X &#x60;CHECKOUT_INITIATED&#x60;) or a neutral &#x60;siteEvent&#x60; the platform maps to its closest type. Each platform stores a subset of the optional fields; sending one it does not store answers 400 naming the supported fields. NOT idempotent unless noted per platform: do not retry blindly.  OpenAI Ads: creates a conversion event setting on the pixel (&#x60;POST /conversions/event_settings&#x60;, source &#x3D; the pixel). Accepts &#x60;name&#x60;, &#x60;type&#x60; and &#x60;siteEvent&#x60; only. &#x60;type&#x60; is a standard event (&#x60;order_created&#x60;, &#x60;lead_created&#x60;, &#x60;items_added&#x60;, &#x60;contents_viewed&#x60;, &#x60;checkout_started&#x60;, &#x60;registration_completed&#x60;, &#x60;subscription_created&#x60;, &#x60;trial_started&#x60;, &#x60;appointment_scheduled&#x60;, &#x60;page_viewed&#x60;, &#x60;app_installed&#x60;, &#x60;app_opened&#x60;) or, for anything else, the custom event name itself (1 to 64 letters, digits, underscores or dashes; stored lowercase). &#x60;siteEvent&#x60; maps &#x60;search&#x60; and &#x60;add_payment_info&#x60; to the custom events &#x60;search&#x60; and &#x60;addpaymentinfo&#x60;, the names Zernio&#39;s Shopify pixel sends. The click attribution window is 30 days, the only value OpenAI documents. Only standard events can be a conversions campaign&#39;s optimization goal.  LinkedIn (&#x60;linkedinads&#x60;): creates an event-specific Insight Tag conversion rule (no URL match rules), the kind a page or the Shopify pixel fires by id. &#x60;type&#x60; is a LinkedIn conversion type (e.g. &#x60;PURCHASE&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;START_CHECKOUT&#x60;, &#x60;LEAD&#x60;); &#x60;siteEvent&#x60; maps to &#x60;KEY_PAGE_VIEW&#x60;, &#x60;VIEW_CONTENT&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;SEARCH&#x60;, &#x60;START_CHECKOUT&#x60;, &#x60;ADD_BILLING_INFO&#x60; or &#x60;PURCHASE&#x60;. &#x60;defaultValue&#x60; needs &#x60;currency&#x60; (the ad account currency) and is a fallback: a value sent with the event wins. Click and view windows are in days (LinkedIn validates them: the docs list 1, 7 and 30, and rules with 90 exist). Stores name, type, siteEvent, enabled, defaultValue, currency, clickWindowDays, viewWindowDays. Not idempotent.  Meta: creates a custom conversion on &#x60;adAccountId&#x60; (default: the pixel&#39;s owner ad account). Accepts &#x60;name&#x60;, &#x60;type&#x60; (Meta &#x60;custom_event_type&#x60;: &#x60;PURCHASE&#x60;, &#x60;LEAD&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;COMPLETE_REGISTRATION&#x60;, &#x60;OTHER&#x60;...), &#x60;siteEvent&#x60;, &#x60;urlContains&#x60; and &#x60;defaultValue&#x60; (in the ad account currency). The rule matches the standard event of &#x60;siteEvent&#x60; (or of &#x60;type&#x60;), plus &#x60;urlContains&#x60; when given; &#x60;urlContains&#x60; alone matches page views on that URL. &#x60;type: OTHER&#x60; needs &#x60;siteEvent&#x60; or &#x60;urlContains&#x60;. Idempotent by name: an active conversion with the same name on this pixel is returned instead of a duplicate. Meta caps custom conversions per ad account; the cap answers 400.  Google Ads (&#x60;googleads&#x60;): creates a WEBPAGE conversion action. &#x60;type&#x60; is a ConversionActionCategory (e.g. &#x60;PURCHASE&#x60;, &#x60;SIGNUP&#x60;, &#x60;DEFAULT&#x60;); &#x60;siteEvent&#x60; maps page_view, add_to_cart, initiate_checkout and purchase, while view_content, search and add_payment_info answer 400 (Google has no category for them). Stored fields: name, type, defaultValue, currency, alwaysUseDefaultValue, clickWindowDays (1 to 90), viewWindowDays (1 to 30), primary, countingType, enabled. Actions are created enabled (&#x60;enabled: false&#x60; answers 400); Google blocks the HIDDEN status on WEBPAGE actions. Names are unique per account, so a replay answers 400 (DUPLICATE_NAME) instead of creating a second one.  Pinterest (platform &#x60;pinterestads&#x60;): creates an advertiser defined event on the tag&#39;s ad account. Fields: &#x60;name&#x60; (1-100 letters, digits, &#x60;_&#x60; or &#x60;-&#x60;, case-insensitive, max 15 per ad account) and &#x60;type&#x60; (one of Pinterest&#39;s optimizable types: SIGNUP, ADD_TO_CART, LEAD, CHECKOUT, SUBSCRIBE, ADD_TO_WISHLIST, ADD_PAYMENT_INFO, INITIATE_CHECKOUT, CONTACT, CUSTOMIZE_PRODUCT, FIND_LOCATION, SCHEDULE, SUBMIT_APPLICATION, START_TRIAL, PAGE_VISIT, VIEW_CATEGORY, VIEW_CONTENT, SEARCH, WATCH_VIDEO) or &#x60;siteEvent&#x60;. A duplicate name answers 400.  TikTok: &#x60;POST /pixel/event/create/&#x60;. &#x60;type&#x60; is a TikTok pixel event type (SHOPPING, ON_WEB_CART, ON_WEB_DETAIL, INITIATE_ORDER, ADD_BILLING, ON_WEB_SEARCH, PAGE_VIEW, ON_WEB_REGISTER, FORM, ...), or pass &#x60;siteEvent&#x60;. Stores &#x60;name&#x60; (at most 40 characters), &#x60;defaultValue&#x60; and &#x60;currency&#x60; (USD, JPY or INR only). TikTok returns no id: the new event is read back from the pixel, and while TikTok&#39;s listing has not refreshed the response carries an empty &#x60;id&#x60; and &#x60;status: pending&#x60;.  X Ads (platform &#x60;xads&#x60;): creates a web event tag. Fields: &#x60;name&#x60;, &#x60;type&#x60; (X enum: ADDED_PAYMENT_INFO, ADD_TO_CART, ADD_TO_WISHLIST, CHECKOUT_INITIATED, CONTENT_VIEW, CUSTOM, DOWNLOAD, INSTALL, LANDING_PAGE_VIEW, LOGIN, PRODUCT_CUSTOMIZATION, PURCHASE, SEARCH, SESSION, SIGN_UP, SITE_VISIT, START_TRIAL, SUBSCRIBE) or &#x60;siteEvent&#x60;, &#x60;clickWindowDays&#x60; (1, 7, 14, 30, 60 or 90; default 30) and &#x60;viewWindowDays&#x60; (0, 1, 7, 14, 30, 60 or 90, at most the click window; default 1). Retargeting is enabled, as in Events Manager. 

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

Removes the conversion event. Platforms without a hard delete archive or disable it instead; &#x60;state&#x60; in the response says which (&#x60;deleted&#x60;, &#x60;archived&#x60;, &#x60;disabled&#x60;).  OpenAI Ads answers 501: there is no delete or archive route for event settings (&#x60;DELETE /v1/conversions/event_settings/{id}&#x60; and &#x60;POST .../{id}/archive&#x60; answer 404 \&quot;Invalid URL\&quot;). Archive the event in OpenAI Ads Manager.  LinkedIn (&#x60;linkedinads&#x60;): LinkedIn has no delete for conversion rules (not in the conversion-tracking API, and &#x60;DELETE /rest/conversions/{id}&#x60; has no route), so the rule is disabled (&#x60;enabled: false&#x60;) and &#x60;state&#x60; is &#x60;disabled&#x60;. Re-enable it with &#x60;enabled: true&#x60;.  Meta: &#x60;archived&#x60;. Meta&#39;s delete archives the custom conversion (it stays readable with &#x60;status: archived&#x60;) and there is no hard delete; deleting an archived one is a no-op.  Google Ads (&#x60;googleads&#x60;): removes the conversion action (state &#x60;archived&#x60;). Google keeps it with status REMOVED and its history; PATCH with &#x60;enabled: true&#x60; restores it. Deleting an already archived action succeeds without a call to Google.  Pinterest (platform &#x60;pinterestads&#x60;): stops Pinterest tracking the event name (&#x60;state: disabled&#x60;); Pinterest keeps the event&#39;s history.  TikTok Ads answers 501: TikTok&#39;s &#x60;/pixel/event/delete/&#x60; answers OK but leaves the event on the pixel, so nothing is deleted. Delete the event in TikTok Events Manager.  X Ads (platform &#x60;xads&#x60;): deletes the web event tag for good. Events X auto-created with the pixel cannot be deleted (400). X keeps the event&#39;s own website tag id on the account (it has no delete for website tags), left without a conversion event. 

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

Removes the conversion event. Platforms without a hard delete archive or disable it instead; &#x60;state&#x60; in the response says which (&#x60;deleted&#x60;, &#x60;archived&#x60;, &#x60;disabled&#x60;).  OpenAI Ads answers 501: there is no delete or archive route for event settings (&#x60;DELETE /v1/conversions/event_settings/{id}&#x60; and &#x60;POST .../{id}/archive&#x60; answer 404 \&quot;Invalid URL\&quot;). Archive the event in OpenAI Ads Manager.  LinkedIn (&#x60;linkedinads&#x60;): LinkedIn has no delete for conversion rules (not in the conversion-tracking API, and &#x60;DELETE /rest/conversions/{id}&#x60; has no route), so the rule is disabled (&#x60;enabled: false&#x60;) and &#x60;state&#x60; is &#x60;disabled&#x60;. Re-enable it with &#x60;enabled: true&#x60;.  Meta: &#x60;archived&#x60;. Meta&#39;s delete archives the custom conversion (it stays readable with &#x60;status: archived&#x60;) and there is no hard delete; deleting an archived one is a no-op.  Google Ads (&#x60;googleads&#x60;): removes the conversion action (state &#x60;archived&#x60;). Google keeps it with status REMOVED and its history; PATCH with &#x60;enabled: true&#x60; restores it. Deleting an already archived action succeeds without a call to Google.  Pinterest (platform &#x60;pinterestads&#x60;): stops Pinterest tracking the event name (&#x60;state: disabled&#x60;); Pinterest keeps the event&#39;s history.  TikTok Ads answers 501: TikTok&#39;s &#x60;/pixel/event/delete/&#x60; answers OK but leaves the event on the pixel, so nothing is deleted. Delete the event in TikTok Events Manager.  X Ads (platform &#x60;xads&#x60;): deletes the web event tag for good. Events X auto-created with the pixel cannot be deleted (400). X keeps the event&#39;s own website tag id on the account (it has no delete for website tags), left without a conversion event. 

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

Returns the full tag record including the base-code &#x60;code&#x60; snippet, &#x60;lastFiredTime&#x60;, &#x60;ownerBusinessId&#x60;, &#x60;isUnavailable&#x60;, etc. Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  OpenAI Ads (&#x60;openaiads&#x60;): &#x60;tagId&#x60; is the pixel&#39;s API id (&#x60;cds_...&#x60;) or its &#x60;pixel_id&#x60;. OpenAI documents no single-pixel read, so the tag is resolved from the pixel list; the response adds &#x60;code&#x60; (the official &#x60;oaiq&#x60; base code plus &#x60;page_viewed&#x60;) and &#x60;events&#x60; (the conversion event settings whose source is this pixel). &#x60;siteTagId&#x60; is the &#x60;pixel_id&#x60; the site and the Conversions API send; &#x60;id&#x60; is what event settings reference.  LinkedIn (&#x60;linkedinads&#x60;): &#x60;code&#x60; is LinkedIn&#39;s base code, &#x60;lastFiredTime&#x60; is the most recent callback across the tag&#39;s domains (unix seconds, null when it never fired) and &#x60;events&#x60; lists the ad account&#39;s conversion rules. &#x60;siteEvent&#x60; and &#x60;siteEventId&#x60; are set only on rules a page can fire (event-specific Insight Tag rules: not Conversions API rules, no URL match rules). &#x60;adAccountId&#x60; picks which ad account&#39;s rules to read; it defaults to the account that created the tag.  Pinterest (platform &#x60;pinterestads&#x60;): returns the tag with Pinterest&#39;s own &#x60;code&#x60; snippet and &#x60;lastFiredTime&#x60;. Without &#x60;adAccountId&#x60; Zernio finds the ad account that owns the tag (404 when no readable ad account holds it).  TikTok: read from &#x60;/pixel/list/?pixel_id&#x3D;&#x60;; &#x60;code&#x60; is TikTok&#39;s &#x60;pixel_script&#x60;, &#x60;events&#x60; the pixel events. &#x60;lastFiredTime&#x60; is not available on TikTok. Without &#x60;adAccountId&#x60; the connection&#39;s advertisers are searched.  X Ads (platform &#x60;xads&#x60;): &#x60;tagId&#x60; is the X ad account id. Returns the pixel id as &#x60;siteTagId&#x60;, the X Pixel base code as &#x60;code&#x60;, and the conversion events the site can fire in &#x60;events&#x60; (each with &#x60;siteEventId&#x60; &#x3D; &#x60;tw-&lt;pixel&gt;-&lt;event&gt;&#x60;, also the &#x60;event_id&#x60; of the X Conversions API). An ad account without a pixel answers 400. 

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

Returns the full tag record including the base-code &#x60;code&#x60; snippet, &#x60;lastFiredTime&#x60;, &#x60;ownerBusinessId&#x60;, &#x60;isUnavailable&#x60;, etc. Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  OpenAI Ads (&#x60;openaiads&#x60;): &#x60;tagId&#x60; is the pixel&#39;s API id (&#x60;cds_...&#x60;) or its &#x60;pixel_id&#x60;. OpenAI documents no single-pixel read, so the tag is resolved from the pixel list; the response adds &#x60;code&#x60; (the official &#x60;oaiq&#x60; base code plus &#x60;page_viewed&#x60;) and &#x60;events&#x60; (the conversion event settings whose source is this pixel). &#x60;siteTagId&#x60; is the &#x60;pixel_id&#x60; the site and the Conversions API send; &#x60;id&#x60; is what event settings reference.  LinkedIn (&#x60;linkedinads&#x60;): &#x60;code&#x60; is LinkedIn&#39;s base code, &#x60;lastFiredTime&#x60; is the most recent callback across the tag&#39;s domains (unix seconds, null when it never fired) and &#x60;events&#x60; lists the ad account&#39;s conversion rules. &#x60;siteEvent&#x60; and &#x60;siteEventId&#x60; are set only on rules a page can fire (event-specific Insight Tag rules: not Conversions API rules, no URL match rules). &#x60;adAccountId&#x60; picks which ad account&#39;s rules to read; it defaults to the account that created the tag.  Pinterest (platform &#x60;pinterestads&#x60;): returns the tag with Pinterest&#39;s own &#x60;code&#x60; snippet and &#x60;lastFiredTime&#x60;. Without &#x60;adAccountId&#x60; Zernio finds the ad account that owns the tag (404 when no readable ad account holds it).  TikTok: read from &#x60;/pixel/list/?pixel_id&#x3D;&#x60;; &#x60;code&#x60; is TikTok&#39;s &#x60;pixel_script&#x60;, &#x60;events&#x60; the pixel events. &#x60;lastFiredTime&#x60; is not available on TikTok. Without &#x60;adAccountId&#x60; the connection&#39;s advertisers are searched.  X Ads (platform &#x60;xads&#x60;): &#x60;tagId&#x60; is the X ad account id. Returns the pixel id as &#x60;siteTagId&#x60;, the X Pixel base code as &#x60;code&#x60;, and the conversion events the site can fire in &#x60;events&#x60; (each with &#x60;siteEventId&#x60; &#x3D; &#x60;tw-&lt;pixel&gt;-&lt;event&gt;&#x60;, also the &#x60;event_id&#x60; of the X Conversions API). An ad account without a pixel answers 400. 

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


## getTrackingTagDiagnostics

> GetTrackingTagDiagnostics200Response getTrackingTagDiagnostics(accountId, tagId)

Get tag diagnostics

The platform&#39;s health checks for the tag. Platforms without tag diagnostics answer 501.  Meta: the pixel&#39;s checks from Events Manager (&#x60;da_checks&#x60;), e.g. whether events miss parameters or their content ids do not match the pixel&#39;s catalogs. 

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
        try {
            GetTrackingTagDiagnostics200Response result = apiInstance.getTrackingTagDiagnostics(accountId, tagId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagDiagnostics");
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

### Return type

[**GetTrackingTagDiagnostics200Response**](GetTrackingTagDiagnostics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Diagnostics fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no tag diagnostics (code &#x60;platform_not_supported&#x60;). |  -  |
| **502** | The platform was unreachable or returned an unclassified error (type: platform_error). Retryable. |  -  |

## getTrackingTagDiagnosticsWithHttpInfo

> ApiResponse<GetTrackingTagDiagnostics200Response> getTrackingTagDiagnostics getTrackingTagDiagnosticsWithHttpInfo(accountId, tagId)

Get tag diagnostics

The platform&#39;s health checks for the tag. Platforms without tag diagnostics answer 501.  Meta: the pixel&#39;s checks from Events Manager (&#x60;da_checks&#x60;), e.g. whether events miss parameters or their content ids do not match the pixel&#39;s catalogs. 

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
        try {
            ApiResponse<GetTrackingTagDiagnostics200Response> response = apiInstance.getTrackingTagDiagnosticsWithHttpInfo(accountId, tagId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#getTrackingTagDiagnostics");
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

### Return type

ApiResponse<[**GetTrackingTagDiagnostics200Response**](GetTrackingTagDiagnostics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Diagnostics fetched |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no tag diagnostics (code &#x60;platform_not_supported&#x60;). |  -  |
| **502** | The platform was unreachable or returned an unclassified error (type: platform_error). Retryable. |  -  |


## getTrackingTagStats

> GetTrackingTagStats200Response getTrackingTagStats(accountId, tagId, adAccountId, aggregation, startTime, endTime)

Get aggregated event stats

Returns event counts / health for the tag, where the platform exposes them. Meta: aggregated counts (&#x60;GET /{pixel_id}/stats&#x60;), rows passed through as-is; their shape depends on the &#x60;aggregation&#x60; requested. Platforms without a stats API answer 501.  OpenAI Ads: the recent-events stream (&#x60;GET /conversions/events&#x60;), the latest (at most 50) events received in the last 15 minutes, one row per event (&#x60;event_type&#x60;, &#x60;api_channel&#x60;, &#x60;event_timestamp_ms&#x60;, &#x60;received_at_ms&#x60;, ...). Both sources appear: &#x60;api_channel&#x60; is &#x60;pixel_sdk&#x60; for the on-site Pixel (including its &#x60;openai::sdk_init&#x60; load event) and &#x60;server_to_server&#x60; for Conversions API events. It is a fixed window: &#x60;startTime&#x60;/&#x60;endTime&#x60; answer 400. Use it to confirm an install fires; attributed totals come from ads analytics. Accounts not enabled for the stream answer 422 &#x60;feature_not_available&#x60;.  LinkedIn (&#x60;linkedinads&#x60;): health rows rather than counts, since LinkedIn exposes no per- event fire counts: one row per site domain the tag has seen (&#x60;kind: domain&#x60;, &#x60;domainName&#x60;, &#x60;lastFiredTime&#x60;, &#x60;creationTime&#x60;, &#x60;blocked&#x60;), capped at the 100 domains that fired most recently (newest first; a tag seen on more domains drops the least recent), and one per conversion rule (&#x60;kind: conversion_rule&#x60;, &#x60;id&#x60;, &#x60;name&#x60;, &#x60;type&#x60;, &#x60;conversionMethod&#x60;, &#x60;status&#x60;, &#x60;lastFiredTime&#x60;). Times are unix seconds; &#x60;startTime&#x60;/&#x60;endTime&#x60; are ignored.  Pinterest (platform &#x60;pinterestads&#x60;): rows typed by &#x60;type&#x60;: one &#x60;tag&#x60; row (&#x60;lastFiredTime&#x60;, &#x60;status&#x60;, &#x60;enhancedMatchStatus&#x60;), &#x60;event&#x60; rows for the conversion events Pinterest has seen on the tag (&#x60;source&#x60; is &#x60;page_visit&#x60; or &#x60;ocpm_eligible&#x60;, the latter meaning the event can be optimized for, with the neutral &#x60;siteEvent&#x60; where one maps), and &#x60;event_quality&#x60; rows with the ad account&#39;s Event Quality Score for tag events over the last &#x60;1d&#x60; and &#x60;14d&#x60; (ad-account level, not per tag; an account Pinterest cannot score yet carries &#x60;error&#x60; instead). Pinterest has no time-bounded counts, so &#x60;startTime&#x60;/&#x60;endTime&#x60; answer 400.  TikTok: per-event counts from &#x60;/pixel/event/stats/&#x60; (&#x60;total_count&#x60;, &#x60;browser_event_total_count&#x60;, &#x60;server_event_total_count&#x60;, &#x60;attributed_count&#x60;, &#x60;preview_count&#x60;), bucketed by UTC day. Defaults to the last 7 days; at most 30 days per request. &#x60;aggregation&#x60; is not accepted.  X Ads (platform &#x60;xads&#x60;): X has no event counts per pixel or event (only campaign-level conversion metrics). Each row is one web event tag with its &#x60;status&#x60; (TRACKING, UNVERIFIED, DORMANT), &#x60;lastTrackedTime&#x60; (unix seconds, null if never seen), &#x60;autoCreated&#x60; and, for events the site can fire, &#x60;siteEventId&#x60;. 

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
| **400** | Invalid query parameter, or (Meta) the startTime/endTime window is too large for Meta to answer: narrow it, e.g. into 7-day ranges. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the Meta token lacks ads permissions (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | The platform does not offer this operation (code &#x60;platform_not_supported&#x60;); the message names the reason and the alternative. |  -  |
| **502** | Meta was unreachable or returned an unclassified error (type: platform_error; the raw Meta payload is in platformError). Retryable. |  -  |

## getTrackingTagStatsWithHttpInfo

> ApiResponse<GetTrackingTagStats200Response> getTrackingTagStats getTrackingTagStatsWithHttpInfo(accountId, tagId, adAccountId, aggregation, startTime, endTime)

Get aggregated event stats

Returns event counts / health for the tag, where the platform exposes them. Meta: aggregated counts (&#x60;GET /{pixel_id}/stats&#x60;), rows passed through as-is; their shape depends on the &#x60;aggregation&#x60; requested. Platforms without a stats API answer 501.  OpenAI Ads: the recent-events stream (&#x60;GET /conversions/events&#x60;), the latest (at most 50) events received in the last 15 minutes, one row per event (&#x60;event_type&#x60;, &#x60;api_channel&#x60;, &#x60;event_timestamp_ms&#x60;, &#x60;received_at_ms&#x60;, ...). Both sources appear: &#x60;api_channel&#x60; is &#x60;pixel_sdk&#x60; for the on-site Pixel (including its &#x60;openai::sdk_init&#x60; load event) and &#x60;server_to_server&#x60; for Conversions API events. It is a fixed window: &#x60;startTime&#x60;/&#x60;endTime&#x60; answer 400. Use it to confirm an install fires; attributed totals come from ads analytics. Accounts not enabled for the stream answer 422 &#x60;feature_not_available&#x60;.  LinkedIn (&#x60;linkedinads&#x60;): health rows rather than counts, since LinkedIn exposes no per- event fire counts: one row per site domain the tag has seen (&#x60;kind: domain&#x60;, &#x60;domainName&#x60;, &#x60;lastFiredTime&#x60;, &#x60;creationTime&#x60;, &#x60;blocked&#x60;), capped at the 100 domains that fired most recently (newest first; a tag seen on more domains drops the least recent), and one per conversion rule (&#x60;kind: conversion_rule&#x60;, &#x60;id&#x60;, &#x60;name&#x60;, &#x60;type&#x60;, &#x60;conversionMethod&#x60;, &#x60;status&#x60;, &#x60;lastFiredTime&#x60;). Times are unix seconds; &#x60;startTime&#x60;/&#x60;endTime&#x60; are ignored.  Pinterest (platform &#x60;pinterestads&#x60;): rows typed by &#x60;type&#x60;: one &#x60;tag&#x60; row (&#x60;lastFiredTime&#x60;, &#x60;status&#x60;, &#x60;enhancedMatchStatus&#x60;), &#x60;event&#x60; rows for the conversion events Pinterest has seen on the tag (&#x60;source&#x60; is &#x60;page_visit&#x60; or &#x60;ocpm_eligible&#x60;, the latter meaning the event can be optimized for, with the neutral &#x60;siteEvent&#x60; where one maps), and &#x60;event_quality&#x60; rows with the ad account&#39;s Event Quality Score for tag events over the last &#x60;1d&#x60; and &#x60;14d&#x60; (ad-account level, not per tag; an account Pinterest cannot score yet carries &#x60;error&#x60; instead). Pinterest has no time-bounded counts, so &#x60;startTime&#x60;/&#x60;endTime&#x60; answer 400.  TikTok: per-event counts from &#x60;/pixel/event/stats/&#x60; (&#x60;total_count&#x60;, &#x60;browser_event_total_count&#x60;, &#x60;server_event_total_count&#x60;, &#x60;attributed_count&#x60;, &#x60;preview_count&#x60;), bucketed by UTC day. Defaults to the last 7 days; at most 30 days per request. &#x60;aggregation&#x60; is not accepted.  X Ads (platform &#x60;xads&#x60;): X has no event counts per pixel or event (only campaign-level conversion metrics). Each row is one web event tag with its &#x60;status&#x60; (TRACKING, UNVERIFIED, DORMANT), &#x60;lastTrackedTime&#x60; (unix seconds, null if never seen), &#x60;autoCreated&#x60; and, for events the site can fire, &#x60;siteEventId&#x60;. 

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
| **400** | Invalid query parameter, or (Meta) the startTime/endTime window is too large for Meta to answer: narrow it, e.g. into 7-day ranges. |  -  |
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

Puts the Meta pixel on a connected Shopify store&#39;s storefront and checkout through Zernio&#39;s Shopify web pixel (a Shopify app pixel, no theme edits). The store then sends PageView, ViewContent, AddToCart, Search, InitiateCheckout, AddPaymentInfo and Purchase (with value, currency, content_ids and contents) to the pixel, each with an event id. Purchase uses &#x60;shopify_order_{orderId}&#x60; as its event id, so a Conversions API Purchase you send for the same order with that &#x60;eventId&#x60; is deduplicated by Meta.  Idempotent: a store runs one Zernio web pixel holding one tag per platform, so calling it again updates the install, installing a different tag of the same platform replaces the previous one (reported in &#x60;replacedTagId&#x60;), and other platforms&#39; tags are kept. Events respect the store&#39;s customer privacy settings (marketing consent).  &#x60;accountId&#x60; is the Meta ads account that owns the pixel (&#x60;tagId&#x60;); &#x60;storeAccountId&#x60; is the Shopify account.  OpenAI Ads on Shopify: each event is sent through OpenAI&#39;s documented image tag (&#x60;GET https://bzr.openai.com/v1/sdk/events&#x60;) as &#x60;page_viewed&#x60;, &#x60;contents_viewed&#x60;, &#x60;items_added&#x60;, &#x60;checkout_started&#x60;, &#x60;order_created&#x60;, and custom events &#x60;search&#x60; and &#x60;addpaymentinfo&#x60; (lowercase, so a Conversions API Search/AddPaymentInfo with the same event id deduplicates). Amounts are sent in the currency&#39;s minor unit. The landing page&#39;s &#x60;oppref&#x60; click id is kept in the &#x60;__oppref&#x60; cookie for 30 days and sent with every event. The image tag cannot carry the &#x60;__obref&#x60; browser id (OpenAI rejects the parameter), and the search text is never sent. On WordPress the widget holds the official &#x60;oaiq&#x60; base code and a &#x60;page_viewed&#x60; call.  Stores connected before pixel support must re-approve the Zernio app: the call then answers 409 &#x60;reconnect_required&#x60; with &#x60;details.authUrl&#x60; to send the merchant to (the Shopify account id stays the same). Platforms without an install path return 501.  **WordPress** (&#x60;storeAccountId&#x60; is a connected WordPress.com or self-hosted site): Zernio adds a Custom HTML widget with the Meta pixel base code (fbevents.js, &#x60;init&#x60;, &#x60;PageView&#x60;) to a widget area of the active theme (a footer area when there is one, else the first active area; pass &#x60;sidebarId&#x60; to choose), then reads the widget back to confirm WordPress kept the &#x60;&lt;script&gt;&#x60; tag. The widget carries a Zernio marker, so the call is idempotent per pixel: repeating it updates or moves the same widget, and pixel code the site owner pasted by hand is never touched. Several pixels can run side by side (one widget each). When the site cannot run the pixel, nothing is left behind and the call answers 422 &#x60;tracking_tag_install_blocked&#x60; with &#x60;details.reason&#x60;: - &#x60;insufficient_permissions&#x60;: the connected user lacks &#x60;edit_theme_options&#x60; (needs Administrator). - &#x60;scripts_stripped&#x60;: WordPress removed the script (the user lacks &#x60;unfiltered_html&#x60;, e.g. a multisite admin who is not a Super Admin, or &#x60;DISALLOW_UNFILTERED_HTML&#x60; is set). - &#x60;wordpress_com_plan&#x60;: a WordPress.com plan that strips scripts (plans without plugins). - &#x60;no_widget_areas&#x60;: the theme has no widget areas (block themes such as Twenty Twenty-Five). - &#x60;widgets_api_unavailable&#x60;: no widgets REST API (WordPress older than 5.8, or disabled). The &#x60;error&#x60; message names the manual alternative (Meta&#39;s official WordPress plugin). With &#x60;verifyHomepage&#x60; (default true) the homepage is fetched afterwards and &#x60;homepageCheck&#x60; says whether the pixel is visible; &#x60;not_found&#x60; can be a stale page cache, the widget read-back is authoritative.  **LinkedIn** (&#x60;linkedinads&#x60;): Shopify sends every page view to the Insight Tag, plus each store event that has an enabled event-specific Insight Tag conversion rule of the matching type (view_content &#x3D; VIEW_CONTENT, add_to_cart &#x3D; ADD_TO_CART, search &#x3D; SEARCH, initiate_checkout &#x3D; START_CHECKOUT, add_payment_info &#x3D; ADD_BILLING_INFO, purchase &#x3D; PURCHASE). Each conversion carries the event id; Purchase uses &#x60;shopify_order_{orderId}&#x60;, so a Conversions API event sent to a separate CONVERSIONS_API rule with that &#x60;eventId&#x60; is deduplicated by LinkedIn. Conversions API rules cannot be fired from a page, and no rule is created for you. The &#x60;li_fat_id&#x60; click id is read from the landing URL and kept in a first-party cookie for 30 days. WordPress gets LinkedIn&#39;s base code, which records page views.  **Pinterest (platform &#x60;pinterestads&#x60;)**: Shopify sends &#x60;pagevisit&#x60;, &#x60;viewcontent&#x60;, &#x60;addtocart&#x60;, &#x60;search&#x60;, &#x60;initiatecheckout&#x60;, &#x60;addpaymentinfo&#x60; and &#x60;checkout&#x60; to the tag, each with &#x60;event_id&#x60; (Purchase: &#x60;shopify_order_{orderId}&#x60;, for dedup with the Pinterest Conversions API), value, currency, order quantity and line items, plus the &#x60;epik&#x60; click id kept in the &#x60;_epik&#x60; cookie. WordPress gets Pinterest&#39;s base code (core.js, &#x60;load&#x60;, &#x60;page&#x60;) with a &#x60;pagevisit&#x60; event; the manual fallback is the official Pinterest for WooCommerce plugin (WooCommerce stores). 

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

Puts the Meta pixel on a connected Shopify store&#39;s storefront and checkout through Zernio&#39;s Shopify web pixel (a Shopify app pixel, no theme edits). The store then sends PageView, ViewContent, AddToCart, Search, InitiateCheckout, AddPaymentInfo and Purchase (with value, currency, content_ids and contents) to the pixel, each with an event id. Purchase uses &#x60;shopify_order_{orderId}&#x60; as its event id, so a Conversions API Purchase you send for the same order with that &#x60;eventId&#x60; is deduplicated by Meta.  Idempotent: a store runs one Zernio web pixel holding one tag per platform, so calling it again updates the install, installing a different tag of the same platform replaces the previous one (reported in &#x60;replacedTagId&#x60;), and other platforms&#39; tags are kept. Events respect the store&#39;s customer privacy settings (marketing consent).  &#x60;accountId&#x60; is the Meta ads account that owns the pixel (&#x60;tagId&#x60;); &#x60;storeAccountId&#x60; is the Shopify account.  OpenAI Ads on Shopify: each event is sent through OpenAI&#39;s documented image tag (&#x60;GET https://bzr.openai.com/v1/sdk/events&#x60;) as &#x60;page_viewed&#x60;, &#x60;contents_viewed&#x60;, &#x60;items_added&#x60;, &#x60;checkout_started&#x60;, &#x60;order_created&#x60;, and custom events &#x60;search&#x60; and &#x60;addpaymentinfo&#x60; (lowercase, so a Conversions API Search/AddPaymentInfo with the same event id deduplicates). Amounts are sent in the currency&#39;s minor unit. The landing page&#39;s &#x60;oppref&#x60; click id is kept in the &#x60;__oppref&#x60; cookie for 30 days and sent with every event. The image tag cannot carry the &#x60;__obref&#x60; browser id (OpenAI rejects the parameter), and the search text is never sent. On WordPress the widget holds the official &#x60;oaiq&#x60; base code and a &#x60;page_viewed&#x60; call.  Stores connected before pixel support must re-approve the Zernio app: the call then answers 409 &#x60;reconnect_required&#x60; with &#x60;details.authUrl&#x60; to send the merchant to (the Shopify account id stays the same). Platforms without an install path return 501.  **WordPress** (&#x60;storeAccountId&#x60; is a connected WordPress.com or self-hosted site): Zernio adds a Custom HTML widget with the Meta pixel base code (fbevents.js, &#x60;init&#x60;, &#x60;PageView&#x60;) to a widget area of the active theme (a footer area when there is one, else the first active area; pass &#x60;sidebarId&#x60; to choose), then reads the widget back to confirm WordPress kept the &#x60;&lt;script&gt;&#x60; tag. The widget carries a Zernio marker, so the call is idempotent per pixel: repeating it updates or moves the same widget, and pixel code the site owner pasted by hand is never touched. Several pixels can run side by side (one widget each). When the site cannot run the pixel, nothing is left behind and the call answers 422 &#x60;tracking_tag_install_blocked&#x60; with &#x60;details.reason&#x60;: - &#x60;insufficient_permissions&#x60;: the connected user lacks &#x60;edit_theme_options&#x60; (needs Administrator). - &#x60;scripts_stripped&#x60;: WordPress removed the script (the user lacks &#x60;unfiltered_html&#x60;, e.g. a multisite admin who is not a Super Admin, or &#x60;DISALLOW_UNFILTERED_HTML&#x60; is set). - &#x60;wordpress_com_plan&#x60;: a WordPress.com plan that strips scripts (plans without plugins). - &#x60;no_widget_areas&#x60;: the theme has no widget areas (block themes such as Twenty Twenty-Five). - &#x60;widgets_api_unavailable&#x60;: no widgets REST API (WordPress older than 5.8, or disabled). The &#x60;error&#x60; message names the manual alternative (Meta&#39;s official WordPress plugin). With &#x60;verifyHomepage&#x60; (default true) the homepage is fetched afterwards and &#x60;homepageCheck&#x60; says whether the pixel is visible; &#x60;not_found&#x60; can be a stale page cache, the widget read-back is authoritative.  **LinkedIn** (&#x60;linkedinads&#x60;): Shopify sends every page view to the Insight Tag, plus each store event that has an enabled event-specific Insight Tag conversion rule of the matching type (view_content &#x3D; VIEW_CONTENT, add_to_cart &#x3D; ADD_TO_CART, search &#x3D; SEARCH, initiate_checkout &#x3D; START_CHECKOUT, add_payment_info &#x3D; ADD_BILLING_INFO, purchase &#x3D; PURCHASE). Each conversion carries the event id; Purchase uses &#x60;shopify_order_{orderId}&#x60;, so a Conversions API event sent to a separate CONVERSIONS_API rule with that &#x60;eventId&#x60; is deduplicated by LinkedIn. Conversions API rules cannot be fired from a page, and no rule is created for you. The &#x60;li_fat_id&#x60; click id is read from the landing URL and kept in a first-party cookie for 30 days. WordPress gets LinkedIn&#39;s base code, which records page views.  **Pinterest (platform &#x60;pinterestads&#x60;)**: Shopify sends &#x60;pagevisit&#x60;, &#x60;viewcontent&#x60;, &#x60;addtocart&#x60;, &#x60;search&#x60;, &#x60;initiatecheckout&#x60;, &#x60;addpaymentinfo&#x60; and &#x60;checkout&#x60; to the tag, each with &#x60;event_id&#x60; (Purchase: &#x60;shopify_order_{orderId}&#x60;, for dedup with the Pinterest Conversions API), value, currency, order quantity and line items, plus the &#x60;epik&#x60; click id kept in the &#x60;_epik&#x60; cookie. WordPress gets Pinterest&#39;s base code (core.js, &#x60;load&#x60;, &#x60;page&#x60;) with a &#x60;pagevisit&#x60; event; the manual fallback is the official Pinterest for WooCommerce plugin (WooCommerce stores). 

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

The tag&#39;s conversion events, on platforms where each conversion is its own object: Google conversion actions, LinkedIn conversion rules, X web event tags, OpenAI event settings, TikTok pixel events, Meta custom conversions, Pinterest advertiser defined events.  OpenAI Ads: the account&#39;s conversion event settings whose source is this pixel. &#x60;siteEventId&#x60; is the event name the site sends (a standard event such as &#x60;order_created&#x60;, or the lowercase custom event name); &#x60;clickWindowDays&#x60; is the click attribution window and &#x60;viewWindowDays&#x60; the view-through window (0 &#x3D; off).  LinkedIn (&#x60;linkedinads&#x60;): the conversion rules of the ad account (&#x60;adAccountId&#x60;, default the account that created the tag), including Conversions API and URL-match rules. &#x60;siteEventId&#x60; (the rule id a page fires) is set only on event-specific Insight Tag rules; &#x60;defaultValue&#x60;/&#x60;currency&#x60; come from the rule value, &#x60;clickWindowDays&#x60;/&#x60;viewWindowDays&#x60; from its post-click and view-through windows.  Meta: the pixel&#39;s custom conversions. Meta keeps them per AD ACCOUNT (a pixel has no custom conversions edge), so the list reads &#x60;adAccountId&#x60; (default: the pixel&#39;s owner ad account) and keeps the conversions whose pixel is this one. Archived conversions are included with &#x60;status: archived&#x60;. &#x60;urlContains&#x60; and &#x60;siteEvent&#x60; are parsed from Meta&#39;s rule.  Google Ads (&#x60;googleads&#x60;): the enabled WEBPAGE conversion actions of the account; &#x60;siteEventId&#x60; is the conversion label (the part after &#x60;AW-.../&#x60; in &#x60;send_to&#x60;), and value settings, lookback windows, &#x60;primary&#x60; and &#x60;countingType&#x60; are returned. Archived (removed) actions are listed with status &#x60;REMOVED&#x60;; imported (GA4, upload, app) actions are not events of the tag.  Pinterest (platform &#x60;pinterestads&#x60;): the ad account&#39;s advertiser defined events, custom event names mapped to a standard type (&#x60;type&#x60;, e.g. &#x60;SIGNUP&#x60;). They belong to the ad account, so every tag on it shares them. &#x60;id&#x60;, &#x60;name&#x60; and &#x60;siteEventId&#x60; are all the event name, which the site sends as &#x60;pintrk(&#39;track&#39;, &#39;&lt;name&gt;&#39;)&#x60; or the Conversions API sends as &#x60;event_name&#x60;. Standard events (&#x60;pagevisit&#x60;, &#x60;checkout&#x60;...) need no object and are not listed.  TikTok: the pixel&#39;s events from &#x60;/pixel/list/&#x60;. TikTok refreshes this list every 2 to 4 hours, so a just-created event can be missing. &#x60;siteEventId&#x60; is the &#x60;ttq.track()&#x60; name the site fires.  X Ads (platform &#x60;xads&#x60;): the ad account&#39;s web event tags the site can fire. Events X auto-creates with the pixel (site visits, landing page views, one per standard type) share the pixel id, cannot be fired one by one and are left out; they still appear in stats. 

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

The tag&#39;s conversion events, on platforms where each conversion is its own object: Google conversion actions, LinkedIn conversion rules, X web event tags, OpenAI event settings, TikTok pixel events, Meta custom conversions, Pinterest advertiser defined events.  OpenAI Ads: the account&#39;s conversion event settings whose source is this pixel. &#x60;siteEventId&#x60; is the event name the site sends (a standard event such as &#x60;order_created&#x60;, or the lowercase custom event name); &#x60;clickWindowDays&#x60; is the click attribution window and &#x60;viewWindowDays&#x60; the view-through window (0 &#x3D; off).  LinkedIn (&#x60;linkedinads&#x60;): the conversion rules of the ad account (&#x60;adAccountId&#x60;, default the account that created the tag), including Conversions API and URL-match rules. &#x60;siteEventId&#x60; (the rule id a page fires) is set only on event-specific Insight Tag rules; &#x60;defaultValue&#x60;/&#x60;currency&#x60; come from the rule value, &#x60;clickWindowDays&#x60;/&#x60;viewWindowDays&#x60; from its post-click and view-through windows.  Meta: the pixel&#39;s custom conversions. Meta keeps them per AD ACCOUNT (a pixel has no custom conversions edge), so the list reads &#x60;adAccountId&#x60; (default: the pixel&#39;s owner ad account) and keeps the conversions whose pixel is this one. Archived conversions are included with &#x60;status: archived&#x60;. &#x60;urlContains&#x60; and &#x60;siteEvent&#x60; are parsed from Meta&#39;s rule.  Google Ads (&#x60;googleads&#x60;): the enabled WEBPAGE conversion actions of the account; &#x60;siteEventId&#x60; is the conversion label (the part after &#x60;AW-.../&#x60; in &#x60;send_to&#x60;), and value settings, lookback windows, &#x60;primary&#x60; and &#x60;countingType&#x60; are returned. Archived (removed) actions are listed with status &#x60;REMOVED&#x60;; imported (GA4, upload, app) actions are not events of the tag.  Pinterest (platform &#x60;pinterestads&#x60;): the ad account&#39;s advertiser defined events, custom event names mapped to a standard type (&#x60;type&#x60;, e.g. &#x60;SIGNUP&#x60;). They belong to the ad account, so every tag on it shares them. &#x60;id&#x60;, &#x60;name&#x60; and &#x60;siteEventId&#x60; are all the event name, which the site sends as &#x60;pintrk(&#39;track&#39;, &#39;&lt;name&gt;&#39;)&#x60; or the Conversions API sends as &#x60;event_name&#x60;. Standard events (&#x60;pagevisit&#x60;, &#x60;checkout&#x60;...) need no object and are not listed.  TikTok: the pixel&#39;s events from &#x60;/pixel/list/&#x60;. TikTok refreshes this list every 2 to 4 hours, so a just-created event can be missing. &#x60;siteEventId&#x60; is the &#x60;ttq.track()&#x60; name the site fires.  X Ads (platform &#x60;xads&#x60;): the ad account&#39;s web event tags the site can fire. Events X auto-creates with the pixel (site visits, landing page views, one per standard type) share the pixel id, cannot be fired one by one and are left out; they still appear in stats. 

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


## listTrackingTagPartners

> ListTrackingTagPartners200Response listTrackingTagPartners(accountId, tagId)

List partner businesses of a tag

Other businesses the tag is shared with. Read-only. Platforms without partner sharing answer 501.  Meta: the pixel&#39;s shared agencies. Sharing a pixel with a new partner is not available: &#x60;/{pixel}/agencies&#x60; answers \&quot;(#3) Application does not have the capability to make this API call\&quot; for our app. 

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
        try {
            ListTrackingTagPartners200Response result = apiInstance.listTrackingTagPartners(accountId, tagId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagPartners");
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

### Return type

[**ListTrackingTagPartners200Response**](ListTrackingTagPartners200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Partners listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no partner sharing (code &#x60;platform_not_supported&#x60;). |  -  |

## listTrackingTagPartnersWithHttpInfo

> ApiResponse<ListTrackingTagPartners200Response> listTrackingTagPartners listTrackingTagPartnersWithHttpInfo(accountId, tagId)

List partner businesses of a tag

Other businesses the tag is shared with. Read-only. Platforms without partner sharing answer 501.  Meta: the pixel&#39;s shared agencies. Sharing a pixel with a new partner is not available: &#x60;/{pixel}/agencies&#x60; answers \&quot;(#3) Application does not have the capability to make this API call\&quot; for our app. 

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
        try {
            ApiResponse<ListTrackingTagPartners200Response> response = apiInstance.listTrackingTagPartnersWithHttpInfo(accountId, tagId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagPartners");
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

### Return type

ApiResponse<[**ListTrackingTagPartners200Response**](ListTrackingTagPartners200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Partners listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no partner sharing (code &#x60;platform_not_supported&#x60;). |  -  |


## listTrackingTagSharedAccounts

> ListTrackingTagSharedAccounts200Response listTrackingTagSharedAccounts(accountId, tagId)

List accounts it is shared with

Meta (&#x60;metaads&#x60;) and LinkedIn (&#x60;linkedinads&#x60;); other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): the ad accounts this connection can see that hold access to the Insight Tag; the role (&#x60;FULL&#x60; or &#x60;USE_ONLY&#x60;) is appended to &#x60;name&#x60;. LinkedIn exposes permissions per ad account only, so accounts the connection cannot see are not listed.  TikTok (&#x60;tiktokads&#x60;): the advertisers linked to the pixel in its Business Center (&#x60;/bc/pixel/link/get/&#x60;); a pixel outside Business Center answers 400. 

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

Meta (&#x60;metaads&#x60;) and LinkedIn (&#x60;linkedinads&#x60;); other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): the ad accounts this connection can see that hold access to the Insight Tag; the role (&#x60;FULL&#x60; or &#x60;USE_ONLY&#x60;) is appended to &#x60;name&#x60;. LinkedIn exposes permissions per ad account only, so accounts the connection cannot see are not listed.  TikTok (&#x60;tiktokads&#x60;): the advertisers linked to the pixel in its Business Center (&#x60;/bc/pixel/link/get/&#x60;); a pixel outside Business Center answers 400. 

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


## listTrackingTagUsers

> ListTrackingTagUsers200Response listTrackingTagUsers(accountId, tagId)

List tag users

People and system users of the owning business with access to the tag. Platforms without tag user assignment answer 501.  Meta: the pixel&#39;s assigned users in its owning Business Manager. A pixel on a personal ad account has no business and returns an empty list. Needs the &#x60;business_management&#x60; permission on the connecting Meta user (an admin of the owning business); without it the call answers 403 asking to reconnect. 

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
        try {
            ListTrackingTagUsers200Response result = apiInstance.listTrackingTagUsers(accountId, tagId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagUsers");
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

### Return type

[**ListTrackingTagUsers200Response**](ListTrackingTagUsers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag users listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no tag user assignment (code &#x60;platform_not_supported&#x60;). |  -  |

## listTrackingTagUsersWithHttpInfo

> ApiResponse<ListTrackingTagUsers200Response> listTrackingTagUsers listTrackingTagUsersWithHttpInfo(accountId, tagId)

List tag users

People and system users of the owning business with access to the tag. Platforms without tag user assignment answer 501.  Meta: the pixel&#39;s assigned users in its owning Business Manager. A pixel on a personal ad account has no business and returns an empty list. Needs the &#x60;business_management&#x60; permission on the connecting Meta user (an admin of the owning business); without it the call answers 403 asking to reconnect. 

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
        try {
            ApiResponse<ListTrackingTagUsers200Response> response = apiInstance.listTrackingTagUsersWithHttpInfo(accountId, tagId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#listTrackingTagUsers");
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

### Return type

ApiResponse<[**ListTrackingTagUsers200Response**](ListTrackingTagUsers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag users listed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform has no tag user assignment (code &#x60;platform_not_supported&#x60;). |  -  |


## listTrackingTags

> ListTrackingTags200Response listTrackingTags(accountId, adAccountId)

List tracking tags

Returns the tracking tags (Meta Pixels, or OpenAI Ads pixels) the connected ads account can see. Pass &#x60;?adAccountId&#x3D;act_...&#x60; (Meta only) to scope the list to a single ad account; omit it to list every pixel reachable by the token (the name is then suffixed with the ad account it was discovered on, for disambiguation). The list view omits &#x60;code&#x60;. Call &#x60;getTrackingTag&#x60; for the install snippet and full detail.  Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501. The &#x60;accountId&#x60; must be the ads SocialAccount created by the Ads add-on connect flow (Meta) or the OpenAI Ads connect flow, not a Facebook/Instagram posting account. Get your Meta &#x60;act_...&#x60; ids from &#x60;GET /v1/ads/accounts&#x60;; &#x60;adAccountId&#x60; is ignored for OpenAI Ads (one API key maps to exactly one ad account).  LinkedIn (&#x60;linkedinads&#x60;): lists the Insight Tag of each ad account (LinkedIn allows one per ad account; a tag shared with several accounts appears once). &#x60;adAccountId&#x60; is the numeric ad account id or &#x60;urn:li:sponsoredAccount:{id}&#x60;; omit it to scan every active ad account the connection can see. The tag &#x60;id&#x60; IS the partner id the site embeds, so &#x60;siteTagId&#x60; equals &#x60;id&#x60;. LinkedIn tags have no name; it is shown as &#x60;Insight Tag {id}&#x60;.  Pinterest (platform &#x60;pinterestads&#x60;): lists Pinterest tags (conversion tags). &#x60;adAccountId&#x60; is the numeric Pinterest ad account id (no prefix); omit it to walk every ad account the connection can read (an ad account the user has no Business Access role on is skipped). &#x60;id&#x60; equals &#x60;siteTagId&#x60;, the id the site loads with &#x60;pintrk(&#39;load&#39;, id)&#x60;.  TikTok (platform &#x60;tiktokads&#x60;): TikTok Pixels across the connection&#39;s advertisers, or one advertiser with &#x60;?adAccountId&#x3D;&lt;numeric advertiser_id&gt;&#x60;. &#x60;id&#x60; is the numeric &#x60;pixel_id&#x60;, &#x60;siteTagId&#x60; the alphanumeric &#x60;pixel_code&#x60; from Events Manager. Connections authorized before the Pixel Management permission (about 2026-05-28) answer 403 until reconnected.  X Ads (platform &#x60;xads&#x60;): one X Pixel per X ad account, so &#x60;TrackingTag.id&#x60; is the ad account id (base36, e.g. &#x60;18ce54d4x5t&#x60;) and &#x60;siteTagId&#x60; is the pixel id the site embeds. Ad accounts without a pixel are left out. &#x60;adAccountId&#x60; scopes the list to one ad account. 

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

Returns the tracking tags (Meta Pixels, or OpenAI Ads pixels) the connected ads account can see. Pass &#x60;?adAccountId&#x3D;act_...&#x60; (Meta only) to scope the list to a single ad account; omit it to list every pixel reachable by the token (the name is then suffixed with the ad account it was discovered on, for disambiguation). The list view omits &#x60;code&#x60;. Call &#x60;getTrackingTag&#x60; for the install snippet and full detail.  Meta (platform &#x60;metaads&#x60;) and OpenAI Ads (platform &#x60;openaiads&#x60;); other platforms return 501. The &#x60;accountId&#x60; must be the ads SocialAccount created by the Ads add-on connect flow (Meta) or the OpenAI Ads connect flow, not a Facebook/Instagram posting account. Get your Meta &#x60;act_...&#x60; ids from &#x60;GET /v1/ads/accounts&#x60;; &#x60;adAccountId&#x60; is ignored for OpenAI Ads (one API key maps to exactly one ad account).  LinkedIn (&#x60;linkedinads&#x60;): lists the Insight Tag of each ad account (LinkedIn allows one per ad account; a tag shared with several accounts appears once). &#x60;adAccountId&#x60; is the numeric ad account id or &#x60;urn:li:sponsoredAccount:{id}&#x60;; omit it to scan every active ad account the connection can see. The tag &#x60;id&#x60; IS the partner id the site embeds, so &#x60;siteTagId&#x60; equals &#x60;id&#x60;. LinkedIn tags have no name; it is shown as &#x60;Insight Tag {id}&#x60;.  Pinterest (platform &#x60;pinterestads&#x60;): lists Pinterest tags (conversion tags). &#x60;adAccountId&#x60; is the numeric Pinterest ad account id (no prefix); omit it to walk every ad account the connection can read (an ad account the user has no Business Access role on is skipped). &#x60;id&#x60; equals &#x60;siteTagId&#x60;, the id the site loads with &#x60;pintrk(&#39;load&#39;, id)&#x60;.  TikTok (platform &#x60;tiktokads&#x60;): TikTok Pixels across the connection&#39;s advertisers, or one advertiser with &#x60;?adAccountId&#x3D;&lt;numeric advertiser_id&gt;&#x60;. &#x60;id&#x60; is the numeric &#x60;pixel_id&#x60;, &#x60;siteTagId&#x60; the alphanumeric &#x60;pixel_code&#x60; from Events Manager. Connections authorized before the Pixel Management permission (about 2026-05-28) answer 403 until reconnected.  X Ads (platform &#x60;xads&#x60;): one X Pixel per X ad account, so &#x60;TrackingTag.id&#x60; is the ad account id (base36, e.g. &#x60;18ce54d4x5t&#x60;) and &#x60;siteTagId&#x60; is the pixel id the site embeds. Ad accounts without a pixel are left out. &#x60;adAccountId&#x60; scopes the list to one ad account. 

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

&#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. Meta and LinkedIn; other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): revokes the ad account&#39;s access. Zernio answers 400 instead of revoking the last ad account that holds the tag: LinkedIn accepts that call and the tag is orphaned (verified live).  TikTok: unlinks through Business Center (&#x60;/bc/pixel/link/update/&#x60; with &#x60;UNLINK&#x60;). 

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

&#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. Meta and LinkedIn; other platforms return 501.  LinkedIn (&#x60;linkedinads&#x60;): revokes the ad account&#39;s access. Zernio answers 400 instead of revoking the last ad account that holds the tag: LinkedIn accepts that call and the tag is orphaned (verified live).  TikTok: unlinks through Business Center (&#x60;/bc/pixel/link/update/&#x60; with &#x60;UNLINK&#x60;). 

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


## removeTrackingTagUser

> RemoveTrackingTagUser200Response removeTrackingTagUser(accountId, tagId, userId)

Remove a user from a tag

Removes a user&#39;s access to the tag, on platforms whose API allows it.  Meta answers 501: the Business SDK has no delete on the pixel&#39;s assigned users, &#x60;DELETE /{pixel}/assigned_users&#x60; answers \&quot;Unsupported delete request\&quot; (code 100, subcode 33) and re-assigning with no tasks is refused. Remove the user in Business Settings. 

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
        String userId = "userId_example"; // String | User id (`TrackingTagUser.id`).
        try {
            RemoveTrackingTagUser200Response result = apiInstance.removeTrackingTagUser(accountId, tagId, userId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagUser");
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
| **userId** | **String**| User id (&#x60;TrackingTagUser.id&#x60;). | |

### Return type

[**RemoveTrackingTagUser200Response**](RemoveTrackingTagUser200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot remove tag users through its API (code &#x60;platform_not_supported&#x60;); the message says where to do it. |  -  |

## removeTrackingTagUserWithHttpInfo

> ApiResponse<RemoveTrackingTagUser200Response> removeTrackingTagUser removeTrackingTagUserWithHttpInfo(accountId, tagId, userId)

Remove a user from a tag

Removes a user&#39;s access to the tag, on platforms whose API allows it.  Meta answers 501: the Business SDK has no delete on the pixel&#39;s assigned users, &#x60;DELETE /{pixel}/assigned_users&#x60; answers \&quot;Unsupported delete request\&quot; (code 100, subcode 33) and re-assigning with no tasks is refused. Remove the user in Business Settings. 

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
        String userId = "userId_example"; // String | User id (`TrackingTagUser.id`).
        try {
            ApiResponse<RemoveTrackingTagUser200Response> response = apiInstance.removeTrackingTagUserWithHttpInfo(accountId, tagId, userId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TrackingTagsApi#removeTrackingTagUser");
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
| **userId** | **String**| User id (&#x60;TrackingTagUser.id&#x60;). | |

### Return type

ApiResponse<[**RemoveTrackingTagUser200Response**](RemoveTrackingTagUser200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the platform token lacks the permission (reconnect required). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | The platform cannot remove tag users through its API (code &#x60;platform_not_supported&#x60;); the message says where to do it. |  -  |


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

Partial-update a pixel. Whitelisted fields: &#x60;name&#x60; (rename), &#x60;enableAutomaticMatching&#x60;, &#x60;automaticMatchingFields&#x60;, &#x60;firstPartyCookieStatus&#x60;, &#x60;dataUseSetting&#x60;. At least one is required. Returns the re-fetched canonical tag. Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  OpenAI Ads answers 501: its API has no pixel update or delete route (&#x60;POST&#x60;/&#x60;PATCH&#x60;/&#x60;PUT&#x60;/&#x60;DELETE /v1/conversions/pixels/{id}&#x60; answer 405 \&quot;Invalid method\&quot;); rename a pixel in OpenAI Ads Manager.  Google Ads (&#x60;googleads&#x60;): the only writable tag setting is &#x60;autoTagging&#x60; (the account&#39;s gclid auto-tagging, without which the tag cannot attribute conversions to ad clicks). Google rejects every write to &#x60;conversion_tracking_setting&#x60; for our developer token (&#x60;SERVICE_ACCESS_DENIED&#x60;), so the tag id and cross-account ownership stay managed in the Google Ads UI.  There is no DELETE: Meta has no API to delete a pixel. To stop using one, unshare it from your ad accounts (&#x60;DELETE .../tracking-tags/{tagId}/shared-accounts&#x60;) or disable it in Events Manager.  LinkedIn (&#x60;linkedinads&#x60;): only &#x60;firstPartyCookieStatus&#x60; (&#x60;first_party_cookie_enabled&#x60; or &#x60;first_party_cookie_disabled&#x60;), which sets the tag&#39;s first-party tracking. It applies to every ad account using the tag. &#x60;empty&#x60; answers 400: LinkedIn has no unset state.  Pinterest (platform &#x60;pinterestads&#x60;): 501. Pinterest API v5 has no endpoint to edit a tag: its spec lists only POST/GET on &#x60;conversion_tags&#x60; and GET on &#x60;conversion_tags/{id}&#x60;, and PATCH or PUT on &#x60;conversion_tags/{id}&#x60; answer 405 \&quot;Method not allowed\&quot;. Set enhanced match at creation (&#x60;automaticMatchingFields&#x60;) or change it and the name in Pinterest Ads Manager.  TikTok: &#x60;name&#x60;, &#x60;enableAutomaticMatching&#x60; + &#x60;automaticMatchingFields&#x60; (folded onto TikTok&#39;s five switches: em, ph, fn/ln, ct/st/zp/country, external_id; ge and db answer 400), and first-party cookies via &#x60;enableFirstPartyCookies&#x60; or &#x60;firstPartyCookieStatus&#x60; (enabled or disabled). TikTok has no pixel delete: the endpoint is absent from its API and &#x60;POST /pixel/delete/&#x60; answers 404.  Pinterest (platform &#x60;pinterestads&#x60;): 501. Pinterest API v5 only creates, lists and reads tags (no update endpoint); rename a tag or change its enhanced match settings in Pinterest Ads Manager.  X Ads (platform &#x60;xads&#x60;): only &#x60;firstPartyCookieStatus&#x60; (&#x60;first_party_cookie_enabled&#x60; or &#x60;first_party_cookie_disabled&#x60;), which sets the pixel&#39;s first-party cookie setting. X has no API to rename or delete a pixel. 

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

Partial-update a pixel. Whitelisted fields: &#x60;name&#x60; (rename), &#x60;enableAutomaticMatching&#x60;, &#x60;automaticMatchingFields&#x60;, &#x60;firstPartyCookieStatus&#x60;, &#x60;dataUseSetting&#x60;. At least one is required. Returns the re-fetched canonical tag. Meta only (platform &#x60;metaads&#x60;); other platforms return 501.  OpenAI Ads answers 501: its API has no pixel update or delete route (&#x60;POST&#x60;/&#x60;PATCH&#x60;/&#x60;PUT&#x60;/&#x60;DELETE /v1/conversions/pixels/{id}&#x60; answer 405 \&quot;Invalid method\&quot;); rename a pixel in OpenAI Ads Manager.  Google Ads (&#x60;googleads&#x60;): the only writable tag setting is &#x60;autoTagging&#x60; (the account&#39;s gclid auto-tagging, without which the tag cannot attribute conversions to ad clicks). Google rejects every write to &#x60;conversion_tracking_setting&#x60; for our developer token (&#x60;SERVICE_ACCESS_DENIED&#x60;), so the tag id and cross-account ownership stay managed in the Google Ads UI.  There is no DELETE: Meta has no API to delete a pixel. To stop using one, unshare it from your ad accounts (&#x60;DELETE .../tracking-tags/{tagId}/shared-accounts&#x60;) or disable it in Events Manager.  LinkedIn (&#x60;linkedinads&#x60;): only &#x60;firstPartyCookieStatus&#x60; (&#x60;first_party_cookie_enabled&#x60; or &#x60;first_party_cookie_disabled&#x60;), which sets the tag&#39;s first-party tracking. It applies to every ad account using the tag. &#x60;empty&#x60; answers 400: LinkedIn has no unset state.  Pinterest (platform &#x60;pinterestads&#x60;): 501. Pinterest API v5 has no endpoint to edit a tag: its spec lists only POST/GET on &#x60;conversion_tags&#x60; and GET on &#x60;conversion_tags/{id}&#x60;, and PATCH or PUT on &#x60;conversion_tags/{id}&#x60; answer 405 \&quot;Method not allowed\&quot;. Set enhanced match at creation (&#x60;automaticMatchingFields&#x60;) or change it and the name in Pinterest Ads Manager.  TikTok: &#x60;name&#x60;, &#x60;enableAutomaticMatching&#x60; + &#x60;automaticMatchingFields&#x60; (folded onto TikTok&#39;s five switches: em, ph, fn/ln, ct/st/zp/country, external_id; ge and db answer 400), and first-party cookies via &#x60;enableFirstPartyCookies&#x60; or &#x60;firstPartyCookieStatus&#x60; (enabled or disabled). TikTok has no pixel delete: the endpoint is absent from its API and &#x60;POST /pixel/delete/&#x60; answers 404.  Pinterest (platform &#x60;pinterestads&#x60;): 501. Pinterest API v5 only creates, lists and reads tags (no update endpoint); rename a tag or change its enhanced match settings in Pinterest Ads Manager.  X Ads (platform &#x60;xads&#x60;): only &#x60;firstPartyCookieStatus&#x60; (&#x60;first_party_cookie_enabled&#x60; or &#x60;first_party_cookie_disabled&#x60;), which sets the pixel&#39;s first-party cookie setting. X has no API to rename or delete a pixel. 

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

Partial update; at least one field. A field the platform does not store answers 400.  OpenAI Ads answers 501: OpenAI documents only list and create for event settings, and &#x60;POST&#x60;/&#x60;PATCH&#x60;/&#x60;PUT /v1/conversions/event_settings/{id}&#x60; answer 404 \&quot;Invalid URL\&quot;. Create a new event instead.  LinkedIn (&#x60;linkedinads&#x60;): partial update of the conversion rule; same fields as create. Pass &#x60;adAccountId&#x60; when the rule lives in another ad account than the one that created the tag.  Meta: only &#x60;name&#x60; and &#x60;defaultValue&#x60; can change (Meta&#39;s custom conversion update takes nothing else); &#x60;type&#x60;, &#x60;siteEvent&#x60; and &#x60;urlContains&#x60; answer 400, create a new event instead.  Google Ads (&#x60;googleads&#x60;): same fields as create, on the account&#39;s WEBPAGE actions (others answer 404). &#x60;enabled: false&#x60; archives the action (same as DELETE) and &#x60;enabled: true&#x60; restores an archived one.  Pinterest (platform &#x60;pinterestads&#x60;): remaps the event to another &#x60;type&#x60; or &#x60;siteEvent&#x60;. Pinterest identifies the event by its name, so &#x60;name&#x60; cannot change (400): create the new name and delete the old one.  TikTok: &#x60;name&#x60;, &#x60;defaultValue&#x60; and &#x60;currency&#x60; (USD, JPY or INR); the type cannot change (delete and recreate).  X Ads (platform &#x60;xads&#x60;): the same fields as create. Events X auto-created with the pixel cannot be changed (400). 

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

Partial update; at least one field. A field the platform does not store answers 400.  OpenAI Ads answers 501: OpenAI documents only list and create for event settings, and &#x60;POST&#x60;/&#x60;PATCH&#x60;/&#x60;PUT /v1/conversions/event_settings/{id}&#x60; answer 404 \&quot;Invalid URL\&quot;. Create a new event instead.  LinkedIn (&#x60;linkedinads&#x60;): partial update of the conversion rule; same fields as create. Pass &#x60;adAccountId&#x60; when the rule lives in another ad account than the one that created the tag.  Meta: only &#x60;name&#x60; and &#x60;defaultValue&#x60; can change (Meta&#39;s custom conversion update takes nothing else); &#x60;type&#x60;, &#x60;siteEvent&#x60; and &#x60;urlContains&#x60; answer 400, create a new event instead.  Google Ads (&#x60;googleads&#x60;): same fields as create, on the account&#39;s WEBPAGE actions (others answer 404). &#x60;enabled: false&#x60; archives the action (same as DELETE) and &#x60;enabled: true&#x60; restores an archived one.  Pinterest (platform &#x60;pinterestads&#x60;): remaps the event to another &#x60;type&#x60; or &#x60;siteEvent&#x60;. Pinterest identifies the event by its name, so &#x60;name&#x60; cannot change (400): create the new name and delete the old one.  TikTok: &#x60;name&#x60;, &#x60;defaultValue&#x60; and &#x60;currency&#x60; (USD, JPY or INR); the type cannot change (delete and recreate).  X Ads (platform &#x60;xads&#x60;): the same fields as create. Events X auto-created with the pixel cannot be changed (400). 

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

