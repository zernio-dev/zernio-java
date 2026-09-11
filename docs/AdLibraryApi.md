# AdLibraryApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchAdLibrary**](AdLibraryApi.md#searchAdLibrary) | **GET** /v1/ads/library | Search the public Ad Library |
| [**searchAdLibraryWithHttpInfo**](AdLibraryApi.md#searchAdLibraryWithHttpInfo) | **GET** /v1/ads/library | Search the public Ad Library |



## searchAdLibrary

> SearchAdLibrary200Response searchAdLibrary(platform, accountId, q, pageIds, advertiser, countries, adType, status, platforms, mediaType, languages, since, until, searchType, fields, limit, after)

Search the public Ad Library

Competitor and market research over the public ad archives. Meta&#39;s Ad Library (&#x60;GET /ads_archive&#x60;) is searched with Zernio&#39;s own developer access, so &#x60;platform&#x3D;meta&#x60; needs no connected account at all. LinkedIn&#39;s Ad Library (&#x60;GET /rest/adLibrary&#x60;) runs on a connected &#x60;linkedin&#x60; / &#x60;linkedinads&#x60; account, passed as &#x60;accountId&#x60;. Passing a Meta account as &#x60;accountId&#x60; also selects Meta. Rows are returned in the platform&#39;s raw shape under &#x60;data&#x60;; &#x60;paging.after&#x60; is an opaque cursor on both (&#x60;null&#x60; when exhausted).  **Meta coverage.** Political and social-issue ads are searchable worldwide. Every other ad is in the archive only if it was delivered to the EU or UK within the last year, so a US-only commercial advertiser is invisible. Spend, impressions and demographics are political-only fields and are left out of the default projection; request them via &#x60;fields&#x60;. All customers share Zernio&#39;s Meta quota, so a &#x60;429&#x60; means back off for a minute.  **LinkedIn coverage.** Ads served after June 1 2023, worldwide, kept for a year after their last impression. EU-delivered ads carry impression ranges and the disclosed targeting facets. Pages are capped at 25 ads (&#x60;limit&#x60; &gt; 25 is a 400); &#x60;after&#x60; is the next offset.  Which params apply: &#x60;q&#x60;, &#x60;countries&#x60;, &#x60;since&#x60;, &#x60;until&#x60;, &#x60;limit&#x60;, &#x60;after&#x60; on both; &#x60;pageIds&#x60;, &#x60;adType&#x60;, &#x60;status&#x60;, &#x60;platforms&#x60;, &#x60;mediaType&#x60;, &#x60;languages&#x60;, &#x60;searchType&#x60;, &#x60;fields&#x60; are Meta-only; &#x60;advertiser&#x60; is LinkedIn-only. Passing a param the account&#39;s platform does not support is a 400 naming the param.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdLibraryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdLibraryApi apiInstance = new AdLibraryApi(defaultClient);
        String platform = "meta"; // String | Which archive to search. `meta` needs no accountId. Required unless accountId is given.
        String accountId = "accountId_example"; // String | Zernio SocialAccount id. Required for LinkedIn (linkedin / linkedinads: its token searches). Optional for Meta, where any facebook / instagram / metaads account only selects the platform.
        String q = "q_example"; // String | Keyword search. Meta does not translate it, so write it in the ads' language. Required unless pageIds (Meta) or advertiser (LinkedIn) is given.
        String pageIds = "pageIds_example"; // String | Meta only. Comma-separated Facebook Page ids (max 10) whose ads to list.
        String advertiser = "advertiser_example"; // String | LinkedIn only. Advertiser (Page) name to search.
        String countries = "countries_example"; // String | Comma-separated ISO 3166-1 alpha-2 codes the ads reached. Meta defaults to ALL (an explicit ALL is Meta-only); LinkedIn searches every market when omitted.
        String adType = "ALL"; // String | Meta only.
        String status = "ACTIVE"; // String | Meta only. ACTIVE = eligible for delivery right now.
        String platforms = "platforms_example"; // String | Meta only. Comma-separated publisher platforms: FACEBOOK, INSTAGRAM, AUDIENCE_NETWORK, MESSENGER, WHATSAPP, OCULUS, THREADS, STREAMING_SERVICES.
        String mediaType = "ALL"; // String | Meta only.
        String languages = "languages_example"; // String | Meta only. Comma-separated ISO 639-1 codes of the ad text.
        LocalDate since = LocalDate.now(); // LocalDate | Earliest delivery date (YYYY-MM-DD).
        LocalDate until = LocalDate.now(); // LocalDate | Latest delivery date (YYYY-MM-DD).
        String searchType = "KEYWORD_UNORDERED"; // String | Meta only. Whether q matches words in any order or as an exact phrase (comma-separate phrases to match all of them).
        String fields = "id,page_name,ad_delivery_start_time,ad_creative_bodies"; // String | Meta only. Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently.
        Integer limit = 25; // Integer | Rows per page. LinkedIn accepts at most 25.
        String after = "after_example"; // String | paging.after of the previous page.
        try {
            SearchAdLibrary200Response result = apiInstance.searchAdLibrary(platform, accountId, q, pageIds, advertiser, countries, adType, status, platforms, mediaType, languages, since, until, searchType, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdLibraryApi#searchAdLibrary");
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
| **platform** | **String**| Which archive to search. &#x60;meta&#x60; needs no accountId. Required unless accountId is given. | [optional] [enum: meta, linkedin] |
| **accountId** | **String**| Zernio SocialAccount id. Required for LinkedIn (linkedin / linkedinads: its token searches). Optional for Meta, where any facebook / instagram / metaads account only selects the platform. | [optional] |
| **q** | **String**| Keyword search. Meta does not translate it, so write it in the ads&#39; language. Required unless pageIds (Meta) or advertiser (LinkedIn) is given. | [optional] |
| **pageIds** | **String**| Meta only. Comma-separated Facebook Page ids (max 10) whose ads to list. | [optional] |
| **advertiser** | **String**| LinkedIn only. Advertiser (Page) name to search. | [optional] |
| **countries** | **String**| Comma-separated ISO 3166-1 alpha-2 codes the ads reached. Meta defaults to ALL (an explicit ALL is Meta-only); LinkedIn searches every market when omitted. | [optional] |
| **adType** | **String**| Meta only. | [optional] [default to ALL] [enum: ALL, POLITICAL_AND_ISSUE_ADS, HOUSING_ADS, EMPLOYMENT_ADS, FINANCIAL_PRODUCTS_AND_SERVICES_ADS] |
| **status** | **String**| Meta only. ACTIVE &#x3D; eligible for delivery right now. | [optional] [default to ACTIVE] [enum: ACTIVE, INACTIVE, ALL] |
| **platforms** | **String**| Meta only. Comma-separated publisher platforms: FACEBOOK, INSTAGRAM, AUDIENCE_NETWORK, MESSENGER, WHATSAPP, OCULUS, THREADS, STREAMING_SERVICES. | [optional] |
| **mediaType** | **String**| Meta only. | [optional] [enum: ALL, IMAGE, MEME, VIDEO, NONE] |
| **languages** | **String**| Meta only. Comma-separated ISO 639-1 codes of the ad text. | [optional] |
| **since** | **LocalDate**| Earliest delivery date (YYYY-MM-DD). | [optional] |
| **until** | **LocalDate**| Latest delivery date (YYYY-MM-DD). | [optional] |
| **searchType** | **String**| Meta only. Whether q matches words in any order or as an exact phrase (comma-separate phrases to match all of them). | [optional] [default to KEYWORD_UNORDERED] [enum: KEYWORD_UNORDERED, KEYWORD_EXACT_PHRASE] |
| **fields** | **String**| Meta only. Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently. | [optional] |
| **limit** | **Integer**| Rows per page. LinkedIn accepts at most 25. | [optional] [default to 25] |
| **after** | **String**| paging.after of the previous page. | [optional] |

### Return type

[**SearchAdLibrary200Response**](SearchAdLibrary200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Archived ads (raw platform shape) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included on usage-based plans), or &#x60;payment_required&#x60;: the billing owner has no payment method on file and no legacy paid plan. Searches are free; the card keeps the shared archive quota for real accounts. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta and LinkedIn accounts |  -  |
| **503** | Meta&#39;s Ad Library is unavailable on Zernio&#39;s side (&#x60;PLATFORM_DISABLED&#x60;); LinkedIn searches are unaffected. |  -  |

## searchAdLibraryWithHttpInfo

> ApiResponse<SearchAdLibrary200Response> searchAdLibrary searchAdLibraryWithHttpInfo(platform, accountId, q, pageIds, advertiser, countries, adType, status, platforms, mediaType, languages, since, until, searchType, fields, limit, after)

Search the public Ad Library

Competitor and market research over the public ad archives. Meta&#39;s Ad Library (&#x60;GET /ads_archive&#x60;) is searched with Zernio&#39;s own developer access, so &#x60;platform&#x3D;meta&#x60; needs no connected account at all. LinkedIn&#39;s Ad Library (&#x60;GET /rest/adLibrary&#x60;) runs on a connected &#x60;linkedin&#x60; / &#x60;linkedinads&#x60; account, passed as &#x60;accountId&#x60;. Passing a Meta account as &#x60;accountId&#x60; also selects Meta. Rows are returned in the platform&#39;s raw shape under &#x60;data&#x60;; &#x60;paging.after&#x60; is an opaque cursor on both (&#x60;null&#x60; when exhausted).  **Meta coverage.** Political and social-issue ads are searchable worldwide. Every other ad is in the archive only if it was delivered to the EU or UK within the last year, so a US-only commercial advertiser is invisible. Spend, impressions and demographics are political-only fields and are left out of the default projection; request them via &#x60;fields&#x60;. All customers share Zernio&#39;s Meta quota, so a &#x60;429&#x60; means back off for a minute.  **LinkedIn coverage.** Ads served after June 1 2023, worldwide, kept for a year after their last impression. EU-delivered ads carry impression ranges and the disclosed targeting facets. Pages are capped at 25 ads (&#x60;limit&#x60; &gt; 25 is a 400); &#x60;after&#x60; is the next offset.  Which params apply: &#x60;q&#x60;, &#x60;countries&#x60;, &#x60;since&#x60;, &#x60;until&#x60;, &#x60;limit&#x60;, &#x60;after&#x60; on both; &#x60;pageIds&#x60;, &#x60;adType&#x60;, &#x60;status&#x60;, &#x60;platforms&#x60;, &#x60;mediaType&#x60;, &#x60;languages&#x60;, &#x60;searchType&#x60;, &#x60;fields&#x60; are Meta-only; &#x60;advertiser&#x60; is LinkedIn-only. Passing a param the account&#39;s platform does not support is a 400 naming the param.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdLibraryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdLibraryApi apiInstance = new AdLibraryApi(defaultClient);
        String platform = "meta"; // String | Which archive to search. `meta` needs no accountId. Required unless accountId is given.
        String accountId = "accountId_example"; // String | Zernio SocialAccount id. Required for LinkedIn (linkedin / linkedinads: its token searches). Optional for Meta, where any facebook / instagram / metaads account only selects the platform.
        String q = "q_example"; // String | Keyword search. Meta does not translate it, so write it in the ads' language. Required unless pageIds (Meta) or advertiser (LinkedIn) is given.
        String pageIds = "pageIds_example"; // String | Meta only. Comma-separated Facebook Page ids (max 10) whose ads to list.
        String advertiser = "advertiser_example"; // String | LinkedIn only. Advertiser (Page) name to search.
        String countries = "countries_example"; // String | Comma-separated ISO 3166-1 alpha-2 codes the ads reached. Meta defaults to ALL (an explicit ALL is Meta-only); LinkedIn searches every market when omitted.
        String adType = "ALL"; // String | Meta only.
        String status = "ACTIVE"; // String | Meta only. ACTIVE = eligible for delivery right now.
        String platforms = "platforms_example"; // String | Meta only. Comma-separated publisher platforms: FACEBOOK, INSTAGRAM, AUDIENCE_NETWORK, MESSENGER, WHATSAPP, OCULUS, THREADS, STREAMING_SERVICES.
        String mediaType = "ALL"; // String | Meta only.
        String languages = "languages_example"; // String | Meta only. Comma-separated ISO 639-1 codes of the ad text.
        LocalDate since = LocalDate.now(); // LocalDate | Earliest delivery date (YYYY-MM-DD).
        LocalDate until = LocalDate.now(); // LocalDate | Latest delivery date (YYYY-MM-DD).
        String searchType = "KEYWORD_UNORDERED"; // String | Meta only. Whether q matches words in any order or as an exact phrase (comma-separate phrases to match all of them).
        String fields = "id,page_name,ad_delivery_start_time,ad_creative_bodies"; // String | Meta only. Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently.
        Integer limit = 25; // Integer | Rows per page. LinkedIn accepts at most 25.
        String after = "after_example"; // String | paging.after of the previous page.
        try {
            ApiResponse<SearchAdLibrary200Response> response = apiInstance.searchAdLibraryWithHttpInfo(platform, accountId, q, pageIds, advertiser, countries, adType, status, platforms, mediaType, languages, since, until, searchType, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdLibraryApi#searchAdLibrary");
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
| **platform** | **String**| Which archive to search. &#x60;meta&#x60; needs no accountId. Required unless accountId is given. | [optional] [enum: meta, linkedin] |
| **accountId** | **String**| Zernio SocialAccount id. Required for LinkedIn (linkedin / linkedinads: its token searches). Optional for Meta, where any facebook / instagram / metaads account only selects the platform. | [optional] |
| **q** | **String**| Keyword search. Meta does not translate it, so write it in the ads&#39; language. Required unless pageIds (Meta) or advertiser (LinkedIn) is given. | [optional] |
| **pageIds** | **String**| Meta only. Comma-separated Facebook Page ids (max 10) whose ads to list. | [optional] |
| **advertiser** | **String**| LinkedIn only. Advertiser (Page) name to search. | [optional] |
| **countries** | **String**| Comma-separated ISO 3166-1 alpha-2 codes the ads reached. Meta defaults to ALL (an explicit ALL is Meta-only); LinkedIn searches every market when omitted. | [optional] |
| **adType** | **String**| Meta only. | [optional] [default to ALL] [enum: ALL, POLITICAL_AND_ISSUE_ADS, HOUSING_ADS, EMPLOYMENT_ADS, FINANCIAL_PRODUCTS_AND_SERVICES_ADS] |
| **status** | **String**| Meta only. ACTIVE &#x3D; eligible for delivery right now. | [optional] [default to ACTIVE] [enum: ACTIVE, INACTIVE, ALL] |
| **platforms** | **String**| Meta only. Comma-separated publisher platforms: FACEBOOK, INSTAGRAM, AUDIENCE_NETWORK, MESSENGER, WHATSAPP, OCULUS, THREADS, STREAMING_SERVICES. | [optional] |
| **mediaType** | **String**| Meta only. | [optional] [enum: ALL, IMAGE, MEME, VIDEO, NONE] |
| **languages** | **String**| Meta only. Comma-separated ISO 639-1 codes of the ad text. | [optional] |
| **since** | **LocalDate**| Earliest delivery date (YYYY-MM-DD). | [optional] |
| **until** | **LocalDate**| Latest delivery date (YYYY-MM-DD). | [optional] |
| **searchType** | **String**| Meta only. Whether q matches words in any order or as an exact phrase (comma-separate phrases to match all of them). | [optional] [default to KEYWORD_UNORDERED] [enum: KEYWORD_UNORDERED, KEYWORD_EXACT_PHRASE] |
| **fields** | **String**| Meta only. Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently. | [optional] |
| **limit** | **Integer**| Rows per page. LinkedIn accepts at most 25. | [optional] [default to 25] |
| **after** | **String**| paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**SearchAdLibrary200Response**](SearchAdLibrary200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Archived ads (raw platform shape) |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included on usage-based plans), or &#x60;payment_required&#x60;: the billing owner has no payment method on file and no legacy paid plan. Searches are free; the card keeps the shared archive quota for real accounts. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta and LinkedIn accounts |  -  |
| **503** | Meta&#39;s Ad Library is unavailable on Zernio&#39;s side (&#x60;PLATFORM_DISABLED&#x60;); LinkedIn searches are unaffected. |  -  |

