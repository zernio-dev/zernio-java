# AdCampaignsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAdKeywords**](AdCampaignsApi.md#addAdKeywords) | **POST** /v1/ads/keywords | Add Search keywords to an ad group |
| [**addAdKeywordsWithHttpInfo**](AdCampaignsApi.md#addAdKeywordsWithHttpInfo) | **POST** /v1/ads/keywords | Add Search keywords to an ad group |
| [**attachCampaignAssets**](AdCampaignsApi.md#attachCampaignAssets) | **POST** /v1/ads/campaigns/{campaignId}/assets | Attach extension assets to a Google Search campaign |
| [**attachCampaignAssetsWithHttpInfo**](AdCampaignsApi.md#attachCampaignAssetsWithHttpInfo) | **POST** /v1/ads/campaigns/{campaignId}/assets | Attach extension assets to a Google Search campaign |
| [**boostPost**](AdCampaignsApi.md#boostPost) | **POST** /v1/ads/boost | Boost post as ad |
| [**boostPostWithHttpInfo**](AdCampaignsApi.md#boostPostWithHttpInfo) | **POST** /v1/ads/boost | Boost post as ad |
| [**bulkUpdateAdCampaignStatus**](AdCampaignsApi.md#bulkUpdateAdCampaignStatus) | **POST** /v1/ads/campaigns/bulk-status | Pause or resume many campaigns |
| [**bulkUpdateAdCampaignStatusWithHttpInfo**](AdCampaignsApi.md#bulkUpdateAdCampaignStatusWithHttpInfo) | **POST** /v1/ads/campaigns/bulk-status | Pause or resume many campaigns |
| [**createAdCampaign**](AdCampaignsApi.md#createAdCampaign) | **POST** /v1/ads/campaigns | Create a standalone campaign |
| [**createAdCampaignWithHttpInfo**](AdCampaignsApi.md#createAdCampaignWithHttpInfo) | **POST** /v1/ads/campaigns | Create a standalone campaign |
| [**createAdSet**](AdCampaignsApi.md#createAdSet) | **POST** /v1/ads/ad-sets | Create a standalone ad group |
| [**createAdSetWithHttpInfo**](AdCampaignsApi.md#createAdSetWithHttpInfo) | **POST** /v1/ads/ad-sets | Create a standalone ad group |
| [**createBidStrategy**](AdCampaignsApi.md#createBidStrategy) | **POST** /v1/ads/bid-strategies | Create a Google Ads portfolio bid strategy |
| [**createBidStrategyWithHttpInfo**](AdCampaignsApi.md#createBidStrategyWithHttpInfo) | **POST** /v1/ads/bid-strategies | Create a Google Ads portfolio bid strategy |
| [**createStandaloneAd**](AdCampaignsApi.md#createStandaloneAd) | **POST** /v1/ads/create | Create standalone ad |
| [**createStandaloneAdWithHttpInfo**](AdCampaignsApi.md#createStandaloneAdWithHttpInfo) | **POST** /v1/ads/create | Create standalone ad |
| [**deleteAd**](AdCampaignsApi.md#deleteAd) | **DELETE** /v1/ads/{adId} | Cancel an ad |
| [**deleteAdWithHttpInfo**](AdCampaignsApi.md#deleteAdWithHttpInfo) | **DELETE** /v1/ads/{adId} | Cancel an ad |
| [**deleteAdCampaign**](AdCampaignsApi.md#deleteAdCampaign) | **DELETE** /v1/ads/campaigns/{campaignId} | Delete a campaign |
| [**deleteAdCampaignWithHttpInfo**](AdCampaignsApi.md#deleteAdCampaignWithHttpInfo) | **DELETE** /v1/ads/campaigns/{campaignId} | Delete a campaign |
| [**deleteAdSet**](AdCampaignsApi.md#deleteAdSet) | **DELETE** /v1/ads/ad-sets/{adSetId} | Delete an ad set |
| [**deleteAdSetWithHttpInfo**](AdCampaignsApi.md#deleteAdSetWithHttpInfo) | **DELETE** /v1/ads/ad-sets/{adSetId} | Delete an ad set |
| [**duplicateAd**](AdCampaignsApi.md#duplicateAd) | **POST** /v1/ads/{adId}/duplicate | Duplicate an ad |
| [**duplicateAdWithHttpInfo**](AdCampaignsApi.md#duplicateAdWithHttpInfo) | **POST** /v1/ads/{adId}/duplicate | Duplicate an ad |
| [**duplicateAdCampaign**](AdCampaignsApi.md#duplicateAdCampaign) | **POST** /v1/ads/campaigns/{campaignId}/duplicate | Duplicate a campaign |
| [**duplicateAdCampaignWithHttpInfo**](AdCampaignsApi.md#duplicateAdCampaignWithHttpInfo) | **POST** /v1/ads/campaigns/{campaignId}/duplicate | Duplicate a campaign |
| [**duplicateAdSet**](AdCampaignsApi.md#duplicateAdSet) | **POST** /v1/ads/ad-sets/{adSetId}/duplicate | Duplicate an ad set |
| [**duplicateAdSetWithHttpInfo**](AdCampaignsApi.md#duplicateAdSetWithHttpInfo) | **POST** /v1/ads/ad-sets/{adSetId}/duplicate | Duplicate an ad set |
| [**getAd**](AdCampaignsApi.md#getAd) | **GET** /v1/ads/{adId} | Get ad details |
| [**getAdWithHttpInfo**](AdCampaignsApi.md#getAdWithHttpInfo) | **GET** /v1/ads/{adId} | Get ad details |
| [**getAdSetDetails**](AdCampaignsApi.md#getAdSetDetails) | **GET** /v1/ads/ad-sets/{adSetId} | Live ad-set details incl. learning phase |
| [**getAdSetDetailsWithHttpInfo**](AdCampaignsApi.md#getAdSetDetailsWithHttpInfo) | **GET** /v1/ads/ad-sets/{adSetId} | Live ad-set details incl. learning phase |
| [**getAdTree**](AdCampaignsApi.md#getAdTree) | **GET** /v1/ads/tree | Get campaign tree |
| [**getAdTreeWithHttpInfo**](AdCampaignsApi.md#getAdTreeWithHttpInfo) | **GET** /v1/ads/tree | Get campaign tree |
| [**getAdsTimeline**](AdCampaignsApi.md#getAdsTimeline) | **GET** /v1/ads/timeline | Get daily account metrics |
| [**getAdsTimelineWithHttpInfo**](AdCampaignsApi.md#getAdsTimelineWithHttpInfo) | **GET** /v1/ads/timeline | Get daily account metrics |
| [**getCampaignBidding**](AdCampaignsApi.md#getCampaignBidding) | **GET** /v1/ads/campaigns/{campaignId}/bidding | Read a campaign&#39;s current bidding |
| [**getCampaignBiddingWithHttpInfo**](AdCampaignsApi.md#getCampaignBiddingWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/bidding | Read a campaign&#39;s current bidding |
| [**getCampaignTargeting**](AdCampaignsApi.md#getCampaignTargeting) | **GET** /v1/ads/campaigns/{campaignId}/targeting | Read a Google campaign&#39;s device, location, and language targeting |
| [**getCampaignTargetingWithHttpInfo**](AdCampaignsApi.md#getCampaignTargetingWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/targeting | Read a Google campaign&#39;s device, location, and language targeting |
| [**listAdCampaigns**](AdCampaignsApi.md#listAdCampaigns) | **GET** /v1/ads/campaigns | List campaigns |
| [**listAdCampaignsWithHttpInfo**](AdCampaignsApi.md#listAdCampaignsWithHttpInfo) | **GET** /v1/ads/campaigns | List campaigns |
| [**listAdKeywords**](AdCampaignsApi.md#listAdKeywords) | **GET** /v1/ads/keywords | List Search keywords |
| [**listAdKeywordsWithHttpInfo**](AdCampaignsApi.md#listAdKeywordsWithHttpInfo) | **GET** /v1/ads/keywords | List Search keywords |
| [**listAdSets**](AdCampaignsApi.md#listAdSets) | **GET** /v1/ads/ad-sets | List ad sets |
| [**listAdSetsWithHttpInfo**](AdCampaignsApi.md#listAdSetsWithHttpInfo) | **GET** /v1/ads/ad-sets | List ad sets |
| [**listAds**](AdCampaignsApi.md#listAds) | **GET** /v1/ads | List ads |
| [**listAdsWithHttpInfo**](AdCampaignsApi.md#listAdsWithHttpInfo) | **GET** /v1/ads | List ads |
| [**listBidStrategies**](AdCampaignsApi.md#listBidStrategies) | **GET** /v1/ads/bid-strategies | List Google Ads portfolio bid strategies |
| [**listBidStrategiesWithHttpInfo**](AdCampaignsApi.md#listBidStrategiesWithHttpInfo) | **GET** /v1/ads/bid-strategies | List Google Ads portfolio bid strategies |
| [**listCampaignNegativeKeywords**](AdCampaignsApi.md#listCampaignNegativeKeywords) | **GET** /v1/ads/campaigns/{campaignId}/negative-keywords | List campaign-level negative keywords |
| [**listCampaignNegativeKeywordsWithHttpInfo**](AdCampaignsApi.md#listCampaignNegativeKeywordsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/negative-keywords | List campaign-level negative keywords |
| [**removeAdKeyword**](AdCampaignsApi.md#removeAdKeyword) | **DELETE** /v1/ads/keywords/{keywordId} | Remove a Search keyword |
| [**removeAdKeywordWithHttpInfo**](AdCampaignsApi.md#removeAdKeywordWithHttpInfo) | **DELETE** /v1/ads/keywords/{keywordId} | Remove a Search keyword |
| [**replaceCampaignNegativeKeywords**](AdCampaignsApi.md#replaceCampaignNegativeKeywords) | **PUT** /v1/ads/campaigns/{campaignId}/negative-keywords | Replace campaign-level negative keywords |
| [**replaceCampaignNegativeKeywordsWithHttpInfo**](AdCampaignsApi.md#replaceCampaignNegativeKeywordsWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/negative-keywords | Replace campaign-level negative keywords |
| [**updateAd**](AdCampaignsApi.md#updateAd) | **PUT** /v1/ads/{adId} | Update ad |
| [**updateAdWithHttpInfo**](AdCampaignsApi.md#updateAdWithHttpInfo) | **PUT** /v1/ads/{adId} | Update ad |
| [**updateAdCampaign**](AdCampaignsApi.md#updateAdCampaign) | **PUT** /v1/ads/campaigns/{campaignId} | Update a campaign |
| [**updateAdCampaignWithHttpInfo**](AdCampaignsApi.md#updateAdCampaignWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId} | Update a campaign |
| [**updateAdCampaignStatus**](AdCampaignsApi.md#updateAdCampaignStatus) | **PUT** /v1/ads/campaigns/{campaignId}/status | Pause or resume a campaign |
| [**updateAdCampaignStatusWithHttpInfo**](AdCampaignsApi.md#updateAdCampaignStatusWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/status | Pause or resume a campaign |
| [**updateAdKeyword**](AdCampaignsApi.md#updateAdKeyword) | **PATCH** /v1/ads/keywords/{keywordId} | Pause or enable a Search keyword |
| [**updateAdKeywordWithHttpInfo**](AdCampaignsApi.md#updateAdKeywordWithHttpInfo) | **PATCH** /v1/ads/keywords/{keywordId} | Pause or enable a Search keyword |
| [**updateAdSet**](AdCampaignsApi.md#updateAdSet) | **PUT** /v1/ads/ad-sets/{adSetId} | Update an ad set |
| [**updateAdSetWithHttpInfo**](AdCampaignsApi.md#updateAdSetWithHttpInfo) | **PUT** /v1/ads/ad-sets/{adSetId} | Update an ad set |
| [**updateAdSetStatus**](AdCampaignsApi.md#updateAdSetStatus) | **PUT** /v1/ads/ad-sets/{adSetId}/status | Pause or resume a single ad set |
| [**updateAdSetStatusWithHttpInfo**](AdCampaignsApi.md#updateAdSetStatusWithHttpInfo) | **PUT** /v1/ads/ad-sets/{adSetId}/status | Pause or resume a single ad set |
| [**updateAdStatus**](AdCampaignsApi.md#updateAdStatus) | **PUT** /v1/ads/{adId}/status | Pause or resume a single ad |
| [**updateAdStatusWithHttpInfo**](AdCampaignsApi.md#updateAdStatusWithHttpInfo) | **PUT** /v1/ads/{adId}/status | Pause or resume a single ad |
| [**updateBidStrategy**](AdCampaignsApi.md#updateBidStrategy) | **PATCH** /v1/ads/bid-strategies/{strategyId} | Update a Google Ads portfolio bid strategy |
| [**updateBidStrategyWithHttpInfo**](AdCampaignsApi.md#updateBidStrategyWithHttpInfo) | **PATCH** /v1/ads/bid-strategies/{strategyId} | Update a Google Ads portfolio bid strategy |
| [**updateCampaignTargeting**](AdCampaignsApi.md#updateCampaignTargeting) | **PUT** /v1/ads/campaigns/{campaignId}/targeting | Edit a Google campaign&#39;s device, location, or language targeting |
| [**updateCampaignTargetingWithHttpInfo**](AdCampaignsApi.md#updateCampaignTargetingWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/targeting | Edit a Google campaign&#39;s device, location, or language targeting |



## addAdKeywords

> AddAdKeywords201Response addAdKeywords(addAdKeywordsRequest)

Add Search keywords to an ad group

Adds one or more keyword criteria to an existing Google Search ad group, without touching the keywords already there (unlike the whole-set diff on &#x60;PUT /v1/ads/{adId}&#x60;, &#x60;keywords&#x60;/&#x60;negativeKeywords&#x60; in &#x60;platformSpecificData&#x60;, which replaces the set). Set &#x60;negative: true&#x60; to add ad-group-level negatives instead of positive keywords. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        AddAdKeywordsRequest addAdKeywordsRequest = new AddAdKeywordsRequest(); // AddAdKeywordsRequest | 
        try {
            AddAdKeywords201Response result = apiInstance.addAdKeywords(addAdKeywordsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#addAdKeywords");
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
| **addAdKeywordsRequest** | [**AddAdKeywordsRequest**](AddAdKeywordsRequest.md)|  | |

### Return type

[**AddAdKeywords201Response**](AddAdKeywords201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Keywords added |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | The ad group (\&quot;adSetId\&quot;) was not found for this account. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## addAdKeywordsWithHttpInfo

> ApiResponse<AddAdKeywords201Response> addAdKeywords addAdKeywordsWithHttpInfo(addAdKeywordsRequest)

Add Search keywords to an ad group

Adds one or more keyword criteria to an existing Google Search ad group, without touching the keywords already there (unlike the whole-set diff on &#x60;PUT /v1/ads/{adId}&#x60;, &#x60;keywords&#x60;/&#x60;negativeKeywords&#x60; in &#x60;platformSpecificData&#x60;, which replaces the set). Set &#x60;negative: true&#x60; to add ad-group-level negatives instead of positive keywords. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        AddAdKeywordsRequest addAdKeywordsRequest = new AddAdKeywordsRequest(); // AddAdKeywordsRequest | 
        try {
            ApiResponse<AddAdKeywords201Response> response = apiInstance.addAdKeywordsWithHttpInfo(addAdKeywordsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#addAdKeywords");
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
| **addAdKeywordsRequest** | [**AddAdKeywordsRequest**](AddAdKeywordsRequest.md)|  | |

### Return type

ApiResponse<[**AddAdKeywords201Response**](AddAdKeywords201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Keywords added |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | The ad group (\&quot;adSetId\&quot;) was not found for this account. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## attachCampaignAssets

> AttachCampaignAssets201Response attachCampaignAssets(campaignId, attachCampaignAssetsRequest)

Attach extension assets to a Google Search campaign

Attach sitelinks, callouts and/or structured snippets to an already-existing Google Search campaign. These are the same builders POST /v1/ads/create uses, but without rebuilding the hierarchy. At least one of sitelinks, callouts or structuredSnippets is required.  Google-only. Other platforms have no equivalent extension surface and return 501.  Approval status is Google-async; poll &#x60;asset.policy_summary&#x60; after review. Assets stay in the account library even if the campaign is later deleted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        AttachCampaignAssetsRequest attachCampaignAssetsRequest = new AttachCampaignAssetsRequest(); // AttachCampaignAssetsRequest | 
        try {
            AttachCampaignAssets201Response result = apiInstance.attachCampaignAssets(campaignId, attachCampaignAssetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#attachCampaignAssets");
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
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **attachCampaignAssetsRequest** | [**AttachCampaignAssetsRequest**](AttachCampaignAssetsRequest.md)|  | |

### Return type

[**AttachCampaignAssets201Response**](AttachCampaignAssets201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Assets attached |  -  |
| **400** | Invalid input, Google rejected the assets, an unknown customerId (not one of this connection&#39;s Google Ads accounts), or a required customerId missing when the connection has multiple Google Ads accounts |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **422** | No Google Ads customer accounts on this connection. Reconnect Google Ads. |  -  |
| **501** | Only supported on Google Ads |  -  |

## attachCampaignAssetsWithHttpInfo

> ApiResponse<AttachCampaignAssets201Response> attachCampaignAssets attachCampaignAssetsWithHttpInfo(campaignId, attachCampaignAssetsRequest)

Attach extension assets to a Google Search campaign

Attach sitelinks, callouts and/or structured snippets to an already-existing Google Search campaign. These are the same builders POST /v1/ads/create uses, but without rebuilding the hierarchy. At least one of sitelinks, callouts or structuredSnippets is required.  Google-only. Other platforms have no equivalent extension surface and return 501.  Approval status is Google-async; poll &#x60;asset.policy_summary&#x60; after review. Assets stay in the account library even if the campaign is later deleted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        AttachCampaignAssetsRequest attachCampaignAssetsRequest = new AttachCampaignAssetsRequest(); // AttachCampaignAssetsRequest | 
        try {
            ApiResponse<AttachCampaignAssets201Response> response = apiInstance.attachCampaignAssetsWithHttpInfo(campaignId, attachCampaignAssetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#attachCampaignAssets");
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
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **attachCampaignAssetsRequest** | [**AttachCampaignAssetsRequest**](AttachCampaignAssetsRequest.md)|  | |

### Return type

ApiResponse<[**AttachCampaignAssets201Response**](AttachCampaignAssets201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Assets attached |  -  |
| **400** | Invalid input, Google rejected the assets, an unknown customerId (not one of this connection&#39;s Google Ads accounts), or a required customerId missing when the connection has multiple Google Ads accounts |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **422** | No Google Ads customer accounts on this connection. Reconnect Google Ads. |  -  |
| **501** | Only supported on Google Ads |  -  |


## boostPost

> UpdateAd200Response boostPost(boostPostRequest, idempotencyKey)

Boost post as ad

Creates a paid ad from an existing published post, keeping the post&#39;s engagement. By default it provisions the whole hierarchy (campaign, ad set, ad).  **Attach shape (Meta).** Send &#x60;adSetId&#x60; to put the ad under an EXISTING ad set instead, so that ad set keeps its learning phase. It then owns &#x60;budget&#x60;, &#x60;schedule&#x60; and &#x60;targeting&#x60;, and sending any of those alongside &#x60;adSetId&#x60; is a 400 rather than a silent drop. &#x60;budget&#x60; is required only without &#x60;adSetId&#x60;.  &#x60;instagramAccountId&#x60;, &#x60;destinationType&#x60; and &#x60;adSetId&#x60; are Meta-only and return 400 on other platforms.  **Retries.** Boosts are NOT idempotent and can take minutes when Meta requires re-hosting an Instagram video, so do not retry on client timeout. Send an Idempotency-Key header to make retries safe: same key and body replays the original 201, and distinct keys always create distinct ads. Without the header, an identical request is treated as a retry: while one is in flight it returns 409, and within 10 minutes of a completed boost it returns the already-created ad instead of creating another. To intentionally duplicate an ad, send distinct Idempotency-Keys (or vary the body, e.g. the name). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BoostPostRequest boostPostRequest = new BoostPostRequest(); // BoostPostRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            UpdateAd200Response result = apiInstance.boostPost(boostPostRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#boostPost");
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
| **boostPostRequest** | [**BoostPostRequest**](BoostPostRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**UpdateAd200Response**](UpdateAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad created |  -  |
| **400** | Missing required fields or invalid values |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. Also returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **409** | An identical boost request is already in progress (with or without an Idempotency-Key). Wait for it to finish instead of retrying.  |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads), missing linked account, or (for TikTok) the connected TikTok user is not authorized as an Identity on the target advertiser. Returned with code &#x60;ads_connection_required&#x60;; the message includes the actionable \&quot;TikTok Ads Manager → Assets → Identity\&quot; remediation step. Also returned as &#x60;idempotency_key_reused&#x60; when an Idempotency-Key is reused with a different request body.  |  -  |

## boostPostWithHttpInfo

> ApiResponse<UpdateAd200Response> boostPost boostPostWithHttpInfo(boostPostRequest, idempotencyKey)

Boost post as ad

Creates a paid ad from an existing published post, keeping the post&#39;s engagement. By default it provisions the whole hierarchy (campaign, ad set, ad).  **Attach shape (Meta).** Send &#x60;adSetId&#x60; to put the ad under an EXISTING ad set instead, so that ad set keeps its learning phase. It then owns &#x60;budget&#x60;, &#x60;schedule&#x60; and &#x60;targeting&#x60;, and sending any of those alongside &#x60;adSetId&#x60; is a 400 rather than a silent drop. &#x60;budget&#x60; is required only without &#x60;adSetId&#x60;.  &#x60;instagramAccountId&#x60;, &#x60;destinationType&#x60; and &#x60;adSetId&#x60; are Meta-only and return 400 on other platforms.  **Retries.** Boosts are NOT idempotent and can take minutes when Meta requires re-hosting an Instagram video, so do not retry on client timeout. Send an Idempotency-Key header to make retries safe: same key and body replays the original 201, and distinct keys always create distinct ads. Without the header, an identical request is treated as a retry: while one is in flight it returns 409, and within 10 minutes of a completed boost it returns the already-created ad instead of creating another. To intentionally duplicate an ad, send distinct Idempotency-Keys (or vary the body, e.g. the name). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BoostPostRequest boostPostRequest = new BoostPostRequest(); // BoostPostRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<UpdateAd200Response> response = apiInstance.boostPostWithHttpInfo(boostPostRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#boostPost");
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
| **boostPostRequest** | [**BoostPostRequest**](BoostPostRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**UpdateAd200Response**](UpdateAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad created |  -  |
| **400** | Missing required fields or invalid values |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. Also returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **409** | An identical boost request is already in progress (with or without an Idempotency-Key). Wait for it to finish instead of retrying.  |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads), missing linked account, or (for TikTok) the connected TikTok user is not authorized as an Identity on the target advertiser. Returned with code &#x60;ads_connection_required&#x60;; the message includes the actionable \&quot;TikTok Ads Manager → Assets → Identity\&quot; remediation step. Also returned as &#x60;idempotency_key_reused&#x60; when an Idempotency-Key is reused with a different request body.  |  -  |


## bulkUpdateAdCampaignStatus

> BulkUpdateAdCampaignStatus200Response bulkUpdateAdCampaignStatus(bulkUpdateAdCampaignStatusRequest)

Pause or resume many campaigns

Process up to 50 campaigns in one call. Each campaign is updated concurrently and the response contains a per-campaign result so a single bad row does not fail the whole batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BulkUpdateAdCampaignStatusRequest bulkUpdateAdCampaignStatusRequest = new BulkUpdateAdCampaignStatusRequest(); // BulkUpdateAdCampaignStatusRequest | 
        try {
            BulkUpdateAdCampaignStatus200Response result = apiInstance.bulkUpdateAdCampaignStatus(bulkUpdateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#bulkUpdateAdCampaignStatus");
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
| **bulkUpdateAdCampaignStatusRequest** | [**BulkUpdateAdCampaignStatusRequest**](BulkUpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**BulkUpdateAdCampaignStatus200Response**](BulkUpdateAdCampaignStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign results |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |

## bulkUpdateAdCampaignStatusWithHttpInfo

> ApiResponse<BulkUpdateAdCampaignStatus200Response> bulkUpdateAdCampaignStatus bulkUpdateAdCampaignStatusWithHttpInfo(bulkUpdateAdCampaignStatusRequest)

Pause or resume many campaigns

Process up to 50 campaigns in one call. Each campaign is updated concurrently and the response contains a per-campaign result so a single bad row does not fail the whole batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BulkUpdateAdCampaignStatusRequest bulkUpdateAdCampaignStatusRequest = new BulkUpdateAdCampaignStatusRequest(); // BulkUpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<BulkUpdateAdCampaignStatus200Response> response = apiInstance.bulkUpdateAdCampaignStatusWithHttpInfo(bulkUpdateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#bulkUpdateAdCampaignStatus");
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
| **bulkUpdateAdCampaignStatusRequest** | [**BulkUpdateAdCampaignStatusRequest**](BulkUpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**BulkUpdateAdCampaignStatus200Response**](BulkUpdateAdCampaignStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign results |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |


## createAdCampaign

> CreateAdCampaign201Response createAdCampaign(createAdCampaignRequest, idempotencyKey)

Create a standalone campaign

Creates a campaign WITHOUT its first ad set / ad, on the platform of the given &#x60;accountId&#x60;. Ad sets join it later via &#x60;existingCampaignId&#x60; on the create endpoints. Platform notes: on Meta a budget here is campaign-level (CBO) by definition; omit it for ABO (each ad set carries its own budget), and &#x60;specialAdCategories&#x60; is Meta-only (400 elsewhere); &#x60;bidStrategy&#x60; is Meta and Google (400 elsewhere), and Google also accepts &#x60;portfolioBidStrategyId&#x60; instead. Google, X and OpenAI require a budget (422 without one; OpenAI accepts only &#x60;budgetType: lifetime&#x60;, Google only &#x60;budgetType: daily&#x60;). LinkedIn creates the campaign GROUP (our campaign level) and rejects a budget, which lives on the campaign (ad set) level there; it comes back &#x60;status: DRAFT&#x60;. TikTok campaigns are created without a status and report &#x60;ENABLE&#x60;. Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60; where the platform supports it.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdCampaignRequest createAdCampaignRequest = new CreateAdCampaignRequest(); // CreateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            CreateAdCampaign201Response result = apiInstance.createAdCampaign(createAdCampaignRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdCampaign");
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
| **createAdCampaignRequest** | [**CreateAdCampaignRequest**](CreateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

[**CreateAdCampaign201Response**](CreateAdCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Campaign created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createAdCampaignWithHttpInfo

> ApiResponse<CreateAdCampaign201Response> createAdCampaign createAdCampaignWithHttpInfo(createAdCampaignRequest, idempotencyKey)

Create a standalone campaign

Creates a campaign WITHOUT its first ad set / ad, on the platform of the given &#x60;accountId&#x60;. Ad sets join it later via &#x60;existingCampaignId&#x60; on the create endpoints. Platform notes: on Meta a budget here is campaign-level (CBO) by definition; omit it for ABO (each ad set carries its own budget), and &#x60;specialAdCategories&#x60; is Meta-only (400 elsewhere); &#x60;bidStrategy&#x60; is Meta and Google (400 elsewhere), and Google also accepts &#x60;portfolioBidStrategyId&#x60; instead. Google, X and OpenAI require a budget (422 without one; OpenAI accepts only &#x60;budgetType: lifetime&#x60;, Google only &#x60;budgetType: daily&#x60;). LinkedIn creates the campaign GROUP (our campaign level) and rejects a budget, which lives on the campaign (ad set) level there; it comes back &#x60;status: DRAFT&#x60;. TikTok campaigns are created without a status and report &#x60;ENABLE&#x60;. Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60; where the platform supports it.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdCampaignRequest createAdCampaignRequest = new CreateAdCampaignRequest(); // CreateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            ApiResponse<CreateAdCampaign201Response> response = apiInstance.createAdCampaignWithHttpInfo(createAdCampaignRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdCampaign");
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
| **createAdCampaignRequest** | [**CreateAdCampaignRequest**](CreateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

ApiResponse<[**CreateAdCampaign201Response**](CreateAdCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Campaign created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## createAdSet

> CreateAdSet201Response createAdSet(createAdSetRequest, idempotencyKey)

Create a standalone ad group

Google Ads compliance row C.190: creates an ad group WITHOUT an ad, under an existing campaign. Ads join it later via &#x60;existingAdGroupId&#x60; on POST /v1/ads/create. Google only; every other platform returns 501.  Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60;. The new ad group has no ad yet, so it will not appear in GET /v1/ads/tree (built purely from &#x60;ads&#x60; rows) until one is added; use GET /v1/ads/ad-sets to see it in the meantime.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdSetRequest createAdSetRequest = new CreateAdSetRequest(); // CreateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            CreateAdSet201Response result = apiInstance.createAdSet(createAdSetRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdSet");
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
| **createAdSetRequest** | [**CreateAdSetRequest**](CreateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

[**CreateAdSet201Response**](CreateAdSet201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad group created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | accountId does not belong to a Google Ads connection |  -  |
| **501** | Only supported on Google Ads |  -  |

## createAdSetWithHttpInfo

> ApiResponse<CreateAdSet201Response> createAdSet createAdSetWithHttpInfo(createAdSetRequest, idempotencyKey)

Create a standalone ad group

Google Ads compliance row C.190: creates an ad group WITHOUT an ad, under an existing campaign. Ads join it later via &#x60;existingAdGroupId&#x60; on POST /v1/ads/create. Google only; every other platform returns 501.  Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60;. The new ad group has no ad yet, so it will not appear in GET /v1/ads/tree (built purely from &#x60;ads&#x60; rows) until one is added; use GET /v1/ads/ad-sets to see it in the meantime.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdSetRequest createAdSetRequest = new CreateAdSetRequest(); // CreateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            ApiResponse<CreateAdSet201Response> response = apiInstance.createAdSetWithHttpInfo(createAdSetRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdSet");
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
| **createAdSetRequest** | [**CreateAdSetRequest**](CreateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

ApiResponse<[**CreateAdSet201Response**](CreateAdSet201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad group created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | accountId does not belong to a Google Ads connection |  -  |
| **501** | Only supported on Google Ads |  -  |


## createBidStrategy

> CreateBidStrategy201Response createBidStrategy(createBidStrategyRequest)

Create a Google Ads portfolio bid strategy

Creates a standalone bid strategy shared across campaigns. Attach it to a campaign with &#x60;portfolioBidStrategyId&#x60; on POST /v1/ads/create, PUT /v1/ads/campaigns/{campaignId}, or PUT /v1/ads/ad-sets/{adSetId}. Attaching a strategy aligned to a shared budget fails there with a 400 (Google&#39;s &#x60;BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED&#x60;); this is not retryable.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateBidStrategyRequest createBidStrategyRequest = new CreateBidStrategyRequest(); // CreateBidStrategyRequest | 
        try {
            CreateBidStrategy201Response result = apiInstance.createBidStrategy(createBidStrategyRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createBidStrategy");
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
| **createBidStrategyRequest** | [**CreateBidStrategyRequest**](CreateBidStrategyRequest.md)|  | |

### Return type

[**CreateBidStrategy201Response**](CreateBidStrategy201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bid strategy created |  -  |
| **400** | Invalid input, or Google rejected the strategy (e.g. shared-budget alignment). The message carries Google&#39;s error. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer accounts on this connection. Reconnect Google Ads. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## createBidStrategyWithHttpInfo

> ApiResponse<CreateBidStrategy201Response> createBidStrategy createBidStrategyWithHttpInfo(createBidStrategyRequest)

Create a Google Ads portfolio bid strategy

Creates a standalone bid strategy shared across campaigns. Attach it to a campaign with &#x60;portfolioBidStrategyId&#x60; on POST /v1/ads/create, PUT /v1/ads/campaigns/{campaignId}, or PUT /v1/ads/ad-sets/{adSetId}. Attaching a strategy aligned to a shared budget fails there with a 400 (Google&#39;s &#x60;BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED&#x60;); this is not retryable.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateBidStrategyRequest createBidStrategyRequest = new CreateBidStrategyRequest(); // CreateBidStrategyRequest | 
        try {
            ApiResponse<CreateBidStrategy201Response> response = apiInstance.createBidStrategyWithHttpInfo(createBidStrategyRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createBidStrategy");
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
| **createBidStrategyRequest** | [**CreateBidStrategyRequest**](CreateBidStrategyRequest.md)|  | |

### Return type

ApiResponse<[**CreateBidStrategy201Response**](CreateBidStrategy201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bid strategy created |  -  |
| **400** | Invalid input, or Google rejected the strategy (e.g. shared-budget alignment). The message carries Google&#39;s error. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer accounts on this connection. Reconnect Google Ads. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## createStandaloneAd

> CreateStandaloneAd200Response createStandaloneAd(createStandaloneAdRequest, idempotencyKey)

Create standalone ad

Create a paid ad with custom creative across Meta, Google Ads, Pinterest, TikTok, X, LinkedIn, and OpenAI Ads (ChatGPT Ads).  Three mutually-exclusive request shapes are selected by the body:  - Legacy single-creative shape (all platforms, the default). - Meta-only multi-creative shape via the creatives array: one ad set with N ads sharing budget and targeting. - Attach shape via adSetId: adds one new ad to an existing ad set, inheriting its budget, targeting, and schedule (Meta, TikTok, and LinkedIn). On LinkedIn adSetId is the existing Campaign id, and the budget, schedule, targeting and bidding fields must be omitted.  Per-platform required fields, budget minimums, and video-ad rules are documented on each property below.  LinkedIn creates a Single Image or Single Video Ad backed by a Direct Sponsored Content \&quot;dark post\&quot; authored by a Company Page (see &#x60;organizationId&#x60;). Supported goals are engagement, traffic, awareness, and video_views (video ads use the &#x60;video&#x60; field; video_views requires a video), and traffic ads require &#x60;linkUrl&#x60;.  **Idempotency:** this endpoint is not idempotent at the platform level (a blind retry creates a second campaign/ad set/ad). Send an &#x60;Idempotency-Key&#x60; header to make retries safe: the first request with a given key creates the ad and we store the response; a retry with the same key replays that exact response (with &#x60;Idempotent-Replayed: true&#x60;) instead of creating duplicates. Reusing a key with a different body returns 422; a key whose first request is still in flight returns 409 (retry after a short backoff). Keys are scoped to your credential and expire after 24h. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateStandaloneAdRequest createStandaloneAdRequest = new CreateStandaloneAdRequest(); // CreateStandaloneAdRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            CreateStandaloneAd200Response result = apiInstance.createStandaloneAd(createStandaloneAdRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createStandaloneAd");
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
| **createStandaloneAdRequest** | [**CreateStandaloneAdRequest**](CreateStandaloneAdRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**CreateStandaloneAd200Response**](CreateStandaloneAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateOnly dry-run passed, nothing was created |  -  |
| **201** | Ad(s) created |  -  |
| **400** | Missing required fields, invalid values, non-Meta platform used with creatives[] / adSetId, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. Also returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or missing linked account |  -  |
| **501** | The requested option is not supported on this platform: &#x60;validateOnly&#x60; outside Meta, or a shape the adapter does not implement. Carries code &#x60;feature_not_available&#x60;.  |  -  |
| **502** | The platform rejected the request, or failed to produce media the ad needs (e.g. Meta generated no poster for an uploaded video when no &#x60;video.thumbnailUrl&#x60; was supplied). Inspect &#x60;platformError&#x60; for the upstream payload. Failures we raise carry a &#x60;reason&#x60;; a payload forwarded verbatim from Meta may not. On the &#x60;creatives[]&#x60; shape a missing poster also carries &#x60;creativeIndex&#x60; and &#x60;videoUrl&#x60; to identify the entry. An upstream 4xx status is forwarded instead of 502.  |  -  |

## createStandaloneAdWithHttpInfo

> ApiResponse<CreateStandaloneAd200Response> createStandaloneAd createStandaloneAdWithHttpInfo(createStandaloneAdRequest, idempotencyKey)

Create standalone ad

Create a paid ad with custom creative across Meta, Google Ads, Pinterest, TikTok, X, LinkedIn, and OpenAI Ads (ChatGPT Ads).  Three mutually-exclusive request shapes are selected by the body:  - Legacy single-creative shape (all platforms, the default). - Meta-only multi-creative shape via the creatives array: one ad set with N ads sharing budget and targeting. - Attach shape via adSetId: adds one new ad to an existing ad set, inheriting its budget, targeting, and schedule (Meta, TikTok, and LinkedIn). On LinkedIn adSetId is the existing Campaign id, and the budget, schedule, targeting and bidding fields must be omitted.  Per-platform required fields, budget minimums, and video-ad rules are documented on each property below.  LinkedIn creates a Single Image or Single Video Ad backed by a Direct Sponsored Content \&quot;dark post\&quot; authored by a Company Page (see &#x60;organizationId&#x60;). Supported goals are engagement, traffic, awareness, and video_views (video ads use the &#x60;video&#x60; field; video_views requires a video), and traffic ads require &#x60;linkUrl&#x60;.  **Idempotency:** this endpoint is not idempotent at the platform level (a blind retry creates a second campaign/ad set/ad). Send an &#x60;Idempotency-Key&#x60; header to make retries safe: the first request with a given key creates the ad and we store the response; a retry with the same key replays that exact response (with &#x60;Idempotent-Replayed: true&#x60;) instead of creating duplicates. Reusing a key with a different body returns 422; a key whose first request is still in flight returns 409 (retry after a short backoff). Keys are scoped to your credential and expire after 24h. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateStandaloneAdRequest createStandaloneAdRequest = new CreateStandaloneAdRequest(); // CreateStandaloneAdRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<CreateStandaloneAd200Response> response = apiInstance.createStandaloneAdWithHttpInfo(createStandaloneAdRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createStandaloneAd");
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
| **createStandaloneAdRequest** | [**CreateStandaloneAdRequest**](CreateStandaloneAdRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**CreateStandaloneAd200Response**](CreateStandaloneAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | validateOnly dry-run passed, nothing was created |  -  |
| **201** | Ad(s) created |  -  |
| **400** | Missing required fields, invalid values, non-Meta platform used with creatives[] / adSetId, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. Also returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or missing linked account |  -  |
| **501** | The requested option is not supported on this platform: &#x60;validateOnly&#x60; outside Meta, or a shape the adapter does not implement. Carries code &#x60;feature_not_available&#x60;.  |  -  |
| **502** | The platform rejected the request, or failed to produce media the ad needs (e.g. Meta generated no poster for an uploaded video when no &#x60;video.thumbnailUrl&#x60; was supplied). Inspect &#x60;platformError&#x60; for the upstream payload. Failures we raise carry a &#x60;reason&#x60;; a payload forwarded verbatim from Meta may not. On the &#x60;creatives[]&#x60; shape a missing poster also carries &#x60;creativeIndex&#x60; and &#x60;videoUrl&#x60; to identify the entry. An upstream 4xx status is forwarded instead of 502.  |  -  |


## deleteAd

> DeleteAccountGroup200Response deleteAd(adId)

Cancel an ad

Cancels the ad on the platform and marks it as cancelled in the database. The ad is preserved for history. OpenAI Ads has no delete API; the ad is archived instead (a terminal state, the closest equivalent).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        try {
            DeleteAccountGroup200Response result = apiInstance.deleteAd(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAd");
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
| **200** | Ad cancelled |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## deleteAdWithHttpInfo

> ApiResponse<DeleteAccountGroup200Response> deleteAd deleteAdWithHttpInfo(adId)

Cancel an ad

Cancels the ad on the platform and marks it as cancelled in the database. The ad is preserved for history. OpenAI Ads has no delete API; the ad is archived instead (a terminal state, the closest equivalent).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        try {
            ApiResponse<DeleteAccountGroup200Response> response = apiInstance.deleteAdWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAd");
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
| **200** | Ad cancelled |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## deleteAdCampaign

> DeleteAdCampaign200Response deleteAdCampaign(campaignId, deleteAdCampaignRequest)

Delete a campaign

Deletes the whole campaign on the platform, cascading to its ad sets and ads. Locally, all Ad documents for this campaign are marked &#x60;status: cancelled&#x60;.  **Empty campaigns.** A campaign with zero ads has no local Ad documents to resolve, so it is invisible to &#x60;/v1/ads/tree&#x60; and this endpoint would 404. That state is produced by the two-step create flow (campaign, then ads via &#x60;existingCampaignId&#x60;) whenever Meta rejects the ad step. To delete such a shell, send &#x60;accountId&#x60; in the body: we skip the local lookup entirely and forward the delete to Meta. &#x60;accountId&#x60; is ignored when the campaign does have ads. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        DeleteAdCampaignRequest deleteAdCampaignRequest = new DeleteAdCampaignRequest(); // DeleteAdCampaignRequest | 
        try {
            DeleteAdCampaign200Response result = apiInstance.deleteAdCampaign(campaignId, deleteAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **deleteAdCampaignRequest** | [**DeleteAdCampaignRequest**](DeleteAdCampaignRequest.md)|  | |

### Return type

[**DeleteAdCampaign200Response**](DeleteAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |

## deleteAdCampaignWithHttpInfo

> ApiResponse<DeleteAdCampaign200Response> deleteAdCampaign deleteAdCampaignWithHttpInfo(campaignId, deleteAdCampaignRequest)

Delete a campaign

Deletes the whole campaign on the platform, cascading to its ad sets and ads. Locally, all Ad documents for this campaign are marked &#x60;status: cancelled&#x60;.  **Empty campaigns.** A campaign with zero ads has no local Ad documents to resolve, so it is invisible to &#x60;/v1/ads/tree&#x60; and this endpoint would 404. That state is produced by the two-step create flow (campaign, then ads via &#x60;existingCampaignId&#x60;) whenever Meta rejects the ad step. To delete such a shell, send &#x60;accountId&#x60; in the body: we skip the local lookup entirely and forward the delete to Meta. &#x60;accountId&#x60; is ignored when the campaign does have ads. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        DeleteAdCampaignRequest deleteAdCampaignRequest = new DeleteAdCampaignRequest(); // DeleteAdCampaignRequest | 
        try {
            ApiResponse<DeleteAdCampaign200Response> response = apiInstance.deleteAdCampaignWithHttpInfo(campaignId, deleteAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **deleteAdCampaignRequest** | [**DeleteAdCampaignRequest**](DeleteAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**DeleteAdCampaign200Response**](DeleteAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |


## deleteAdSet

> DeleteAdSet200Response deleteAdSet(adSetId)

Delete an ad set

Deletes the ad set on the platform, cascading to its ads only (never the campaign). Locally, every Ad document under the ad set is marked &#x60;status: cancelled&#x60;.  Delete is soft on platforms that have no hard delete: LinkedIn moves the campaign to &#x60;PENDING_DELETION&#x60;, Pinterest archives the ad group, and X soft-flags the line item. Google removes the ad group. All remain readable for reporting. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        try {
            DeleteAdSet200Response result = apiInstance.deleteAdSet(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdSet");
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
| **adSetId** | **String**| Platform ad set ID | |

### Return type

[**DeleteAdSet200Response**](DeleteAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad set not found |  -  |
| **501** | Operation not supported on this platform |  -  |

## deleteAdSetWithHttpInfo

> ApiResponse<DeleteAdSet200Response> deleteAdSet deleteAdSetWithHttpInfo(adSetId)

Delete an ad set

Deletes the ad set on the platform, cascading to its ads only (never the campaign). Locally, every Ad document under the ad set is marked &#x60;status: cancelled&#x60;.  Delete is soft on platforms that have no hard delete: LinkedIn moves the campaign to &#x60;PENDING_DELETION&#x60;, Pinterest archives the ad group, and X soft-flags the line item. Google removes the ad group. All remain readable for reporting. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        try {
            ApiResponse<DeleteAdSet200Response> response = apiInstance.deleteAdSetWithHttpInfo(adSetId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdSet");
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
| **adSetId** | **String**| Platform ad set ID | |

### Return type

ApiResponse<[**DeleteAdSet200Response**](DeleteAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad set not found |  -  |
| **501** | Operation not supported on this platform |  -  |


## duplicateAd

> DuplicateAd200Response duplicateAd(adId, idempotencyKey, duplicateAdRequest)

Duplicate an ad

Duplicates a single ad via Meta&#39;s native &#x60;POST /{ad-id}/copies&#x60;. The copy is created paused. &#x60;adSetId&#x60; retargets the copy into another ad set; omitted &#x3D; the source&#39;s own ad set. Accepts the Zernio ad id or the platform ad id. Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad ID or platform ad ID
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        DuplicateAdRequest duplicateAdRequest = new DuplicateAdRequest(); // DuplicateAdRequest | 
        try {
            DuplicateAd200Response result = apiInstance.duplicateAd(adId, idempotencyKey, duplicateAdRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAd");
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
| **adId** | **String**| Zernio ad ID or platform ad ID | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |
| **duplicateAdRequest** | [**DuplicateAdRequest**](DuplicateAdRequest.md)|  | [optional] |

### Return type

[**DuplicateAd200Response**](DuplicateAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## duplicateAdWithHttpInfo

> ApiResponse<DuplicateAd200Response> duplicateAd duplicateAdWithHttpInfo(adId, idempotencyKey, duplicateAdRequest)

Duplicate an ad

Duplicates a single ad via Meta&#39;s native &#x60;POST /{ad-id}/copies&#x60;. The copy is created paused. &#x60;adSetId&#x60; retargets the copy into another ad set; omitted &#x3D; the source&#39;s own ad set. Accepts the Zernio ad id or the platform ad id. Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad ID or platform ad ID
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        DuplicateAdRequest duplicateAdRequest = new DuplicateAdRequest(); // DuplicateAdRequest | 
        try {
            ApiResponse<DuplicateAd200Response> response = apiInstance.duplicateAdWithHttpInfo(adId, idempotencyKey, duplicateAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAd");
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
| **adId** | **String**| Zernio ad ID or platform ad ID | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |
| **duplicateAdRequest** | [**DuplicateAdRequest**](DuplicateAdRequest.md)|  | [optional] |

### Return type

ApiResponse<[**DuplicateAd200Response**](DuplicateAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## duplicateAdCampaign

> DuplicateAdCampaign200Response duplicateAdCampaign(campaignId, duplicateAdCampaignRequest, idempotencyKey)

Duplicate a campaign

Duplicates a campaign, including its ad sets, ads, creatives, and targeting by default (&#x60;deepCopy: true&#x60;). The copy is created paused so callers can review before launching.  Per-platform implementation: - **Meta** uses the native &#x60;POST /{campaign-id}/copies&#x60; endpoint. - **TikTok** has no native copy primitive; Zernio walks the source   graph (&#x60;/v2/campaign/get/&#x60;, &#x60;/v2/adgroup/get/&#x60;, &#x60;/v2/ad/get/&#x60;) and   recreates each entity via the corresponding &#x60;/create/&#x60; endpoints,   carrying over budget / targeting / bid_type / bid_price /   deep_bid_type / creative fields. Spark Ad linkage (&#x60;tiktok_item_id&#x60;)   is preserved. - **LinkedIn** has no native copy primitive; Zernio walks the source   CampaignGroup → Campaigns → Creatives and recreates each entity,   carrying over &#x60;type&#x60; / &#x60;costType&#x60; / &#x60;unitCost&#x60; /   &#x60;optimizationTargetType&#x60; / &#x60;creativeSelection&#x60; / &#x60;objectiveType&#x60; /   &#x60;format&#x60; / &#x60;dailyBudget&#x60; / &#x60;totalBudget&#x60; / &#x60;targetingCriteria&#x60; /   &#x60;runSchedule&#x60; and every Creative&#39;s &#x60;content&#x60; object verbatim.   &#x60;statusOption: INHERITED_FROM_SOURCE&#x60; is evaluated **per entity**:   any Group / Campaign / Creative whose source is &#x60;ACTIVE&#x60; gets its   clone activated too. Duplicating an ACTIVE campaign with   &#x60;INHERITED_FROM_SOURCE&#x60; starts a second front of spend the moment   the clone activates. The safe default is &#x60;PAUSED&#x60;.  The new hierarchy is asynchronous to materialize in our DB, and we trigger sync discovery automatically. Set &#x60;syncAfter: false&#x60; to skip and poll &#x60;/v1/ads/tree&#x60; on your own cadence.  Other platforms return 501 Not Implemented. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Source platform campaign ID
        DuplicateAdCampaignRequest duplicateAdCampaignRequest = new DuplicateAdCampaignRequest(); // DuplicateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            DuplicateAdCampaign200Response result = apiInstance.duplicateAdCampaign(campaignId, duplicateAdCampaignRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdCampaign");
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
| **campaignId** | **String**| Source platform campaign ID | |
| **duplicateAdCampaignRequest** | [**DuplicateAdCampaignRequest**](DuplicateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

[**DuplicateAdCampaign200Response**](DuplicateAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Source campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |

## duplicateAdCampaignWithHttpInfo

> ApiResponse<DuplicateAdCampaign200Response> duplicateAdCampaign duplicateAdCampaignWithHttpInfo(campaignId, duplicateAdCampaignRequest, idempotencyKey)

Duplicate a campaign

Duplicates a campaign, including its ad sets, ads, creatives, and targeting by default (&#x60;deepCopy: true&#x60;). The copy is created paused so callers can review before launching.  Per-platform implementation: - **Meta** uses the native &#x60;POST /{campaign-id}/copies&#x60; endpoint. - **TikTok** has no native copy primitive; Zernio walks the source   graph (&#x60;/v2/campaign/get/&#x60;, &#x60;/v2/adgroup/get/&#x60;, &#x60;/v2/ad/get/&#x60;) and   recreates each entity via the corresponding &#x60;/create/&#x60; endpoints,   carrying over budget / targeting / bid_type / bid_price /   deep_bid_type / creative fields. Spark Ad linkage (&#x60;tiktok_item_id&#x60;)   is preserved. - **LinkedIn** has no native copy primitive; Zernio walks the source   CampaignGroup → Campaigns → Creatives and recreates each entity,   carrying over &#x60;type&#x60; / &#x60;costType&#x60; / &#x60;unitCost&#x60; /   &#x60;optimizationTargetType&#x60; / &#x60;creativeSelection&#x60; / &#x60;objectiveType&#x60; /   &#x60;format&#x60; / &#x60;dailyBudget&#x60; / &#x60;totalBudget&#x60; / &#x60;targetingCriteria&#x60; /   &#x60;runSchedule&#x60; and every Creative&#39;s &#x60;content&#x60; object verbatim.   &#x60;statusOption: INHERITED_FROM_SOURCE&#x60; is evaluated **per entity**:   any Group / Campaign / Creative whose source is &#x60;ACTIVE&#x60; gets its   clone activated too. Duplicating an ACTIVE campaign with   &#x60;INHERITED_FROM_SOURCE&#x60; starts a second front of spend the moment   the clone activates. The safe default is &#x60;PAUSED&#x60;.  The new hierarchy is asynchronous to materialize in our DB, and we trigger sync discovery automatically. Set &#x60;syncAfter: false&#x60; to skip and poll &#x60;/v1/ads/tree&#x60; on your own cadence.  Other platforms return 501 Not Implemented. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Source platform campaign ID
        DuplicateAdCampaignRequest duplicateAdCampaignRequest = new DuplicateAdCampaignRequest(); // DuplicateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            ApiResponse<DuplicateAdCampaign200Response> response = apiInstance.duplicateAdCampaignWithHttpInfo(campaignId, duplicateAdCampaignRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdCampaign");
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
| **campaignId** | **String**| Source platform campaign ID | |
| **duplicateAdCampaignRequest** | [**DuplicateAdCampaignRequest**](DuplicateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

ApiResponse<[**DuplicateAdCampaign200Response**](DuplicateAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Source campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |


## duplicateAdSet

> DuplicateAdSet200Response duplicateAdSet(adSetId, duplicateAdSetRequest, idempotencyKey)

Duplicate an ad set

Duplicates an ad set, including its ads and creatives by default (&#x60;deepCopy: true&#x60;), via Meta&#39;s native &#x60;POST /{adset-id}/copies&#x60;. The copy is created paused so callers can review before launching. &#x60;campaignId&#x60; retargets the copy into another campaign; omitted &#x3D; the source&#39;s own campaign. The new hierarchy materializes asynchronously, and sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Source platform ad set ID
        DuplicateAdSetRequest duplicateAdSetRequest = new DuplicateAdSetRequest(); // DuplicateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            DuplicateAdSet200Response result = apiInstance.duplicateAdSet(adSetId, duplicateAdSetRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdSet");
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
| **adSetId** | **String**| Source platform ad set ID | |
| **duplicateAdSetRequest** | [**DuplicateAdSetRequest**](DuplicateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

[**DuplicateAdSet200Response**](DuplicateAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Source ad set not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## duplicateAdSetWithHttpInfo

> ApiResponse<DuplicateAdSet200Response> duplicateAdSet duplicateAdSetWithHttpInfo(adSetId, duplicateAdSetRequest, idempotencyKey)

Duplicate an ad set

Duplicates an ad set, including its ads and creatives by default (&#x60;deepCopy: true&#x60;), via Meta&#39;s native &#x60;POST /{adset-id}/copies&#x60;. The copy is created paused so callers can review before launching. &#x60;campaignId&#x60; retargets the copy into another campaign; omitted &#x3D; the source&#39;s own campaign. The new hierarchy materializes asynchronously, and sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Source platform ad set ID
        DuplicateAdSetRequest duplicateAdSetRequest = new DuplicateAdSetRequest(); // DuplicateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.
        try {
            ApiResponse<DuplicateAdSet200Response> response = apiInstance.duplicateAdSetWithHttpInfo(adSetId, duplicateAdSetRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdSet");
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
| **adSetId** | **String**| Source platform ad set ID | |
| **duplicateAdSetRequest** | [**DuplicateAdSetRequest**](DuplicateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. | [optional] |

### Return type

ApiResponse<[**DuplicateAdSet200Response**](DuplicateAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Source ad set not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAd

> GetAd200Response getAd(adId)

Get ad details

Returns an ad with its creative, targeting, status, and performance metrics.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: - the Zernio internal &#x60;_id&#x60; (24-char hex) - Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;) - the creative&#39;s &#x60;effective_object_story_id&#x60; (&#x60;{pageId}_{postId}&#x60; shape, Facebook side) - the creative&#39;s &#x60;effective_instagram_media_id&#x60; (Instagram side)  Any of the four resolve to the same ad. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs. See description for details. 
        try {
            GetAd200Response result = apiInstance.getAd(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAd");
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
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. See description for details.  | |

### Return type

[**GetAd200Response**](GetAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad details |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getAdWithHttpInfo

> ApiResponse<GetAd200Response> getAd getAdWithHttpInfo(adId)

Get ad details

Returns an ad with its creative, targeting, status, and performance metrics.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: - the Zernio internal &#x60;_id&#x60; (24-char hex) - Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;) - the creative&#39;s &#x60;effective_object_story_id&#x60; (&#x60;{pageId}_{postId}&#x60; shape, Facebook side) - the creative&#39;s &#x60;effective_instagram_media_id&#x60; (Instagram side)  Any of the four resolve to the same ad. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs. See description for details. 
        try {
            ApiResponse<GetAd200Response> response = apiInstance.getAdWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAd");
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
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. See description for details.  | |

### Return type

ApiResponse<[**GetAd200Response**](GetAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad details |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getAdSetDetails

> GetAdSetDetails200Response getAdSetDetails(adSetId, accountId, fields)

Live ad-set details incl. learning phase

Reads the ad set live from Meta, returned verbatim. The default projection includes &#x60;learning_stage_info&#x60; (learning-phase status: LEARNING / SUCCESS / FAIL / WAIVING; Meta omits its &#x60;status&#x60; key on paused ad sets), delivery settings, budgets, schedule and targeting. &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Meta ad set id (platformAdSetId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            GetAdSetDetails200Response result = apiInstance.getAdSetDetails(adSetId, accountId, fields);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetDetails");
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
| **adSetId** | **String**| Meta ad set id (platformAdSetId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

[**GetAdSetDetails200Response**](GetAdSetDetails200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ad set as returned by Meta |  -  |
| **400** | Invalid input, or Meta rejected the query; the message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdSetDetailsWithHttpInfo

> ApiResponse<GetAdSetDetails200Response> getAdSetDetails getAdSetDetailsWithHttpInfo(adSetId, accountId, fields)

Live ad-set details incl. learning phase

Reads the ad set live from Meta, returned verbatim. The default projection includes &#x60;learning_stage_info&#x60; (learning-phase status: LEARNING / SUCCESS / FAIL / WAIVING; Meta omits its &#x60;status&#x60; key on paused ad sets), delivery settings, budgets, schedule and targeting. &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Meta ad set id (platformAdSetId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            ApiResponse<GetAdSetDetails200Response> response = apiInstance.getAdSetDetailsWithHttpInfo(adSetId, accountId, fields);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetDetails");
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
| **adSetId** | **String**| Meta ad set id (platformAdSetId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

ApiResponse<[**GetAdSetDetails200Response**](GetAdSetDetails200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ad set as returned by Meta |  -  |
| **400** | Invalid input, or Meta rejected the query; the message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdTree

> AdTreeResponse getAdTree(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel)

Get campaign tree

Returns a nested Campaign &gt; Ad Set &gt; Ad hierarchy with rolled-up metrics at each level. Uses a two-stage aggregation: ads are grouped into ad sets, then ad sets into campaigns. Metrics are computed over an optional date range, then rolled up from ad level to ad set and campaign levels. Pagination is at the campaign level. Ads without a campaign or ad set ID are grouped into synthetic \&quot;Ungrouped\&quot; buckets. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  Pass &#x60;timeIncrement&#x3D;1&#x60; to also get a daily breakdown: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) in the same call. Use &#x60;dailyLevel&#x60; (&#x60;campaign&#x60; default, or &#x60;adset&#x60; / &#x60;ad&#x60;) to choose which levels carry the series. This replaces calling the tree once per day for per-campaign daily trends.  **Deleted objects stay in the tree.** Deleting an ad or a campaign is a soft delete: the Ad documents move to &#x60;status: cancelled&#x60; and are kept indefinitely, so their historical spend still counts toward the metrics of any date range they fall in. There is no pruning job and no retention window. Filter on &#x60;status&#x60; if your view should hide them, but do that after reading the totals, not before. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | Campaigns per page
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager but a team usually cares about a subset). Comma-separate for multiple (`?adAccountId=act_1,act_2,act_3`); single value keeps its old shape. Max 50 accounts per request; the plural aliases `adAccountIds` and `platformAdAccountIds` are rejected with a 400 to stop them from silently returning the unfiltered fleet.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page's ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta's numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination. Pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the `campaignId` filter on GET /v1/ads.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass `hasDelivery` or `minSpend` to also filter the campaign set to this window. Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend. Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. Filters the campaign set itself, so `pagination.total` counts only matching campaigns.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount. Expressed in each campaign's OWN currency (the `currency` field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies `hasDelivery`; `minSpend=0` applies no filter.
        String sort = "newest"; // String | Campaign-level sort order. `newest` (default) / `oldest` order by the campaign's newest-ad createdAt. `spend_desc` / `spend_asc` order by aggregated spend in the requested date range; campaigns with no spend land at the end.
        Integer timeIncrement = 1; // Integer | Set to `1` to also return a daily breakdown. Mirrors Meta Insights' `time_increment=1`: each node gains a `daily[]` array of per-day metrics (same fields as the aggregated `metrics`) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only `1` (daily) is supported. The daily series covers the same date range and uses the same source data as `metrics`, except `reach` on Meta and TikTok: the range total is the platform's de-duplicated value, so daily reach does not sum to it. See `dailyLevel` to control which levels carry it.
        String dailyLevel = "campaign"; // String | Which tree levels get the `daily[]` series when `timeIncrement=1`. `campaign` (default) attaches it on campaign nodes only: the common per-campaign-trend case, and the smallest payload. `adset` adds it on ad sets too; `ad` adds it on every ad in `ads[]` as well (heaviest: a long range × up to 100 ads per ad set). Scope with `campaignId` to keep `ad`-level responses small. Ignored when `timeIncrement` is unset.
        try {
            AdTreeResponse result = apiInstance.getAdTree(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdTree");
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
| **limit** | **Integer**| Campaigns per page | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager but a team usually cares about a subset). Comma-separate for multiple (&#x60;?adAccountId&#x3D;act_1,act_2,act_3&#x60;); single value keeps its old shape. Max 50 accounts per request; the plural aliases &#x60;adAccountIds&#x60; and &#x60;platformAdAccountIds&#x60; are rejected with a 400 to stop them from silently returning the unfiltered fleet. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page&#39;s ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta&#39;s numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination. Pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the &#x60;campaignId&#x60; filter on GET /v1/ads. | [optional] |
| **fromDate** | **LocalDate**| Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass &#x60;hasDelivery&#x60; or &#x60;minSpend&#x60; to also filter the campaign set to this window. Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend. Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. Filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount. Expressed in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. | [optional] |
| **sort** | **String**| Campaign-level sort order. &#x60;newest&#x60; (default) / &#x60;oldest&#x60; order by the campaign&#39;s newest-ad createdAt. &#x60;spend_desc&#x60; / &#x60;spend_asc&#x60; order by aggregated spend in the requested date range; campaigns with no spend land at the end. | [optional] [default to newest] [enum: newest, oldest, spend_desc, spend_asc] |
| **timeIncrement** | **Integer**| Set to &#x60;1&#x60; to also return a daily breakdown. Mirrors Meta Insights&#39; &#x60;time_increment&#x3D;1&#x60;: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only &#x60;1&#x60; (daily) is supported. The daily series covers the same date range and uses the same source data as &#x60;metrics&#x60;, except &#x60;reach&#x60; on Meta and TikTok: the range total is the platform&#39;s de-duplicated value, so daily reach does not sum to it. See &#x60;dailyLevel&#x60; to control which levels carry it. | [optional] [enum: 1] |
| **dailyLevel** | **String**| Which tree levels get the &#x60;daily[]&#x60; series when &#x60;timeIncrement&#x3D;1&#x60;. &#x60;campaign&#x60; (default) attaches it on campaign nodes only: the common per-campaign-trend case, and the smallest payload. &#x60;adset&#x60; adds it on ad sets too; &#x60;ad&#x60; adds it on every ad in &#x60;ads[]&#x60; as well (heaviest: a long range × up to 100 ads per ad set). Scope with &#x60;campaignId&#x60; to keep &#x60;ad&#x60;-level responses small. Ignored when &#x60;timeIncrement&#x60; is unset. | [optional] [default to campaign] [enum: campaign, adset, ad] |

### Return type

[**AdTreeResponse**](AdTreeResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nested campaign tree with pagination |  -  |
| **202** | Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## getAdTreeWithHttpInfo

> ApiResponse<AdTreeResponse> getAdTree getAdTreeWithHttpInfo(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel)

Get campaign tree

Returns a nested Campaign &gt; Ad Set &gt; Ad hierarchy with rolled-up metrics at each level. Uses a two-stage aggregation: ads are grouped into ad sets, then ad sets into campaigns. Metrics are computed over an optional date range, then rolled up from ad level to ad set and campaign levels. Pagination is at the campaign level. Ads without a campaign or ad set ID are grouped into synthetic \&quot;Ungrouped\&quot; buckets. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  Pass &#x60;timeIncrement&#x3D;1&#x60; to also get a daily breakdown: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) in the same call. Use &#x60;dailyLevel&#x60; (&#x60;campaign&#x60; default, or &#x60;adset&#x60; / &#x60;ad&#x60;) to choose which levels carry the series. This replaces calling the tree once per day for per-campaign daily trends.  **Deleted objects stay in the tree.** Deleting an ad or a campaign is a soft delete: the Ad documents move to &#x60;status: cancelled&#x60; and are kept indefinitely, so their historical spend still counts toward the metrics of any date range they fall in. There is no pruning job and no retention window. Filter on &#x60;status&#x60; if your view should hide them, but do that after reading the totals, not before. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | Campaigns per page
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager but a team usually cares about a subset). Comma-separate for multiple (`?adAccountId=act_1,act_2,act_3`); single value keeps its old shape. Max 50 accounts per request; the plural aliases `adAccountIds` and `platformAdAccountIds` are rejected with a 400 to stop them from silently returning the unfiltered fleet.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page's ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta's numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination. Pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the `campaignId` filter on GET /v1/ads.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass `hasDelivery` or `minSpend` to also filter the campaign set to this window. Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend. Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. Filters the campaign set itself, so `pagination.total` counts only matching campaigns.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount. Expressed in each campaign's OWN currency (the `currency` field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies `hasDelivery`; `minSpend=0` applies no filter.
        String sort = "newest"; // String | Campaign-level sort order. `newest` (default) / `oldest` order by the campaign's newest-ad createdAt. `spend_desc` / `spend_asc` order by aggregated spend in the requested date range; campaigns with no spend land at the end.
        Integer timeIncrement = 1; // Integer | Set to `1` to also return a daily breakdown. Mirrors Meta Insights' `time_increment=1`: each node gains a `daily[]` array of per-day metrics (same fields as the aggregated `metrics`) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only `1` (daily) is supported. The daily series covers the same date range and uses the same source data as `metrics`, except `reach` on Meta and TikTok: the range total is the platform's de-duplicated value, so daily reach does not sum to it. See `dailyLevel` to control which levels carry it.
        String dailyLevel = "campaign"; // String | Which tree levels get the `daily[]` series when `timeIncrement=1`. `campaign` (default) attaches it on campaign nodes only: the common per-campaign-trend case, and the smallest payload. `adset` adds it on ad sets too; `ad` adds it on every ad in `ads[]` as well (heaviest: a long range × up to 100 ads per ad set). Scope with `campaignId` to keep `ad`-level responses small. Ignored when `timeIncrement` is unset.
        try {
            ApiResponse<AdTreeResponse> response = apiInstance.getAdTreeWithHttpInfo(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdTree");
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
| **limit** | **Integer**| Campaigns per page | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager but a team usually cares about a subset). Comma-separate for multiple (&#x60;?adAccountId&#x3D;act_1,act_2,act_3&#x60;); single value keeps its old shape. Max 50 accounts per request; the plural aliases &#x60;adAccountIds&#x60; and &#x60;platformAdAccountIds&#x60; are rejected with a 400 to stop them from silently returning the unfiltered fleet. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page&#39;s ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta&#39;s numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination. Pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the &#x60;campaignId&#x60; filter on GET /v1/ads. | [optional] |
| **fromDate** | **LocalDate**| Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass &#x60;hasDelivery&#x60; or &#x60;minSpend&#x60; to also filter the campaign set to this window. Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend. Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. Filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount. Expressed in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. | [optional] |
| **sort** | **String**| Campaign-level sort order. &#x60;newest&#x60; (default) / &#x60;oldest&#x60; order by the campaign&#39;s newest-ad createdAt. &#x60;spend_desc&#x60; / &#x60;spend_asc&#x60; order by aggregated spend in the requested date range; campaigns with no spend land at the end. | [optional] [default to newest] [enum: newest, oldest, spend_desc, spend_asc] |
| **timeIncrement** | **Integer**| Set to &#x60;1&#x60; to also return a daily breakdown. Mirrors Meta Insights&#39; &#x60;time_increment&#x3D;1&#x60;: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only &#x60;1&#x60; (daily) is supported. The daily series covers the same date range and uses the same source data as &#x60;metrics&#x60;, except &#x60;reach&#x60; on Meta and TikTok: the range total is the platform&#39;s de-duplicated value, so daily reach does not sum to it. See &#x60;dailyLevel&#x60; to control which levels carry it. | [optional] [enum: 1] |
| **dailyLevel** | **String**| Which tree levels get the &#x60;daily[]&#x60; series when &#x60;timeIncrement&#x3D;1&#x60;. &#x60;campaign&#x60; (default) attaches it on campaign nodes only: the common per-campaign-trend case, and the smallest payload. &#x60;adset&#x60; adds it on ad sets too; &#x60;ad&#x60; adds it on every ad in &#x60;ads[]&#x60; as well (heaviest: a long range × up to 100 ads per ad set). Scope with &#x60;campaignId&#x60; to keep &#x60;ad&#x60;-level responses small. Ignored when &#x60;timeIncrement&#x60; is unset. | [optional] [default to campaign] [enum: campaign, adset, ad] |

### Return type

ApiResponse<[**AdTreeResponse**](AdTreeResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nested campaign tree with pagination |  -  |
| **202** | Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## getAdsTimeline

> AdsTimelineResponse getAdsTimeline(accountId, adAccountId, fromDate, toDate, platform)

Get daily account metrics

Returns daily aggregate metrics across all ads in a SocialAccount as a single time series, one row per calendar day in the requested range. Use this for dashboards that draw a daily-spend or daily-conversions chart, instead of calling &#x60;/v1/ads/tree&#x60; once per day.  &#x60;accountId&#x60; is required. The lookup is sibling-expanded so passing the &#x60;metaads&#x60; ID also includes ads under the linked &#x60;facebook&#x60; / &#x60;instagram&#x60; posting account (and vice-versa), the same convention as &#x60;/v1/ads/tree&#x60; and &#x60;/v1/ads&#x60;.  Date range defaults to the last 90 days. Capped at 730 days. Ranges older than the ingested history return a &#x60;202&#x60; immediately with the covered part and &#x60;backfillPending: true&#x60; while the rest is backfilled in the background; repeat the request shortly until it returns 200 with full data.  With adAccountId set to a Google customer id this is the customer-level performance report (clicks, cost, impressions, conversions, all conversions per day). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID. Sibling-expanded to its linked posting↔ads pair.
        String adAccountId = "adAccountId_example"; // String | Optional platform-native ad account ID (e.g. Meta `act_…`, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don't carry this column; the recurring 7-day re-sync repopulates them naturally.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String platform = "facebook"; // String | Restrict to one platform.
        try {
            AdsTimelineResponse result = apiInstance.getAdsTimeline(accountId, adAccountId, fromDate, toDate, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdsTimeline");
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
| **accountId** | **String**| Account ID. Sibling-expanded to its linked posting↔ads pair. | |
| **adAccountId** | **String**| Optional platform-native ad account ID (e.g. Meta &#x60;act_…&#x60;, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don&#39;t carry this column; the recurring 7-day re-sync repopulates them naturally. | [optional] |
| **fromDate** | **LocalDate**| Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **platform** | **String**| Restrict to one platform. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

[**AdsTimelineResponse**](AdsTimelineResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily time series of aggregate metrics. Empty &#x60;rows&#x60; means the account has no ad activity in the range. |  -  |
| **202** | Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## getAdsTimelineWithHttpInfo

> ApiResponse<AdsTimelineResponse> getAdsTimeline getAdsTimelineWithHttpInfo(accountId, adAccountId, fromDate, toDate, platform)

Get daily account metrics

Returns daily aggregate metrics across all ads in a SocialAccount as a single time series, one row per calendar day in the requested range. Use this for dashboards that draw a daily-spend or daily-conversions chart, instead of calling &#x60;/v1/ads/tree&#x60; once per day.  &#x60;accountId&#x60; is required. The lookup is sibling-expanded so passing the &#x60;metaads&#x60; ID also includes ads under the linked &#x60;facebook&#x60; / &#x60;instagram&#x60; posting account (and vice-versa), the same convention as &#x60;/v1/ads/tree&#x60; and &#x60;/v1/ads&#x60;.  Date range defaults to the last 90 days. Capped at 730 days. Ranges older than the ingested history return a &#x60;202&#x60; immediately with the covered part and &#x60;backfillPending: true&#x60; while the rest is backfilled in the background; repeat the request shortly until it returns 200 with full data.  With adAccountId set to a Google customer id this is the customer-level performance report (clicks, cost, impressions, conversions, all conversions per day). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID. Sibling-expanded to its linked posting↔ads pair.
        String adAccountId = "adAccountId_example"; // String | Optional platform-native ad account ID (e.g. Meta `act_…`, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don't carry this column; the recurring 7-day re-sync repopulates them naturally.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String platform = "facebook"; // String | Restrict to one platform.
        try {
            ApiResponse<AdsTimelineResponse> response = apiInstance.getAdsTimelineWithHttpInfo(accountId, adAccountId, fromDate, toDate, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdsTimeline");
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
| **accountId** | **String**| Account ID. Sibling-expanded to its linked posting↔ads pair. | |
| **adAccountId** | **String**| Optional platform-native ad account ID (e.g. Meta &#x60;act_…&#x60;, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don&#39;t carry this column; the recurring 7-day re-sync repopulates them naturally. | [optional] |
| **fromDate** | **LocalDate**| Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **platform** | **String**| Restrict to one platform. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

ApiResponse<[**AdsTimelineResponse**](AdsTimelineResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily time series of aggregate metrics. Empty &#x60;rows&#x60; means the account has no ad activity in the range. |  -  |
| **202** | Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## getCampaignBidding

> GetCampaignBidding200Response getCampaignBidding(campaignId, accountId, platform, customerId)

Read a campaign&#39;s current bidding

Read of the campaign&#39;s bidding strategy on Google, cached for the quota window, for pre-filling the bid strategy block before a PUT to /v1/ads/campaigns/{campaignId}. Google Ads only; &#x60;platform&#x60; is required and rejected when it is anything else, since a &#x60;campaignId&#x60; is not globally unique. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  Maps Google&#39;s bidding strategy onto the same triplet PUT accepts: &#x60;LOWEST_COST_WITHOUT_CAP&#x60; (Maximize Conversions, no target), &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60; (Target CPA), &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60; (Target ROAS), &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60; (Maximize Clicks with a CPC ceiling). A campaign on a portfolio strategy returns &#x60;portfolio&#x60; (id + name) and &#x60;bidSpec.portfolioBidStrategyId&#x60; instead of the triplet. Anything else (Manual CPC, Target Impression Share, ...) returns &#x60;bidSpec: null&#x60;; show &#x60;biddingStrategyType&#x60; as-is. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        String accountId = "accountId_example"; // String | Zernio Google Ads SocialAccount id: resolves the customer id + refresh token.
        String platform = "google"; // String | Required: campaign IDs are not globally unique. Only \"google\" is supported today.
        String customerId = "customerId_example"; // String | Numeric Google Ads customer id (no dashes). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one.
        try {
            GetCampaignBidding200Response result = apiInstance.getCampaignBidding(campaignId, accountId, platform, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignBidding");
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
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **accountId** | **String**| Zernio Google Ads SocialAccount id: resolves the customer id + refresh token. | |
| **platform** | **String**| Required: campaign IDs are not globally unique. Only \&quot;google\&quot; is supported today. | [enum: google] |
| **customerId** | **String**| Numeric Google Ads customer id (no dashes). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one. | [optional] |

### Return type

[**GetCampaignBidding200Response**](GetCampaignBidding200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign bidding |  -  |
| **400** | Invalid input (accountId, customerId, or a non-numeric campaignId), or a platform other than \&quot;google\&quot; |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Campaign not found on Google Ads |  -  |
| **501** | Not a Google Ads account: the connection behind accountId resolves to another platform. |  -  |

## getCampaignBiddingWithHttpInfo

> ApiResponse<GetCampaignBidding200Response> getCampaignBidding getCampaignBiddingWithHttpInfo(campaignId, accountId, platform, customerId)

Read a campaign&#39;s current bidding

Read of the campaign&#39;s bidding strategy on Google, cached for the quota window, for pre-filling the bid strategy block before a PUT to /v1/ads/campaigns/{campaignId}. Google Ads only; &#x60;platform&#x60; is required and rejected when it is anything else, since a &#x60;campaignId&#x60; is not globally unique. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  Maps Google&#39;s bidding strategy onto the same triplet PUT accepts: &#x60;LOWEST_COST_WITHOUT_CAP&#x60; (Maximize Conversions, no target), &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60; (Target CPA), &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60; (Target ROAS), &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60; (Maximize Clicks with a CPC ceiling). A campaign on a portfolio strategy returns &#x60;portfolio&#x60; (id + name) and &#x60;bidSpec.portfolioBidStrategyId&#x60; instead of the triplet. Anything else (Manual CPC, Target Impression Share, ...) returns &#x60;bidSpec: null&#x60;; show &#x60;biddingStrategyType&#x60; as-is. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        String accountId = "accountId_example"; // String | Zernio Google Ads SocialAccount id: resolves the customer id + refresh token.
        String platform = "google"; // String | Required: campaign IDs are not globally unique. Only \"google\" is supported today.
        String customerId = "customerId_example"; // String | Numeric Google Ads customer id (no dashes). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one.
        try {
            ApiResponse<GetCampaignBidding200Response> response = apiInstance.getCampaignBiddingWithHttpInfo(campaignId, accountId, platform, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignBidding");
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
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **accountId** | **String**| Zernio Google Ads SocialAccount id: resolves the customer id + refresh token. | |
| **platform** | **String**| Required: campaign IDs are not globally unique. Only \&quot;google\&quot; is supported today. | [enum: google] |
| **customerId** | **String**| Numeric Google Ads customer id (no dashes). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one. | [optional] |

### Return type

ApiResponse<[**GetCampaignBidding200Response**](GetCampaignBidding200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign bidding |  -  |
| **400** | Invalid input (accountId, customerId, or a non-numeric campaignId), or a platform other than \&quot;google\&quot; |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Campaign not found on Google Ads |  -  |
| **501** | Not a Google Ads account: the connection behind accountId resolves to another platform. |  -  |


## getCampaignTargeting

> GetCampaignTargeting200Response getCampaignTargeting(campaignId, platform)

Read a Google campaign&#39;s device, location, and language targeting

Google Ads compliance requires geo, language, budget, and bidding targeting set at creation to stay editable afterwards; this reads the campaign state so an integrator can build an editor around it. Cached for the quota window (10 minutes fresh, up to 7 days last-good), not always a live read. Google only; every other platform returns 501.  &#x60;devices&#x60; always lists all four device types with &#x60;included&#x60; reflecting Google&#39;s negative device criteria (a device absent from any negative criterion is included by default). This read has no bid-modifier source, so &#x60;bidModifier&#x60; is always &#x60;null&#x60; even for a device with one configured. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        String platform = "google"; // String | Disambiguates when the same campaignId string exists on more than one connected platform.
        try {
            GetCampaignTargeting200Response result = apiInstance.getCampaignTargeting(campaignId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignTargeting");
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
| **campaignId** | **String**| Google platform campaign ID | |
| **platform** | **String**| Disambiguates when the same campaignId string exists on more than one connected platform. | [optional] [enum: google] |

### Return type

[**GetCampaignTargeting200Response**](GetCampaignTargeting200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current campaign targeting |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## getCampaignTargetingWithHttpInfo

> ApiResponse<GetCampaignTargeting200Response> getCampaignTargeting getCampaignTargetingWithHttpInfo(campaignId, platform)

Read a Google campaign&#39;s device, location, and language targeting

Google Ads compliance requires geo, language, budget, and bidding targeting set at creation to stay editable afterwards; this reads the campaign state so an integrator can build an editor around it. Cached for the quota window (10 minutes fresh, up to 7 days last-good), not always a live read. Google only; every other platform returns 501.  &#x60;devices&#x60; always lists all four device types with &#x60;included&#x60; reflecting Google&#39;s negative device criteria (a device absent from any negative criterion is included by default). This read has no bid-modifier source, so &#x60;bidModifier&#x60; is always &#x60;null&#x60; even for a device with one configured. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        String platform = "google"; // String | Disambiguates when the same campaignId string exists on more than one connected platform.
        try {
            ApiResponse<GetCampaignTargeting200Response> response = apiInstance.getCampaignTargetingWithHttpInfo(campaignId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignTargeting");
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
| **campaignId** | **String**| Google platform campaign ID | |
| **platform** | **String**| Disambiguates when the same campaignId string exists on more than one connected platform. | [optional] [enum: google] |

### Return type

ApiResponse<[**GetCampaignTargeting200Response**](GetCampaignTargeting200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current campaign targeting |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## listAdCampaigns

> ListAdCampaigns200Response listAdCampaigns(includeEmpty, page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend)

List campaigns

Returns campaigns as virtual aggregations over ad documents grouped by platform campaign ID. Metrics (spend, impressions, clicks, etc.) are summed across all ads in each campaign. Campaign status is derived from child ad statuses (active &gt; pending_review &gt; paused &gt; error &gt; completed &gt; cancelled &gt; rejected). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Boolean includeEmpty = true; // Boolean | Meta only. Campaign reads aggregate over ad documents, so a campaign with ZERO ads is normally invisible here, the state the two-step create (campaign, then ads via `existingCampaignId`) leaves behind whenever Meta rejects the ad step. Set true to list those too, with `adCount: 0` and zeroed metrics. Requires `accountId` and `adAccountId`, since an empty campaign has no ad row to resolve a token or ad account from.
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | 
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta)
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend. Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window. Filters the campaign set itself, so `pagination.total` counts only matching campaigns. Mirrors the same filter on /v1/ads/tree.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount, in each campaign's OWN currency (the `currency` field on the campaign). Implies `hasDelivery`; `minSpend=0` applies no filter. Mirrors the same filter on /v1/ads/tree.
        try {
            ListAdCampaigns200Response result = apiInstance.listAdCampaigns(includeEmpty, page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdCampaigns");
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
| **includeEmpty** | **Boolean**| Meta only. Campaign reads aggregate over ad documents, so a campaign with ZERO ads is normally invisible here, the state the two-step create (campaign, then ads via &#x60;existingCampaignId&#x60;) leaves behind whenever Meta rejects the ad step. Set true to list those too, with &#x60;adCount: 0&#x60; and zeroed metrics. Requires &#x60;accountId&#x60; and &#x60;adAccountId&#x60;, since an empty campaign has no ad row to resolve a token or ad account from. | [optional] |
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta) | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend. Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window. Filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. Mirrors the same filter on /v1/ads/tree. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount, in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign). Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. Mirrors the same filter on /v1/ads/tree. | [optional] |

### Return type

[**ListAdCampaigns200Response**](ListAdCampaigns200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated campaigns |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdCampaignsWithHttpInfo

> ApiResponse<ListAdCampaigns200Response> listAdCampaigns listAdCampaignsWithHttpInfo(includeEmpty, page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend)

List campaigns

Returns campaigns as virtual aggregations over ad documents grouped by platform campaign ID. Metrics (spend, impressions, clicks, etc.) are summed across all ads in each campaign. Campaign status is derived from child ad statuses (active &gt; pending_review &gt; paused &gt; error &gt; completed &gt; cancelled &gt; rejected). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Boolean includeEmpty = true; // Boolean | Meta only. Campaign reads aggregate over ad documents, so a campaign with ZERO ads is normally invisible here, the state the two-step create (campaign, then ads via `existingCampaignId`) leaves behind whenever Meta rejects the ad step. Set true to list those too, with `adCount: 0` and zeroed metrics. Requires `accountId` and `adAccountId`, since an empty campaign has no ad row to resolve a token or ad account from.
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | 
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta)
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend. Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window. Filters the campaign set itself, so `pagination.total` counts only matching campaigns. Mirrors the same filter on /v1/ads/tree.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount, in each campaign's OWN currency (the `currency` field on the campaign). Implies `hasDelivery`; `minSpend=0` applies no filter. Mirrors the same filter on /v1/ads/tree.
        try {
            ApiResponse<ListAdCampaigns200Response> response = apiInstance.listAdCampaignsWithHttpInfo(includeEmpty, page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdCampaigns");
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
| **includeEmpty** | **Boolean**| Meta only. Campaign reads aggregate over ad documents, so a campaign with ZERO ads is normally invisible here, the state the two-step create (campaign, then ads via &#x60;existingCampaignId&#x60;) leaves behind whenever Meta rejects the ad step. Set true to list those too, with &#x60;adCount: 0&#x60; and zeroed metrics. Requires &#x60;accountId&#x60; and &#x60;adAccountId&#x60;, since an empty campaign has no ad row to resolve a token or ad account from. | [optional] |
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta) | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend. Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window. Filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. Mirrors the same filter on /v1/ads/tree. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount, in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign). Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. Mirrors the same filter on /v1/ads/tree. | [optional] |

### Return type

ApiResponse<[**ListAdCampaigns200Response**](ListAdCampaigns200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated campaigns |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdKeywords

> ListAdKeywords200Response listAdKeywords(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search)

List Search keywords

Returns the Google Search keyword criteria (positive and negative) synced from connected Google Ads accounts, one row per ad-group keyword. Refreshed about once a week per Google Ads customer (the keyword sweep rides the ads discovery pass on a slower slot, to stay inside Google&#39;s shared daily API quota), so keywords added on Google can take several days to appear. A customer synced for the first time is populated on the next discovery pass rather than waiting for its weekly slot, and connecting an account or triggering a manual sync refreshes it immediately. Campaign-level negative keywords are not included; only ad-group-level criteria are. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String adSetId = "adSetId_example"; // String | Platform ad group ID (Google ad group)
        String status = "active"; // String | Keyword criterion status
        String matchType = "exact"; // String | 
        Boolean negative = true; // Boolean | true = negative keywords only, false = positive only. Omit for both.
        String search = "search_example"; // String | Case-insensitive substring match on the keyword text
        try {
            ListAdKeywords200Response result = apiInstance.listAdKeywords(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdKeywords");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **adSetId** | **String**| Platform ad group ID (Google ad group) | [optional] |
| **status** | **String**| Keyword criterion status | [optional] [enum: active, paused] |
| **matchType** | **String**|  | [optional] [enum: exact, phrase, broad, unknown] |
| **negative** | **Boolean**| true &#x3D; negative keywords only, false &#x3D; positive only. Omit for both. | [optional] |
| **search** | **String**| Case-insensitive substring match on the keyword text | [optional] |

### Return type

[**ListAdKeywords200Response**](ListAdKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated keywords |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdKeywordsWithHttpInfo

> ApiResponse<ListAdKeywords200Response> listAdKeywords listAdKeywordsWithHttpInfo(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search)

List Search keywords

Returns the Google Search keyword criteria (positive and negative) synced from connected Google Ads accounts, one row per ad-group keyword. Refreshed about once a week per Google Ads customer (the keyword sweep rides the ads discovery pass on a slower slot, to stay inside Google&#39;s shared daily API quota), so keywords added on Google can take several days to appear. A customer synced for the first time is populated on the next discovery pass rather than waiting for its weekly slot, and connecting an account or triggering a manual sync refreshes it immediately. Campaign-level negative keywords are not included; only ad-group-level criteria are. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String adSetId = "adSetId_example"; // String | Platform ad group ID (Google ad group)
        String status = "active"; // String | Keyword criterion status
        String matchType = "exact"; // String | 
        Boolean negative = true; // Boolean | true = negative keywords only, false = positive only. Omit for both.
        String search = "search_example"; // String | Case-insensitive substring match on the keyword text
        try {
            ApiResponse<ListAdKeywords200Response> response = apiInstance.listAdKeywordsWithHttpInfo(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdKeywords");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **adSetId** | **String**| Platform ad group ID (Google ad group) | [optional] |
| **status** | **String**| Keyword criterion status | [optional] [enum: active, paused] |
| **matchType** | **String**|  | [optional] [enum: exact, phrase, broad, unknown] |
| **negative** | **Boolean**| true &#x3D; negative keywords only, false &#x3D; positive only. Omit for both. | [optional] |
| **search** | **String**| Case-insensitive substring match on the keyword text | [optional] |

### Return type

ApiResponse<[**ListAdKeywords200Response**](ListAdKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated keywords |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdSets

> ListAdSets200Response listAdSets(accountId, campaignId, platform)

List ad sets

Ad sets (Google ad groups) synced for the connection, optionally filtered by platform and campaignId. Reads the &#x60;ad_sets&#x60; table directly, independent of the &#x60;ads&#x60; rollup GET /v1/ads/tree uses, so a newly created standalone ad group with no ad yet (POST /v1/ads/ad-sets, Google only) is visible here even though it is invisible in the tree until an ad joins it via &#x60;existingAdGroupId&#x60;. Returns at most 500 rows, newest first.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String platform = "facebook"; // String | 
        try {
            ListAdSets200Response result = apiInstance.listAdSets(accountId, campaignId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdSets");
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
| **accountId** | **String**| Account ID | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

[**ListAdSets200Response**](ListAdSets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |

## listAdSetsWithHttpInfo

> ApiResponse<ListAdSets200Response> listAdSets listAdSetsWithHttpInfo(accountId, campaignId, platform)

List ad sets

Ad sets (Google ad groups) synced for the connection, optionally filtered by platform and campaignId. Reads the &#x60;ad_sets&#x60; table directly, independent of the &#x60;ads&#x60; rollup GET /v1/ads/tree uses, so a newly created standalone ad group with no ad yet (POST /v1/ads/ad-sets, Google only) is visible here even though it is invisible in the tree until an ad joins it via &#x60;existingAdGroupId&#x60;. Returns at most 500 rows, newest first.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String platform = "facebook"; // String | 
        try {
            ApiResponse<ListAdSets200Response> response = apiInstance.listAdSetsWithHttpInfo(accountId, campaignId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdSets");
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
| **accountId** | **String**| Account ID | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

ApiResponse<[**ListAdSets200Response**](ListAdSets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |


## listAds

> AdsListResponse listAds(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate)

List ads

Returns a paginated list of ads with metrics computed over an optional date range. Use source&#x3D;all to include externally-synced ads from platform ad managers. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  To find the Zernio ad behind a comment you see in Meta Business Manager, filter by platformAdId (the Meta ad ID), effectiveObjectStoryId (Facebook), or effectiveInstagramMediaId (Instagram). Those are the post/media the ad&#39;s engagement lives on, and are also returned on each ad&#39;s &#x60;creative&#x60; object. Then call GET /v1/ads/{adId}/comments with the returned ad id. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String source = "zernio"; // String | all (default) = Zernio-created + platform-discovered ads. zernio = restrict to Zernio-created only.
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | 
        String platform = "facebook"; // String | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad's `creative.pageId`; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID (filter ads within a campaign)
        String adSetId = "adSetId_example"; // String | Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard).
        String platformAdId = "platformAdId_example"; // String | Meta ad ID. Returns the ad with this platform-side ad ID.
        String effectiveObjectStoryId = "effectiveObjectStoryId_example"; // String | Facebook `{pageId}_{postId}` of the post the ad's engagement lives on (Meta `effective_object_story_id`). Use to map a Business-Manager-visible post back to the Zernio ad.
        String effectiveInstagramMediaId = "effectiveInstagramMediaId_example"; // String | Instagram media ID of the boosted post (Meta `effective_instagram_media_id`). Use to map a Business-Manager-visible IG post back to the Zernio ad.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        try {
            AdsListResponse result = apiInstance.listAds(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAds");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **source** | **String**| all (default) &#x3D; Zernio-created + platform-discovered ads. zernio &#x3D; restrict to Zernio-created only. | [optional] [default to all] [enum: zernio, all] |
| **status** | [**AdStatus**](.md)|  | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad&#39;s &#x60;creative.pageId&#x60;; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID (filter ads within a campaign) | [optional] |
| **adSetId** | **String**| Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard). | [optional] |
| **platformAdId** | **String**| Meta ad ID. Returns the ad with this platform-side ad ID. | [optional] |
| **effectiveObjectStoryId** | **String**| Facebook &#x60;{pageId}_{postId}&#x60; of the post the ad&#39;s engagement lives on (Meta &#x60;effective_object_story_id&#x60;). Use to map a Business-Manager-visible post back to the Zernio ad. | [optional] |
| **effectiveInstagramMediaId** | **String**| Instagram media ID of the boosted post (Meta &#x60;effective_instagram_media_id&#x60;). Use to map a Business-Manager-visible IG post back to the Zernio ad. | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |

### Return type

[**AdsListResponse**](AdsListResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated ads |  -  |
| **202** | Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdsWithHttpInfo

> ApiResponse<AdsListResponse> listAds listAdsWithHttpInfo(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate)

List ads

Returns a paginated list of ads with metrics computed over an optional date range. Use source&#x3D;all to include externally-synced ads from platform ad managers. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  To find the Zernio ad behind a comment you see in Meta Business Manager, filter by platformAdId (the Meta ad ID), effectiveObjectStoryId (Facebook), or effectiveInstagramMediaId (Instagram). Those are the post/media the ad&#39;s engagement lives on, and are also returned on each ad&#39;s &#x60;creative&#x60; object. Then call GET /v1/ads/{adId}/comments with the returned ad id. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String source = "zernio"; // String | all (default) = Zernio-created + platform-discovered ads. zernio = restrict to Zernio-created only.
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | 
        String platform = "facebook"; // String | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad's `creative.pageId`; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID (filter ads within a campaign)
        String adSetId = "adSetId_example"; // String | Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard).
        String platformAdId = "platformAdId_example"; // String | Meta ad ID. Returns the ad with this platform-side ad ID.
        String effectiveObjectStoryId = "effectiveObjectStoryId_example"; // String | Facebook `{pageId}_{postId}` of the post the ad's engagement lives on (Meta `effective_object_story_id`). Use to map a Business-Manager-visible post back to the Zernio ad.
        String effectiveInstagramMediaId = "effectiveInstagramMediaId_example"; // String | Instagram media ID of the boosted post (Meta `effective_instagram_media_id`). Use to map a Business-Manager-visible IG post back to the Zernio ad.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        try {
            ApiResponse<AdsListResponse> response = apiInstance.listAdsWithHttpInfo(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAds");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **source** | **String**| all (default) &#x3D; Zernio-created + platform-discovered ads. zernio &#x3D; restrict to Zernio-created only. | [optional] [default to all] [enum: zernio, all] |
| **status** | [**AdStatus**](.md)|  | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad&#39;s &#x60;creative.pageId&#x60;; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID (filter ads within a campaign) | [optional] |
| **adSetId** | **String**| Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard). | [optional] |
| **platformAdId** | **String**| Meta ad ID. Returns the ad with this platform-side ad ID. | [optional] |
| **effectiveObjectStoryId** | **String**| Facebook &#x60;{pageId}_{postId}&#x60; of the post the ad&#39;s engagement lives on (Meta &#x60;effective_object_story_id&#x60;). Use to map a Business-Manager-visible post back to the Zernio ad. | [optional] |
| **effectiveInstagramMediaId** | **String**| Instagram media ID of the boosted post (Meta &#x60;effective_instagram_media_id&#x60;). Use to map a Business-Manager-visible IG post back to the Zernio ad. | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |

### Return type

ApiResponse<[**AdsListResponse**](AdsListResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated ads |  -  |
| **202** | Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listBidStrategies

> ListBidStrategies200Response listBidStrategies(accountId, customerId, fromDate, toDate)

List Google Ads portfolio bid strategies

Bidding strategy report: type, status, campaign count, clicks, cost, cost per conversion, impressions, average CPC and conversions over the date range (default last 30 days). Reads Google&#39;s &#x60;bidding_strategy&#x60; resource, cached for the quota window. Draws on the shared Google Ads operations budget. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String customerId = "customerId_example"; // String | Numeric Google Ads customer id (no dashes). Defaults to the account's connected customer.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Defaults to 30 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Defaults to today.
        try {
            ListBidStrategies200Response result = apiInstance.listBidStrategies(accountId, customerId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listBidStrategies");
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
| **accountId** | **String**| Google ads SocialAccount id. | |
| **customerId** | **String**| Numeric Google Ads customer id (no dashes). Defaults to the account&#39;s connected customer. | [optional] |
| **fromDate** | **LocalDate**| Defaults to 30 days ago. | [optional] |
| **toDate** | **LocalDate**| Defaults to today. | [optional] |

### Return type

[**ListBidStrategies200Response**](ListBidStrategies200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Portfolio bid strategies |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## listBidStrategiesWithHttpInfo

> ApiResponse<ListBidStrategies200Response> listBidStrategies listBidStrategiesWithHttpInfo(accountId, customerId, fromDate, toDate)

List Google Ads portfolio bid strategies

Bidding strategy report: type, status, campaign count, clicks, cost, cost per conversion, impressions, average CPC and conversions over the date range (default last 30 days). Reads Google&#39;s &#x60;bidding_strategy&#x60; resource, cached for the quota window. Draws on the shared Google Ads operations budget. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String customerId = "customerId_example"; // String | Numeric Google Ads customer id (no dashes). Defaults to the account's connected customer.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Defaults to 30 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Defaults to today.
        try {
            ApiResponse<ListBidStrategies200Response> response = apiInstance.listBidStrategiesWithHttpInfo(accountId, customerId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listBidStrategies");
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
| **accountId** | **String**| Google ads SocialAccount id. | |
| **customerId** | **String**| Numeric Google Ads customer id (no dashes). Defaults to the account&#39;s connected customer. | [optional] |
| **fromDate** | **LocalDate**| Defaults to 30 days ago. | [optional] |
| **toDate** | **LocalDate**| Defaults to today. | [optional] |

### Return type

ApiResponse<[**ListBidStrategies200Response**](ListBidStrategies200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Portfolio bid strategies |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## listCampaignNegativeKeywords

> ListCampaignNegativeKeywords200Response listCampaignNegativeKeywords(campaignId, platform)

List campaign-level negative keywords

Returns the campaign-level negative keywords (&#x60;campaign_criterion.negative&#x60;), distinct from the ad-group-level negatives under &#x60;GET /v1/ads/keywords&#x60;. Cached for the quota window (not synced to Postgres), and gated by the shared Google Ads operations budget like every other on-demand Google surface. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  The platform is always discovered from the campaign itself; a non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was passed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String platform = "facebook"; // String | Optional and NOT authoritative: the resolved campaign's own platform decides 200 vs 501, never this hint.
        try {
            ListCampaignNegativeKeywords200Response result = apiInstance.listCampaignNegativeKeywords(campaignId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignNegativeKeywords");
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
| **campaignId** | **String**| Platform campaign ID | |
| **platform** | **String**| Optional and NOT authoritative: the resolved campaign&#39;s own platform decides 200 vs 501, never this hint. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

[**ListCampaignNegativeKeywords200Response**](ListCampaignNegativeKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## listCampaignNegativeKeywordsWithHttpInfo

> ApiResponse<ListCampaignNegativeKeywords200Response> listCampaignNegativeKeywords listCampaignNegativeKeywordsWithHttpInfo(campaignId, platform)

List campaign-level negative keywords

Returns the campaign-level negative keywords (&#x60;campaign_criterion.negative&#x60;), distinct from the ad-group-level negatives under &#x60;GET /v1/ads/keywords&#x60;. Cached for the quota window (not synced to Postgres), and gated by the shared Google Ads operations budget like every other on-demand Google surface. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  The platform is always discovered from the campaign itself; a non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was passed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String platform = "facebook"; // String | Optional and NOT authoritative: the resolved campaign's own platform decides 200 vs 501, never this hint.
        try {
            ApiResponse<ListCampaignNegativeKeywords200Response> response = apiInstance.listCampaignNegativeKeywordsWithHttpInfo(campaignId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignNegativeKeywords");
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
| **campaignId** | **String**| Platform campaign ID | |
| **platform** | **String**| Optional and NOT authoritative: the resolved campaign&#39;s own platform decides 200 vs 501, never this hint. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

ApiResponse<[**ListCampaignNegativeKeywords200Response**](ListCampaignNegativeKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## removeAdKeyword

> RemoveAdKeyword200Response removeAdKeyword(keywordId)

Remove a Search keyword

Removes one keyword criterion (positive or negative) from its ad group (M.140).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (not the Google criterion ID)
        try {
            RemoveAdKeyword200Response result = apiInstance.removeAdKeyword(keywordId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeAdKeyword");
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
| **keywordId** | **String**| Zernio keyword ID (not the Google criterion ID) | |

### Return type

[**RemoveAdKeyword200Response**](RemoveAdKeyword200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keyword removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Keyword not found |  -  |

## removeAdKeywordWithHttpInfo

> ApiResponse<RemoveAdKeyword200Response> removeAdKeyword removeAdKeywordWithHttpInfo(keywordId)

Remove a Search keyword

Removes one keyword criterion (positive or negative) from its ad group (M.140).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (not the Google criterion ID)
        try {
            ApiResponse<RemoveAdKeyword200Response> response = apiInstance.removeAdKeywordWithHttpInfo(keywordId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeAdKeyword");
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
| **keywordId** | **String**| Zernio keyword ID (not the Google criterion ID) | |

### Return type

ApiResponse<[**RemoveAdKeyword200Response**](RemoveAdKeyword200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keyword removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Keyword not found |  -  |


## replaceCampaignNegativeKeywords

> ReplaceCampaignNegativeKeywords200Response replaceCampaignNegativeKeywords(campaignId, replaceCampaignNegativeKeywordsRequest)

Replace campaign-level negative keywords

Replaces the FULL set of campaign-level negative keywords (C.270): the desired list is diffed against what Google already has, and the difference is applied as one &#x60;create&#x60;/&#x60;remove&#x60; mutate. Send an empty array to clear every campaign negative.  The platform is always discovered from the campaign itself; a non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was sent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        ReplaceCampaignNegativeKeywordsRequest replaceCampaignNegativeKeywordsRequest = new ReplaceCampaignNegativeKeywordsRequest(); // ReplaceCampaignNegativeKeywordsRequest | 
        try {
            ReplaceCampaignNegativeKeywords200Response result = apiInstance.replaceCampaignNegativeKeywords(campaignId, replaceCampaignNegativeKeywordsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceCampaignNegativeKeywords");
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
| **campaignId** | **String**| Platform campaign ID | |
| **replaceCampaignNegativeKeywordsRequest** | [**ReplaceCampaignNegativeKeywordsRequest**](ReplaceCampaignNegativeKeywordsRequest.md)|  | |

### Return type

[**ReplaceCampaignNegativeKeywords200Response**](ReplaceCampaignNegativeKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords replaced |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## replaceCampaignNegativeKeywordsWithHttpInfo

> ApiResponse<ReplaceCampaignNegativeKeywords200Response> replaceCampaignNegativeKeywords replaceCampaignNegativeKeywordsWithHttpInfo(campaignId, replaceCampaignNegativeKeywordsRequest)

Replace campaign-level negative keywords

Replaces the FULL set of campaign-level negative keywords (C.270): the desired list is diffed against what Google already has, and the difference is applied as one &#x60;create&#x60;/&#x60;remove&#x60; mutate. Send an empty array to clear every campaign negative.  The platform is always discovered from the campaign itself; a non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was sent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        ReplaceCampaignNegativeKeywordsRequest replaceCampaignNegativeKeywordsRequest = new ReplaceCampaignNegativeKeywordsRequest(); // ReplaceCampaignNegativeKeywordsRequest | 
        try {
            ApiResponse<ReplaceCampaignNegativeKeywords200Response> response = apiInstance.replaceCampaignNegativeKeywordsWithHttpInfo(campaignId, replaceCampaignNegativeKeywordsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceCampaignNegativeKeywords");
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
| **campaignId** | **String**| Platform campaign ID | |
| **replaceCampaignNegativeKeywordsRequest** | [**ReplaceCampaignNegativeKeywordsRequest**](ReplaceCampaignNegativeKeywordsRequest.md)|  | |

### Return type

ApiResponse<[**ReplaceCampaignNegativeKeywords200Response**](ReplaceCampaignNegativeKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords replaced |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## updateAd

> UpdateAd200Response updateAd(adId, updateAdRequest)

Update ad

Patch one or more fields on an ad. Status, budget, targeting, and creative changes are propagated to the platform.  Per-platform support: - **Meta** (Facebook + Instagram): all fields supported. - **TikTok**: status, budget, targeting (via &#x60;/v2/adgroup/update/&#x60;), and creative   (via &#x60;/v2/ad/update/&#x60; patch-style: &#x60;headline&#x60; is ignored, &#x60;body&#x60; becomes &#x60;ad_text&#x60;). - **Google**: status, budget, KEYWORD edits via &#x60;targeting.keywords&#x60; /   &#x60;targeting.negativeKeywords&#x60;, and DEVICE bid adjustments via &#x60;targeting.devices&#x60;.   Each list you send becomes the FULL new set of its kind (criteria not in the   list are removed); a kind left out is untouched. Any other &#x60;targeting&#x60; field   returns 400: Google cannot mutate broad targeting post-create without recreating   the campaign. &#x60;creative&#x60; returns 501. - **LinkedIn**: status, budget, targeting (geo countries only, applied to the   LinkedIn Campaign via PARTIAL_UPDATE), and creative (uploads new media, creates a   replacement inline creative on the same campaign, pauses the old one). - **Pinterest / X / OpenAI Ads**: status + budget only. Sending   &#x60;targeting&#x60; or &#x60;creative&#x60; returns 501 with code &#x60;unsupported_platform_operation&#x60;.   OpenAI Ads budget is lifetime-only (see &#x60;budget.type&#x60; below).  **Google keyword replacement:** These edits affect the ad&#39;s entire ad group, including sibling ads. Positive (&#x60;targeting.keywords&#x60;) and negative (&#x60;targeting.negativeKeywords&#x60;) sets are independent: omit a field to leave that set unchanged, or send &#x60;[]&#x60; to remove every keyword of that kind.  Zernio compares each supplied set with Google&#39;s live criteria by case-insensitive keyword text and match type. A matching criterion is left untouched, retaining its criterion ID, enabled/paused status, keyword-level bid overrides, labels, and criterion-associated history/statistics. Zernio does not reset its quality score; Google continues to calculate scores and statistics normally. Text comparison does not trim whitespace.  A bare string or an object without &#x60;matchType&#x60; means &#x60;broad&#x60;, not the existing criterion&#39;s match type. For example, resending an existing &#x60;{ \&quot;text\&quot;: \&quot;plumber\&quot;, \&quot;matchType\&quot;: \&quot;exact\&quot; }&#x60; preserves it; sending &#x60;\&quot;plumber\&quot;&#x60; instead removes that EXACT criterion and requests a BROAD one. Changing text or match type removes criteria no longer requested and creates any missing criteria. New criteria get new IDs and do not inherit removed criteria&#39;s bid overrides, labels, or history. Historical reporting for a removed criterion is not transferred to its replacement.  To add keywords without replacing a set, use [POST /v1/ads/keywords](https://docs.zernio.com/ad-campaigns/add-ad-keywords). Use &#x60;PATCH /v1/ads/keywords/{keywordId}&#x60; to pause/enable one keyword, or &#x60;DELETE /v1/ads/keywords/{keywordId}&#x60; to remove it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdRequest updateAdRequest = new UpdateAdRequest(); // UpdateAdRequest | 
        try {
            UpdateAd200Response result = apiInstance.updateAd(adId, updateAdRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAd");
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
| **updateAdRequest** | [**UpdateAdRequest**](UpdateAdRequest.md)|  | |

### Return type

[**UpdateAd200Response**](UpdateAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad updated |  -  |
| **400** | Invalid status transition, budget below minimum, or a LinkedIn creative update without imageUrl or videoUrl |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Resource not found |  -  |
| **501** | targeting or creative not supported on the platform (supported on Meta, TikTok, and LinkedIn) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |

## updateAdWithHttpInfo

> ApiResponse<UpdateAd200Response> updateAd updateAdWithHttpInfo(adId, updateAdRequest)

Update ad

Patch one or more fields on an ad. Status, budget, targeting, and creative changes are propagated to the platform.  Per-platform support: - **Meta** (Facebook + Instagram): all fields supported. - **TikTok**: status, budget, targeting (via &#x60;/v2/adgroup/update/&#x60;), and creative   (via &#x60;/v2/ad/update/&#x60; patch-style: &#x60;headline&#x60; is ignored, &#x60;body&#x60; becomes &#x60;ad_text&#x60;). - **Google**: status, budget, KEYWORD edits via &#x60;targeting.keywords&#x60; /   &#x60;targeting.negativeKeywords&#x60;, and DEVICE bid adjustments via &#x60;targeting.devices&#x60;.   Each list you send becomes the FULL new set of its kind (criteria not in the   list are removed); a kind left out is untouched. Any other &#x60;targeting&#x60; field   returns 400: Google cannot mutate broad targeting post-create without recreating   the campaign. &#x60;creative&#x60; returns 501. - **LinkedIn**: status, budget, targeting (geo countries only, applied to the   LinkedIn Campaign via PARTIAL_UPDATE), and creative (uploads new media, creates a   replacement inline creative on the same campaign, pauses the old one). - **Pinterest / X / OpenAI Ads**: status + budget only. Sending   &#x60;targeting&#x60; or &#x60;creative&#x60; returns 501 with code &#x60;unsupported_platform_operation&#x60;.   OpenAI Ads budget is lifetime-only (see &#x60;budget.type&#x60; below).  **Google keyword replacement:** These edits affect the ad&#39;s entire ad group, including sibling ads. Positive (&#x60;targeting.keywords&#x60;) and negative (&#x60;targeting.negativeKeywords&#x60;) sets are independent: omit a field to leave that set unchanged, or send &#x60;[]&#x60; to remove every keyword of that kind.  Zernio compares each supplied set with Google&#39;s live criteria by case-insensitive keyword text and match type. A matching criterion is left untouched, retaining its criterion ID, enabled/paused status, keyword-level bid overrides, labels, and criterion-associated history/statistics. Zernio does not reset its quality score; Google continues to calculate scores and statistics normally. Text comparison does not trim whitespace.  A bare string or an object without &#x60;matchType&#x60; means &#x60;broad&#x60;, not the existing criterion&#39;s match type. For example, resending an existing &#x60;{ \&quot;text\&quot;: \&quot;plumber\&quot;, \&quot;matchType\&quot;: \&quot;exact\&quot; }&#x60; preserves it; sending &#x60;\&quot;plumber\&quot;&#x60; instead removes that EXACT criterion and requests a BROAD one. Changing text or match type removes criteria no longer requested and creates any missing criteria. New criteria get new IDs and do not inherit removed criteria&#39;s bid overrides, labels, or history. Historical reporting for a removed criterion is not transferred to its replacement.  To add keywords without replacing a set, use [POST /v1/ads/keywords](https://docs.zernio.com/ad-campaigns/add-ad-keywords). Use &#x60;PATCH /v1/ads/keywords/{keywordId}&#x60; to pause/enable one keyword, or &#x60;DELETE /v1/ads/keywords/{keywordId}&#x60; to remove it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdRequest updateAdRequest = new UpdateAdRequest(); // UpdateAdRequest | 
        try {
            ApiResponse<UpdateAd200Response> response = apiInstance.updateAdWithHttpInfo(adId, updateAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAd");
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
| **updateAdRequest** | [**UpdateAdRequest**](UpdateAdRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAd200Response**](UpdateAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad updated |  -  |
| **400** | Invalid status transition, budget below minimum, or a LinkedIn creative update without imageUrl or videoUrl |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Resource not found |  -  |
| **501** | targeting or creative not supported on the platform (supported on Meta, TikTok, and LinkedIn) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. |  -  |


## updateAdCampaign

> UpdateAdCampaign200Response updateAdCampaign(campaignId, updateAdCampaignRequest)

Update a campaign

Campaign-level edits. Send at least one of &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;portfolioBidStrategyId&#x60;, &#x60;name&#x60; or &#x60;platformSpecificData&#x60;. An unsupported field is always an error, never a silent drop.  | Body field | Meta | Google | Others | |---|---|---|---| | &#x60;bidStrategy&#x60; | Yes | Yes | 501 | | &#x60;bidAmount&#x60;, &#x60;roasAverageFloor&#x60; | 400 (ad-set level) | Yes | 400 | | &#x60;portfolioBidStrategyId&#x60; | 400 | Yes | 400 | | &#x60;budget&#x60; (CBO; ABO returns 409) | Yes | 501 | 501 | | &#x60;name&#x60; | Yes | 501 | 501 | | &#x60;platformSpecificData.spendCap&#x60; | Yes | 400 | 400 | | &#x60;accountId&#x60; (empty campaigns) | Yes | - | - |  On Google: &#x60;LOWEST_COST_WITHOUT_CAP&#x60; &#x3D; Maximize Conversions, &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Target CPA, &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60; &#x3D; Target ROAS, &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Maximize Clicks with a CPC ceiling; &#x60;portfolioBidStrategyId&#x60; attaches a portfolio strategy instead (exclusive with &#x60;bidStrategy&#x60;). Setting the standard triplet on a campaign that is currently on a PORTFOLIO strategy is rejected: detach it in Google Ads first, since it is shared across campaigns.  &#x60;accountId&#x60; forwards the update straight to Meta for a campaign with zero ads, which would otherwise 404; the response then carries &#x60;updated: 0&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignRequest updateAdCampaignRequest = new UpdateAdCampaignRequest(); // UpdateAdCampaignRequest | 
        try {
            UpdateAdCampaign200Response result = apiInstance.updateAdCampaign(campaignId, updateAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignRequest** | [**UpdateAdCampaignRequest**](UpdateAdCampaignRequest.md)|  | |

### Return type

[**UpdateAdCampaign200Response**](UpdateAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid input, or a field the resolved platform does not support at the campaign level (see the support table) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign is ABO. Route to /v1/ads/ad-sets/{adSetId} instead |  -  |
| **501** | Operation not supported on this platform |  -  |

## updateAdCampaignWithHttpInfo

> ApiResponse<UpdateAdCampaign200Response> updateAdCampaign updateAdCampaignWithHttpInfo(campaignId, updateAdCampaignRequest)

Update a campaign

Campaign-level edits. Send at least one of &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;portfolioBidStrategyId&#x60;, &#x60;name&#x60; or &#x60;platformSpecificData&#x60;. An unsupported field is always an error, never a silent drop.  | Body field | Meta | Google | Others | |---|---|---|---| | &#x60;bidStrategy&#x60; | Yes | Yes | 501 | | &#x60;bidAmount&#x60;, &#x60;roasAverageFloor&#x60; | 400 (ad-set level) | Yes | 400 | | &#x60;portfolioBidStrategyId&#x60; | 400 | Yes | 400 | | &#x60;budget&#x60; (CBO; ABO returns 409) | Yes | 501 | 501 | | &#x60;name&#x60; | Yes | 501 | 501 | | &#x60;platformSpecificData.spendCap&#x60; | Yes | 400 | 400 | | &#x60;accountId&#x60; (empty campaigns) | Yes | - | - |  On Google: &#x60;LOWEST_COST_WITHOUT_CAP&#x60; &#x3D; Maximize Conversions, &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Target CPA, &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60; &#x3D; Target ROAS, &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Maximize Clicks with a CPC ceiling; &#x60;portfolioBidStrategyId&#x60; attaches a portfolio strategy instead (exclusive with &#x60;bidStrategy&#x60;). Setting the standard triplet on a campaign that is currently on a PORTFOLIO strategy is rejected: detach it in Google Ads first, since it is shared across campaigns.  &#x60;accountId&#x60; forwards the update straight to Meta for a campaign with zero ads, which would otherwise 404; the response then carries &#x60;updated: 0&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignRequest updateAdCampaignRequest = new UpdateAdCampaignRequest(); // UpdateAdCampaignRequest | 
        try {
            ApiResponse<UpdateAdCampaign200Response> response = apiInstance.updateAdCampaignWithHttpInfo(campaignId, updateAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignRequest** | [**UpdateAdCampaignRequest**](UpdateAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCampaign200Response**](UpdateAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid input, or a field the resolved platform does not support at the campaign level (see the support table) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign is ABO. Route to /v1/ads/ad-sets/{adSetId} instead |  -  |
| **501** | Operation not supported on this platform |  -  |


## updateAdCampaignStatus

> UpdateAdCampaignStatus200Response updateAdCampaignStatus(campaignId, updateAdCampaignStatusRequest)

Pause or resume a campaign

Writes the campaign&#39;s own on/off switch, then lets the platform cascade delivery to its ad sets and ads. Makes one platform API call, not one per ad.  The switch is always written, whatever delivery status the ads underneath report: an ad still in review does not block resuming its campaign. The echoed &#x60;status&#x60; is the confirmation that it landed.  &#x60;updated&#x60; / &#x60;skipped&#x60; describe only the ads whose own stored status CHANGED alongside it, so &#x60;updated: 0&#x60; is a normal successful response, not a no-op. Ads are skipped when they are in a terminal status (rejected, completed, cancelled), already in the target state, or switched on but not yet delivering. The last group keeps its &#x60;pending_review&#x60; / &#x60;error&#x60; status until the platform reports what it became. &#x60;skippedReasons&#x60; names which case applies.  On Meta this flips the campaign only. An ad set paused in its own right stays paused, so pair this with PUT /v1/ads/ad-sets/{adSetId}/status when you also need the ad set switched back on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            UpdateAdCampaignStatus200Response result = apiInstance.updateAdCampaignStatus(campaignId, updateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaignStatus");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**UpdateAdCampaignStatus200Response**](UpdateAdCampaignStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign status updated |  -  |
| **400** | Invalid input or campaign spans multiple accounts |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | No ads found for this campaign |  -  |

## updateAdCampaignStatusWithHttpInfo

> ApiResponse<UpdateAdCampaignStatus200Response> updateAdCampaignStatus updateAdCampaignStatusWithHttpInfo(campaignId, updateAdCampaignStatusRequest)

Pause or resume a campaign

Writes the campaign&#39;s own on/off switch, then lets the platform cascade delivery to its ad sets and ads. Makes one platform API call, not one per ad.  The switch is always written, whatever delivery status the ads underneath report: an ad still in review does not block resuming its campaign. The echoed &#x60;status&#x60; is the confirmation that it landed.  &#x60;updated&#x60; / &#x60;skipped&#x60; describe only the ads whose own stored status CHANGED alongside it, so &#x60;updated: 0&#x60; is a normal successful response, not a no-op. Ads are skipped when they are in a terminal status (rejected, completed, cancelled), already in the target state, or switched on but not yet delivering. The last group keeps its &#x60;pending_review&#x60; / &#x60;error&#x60; status until the platform reports what it became. &#x60;skippedReasons&#x60; names which case applies.  On Meta this flips the campaign only. An ad set paused in its own right stays paused, so pair this with PUT /v1/ads/ad-sets/{adSetId}/status when you also need the ad set switched back on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<UpdateAdCampaignStatus200Response> response = apiInstance.updateAdCampaignStatusWithHttpInfo(campaignId, updateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaignStatus");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCampaignStatus200Response**](UpdateAdCampaignStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign status updated |  -  |
| **400** | Invalid input or campaign spans multiple accounts |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | No ads found for this campaign |  -  |


## updateAdKeyword

> UpdateAdKeyword200Response updateAdKeyword(keywordId, updateAdKeywordRequest)

Pause or enable a Search keyword

Changes &#x60;ad_group_criterion.status&#x60; for one keyword criterion (M.140). Negative keywords have no status on Google and cannot be paused or enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (not the Google criterion ID)
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            UpdateAdKeyword200Response result = apiInstance.updateAdKeyword(keywordId, updateAdKeywordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdKeyword");
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
| **keywordId** | **String**| Zernio keyword ID (not the Google criterion ID) | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

[**UpdateAdKeyword200Response**](UpdateAdKeyword200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keyword updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Keyword not found |  -  |
| **422** | Negative keywords have no status on Google; they cannot be paused or enabled. |  -  |

## updateAdKeywordWithHttpInfo

> ApiResponse<UpdateAdKeyword200Response> updateAdKeyword updateAdKeywordWithHttpInfo(keywordId, updateAdKeywordRequest)

Pause or enable a Search keyword

Changes &#x60;ad_group_criterion.status&#x60; for one keyword criterion (M.140). Negative keywords have no status on Google and cannot be paused or enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (not the Google criterion ID)
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            ApiResponse<UpdateAdKeyword200Response> response = apiInstance.updateAdKeywordWithHttpInfo(keywordId, updateAdKeywordRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdKeyword");
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
| **keywordId** | **String**| Zernio keyword ID (not the Google criterion ID) | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdKeyword200Response**](UpdateAdKeyword200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keyword updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Keyword not found |  -  |
| **422** | Negative keywords have no status on Google; they cannot be paused or enabled. |  -  |


## updateAdSet

> UpdateAdSet200Response updateAdSet(adSetId, updateAdSetRequest)

Update an ad set

Ad-set-level writes. Use this for ABO budget updates, ad-set-scoped pause/resume, bid-strategy edits, Meta value-rule-set attach/detach, and Meta-only post-launch delivery settings via &#x60;platformSpecificData&#x60;. At least one updatable field is required.  Value rule sets (Meta only, see &#x60;/v1/ads/value-rule-sets&#x60;): - ATTACH or REPLACE: send &#x60;valueRuleSetId&#x60;. Attachment is driven by the id&#39;s   presence, so &#x60;valueRulesApplied: true&#x60; is optional. Sending a different id   replaces the previous association; there is no separate replace call. - DETACH: send &#x60;valueRulesApplied: false&#x60; and OMIT &#x60;valueRuleSetId&#x60;. - Sending &#x60;valueRulesApplied: false&#x60; TOGETHER with &#x60;valueRuleSetId&#x60; returns 400   &#x60;mutually_exclusive_fields&#x60;. This is deliberate: Meta attaches the rule set   whenever &#x60;value_rule_set_id&#x60; is present, even with &#x60;value_rules_applied&#x60; false,   so echoing stored state while asking to detach would silently keep the bid   adjustments live. - Eligibility: only ad sets on &#x60;LOWEST_COST_WITHOUT_CAP&#x60; or &#x60;COST_CAP&#x60;. Meta   rejects the rest server-side. - Read back with &#x60;GET /v1/ads/ad-sets/{adSetId}?fields&#x3D;value_rule_set_id&#x60;. Meta   does not document &#x60;value_rules_applied&#x60; as a readable ad-set field, so the   boolean cannot be read back.  Bid strategy compatibility (per Meta&#39;s spec): - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: no &#x60;bidAmount&#x60;, no &#x60;roasAverageFloor&#x60;. - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; / &#x60;COST_CAP&#x60;: &#x60;bidAmount&#x60; REQUIRED (whole currency units). - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60;: &#x60;roasAverageFloor&#x60; REQUIRED (decimal multiplier, e.g. 2.0 &#x3D; 2.0x ROAS). - Meta only: send &#x60;bidAmount&#x60; WITHOUT &#x60;bidStrategy&#x60; to change the cap amount on an ad set   under a COST_CAP / LOWEST_COST_WITH_BID_CAP parent campaign, leaving the strategy itself   (inherited from the campaign) untouched. &#x60;roasAverageFloor&#x60; without &#x60;bidStrategy&#x60; is   rejected (it has no meaning outside LOWEST_COST_WITH_MIN_ROAS).  Delivery settings are validated by Meta against the campaign objective; incompatible combinations (e.g. a billingEvent the optimization goal doesn&#39;t allow) surface as 400s from Meta.  When updating &#x60;budget&#x60; on an ABO campaign: if the parent campaign is CBO, the response is 409 with code BUDGET_LEVEL_MISMATCH. Route to PUT /v1/ads/campaigns/{campaignId} instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdSetRequest updateAdSetRequest = new UpdateAdSetRequest(); // UpdateAdSetRequest | 
        try {
            UpdateAdSet200Response result = apiInstance.updateAdSet(adSetId, updateAdSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSet");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdSetRequest** | [**UpdateAdSetRequest**](UpdateAdSetRequest.md)|  | |

### Return type

[**UpdateAdSet200Response**](UpdateAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad set not found |  -  |
| **409** | Campaign is CBO. Route to /v1/ads/campaigns/{campaignId} instead |  -  |
| **422** | bidStrategy is LOWEST_COST_WITH_MIN_ROAS on OpenAI (unsupported: no ROAS-based bidding) |  -  |
| **501** | bidStrategy not supported on the platform (Meta, TikTok, and OpenAI only) |  -  |

## updateAdSetWithHttpInfo

> ApiResponse<UpdateAdSet200Response> updateAdSet updateAdSetWithHttpInfo(adSetId, updateAdSetRequest)

Update an ad set

Ad-set-level writes. Use this for ABO budget updates, ad-set-scoped pause/resume, bid-strategy edits, Meta value-rule-set attach/detach, and Meta-only post-launch delivery settings via &#x60;platformSpecificData&#x60;. At least one updatable field is required.  Value rule sets (Meta only, see &#x60;/v1/ads/value-rule-sets&#x60;): - ATTACH or REPLACE: send &#x60;valueRuleSetId&#x60;. Attachment is driven by the id&#39;s   presence, so &#x60;valueRulesApplied: true&#x60; is optional. Sending a different id   replaces the previous association; there is no separate replace call. - DETACH: send &#x60;valueRulesApplied: false&#x60; and OMIT &#x60;valueRuleSetId&#x60;. - Sending &#x60;valueRulesApplied: false&#x60; TOGETHER with &#x60;valueRuleSetId&#x60; returns 400   &#x60;mutually_exclusive_fields&#x60;. This is deliberate: Meta attaches the rule set   whenever &#x60;value_rule_set_id&#x60; is present, even with &#x60;value_rules_applied&#x60; false,   so echoing stored state while asking to detach would silently keep the bid   adjustments live. - Eligibility: only ad sets on &#x60;LOWEST_COST_WITHOUT_CAP&#x60; or &#x60;COST_CAP&#x60;. Meta   rejects the rest server-side. - Read back with &#x60;GET /v1/ads/ad-sets/{adSetId}?fields&#x3D;value_rule_set_id&#x60;. Meta   does not document &#x60;value_rules_applied&#x60; as a readable ad-set field, so the   boolean cannot be read back.  Bid strategy compatibility (per Meta&#39;s spec): - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: no &#x60;bidAmount&#x60;, no &#x60;roasAverageFloor&#x60;. - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; / &#x60;COST_CAP&#x60;: &#x60;bidAmount&#x60; REQUIRED (whole currency units). - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60;: &#x60;roasAverageFloor&#x60; REQUIRED (decimal multiplier, e.g. 2.0 &#x3D; 2.0x ROAS). - Meta only: send &#x60;bidAmount&#x60; WITHOUT &#x60;bidStrategy&#x60; to change the cap amount on an ad set   under a COST_CAP / LOWEST_COST_WITH_BID_CAP parent campaign, leaving the strategy itself   (inherited from the campaign) untouched. &#x60;roasAverageFloor&#x60; without &#x60;bidStrategy&#x60; is   rejected (it has no meaning outside LOWEST_COST_WITH_MIN_ROAS).  Delivery settings are validated by Meta against the campaign objective; incompatible combinations (e.g. a billingEvent the optimization goal doesn&#39;t allow) surface as 400s from Meta.  When updating &#x60;budget&#x60; on an ABO campaign: if the parent campaign is CBO, the response is 409 with code BUDGET_LEVEL_MISMATCH. Route to PUT /v1/ads/campaigns/{campaignId} instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdSetRequest updateAdSetRequest = new UpdateAdSetRequest(); // UpdateAdSetRequest | 
        try {
            ApiResponse<UpdateAdSet200Response> response = apiInstance.updateAdSetWithHttpInfo(adSetId, updateAdSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSet");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdSetRequest** | [**UpdateAdSetRequest**](UpdateAdSetRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdSet200Response**](UpdateAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad set not found |  -  |
| **409** | Campaign is CBO. Route to /v1/ads/campaigns/{campaignId} instead |  -  |
| **422** | bidStrategy is LOWEST_COST_WITH_MIN_ROAS on OpenAI (unsupported: no ROAS-based bidding) |  -  |
| **501** | bidStrategy not supported on the platform (Meta, TikTok, and OpenAI only) |  -  |


## updateAdSetStatus

> UpdateAdSetStatus200Response updateAdSetStatus(adSetId, updateAdCampaignStatusRequest)

Pause or resume a single ad set

Ad-set-scoped pause/resume (doesn&#39;t touch sibling ad sets). Thin wrapper over PUT /v1/ads/ad-sets/{adSetId} for callers that only want the status toggle and prefer a symmetric URL to /v1/ads/campaigns/{campaignId}/status.  On Meta and LinkedIn this writes the ad set&#39;s own on/off switch (Meta: &#x60;configured_status&#x60;), whatever delivery status its ads report: an ad still in review does not block resuming its ad set. The echoed &#x60;status&#x60; is the confirmation that it landed. Where the platform has no ad-set switch (TikTok and others) the toggle is emulated by flipping the child ads; a call with no actionable ad then writes nothing and returns a &#x60;message&#x60; with no &#x60;status&#x60;.  &#x60;updated&#x60; / &#x60;skipped&#x60; describe only the ads whose own stored status CHANGED alongside the switch, so &#x60;updated: 0&#x60; is a normal successful response. See &#x60;skippedReasons&#x60; for which of the three cases applies (terminal, already in the target state, or switched on but not yet delivering).  A campaign created paused needs its campaign resumed as well: pair this with PUT /v1/ads/campaigns/{campaignId}/status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            UpdateAdSetStatus200Response result = apiInstance.updateAdSetStatus(adSetId, updateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSetStatus");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**UpdateAdSetStatus200Response**](UpdateAdSetStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set status updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad set not found |  -  |

## updateAdSetStatusWithHttpInfo

> ApiResponse<UpdateAdSetStatus200Response> updateAdSetStatus updateAdSetStatusWithHttpInfo(adSetId, updateAdCampaignStatusRequest)

Pause or resume a single ad set

Ad-set-scoped pause/resume (doesn&#39;t touch sibling ad sets). Thin wrapper over PUT /v1/ads/ad-sets/{adSetId} for callers that only want the status toggle and prefer a symmetric URL to /v1/ads/campaigns/{campaignId}/status.  On Meta and LinkedIn this writes the ad set&#39;s own on/off switch (Meta: &#x60;configured_status&#x60;), whatever delivery status its ads report: an ad still in review does not block resuming its ad set. The echoed &#x60;status&#x60; is the confirmation that it landed. Where the platform has no ad-set switch (TikTok and others) the toggle is emulated by flipping the child ads; a call with no actionable ad then writes nothing and returns a &#x60;message&#x60; with no &#x60;status&#x60;.  &#x60;updated&#x60; / &#x60;skipped&#x60; describe only the ads whose own stored status CHANGED alongside the switch, so &#x60;updated: 0&#x60; is a normal successful response. See &#x60;skippedReasons&#x60; for which of the three cases applies (terminal, already in the target state, or switched on but not yet delivering).  A campaign created paused needs its campaign resumed as well: pair this with PUT /v1/ads/campaigns/{campaignId}/status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<UpdateAdSetStatus200Response> response = apiInstance.updateAdSetStatusWithHttpInfo(adSetId, updateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSetStatus");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdSetStatus200Response**](UpdateAdSetStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set status updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad set not found |  -  |


## updateAdStatus

> UpdateAdStatus200Response updateAdStatus(adId, updateAdKeywordRequest)

Pause or resume a single ad

Ad-scoped pause/resume: touches ONLY this ad, never its parent ad set or campaign (so sibling ads keep running). Thin wrapper over the &#x60;status&#x60; field of PUT /v1/ads/{adId}, for callers that want a URL symmetric to /v1/ads/campaigns/{campaignId}/status and /v1/ads/ad-sets/{adSetId}/status.  &#x60;{adId}&#x60; accepts the same identifier dialects as GET/PUT /v1/ads/{adId} (Zernio hex &#x60;_id&#x60;, Meta numeric &#x60;platformAdId&#x60;, or the creative&#39;s effective story/media IDs). &#x60;platform&#x60; is inferred from the ad, so it&#39;s not required in the body. Ads in terminal statuses (rejected, completed, cancelled) and no-op flips (already in the target state) are skipped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs.
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            UpdateAdStatus200Response result = apiInstance.updateAdStatus(adId, updateAdKeywordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdStatus");
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
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

[**UpdateAdStatus200Response**](UpdateAdStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad status updated (or skipped when no change was needed) |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad not found |  -  |

## updateAdStatusWithHttpInfo

> ApiResponse<UpdateAdStatus200Response> updateAdStatus updateAdStatusWithHttpInfo(adId, updateAdKeywordRequest)

Pause or resume a single ad

Ad-scoped pause/resume: touches ONLY this ad, never its parent ad set or campaign (so sibling ads keep running). Thin wrapper over the &#x60;status&#x60; field of PUT /v1/ads/{adId}, for callers that want a URL symmetric to /v1/ads/campaigns/{campaignId}/status and /v1/ads/ad-sets/{adSetId}/status.  &#x60;{adId}&#x60; accepts the same identifier dialects as GET/PUT /v1/ads/{adId} (Zernio hex &#x60;_id&#x60;, Meta numeric &#x60;platformAdId&#x60;, or the creative&#39;s effective story/media IDs). &#x60;platform&#x60; is inferred from the ad, so it&#39;s not required in the body. Ads in terminal statuses (rejected, completed, cancelled) and no-op flips (already in the target state) are skipped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs.
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            ApiResponse<UpdateAdStatus200Response> response = apiInstance.updateAdStatusWithHttpInfo(adId, updateAdKeywordRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdStatus");
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
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdStatus200Response**](UpdateAdStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad status updated (or skipped when no change was needed) |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Ad not found |  -  |


## updateBidStrategy

> UpdateBidStrategy200Response updateBidStrategy(strategyId, updateBidStrategyRequest)

Update a Google Ads portfolio bid strategy

Renames or retargets a portfolio bid strategy. The strategy&#39;s status is output only on Google&#39;s side, so it cannot be changed here; remove a strategy in Google Ads. &#x60;type&#x60; is only needed alongside &#x60;targetCpa&#x60;/&#x60;targetRoas&#x60; to disambiguate the field Google writes to (TARGET_CPA and MAXIMIZE_CONVERSIONS both take a target CPA; TARGET_ROAS and MAXIMIZE_CONVERSION_VALUE both take a target ROAS); the strategy&#39;s family is otherwise immutable once created.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String strategyId = "strategyId_example"; // String | Numeric Google Ads bid strategy id.
        UpdateBidStrategyRequest updateBidStrategyRequest = new UpdateBidStrategyRequest(); // UpdateBidStrategyRequest | 
        try {
            UpdateBidStrategy200Response result = apiInstance.updateBidStrategy(strategyId, updateBidStrategyRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateBidStrategy");
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
| **strategyId** | **String**| Numeric Google Ads bid strategy id. | |
| **updateBidStrategyRequest** | [**UpdateBidStrategyRequest**](UpdateBidStrategyRequest.md)|  | |

### Return type

[**UpdateBidStrategy200Response**](UpdateBidStrategy200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bid strategy updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## updateBidStrategyWithHttpInfo

> ApiResponse<UpdateBidStrategy200Response> updateBidStrategy updateBidStrategyWithHttpInfo(strategyId, updateBidStrategyRequest)

Update a Google Ads portfolio bid strategy

Renames or retargets a portfolio bid strategy. The strategy&#39;s status is output only on Google&#39;s side, so it cannot be changed here; remove a strategy in Google Ads. &#x60;type&#x60; is only needed alongside &#x60;targetCpa&#x60;/&#x60;targetRoas&#x60; to disambiguate the field Google writes to (TARGET_CPA and MAXIMIZE_CONVERSIONS both take a target CPA; TARGET_ROAS and MAXIMIZE_CONVERSION_VALUE both take a target ROAS); the strategy&#39;s family is otherwise immutable once created.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String strategyId = "strategyId_example"; // String | Numeric Google Ads bid strategy id.
        UpdateBidStrategyRequest updateBidStrategyRequest = new UpdateBidStrategyRequest(); // UpdateBidStrategyRequest | 
        try {
            ApiResponse<UpdateBidStrategy200Response> response = apiInstance.updateBidStrategyWithHttpInfo(strategyId, updateBidStrategyRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateBidStrategy");
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
| **strategyId** | **String**| Numeric Google Ads bid strategy id. | |
| **updateBidStrategyRequest** | [**UpdateBidStrategyRequest**](UpdateBidStrategyRequest.md)|  | |

### Return type

ApiResponse<[**UpdateBidStrategy200Response**](UpdateBidStrategy200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bid strategy updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## updateCampaignTargeting

> UpdateCampaignTargeting200Response updateCampaignTargeting(campaignId, updateCampaignTargetingRequest)

Edit a Google campaign&#39;s device, location, or language targeting

Google Ads compliance row M.10: geo and language targeting set at creation must stay editable afterwards. Send at least one of &#x60;devices&#x60;, &#x60;locations&#x60;, &#x60;languages&#x60;; each provided field REPLACES that field&#39;s existing criteria on the campaign (a full set, not a delta). Fields left out of the body are untouched. Google only; every other platform returns 501.  &#x60;locations&#x60; accepts the same shapes as campaign creation: a bare array of ISO country codes, or an object with &#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; key lists (&#x60;key&#x60; from GET /v1/ads/targeting/search?dimension&#x3D;geo). Negative (excluded) locations are left untouched by this endpoint.  &#x60;languages&#x60; is an array of Google&#39;s language codes (ISO 639-1, plus variants such as &#x60;zh_CN&#x60;); an unknown code returns 400.  The response includes the refreshed &#x60;devices&#x60;/&#x60;locations&#x60;/&#x60;languages&#x60; state read back from Google after the edit, and invalidates the cached copy &#x60;GET&#x60; on this campaign would otherwise keep serving. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        UpdateCampaignTargetingRequest updateCampaignTargetingRequest = new UpdateCampaignTargetingRequest(); // UpdateCampaignTargetingRequest | 
        try {
            UpdateCampaignTargeting200Response result = apiInstance.updateCampaignTargeting(campaignId, updateCampaignTargetingRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignTargeting");
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
| **campaignId** | **String**| Google platform campaign ID | |
| **updateCampaignTargetingRequest** | [**UpdateCampaignTargetingRequest**](UpdateCampaignTargetingRequest.md)|  | |

### Return type

[**UpdateCampaignTargeting200Response**](UpdateCampaignTargeting200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Targeting updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## updateCampaignTargetingWithHttpInfo

> ApiResponse<UpdateCampaignTargeting200Response> updateCampaignTargeting updateCampaignTargetingWithHttpInfo(campaignId, updateCampaignTargetingRequest)

Edit a Google campaign&#39;s device, location, or language targeting

Google Ads compliance row M.10: geo and language targeting set at creation must stay editable afterwards. Send at least one of &#x60;devices&#x60;, &#x60;locations&#x60;, &#x60;languages&#x60;; each provided field REPLACES that field&#39;s existing criteria on the campaign (a full set, not a delta). Fields left out of the body are untouched. Google only; every other platform returns 501.  &#x60;locations&#x60; accepts the same shapes as campaign creation: a bare array of ISO country codes, or an object with &#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; key lists (&#x60;key&#x60; from GET /v1/ads/targeting/search?dimension&#x3D;geo). Negative (excluded) locations are left untouched by this endpoint.  &#x60;languages&#x60; is an array of Google&#39;s language codes (ISO 639-1, plus variants such as &#x60;zh_CN&#x60;); an unknown code returns 400.  The response includes the refreshed &#x60;devices&#x60;/&#x60;locations&#x60;/&#x60;languages&#x60; state read back from Google after the edit, and invalidates the cached copy &#x60;GET&#x60; on this campaign would otherwise keep serving. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        UpdateCampaignTargetingRequest updateCampaignTargetingRequest = new UpdateCampaignTargetingRequest(); // UpdateCampaignTargetingRequest | 
        try {
            ApiResponse<UpdateCampaignTargeting200Response> response = apiInstance.updateCampaignTargetingWithHttpInfo(campaignId, updateCampaignTargetingRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignTargeting");
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
| **campaignId** | **String**| Google platform campaign ID | |
| **updateCampaignTargetingRequest** | [**UpdateCampaignTargetingRequest**](UpdateCampaignTargetingRequest.md)|  | |

### Return type

ApiResponse<[**UpdateCampaignTargeting200Response**](UpdateCampaignTargeting200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Targeting updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

