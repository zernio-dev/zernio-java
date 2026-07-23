# AdAccountsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAdAccountFinance**](AdAccountsApi.md#getAdAccountFinance) | **GET** /v1/ads/accounts/finance | Ad account finances |
| [**getAdAccountFinanceWithHttpInfo**](AdAccountsApi.md#getAdAccountFinanceWithHttpInfo) | **GET** /v1/ads/accounts/finance | Ad account finances |
| [**getAdComments**](AdAccountsApi.md#getAdComments) | **GET** /v1/ads/{adId}/comments | List comments on an ad |
| [**getAdCommentsWithHttpInfo**](AdAccountsApi.md#getAdCommentsWithHttpInfo) | **GET** /v1/ads/{adId}/comments | List comments on an ad |
| [**getAdsActivityLog**](AdAccountsApi.md#getAdsActivityLog) | **GET** /v1/ads/activity | Ad account change / audit log |
| [**getAdsActivityLogWithHttpInfo**](AdAccountsApi.md#getAdsActivityLogWithHttpInfo) | **GET** /v1/ads/activity | Ad account change / audit log |
| [**getDsaDefaults**](AdAccountsApi.md#getDsaDefaults) | **GET** /v1/ads/dsa-defaults | Get ad account DSA defaults |
| [**getDsaDefaultsWithHttpInfo**](AdAccountsApi.md#getDsaDefaultsWithHttpInfo) | **GET** /v1/ads/dsa-defaults | Get ad account DSA defaults |
| [**getDsaRecommendations**](AdAccountsApi.md#getDsaRecommendations) | **GET** /v1/ads/dsa-recommendations | List DSA beneficiary/payor suggestions |
| [**getDsaRecommendationsWithHttpInfo**](AdAccountsApi.md#getDsaRecommendationsWithHttpInfo) | **GET** /v1/ads/dsa-recommendations | List DSA beneficiary/payor suggestions |
| [**listAdAccounts**](AdAccountsApi.md#listAdAccounts) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdAccountsWithHttpInfo**](AdAccountsApi.md#listAdAccountsWithHttpInfo) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdLabels**](AdAccountsApi.md#listAdLabels) | **GET** /v1/ads/labels | Ad labels |
| [**listAdLabelsWithHttpInfo**](AdAccountsApi.md#listAdLabelsWithHttpInfo) | **GET** /v1/ads/labels | Ad labels |
| [**listAdStudies**](AdAccountsApi.md#listAdStudies) | **GET** /v1/ads/studies | A/B tests and lift studies |
| [**listAdStudiesWithHttpInfo**](AdAccountsApi.md#listAdStudiesWithHttpInfo) | **GET** /v1/ads/studies | A/B tests and lift studies |
| [**listAdsBusinessCenters**](AdAccountsApi.md#listAdsBusinessCenters) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listAdsBusinessCentersWithHttpInfo**](AdAccountsApi.md#listAdsBusinessCentersWithHttpInfo) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listHighDemandPeriods**](AdAccountsApi.md#listHighDemandPeriods) | **GET** /v1/ads/high-demand-periods | High demand periods / budget schedules |
| [**listHighDemandPeriodsWithHttpInfo**](AdAccountsApi.md#listHighDemandPeriodsWithHttpInfo) | **GET** /v1/ads/high-demand-periods | High demand periods / budget schedules |
| [**listMetaBusinesses**](AdAccountsApi.md#listMetaBusinesses) | **GET** /v1/ads/businesses | Businesses list |
| [**listMetaBusinessesWithHttpInfo**](AdAccountsApi.md#listMetaBusinessesWithHttpInfo) | **GET** /v1/ads/businesses | Businesses list |
| [**updateAdAccount**](AdAccountsApi.md#updateAdAccount) | **PATCH** /v1/ads/accounts | Update ad account settings |
| [**updateAdAccountWithHttpInfo**](AdAccountsApi.md#updateAdAccountWithHttpInfo) | **PATCH** /v1/ads/accounts | Update ad account settings |



## getAdAccountFinance

> GetAdAccountFinance200Response getAdAccountFinance(accountId, adAccountId)

Ad account finances

Finances of one Meta ad account: prepaid &#x60;balance&#x60;, lifetime &#x60;amountSpent&#x60;, account &#x60;spendCap&#x60; (null &#x3D; no cap) and the &#x60;fundingSource&#x60;. Money values are converted from Meta&#39;s minor units to whole units of &#x60;currency&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        try {
            GetAdAccountFinance200Response result = apiInstance.getAdAccountFinance(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdAccountFinance");
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

### Return type

[**GetAdAccountFinance200Response**](GetAdAccountFinance200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account finances |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdAccountFinanceWithHttpInfo

> ApiResponse<GetAdAccountFinance200Response> getAdAccountFinance getAdAccountFinanceWithHttpInfo(accountId, adAccountId)

Ad account finances

Finances of one Meta ad account: prepaid &#x60;balance&#x60;, lifetime &#x60;amountSpent&#x60;, account &#x60;spendCap&#x60; (null &#x3D; no cap) and the &#x60;fundingSource&#x60;. Money values are converted from Meta&#39;s minor units to whole units of &#x60;currency&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        try {
            ApiResponse<GetAdAccountFinance200Response> response = apiInstance.getAdAccountFinanceWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdAccountFinance");
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

### Return type

ApiResponse<[**GetAdAccountFinance200Response**](GetAdAccountFinance200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account finances |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdComments

> GetAdComments200Response getAdComments(adId, placement, limit, cursor)

List comments on an ad

Returns comments on an ad&#39;s underlying creative post. Useful for moderating or analyzing engagement on dark posts (ad creatives that never went live organically), which the regular GET /v1/inbox/comments/{postId} endpoint cannot serve because dark posts are not in Zernio&#39;s post database.  An ad that runs on both Facebook feed and Instagram feed has two separate underlying posts with separate comment threads (the creative&#39;s effective_object_story_id and effective_instagram_media_id). Use the &#x60;placement&#x60; query param to pick one; with no param the Instagram side is returned when it exists, otherwise Facebook. The identifiers are read from the ad record (persisted during sync) with a Marketing-API fallback for ads that predate the field.  For Instagram-placed comments, the Instagram account that runs the ad must be connected to Zernio — those comments are read through that account&#39;s token. If no connected Instagram account on the profile can read the ad&#39;s media, the call returns ads_connection_required (the Facebook side, if any, is still readable via ?placement&#x3D;facebook).  Meta-only. Other ad platforms (TikTok, LinkedIn, Pinterest, Google, X) do not expose a public per-ad comments API and return feature_not_available.  Requires the Ads add-on. Response shape matches GET /v1/inbox/comments/{postId}.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: Zernio internal &#x60;_id&#x60; (24-char hex), Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;), or the creative&#39;s &#x60;effective_object_story_id&#x60; / &#x60;effective_instagram_media_id&#x60;. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String adId = "adId_example"; // String | Internal Zernio ad ID (ObjectId).
        String placement = "facebook"; // String | Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response.
        try {
            GetAdComments200Response result = apiInstance.getAdComments(adId, placement, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdComments");
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
| **adId** | **String**| Internal Zernio ad ID (ObjectId). | |
| **placement** | **String**| Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement. | [optional] [enum: facebook, instagram] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| Pagination cursor from a previous response. | [optional] |

### Return type

[**GetAdComments200Response**](GetAdComments200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments on the ad |  -  |
| **400** | Invalid ad ID format, or the ad&#39;s creative format does not expose a commentable underlying post (code ad_not_commentable).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included by default on usage-based plans), or ad platform is not Meta (code feature_not_available). |  -  |
| **404** | Resource not found |  -  |
| **422** | Ads account token unavailable, or (for Instagram-placed ads) no connected Instagram account on the profile can read the ad&#39;s media (code ads_connection_required).  |  -  |

## getAdCommentsWithHttpInfo

> ApiResponse<GetAdComments200Response> getAdComments getAdCommentsWithHttpInfo(adId, placement, limit, cursor)

List comments on an ad

Returns comments on an ad&#39;s underlying creative post. Useful for moderating or analyzing engagement on dark posts (ad creatives that never went live organically), which the regular GET /v1/inbox/comments/{postId} endpoint cannot serve because dark posts are not in Zernio&#39;s post database.  An ad that runs on both Facebook feed and Instagram feed has two separate underlying posts with separate comment threads (the creative&#39;s effective_object_story_id and effective_instagram_media_id). Use the &#x60;placement&#x60; query param to pick one; with no param the Instagram side is returned when it exists, otherwise Facebook. The identifiers are read from the ad record (persisted during sync) with a Marketing-API fallback for ads that predate the field.  For Instagram-placed comments, the Instagram account that runs the ad must be connected to Zernio — those comments are read through that account&#39;s token. If no connected Instagram account on the profile can read the ad&#39;s media, the call returns ads_connection_required (the Facebook side, if any, is still readable via ?placement&#x3D;facebook).  Meta-only. Other ad platforms (TikTok, LinkedIn, Pinterest, Google, X) do not expose a public per-ad comments API and return feature_not_available.  Requires the Ads add-on. Response shape matches GET /v1/inbox/comments/{postId}.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: Zernio internal &#x60;_id&#x60; (24-char hex), Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;), or the creative&#39;s &#x60;effective_object_story_id&#x60; / &#x60;effective_instagram_media_id&#x60;. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String adId = "adId_example"; // String | Internal Zernio ad ID (ObjectId).
        String placement = "facebook"; // String | Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response.
        try {
            ApiResponse<GetAdComments200Response> response = apiInstance.getAdCommentsWithHttpInfo(adId, placement, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdComments");
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
| **adId** | **String**| Internal Zernio ad ID (ObjectId). | |
| **placement** | **String**| Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement. | [optional] [enum: facebook, instagram] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| Pagination cursor from a previous response. | [optional] |

### Return type

ApiResponse<[**GetAdComments200Response**](GetAdComments200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments on the ad |  -  |
| **400** | Invalid ad ID format, or the ad&#39;s creative format does not expose a commentable underlying post (code ad_not_commentable).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included by default on usage-based plans), or ad platform is not Meta (code feature_not_available). |  -  |
| **404** | Resource not found |  -  |
| **422** | Ads account token unavailable, or (for Instagram-placed ads) no connected Instagram account on the profile can read the ad&#39;s media (code ads_connection_required).  |  -  |


## getAdsActivityLog

> GetAdsActivityLog200Response getAdsActivityLog(accountId, adAccountId, since, until, objectId, limit, after)

Ad account change / audit log

Account-level audit log from Meta&#39;s &#x60;/act_X/activities&#x60;: who changed what and when (creates, edits, status flips, budget changes...) with Meta&#39;s translated event names and the structured before/after in &#x60;extra_data&#x60;. Rows are returned verbatim. Meta has no server-side per-object filter on this edge, so &#x60;objectId&#x60; filters the returned page client-side (combine with paging to walk history for one campaign/ad set/ad).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        LocalDate since = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD).
        LocalDate until = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD).
        String objectId = "objectId_example"; // String | Client-side filter to one Meta object id (campaign, ad set or ad).
        Integer limit = 50; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            GetAdsActivityLog200Response result = apiInstance.getAdsActivityLog(accountId, adAccountId, since, until, objectId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdsActivityLog");
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
| **since** | **LocalDate**| Start of range (YYYY-MM-DD). | [optional] |
| **until** | **LocalDate**| End of range (YYYY-MM-DD). | [optional] |
| **objectId** | **String**| Client-side filter to one Meta object id (campaign, ad set or ad). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 50] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**GetAdsActivityLog200Response**](GetAdsActivityLog200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity rows (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdsActivityLogWithHttpInfo

> ApiResponse<GetAdsActivityLog200Response> getAdsActivityLog getAdsActivityLogWithHttpInfo(accountId, adAccountId, since, until, objectId, limit, after)

Ad account change / audit log

Account-level audit log from Meta&#39;s &#x60;/act_X/activities&#x60;: who changed what and when (creates, edits, status flips, budget changes...) with Meta&#39;s translated event names and the structured before/after in &#x60;extra_data&#x60;. Rows are returned verbatim. Meta has no server-side per-object filter on this edge, so &#x60;objectId&#x60; filters the returned page client-side (combine with paging to walk history for one campaign/ad set/ad).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        LocalDate since = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD).
        LocalDate until = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD).
        String objectId = "objectId_example"; // String | Client-side filter to one Meta object id (campaign, ad set or ad).
        Integer limit = 50; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<GetAdsActivityLog200Response> response = apiInstance.getAdsActivityLogWithHttpInfo(accountId, adAccountId, since, until, objectId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdsActivityLog");
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
| **since** | **LocalDate**| Start of range (YYYY-MM-DD). | [optional] |
| **until** | **LocalDate**| End of range (YYYY-MM-DD). | [optional] |
| **objectId** | **String**| Client-side filter to one Meta object id (campaign, ad set or ad). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 50] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**GetAdsActivityLog200Response**](GetAdsActivityLog200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity rows (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getDsaDefaults

> UpdateAdAccount200Response getDsaDefaults(accountId, adAccountId)

Get ad account DSA defaults

Returns the default DSA beneficiary and payor currently set on a Meta ad account, whether they were set via &#x60;PATCH /v1/ads/accounts&#x60; or in Meta Ads Manager. Fields are omitted when no default is configured. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            UpdateAdAccount200Response result = apiInstance.getDsaDefaults(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getDsaDefaults");
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
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current DSA defaults (empty object when none are set) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |

## getDsaDefaultsWithHttpInfo

> ApiResponse<UpdateAdAccount200Response> getDsaDefaults getDsaDefaultsWithHttpInfo(accountId, adAccountId)

Get ad account DSA defaults

Returns the default DSA beneficiary and payor currently set on a Meta ad account, whether they were set via &#x60;PATCH /v1/ads/accounts&#x60; or in Meta Ads Manager. Fields are omitted when no default is configured. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ApiResponse<UpdateAdAccount200Response> response = apiInstance.getDsaDefaultsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getDsaDefaults");
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
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

ApiResponse<[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current DSA defaults (empty object when none are set) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |


## getDsaRecommendations

> GetDsaRecommendations200Response getDsaRecommendations(accountId, adAccountId)

List DSA beneficiary/payor suggestions

Returns Meta&#39;s suggested beneficiary/payor names for an ad account, derived by Meta from the account&#39;s recent activity. Useful for prefilling &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60; inputs, or the defaults sent to &#x60;PATCH /v1/ads/accounts&#x60;, in your own UI.  Meta returns a single flat list. Entries are not labeled as beneficiary or payor, and since these are legal disclosures Zernio never applies them automatically: let your user pick the right entity. The list may be empty for accounts with little activity. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            GetDsaRecommendations200Response result = apiInstance.getDsaRecommendations(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getDsaRecommendations");
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
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

[**GetDsaRecommendations200Response**](GetDsaRecommendations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Suggested DSA strings (may be empty when Meta has no recommendations) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |

## getDsaRecommendationsWithHttpInfo

> ApiResponse<GetDsaRecommendations200Response> getDsaRecommendations getDsaRecommendationsWithHttpInfo(accountId, adAccountId)

List DSA beneficiary/payor suggestions

Returns Meta&#39;s suggested beneficiary/payor names for an ad account, derived by Meta from the account&#39;s recent activity. Useful for prefilling &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60; inputs, or the defaults sent to &#x60;PATCH /v1/ads/accounts&#x60;, in your own UI.  Meta returns a single flat list. Entries are not labeled as beneficiary or payor, and since these are legal disclosures Zernio never applies them automatically: let your user pick the right entity. The list may be empty for accounts with little activity. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ApiResponse<GetDsaRecommendations200Response> response = apiInstance.getDsaRecommendationsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getDsaRecommendations");
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
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

ApiResponse<[**GetDsaRecommendations200Response**](GetDsaRecommendations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Suggested DSA strings (may be empty when Meta has no recommendations) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |


## listAdAccounts

> ListAdAccounts200Response listAdAccounts(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given social account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs).  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Filter response to a single platform ad account ID (e.g. `act_123` for Meta, advertiser_id for TikTok). Returns at most one item.
        Integer limit = 56; // Integer | Clamp the returned `accounts[]` length. Useful for typeahead pickers on agency tokens with hundreds of advertisers.
        try {
            ListAdAccounts200Response result = apiInstance.listAdAccounts(accountId, adAccountId, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdAccounts");
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
| **accountId** | **String**| Social account ID | |
| **adAccountId** | **String**| Filter response to a single platform ad account ID (e.g. &#x60;act_123&#x60; for Meta, advertiser_id for TikTok). Returns at most one item. | [optional] |
| **limit** | **Integer**| Clamp the returned &#x60;accounts[]&#x60; length. Useful for typeahead pickers on agency tokens with hundreds of advertisers. | [optional] |

### Return type

[**ListAdAccounts200Response**](ListAdAccounts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad accounts |  -  |
| **401** | Unauthorized |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or Instagram missing linked Facebook account |  -  |

## listAdAccountsWithHttpInfo

> ApiResponse<ListAdAccounts200Response> listAdAccounts listAdAccountsWithHttpInfo(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given social account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs).  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Filter response to a single platform ad account ID (e.g. `act_123` for Meta, advertiser_id for TikTok). Returns at most one item.
        Integer limit = 56; // Integer | Clamp the returned `accounts[]` length. Useful for typeahead pickers on agency tokens with hundreds of advertisers.
        try {
            ApiResponse<ListAdAccounts200Response> response = apiInstance.listAdAccountsWithHttpInfo(accountId, adAccountId, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdAccounts");
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
| **accountId** | **String**| Social account ID | |
| **adAccountId** | **String**| Filter response to a single platform ad account ID (e.g. &#x60;act_123&#x60; for Meta, advertiser_id for TikTok). Returns at most one item. | [optional] |
| **limit** | **Integer**| Clamp the returned &#x60;accounts[]&#x60; length. Useful for typeahead pickers on agency tokens with hundreds of advertisers. | [optional] |

### Return type

ApiResponse<[**ListAdAccounts200Response**](ListAdAccounts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad accounts |  -  |
| **401** | Unauthorized |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or Instagram missing linked Facebook account |  -  |


## listAdLabels

> ListAdLabels200Response listAdLabels(accountId, adAccountId, limit, after)

Ad labels

Lists the ad account&#39;s organizational labels (Meta&#39;s &#x60;/act_X/adlabels&#x60;), rows returned verbatim (id, name, created/updated time).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdLabels200Response result = apiInstance.listAdLabels(accountId, adAccountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdLabels");
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
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdLabels200Response**](ListAdLabels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad labels (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdLabelsWithHttpInfo

> ApiResponse<ListAdLabels200Response> listAdLabels listAdLabelsWithHttpInfo(accountId, adAccountId, limit, after)

Ad labels

Lists the ad account&#39;s organizational labels (Meta&#39;s &#x60;/act_X/adlabels&#x60;), rows returned verbatim (id, name, created/updated time).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdLabels200Response> response = apiInstance.listAdLabelsWithHttpInfo(accountId, adAccountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdLabels");
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
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdLabels200Response**](ListAdLabels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad labels (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdStudies

> ListAdStudies200Response listAdStudies(accountId, adAccountId, fields, limit, after)

A/B tests and lift studies

Lists the ad account&#39;s A/B tests and lift studies (Meta&#39;s &#x60;/act_X/ad_studies&#x60;), rows returned verbatim. The default projection covers id, name, type, timing and cells with split percentages; &#x60;fields&#x60; is a raw-passthrough override.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdStudies200Response result = apiInstance.listAdStudies(accountId, adAccountId, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdStudies");
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

[**ListAdStudies200Response**](ListAdStudies200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad studies (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdStudiesWithHttpInfo

> ApiResponse<ListAdStudies200Response> listAdStudies listAdStudiesWithHttpInfo(accountId, adAccountId, fields, limit, after)

A/B tests and lift studies

Lists the ad account&#39;s A/B tests and lift studies (Meta&#39;s &#x60;/act_X/ad_studies&#x60;), rows returned verbatim. The default projection covers id, name, type, timing and cells with split percentages; &#x60;fields&#x60; is a raw-passthrough override.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdStudies200Response> response = apiInstance.listAdStudiesWithHttpInfo(accountId, adAccountId, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdStudies");
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

ApiResponse<[**ListAdStudies200Response**](ListAdStudies200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad studies (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdsBusinessCenters

> ListAdsBusinessCenters200Response listAdsBusinessCenters(accountId)

List TikTok Business Centers

Returns the TikTok Business Centers (BCs) the connected &#x60;tiktokads&#x60; account can read. Each BC reports its advertiser count so callers can build agency-style pickers without re-walking &#x60;/v1/ads/accounts&#x60; per BC.  TikTok-only. Solo advertisers (non-agency tokens) return an empty array. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | ID of the `tiktokads` (or parent `tiktok` posting) SocialAccount
        try {
            ListAdsBusinessCenters200Response result = apiInstance.listAdsBusinessCenters(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdsBusinessCenters");
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
| **accountId** | **String**| ID of the &#x60;tiktokads&#x60; (or parent &#x60;tiktok&#x60; posting) SocialAccount | |

### Return type

[**ListAdsBusinessCenters200Response**](ListAdsBusinessCenters200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business centers |  -  |
| **401** | Unauthorized |  -  |
| **404** | TikTok account not found |  -  |
| **422** | TikTok Ads not connected |  -  |

## listAdsBusinessCentersWithHttpInfo

> ApiResponse<ListAdsBusinessCenters200Response> listAdsBusinessCenters listAdsBusinessCentersWithHttpInfo(accountId)

List TikTok Business Centers

Returns the TikTok Business Centers (BCs) the connected &#x60;tiktokads&#x60; account can read. Each BC reports its advertiser count so callers can build agency-style pickers without re-walking &#x60;/v1/ads/accounts&#x60; per BC.  TikTok-only. Solo advertisers (non-agency tokens) return an empty array. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | ID of the `tiktokads` (or parent `tiktok` posting) SocialAccount
        try {
            ApiResponse<ListAdsBusinessCenters200Response> response = apiInstance.listAdsBusinessCentersWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdsBusinessCenters");
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
| **accountId** | **String**| ID of the &#x60;tiktokads&#x60; (or parent &#x60;tiktok&#x60; posting) SocialAccount | |

### Return type

ApiResponse<[**ListAdsBusinessCenters200Response**](ListAdsBusinessCenters200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business centers |  -  |
| **401** | Unauthorized |  -  |
| **404** | TikTok account not found |  -  |
| **422** | TikTok Ads not connected |  -  |


## listHighDemandPeriods

> ListHighDemandPeriods200Response listHighDemandPeriods(accountId, campaignId, adSetId, limit, after)

High demand periods / budget schedules

Scheduled budget increases (Meta&#39;s budget-scheduling API). The Graph edge lives on the campaign and ad-set nodes only, so exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60; (platform ids) is required. Rows returned verbatim (budget_value, budget_value_type, time window, recurrence).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String campaignId = "campaignId_example"; // String | Platform campaign id. Exactly one of campaignId / adSetId.
        String adSetId = "adSetId_example"; // String | Platform ad set id. Exactly one of campaignId / adSetId.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListHighDemandPeriods200Response result = apiInstance.listHighDemandPeriods(accountId, campaignId, adSetId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listHighDemandPeriods");
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
| **campaignId** | **String**| Platform campaign id. Exactly one of campaignId / adSetId. | [optional] |
| **adSetId** | **String**| Platform ad set id. Exactly one of campaignId / adSetId. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListHighDemandPeriods200Response**](ListHighDemandPeriods200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budget schedules (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listHighDemandPeriodsWithHttpInfo

> ApiResponse<ListHighDemandPeriods200Response> listHighDemandPeriods listHighDemandPeriodsWithHttpInfo(accountId, campaignId, adSetId, limit, after)

High demand periods / budget schedules

Scheduled budget increases (Meta&#39;s budget-scheduling API). The Graph edge lives on the campaign and ad-set nodes only, so exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60; (platform ids) is required. Rows returned verbatim (budget_value, budget_value_type, time window, recurrence).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String campaignId = "campaignId_example"; // String | Platform campaign id. Exactly one of campaignId / adSetId.
        String adSetId = "adSetId_example"; // String | Platform ad set id. Exactly one of campaignId / adSetId.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListHighDemandPeriods200Response> response = apiInstance.listHighDemandPeriodsWithHttpInfo(accountId, campaignId, adSetId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listHighDemandPeriods");
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
| **campaignId** | **String**| Platform campaign id. Exactly one of campaignId / adSetId. | [optional] |
| **adSetId** | **String**| Platform ad set id. Exactly one of campaignId / adSetId. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListHighDemandPeriods200Response**](ListHighDemandPeriods200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budget schedules (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listMetaBusinesses

> ListMetaBusinesses200Response listMetaBusinesses(accountId, limit, after)

Businesses list

Business Manager portfolios the connected Meta user belongs to (Meta&#39;s &#x60;/me/businesses&#x60;), rows returned verbatim (id, name, verification_status, created_time). Token-scoped, so no &#x60;adAccountId&#x60; is needed. For TikTok Business Centers use &#x60;GET /v1/ads/business-centers&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListMetaBusinesses200Response result = apiInstance.listMetaBusinesses(accountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listMetaBusinesses");
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
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListMetaBusinesses200Response**](ListMetaBusinesses200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Businesses (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listMetaBusinessesWithHttpInfo

> ApiResponse<ListMetaBusinesses200Response> listMetaBusinesses listMetaBusinessesWithHttpInfo(accountId, limit, after)

Businesses list

Business Manager portfolios the connected Meta user belongs to (Meta&#39;s &#x60;/me/businesses&#x60;), rows returned verbatim (id, name, verification_status, created_time). Token-scoped, so no &#x60;adAccountId&#x60; is needed. For TikTok Business Centers use &#x60;GET /v1/ads/business-centers&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListMetaBusinesses200Response> response = apiInstance.listMetaBusinessesWithHttpInfo(accountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listMetaBusinesses");
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
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListMetaBusinesses200Response**](ListMetaBusinesses200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Businesses (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## updateAdAccount

> UpdateAdAccount200Response updateAdAccount(updateAdAccountRequest)

Update ad account settings

Sets the default DSA beneficiary and payor on a Meta ad account (EU DSA, Article 26). Set them once and every EU-targeted call to &#x60;/v1/ads/create&#x60;, &#x60;/v1/ads/boost&#x60; and &#x60;/v1/ads/ctwa&#x60; on that ad account can omit &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60;: Meta applies the defaults automatically.  The values are written to the ad account on Meta, the same setting Ads Manager edits. Nothing is stored in Zernio, and defaults already set in Ads Manager work identically. Zernio never guesses these values for you. Beneficiary and payor are legal disclosures shown to EU users, so you must provide the entity names explicitly. Use &#x60;GET /v1/ads/dsa-recommendations&#x60; to offer suggestions in your UI.  If &#x60;defaultDsaPayor&#x60; is omitted, the beneficiary is also set as the payor, which covers the common case where the same entity benefits from and pays for the ads. Read the current values back with &#x60;GET /v1/ads/dsa-defaults&#x60;.  Currently supported for Meta accounts only; other platforms return 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        UpdateAdAccountRequest updateAdAccountRequest = new UpdateAdAccountRequest(); // UpdateAdAccountRequest | 
        try {
            UpdateAdAccount200Response result = apiInstance.updateAdAccount(updateAdAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAdAccount");
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
| **updateAdAccountRequest** | [**UpdateAdAccountRequest**](UpdateAdAccountRequest.md)|  | |

### Return type

[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DSA defaults updated (re-read from Meta after the write) |  -  |
| **400** | Unsupported platform (non-Meta account) or invalid adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |

## updateAdAccountWithHttpInfo

> ApiResponse<UpdateAdAccount200Response> updateAdAccount updateAdAccountWithHttpInfo(updateAdAccountRequest)

Update ad account settings

Sets the default DSA beneficiary and payor on a Meta ad account (EU DSA, Article 26). Set them once and every EU-targeted call to &#x60;/v1/ads/create&#x60;, &#x60;/v1/ads/boost&#x60; and &#x60;/v1/ads/ctwa&#x60; on that ad account can omit &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60;: Meta applies the defaults automatically.  The values are written to the ad account on Meta, the same setting Ads Manager edits. Nothing is stored in Zernio, and defaults already set in Ads Manager work identically. Zernio never guesses these values for you. Beneficiary and payor are legal disclosures shown to EU users, so you must provide the entity names explicitly. Use &#x60;GET /v1/ads/dsa-recommendations&#x60; to offer suggestions in your UI.  If &#x60;defaultDsaPayor&#x60; is omitted, the beneficiary is also set as the payor, which covers the common case where the same entity benefits from and pays for the ads. Read the current values back with &#x60;GET /v1/ads/dsa-defaults&#x60;.  Currently supported for Meta accounts only; other platforms return 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAccountsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAccountsApi apiInstance = new AdAccountsApi(defaultClient);
        UpdateAdAccountRequest updateAdAccountRequest = new UpdateAdAccountRequest(); // UpdateAdAccountRequest | 
        try {
            ApiResponse<UpdateAdAccount200Response> response = apiInstance.updateAdAccountWithHttpInfo(updateAdAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAdAccount");
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
| **updateAdAccountRequest** | [**UpdateAdAccountRequest**](UpdateAdAccountRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DSA defaults updated (re-read from Meta after the write) |  -  |
| **400** | Unsupported platform (non-Meta account) or invalid adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |

