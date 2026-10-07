# AccountsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAccount**](AccountsApi.md#deleteAccount) | **DELETE** /v1/accounts/{accountId} | Disconnect account |
| [**deleteAccountWithHttpInfo**](AccountsApi.md#deleteAccountWithHttpInfo) | **DELETE** /v1/accounts/{accountId} | Disconnect account |
| [**getAccountHealth**](AccountsApi.md#getAccountHealth) | **GET** /v1/accounts/{accountId}/health | Check account health |
| [**getAccountHealthWithHttpInfo**](AccountsApi.md#getAccountHealthWithHttpInfo) | **GET** /v1/accounts/{accountId}/health | Check account health |
| [**getAccountPosts**](AccountsApi.md#getAccountPosts) | **GET** /v1/accounts/{accountId}/posts | List posts published on the platform |
| [**getAccountPostsWithHttpInfo**](AccountsApi.md#getAccountPostsWithHttpInfo) | **GET** /v1/accounts/{accountId}/posts | List posts published on the platform |
| [**getAllAccountsHealth**](AccountsApi.md#getAllAccountsHealth) | **GET** /v1/accounts/health | Check accounts health |
| [**getAllAccountsHealthWithHttpInfo**](AccountsApi.md#getAllAccountsHealthWithHttpInfo) | **GET** /v1/accounts/health | Check accounts health |
| [**getBlueskySettings**](AccountsApi.md#getBlueskySettings) | **GET** /v1/accounts/{accountId}/bluesky-settings | Get Bluesky account settings |
| [**getBlueskySettingsWithHttpInfo**](AccountsApi.md#getBlueskySettingsWithHttpInfo) | **GET** /v1/accounts/{accountId}/bluesky-settings | Get Bluesky account settings |
| [**getFollowerStats**](AccountsApi.md#getFollowerStats) | **GET** /v1/accounts/follower-stats | Get follower stats |
| [**getFollowerStatsWithHttpInfo**](AccountsApi.md#getFollowerStatsWithHttpInfo) | **GET** /v1/accounts/follower-stats | Get follower stats |
| [**getInstagramFollowStatus**](AccountsApi.md#getInstagramFollowStatus) | **GET** /v1/accounts/{accountId}/follow-status/{userId} | Check whether an Instagram user follows the account |
| [**getInstagramFollowStatusWithHttpInfo**](AccountsApi.md#getInstagramFollowStatusWithHttpInfo) | **GET** /v1/accounts/{accountId}/follow-status/{userId} | Check whether an Instagram user follows the account |
| [**getSlackSettings**](AccountsApi.md#getSlackSettings) | **GET** /v1/accounts/{accountId}/slack-settings | Get Slack account settings |
| [**getSlackSettingsWithHttpInfo**](AccountsApi.md#getSlackSettingsWithHttpInfo) | **GET** /v1/accounts/{accountId}/slack-settings | Get Slack account settings |
| [**getTikTokCreatorInfo**](AccountsApi.md#getTikTokCreatorInfo) | **GET** /v1/accounts/{accountId}/tiktok/creator-info | Get TikTok creator info |
| [**getTikTokCreatorInfoWithHttpInfo**](AccountsApi.md#getTikTokCreatorInfoWithHttpInfo) | **GET** /v1/accounts/{accountId}/tiktok/creator-info | Get TikTok creator info |
| [**grantBusinessPartner**](AccountsApi.md#grantBusinessPartner) | **POST** /v1/accounts/{accountId}/business-partners | Share the Page with a partner business |
| [**grantBusinessPartnerWithHttpInfo**](AccountsApi.md#grantBusinessPartnerWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-partners | Share the Page with a partner business |
| [**listAccounts**](AccountsApi.md#listAccounts) | **GET** /v1/accounts | List accounts |
| [**listAccountsWithHttpInfo**](AccountsApi.md#listAccountsWithHttpInfo) | **GET** /v1/accounts | List accounts |
| [**listBusinessPartners**](AccountsApi.md#listBusinessPartners) | **GET** /v1/accounts/{accountId}/business-partners | List partner businesses of the Page |
| [**listBusinessPartnersWithHttpInfo**](AccountsApi.md#listBusinessPartnersWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-partners | List partner businesses of the Page |
| [**listTikTokCommercialMusic**](AccountsApi.md#listTikTokCommercialMusic) | **GET** /v1/accounts/{accountId}/tiktok/commercial-music | List trending commercial music |
| [**listTikTokCommercialMusicWithHttpInfo**](AccountsApi.md#listTikTokCommercialMusicWithHttpInfo) | **GET** /v1/accounts/{accountId}/tiktok/commercial-music | List trending commercial music |
| [**moveAccountToProfile**](AccountsApi.md#moveAccountToProfile) | **PATCH** /v1/accounts/{accountId} | Move account to another profile |
| [**moveAccountToProfileWithHttpInfo**](AccountsApi.md#moveAccountToProfileWithHttpInfo) | **PATCH** /v1/accounts/{accountId} | Move account to another profile |
| [**revokeBusinessPartner**](AccountsApi.md#revokeBusinessPartner) | **DELETE** /v1/accounts/{accountId}/business-partners | Revoke a partner business from the Page |
| [**revokeBusinessPartnerWithHttpInfo**](AccountsApi.md#revokeBusinessPartnerWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-partners | Revoke a partner business from the Page |
| [**searchTikTokLocations**](AccountsApi.md#searchTikTokLocations) | **GET** /v1/accounts/{accountId}/tiktok/locations | Search TikTok location tags |
| [**searchTikTokLocationsWithHttpInfo**](AccountsApi.md#searchTikTokLocationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/tiktok/locations | Search TikTok location tags |
| [**updateAccount**](AccountsApi.md#updateAccount) | **PUT** /v1/accounts/{accountId} | Update account |
| [**updateAccountWithHttpInfo**](AccountsApi.md#updateAccountWithHttpInfo) | **PUT** /v1/accounts/{accountId} | Update account |
| [**updateBlueskySettings**](AccountsApi.md#updateBlueskySettings) | **PATCH** /v1/accounts/{accountId}/bluesky-settings | Update Bluesky account settings |
| [**updateBlueskySettingsWithHttpInfo**](AccountsApi.md#updateBlueskySettingsWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/bluesky-settings | Update Bluesky account settings |
| [**updateSlackSettings**](AccountsApi.md#updateSlackSettings) | **PATCH** /v1/accounts/{accountId}/slack-settings | Update Slack account settings |
| [**updateSlackSettingsWithHttpInfo**](AccountsApi.md#updateSlackSettingsWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/slack-settings | Update Slack account settings |



## deleteAccount

> DeleteAccountGroup200Response deleteAccount(accountId)

Disconnect account

Disconnects and removes a connected account. Repeating the call for an account already disconnected returns 404, the account stays in its 1h grace window and the disconnect is not re-run.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            DeleteAccountGroup200Response result = apiInstance.deleteAccount(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#deleteAccount");
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

### Return type

[**DeleteAccountGroup200Response**](DeleteAccountGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disconnected |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## deleteAccountWithHttpInfo

> ApiResponse<DeleteAccountGroup200Response> deleteAccount deleteAccountWithHttpInfo(accountId)

Disconnect account

Disconnects and removes a connected account. Repeating the call for an account already disconnected returns 404, the account stays in its 1h grace window and the disconnect is not re-run.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<DeleteAccountGroup200Response> response = apiInstance.deleteAccountWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#deleteAccount");
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

### Return type

ApiResponse<[**DeleteAccountGroup200Response**](DeleteAccountGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disconnected |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getAccountHealth

> GetAccountHealth200Response getAccountHealth(accountId)

Check account health

Returns detailed health info for a specific account including token status, permissions, and recommendations.  For WhatsApp accounts the response also includes &#x60;platformConnection&#x60;, a live probe of the Meta link behind the channel (the same read as &#x60;GET /v1/whatsapp/number-info&#x60;). The OAuth token can be perfectly valid while Meta refuses to serve the phone-number object (for example after a phone-side coexistence disconnect), so &#x60;tokenStatus&#x60; alone is not a liveness signal for WhatsApp. When the Meta link is dead, &#x60;platformConnection.status&#x60; is &#x60;disconnected&#x60; and the overall &#x60;status&#x60; is &#x60;error&#x60;. When Meta reports that the number&#39;s inbound message webhook does not reach Zernio, &#x60;platformConnection.inboundWebhookSubscribed&#x60; is &#x60;false&#x60;, an entry is added to &#x60;issues&#x60;, and the overall &#x60;status&#x60; is at least &#x60;warning&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The account ID to check
        try {
            GetAccountHealth200Response result = apiInstance.getAccountHealth(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getAccountHealth");
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
| **accountId** | **String**| The account ID to check | |

### Return type

[**GetAccountHealth200Response**](GetAccountHealth200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account health details |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getAccountHealthWithHttpInfo

> ApiResponse<GetAccountHealth200Response> getAccountHealth getAccountHealthWithHttpInfo(accountId)

Check account health

Returns detailed health info for a specific account including token status, permissions, and recommendations.  For WhatsApp accounts the response also includes &#x60;platformConnection&#x60;, a live probe of the Meta link behind the channel (the same read as &#x60;GET /v1/whatsapp/number-info&#x60;). The OAuth token can be perfectly valid while Meta refuses to serve the phone-number object (for example after a phone-side coexistence disconnect), so &#x60;tokenStatus&#x60; alone is not a liveness signal for WhatsApp. When the Meta link is dead, &#x60;platformConnection.status&#x60; is &#x60;disconnected&#x60; and the overall &#x60;status&#x60; is &#x60;error&#x60;. When Meta reports that the number&#39;s inbound message webhook does not reach Zernio, &#x60;platformConnection.inboundWebhookSubscribed&#x60; is &#x60;false&#x60;, an entry is added to &#x60;issues&#x60;, and the overall &#x60;status&#x60; is at least &#x60;warning&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The account ID to check
        try {
            ApiResponse<GetAccountHealth200Response> response = apiInstance.getAccountHealthWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getAccountHealth");
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
| **accountId** | **String**| The account ID to check | |

### Return type

ApiResponse<[**GetAccountHealth200Response**](GetAccountHealth200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account health details |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getAccountPosts

> GetAccountPosts200Response getAccountPosts(accountId)

List posts published on the platform

Returns the 25 most recent posts that exist on the platform for a connected account, read live from the platform API. This covers everything on the account, including posts that were never created through Zernio.  Use it to obtain the platform&#39;s own post id, which the analytics endpoints take as input. On YouTube the returned &#x60;id&#x60; is the video ID that &#x60;GET /v1/analytics/youtube/daily-views&#x60;, &#x60;/video-retention&#x60; and &#x60;/demographics&#x60; expect as &#x60;videoId&#x60;, so this endpoint is what backs a video picker in your own UI.  Not every field applies to every platform: &#x60;reactionCount&#x60; is Facebook and LinkedIn, &#x60;shareCount&#x60; is platform dependent, &#x60;cid&#x60; is the Bluesky content id needed to reply, and &#x60;subreddit&#x60; is Reddit only. Absent fields are omitted from the response.  The account&#39;s token is refreshed before the call when it has expired. When the refresh cannot recover it, the response is a 401 with code &#x60;TOKEN_EXPIRED&#x60; and the account has to be reconnected. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetAccountPosts200Response result = apiInstance.getAccountPosts(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getAccountPosts");
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

### Return type

[**GetAccountPosts200Response**](GetAccountPosts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Posts list |  -  |
| **400** | Invalid accountId, platform does not support posts listing, or the account has no access token |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | X analytics capability not enabled for this account (code X_ANALYTICS_NOT_ENABLED) |  -  |
| **404** | Resource not found |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## getAccountPostsWithHttpInfo

> ApiResponse<GetAccountPosts200Response> getAccountPosts getAccountPostsWithHttpInfo(accountId)

List posts published on the platform

Returns the 25 most recent posts that exist on the platform for a connected account, read live from the platform API. This covers everything on the account, including posts that were never created through Zernio.  Use it to obtain the platform&#39;s own post id, which the analytics endpoints take as input. On YouTube the returned &#x60;id&#x60; is the video ID that &#x60;GET /v1/analytics/youtube/daily-views&#x60;, &#x60;/video-retention&#x60; and &#x60;/demographics&#x60; expect as &#x60;videoId&#x60;, so this endpoint is what backs a video picker in your own UI.  Not every field applies to every platform: &#x60;reactionCount&#x60; is Facebook and LinkedIn, &#x60;shareCount&#x60; is platform dependent, &#x60;cid&#x60; is the Bluesky content id needed to reply, and &#x60;subreddit&#x60; is Reddit only. Absent fields are omitted from the response.  The account&#39;s token is refreshed before the call when it has expired. When the refresh cannot recover it, the response is a 401 with code &#x60;TOKEN_EXPIRED&#x60; and the account has to be reconnected. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetAccountPosts200Response> response = apiInstance.getAccountPostsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getAccountPosts");
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

### Return type

ApiResponse<[**GetAccountPosts200Response**](GetAccountPosts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Posts list |  -  |
| **400** | Invalid accountId, platform does not support posts listing, or the account has no access token |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | X analytics capability not enabled for this account (code X_ANALYTICS_NOT_ENABLED) |  -  |
| **404** | Resource not found |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## getAllAccountsHealth

> GetAllAccountsHealth200Response getAllAccountsHealth(profileId, platform, status)

Check accounts health

Returns health status of all connected accounts including token validity, permissions, and issues needing attention.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile ID
        String platform = "facebook"; // String | Filter by platform
        String status = "healthy"; // String | Filter by health status
        try {
            GetAllAccountsHealth200Response result = apiInstance.getAllAccountsHealth(profileId, platform, status);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getAllAccountsHealth");
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
| **platform** | **String**| Filter by platform | [optional] [enum: facebook, instagram, linkedin, twitter, tiktok, youtube, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, discord, slack, whatsapp, shopify, wordpress, linkedinads, metaads, pinterestads, tiktokads, xads, googleads, openaiads, whopads] |
| **status** | **String**| Filter by health status | [optional] [enum: healthy, warning, error] |

### Return type

[**GetAllAccountsHealth200Response**](GetAllAccountsHealth200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account health summary |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## getAllAccountsHealthWithHttpInfo

> ApiResponse<GetAllAccountsHealth200Response> getAllAccountsHealth getAllAccountsHealthWithHttpInfo(profileId, platform, status)

Check accounts health

Returns health status of all connected accounts including token validity, permissions, and issues needing attention.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile ID
        String platform = "facebook"; // String | Filter by platform
        String status = "healthy"; // String | Filter by health status
        try {
            ApiResponse<GetAllAccountsHealth200Response> response = apiInstance.getAllAccountsHealthWithHttpInfo(profileId, platform, status);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getAllAccountsHealth");
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
| **platform** | **String**| Filter by platform | [optional] [enum: facebook, instagram, linkedin, twitter, tiktok, youtube, threads, pinterest, reddit, bluesky, googlebusiness, telegram, snapchat, discord, slack, whatsapp, shopify, wordpress, linkedinads, metaads, pinterestads, tiktokads, xads, googleads, openaiads, whopads] |
| **status** | **String**| Filter by health status | [optional] [enum: healthy, warning, error] |

### Return type

ApiResponse<[**GetAllAccountsHealth200Response**](GetAllAccountsHealth200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account health summary |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## getBlueskySettings

> GetBlueskySettings200Response getBlueskySettings(accountId)

Get Bluesky account settings

Returns the account&#39;s default post languages (defaultLangs), applied at publish time whenever a post&#39;s platformSpecificData.langs is absent. Null when no default is set.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetBlueskySettings200Response result = apiInstance.getBlueskySettings(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getBlueskySettings");
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

### Return type

[**GetBlueskySettings200Response**](GetBlueskySettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bluesky account settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |

## getBlueskySettingsWithHttpInfo

> ApiResponse<GetBlueskySettings200Response> getBlueskySettings getBlueskySettingsWithHttpInfo(accountId)

Get Bluesky account settings

Returns the account&#39;s default post languages (defaultLangs), applied at publish time whenever a post&#39;s platformSpecificData.langs is absent. Null when no default is set.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetBlueskySettings200Response> response = apiInstance.getBlueskySettingsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getBlueskySettings");
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

### Return type

ApiResponse<[**GetBlueskySettings200Response**](GetBlueskySettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bluesky account settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |


## getFollowerStats

> FollowerStatsResponse getFollowerStats(accountIds, profileId, fromDate, toDate, granularity)

Get follower stats

Returns follower count history and growth metrics for connected accounts. Requires analytics add-on subscription. Follower counts are refreshed once per day. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountIds = "accountIds_example"; // String | Comma-separated list of account IDs (optional, defaults to all user's accounts)
        String profileId = "profileId_example"; // String | Filter by profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start date in YYYY-MM-DD format (defaults to 30 days ago)
        LocalDate toDate = LocalDate.now(); // LocalDate | End date in YYYY-MM-DD format (defaults to today)
        String granularity = "daily"; // String | Data aggregation level
        try {
            FollowerStatsResponse result = apiInstance.getFollowerStats(accountIds, profileId, fromDate, toDate, granularity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getFollowerStats");
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
| **accountIds** | **String**| Comma-separated list of account IDs (optional, defaults to all user&#39;s accounts) | [optional] |
| **profileId** | **String**| Filter by profile ID | [optional] |
| **fromDate** | **LocalDate**| Start date in YYYY-MM-DD format (defaults to 30 days ago) | [optional] |
| **toDate** | **LocalDate**| End date in YYYY-MM-DD format (defaults to today) | [optional] |
| **granularity** | **String**| Data aggregation level | [optional] [default to daily] [enum: daily, weekly, monthly] |

### Return type

[**FollowerStatsResponse**](FollowerStatsResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Follower stats |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |

## getFollowerStatsWithHttpInfo

> ApiResponse<FollowerStatsResponse> getFollowerStats getFollowerStatsWithHttpInfo(accountIds, profileId, fromDate, toDate, granularity)

Get follower stats

Returns follower count history and growth metrics for connected accounts. Requires analytics add-on subscription. Follower counts are refreshed once per day. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountIds = "accountIds_example"; // String | Comma-separated list of account IDs (optional, defaults to all user's accounts)
        String profileId = "profileId_example"; // String | Filter by profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start date in YYYY-MM-DD format (defaults to 30 days ago)
        LocalDate toDate = LocalDate.now(); // LocalDate | End date in YYYY-MM-DD format (defaults to today)
        String granularity = "daily"; // String | Data aggregation level
        try {
            ApiResponse<FollowerStatsResponse> response = apiInstance.getFollowerStatsWithHttpInfo(accountIds, profileId, fromDate, toDate, granularity);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getFollowerStats");
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
| **accountIds** | **String**| Comma-separated list of account IDs (optional, defaults to all user&#39;s accounts) | [optional] |
| **profileId** | **String**| Filter by profile ID | [optional] |
| **fromDate** | **LocalDate**| Start date in YYYY-MM-DD format (defaults to 30 days ago) | [optional] |
| **toDate** | **LocalDate**| End date in YYYY-MM-DD format (defaults to today) | [optional] |
| **granularity** | **String**| Data aggregation level | [optional] [default to daily] [enum: daily, weekly, monthly] |

### Return type

ApiResponse<[**FollowerStatsResponse**](FollowerStatsResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Follower stats |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Analytics access required. Legacy plans need the Analytics add-on; included by default on usage-based plans. |  -  |


## getInstagramFollowStatus

> GetInstagramFollowStatus200Response getInstagramFollowStatus(accountId, userId, refresh)

Check whether an Instagram user follows the account

Resolves the follow relationship between an Instagram user and the connected account, plus their public profile counters.  &#x60;userId&#x60; is the Instagram-scoped id (IGSID) Meta gives you on a webhook: &#x60;sender.id&#x60; on &#x60;message.received&#x60;, &#x60;comment.author.id&#x60; on &#x60;comment.received&#x60;.  **Meta only answers for people who have MESSAGED the account.** Commenting grants no consent, so a commenter who has never DMed you is unresolvable - that is a platform rule, not a limitation of this endpoint. When it cannot be resolved the response is still &#x60;200&#x60; with &#x60;isFollower: null&#x60; and an &#x60;unavailableReason&#x60;, because \&quot;unknown\&quot; is a normal state to branch on:    * &#x60;consent_required&#x60; - the user has never messaged this account.   * &#x60;dm_access_disabled&#x60; - the account owner turned off Instagram Direct API access.   * &#x60;not_messageable&#x60; - the id is not a messaging-scoped id.   * &#x60;error&#x60; - a transient Graph API failure.  To gate a comment automation on this, use the automation&#39;s &#x60;audience&#x60; rules instead of calling this per comment - they run the same lookup only on comments that actually match a keyword, and can ask the commenter to confirm with one tap.  Answers are cached briefly per (account, user). Pass &#x60;refresh&#x3D;true&#x60; right after asking someone to follow, so a follow from a moment ago is visible. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Instagram account ID
        String userId = "userId_example"; // String | Instagram-scoped user id (IGSID) from a webhook payload
        Boolean refresh = true; // Boolean | Bypass the cache and re-query Meta
        try {
            GetInstagramFollowStatus200Response result = apiInstance.getInstagramFollowStatus(accountId, userId, refresh);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getInstagramFollowStatus");
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
| **accountId** | **String**| Instagram account ID | |
| **userId** | **String**| Instagram-scoped user id (IGSID) from a webhook payload | |
| **refresh** | **Boolean**| Bypass the cache and re-query Meta | [optional] |

### Return type

[**GetInstagramFollowStatus200Response**](GetInstagramFollowStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Follow status (fields are null when Meta would not resolve it) |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getInstagramFollowStatusWithHttpInfo

> ApiResponse<GetInstagramFollowStatus200Response> getInstagramFollowStatus getInstagramFollowStatusWithHttpInfo(accountId, userId, refresh)

Check whether an Instagram user follows the account

Resolves the follow relationship between an Instagram user and the connected account, plus their public profile counters.  &#x60;userId&#x60; is the Instagram-scoped id (IGSID) Meta gives you on a webhook: &#x60;sender.id&#x60; on &#x60;message.received&#x60;, &#x60;comment.author.id&#x60; on &#x60;comment.received&#x60;.  **Meta only answers for people who have MESSAGED the account.** Commenting grants no consent, so a commenter who has never DMed you is unresolvable - that is a platform rule, not a limitation of this endpoint. When it cannot be resolved the response is still &#x60;200&#x60; with &#x60;isFollower: null&#x60; and an &#x60;unavailableReason&#x60;, because \&quot;unknown\&quot; is a normal state to branch on:    * &#x60;consent_required&#x60; - the user has never messaged this account.   * &#x60;dm_access_disabled&#x60; - the account owner turned off Instagram Direct API access.   * &#x60;not_messageable&#x60; - the id is not a messaging-scoped id.   * &#x60;error&#x60; - a transient Graph API failure.  To gate a comment automation on this, use the automation&#39;s &#x60;audience&#x60; rules instead of calling this per comment - they run the same lookup only on comments that actually match a keyword, and can ask the commenter to confirm with one tap.  Answers are cached briefly per (account, user). Pass &#x60;refresh&#x3D;true&#x60; right after asking someone to follow, so a follow from a moment ago is visible. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Instagram account ID
        String userId = "userId_example"; // String | Instagram-scoped user id (IGSID) from a webhook payload
        Boolean refresh = true; // Boolean | Bypass the cache and re-query Meta
        try {
            ApiResponse<GetInstagramFollowStatus200Response> response = apiInstance.getInstagramFollowStatusWithHttpInfo(accountId, userId, refresh);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getInstagramFollowStatus");
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
| **accountId** | **String**| Instagram account ID | |
| **userId** | **String**| Instagram-scoped user id (IGSID) from a webhook payload | |
| **refresh** | **Boolean**| Bypass the cache and re-query Meta | [optional] |

### Return type

ApiResponse<[**GetInstagramFollowStatus200Response**](GetInstagramFollowStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Follow status (fields are null when Meta would not resolve it) |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getSlackSettings

> GetSlackSettings200Response getSlackSettings(accountId)

Get Slack account settings

Returns the connected Slack channel details and the default message identity (name and avatar shown as the author on every post, with Slack&#39;s APP badge). The identity applies to messages only; the app&#39;s own Slack profile is global and cannot be changed per workspace.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            GetSlackSettings200Response result = apiInstance.getSlackSettings(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getSlackSettings");
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

### Return type

[**GetSlackSettings200Response**](GetSlackSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Slack account settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |

## getSlackSettingsWithHttpInfo

> ApiResponse<GetSlackSettings200Response> getSlackSettings getSlackSettingsWithHttpInfo(accountId)

Get Slack account settings

Returns the connected Slack channel details and the default message identity (name and avatar shown as the author on every post, with Slack&#39;s APP badge). The identity applies to messages only; the app&#39;s own Slack profile is global and cannot be changed per workspace.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetSlackSettings200Response> response = apiInstance.getSlackSettingsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getSlackSettings");
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

### Return type

ApiResponse<[**GetSlackSettings200Response**](GetSlackSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Slack account settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |


## getTikTokCreatorInfo

> GetTikTokCreatorInfo200Response getTikTokCreatorInfo(accountId, mediaType)

Get TikTok creator info

Returns TikTok creator details, available privacy levels, posting limits, and commercial content options for a specific TikTok account. Only works with TikTok accounts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The TikTok account ID
        String mediaType = "video"; // String | The media type to get creator info for (affects available interaction settings)
        try {
            GetTikTokCreatorInfo200Response result = apiInstance.getTikTokCreatorInfo(accountId, mediaType);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getTikTokCreatorInfo");
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
| **accountId** | **String**| The TikTok account ID | |
| **mediaType** | **String**| The media type to get creator info for (affects available interaction settings) | [optional] [default to video] [enum: video, photo] |

### Return type

[**GetTikTokCreatorInfo200Response**](GetTikTokCreatorInfo200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TikTok creator info and posting options |  -  |
| **400** | Account is not a TikTok account |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **429** | Creator has reached TikTok daily posting limit |  -  |

## getTikTokCreatorInfoWithHttpInfo

> ApiResponse<GetTikTokCreatorInfo200Response> getTikTokCreatorInfo getTikTokCreatorInfoWithHttpInfo(accountId, mediaType)

Get TikTok creator info

Returns TikTok creator details, available privacy levels, posting limits, and commercial content options for a specific TikTok account. Only works with TikTok accounts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The TikTok account ID
        String mediaType = "video"; // String | The media type to get creator info for (affects available interaction settings)
        try {
            ApiResponse<GetTikTokCreatorInfo200Response> response = apiInstance.getTikTokCreatorInfoWithHttpInfo(accountId, mediaType);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getTikTokCreatorInfo");
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
| **accountId** | **String**| The TikTok account ID | |
| **mediaType** | **String**| The media type to get creator info for (affects available interaction settings) | [optional] [default to video] [enum: video, photo] |

### Return type

ApiResponse<[**GetTikTokCreatorInfo200Response**](GetTikTokCreatorInfo200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TikTok creator info and posting options |  -  |
| **400** | Account is not a TikTok account |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **429** | Creator has reached TikTok daily posting limit |  -  |


## grantBusinessPartner

> GrantBusinessPartner200Response grantBusinessPartner(accountId, grantBusinessPartnerRequest)

Share the Page with a partner business

Grants a partner business portfolio tasks on the Facebook Page behind this account. With &#x60;ADVERTISE&#x60;, the partner can run ads for the Page from ad accounts in its own portfolio, which is how an integrator advertises for an end user without touching the end user&#39;s ad accounts.  Meta only lets a user token share a Page that a business portfolio owns. A Page outside any portfolio must first be claimed into one at business.facebook.com; this endpoint answers &#x60;422&#x60; until that is done. Meta refuses a second grant to a portfolio that already has access instead of replacing its tasks, so that case answers &#x60;200&#x60; with &#x60;alreadyShared: true&#x60; and the tasks the partner currently holds. To change a partner&#39;s tasks, revoke and grant again.  After the grant, the partner assigns its own people to the Page with &#x60;POST /v1/ads/page-users&#x60;; Meta does not assign partner admins automatically. The Instagram professional account linked to the Page is returned in &#x60;page&#x60; so the partner can reference it; Meta exposes no API to share Instagram accounts, that is done in Business Settings. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id of the Facebook or Instagram account.
        GrantBusinessPartnerRequest grantBusinessPartnerRequest = new GrantBusinessPartnerRequest(); // GrantBusinessPartnerRequest | 
        try {
            GrantBusinessPartner200Response result = apiInstance.grantBusinessPartner(accountId, grantBusinessPartnerRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#grantBusinessPartner");
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
| **accountId** | **String**| Zernio SocialAccount id of the Facebook or Instagram account. | |
| **grantBusinessPartnerRequest** | [**GrantBusinessPartnerRequest**](GrantBusinessPartnerRequest.md)|  | |

### Return type

[**GrantBusinessPartner200Response**](GrantBusinessPartner200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Page shared |  -  |
| **200** | The portfolio already had access; nothing changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Meta refused: the connecting user lacks business_management or is not an admin of the owning portfolio. Reconnect the account. |  -  |
| **404** | Account not found, or Meta could not load the partner business. |  -  |
| **422** | The Page is not owned by a business portfolio, or no Page is linked to the account. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## grantBusinessPartnerWithHttpInfo

> ApiResponse<GrantBusinessPartner200Response> grantBusinessPartner grantBusinessPartnerWithHttpInfo(accountId, grantBusinessPartnerRequest)

Share the Page with a partner business

Grants a partner business portfolio tasks on the Facebook Page behind this account. With &#x60;ADVERTISE&#x60;, the partner can run ads for the Page from ad accounts in its own portfolio, which is how an integrator advertises for an end user without touching the end user&#39;s ad accounts.  Meta only lets a user token share a Page that a business portfolio owns. A Page outside any portfolio must first be claimed into one at business.facebook.com; this endpoint answers &#x60;422&#x60; until that is done. Meta refuses a second grant to a portfolio that already has access instead of replacing its tasks, so that case answers &#x60;200&#x60; with &#x60;alreadyShared: true&#x60; and the tasks the partner currently holds. To change a partner&#39;s tasks, revoke and grant again.  After the grant, the partner assigns its own people to the Page with &#x60;POST /v1/ads/page-users&#x60;; Meta does not assign partner admins automatically. The Instagram professional account linked to the Page is returned in &#x60;page&#x60; so the partner can reference it; Meta exposes no API to share Instagram accounts, that is done in Business Settings. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id of the Facebook or Instagram account.
        GrantBusinessPartnerRequest grantBusinessPartnerRequest = new GrantBusinessPartnerRequest(); // GrantBusinessPartnerRequest | 
        try {
            ApiResponse<GrantBusinessPartner200Response> response = apiInstance.grantBusinessPartnerWithHttpInfo(accountId, grantBusinessPartnerRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#grantBusinessPartner");
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
| **accountId** | **String**| Zernio SocialAccount id of the Facebook or Instagram account. | |
| **grantBusinessPartnerRequest** | [**GrantBusinessPartnerRequest**](GrantBusinessPartnerRequest.md)|  | |

### Return type

ApiResponse<[**GrantBusinessPartner200Response**](GrantBusinessPartner200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Page shared |  -  |
| **200** | The portfolio already had access; nothing changed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Meta refused: the connecting user lacks business_management or is not an admin of the owning portfolio. Reconnect the account. |  -  |
| **404** | Account not found, or Meta could not load the partner business. |  -  |
| **422** | The Page is not owned by a business portfolio, or no Page is linked to the account. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## listAccounts

> AccountsListResponse listAccounts(profileId, platform, status, search, category, sort, order, includeOverLimit, excludeHidden, includeSandbox, includeStatusCounts, page, limit, profileIds, perProfile)

List accounts

Returns connected accounts. Only includes accounts within the plan limit by default. Follower data requires analytics add-on. Supports optional server-side pagination via page/limit params. When omitted, returns all accounts (backward-compatible). page and limit must be supplied together; out-of-range page/limit values are rejected with 400 rather than silently clamped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter accounts by profile ID. Must be a valid ObjectId.
        String platform = "platform_example"; // String | Filter accounts by platform (e.g. \"instagram\", \"twitter\").
        String status = "connected"; // String | Filter accounts by connection status. `connected` returns healthy accounts; `disconnected` returns accounts that need reconnection (per the same reconnection check surfaced in the dashboard). Omit to return accounts in any status. When combined with page/limit, pagination totals reflect the filtered result set. 
        String search = "search_example"; // String | Case-insensitive match on the account username, display name or platform user id, or an exact account id. Combine with page/limit to paginate the matches.
        String category = "social"; // String | Only accounts of this kind. ads = ad accounts (Meta, Google, LinkedIn, Pinterest, TikTok, X, OpenAI), communication = WhatsApp, Telegram, Discord, Slack and iMessage, blogs = Shopify and WordPress, social = every other platform.
        String sort = "account"; // String | Sort a paginated listing (page/limit) by account name, platform, profile name, status (accounts needing a reconnect first when ascending) or connection date. Ties keep the default order: platform, then newest first.
        String order = "asc"; // String | Direction for `sort`.
        Boolean includeOverLimit = false; // Boolean | When true, includes accounts from over-limit profiles.
        Boolean excludeHidden = false; // Boolean | When true, leaves out accounts the dashboard does not show as connections: posting accounts with `enabled: false` (ads accounts are always kept, whatever their `enabled` value) and the internal `sms` and `phone` accounts behind each phone number. Applied before pagination, so page totals and `statusCounts` count only the remaining accounts. Sandbox accounts added by `includeSandbox` are appended after this filter. Accepts `true` or `false` in any letter case; any other value returns 400. 
        Boolean includeSandbox = false; // Boolean | When true, appends the shared WhatsApp sandbox account and the iMessage sandbox account to the list when they are active, honouring `platform` but no other filter. Ignored on a paginated request (page/limit) and together with `perProfile`. Accepts `true` or `false` in any letter case; any other value returns 400. 
        Boolean includeStatusCounts = false; // Boolean | When true, the response carries `statusCounts`: how many accounts match every other filter of the request (with `status` lifted) in total and how many of those need a reconnection. Accepts `true` or `false` in any letter case; any other value returns 400. 
        Integer page = 56; // Integer | Page number (1-based). Must be provided together with limit to enable server-side pagination; sending only one of the two returns 400. Omit both for all accounts. 
        Integer limit = 56; // Integer | Page size. Must be provided together with page; sending only one of the two returns 400. 
        String profileIds = "profileIds_example"; // String | Comma-separated profile IDs (up to 50) to preview, together with perProfile. The response then also carries `profileTotals`.
        Integer perProfile = 56; // Integer | Return a preview of each profile in profileIds: the newest account of every platform it has, topped up to at least N. Requires profileIds; cannot be combined with page and limit.
        try {
            AccountsListResponse result = apiInstance.listAccounts(profileId, platform, status, search, category, sort, order, includeOverLimit, excludeHidden, includeSandbox, includeStatusCounts, page, limit, profileIds, perProfile);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#listAccounts");
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
| **profileId** | **String**| Filter accounts by profile ID. Must be a valid ObjectId. | [optional] |
| **platform** | **String**| Filter accounts by platform (e.g. \&quot;instagram\&quot;, \&quot;twitter\&quot;). | [optional] |
| **status** | **String**| Filter accounts by connection status. &#x60;connected&#x60; returns healthy accounts; &#x60;disconnected&#x60; returns accounts that need reconnection (per the same reconnection check surfaced in the dashboard). Omit to return accounts in any status. When combined with page/limit, pagination totals reflect the filtered result set.  | [optional] [enum: connected, disconnected] |
| **search** | **String**| Case-insensitive match on the account username, display name or platform user id, or an exact account id. Combine with page/limit to paginate the matches. | [optional] |
| **category** | **String**| Only accounts of this kind. ads &#x3D; ad accounts (Meta, Google, LinkedIn, Pinterest, TikTok, X, OpenAI), communication &#x3D; WhatsApp, Telegram, Discord, Slack and iMessage, blogs &#x3D; Shopify and WordPress, social &#x3D; every other platform. | [optional] [enum: social, ads, communication, blogs] |
| **sort** | **String**| Sort a paginated listing (page/limit) by account name, platform, profile name, status (accounts needing a reconnect first when ascending) or connection date. Ties keep the default order: platform, then newest first. | [optional] [enum: account, platform, profile, status, connected] |
| **order** | **String**| Direction for &#x60;sort&#x60;. | [optional] [default to asc] [enum: asc, desc] |
| **includeOverLimit** | **Boolean**| When true, includes accounts from over-limit profiles. | [optional] [default to false] |
| **excludeHidden** | **Boolean**| When true, leaves out accounts the dashboard does not show as connections: posting accounts with &#x60;enabled: false&#x60; (ads accounts are always kept, whatever their &#x60;enabled&#x60; value) and the internal &#x60;sms&#x60; and &#x60;phone&#x60; accounts behind each phone number. Applied before pagination, so page totals and &#x60;statusCounts&#x60; count only the remaining accounts. Sandbox accounts added by &#x60;includeSandbox&#x60; are appended after this filter. Accepts &#x60;true&#x60; or &#x60;false&#x60; in any letter case; any other value returns 400.  | [optional] [default to false] |
| **includeSandbox** | **Boolean**| When true, appends the shared WhatsApp sandbox account and the iMessage sandbox account to the list when they are active, honouring &#x60;platform&#x60; but no other filter. Ignored on a paginated request (page/limit) and together with &#x60;perProfile&#x60;. Accepts &#x60;true&#x60; or &#x60;false&#x60; in any letter case; any other value returns 400.  | [optional] [default to false] |
| **includeStatusCounts** | **Boolean**| When true, the response carries &#x60;statusCounts&#x60;: how many accounts match every other filter of the request (with &#x60;status&#x60; lifted) in total and how many of those need a reconnection. Accepts &#x60;true&#x60; or &#x60;false&#x60; in any letter case; any other value returns 400.  | [optional] [default to false] |
| **page** | **Integer**| Page number (1-based). Must be provided together with limit to enable server-side pagination; sending only one of the two returns 400. Omit both for all accounts.  | [optional] |
| **limit** | **Integer**| Page size. Must be provided together with page; sending only one of the two returns 400.  | [optional] |
| **profileIds** | **String**| Comma-separated profile IDs (up to 50) to preview, together with perProfile. The response then also carries &#x60;profileTotals&#x60;. | [optional] |
| **perProfile** | **Integer**| Return a preview of each profile in profileIds: the newest account of every platform it has, topped up to at least N. Requires profileIds; cannot be combined with page and limit. | [optional] |

### Return type

[**AccountsListResponse**](AccountsListResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accounts (with optional pagination) |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## listAccountsWithHttpInfo

> ApiResponse<AccountsListResponse> listAccounts listAccountsWithHttpInfo(profileId, platform, status, search, category, sort, order, includeOverLimit, excludeHidden, includeSandbox, includeStatusCounts, page, limit, profileIds, perProfile)

List accounts

Returns connected accounts. Only includes accounts within the plan limit by default. Follower data requires analytics add-on. Supports optional server-side pagination via page/limit params. When omitted, returns all accounts (backward-compatible). page and limit must be supplied together; out-of-range page/limit values are rejected with 400 rather than silently clamped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter accounts by profile ID. Must be a valid ObjectId.
        String platform = "platform_example"; // String | Filter accounts by platform (e.g. \"instagram\", \"twitter\").
        String status = "connected"; // String | Filter accounts by connection status. `connected` returns healthy accounts; `disconnected` returns accounts that need reconnection (per the same reconnection check surfaced in the dashboard). Omit to return accounts in any status. When combined with page/limit, pagination totals reflect the filtered result set. 
        String search = "search_example"; // String | Case-insensitive match on the account username, display name or platform user id, or an exact account id. Combine with page/limit to paginate the matches.
        String category = "social"; // String | Only accounts of this kind. ads = ad accounts (Meta, Google, LinkedIn, Pinterest, TikTok, X, OpenAI), communication = WhatsApp, Telegram, Discord, Slack and iMessage, blogs = Shopify and WordPress, social = every other platform.
        String sort = "account"; // String | Sort a paginated listing (page/limit) by account name, platform, profile name, status (accounts needing a reconnect first when ascending) or connection date. Ties keep the default order: platform, then newest first.
        String order = "asc"; // String | Direction for `sort`.
        Boolean includeOverLimit = false; // Boolean | When true, includes accounts from over-limit profiles.
        Boolean excludeHidden = false; // Boolean | When true, leaves out accounts the dashboard does not show as connections: posting accounts with `enabled: false` (ads accounts are always kept, whatever their `enabled` value) and the internal `sms` and `phone` accounts behind each phone number. Applied before pagination, so page totals and `statusCounts` count only the remaining accounts. Sandbox accounts added by `includeSandbox` are appended after this filter. Accepts `true` or `false` in any letter case; any other value returns 400. 
        Boolean includeSandbox = false; // Boolean | When true, appends the shared WhatsApp sandbox account and the iMessage sandbox account to the list when they are active, honouring `platform` but no other filter. Ignored on a paginated request (page/limit) and together with `perProfile`. Accepts `true` or `false` in any letter case; any other value returns 400. 
        Boolean includeStatusCounts = false; // Boolean | When true, the response carries `statusCounts`: how many accounts match every other filter of the request (with `status` lifted) in total and how many of those need a reconnection. Accepts `true` or `false` in any letter case; any other value returns 400. 
        Integer page = 56; // Integer | Page number (1-based). Must be provided together with limit to enable server-side pagination; sending only one of the two returns 400. Omit both for all accounts. 
        Integer limit = 56; // Integer | Page size. Must be provided together with page; sending only one of the two returns 400. 
        String profileIds = "profileIds_example"; // String | Comma-separated profile IDs (up to 50) to preview, together with perProfile. The response then also carries `profileTotals`.
        Integer perProfile = 56; // Integer | Return a preview of each profile in profileIds: the newest account of every platform it has, topped up to at least N. Requires profileIds; cannot be combined with page and limit.
        try {
            ApiResponse<AccountsListResponse> response = apiInstance.listAccountsWithHttpInfo(profileId, platform, status, search, category, sort, order, includeOverLimit, excludeHidden, includeSandbox, includeStatusCounts, page, limit, profileIds, perProfile);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#listAccounts");
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
| **profileId** | **String**| Filter accounts by profile ID. Must be a valid ObjectId. | [optional] |
| **platform** | **String**| Filter accounts by platform (e.g. \&quot;instagram\&quot;, \&quot;twitter\&quot;). | [optional] |
| **status** | **String**| Filter accounts by connection status. &#x60;connected&#x60; returns healthy accounts; &#x60;disconnected&#x60; returns accounts that need reconnection (per the same reconnection check surfaced in the dashboard). Omit to return accounts in any status. When combined with page/limit, pagination totals reflect the filtered result set.  | [optional] [enum: connected, disconnected] |
| **search** | **String**| Case-insensitive match on the account username, display name or platform user id, or an exact account id. Combine with page/limit to paginate the matches. | [optional] |
| **category** | **String**| Only accounts of this kind. ads &#x3D; ad accounts (Meta, Google, LinkedIn, Pinterest, TikTok, X, OpenAI), communication &#x3D; WhatsApp, Telegram, Discord, Slack and iMessage, blogs &#x3D; Shopify and WordPress, social &#x3D; every other platform. | [optional] [enum: social, ads, communication, blogs] |
| **sort** | **String**| Sort a paginated listing (page/limit) by account name, platform, profile name, status (accounts needing a reconnect first when ascending) or connection date. Ties keep the default order: platform, then newest first. | [optional] [enum: account, platform, profile, status, connected] |
| **order** | **String**| Direction for &#x60;sort&#x60;. | [optional] [default to asc] [enum: asc, desc] |
| **includeOverLimit** | **Boolean**| When true, includes accounts from over-limit profiles. | [optional] [default to false] |
| **excludeHidden** | **Boolean**| When true, leaves out accounts the dashboard does not show as connections: posting accounts with &#x60;enabled: false&#x60; (ads accounts are always kept, whatever their &#x60;enabled&#x60; value) and the internal &#x60;sms&#x60; and &#x60;phone&#x60; accounts behind each phone number. Applied before pagination, so page totals and &#x60;statusCounts&#x60; count only the remaining accounts. Sandbox accounts added by &#x60;includeSandbox&#x60; are appended after this filter. Accepts &#x60;true&#x60; or &#x60;false&#x60; in any letter case; any other value returns 400.  | [optional] [default to false] |
| **includeSandbox** | **Boolean**| When true, appends the shared WhatsApp sandbox account and the iMessage sandbox account to the list when they are active, honouring &#x60;platform&#x60; but no other filter. Ignored on a paginated request (page/limit) and together with &#x60;perProfile&#x60;. Accepts &#x60;true&#x60; or &#x60;false&#x60; in any letter case; any other value returns 400.  | [optional] [default to false] |
| **includeStatusCounts** | **Boolean**| When true, the response carries &#x60;statusCounts&#x60;: how many accounts match every other filter of the request (with &#x60;status&#x60; lifted) in total and how many of those need a reconnection. Accepts &#x60;true&#x60; or &#x60;false&#x60; in any letter case; any other value returns 400.  | [optional] [default to false] |
| **page** | **Integer**| Page number (1-based). Must be provided together with limit to enable server-side pagination; sending only one of the two returns 400. Omit both for all accounts.  | [optional] |
| **limit** | **Integer**| Page size. Must be provided together with page; sending only one of the two returns 400.  | [optional] |
| **profileIds** | **String**| Comma-separated profile IDs (up to 50) to preview, together with perProfile. The response then also carries &#x60;profileTotals&#x60;. | [optional] |
| **perProfile** | **Integer**| Return a preview of each profile in profileIds: the newest account of every platform it has, topped up to at least N. Requires profileIds; cannot be combined with page and limit. | [optional] |

### Return type

ApiResponse<[**AccountsListResponse**](AccountsListResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accounts (with optional pagination) |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## listBusinessPartners

> ListBusinessPartners200Response listBusinessPartners(accountId)

List partner businesses of the Page

The business portfolios (Meta Business Managers) that may act on the Facebook Page behind this account, plus the Page&#39;s owning portfolio and linked Instagram professional account. Works on Facebook accounts and on Instagram accounts connected through Facebook Login. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id of the Facebook or Instagram account.
        try {
            ListBusinessPartners200Response result = apiInstance.listBusinessPartners(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#listBusinessPartners");
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
| **accountId** | **String**| Zernio SocialAccount id of the Facebook or Instagram account. | |

### Return type

[**ListBusinessPartners200Response**](ListBusinessPartners200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page ownership and partners |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Meta refused: the connecting user lacks business_management or is not an admin of the owning portfolio. Reconnect the account. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | No Facebook Page is linked (Instagram Login account, or no Page selected). |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## listBusinessPartnersWithHttpInfo

> ApiResponse<ListBusinessPartners200Response> listBusinessPartners listBusinessPartnersWithHttpInfo(accountId)

List partner businesses of the Page

The business portfolios (Meta Business Managers) that may act on the Facebook Page behind this account, plus the Page&#39;s owning portfolio and linked Instagram professional account. Works on Facebook accounts and on Instagram accounts connected through Facebook Login. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id of the Facebook or Instagram account.
        try {
            ApiResponse<ListBusinessPartners200Response> response = apiInstance.listBusinessPartnersWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#listBusinessPartners");
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
| **accountId** | **String**| Zernio SocialAccount id of the Facebook or Instagram account. | |

### Return type

ApiResponse<[**ListBusinessPartners200Response**](ListBusinessPartners200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page ownership and partners |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Meta refused: the connecting user lacks business_management or is not an admin of the owning portfolio. Reconnect the account. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | No Facebook Page is linked (Instagram Login account, or no Page selected). |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## listTikTokCommercialMusic

> ListTikTokCommercialMusic200Response listTikTokCommercialMusic(accountId, countryCode)

List trending commercial music

Returns the 100 currently trending tracks of TikTok&#39;s Commercial Music Library for a TikTok account connected through the TikTok for Business app. Send a track&#39;s clip.id as tiktokSettings.musicSoundInfo.musicSoundId when creating a post; fall back to id only when the track has no clip. Both publish, but with the full-track id TikTok has shown viewers \&quot;This song is not available in your country\&quot; on the sound page (observed from Germany, 2026-10-06), while the clip id gave a working sound page for the same track. The list is not paged; countryCode selects the country chart.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The TikTok account ID
        String countryCode = "countryCode_example"; // String | Two-letter ISO 3166-1 country code of the chart to read (for example ES). Defaults to TikTok's global chart.
        try {
            ListTikTokCommercialMusic200Response result = apiInstance.listTikTokCommercialMusic(accountId, countryCode);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#listTikTokCommercialMusic");
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
| **accountId** | **String**| The TikTok account ID | |
| **countryCode** | **String**| Two-letter ISO 3166-1 country code of the chart to read (for example ES). Defaults to TikTok&#39;s global chart. | [optional] |

### Return type

[**ListTikTokCommercialMusic200Response**](ListTikTokCommercialMusic200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The trending tracks, rank 1 first |  -  |
| **400** | Invalid request |  -  |
| **404** | Account not found |  -  |

## listTikTokCommercialMusicWithHttpInfo

> ApiResponse<ListTikTokCommercialMusic200Response> listTikTokCommercialMusic listTikTokCommercialMusicWithHttpInfo(accountId, countryCode)

List trending commercial music

Returns the 100 currently trending tracks of TikTok&#39;s Commercial Music Library for a TikTok account connected through the TikTok for Business app. Send a track&#39;s clip.id as tiktokSettings.musicSoundInfo.musicSoundId when creating a post; fall back to id only when the track has no clip. Both publish, but with the full-track id TikTok has shown viewers \&quot;This song is not available in your country\&quot; on the sound page (observed from Germany, 2026-10-06), while the clip id gave a working sound page for the same track. The list is not paged; countryCode selects the country chart.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The TikTok account ID
        String countryCode = "countryCode_example"; // String | Two-letter ISO 3166-1 country code of the chart to read (for example ES). Defaults to TikTok's global chart.
        try {
            ApiResponse<ListTikTokCommercialMusic200Response> response = apiInstance.listTikTokCommercialMusicWithHttpInfo(accountId, countryCode);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#listTikTokCommercialMusic");
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
| **accountId** | **String**| The TikTok account ID | |
| **countryCode** | **String**| Two-letter ISO 3166-1 country code of the chart to read (for example ES). Defaults to TikTok&#39;s global chart. | [optional] |

### Return type

ApiResponse<[**ListTikTokCommercialMusic200Response**](ListTikTokCommercialMusic200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The trending tracks, rank 1 first |  -  |
| **400** | Invalid request |  -  |
| **404** | Account not found |  -  |


## moveAccountToProfile

> MoveAccountToProfile200Response moveAccountToProfile(accountId, moveAccountToProfileRequest)

Move account to another profile

Moves a connected account to a different profile owned by the same user. The target profile must belong to the same user as the account.  For API keys restricted to specific profiles, BOTH the source account&#39;s current profile AND the target profile must be in the key&#39;s allowed set. Calls with a target profile outside the key&#39;s scope return 403. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        MoveAccountToProfileRequest moveAccountToProfileRequest = new MoveAccountToProfileRequest(); // MoveAccountToProfileRequest | 
        try {
            MoveAccountToProfile200Response result = apiInstance.moveAccountToProfile(accountId, moveAccountToProfileRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#moveAccountToProfile");
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
| **moveAccountToProfileRequest** | [**MoveAccountToProfileRequest**](MoveAccountToProfileRequest.md)|  | |

### Return type

[**MoveAccountToProfile200Response**](MoveAccountToProfile200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account moved |  -  |
| **400** | Missing or invalid profileId |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | API key does not have access to the source account or target profile |  -  |
| **404** | Account or target profile not found |  -  |

## moveAccountToProfileWithHttpInfo

> ApiResponse<MoveAccountToProfile200Response> moveAccountToProfile moveAccountToProfileWithHttpInfo(accountId, moveAccountToProfileRequest)

Move account to another profile

Moves a connected account to a different profile owned by the same user. The target profile must belong to the same user as the account.  For API keys restricted to specific profiles, BOTH the source account&#39;s current profile AND the target profile must be in the key&#39;s allowed set. Calls with a target profile outside the key&#39;s scope return 403. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        MoveAccountToProfileRequest moveAccountToProfileRequest = new MoveAccountToProfileRequest(); // MoveAccountToProfileRequest | 
        try {
            ApiResponse<MoveAccountToProfile200Response> response = apiInstance.moveAccountToProfileWithHttpInfo(accountId, moveAccountToProfileRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#moveAccountToProfile");
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
| **moveAccountToProfileRequest** | [**MoveAccountToProfileRequest**](MoveAccountToProfileRequest.md)|  | |

### Return type

ApiResponse<[**MoveAccountToProfile200Response**](MoveAccountToProfile200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account moved |  -  |
| **400** | Missing or invalid profileId |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | API key does not have access to the source account or target profile |  -  |
| **404** | Account or target profile not found |  -  |


## revokeBusinessPartner

> RevokeBusinessPartner200Response revokeBusinessPartner(accountId, businessId)

Revoke a partner business from the Page

Removes every task the partner business portfolio held on the Page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id of the Facebook or Instagram account.
        String businessId = "businessId_example"; // String | Meta business portfolio id of the partner (numeric string).
        try {
            RevokeBusinessPartner200Response result = apiInstance.revokeBusinessPartner(accountId, businessId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#revokeBusinessPartner");
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
| **accountId** | **String**| Zernio SocialAccount id of the Facebook or Instagram account. | |
| **businessId** | **String**| Meta business portfolio id of the partner (numeric string). | |

### Return type

[**RevokeBusinessPartner200Response**](RevokeBusinessPartner200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Access revoked |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Meta refused: the connecting user lacks business_management or is not an admin of the owning portfolio. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | No Facebook Page is linked to the account. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## revokeBusinessPartnerWithHttpInfo

> ApiResponse<RevokeBusinessPartner200Response> revokeBusinessPartner revokeBusinessPartnerWithHttpInfo(accountId, businessId)

Revoke a partner business from the Page

Removes every task the partner business portfolio held on the Page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id of the Facebook or Instagram account.
        String businessId = "businessId_example"; // String | Meta business portfolio id of the partner (numeric string).
        try {
            ApiResponse<RevokeBusinessPartner200Response> response = apiInstance.revokeBusinessPartnerWithHttpInfo(accountId, businessId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#revokeBusinessPartner");
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
| **accountId** | **String**| Zernio SocialAccount id of the Facebook or Instagram account. | |
| **businessId** | **String**| Meta business portfolio id of the partner (numeric string). | |

### Return type

ApiResponse<[**RevokeBusinessPartner200Response**](RevokeBusinessPartner200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Access revoked |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Meta refused: the connecting user lacks business_management or is not an admin of the owning portfolio. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | No Facebook Page is linked to the account. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  Google Ads: writes and reports run on one developer token shared by every Google Ads account on Zernio. The token holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. The envelope has &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed.  Meta ads: every Meta throttle (codes 4, 17, 32, 613 and the business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta itself answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when Meta sends one, otherwise it is Meta&#39;s documented 60-second minimum (30 seconds for the one-write-per-30-seconds limit on a single object).  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## searchTikTokLocations

> SearchTikTokLocations200Response searchTikTokLocations(accountId, query)

Search TikTok location tags

Searches the location tags a TikTok account connected through the TikTok for Business app can attach to a video post. Send a result&#39;s id and name as tiktokSettings.locationId and locationName when creating a post. TikTok answers the 20 closest matches and fills the list with fuzzy matches when nothing matches, so an unrelated result does not mean the place is missing.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The TikTok account ID
        String query = "query_example"; // String | Place name to search, for example a city, a venue or an address
        try {
            SearchTikTokLocations200Response result = apiInstance.searchTikTokLocations(accountId, query);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#searchTikTokLocations");
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
| **accountId** | **String**| The TikTok account ID | |
| **query** | **String**| Place name to search, for example a city, a venue or an address | |

### Return type

[**SearchTikTokLocations200Response**](SearchTikTokLocations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The closest location tags, best match first |  -  |
| **400** | Invalid request |  -  |
| **404** | Account not found |  -  |

## searchTikTokLocationsWithHttpInfo

> ApiResponse<SearchTikTokLocations200Response> searchTikTokLocations searchTikTokLocationsWithHttpInfo(accountId, query)

Search TikTok location tags

Searches the location tags a TikTok account connected through the TikTok for Business app can attach to a video post. Send a result&#39;s id and name as tiktokSettings.locationId and locationName when creating a post. TikTok answers the 20 closest matches and fills the list with fuzzy matches when nothing matches, so an unrelated result does not mean the place is missing.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The TikTok account ID
        String query = "query_example"; // String | Place name to search, for example a city, a venue or an address
        try {
            ApiResponse<SearchTikTokLocations200Response> response = apiInstance.searchTikTokLocationsWithHttpInfo(accountId, query);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#searchTikTokLocations");
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
| **accountId** | **String**| The TikTok account ID | |
| **query** | **String**| Place name to search, for example a city, a venue or an address | |

### Return type

ApiResponse<[**SearchTikTokLocations200Response**](SearchTikTokLocations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The closest location tags, best match first |  -  |
| **400** | Invalid request |  -  |
| **404** | Account not found |  -  |


## updateAccount

> UpdateAccount200Response updateAccount(accountId, updateAccountRequest)

Update account

Updates a connected account&#39;s display name or username override.  For X accounts on usage-based billing, also accepts an &#x60;xCapabilities&#x60; object to toggle background API operations that incur X API pass-through costs. Both fields are opt-in (default &#x60;false&#x60;). When off, no analytics syncs or DM polling are performed for that account, and no API call is metered for those operations. Publishing and deleting posts are always available regardless of these toggles. Setting &#x60;xCapabilities&#x60; on a non-X account returns 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateAccountRequest updateAccountRequest = new UpdateAccountRequest(); // UpdateAccountRequest | 
        try {
            UpdateAccount200Response result = apiInstance.updateAccount(accountId, updateAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#updateAccount");
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
| **updateAccountRequest** | [**UpdateAccountRequest**](UpdateAccountRequest.md)|  | |

### Return type

[**UpdateAccount200Response**](UpdateAccount200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **400** | Invalid request (e.g. xCapabilities on a non-X account) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## updateAccountWithHttpInfo

> ApiResponse<UpdateAccount200Response> updateAccount updateAccountWithHttpInfo(accountId, updateAccountRequest)

Update account

Updates a connected account&#39;s display name or username override.  For X accounts on usage-based billing, also accepts an &#x60;xCapabilities&#x60; object to toggle background API operations that incur X API pass-through costs. Both fields are opt-in (default &#x60;false&#x60;). When off, no analytics syncs or DM polling are performed for that account, and no API call is metered for those operations. Publishing and deleting posts are always available regardless of these toggles. Setting &#x60;xCapabilities&#x60; on a non-X account returns 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateAccountRequest updateAccountRequest = new UpdateAccountRequest(); // UpdateAccountRequest | 
        try {
            ApiResponse<UpdateAccount200Response> response = apiInstance.updateAccountWithHttpInfo(accountId, updateAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#updateAccount");
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
| **updateAccountRequest** | [**UpdateAccountRequest**](UpdateAccountRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAccount200Response**](UpdateAccount200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **400** | Invalid request (e.g. xCapabilities on a non-X account) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## updateBlueskySettings

> void updateBlueskySettings(accountId, updateBlueskySettingsRequest)

Update Bluesky account settings

Set or clear the account&#39;s default post languages. 1-3 BCP-47 codes (e.g. \&quot;pt\&quot;, \&quot;en-US\&quot;), the same validation as per-post langs; explicit null clears the default. Per-post platformSpecificData.langs always overrides this default. Applies to posts published after the change; already-published posts cannot be retagged (Bluesky has no post edit).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateBlueskySettingsRequest updateBlueskySettingsRequest = new UpdateBlueskySettingsRequest(); // UpdateBlueskySettingsRequest | 
        try {
            apiInstance.updateBlueskySettings(accountId, updateBlueskySettingsRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#updateBlueskySettings");
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
| **updateBlueskySettingsRequest** | [**UpdateBlueskySettingsRequest**](UpdateBlueskySettingsRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |

## updateBlueskySettingsWithHttpInfo

> ApiResponse<Void> updateBlueskySettings updateBlueskySettingsWithHttpInfo(accountId, updateBlueskySettingsRequest)

Update Bluesky account settings

Set or clear the account&#39;s default post languages. 1-3 BCP-47 codes (e.g. \&quot;pt\&quot;, \&quot;en-US\&quot;), the same validation as per-post langs; explicit null clears the default. Per-post platformSpecificData.langs always overrides this default. Applies to posts published after the change; already-published posts cannot be retagged (Bluesky has no post edit).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateBlueskySettingsRequest updateBlueskySettingsRequest = new UpdateBlueskySettingsRequest(); // UpdateBlueskySettingsRequest | 
        try {
            ApiResponse<Void> response = apiInstance.updateBlueskySettingsWithHttpInfo(accountId, updateBlueskySettingsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#updateBlueskySettings");
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
| **updateBlueskySettingsRequest** | [**UpdateBlueskySettingsRequest**](UpdateBlueskySettingsRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |


## updateSlackSettings

> void updateSlackSettings(accountId, updateSlackSettingsRequest)

Update Slack account settings

Set or clear the default message identity for this channel. Empty string clears a field; per-post platformSpecificData.username/iconUrl still override these defaults.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateSlackSettingsRequest updateSlackSettingsRequest = new UpdateSlackSettingsRequest(); // UpdateSlackSettingsRequest | 
        try {
            apiInstance.updateSlackSettings(accountId, updateSlackSettingsRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#updateSlackSettings");
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
| **updateSlackSettingsRequest** | [**UpdateSlackSettingsRequest**](UpdateSlackSettingsRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |

## updateSlackSettingsWithHttpInfo

> ApiResponse<Void> updateSlackSettings updateSlackSettingsWithHttpInfo(accountId, updateSlackSettingsRequest)

Update Slack account settings

Set or clear the default message identity for this channel. Empty string clears a field; per-post platformSpecificData.username/iconUrl still override these defaults.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateSlackSettingsRequest updateSlackSettingsRequest = new UpdateSlackSettingsRequest(); // UpdateSlackSettingsRequest | 
        try {
            ApiResponse<Void> response = apiInstance.updateSlackSettingsWithHttpInfo(accountId, updateSlackSettingsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#updateSlackSettings");
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
| **updateSlackSettingsRequest** | [**UpdateSlackSettingsRequest**](UpdateSlackSettingsRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Account not found |  -  |

