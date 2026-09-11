# AdAccountsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAccountCallouts**](AdAccountsApi.md#addAccountCallouts) | **POST** /v1/ads/accounts/callouts | Add account callouts |
| [**addAccountCalloutsWithHttpInfo**](AdAccountsApi.md#addAccountCalloutsWithHttpInfo) | **POST** /v1/ads/accounts/callouts | Add account callouts |
| [**addAccountSitelinks**](AdAccountsApi.md#addAccountSitelinks) | **POST** /v1/ads/accounts/sitelinks | Add account sitelinks |
| [**addAccountSitelinksWithHttpInfo**](AdAccountsApi.md#addAccountSitelinksWithHttpInfo) | **POST** /v1/ads/accounts/sitelinks | Add account sitelinks |
| [**addAccountStructuredSnippets**](AdAccountsApi.md#addAccountStructuredSnippets) | **POST** /v1/ads/accounts/structured-snippets | Add account snippets |
| [**addAccountStructuredSnippetsWithHttpInfo**](AdAccountsApi.md#addAccountStructuredSnippetsWithHttpInfo) | **POST** /v1/ads/accounts/structured-snippets | Add account snippets |
| [**createAdAccount**](AdAccountsApi.md#createAdAccount) | **POST** /v1/ads/accounts | Create Meta ad account |
| [**createAdAccountWithHttpInfo**](AdAccountsApi.md#createAdAccountWithHttpInfo) | **POST** /v1/ads/accounts | Create Meta ad account |
| [**createAdNegativeKeywordList**](AdAccountsApi.md#createAdNegativeKeywordList) | **POST** /v1/ads/accounts/negative-keyword-lists | Create a negative keyword list |
| [**createAdNegativeKeywordListWithHttpInfo**](AdAccountsApi.md#createAdNegativeKeywordListWithHttpInfo) | **POST** /v1/ads/accounts/negative-keyword-lists | Create a negative keyword list |
| [**createCustomConversion**](AdAccountsApi.md#createCustomConversion) | **POST** /v1/accounts/{accountId}/custom-conversions | Create custom conversion |
| [**createCustomConversionWithHttpInfo**](AdAccountsApi.md#createCustomConversionWithHttpInfo) | **POST** /v1/accounts/{accountId}/custom-conversions | Create custom conversion |
| [**createHighDemandPeriod**](AdAccountsApi.md#createHighDemandPeriod) | **POST** /v1/ads/high-demand-periods | Schedule a budget increase |
| [**createHighDemandPeriodWithHttpInfo**](AdAccountsApi.md#createHighDemandPeriodWithHttpInfo) | **POST** /v1/ads/high-demand-periods | Schedule a budget increase |
| [**createValueRuleSet**](AdAccountsApi.md#createValueRuleSet) | **POST** /v1/ads/value-rule-sets | Create a value rule set |
| [**createValueRuleSetWithHttpInfo**](AdAccountsApi.md#createValueRuleSetWithHttpInfo) | **POST** /v1/ads/value-rule-sets | Create a value rule set |
| [**deleteAdComment**](AdAccountsApi.md#deleteAdComment) | **DELETE** /v1/ads/{adId}/comments/{commentId} | Delete an ad comment |
| [**deleteAdCommentWithHttpInfo**](AdAccountsApi.md#deleteAdCommentWithHttpInfo) | **DELETE** /v1/ads/{adId}/comments/{commentId} | Delete an ad comment |
| [**deleteAdNegativeKeywordList**](AdAccountsApi.md#deleteAdNegativeKeywordList) | **DELETE** /v1/ads/accounts/negative-keyword-lists/{listId} | Delete a negative keyword list |
| [**deleteAdNegativeKeywordListWithHttpInfo**](AdAccountsApi.md#deleteAdNegativeKeywordListWithHttpInfo) | **DELETE** /v1/ads/accounts/negative-keyword-lists/{listId} | Delete a negative keyword list |
| [**deleteValueRuleSet**](AdAccountsApi.md#deleteValueRuleSet) | **DELETE** /v1/ads/value-rule-sets/{valueRuleSetId} | Delete a value rule set |
| [**deleteValueRuleSetWithHttpInfo**](AdAccountsApi.md#deleteValueRuleSetWithHttpInfo) | **DELETE** /v1/ads/value-rule-sets/{valueRuleSetId} | Delete a value rule set |
| [**getAdAccountFinance**](AdAccountsApi.md#getAdAccountFinance) | **GET** /v1/ads/accounts/finance | Ad account finances |
| [**getAdAccountFinanceWithHttpInfo**](AdAccountsApi.md#getAdAccountFinanceWithHttpInfo) | **GET** /v1/ads/accounts/finance | Ad account finances |
| [**getAdComments**](AdAccountsApi.md#getAdComments) | **GET** /v1/ads/{adId}/comments | List comments on an ad |
| [**getAdCommentsWithHttpInfo**](AdAccountsApi.md#getAdCommentsWithHttpInfo) | **GET** /v1/ads/{adId}/comments | List comments on an ad |
| [**getAdNegativeKeywordList**](AdAccountsApi.md#getAdNegativeKeywordList) | **GET** /v1/ads/accounts/negative-keyword-lists/{listId} | Get a negative keyword list |
| [**getAdNegativeKeywordListWithHttpInfo**](AdAccountsApi.md#getAdNegativeKeywordListWithHttpInfo) | **GET** /v1/ads/accounts/negative-keyword-lists/{listId} | Get a negative keyword list |
| [**getAdsActivityLog**](AdAccountsApi.md#getAdsActivityLog) | **GET** /v1/ads/activity | Ad account change / audit log |
| [**getAdsActivityLogWithHttpInfo**](AdAccountsApi.md#getAdsActivityLogWithHttpInfo) | **GET** /v1/ads/activity | Ad account change / audit log |
| [**getDsaDefaults**](AdAccountsApi.md#getDsaDefaults) | **GET** /v1/ads/dsa-defaults | Get ad account DSA defaults |
| [**getDsaDefaultsWithHttpInfo**](AdAccountsApi.md#getDsaDefaultsWithHttpInfo) | **GET** /v1/ads/dsa-defaults | Get ad account DSA defaults |
| [**getDsaRecommendations**](AdAccountsApi.md#getDsaRecommendations) | **GET** /v1/ads/dsa-recommendations | Get DSA recommendations |
| [**getDsaRecommendationsWithHttpInfo**](AdAccountsApi.md#getDsaRecommendationsWithHttpInfo) | **GET** /v1/ads/dsa-recommendations | Get DSA recommendations |
| [**getIosFourteenCampaignLimits**](AdAccountsApi.md#getIosFourteenCampaignLimits) | **GET** /v1/ads/ios-fourteen-campaign-limits | Get iOS 14 campaign limits |
| [**getIosFourteenCampaignLimitsWithHttpInfo**](AdAccountsApi.md#getIosFourteenCampaignLimitsWithHttpInfo) | **GET** /v1/ads/ios-fourteen-campaign-limits | Get iOS 14 campaign limits |
| [**getValueRuleSet**](AdAccountsApi.md#getValueRuleSet) | **GET** /v1/ads/value-rule-sets/{valueRuleSetId} | Read a value rule set |
| [**getValueRuleSetWithHttpInfo**](AdAccountsApi.md#getValueRuleSetWithHttpInfo) | **GET** /v1/ads/value-rule-sets/{valueRuleSetId} | Read a value rule set |
| [**hideAdComment**](AdAccountsApi.md#hideAdComment) | **POST** /v1/ads/{adId}/comments/{commentId}/hide | Hide or unhide an ad comment |
| [**hideAdCommentWithHttpInfo**](AdAccountsApi.md#hideAdCommentWithHttpInfo) | **POST** /v1/ads/{adId}/comments/{commentId}/hide | Hide or unhide an ad comment |
| [**listAccountCallouts**](AdAccountsApi.md#listAccountCallouts) | **GET** /v1/ads/accounts/callouts | List account callouts |
| [**listAccountCalloutsWithHttpInfo**](AdAccountsApi.md#listAccountCalloutsWithHttpInfo) | **GET** /v1/ads/accounts/callouts | List account callouts |
| [**listAccountSitelinks**](AdAccountsApi.md#listAccountSitelinks) | **GET** /v1/ads/accounts/sitelinks | List account sitelinks |
| [**listAccountSitelinksWithHttpInfo**](AdAccountsApi.md#listAccountSitelinksWithHttpInfo) | **GET** /v1/ads/accounts/sitelinks | List account sitelinks |
| [**listAccountStructuredSnippets**](AdAccountsApi.md#listAccountStructuredSnippets) | **GET** /v1/ads/accounts/structured-snippets | List account snippets |
| [**listAccountStructuredSnippetsWithHttpInfo**](AdAccountsApi.md#listAccountStructuredSnippetsWithHttpInfo) | **GET** /v1/ads/accounts/structured-snippets | List account snippets |
| [**listAdAccounts**](AdAccountsApi.md#listAdAccounts) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdAccountsWithHttpInfo**](AdAccountsApi.md#listAdAccountsWithHttpInfo) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdLabels**](AdAccountsApi.md#listAdLabels) | **GET** /v1/ads/labels | Ad labels |
| [**listAdLabelsWithHttpInfo**](AdAccountsApi.md#listAdLabelsWithHttpInfo) | **GET** /v1/ads/labels | Ad labels |
| [**listAdNegativeKeywordLists**](AdAccountsApi.md#listAdNegativeKeywordLists) | **GET** /v1/ads/accounts/negative-keyword-lists | List negative keyword lists |
| [**listAdNegativeKeywordListsWithHttpInfo**](AdAccountsApi.md#listAdNegativeKeywordListsWithHttpInfo) | **GET** /v1/ads/accounts/negative-keyword-lists | List negative keyword lists |
| [**listAdStudies**](AdAccountsApi.md#listAdStudies) | **GET** /v1/ads/studies | A/B tests and lift studies |
| [**listAdStudiesWithHttpInfo**](AdAccountsApi.md#listAdStudiesWithHttpInfo) | **GET** /v1/ads/studies | A/B tests and lift studies |
| [**listAdsBusinessCenters**](AdAccountsApi.md#listAdsBusinessCenters) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listAdsBusinessCentersWithHttpInfo**](AdAccountsApi.md#listAdsBusinessCentersWithHttpInfo) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listAdsInstagramAccounts**](AdAccountsApi.md#listAdsInstagramAccounts) | **GET** /v1/ads/instagram-accounts | List Instagram ad identities |
| [**listAdsInstagramAccountsWithHttpInfo**](AdAccountsApi.md#listAdsInstagramAccountsWithHttpInfo) | **GET** /v1/ads/instagram-accounts | List Instagram ad identities |
| [**listAdvertisableApplications**](AdAccountsApi.md#listAdvertisableApplications) | **GET** /v1/ads/advertisable-applications | List advertisable apps |
| [**listAdvertisableApplicationsWithHttpInfo**](AdAccountsApi.md#listAdvertisableApplicationsWithHttpInfo) | **GET** /v1/ads/advertisable-applications | List advertisable apps |
| [**listCustomConversions**](AdAccountsApi.md#listCustomConversions) | **GET** /v1/accounts/{accountId}/custom-conversions | List custom conversions |
| [**listCustomConversionsWithHttpInfo**](AdAccountsApi.md#listCustomConversionsWithHttpInfo) | **GET** /v1/accounts/{accountId}/custom-conversions | List custom conversions |
| [**listHighDemandPeriods**](AdAccountsApi.md#listHighDemandPeriods) | **GET** /v1/ads/high-demand-periods | List high-demand periods |
| [**listHighDemandPeriodsWithHttpInfo**](AdAccountsApi.md#listHighDemandPeriodsWithHttpInfo) | **GET** /v1/ads/high-demand-periods | List high-demand periods |
| [**listMetaBusinesses**](AdAccountsApi.md#listMetaBusinesses) | **GET** /v1/ads/businesses | Businesses list |
| [**listMetaBusinessesWithHttpInfo**](AdAccountsApi.md#listMetaBusinessesWithHttpInfo) | **GET** /v1/ads/businesses | Businesses list |
| [**listTikTokAdPixels**](AdAccountsApi.md#listTikTokAdPixels) | **GET** /v1/ads/pixels | List TikTok ad pixels |
| [**listTikTokAdPixelsWithHttpInfo**](AdAccountsApi.md#listTikTokAdPixelsWithHttpInfo) | **GET** /v1/ads/pixels | List TikTok ad pixels |
| [**listValueRuleSets**](AdAccountsApi.md#listValueRuleSets) | **GET** /v1/ads/value-rule-sets | List value rule sets |
| [**listValueRuleSetsWithHttpInfo**](AdAccountsApi.md#listValueRuleSetsWithHttpInfo) | **GET** /v1/ads/value-rule-sets | List value rule sets |
| [**removeAccountCallout**](AdAccountsApi.md#removeAccountCallout) | **DELETE** /v1/ads/accounts/callouts | Remove account callout |
| [**removeAccountCalloutWithHttpInfo**](AdAccountsApi.md#removeAccountCalloutWithHttpInfo) | **DELETE** /v1/ads/accounts/callouts | Remove account callout |
| [**removeAccountSitelink**](AdAccountsApi.md#removeAccountSitelink) | **DELETE** /v1/ads/accounts/sitelinks | Remove account sitelink |
| [**removeAccountSitelinkWithHttpInfo**](AdAccountsApi.md#removeAccountSitelinkWithHttpInfo) | **DELETE** /v1/ads/accounts/sitelinks | Remove account sitelink |
| [**removeAccountStructuredSnippet**](AdAccountsApi.md#removeAccountStructuredSnippet) | **DELETE** /v1/ads/accounts/structured-snippets | Remove account snippet |
| [**removeAccountStructuredSnippetWithHttpInfo**](AdAccountsApi.md#removeAccountStructuredSnippetWithHttpInfo) | **DELETE** /v1/ads/accounts/structured-snippets | Remove account snippet |
| [**replaceAdNegativeKeywordListKeywords**](AdAccountsApi.md#replaceAdNegativeKeywordListKeywords) | **PUT** /v1/ads/accounts/negative-keyword-lists/{listId}/keywords | Replace negative list keywords |
| [**replaceAdNegativeKeywordListKeywordsWithHttpInfo**](AdAccountsApi.md#replaceAdNegativeKeywordListKeywordsWithHttpInfo) | **PUT** /v1/ads/accounts/negative-keyword-lists/{listId}/keywords | Replace negative list keywords |
| [**replyToAdComment**](AdAccountsApi.md#replyToAdComment) | **POST** /v1/ads/{adId}/comments/{commentId}/reply | Reply to an ad comment |
| [**replyToAdCommentWithHttpInfo**](AdAccountsApi.md#replyToAdCommentWithHttpInfo) | **POST** /v1/ads/{adId}/comments/{commentId}/reply | Reply to an ad comment |
| [**updateAccountCallouts**](AdAccountsApi.md#updateAccountCallouts) | **PUT** /v1/ads/accounts/callouts | Update account callouts |
| [**updateAccountCalloutsWithHttpInfo**](AdAccountsApi.md#updateAccountCalloutsWithHttpInfo) | **PUT** /v1/ads/accounts/callouts | Update account callouts |
| [**updateAccountSitelinks**](AdAccountsApi.md#updateAccountSitelinks) | **PUT** /v1/ads/accounts/sitelinks | Update account sitelinks |
| [**updateAccountSitelinksWithHttpInfo**](AdAccountsApi.md#updateAccountSitelinksWithHttpInfo) | **PUT** /v1/ads/accounts/sitelinks | Update account sitelinks |
| [**updateAccountStructuredSnippets**](AdAccountsApi.md#updateAccountStructuredSnippets) | **PUT** /v1/ads/accounts/structured-snippets | Update account snippets |
| [**updateAccountStructuredSnippetsWithHttpInfo**](AdAccountsApi.md#updateAccountStructuredSnippetsWithHttpInfo) | **PUT** /v1/ads/accounts/structured-snippets | Update account snippets |
| [**updateAdAccount**](AdAccountsApi.md#updateAdAccount) | **PATCH** /v1/ads/accounts | Update ad account settings |
| [**updateAdAccountWithHttpInfo**](AdAccountsApi.md#updateAdAccountWithHttpInfo) | **PATCH** /v1/ads/accounts | Update ad account settings |
| [**updateAdNegativeKeywordList**](AdAccountsApi.md#updateAdNegativeKeywordList) | **PUT** /v1/ads/accounts/negative-keyword-lists/{listId} | Rename a negative keyword list |
| [**updateAdNegativeKeywordListWithHttpInfo**](AdAccountsApi.md#updateAdNegativeKeywordListWithHttpInfo) | **PUT** /v1/ads/accounts/negative-keyword-lists/{listId} | Rename a negative keyword list |
| [**updateValueRuleSet**](AdAccountsApi.md#updateValueRuleSet) | **PUT** /v1/ads/value-rule-sets/{valueRuleSetId} | Replace a value rule set |
| [**updateValueRuleSetWithHttpInfo**](AdAccountsApi.md#updateValueRuleSetWithHttpInfo) | **PUT** /v1/ads/value-rule-sets/{valueRuleSetId} | Replace a value rule set |



## addAccountCallouts

> AddAccountCallouts201Response addAccountCallouts(addAccountCalloutsRequest)

Add account callouts

Creates assets and customer_asset links for this Google customer. Links apply at account level.

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
        AddAccountCalloutsRequest addAccountCalloutsRequest = new AddAccountCalloutsRequest(); // AddAccountCalloutsRequest | 
        try {
            AddAccountCallouts201Response result = apiInstance.addAccountCallouts(addAccountCalloutsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#addAccountCallouts");
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
| **addAccountCalloutsRequest** | [**AddAccountCalloutsRequest**](AddAccountCalloutsRequest.md)|  | |

### Return type

[**AddAccountCallouts201Response**](AddAccountCallouts201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## addAccountCalloutsWithHttpInfo

> ApiResponse<AddAccountCallouts201Response> addAccountCallouts addAccountCalloutsWithHttpInfo(addAccountCalloutsRequest)

Add account callouts

Creates assets and customer_asset links for this Google customer. Links apply at account level.

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
        AddAccountCalloutsRequest addAccountCalloutsRequest = new AddAccountCalloutsRequest(); // AddAccountCalloutsRequest | 
        try {
            ApiResponse<AddAccountCallouts201Response> response = apiInstance.addAccountCalloutsWithHttpInfo(addAccountCalloutsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#addAccountCallouts");
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
| **addAccountCalloutsRequest** | [**AddAccountCalloutsRequest**](AddAccountCalloutsRequest.md)|  | |

### Return type

ApiResponse<[**AddAccountCallouts201Response**](AddAccountCallouts201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## addAccountSitelinks

> AddAccountSitelinks201Response addAccountSitelinks(addAccountSitelinksRequest)

Add account sitelinks

Creates assets and customer_asset links for this Google customer. Links apply at account level.

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
        AddAccountSitelinksRequest addAccountSitelinksRequest = new AddAccountSitelinksRequest(); // AddAccountSitelinksRequest | 
        try {
            AddAccountSitelinks201Response result = apiInstance.addAccountSitelinks(addAccountSitelinksRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#addAccountSitelinks");
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
| **addAccountSitelinksRequest** | [**AddAccountSitelinksRequest**](AddAccountSitelinksRequest.md)|  | |

### Return type

[**AddAccountSitelinks201Response**](AddAccountSitelinks201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## addAccountSitelinksWithHttpInfo

> ApiResponse<AddAccountSitelinks201Response> addAccountSitelinks addAccountSitelinksWithHttpInfo(addAccountSitelinksRequest)

Add account sitelinks

Creates assets and customer_asset links for this Google customer. Links apply at account level.

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
        AddAccountSitelinksRequest addAccountSitelinksRequest = new AddAccountSitelinksRequest(); // AddAccountSitelinksRequest | 
        try {
            ApiResponse<AddAccountSitelinks201Response> response = apiInstance.addAccountSitelinksWithHttpInfo(addAccountSitelinksRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#addAccountSitelinks");
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
| **addAccountSitelinksRequest** | [**AddAccountSitelinksRequest**](AddAccountSitelinksRequest.md)|  | |

### Return type

ApiResponse<[**AddAccountSitelinks201Response**](AddAccountSitelinks201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## addAccountStructuredSnippets

> AddAccountStructuredSnippets201Response addAccountStructuredSnippets(addAccountStructuredSnippetsRequest)

Add account snippets

Creates assets and customer_asset links for this Google customer. Links apply at account level.

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
        AddAccountStructuredSnippetsRequest addAccountStructuredSnippetsRequest = new AddAccountStructuredSnippetsRequest(); // AddAccountStructuredSnippetsRequest | 
        try {
            AddAccountStructuredSnippets201Response result = apiInstance.addAccountStructuredSnippets(addAccountStructuredSnippetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#addAccountStructuredSnippets");
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
| **addAccountStructuredSnippetsRequest** | [**AddAccountStructuredSnippetsRequest**](AddAccountStructuredSnippetsRequest.md)|  | |

### Return type

[**AddAccountStructuredSnippets201Response**](AddAccountStructuredSnippets201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## addAccountStructuredSnippetsWithHttpInfo

> ApiResponse<AddAccountStructuredSnippets201Response> addAccountStructuredSnippets addAccountStructuredSnippetsWithHttpInfo(addAccountStructuredSnippetsRequest)

Add account snippets

Creates assets and customer_asset links for this Google customer. Links apply at account level.

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
        AddAccountStructuredSnippetsRequest addAccountStructuredSnippetsRequest = new AddAccountStructuredSnippetsRequest(); // AddAccountStructuredSnippetsRequest | 
        try {
            ApiResponse<AddAccountStructuredSnippets201Response> response = apiInstance.addAccountStructuredSnippetsWithHttpInfo(addAccountStructuredSnippetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#addAccountStructuredSnippets");
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
| **addAccountStructuredSnippetsRequest** | [**AddAccountStructuredSnippetsRequest**](AddAccountStructuredSnippetsRequest.md)|  | |

### Return type

ApiResponse<[**AddAccountStructuredSnippets201Response**](AddAccountStructuredSnippets201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## createAdAccount

> CreateAdAccount201Response createAdAccount(createAdAccountRequest)

Create Meta ad account

Creates a durable Meta ad account in the end user&#39;s own business portfolio using their connected Meta Ads token. Requires an active metaads accountId, Ads access, business_management permission and business admin access. Discover portfolios with GET /v1/ads/businesses. System-user tokens may return an empty businesses list; supply the known business ID in that case.  The self-serve account starts without a payment method. The user must add a payment method in Ads Manager before ads can deliver. Zernio cannot add payment methods. Meta may require business verification and limits how many accounts a business can create. Closing an account does not guarantee more capacity. An ad account cannot truly be deleted, even after closing it and removing it from a business.  timezoneId is Meta&#39;s numeric ID, not an IANA timezone name. Select it from https://developers.facebook.com/docs/marketing-api/reference/ad-account/timezone-ids/. For example, 1 is America/Los_Angeles. Meta validates supported currencies and IDs. endAdvertiser, mediaAgency and partner default to NONE for the self-serve flow.  The new account is added atomically to an existing scoped ad-account allowlist. Unrestricted connections stay unrestricted. Reconnecting the same Meta identity preserves this scope unless a caller explicitly replaces it. Discovery is nudged immediately. Use the returned adAccountId with the existing ads endpoints.  This operation is not idempotent and Zernio never automatically retries it. Unknown body fields are rejected. No validateOnly or dry-run option is supported. After a timeout or a 502 with details.creationStatus&#x3D;unknown, check the business in Ads Manager before attempting another creation. A 201 with connectionUpdated&#x3D;false means the account exists but needs reconnecting with adAccountIds containing the returned ID and the previous scoped IDs via GET /v1/connect/facebook/ads. Do not repeat the create call. 

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
        CreateAdAccountRequest createAdAccountRequest = new CreateAdAccountRequest(); // CreateAdAccountRequest | 
        try {
            CreateAdAccount201Response result = apiInstance.createAdAccount(createAdAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createAdAccount");
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
| **createAdAccountRequest** | [**CreateAdAccountRequest**](CreateAdAccountRequest.md)|  | |

### Return type

[**CreateAdAccount201Response**](CreateAdAccount201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Ad account created. Check connectionUpdated and payment instructions. |  -  |
| **400** | Invalid input or Meta rejection. details.reason identifies creation_limit, business_verification_required, unsupported_currency, unsupported_timezone or business_unavailable when recognized. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access denied or Meta permission missing. details.reason may be business_management_required, business_admin_required or business_access_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **502** | Creation outcome unknown. Check Ads Manager before repeating this non-idempotent request. |  -  |

## createAdAccountWithHttpInfo

> ApiResponse<CreateAdAccount201Response> createAdAccount createAdAccountWithHttpInfo(createAdAccountRequest)

Create Meta ad account

Creates a durable Meta ad account in the end user&#39;s own business portfolio using their connected Meta Ads token. Requires an active metaads accountId, Ads access, business_management permission and business admin access. Discover portfolios with GET /v1/ads/businesses. System-user tokens may return an empty businesses list; supply the known business ID in that case.  The self-serve account starts without a payment method. The user must add a payment method in Ads Manager before ads can deliver. Zernio cannot add payment methods. Meta may require business verification and limits how many accounts a business can create. Closing an account does not guarantee more capacity. An ad account cannot truly be deleted, even after closing it and removing it from a business.  timezoneId is Meta&#39;s numeric ID, not an IANA timezone name. Select it from https://developers.facebook.com/docs/marketing-api/reference/ad-account/timezone-ids/. For example, 1 is America/Los_Angeles. Meta validates supported currencies and IDs. endAdvertiser, mediaAgency and partner default to NONE for the self-serve flow.  The new account is added atomically to an existing scoped ad-account allowlist. Unrestricted connections stay unrestricted. Reconnecting the same Meta identity preserves this scope unless a caller explicitly replaces it. Discovery is nudged immediately. Use the returned adAccountId with the existing ads endpoints.  This operation is not idempotent and Zernio never automatically retries it. Unknown body fields are rejected. No validateOnly or dry-run option is supported. After a timeout or a 502 with details.creationStatus&#x3D;unknown, check the business in Ads Manager before attempting another creation. A 201 with connectionUpdated&#x3D;false means the account exists but needs reconnecting with adAccountIds containing the returned ID and the previous scoped IDs via GET /v1/connect/facebook/ads. Do not repeat the create call. 

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
        CreateAdAccountRequest createAdAccountRequest = new CreateAdAccountRequest(); // CreateAdAccountRequest | 
        try {
            ApiResponse<CreateAdAccount201Response> response = apiInstance.createAdAccountWithHttpInfo(createAdAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createAdAccount");
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
| **createAdAccountRequest** | [**CreateAdAccountRequest**](CreateAdAccountRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdAccount201Response**](CreateAdAccount201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Ad account created. Check connectionUpdated and payment instructions. |  -  |
| **400** | Invalid input or Meta rejection. details.reason identifies creation_limit, business_verification_required, unsupported_currency, unsupported_timezone or business_unavailable when recognized. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access denied or Meta permission missing. details.reason may be business_management_required, business_admin_required or business_access_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **502** | Creation outcome unknown. Check Ads Manager before repeating this non-idempotent request. |  -  |


## createAdNegativeKeywordList

> CreateAdNegativeKeywordList201Response createAdNegativeKeywordList(createAdNegativeKeywordListRequest)

Create a negative keyword list

Creates one Google Ads shared negative keyword list with optional initial keywords in a single atomic mutation. Daily quota is reserved for every mutate item, so large batches may return 429 before any change. This operation is not idempotent. The list is not attached to any campaign.

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
        CreateAdNegativeKeywordListRequest createAdNegativeKeywordListRequest = new CreateAdNegativeKeywordListRequest(); // CreateAdNegativeKeywordListRequest | 
        try {
            CreateAdNegativeKeywordList201Response result = apiInstance.createAdNegativeKeywordList(createAdNegativeKeywordListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createAdNegativeKeywordList");
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
| **createAdNegativeKeywordListRequest** | [**CreateAdNegativeKeywordListRequest**](CreateAdNegativeKeywordListRequest.md)|  | |

### Return type

[**CreateAdNegativeKeywordList201Response**](CreateAdNegativeKeywordList201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## createAdNegativeKeywordListWithHttpInfo

> ApiResponse<CreateAdNegativeKeywordList201Response> createAdNegativeKeywordList createAdNegativeKeywordListWithHttpInfo(createAdNegativeKeywordListRequest)

Create a negative keyword list

Creates one Google Ads shared negative keyword list with optional initial keywords in a single atomic mutation. Daily quota is reserved for every mutate item, so large batches may return 429 before any change. This operation is not idempotent. The list is not attached to any campaign.

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
        CreateAdNegativeKeywordListRequest createAdNegativeKeywordListRequest = new CreateAdNegativeKeywordListRequest(); // CreateAdNegativeKeywordListRequest | 
        try {
            ApiResponse<CreateAdNegativeKeywordList201Response> response = apiInstance.createAdNegativeKeywordListWithHttpInfo(createAdNegativeKeywordListRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createAdNegativeKeywordList");
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
| **createAdNegativeKeywordListRequest** | [**CreateAdNegativeKeywordListRequest**](CreateAdNegativeKeywordListRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdNegativeKeywordList201Response**](CreateAdNegativeKeywordList201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


## createCustomConversion

> CustomConversionResult createCustomConversion(accountId, createCustomConversionRequest)

Create custom conversion

Provision the Meta custom conversion an ads flow optimises toward, and hand back the &#x60;customConversionId&#x60; for &#x60;promotedObject.customConversionId&#x60; on POST /v1/ads/create. Removes the manual \&quot;create it in Ads Manager first\&quot; step.  **Reuse is ours, not Meta&#39;s.** Meta&#39;s create is not idempotent, so a retried request would otherwise mint a duplicate carrying none of the original&#39;s optimisation history. A non-archived conversion with the same &#x60;name&#x60; on the same &#x60;pixelId&#x60; is returned instead of created, with &#x60;reused: true&#x60; and a 200 rather than a 201.  &#x60;rule&#x60; is forwarded verbatim in Meta&#39;s own grammar (e.g. &#x60;{\&quot;url\&quot;: {\&quot;i_contains\&quot;: \&quot;thank-you\&quot;}}&#x60;); Meta validates it and rejects a malformed one with \&quot;A conversion rule is required at creation time\&quot;.

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
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id.
        CreateCustomConversionRequest createCustomConversionRequest = new CreateCustomConversionRequest(); // CreateCustomConversionRequest | 
        try {
            CustomConversionResult result = apiInstance.createCustomConversion(accountId, createCustomConversionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createCustomConversion");
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
| **accountId** | **String**| Meta ads SocialAccount id. | |
| **createCustomConversionRequest** | [**CreateCustomConversionRequest**](CreateCustomConversionRequest.md)|  | |

### Return type

[**CustomConversionResult**](CustomConversionResult.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | An existing custom conversion was reused |  -  |
| **201** | Custom conversion created |  -  |
| **400** | Invalid input, or Meta rejected the conversion (bad rule, per-account cap reached) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the token lacks the ads permissions. |  -  |

## createCustomConversionWithHttpInfo

> ApiResponse<CustomConversionResult> createCustomConversion createCustomConversionWithHttpInfo(accountId, createCustomConversionRequest)

Create custom conversion

Provision the Meta custom conversion an ads flow optimises toward, and hand back the &#x60;customConversionId&#x60; for &#x60;promotedObject.customConversionId&#x60; on POST /v1/ads/create. Removes the manual \&quot;create it in Ads Manager first\&quot; step.  **Reuse is ours, not Meta&#39;s.** Meta&#39;s create is not idempotent, so a retried request would otherwise mint a duplicate carrying none of the original&#39;s optimisation history. A non-archived conversion with the same &#x60;name&#x60; on the same &#x60;pixelId&#x60; is returned instead of created, with &#x60;reused: true&#x60; and a 200 rather than a 201.  &#x60;rule&#x60; is forwarded verbatim in Meta&#39;s own grammar (e.g. &#x60;{\&quot;url\&quot;: {\&quot;i_contains\&quot;: \&quot;thank-you\&quot;}}&#x60;); Meta validates it and rejects a malformed one with \&quot;A conversion rule is required at creation time\&quot;.

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
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id.
        CreateCustomConversionRequest createCustomConversionRequest = new CreateCustomConversionRequest(); // CreateCustomConversionRequest | 
        try {
            ApiResponse<CustomConversionResult> response = apiInstance.createCustomConversionWithHttpInfo(accountId, createCustomConversionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createCustomConversion");
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
| **accountId** | **String**| Meta ads SocialAccount id. | |
| **createCustomConversionRequest** | [**CreateCustomConversionRequest**](CreateCustomConversionRequest.md)|  | |

### Return type

ApiResponse<[**CustomConversionResult**](CustomConversionResult.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | An existing custom conversion was reused |  -  |
| **201** | Custom conversion created |  -  |
| **400** | Invalid input, or Meta rejected the conversion (bad rule, per-account cap reached) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the token lacks the ads permissions. |  -  |


## createHighDemandPeriod

> CreateHighDemandPeriod201Response createHighDemandPeriod(createHighDemandPeriodRequest)

Schedule a budget increase

Pre-schedule a temporary budget increase (Black Friday, a launch, a sale) instead of editing the budget by hand on the day. Same target rule as the GET: exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60;.  Two Meta constraints worth knowing before you call it. &#x60;timeStart&#x60; / &#x60;timeEnd&#x60; must fall on a 15-minute boundary, and a campaign cannot mix &#x60;ABSOLUTE&#x60; and &#x60;MULTIPLIER&#x60; across its schedules; the second type is rejected with \&quot;Can&#39;t mix your budget scaling selection\&quot;. Window rules (must sit inside the campaign&#39;s run dates, minimum lead time, no overlap) are Meta&#39;s and its message is forwarded verbatim.

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
        CreateHighDemandPeriodRequest createHighDemandPeriodRequest = new CreateHighDemandPeriodRequest(); // CreateHighDemandPeriodRequest | 
        try {
            CreateHighDemandPeriod201Response result = apiInstance.createHighDemandPeriod(createHighDemandPeriodRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createHighDemandPeriod");
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
| **createHighDemandPeriodRequest** | [**CreateHighDemandPeriodRequest**](CreateHighDemandPeriodRequest.md)|  | |

### Return type

[**CreateHighDemandPeriod201Response**](CreateHighDemandPeriod201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **201** | Budget schedule created |  -  |
| **400** | Invalid input, or Meta rejected the schedule |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createHighDemandPeriodWithHttpInfo

> ApiResponse<CreateHighDemandPeriod201Response> createHighDemandPeriod createHighDemandPeriodWithHttpInfo(createHighDemandPeriodRequest)

Schedule a budget increase

Pre-schedule a temporary budget increase (Black Friday, a launch, a sale) instead of editing the budget by hand on the day. Same target rule as the GET: exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60;.  Two Meta constraints worth knowing before you call it. &#x60;timeStart&#x60; / &#x60;timeEnd&#x60; must fall on a 15-minute boundary, and a campaign cannot mix &#x60;ABSOLUTE&#x60; and &#x60;MULTIPLIER&#x60; across its schedules; the second type is rejected with \&quot;Can&#39;t mix your budget scaling selection\&quot;. Window rules (must sit inside the campaign&#39;s run dates, minimum lead time, no overlap) are Meta&#39;s and its message is forwarded verbatim.

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
        CreateHighDemandPeriodRequest createHighDemandPeriodRequest = new CreateHighDemandPeriodRequest(); // CreateHighDemandPeriodRequest | 
        try {
            ApiResponse<CreateHighDemandPeriod201Response> response = apiInstance.createHighDemandPeriodWithHttpInfo(createHighDemandPeriodRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createHighDemandPeriod");
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
| **createHighDemandPeriodRequest** | [**CreateHighDemandPeriodRequest**](CreateHighDemandPeriodRequest.md)|  | |

### Return type

ApiResponse<[**CreateHighDemandPeriod201Response**](CreateHighDemandPeriod201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **201** | Budget schedule created |  -  |
| **400** | Invalid input, or Meta rejected the schedule |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## createValueRuleSet

> CreateValueRuleSet201Response createValueRuleSet(createValueRuleSetRequest)

Create a value rule set

Creates a value rule set on the ad account (Meta&#39;s &#x60;POST /act_X/value_rule_set&#x60;). Attach the returned id to an ad set with &#x60;valueRuleSetId&#x60; on &#x60;POST /v1/ads/create&#x60; or &#x60;PUT /v1/ads/ad-sets/{adSetId}&#x60;.  **Rule order is semantic**: rules are evaluated in array order and only the first matching rule adjusts the bid for an overlapping audience.  &#x60;adjustValue&#x60; is an unsigned magnitude in percent; the direction lives in &#x60;adjustSign&#x60;. &#x60;INCREASE&#x60; accepts 1-1000, &#x60;DECREASE&#x60; accepts 1-90. There is no signed field and 0 is out of range.  &#x60;criteriaValueTypes&#x60; is positionally paired with &#x60;criteriaValues&#x60; (same length, same order). Every type is the literal &#x60;\&quot;NONE\&quot;&#x60; except on &#x60;LOCATION&#x60;, which uses &#x60;LOCATION_COUNTRY&#x60; / &#x60;LOCATION_REGION&#x60; / &#x60;LOCATION_CITY&#x60; / &#x60;LOCATION_COMSCORE_MARKET&#x60; and may mix them within one criterion. Location values are Targeting-Search keys: a two-letter country code for &#x60;LOCATION_COUNTRY&#x60;, a numeric key for the rest.  &#x60;LOCATION_DMA&#x60; was replaced by &#x60;LOCATION_COMSCORE_MARKET&#x60; on 2026-06-22 and rules using DMAs are no longer active, so this API rejects it.  &#x60;AUDIENCE_LABEL&#x60; values (e.g. &#x60;HIGH_VALUE&#x60;) are applied to a Custom Audience in Ads Manager. There is no API to provision them, so label strings are passed through unvalidated and a typo produces a rule that never fires.  Ads Manager turns a rule set read-only (this API stays editable) when a rule uses more than 2 criteria, a custom age range, or the placements &#x60;FB_MARKETPLACE&#x60;, &#x60;FB_SEARCH&#x60;, &#x60;FB_VIDEO&#x60; or &#x60;IG_EXPLORE&#x60;.  Limits: 6 rule sets per ad account, 10 rules per set, 4 criteria per rule. The per-account cap is enforced by Meta, not here.

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
        CreateValueRuleSetRequest createValueRuleSetRequest = new CreateValueRuleSetRequest(); // CreateValueRuleSetRequest | 
        try {
            CreateValueRuleSet201Response result = apiInstance.createValueRuleSet(createValueRuleSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createValueRuleSet");
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
| **createValueRuleSetRequest** | [**CreateValueRuleSetRequest**](CreateValueRuleSetRequest.md)|  | |

### Return type

[**CreateValueRuleSet201Response**](CreateValueRuleSet201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **201** | Value rule set created |  -  |
| **400** | Invalid input, or Meta rejected the create (per-account rule-set cap, ineligible criteria, or an account that is not enabled for value rules) |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createValueRuleSetWithHttpInfo

> ApiResponse<CreateValueRuleSet201Response> createValueRuleSet createValueRuleSetWithHttpInfo(createValueRuleSetRequest)

Create a value rule set

Creates a value rule set on the ad account (Meta&#39;s &#x60;POST /act_X/value_rule_set&#x60;). Attach the returned id to an ad set with &#x60;valueRuleSetId&#x60; on &#x60;POST /v1/ads/create&#x60; or &#x60;PUT /v1/ads/ad-sets/{adSetId}&#x60;.  **Rule order is semantic**: rules are evaluated in array order and only the first matching rule adjusts the bid for an overlapping audience.  &#x60;adjustValue&#x60; is an unsigned magnitude in percent; the direction lives in &#x60;adjustSign&#x60;. &#x60;INCREASE&#x60; accepts 1-1000, &#x60;DECREASE&#x60; accepts 1-90. There is no signed field and 0 is out of range.  &#x60;criteriaValueTypes&#x60; is positionally paired with &#x60;criteriaValues&#x60; (same length, same order). Every type is the literal &#x60;\&quot;NONE\&quot;&#x60; except on &#x60;LOCATION&#x60;, which uses &#x60;LOCATION_COUNTRY&#x60; / &#x60;LOCATION_REGION&#x60; / &#x60;LOCATION_CITY&#x60; / &#x60;LOCATION_COMSCORE_MARKET&#x60; and may mix them within one criterion. Location values are Targeting-Search keys: a two-letter country code for &#x60;LOCATION_COUNTRY&#x60;, a numeric key for the rest.  &#x60;LOCATION_DMA&#x60; was replaced by &#x60;LOCATION_COMSCORE_MARKET&#x60; on 2026-06-22 and rules using DMAs are no longer active, so this API rejects it.  &#x60;AUDIENCE_LABEL&#x60; values (e.g. &#x60;HIGH_VALUE&#x60;) are applied to a Custom Audience in Ads Manager. There is no API to provision them, so label strings are passed through unvalidated and a typo produces a rule that never fires.  Ads Manager turns a rule set read-only (this API stays editable) when a rule uses more than 2 criteria, a custom age range, or the placements &#x60;FB_MARKETPLACE&#x60;, &#x60;FB_SEARCH&#x60;, &#x60;FB_VIDEO&#x60; or &#x60;IG_EXPLORE&#x60;.  Limits: 6 rule sets per ad account, 10 rules per set, 4 criteria per rule. The per-account cap is enforced by Meta, not here.

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
        CreateValueRuleSetRequest createValueRuleSetRequest = new CreateValueRuleSetRequest(); // CreateValueRuleSetRequest | 
        try {
            ApiResponse<CreateValueRuleSet201Response> response = apiInstance.createValueRuleSetWithHttpInfo(createValueRuleSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#createValueRuleSet");
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
| **createValueRuleSetRequest** | [**CreateValueRuleSetRequest**](CreateValueRuleSetRequest.md)|  | |

### Return type

ApiResponse<[**CreateValueRuleSet201Response**](CreateValueRuleSet201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **201** | Value rule set created |  -  |
| **400** | Invalid input, or Meta rejected the create (per-account rule-set cap, ineligible criteria, or an account that is not enabled for value rules) |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## deleteAdComment

> ReplyToAdComment200Response deleteAdComment(adId, commentId, since, until)

Delete an ad comment

Delete your own TikTok ad comment or reply. TikTok must return can_delete&#x3D;true for the comment. Other users&#39; comments can be hidden instead.  Unknown identity and video item fields are resolved only when needed for this action, then persisted for reuse. Comment-specific fields take precedence. If TikTok no longer returns the ad needed to resolve identity, 404 ad_not_found directs you to check deletion or archival in TikTok Ads Manager. Listing can still succeed. Unsupported or unavailable identity returns 403 feature_not_available. Denied access to ad details returns 403 insufficient_permissions with reconnect guidance and the upstream platformError.  Requires Ads access. The ad is resolved within the caller&#39;s accessible profiles. Before moderation, Zernio verifies that the comment belongs to this ad using TikTok&#39;s ad-group comment listing. The default search window is the last 30 days. Use since/until for older comments, with at most 30 days between the dates. Lookups scan at most 2,000 ad-group comments; narrow the date window if exceeded. Meta returns 501 feature_not_available with guidance to use the existing inbox comment endpoints and the account/post IDs from GET /v1/ads/{adId}/comments. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad ID.
        String commentId = "commentId_example"; // String | TikTok comment ID from the ad comment listing.
        LocalDate since = LocalDate.now(); // LocalDate | Start date of the comment lookup window. Defaults to 30 days before until.
        LocalDate until = LocalDate.now(); // LocalDate | End date of the comment lookup window. Defaults to today in UTC.
        try {
            ReplyToAdComment200Response result = apiInstance.deleteAdComment(adId, commentId, since, until);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#deleteAdComment");
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad ID. | |
| **commentId** | **String**| TikTok comment ID from the ad comment listing. | |
| **since** | **LocalDate**| Start date of the comment lookup window. Defaults to 30 days before until. | [optional] |
| **until** | **LocalDate**| End date of the comment lookup window. Defaults to today in UTC. | [optional] |

### Return type

[**ReplyToAdComment200Response**](ReplyToAdComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment action completed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access, own-comment deletion or supported identity is unavailable (feature_not_available), or TikTok denies ad-detail access (insufficient_permissions). |  -  |
| **404** | Ad is inaccessible or unavailable on TikTok for identity resolution (ad_not_found), or the comment was not found on this ad in the selected date window (resource_not_found). |  -  |
| **422** | TikTok Ads connection is unavailable. |  -  |
| **501** | Moderation on this route supports TikTok. Use the inbox comment routes for Meta. |  -  |
| **502** | TikTok rejected the request or was unavailable. Inspect platformError for its code and message. |  -  |

## deleteAdCommentWithHttpInfo

> ApiResponse<ReplyToAdComment200Response> deleteAdComment deleteAdCommentWithHttpInfo(adId, commentId, since, until)

Delete an ad comment

Delete your own TikTok ad comment or reply. TikTok must return can_delete&#x3D;true for the comment. Other users&#39; comments can be hidden instead.  Unknown identity and video item fields are resolved only when needed for this action, then persisted for reuse. Comment-specific fields take precedence. If TikTok no longer returns the ad needed to resolve identity, 404 ad_not_found directs you to check deletion or archival in TikTok Ads Manager. Listing can still succeed. Unsupported or unavailable identity returns 403 feature_not_available. Denied access to ad details returns 403 insufficient_permissions with reconnect guidance and the upstream platformError.  Requires Ads access. The ad is resolved within the caller&#39;s accessible profiles. Before moderation, Zernio verifies that the comment belongs to this ad using TikTok&#39;s ad-group comment listing. The default search window is the last 30 days. Use since/until for older comments, with at most 30 days between the dates. Lookups scan at most 2,000 ad-group comments; narrow the date window if exceeded. Meta returns 501 feature_not_available with guidance to use the existing inbox comment endpoints and the account/post IDs from GET /v1/ads/{adId}/comments. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad ID.
        String commentId = "commentId_example"; // String | TikTok comment ID from the ad comment listing.
        LocalDate since = LocalDate.now(); // LocalDate | Start date of the comment lookup window. Defaults to 30 days before until.
        LocalDate until = LocalDate.now(); // LocalDate | End date of the comment lookup window. Defaults to today in UTC.
        try {
            ApiResponse<ReplyToAdComment200Response> response = apiInstance.deleteAdCommentWithHttpInfo(adId, commentId, since, until);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#deleteAdComment");
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad ID. | |
| **commentId** | **String**| TikTok comment ID from the ad comment listing. | |
| **since** | **LocalDate**| Start date of the comment lookup window. Defaults to 30 days before until. | [optional] |
| **until** | **LocalDate**| End date of the comment lookup window. Defaults to today in UTC. | [optional] |

### Return type

ApiResponse<[**ReplyToAdComment200Response**](ReplyToAdComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment action completed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access, own-comment deletion or supported identity is unavailable (feature_not_available), or TikTok denies ad-detail access (insufficient_permissions). |  -  |
| **404** | Ad is inaccessible or unavailable on TikTok for identity resolution (ad_not_found), or the comment was not found on this ad in the selected date window (resource_not_found). |  -  |
| **422** | TikTok Ads connection is unavailable. |  -  |
| **501** | Moderation on this route supports TikTok. Use the inbox comment routes for Meta. |  -  |
| **502** | TikTok rejected the request or was unavailable. Inspect platformError for its code and message. |  -  |


## deleteAdNegativeKeywordList

> DeleteAdNegativeKeywordList200Response deleteAdNegativeKeywordList(listId, accountId, customerId, platform)

Delete a negative keyword list

Removes the Google shared negative keyword list. Detach it from all campaigns first; an in-use list is rejected. Only NEGATIVE_KEYWORDS shared sets are supported.

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
        String listId = "listId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            DeleteAdNegativeKeywordList200Response result = apiInstance.deleteAdNegativeKeywordList(listId, accountId, customerId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#deleteAdNegativeKeywordList");
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
| **listId** | **String**|  | |
| **accountId** | **String**|  | |
| **customerId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

[**DeleteAdNegativeKeywordList200Response**](DeleteAdNegativeKeywordList200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## deleteAdNegativeKeywordListWithHttpInfo

> ApiResponse<DeleteAdNegativeKeywordList200Response> deleteAdNegativeKeywordList deleteAdNegativeKeywordListWithHttpInfo(listId, accountId, customerId, platform)

Delete a negative keyword list

Removes the Google shared negative keyword list. Detach it from all campaigns first; an in-use list is rejected. Only NEGATIVE_KEYWORDS shared sets are supported.

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
        String listId = "listId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            ApiResponse<DeleteAdNegativeKeywordList200Response> response = apiInstance.deleteAdNegativeKeywordListWithHttpInfo(listId, accountId, customerId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#deleteAdNegativeKeywordList");
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
| **listId** | **String**|  | |
| **accountId** | **String**|  | |
| **customerId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

ApiResponse<[**DeleteAdNegativeKeywordList200Response**](DeleteAdNegativeKeywordList200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


## deleteValueRuleSet

> DeleteValueRuleSet200Response deleteValueRuleSet(valueRuleSetId, accountId)

Delete a value rule set

Deletes the rule set (Meta&#39;s &#x60;POST /{value-rule-set-id}/delete_rule_set&#x60;, a custom action edge rather than an HTTP DELETE on its side). Ad sets pointing at it are not modified here; detach them first with &#x60;valueRulesApplied: false&#x60; on &#x60;PUT /v1/ads/ad-sets/{adSetId}&#x60;.

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
        String valueRuleSetId = "valueRuleSetId_example"; // String | Platform value rule set id.
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            DeleteValueRuleSet200Response result = apiInstance.deleteValueRuleSet(valueRuleSetId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#deleteValueRuleSet");
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
| **valueRuleSetId** | **String**| Platform value rule set id. | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

[**DeleteValueRuleSet200Response**](DeleteValueRuleSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule set deleted |  -  |
| **400** | Invalid input, or Meta rejected the delete. A bad id comes back as GraphMethodException code 100 / subcode 33, which reads like a permission error rather than a 404. |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## deleteValueRuleSetWithHttpInfo

> ApiResponse<DeleteValueRuleSet200Response> deleteValueRuleSet deleteValueRuleSetWithHttpInfo(valueRuleSetId, accountId)

Delete a value rule set

Deletes the rule set (Meta&#39;s &#x60;POST /{value-rule-set-id}/delete_rule_set&#x60;, a custom action edge rather than an HTTP DELETE on its side). Ad sets pointing at it are not modified here; detach them first with &#x60;valueRulesApplied: false&#x60; on &#x60;PUT /v1/ads/ad-sets/{adSetId}&#x60;.

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
        String valueRuleSetId = "valueRuleSetId_example"; // String | Platform value rule set id.
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            ApiResponse<DeleteValueRuleSet200Response> response = apiInstance.deleteValueRuleSetWithHttpInfo(valueRuleSetId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#deleteValueRuleSet");
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
| **valueRuleSetId** | **String**| Platform value rule set id. | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

ApiResponse<[**DeleteValueRuleSet200Response**](DeleteValueRuleSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule set deleted |  -  |
| **400** | Invalid input, or Meta rejected the delete. A bad id comes back as GraphMethodException code 100 / subcode 33, which reads like a permission error rather than a 404. |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Account finances |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdComments

> GetAdComments200Response getAdComments(adId, placement, limit, since, until, cursor)

List comments on an ad

Returns comments on an ad&#39;s underlying creative post. Useful for moderating or analyzing engagement on dark posts (ad creatives that never went live organically), which the regular GET /v1/inbox/comments/{postId} endpoint cannot serve because dark posts are not in Zernio&#39;s post database.  An ad that runs on both Facebook feed and Instagram feed has two separate underlying posts with separate comment threads (the creative&#39;s effective_object_story_id and effective_instagram_media_id). Use the &#x60;placement&#x60; query param to pick one; with no param the Instagram side is returned when it exists, otherwise Facebook. The identifiers are read from the ad record (persisted during sync) with a Marketing-API fallback for ads that predate the field.  For Instagram-placed comments, the Instagram account that runs the ad must be connected to Zernio, because those comments are read through that account&#39;s token. If no connected Instagram account on the profile can read the ad&#39;s media, the call returns ads_connection_required (the Facebook side, if any, is still readable via ?placement&#x3D;facebook).  TikTok uses the connected TikTok Ads advertiser token and supports both paid video ads and Spark Ads. &#x60;since&#x60; and &#x60;until&#x60; select a date window of at most 30 days; the default is the last 30 days. TikTok searches by ad group, so Zernio filters each page to this ad. A page can be empty while &#x60;pagination.hasMore&#x60; is true. Reuse &#x60;pagination.cursor&#x60; with the same &#x60;limit&#x60;; the cursor retains the date window. &#x60;placement&#x60; is Meta-only and returns a 400 for TikTok. Listing needs no identity or video item ID. When the ad group is stored, each page makes one comment-list call and no ad-detail lookup, including for external ads that TikTok no longer returns from ad details. &#x60;meta.tiktokItemId: null&#x60; does not prevent listing. If the ad group is missing, Zernio fetches ad details; unavailable details return 404 ad_not_found, and no ad group returns 400 ad_not_commentable.  TikTok returns replies as separate comments with &#x60;parentId&#x60;; nested reply fetching is not supported. &#x60;canReply&#x60; requires a first-level comment, comment-management permission, a video item ID and a supported TT_USER or CUSTOMIZED_USER identity. &#x60;canDelete&#x60; requires TikTok&#39;s own-comment deletion capability, a video item ID and a supported identity. Both flags are false when identity or item is unknown. Listing uses stored and comment-specific fields without fetching identity. A direct reply or delete request can lazily resolve missing fields and succeed even after a false flag. &#x60;canHide&#x60; is true because visibility changes need only advertiser and comment IDs. &#x60;canLike&#x60; is false. Use the ad comment reply, hide and delete operations below to moderate TikTok comments. Other platforms return feature_not_available.  Requires the Ads add-on. Response shape matches GET /v1/inbox/comments/{postId}.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: Zernio internal &#x60;_id&#x60; (24-char hex), the numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;), or the creative&#39;s &#x60;effective_object_story_id&#x60; / &#x60;effective_instagram_media_id&#x60;. Caller doesn&#39;t need a translation step. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad/post ID.
        String placement = "facebook"; // String | Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement.
        Integer limit = 25; // Integer | 
        LocalDate since = LocalDate.now(); // LocalDate | TikTok-only start date. Defaults to 30 days before until. Maximum window is 30 days.
        LocalDate until = LocalDate.now(); // LocalDate | TikTok-only end date. Defaults to today in UTC.
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response.
        try {
            GetAdComments200Response result = apiInstance.getAdComments(adId, placement, limit, since, until, cursor);
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad/post ID. | |
| **placement** | **String**| Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement. | [optional] [enum: facebook, instagram] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **LocalDate**| TikTok-only start date. Defaults to 30 days before until. Maximum window is 30 days. | [optional] |
| **until** | **LocalDate**| TikTok-only end date. Defaults to today in UTC. | [optional] |
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
| **200** | Comments on the ad. |  -  |
| **400** | Invalid ad ID format, or the ad&#39;s creative format does not expose a commentable underlying post (code ad_not_commentable).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included by default on usage-based plans), or ad platform is not Meta or TikTok (code feature_not_available). |  -  |
| **404** | Resource not found |  -  |
| **422** | Ads account token unavailable, or (for Instagram-placed ads) no connected Instagram account on the profile can read the ad&#39;s media (code ads_connection_required).  |  -  |

## getAdCommentsWithHttpInfo

> ApiResponse<GetAdComments200Response> getAdComments getAdCommentsWithHttpInfo(adId, placement, limit, since, until, cursor)

List comments on an ad

Returns comments on an ad&#39;s underlying creative post. Useful for moderating or analyzing engagement on dark posts (ad creatives that never went live organically), which the regular GET /v1/inbox/comments/{postId} endpoint cannot serve because dark posts are not in Zernio&#39;s post database.  An ad that runs on both Facebook feed and Instagram feed has two separate underlying posts with separate comment threads (the creative&#39;s effective_object_story_id and effective_instagram_media_id). Use the &#x60;placement&#x60; query param to pick one; with no param the Instagram side is returned when it exists, otherwise Facebook. The identifiers are read from the ad record (persisted during sync) with a Marketing-API fallback for ads that predate the field.  For Instagram-placed comments, the Instagram account that runs the ad must be connected to Zernio, because those comments are read through that account&#39;s token. If no connected Instagram account on the profile can read the ad&#39;s media, the call returns ads_connection_required (the Facebook side, if any, is still readable via ?placement&#x3D;facebook).  TikTok uses the connected TikTok Ads advertiser token and supports both paid video ads and Spark Ads. &#x60;since&#x60; and &#x60;until&#x60; select a date window of at most 30 days; the default is the last 30 days. TikTok searches by ad group, so Zernio filters each page to this ad. A page can be empty while &#x60;pagination.hasMore&#x60; is true. Reuse &#x60;pagination.cursor&#x60; with the same &#x60;limit&#x60;; the cursor retains the date window. &#x60;placement&#x60; is Meta-only and returns a 400 for TikTok. Listing needs no identity or video item ID. When the ad group is stored, each page makes one comment-list call and no ad-detail lookup, including for external ads that TikTok no longer returns from ad details. &#x60;meta.tiktokItemId: null&#x60; does not prevent listing. If the ad group is missing, Zernio fetches ad details; unavailable details return 404 ad_not_found, and no ad group returns 400 ad_not_commentable.  TikTok returns replies as separate comments with &#x60;parentId&#x60;; nested reply fetching is not supported. &#x60;canReply&#x60; requires a first-level comment, comment-management permission, a video item ID and a supported TT_USER or CUSTOMIZED_USER identity. &#x60;canDelete&#x60; requires TikTok&#39;s own-comment deletion capability, a video item ID and a supported identity. Both flags are false when identity or item is unknown. Listing uses stored and comment-specific fields without fetching identity. A direct reply or delete request can lazily resolve missing fields and succeed even after a false flag. &#x60;canHide&#x60; is true because visibility changes need only advertiser and comment IDs. &#x60;canLike&#x60; is false. Use the ad comment reply, hide and delete operations below to moderate TikTok comments. Other platforms return feature_not_available.  Requires the Ads add-on. Response shape matches GET /v1/inbox/comments/{postId}.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: Zernio internal &#x60;_id&#x60; (24-char hex), the numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;), or the creative&#39;s &#x60;effective_object_story_id&#x60; / &#x60;effective_instagram_media_id&#x60;. Caller doesn&#39;t need a translation step. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad/post ID.
        String placement = "facebook"; // String | Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement.
        Integer limit = 25; // Integer | 
        LocalDate since = LocalDate.now(); // LocalDate | TikTok-only start date. Defaults to 30 days before until. Maximum window is 30 days.
        LocalDate until = LocalDate.now(); // LocalDate | TikTok-only end date. Defaults to today in UTC.
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response.
        try {
            ApiResponse<GetAdComments200Response> response = apiInstance.getAdCommentsWithHttpInfo(adId, placement, limit, since, until, cursor);
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad/post ID. | |
| **placement** | **String**| Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement. | [optional] [enum: facebook, instagram] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **LocalDate**| TikTok-only start date. Defaults to 30 days before until. Maximum window is 30 days. | [optional] |
| **until** | **LocalDate**| TikTok-only end date. Defaults to today in UTC. | [optional] |
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
| **200** | Comments on the ad. |  -  |
| **400** | Invalid ad ID format, or the ad&#39;s creative format does not expose a commentable underlying post (code ad_not_commentable).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included by default on usage-based plans), or ad platform is not Meta or TikTok (code feature_not_available). |  -  |
| **404** | Resource not found |  -  |
| **422** | Ads account token unavailable, or (for Instagram-placed ads) no connected Instagram account on the profile can read the ad&#39;s media (code ads_connection_required).  |  -  |


## getAdNegativeKeywordList

> GetAdNegativeKeywordList200Response getAdNegativeKeywordList(listId, accountId, customerId, platform)

Get a negative keyword list

Google Ads shared negative keyword lists (shared_set type NEGATIVE_KEYWORDS). Reads are cached for 10 minutes; quota exhaustion may return the last successful result for up to 7 days with stale&#x3D;true. Customer selection is limited to this connection and its account scope. Includes the keywords and their criterion ids.

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
        String listId = "listId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            GetAdNegativeKeywordList200Response result = apiInstance.getAdNegativeKeywordList(listId, accountId, customerId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdNegativeKeywordList");
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
| **listId** | **String**|  | |
| **accountId** | **String**|  | |
| **customerId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

[**GetAdNegativeKeywordList200Response**](GetAdNegativeKeywordList200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## getAdNegativeKeywordListWithHttpInfo

> ApiResponse<GetAdNegativeKeywordList200Response> getAdNegativeKeywordList getAdNegativeKeywordListWithHttpInfo(listId, accountId, customerId, platform)

Get a negative keyword list

Google Ads shared negative keyword lists (shared_set type NEGATIVE_KEYWORDS). Reads are cached for 10 minutes; quota exhaustion may return the last successful result for up to 7 days with stale&#x3D;true. Customer selection is limited to this connection and its account scope. Includes the keywords and their criterion ids.

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
        String listId = "listId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            ApiResponse<GetAdNegativeKeywordList200Response> response = apiInstance.getAdNegativeKeywordListWithHttpInfo(listId, accountId, customerId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getAdNegativeKeywordList");
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
| **listId** | **String**|  | |
| **accountId** | **String**|  | |
| **customerId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

ApiResponse<[**GetAdNegativeKeywordList200Response**](GetAdNegativeKeywordList200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
        String accountId = "accountId_example"; // String | Account ID (metaads, or a facebook/instagram posting account)
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
| **accountId** | **String**| Account ID (metaads, or a facebook/instagram posting account) | |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Current DSA defaults (empty object when none are set) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |

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
        String accountId = "accountId_example"; // String | Account ID (metaads, or a facebook/instagram posting account)
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
| **accountId** | **String**| Account ID (metaads, or a facebook/instagram posting account) | |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Current DSA defaults (empty object when none are set) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |


## getDsaRecommendations

> GetDsaRecommendations200Response getDsaRecommendations(accountId, adAccountId)

Get DSA recommendations

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
        String accountId = "accountId_example"; // String | Account ID (metaads, or a facebook/instagram posting account)
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
| **accountId** | **String**| Account ID (metaads, or a facebook/instagram posting account) | |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Suggested DSA strings (may be empty when Meta has no recommendations) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |

## getDsaRecommendationsWithHttpInfo

> ApiResponse<GetDsaRecommendations200Response> getDsaRecommendations getDsaRecommendationsWithHttpInfo(accountId, adAccountId)

Get DSA recommendations

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
        String accountId = "accountId_example"; // String | Account ID (metaads, or a facebook/instagram posting account)
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
| **accountId** | **String**| Account ID (metaads, or a facebook/instagram posting account) | |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Suggested DSA strings (may be empty when Meta has no recommendations) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |


## getIosFourteenCampaignLimits

> GetIosFourteenCampaignLimits200Response getIosFourteenCampaignLimits(accountId, adAccountId, applicationId)

Get iOS 14 campaign limits

Reads Meta iOS 14 campaign limits for an application on an ad account. applicationId is sent as Meta app_id. This read does not establish that the application is configured for iOS promotion.

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
        String accountId = "accountId_example"; // String | Zernio Meta Ads or Facebook SocialAccount ID.
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID including the act_ prefix.
        String applicationId = "applicationId_example"; // String | Meta application ID from advertisable-applications.
        try {
            GetIosFourteenCampaignLimits200Response result = apiInstance.getIosFourteenCampaignLimits(accountId, adAccountId, applicationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getIosFourteenCampaignLimits");
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
| **accountId** | **String**| Zernio Meta Ads or Facebook SocialAccount ID. | |
| **adAccountId** | **String**| Meta ad account ID including the act_ prefix. | |
| **applicationId** | **String**| Meta application ID from advertisable-applications. | |

### Return type

[**GetIosFourteenCampaignLimits200Response**](GetIosFourteenCampaignLimits200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Application campaign limits. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The account or Meta asset is not accessible. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta Ads and Facebook accounts. |  -  |

## getIosFourteenCampaignLimitsWithHttpInfo

> ApiResponse<GetIosFourteenCampaignLimits200Response> getIosFourteenCampaignLimits getIosFourteenCampaignLimitsWithHttpInfo(accountId, adAccountId, applicationId)

Get iOS 14 campaign limits

Reads Meta iOS 14 campaign limits for an application on an ad account. applicationId is sent as Meta app_id. This read does not establish that the application is configured for iOS promotion.

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
        String accountId = "accountId_example"; // String | Zernio Meta Ads or Facebook SocialAccount ID.
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID including the act_ prefix.
        String applicationId = "applicationId_example"; // String | Meta application ID from advertisable-applications.
        try {
            ApiResponse<GetIosFourteenCampaignLimits200Response> response = apiInstance.getIosFourteenCampaignLimitsWithHttpInfo(accountId, adAccountId, applicationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getIosFourteenCampaignLimits");
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
| **accountId** | **String**| Zernio Meta Ads or Facebook SocialAccount ID. | |
| **adAccountId** | **String**| Meta ad account ID including the act_ prefix. | |
| **applicationId** | **String**| Meta application ID from advertisable-applications. | |

### Return type

ApiResponse<[**GetIosFourteenCampaignLimits200Response**](GetIosFourteenCampaignLimits200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Application campaign limits. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The account or Meta asset is not accessible. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta Ads and Facebook accounts. |  -  |


## getValueRuleSet

> GetValueRuleSet200Response getValueRuleSet(valueRuleSetId, accountId)

Read a value rule set

Reads one value rule set including every nested rule id and criterion id. This is step one of any edit: &#x60;PUT&#x60; is a full replace, so you need the ids before you can keep the objects you are not changing.  Meta&#39;s own read returns &#x60;GENDER&#x60; values lowercase (&#x60;\&quot;male\&quot;&#x60;) while writes require &#x60;\&quot;MALE\&quot;&#x60;. Values are passed through untouched, so never case-compare a stored rule against a fetched one.

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
        String valueRuleSetId = "valueRuleSetId_example"; // String | Platform value rule set id.
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            GetValueRuleSet200Response result = apiInstance.getValueRuleSet(valueRuleSetId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getValueRuleSet");
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
| **valueRuleSetId** | **String**| Platform value rule set id. | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

[**GetValueRuleSet200Response**](GetValueRuleSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule set |  -  |
| **400** | Invalid input, or Meta rejected the read. A bad id comes back as GraphMethodException code 100 / subcode 33, which cannot be told apart from a permission problem. |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getValueRuleSetWithHttpInfo

> ApiResponse<GetValueRuleSet200Response> getValueRuleSet getValueRuleSetWithHttpInfo(valueRuleSetId, accountId)

Read a value rule set

Reads one value rule set including every nested rule id and criterion id. This is step one of any edit: &#x60;PUT&#x60; is a full replace, so you need the ids before you can keep the objects you are not changing.  Meta&#39;s own read returns &#x60;GENDER&#x60; values lowercase (&#x60;\&quot;male\&quot;&#x60;) while writes require &#x60;\&quot;MALE\&quot;&#x60;. Values are passed through untouched, so never case-compare a stored rule against a fetched one.

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
        String valueRuleSetId = "valueRuleSetId_example"; // String | Platform value rule set id.
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            ApiResponse<GetValueRuleSet200Response> response = apiInstance.getValueRuleSetWithHttpInfo(valueRuleSetId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#getValueRuleSet");
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
| **valueRuleSetId** | **String**| Platform value rule set id. | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

ApiResponse<[**GetValueRuleSet200Response**](GetValueRuleSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule set |  -  |
| **400** | Invalid input, or Meta rejected the read. A bad id comes back as GraphMethodException code 100 / subcode 33, which cannot be told apart from a permission problem. |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## hideAdComment

> HideAdComment200Response hideAdComment(adId, commentId, hideAdCommentRequest, since, until)

Hide or unhide an ad comment

Hide or restore a TikTok ad comment. Send hidden&#x3D;true to hide it or hidden&#x3D;false to make it public again. Identity and video item ID are not required; no identity lookup is performed.  Requires Ads access. The ad is resolved within the caller&#39;s accessible profiles. Before moderation, Zernio verifies that the comment belongs to this ad using TikTok&#39;s ad-group comment listing. The default search window is the last 30 days. Use since/until for older comments, with at most 30 days between the dates. Lookups scan at most 2,000 ad-group comments; narrow the date window if exceeded. Meta returns 501 feature_not_available with guidance to use the existing inbox comment endpoints and the account/post IDs from GET /v1/ads/{adId}/comments. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad ID.
        String commentId = "commentId_example"; // String | TikTok comment ID from the ad comment listing.
        HideAdCommentRequest hideAdCommentRequest = new HideAdCommentRequest(); // HideAdCommentRequest | 
        LocalDate since = LocalDate.now(); // LocalDate | Start date of the comment lookup window. Defaults to 30 days before until.
        LocalDate until = LocalDate.now(); // LocalDate | End date of the comment lookup window. Defaults to today in UTC.
        try {
            HideAdComment200Response result = apiInstance.hideAdComment(adId, commentId, hideAdCommentRequest, since, until);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#hideAdComment");
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad ID. | |
| **commentId** | **String**| TikTok comment ID from the ad comment listing. | |
| **hideAdCommentRequest** | [**HideAdCommentRequest**](HideAdCommentRequest.md)|  | |
| **since** | **LocalDate**| Start date of the comment lookup window. Defaults to 30 days before until. | [optional] |
| **until** | **LocalDate**| End date of the comment lookup window. Defaults to today in UTC. | [optional] |

### Return type

[**HideAdComment200Response**](HideAdComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment action completed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access or the required TikTok comment capability is unavailable. |  -  |
| **404** | Ad is inaccessible or the comment was not found on this ad in the selected date window. |  -  |
| **422** | TikTok Ads connection is unavailable. |  -  |
| **501** | Moderation on this route supports TikTok. Use the inbox comment routes for Meta. |  -  |
| **502** | TikTok rejected the request or was unavailable. Inspect platformError for its code and message. |  -  |

## hideAdCommentWithHttpInfo

> ApiResponse<HideAdComment200Response> hideAdComment hideAdCommentWithHttpInfo(adId, commentId, hideAdCommentRequest, since, until)

Hide or unhide an ad comment

Hide or restore a TikTok ad comment. Send hidden&#x3D;true to hide it or hidden&#x3D;false to make it public again. Identity and video item ID are not required; no identity lookup is performed.  Requires Ads access. The ad is resolved within the caller&#39;s accessible profiles. Before moderation, Zernio verifies that the comment belongs to this ad using TikTok&#39;s ad-group comment listing. The default search window is the last 30 days. Use since/until for older comments, with at most 30 days between the dates. Lookups scan at most 2,000 ad-group comments; narrow the date window if exceeded. Meta returns 501 feature_not_available with guidance to use the existing inbox comment endpoints and the account/post IDs from GET /v1/ads/{adId}/comments. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad ID.
        String commentId = "commentId_example"; // String | TikTok comment ID from the ad comment listing.
        HideAdCommentRequest hideAdCommentRequest = new HideAdCommentRequest(); // HideAdCommentRequest | 
        LocalDate since = LocalDate.now(); // LocalDate | Start date of the comment lookup window. Defaults to 30 days before until.
        LocalDate until = LocalDate.now(); // LocalDate | End date of the comment lookup window. Defaults to today in UTC.
        try {
            ApiResponse<HideAdComment200Response> response = apiInstance.hideAdCommentWithHttpInfo(adId, commentId, hideAdCommentRequest, since, until);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#hideAdComment");
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad ID. | |
| **commentId** | **String**| TikTok comment ID from the ad comment listing. | |
| **hideAdCommentRequest** | [**HideAdCommentRequest**](HideAdCommentRequest.md)|  | |
| **since** | **LocalDate**| Start date of the comment lookup window. Defaults to 30 days before until. | [optional] |
| **until** | **LocalDate**| End date of the comment lookup window. Defaults to today in UTC. | [optional] |

### Return type

ApiResponse<[**HideAdComment200Response**](HideAdComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment action completed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access or the required TikTok comment capability is unavailable. |  -  |
| **404** | Ad is inaccessible or the comment was not found on this ad in the selected date window. |  -  |
| **422** | TikTok Ads connection is unavailable. |  -  |
| **501** | Moderation on this route supports TikTok. Use the inbox comment routes for Meta. |  -  |
| **502** | TikTok rejected the request or was unavailable. Inspect platformError for its code and message. |  -  |


## listAccountCallouts

> ListAccountCallouts200Response listAccountCallouts(accountId, customerId)

List account callouts

Lists directly attached Google assets. Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included. Preserves Google RMF C.75 account-level callouts.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ListAccountCallouts200Response result = apiInstance.listAccountCallouts(accountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAccountCallouts");
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
| **customerId** | **String**|  | [optional] |

### Return type

[**ListAccountCallouts200Response**](ListAccountCallouts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## listAccountCalloutsWithHttpInfo

> ApiResponse<ListAccountCallouts200Response> listAccountCallouts listAccountCalloutsWithHttpInfo(accountId, customerId)

List account callouts

Lists directly attached Google assets. Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included. Preserves Google RMF C.75 account-level callouts.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ApiResponse<ListAccountCallouts200Response> response = apiInstance.listAccountCalloutsWithHttpInfo(accountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAccountCallouts");
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
| **customerId** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListAccountCallouts200Response**](ListAccountCallouts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## listAccountSitelinks

> ListAccountSitelinks200Response listAccountSitelinks(accountId, customerId)

List account sitelinks

Lists directly attached Google assets. Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ListAccountSitelinks200Response result = apiInstance.listAccountSitelinks(accountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAccountSitelinks");
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
| **customerId** | **String**|  | [optional] |

### Return type

[**ListAccountSitelinks200Response**](ListAccountSitelinks200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## listAccountSitelinksWithHttpInfo

> ApiResponse<ListAccountSitelinks200Response> listAccountSitelinks listAccountSitelinksWithHttpInfo(accountId, customerId)

List account sitelinks

Lists directly attached Google assets. Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ApiResponse<ListAccountSitelinks200Response> response = apiInstance.listAccountSitelinksWithHttpInfo(accountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAccountSitelinks");
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
| **customerId** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListAccountSitelinks200Response**](ListAccountSitelinks200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## listAccountStructuredSnippets

> ListAccountStructuredSnippets200Response listAccountStructuredSnippets(accountId, customerId)

List account snippets

Lists directly attached Google assets. Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ListAccountStructuredSnippets200Response result = apiInstance.listAccountStructuredSnippets(accountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAccountStructuredSnippets");
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
| **customerId** | **String**|  | [optional] |

### Return type

[**ListAccountStructuredSnippets200Response**](ListAccountStructuredSnippets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## listAccountStructuredSnippetsWithHttpInfo

> ApiResponse<ListAccountStructuredSnippets200Response> listAccountStructuredSnippets listAccountStructuredSnippetsWithHttpInfo(accountId, customerId)

List account snippets

Lists directly attached Google assets. Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ApiResponse<ListAccountStructuredSnippets200Response> response = apiInstance.listAccountStructuredSnippetsWithHttpInfo(accountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAccountStructuredSnippets");
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
| **customerId** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListAccountStructuredSnippets200Response**](ListAccountStructuredSnippets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## listAdAccounts

> ListAdAccounts200Response listAdAccounts(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs). Meta business-login accounts use their own system-user token. Fresh Meta discovery includes businessId and businessName from the owning Business Manager when available; cached entries gain these fields after the next discovery refresh.  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry.  For Google Ads: responds &#x60;429&#x60; when Google&#39;s API quota is temporarily exhausted (instead of an empty list). Retry after a delay. 

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
        String accountId = "accountId_example"; // String | Account ID
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
| **accountId** | **String**| Account ID | |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **400** | Invalid request |  -  |
| **200** | Ad accounts |  -  |
| **401** | Unauthorized |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or Instagram missing linked Facebook account |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## listAdAccountsWithHttpInfo

> ApiResponse<ListAdAccounts200Response> listAdAccounts listAdAccountsWithHttpInfo(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs). Meta business-login accounts use their own system-user token. Fresh Meta discovery includes businessId and businessName from the owning Business Manager when available; cached entries gain these fields after the next discovery refresh.  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry.  For Google Ads: responds &#x60;429&#x60; when Google&#39;s API quota is temporarily exhausted (instead of an empty list). Retry after a delay. 

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
        String accountId = "accountId_example"; // String | Account ID
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
| **accountId** | **String**| Account ID | |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **400** | Invalid request |  -  |
| **200** | Ad accounts |  -  |
| **401** | Unauthorized |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or Instagram missing linked Facebook account |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Ad labels (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdNegativeKeywordLists

> ListAdNegativeKeywordLists200Response listAdNegativeKeywordLists(accountId, customerId, platform)

List negative keyword lists

Google Ads shared negative keyword lists (shared_set type NEGATIVE_KEYWORDS). Reads are cached for 10 minutes; quota exhaustion may return the last successful result for up to 7 days with stale&#x3D;true. Customer selection is limited to this connection and its account scope.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            ListAdNegativeKeywordLists200Response result = apiInstance.listAdNegativeKeywordLists(accountId, customerId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdNegativeKeywordLists");
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
| **customerId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

[**ListAdNegativeKeywordLists200Response**](ListAdNegativeKeywordLists200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## listAdNegativeKeywordListsWithHttpInfo

> ApiResponse<ListAdNegativeKeywordLists200Response> listAdNegativeKeywordLists listAdNegativeKeywordListsWithHttpInfo(accountId, customerId, platform)

List negative keyword lists

Google Ads shared negative keyword lists (shared_set type NEGATIVE_KEYWORDS). Reads are cached for 10 minutes; quota exhaustion may return the last successful result for up to 7 days with stale&#x3D;true. Customer selection is limited to this connection and its account scope.

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
        String accountId = "accountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            ApiResponse<ListAdNegativeKeywordLists200Response> response = apiInstance.listAdNegativeKeywordListsWithHttpInfo(accountId, customerId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdNegativeKeywordLists");
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
| **customerId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai] |

### Return type

ApiResponse<[**ListAdNegativeKeywordLists200Response**](ListAdNegativeKeywordLists200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


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
        String fields = "id,name,type,cells{id,name,treatment_percentage}"; // String | Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently.
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
| **fields** | **String**| Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently. | [optional] |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
        String fields = "id,name,type,cells{id,name,treatment_percentage}"; // String | Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently.
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
| **fields** | **String**| Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently. | [optional] |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Business centers |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Business centers |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | TikTok Ads not connected |  -  |


## listAdsInstagramAccounts

> ListAdsInstagramAccounts200Response listAdsInstagramAccounts(accountId, adAccountId)

List Instagram ad identities

Discovers identities through connected_instagram_accounts, Page linkage and Page-backed identities, with a best-effort business fallback. Business permission errors do not fail discovery. The resolved object uses the same profile-scoped resolver as ad creation; null means no identity was resolved. Format-specific observed-actor fallbacks at creative creation are not predicted.

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
        String accountId = "accountId_example"; // String | Zernio Meta Ads or Facebook SocialAccount ID.
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID including the act_ prefix.
        try {
            ListAdsInstagramAccounts200Response result = apiInstance.listAdsInstagramAccounts(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdsInstagramAccounts");
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
| **accountId** | **String**| Zernio Meta Ads or Facebook SocialAccount ID. | |
| **adAccountId** | **String**| Meta ad account ID including the act_ prefix. | |

### Return type

[**ListAdsInstagramAccounts200Response**](ListAdsInstagramAccounts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Instagram identities and Page linkage. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The account or Meta asset is not accessible. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta Ads and Facebook accounts. |  -  |

## listAdsInstagramAccountsWithHttpInfo

> ApiResponse<ListAdsInstagramAccounts200Response> listAdsInstagramAccounts listAdsInstagramAccountsWithHttpInfo(accountId, adAccountId)

List Instagram ad identities

Discovers identities through connected_instagram_accounts, Page linkage and Page-backed identities, with a best-effort business fallback. Business permission errors do not fail discovery. The resolved object uses the same profile-scoped resolver as ad creation; null means no identity was resolved. Format-specific observed-actor fallbacks at creative creation are not predicted.

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
        String accountId = "accountId_example"; // String | Zernio Meta Ads or Facebook SocialAccount ID.
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID including the act_ prefix.
        try {
            ApiResponse<ListAdsInstagramAccounts200Response> response = apiInstance.listAdsInstagramAccountsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdsInstagramAccounts");
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
| **accountId** | **String**| Zernio Meta Ads or Facebook SocialAccount ID. | |
| **adAccountId** | **String**| Meta ad account ID including the act_ prefix. | |

### Return type

ApiResponse<[**ListAdsInstagramAccounts200Response**](ListAdsInstagramAccounts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Instagram identities and Page linkage. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The account or Meta asset is not accessible. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta Ads and Facebook accounts. |  -  |


## listAdvertisableApplications

> ListAdvertisableApplications200Response listAdvertisableApplications(accountId, adAccountId)

List advertisable apps

Lists applications available to a Meta ad account, their supported platforms and unmodified object store URLs. A listed app still needs a configured mobile platform and store URL to run install promotion.

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
        String accountId = "accountId_example"; // String | Zernio Meta Ads or Facebook SocialAccount ID.
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID including the act_ prefix.
        try {
            ListAdvertisableApplications200Response result = apiInstance.listAdvertisableApplications(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdvertisableApplications");
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
| **accountId** | **String**| Zernio Meta Ads or Facebook SocialAccount ID. | |
| **adAccountId** | **String**| Meta ad account ID including the act_ prefix. | |

### Return type

[**ListAdvertisableApplications200Response**](ListAdvertisableApplications200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Applications available for promotion. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The account or Meta asset is not accessible. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta Ads and Facebook accounts. |  -  |

## listAdvertisableApplicationsWithHttpInfo

> ApiResponse<ListAdvertisableApplications200Response> listAdvertisableApplications listAdvertisableApplicationsWithHttpInfo(accountId, adAccountId)

List advertisable apps

Lists applications available to a Meta ad account, their supported platforms and unmodified object store URLs. A listed app still needs a configured mobile platform and store URL to run install promotion.

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
        String accountId = "accountId_example"; // String | Zernio Meta Ads or Facebook SocialAccount ID.
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID including the act_ prefix.
        try {
            ApiResponse<ListAdvertisableApplications200Response> response = apiInstance.listAdvertisableApplicationsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listAdvertisableApplications");
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
| **accountId** | **String**| Zernio Meta Ads or Facebook SocialAccount ID. | |
| **adAccountId** | **String**| Meta ad account ID including the act_ prefix. | |

### Return type

ApiResponse<[**ListAdvertisableApplications200Response**](ListAdvertisableApplications200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Applications available for promotion. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | The account or Meta asset is not accessible. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only supported on Meta Ads and Facebook accounts. |  -  |


## listCustomConversions

> ListCustomConversions200Response listCustomConversions(accountId, adAccountId)

List custom conversions

The ad account&#39;s Meta custom conversions, including archived ones (&#x60;isArchived&#x60;).

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
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        try {
            ListCustomConversions200Response result = apiInstance.listCustomConversions(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listCustomConversions");
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
| **accountId** | **String**| Meta ads SocialAccount id. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |

### Return type

[**ListCustomConversions200Response**](ListCustomConversions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Custom conversions |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the token lacks the ads permissions. |  -  |

## listCustomConversionsWithHttpInfo

> ApiResponse<ListCustomConversions200Response> listCustomConversions listCustomConversionsWithHttpInfo(accountId, adAccountId)

List custom conversions

The ad account&#39;s Meta custom conversions, including archived ones (&#x60;isArchived&#x60;).

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
        String accountId = "accountId_example"; // String | Meta ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        try {
            ApiResponse<ListCustomConversions200Response> response = apiInstance.listCustomConversionsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listCustomConversions");
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
| **accountId** | **String**| Meta ads SocialAccount id. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |

### Return type

ApiResponse<[**ListCustomConversions200Response**](ListCustomConversions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Custom conversions |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the token lacks the ads permissions. |  -  |


## listHighDemandPeriods

> ListHighDemandPeriods200Response listHighDemandPeriods(accountId, campaignId, adSetId, limit, after)

List high-demand periods

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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Budget schedules (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listHighDemandPeriodsWithHttpInfo

> ApiResponse<ListHighDemandPeriods200Response> listHighDemandPeriods listHighDemandPeriodsWithHttpInfo(accountId, campaignId, adSetId, limit, after)

List high-demand periods

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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Businesses (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listTikTokAdPixels

> ListTikTokAdPixels200Response listTikTokAdPixels(accountId, advertiserId, code)

List TikTok ad pixels

Lists pixels and their supported optimization events for a connected TikTok Ads account. The advertiser defaults to the first advertiser on the connection. Reconnect if Pixel Management permission has not been granted.

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
        String accountId = "accountId_example"; // String | Zernio SocialAccount ID.
        String advertiserId = "advertiserId_example"; // String | Advertiser belonging to this connection.
        String code = "code_example"; // String | Filter by a Pixel Code.
        try {
            ListTikTokAdPixels200Response result = apiInstance.listTikTokAdPixels(accountId, advertiserId, code);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listTikTokAdPixels");
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
| **accountId** | **String**| Zernio SocialAccount ID. | |
| **advertiserId** | **String**| Advertiser belonging to this connection. | [optional] |
| **code** | **String**| Filter by a Pixel Code. | [optional] |

### Return type

[**ListTikTokAdPixels200Response**](ListTikTokAdPixels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TikTok pixels. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **422** | Pixel Management permission is missing (code reconnect_required). Reconnect TikTok Ads to grant it. |  -  |

## listTikTokAdPixelsWithHttpInfo

> ApiResponse<ListTikTokAdPixels200Response> listTikTokAdPixels listTikTokAdPixelsWithHttpInfo(accountId, advertiserId, code)

List TikTok ad pixels

Lists pixels and their supported optimization events for a connected TikTok Ads account. The advertiser defaults to the first advertiser on the connection. Reconnect if Pixel Management permission has not been granted.

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
        String accountId = "accountId_example"; // String | Zernio SocialAccount ID.
        String advertiserId = "advertiserId_example"; // String | Advertiser belonging to this connection.
        String code = "code_example"; // String | Filter by a Pixel Code.
        try {
            ApiResponse<ListTikTokAdPixels200Response> response = apiInstance.listTikTokAdPixelsWithHttpInfo(accountId, advertiserId, code);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listTikTokAdPixels");
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
| **accountId** | **String**| Zernio SocialAccount ID. | |
| **advertiserId** | **String**| Advertiser belonging to this connection. | [optional] |
| **code** | **String**| Filter by a Pixel Code. | [optional] |

### Return type

ApiResponse<[**ListTikTokAdPixels200Response**](ListTikTokAdPixels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TikTok pixels. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **422** | Pixel Management permission is missing (code reconnect_required). Reconnect TikTok Ads to grant it. |  -  |


## listValueRuleSets

> ListValueRuleSets200Response listValueRuleSets(accountId, adAccountId, limit, after)

List value rule sets

Lists the ad account&#39;s value rule sets (Meta&#39;s &#x60;/act_X/value_rule_set&#x60;). A value rule set adjusts the auction bid up or down for audience segments you value differently; attach one to an ad set with &#x60;valueRuleSetId&#x60; on &#x60;POST /v1/ads/create&#x60; or &#x60;PUT /v1/ads/ad-sets/{adSetId}&#x60;.  Rows are returned in the same camelCase shape the &#x60;PUT&#x60; body takes, ids included, so a set round-trips 1:1: **the update is a full replace, not a patch**, so you GET, mutate and send the whole thing back.  Limits: 6 rule sets per ad account, 10 rules per set, 4 criteria per rule.  **Rule order is semantic.** Rules are evaluated in array order and only the FIRST matching rule adjusts the bid for an overlapping audience. The order you send is the order that is stored and returned.  Eligibility: value rule sets apply only to ad sets on the &#x60;LOWEST_COST_WITHOUT_CAP&#x60; (auto-bid) or &#x60;COST_CAP&#x60; bid strategies. Meta rejects the rest server-side.

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
        String after = "after_example"; // String | Cursor from paging.after of the previous page. Meta does not document paging on this edge; `after` comes back null when it omits cursors.
        try {
            ListValueRuleSets200Response result = apiInstance.listValueRuleSets(accountId, adAccountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listValueRuleSets");
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
| **after** | **String**| Cursor from paging.after of the previous page. Meta does not document paging on this edge; &#x60;after&#x60; comes back null when it omits cursors. | [optional] |

### Return type

[**ListValueRuleSets200Response**](ListValueRuleSets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule sets |  -  |
| **400** | Invalid input, or Meta rejected the query. Meta answers a bad rule-set id with GraphMethodException code 100 / subcode 33, which is indistinguishable between not-found, no-permission, and account-not-enabled. |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listValueRuleSetsWithHttpInfo

> ApiResponse<ListValueRuleSets200Response> listValueRuleSets listValueRuleSetsWithHttpInfo(accountId, adAccountId, limit, after)

List value rule sets

Lists the ad account&#39;s value rule sets (Meta&#39;s &#x60;/act_X/value_rule_set&#x60;). A value rule set adjusts the auction bid up or down for audience segments you value differently; attach one to an ad set with &#x60;valueRuleSetId&#x60; on &#x60;POST /v1/ads/create&#x60; or &#x60;PUT /v1/ads/ad-sets/{adSetId}&#x60;.  Rows are returned in the same camelCase shape the &#x60;PUT&#x60; body takes, ids included, so a set round-trips 1:1: **the update is a full replace, not a patch**, so you GET, mutate and send the whole thing back.  Limits: 6 rule sets per ad account, 10 rules per set, 4 criteria per rule.  **Rule order is semantic.** Rules are evaluated in array order and only the FIRST matching rule adjusts the bid for an overlapping audience. The order you send is the order that is stored and returned.  Eligibility: value rule sets apply only to ad sets on the &#x60;LOWEST_COST_WITHOUT_CAP&#x60; (auto-bid) or &#x60;COST_CAP&#x60; bid strategies. Meta rejects the rest server-side.

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
        String after = "after_example"; // String | Cursor from paging.after of the previous page. Meta does not document paging on this edge; `after` comes back null when it omits cursors.
        try {
            ApiResponse<ListValueRuleSets200Response> response = apiInstance.listValueRuleSetsWithHttpInfo(accountId, adAccountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#listValueRuleSets");
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
| **after** | **String**| Cursor from paging.after of the previous page. Meta does not document paging on this edge; &#x60;after&#x60; comes back null when it omits cursors. | [optional] |

### Return type

ApiResponse<[**ListValueRuleSets200Response**](ListValueRuleSets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule sets |  -  |
| **400** | Invalid input, or Meta rejected the query. Meta answers a bad rule-set id with GraphMethodException code 100 / subcode 33, which is indistinguishable between not-found, no-permission, and account-not-enabled. |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## removeAccountCallout

> RemoveAccountCallout200Response removeAccountCallout(removeAccountCalloutRequest)

Remove account callout

Removes the customer_asset attachment only. The underlying shared asset and its campaign or ad-group attachments remain.

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
        RemoveAccountCalloutRequest removeAccountCalloutRequest = new RemoveAccountCalloutRequest(); // RemoveAccountCalloutRequest | 
        try {
            RemoveAccountCallout200Response result = apiInstance.removeAccountCallout(removeAccountCalloutRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#removeAccountCallout");
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
| **removeAccountCalloutRequest** | [**RemoveAccountCalloutRequest**](RemoveAccountCalloutRequest.md)|  | |

### Return type

[**RemoveAccountCallout200Response**](RemoveAccountCallout200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## removeAccountCalloutWithHttpInfo

> ApiResponse<RemoveAccountCallout200Response> removeAccountCallout removeAccountCalloutWithHttpInfo(removeAccountCalloutRequest)

Remove account callout

Removes the customer_asset attachment only. The underlying shared asset and its campaign or ad-group attachments remain.

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
        RemoveAccountCalloutRequest removeAccountCalloutRequest = new RemoveAccountCalloutRequest(); // RemoveAccountCalloutRequest | 
        try {
            ApiResponse<RemoveAccountCallout200Response> response = apiInstance.removeAccountCalloutWithHttpInfo(removeAccountCalloutRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#removeAccountCallout");
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
| **removeAccountCalloutRequest** | [**RemoveAccountCalloutRequest**](RemoveAccountCalloutRequest.md)|  | |

### Return type

ApiResponse<[**RemoveAccountCallout200Response**](RemoveAccountCallout200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## removeAccountSitelink

> RemoveAccountCallout200Response removeAccountSitelink(removeAccountCalloutRequest)

Remove account sitelink

Removes the customer_asset attachment only. The underlying shared asset and its campaign or ad-group attachments remain.

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
        RemoveAccountCalloutRequest removeAccountCalloutRequest = new RemoveAccountCalloutRequest(); // RemoveAccountCalloutRequest | 
        try {
            RemoveAccountCallout200Response result = apiInstance.removeAccountSitelink(removeAccountCalloutRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#removeAccountSitelink");
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
| **removeAccountCalloutRequest** | [**RemoveAccountCalloutRequest**](RemoveAccountCalloutRequest.md)|  | |

### Return type

[**RemoveAccountCallout200Response**](RemoveAccountCallout200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## removeAccountSitelinkWithHttpInfo

> ApiResponse<RemoveAccountCallout200Response> removeAccountSitelink removeAccountSitelinkWithHttpInfo(removeAccountCalloutRequest)

Remove account sitelink

Removes the customer_asset attachment only. The underlying shared asset and its campaign or ad-group attachments remain.

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
        RemoveAccountCalloutRequest removeAccountCalloutRequest = new RemoveAccountCalloutRequest(); // RemoveAccountCalloutRequest | 
        try {
            ApiResponse<RemoveAccountCallout200Response> response = apiInstance.removeAccountSitelinkWithHttpInfo(removeAccountCalloutRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#removeAccountSitelink");
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
| **removeAccountCalloutRequest** | [**RemoveAccountCalloutRequest**](RemoveAccountCalloutRequest.md)|  | |

### Return type

ApiResponse<[**RemoveAccountCallout200Response**](RemoveAccountCallout200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## removeAccountStructuredSnippet

> RemoveAccountCallout200Response removeAccountStructuredSnippet(removeAccountCalloutRequest)

Remove account snippet

Removes the customer_asset attachment only. The underlying shared asset and its campaign or ad-group attachments remain.

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
        RemoveAccountCalloutRequest removeAccountCalloutRequest = new RemoveAccountCalloutRequest(); // RemoveAccountCalloutRequest | 
        try {
            RemoveAccountCallout200Response result = apiInstance.removeAccountStructuredSnippet(removeAccountCalloutRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#removeAccountStructuredSnippet");
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
| **removeAccountCalloutRequest** | [**RemoveAccountCalloutRequest**](RemoveAccountCalloutRequest.md)|  | |

### Return type

[**RemoveAccountCallout200Response**](RemoveAccountCallout200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## removeAccountStructuredSnippetWithHttpInfo

> ApiResponse<RemoveAccountCallout200Response> removeAccountStructuredSnippet removeAccountStructuredSnippetWithHttpInfo(removeAccountCalloutRequest)

Remove account snippet

Removes the customer_asset attachment only. The underlying shared asset and its campaign or ad-group attachments remain.

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
        RemoveAccountCalloutRequest removeAccountCalloutRequest = new RemoveAccountCalloutRequest(); // RemoveAccountCalloutRequest | 
        try {
            ApiResponse<RemoveAccountCallout200Response> response = apiInstance.removeAccountStructuredSnippetWithHttpInfo(removeAccountCalloutRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#removeAccountStructuredSnippet");
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
| **removeAccountCalloutRequest** | [**RemoveAccountCalloutRequest**](RemoveAccountCalloutRequest.md)|  | |

### Return type

ApiResponse<[**RemoveAccountCallout200Response**](RemoveAccountCallout200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## replaceAdNegativeKeywordListKeywords

> ReplaceAdNegativeKeywordListKeywords200Response replaceAdNegativeKeywordListKeywords(listId, replaceAdNegativeKeywordListKeywordsRequest)

Replace negative list keywords

Replaces the full desired keyword set. Existing keywords are diffed by normalized text and match type; creates and removals are applied atomically in one mutation. Unchanged criteria retain their ids. Send an empty keywords array to clear the list. Changes affect every campaign using this list. Each create or removal consumes one daily operation; the entire batch must fit the remaining quota.

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
        String listId = "listId_example"; // String | 
        ReplaceAdNegativeKeywordListKeywordsRequest replaceAdNegativeKeywordListKeywordsRequest = new ReplaceAdNegativeKeywordListKeywordsRequest(); // ReplaceAdNegativeKeywordListKeywordsRequest | 
        try {
            ReplaceAdNegativeKeywordListKeywords200Response result = apiInstance.replaceAdNegativeKeywordListKeywords(listId, replaceAdNegativeKeywordListKeywordsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#replaceAdNegativeKeywordListKeywords");
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
| **listId** | **String**|  | |
| **replaceAdNegativeKeywordListKeywordsRequest** | [**ReplaceAdNegativeKeywordListKeywordsRequest**](ReplaceAdNegativeKeywordListKeywordsRequest.md)|  | |

### Return type

[**ReplaceAdNegativeKeywordListKeywords200Response**](ReplaceAdNegativeKeywordListKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## replaceAdNegativeKeywordListKeywordsWithHttpInfo

> ApiResponse<ReplaceAdNegativeKeywordListKeywords200Response> replaceAdNegativeKeywordListKeywords replaceAdNegativeKeywordListKeywordsWithHttpInfo(listId, replaceAdNegativeKeywordListKeywordsRequest)

Replace negative list keywords

Replaces the full desired keyword set. Existing keywords are diffed by normalized text and match type; creates and removals are applied atomically in one mutation. Unchanged criteria retain their ids. Send an empty keywords array to clear the list. Changes affect every campaign using this list. Each create or removal consumes one daily operation; the entire batch must fit the remaining quota.

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
        String listId = "listId_example"; // String | 
        ReplaceAdNegativeKeywordListKeywordsRequest replaceAdNegativeKeywordListKeywordsRequest = new ReplaceAdNegativeKeywordListKeywordsRequest(); // ReplaceAdNegativeKeywordListKeywordsRequest | 
        try {
            ApiResponse<ReplaceAdNegativeKeywordListKeywords200Response> response = apiInstance.replaceAdNegativeKeywordListKeywordsWithHttpInfo(listId, replaceAdNegativeKeywordListKeywordsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#replaceAdNegativeKeywordListKeywords");
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
| **listId** | **String**|  | |
| **replaceAdNegativeKeywordListKeywordsRequest** | [**ReplaceAdNegativeKeywordListKeywordsRequest**](ReplaceAdNegativeKeywordListKeywordsRequest.md)|  | |

### Return type

ApiResponse<[**ReplaceAdNegativeKeywordListKeywords200Response**](ReplaceAdNegativeKeywordListKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


## replyToAdComment

> ReplyToAdComment200Response replyToAdComment(adId, commentId, replyToAdCommentRequest, since, until)

Reply to an ad comment

Reply to a first-level TikTok ad comment. Requires a TT_USER or CUSTOMIZED_USER identity with comment-management permission. Replies to replies are rejected. The response commentId identifies the new reply. This operation is not idempotent; do not blindly retry an uncertain response.  Unknown identity and video item fields are resolved only when needed for this action, then persisted for reuse. Comment-specific fields take precedence. If TikTok no longer returns the ad needed to resolve identity, 404 ad_not_found directs you to check deletion or archival in TikTok Ads Manager. Listing can still succeed. Unsupported or unavailable identity returns 403 feature_not_available. Denied access to ad details returns 403 insufficient_permissions with reconnect guidance and the upstream platformError.  Requires Ads access. The ad is resolved within the caller&#39;s accessible profiles. Before moderation, Zernio verifies that the comment belongs to this ad using TikTok&#39;s ad-group comment listing. The default search window is the last 30 days. Use since/until for older comments, with at most 30 days between the dates. Lookups scan at most 2,000 ad-group comments; narrow the date window if exceeded. Meta returns 501 feature_not_available with guidance to use the existing inbox comment endpoints and the account/post IDs from GET /v1/ads/{adId}/comments. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad ID.
        String commentId = "commentId_example"; // String | TikTok comment ID from the ad comment listing.
        ReplyToAdCommentRequest replyToAdCommentRequest = new ReplyToAdCommentRequest(); // ReplyToAdCommentRequest | 
        LocalDate since = LocalDate.now(); // LocalDate | Start date of the comment lookup window. Defaults to 30 days before until.
        LocalDate until = LocalDate.now(); // LocalDate | End date of the comment lookup window. Defaults to today in UTC.
        try {
            ReplyToAdComment200Response result = apiInstance.replyToAdComment(adId, commentId, replyToAdCommentRequest, since, until);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#replyToAdComment");
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad ID. | |
| **commentId** | **String**| TikTok comment ID from the ad comment listing. | |
| **replyToAdCommentRequest** | [**ReplyToAdCommentRequest**](ReplyToAdCommentRequest.md)|  | |
| **since** | **LocalDate**| Start date of the comment lookup window. Defaults to 30 days before until. | [optional] |
| **until** | **LocalDate**| End date of the comment lookup window. Defaults to today in UTC. | [optional] |

### Return type

[**ReplyToAdComment200Response**](ReplyToAdComment200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment action completed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access or supported identity is unavailable (feature_not_available), or TikTok denies ad-detail access or comment-management permission (insufficient_permissions). Grant permission and reconnect the TikTok Ads account before retrying. |  -  |
| **404** | Ad is inaccessible or unavailable on TikTok for identity resolution (ad_not_found), or the comment was not found on this ad in the selected date window (resource_not_found). |  -  |
| **422** | TikTok Ads connection is unavailable. |  -  |
| **501** | Moderation on this route supports TikTok. Use the inbox comment routes for Meta. |  -  |
| **502** | TikTok rejected the request or was unavailable. Inspect platformError for its code and message. |  -  |

## replyToAdCommentWithHttpInfo

> ApiResponse<ReplyToAdComment200Response> replyToAdComment replyToAdCommentWithHttpInfo(adId, commentId, replyToAdCommentRequest, since, until)

Reply to an ad comment

Reply to a first-level TikTok ad comment. Requires a TT_USER or CUSTOMIZED_USER identity with comment-management permission. Replies to replies are rejected. The response commentId identifies the new reply. This operation is not idempotent; do not blindly retry an uncertain response.  Unknown identity and video item fields are resolved only when needed for this action, then persisted for reuse. Comment-specific fields take precedence. If TikTok no longer returns the ad needed to resolve identity, 404 ad_not_found directs you to check deletion or archival in TikTok Ads Manager. Listing can still succeed. Unsupported or unavailable identity returns 403 feature_not_available. Denied access to ad details returns 403 insufficient_permissions with reconnect guidance and the upstream platformError.  Requires Ads access. The ad is resolved within the caller&#39;s accessible profiles. Before moderation, Zernio verifies that the comment belongs to this ad using TikTok&#39;s ad-group comment listing. The default search window is the last 30 days. Use since/until for older comments, with at most 30 days between the dates. Lookups scan at most 2,000 ad-group comments; narrow the date window if exceeded. Meta returns 501 feature_not_available with guidance to use the existing inbox comment endpoints and the account/post IDs from GET /v1/ads/{adId}/comments. 

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
        String adId = "adId_example"; // String | Internal Zernio ad ID or indexed platform ad ID.
        String commentId = "commentId_example"; // String | TikTok comment ID from the ad comment listing.
        ReplyToAdCommentRequest replyToAdCommentRequest = new ReplyToAdCommentRequest(); // ReplyToAdCommentRequest | 
        LocalDate since = LocalDate.now(); // LocalDate | Start date of the comment lookup window. Defaults to 30 days before until.
        LocalDate until = LocalDate.now(); // LocalDate | End date of the comment lookup window. Defaults to today in UTC.
        try {
            ApiResponse<ReplyToAdComment200Response> response = apiInstance.replyToAdCommentWithHttpInfo(adId, commentId, replyToAdCommentRequest, since, until);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#replyToAdComment");
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
| **adId** | **String**| Internal Zernio ad ID or indexed platform ad ID. | |
| **commentId** | **String**| TikTok comment ID from the ad comment listing. | |
| **replyToAdCommentRequest** | [**ReplyToAdCommentRequest**](ReplyToAdCommentRequest.md)|  | |
| **since** | **LocalDate**| Start date of the comment lookup window. Defaults to 30 days before until. | [optional] |
| **until** | **LocalDate**| End date of the comment lookup window. Defaults to today in UTC. | [optional] |

### Return type

ApiResponse<[**ReplyToAdComment200Response**](ReplyToAdComment200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comment action completed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access or supported identity is unavailable (feature_not_available), or TikTok denies ad-detail access or comment-management permission (insufficient_permissions). Grant permission and reconnect the TikTok Ads account before retrying. |  -  |
| **404** | Ad is inaccessible or unavailable on TikTok for identity resolution (ad_not_found), or the comment was not found on this ad in the selected date window (resource_not_found). |  -  |
| **422** | TikTok Ads connection is unavailable. |  -  |
| **501** | Moderation on this route supports TikTok. Use the inbox comment routes for Meta. |  -  |
| **502** | TikTok rejected the request or was unavailable. Inspect platformError for its code and message. |  -  |


## updateAccountCallouts

> UpdateAccountCallouts200Response updateAccountCallouts(updateAccountCalloutsRequest)

Update account callouts

Edits existing Google assets in place. Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists.

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
        UpdateAccountCalloutsRequest updateAccountCalloutsRequest = new UpdateAccountCalloutsRequest(); // UpdateAccountCalloutsRequest | 
        try {
            UpdateAccountCallouts200Response result = apiInstance.updateAccountCallouts(updateAccountCalloutsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAccountCallouts");
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
| **updateAccountCalloutsRequest** | [**UpdateAccountCalloutsRequest**](UpdateAccountCalloutsRequest.md)|  | |

### Return type

[**UpdateAccountCallouts200Response**](UpdateAccountCallouts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## updateAccountCalloutsWithHttpInfo

> ApiResponse<UpdateAccountCallouts200Response> updateAccountCallouts updateAccountCalloutsWithHttpInfo(updateAccountCalloutsRequest)

Update account callouts

Edits existing Google assets in place. Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists.

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
        UpdateAccountCalloutsRequest updateAccountCalloutsRequest = new UpdateAccountCalloutsRequest(); // UpdateAccountCalloutsRequest | 
        try {
            ApiResponse<UpdateAccountCallouts200Response> response = apiInstance.updateAccountCalloutsWithHttpInfo(updateAccountCalloutsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAccountCallouts");
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
| **updateAccountCalloutsRequest** | [**UpdateAccountCalloutsRequest**](UpdateAccountCalloutsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAccountCallouts200Response**](UpdateAccountCallouts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## updateAccountSitelinks

> UpdateAccountCallouts200Response updateAccountSitelinks(updateAccountSitelinksRequest)

Update account sitelinks

Edits existing Google assets in place. Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists.

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
        UpdateAccountSitelinksRequest updateAccountSitelinksRequest = new UpdateAccountSitelinksRequest(); // UpdateAccountSitelinksRequest | 
        try {
            UpdateAccountCallouts200Response result = apiInstance.updateAccountSitelinks(updateAccountSitelinksRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAccountSitelinks");
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
| **updateAccountSitelinksRequest** | [**UpdateAccountSitelinksRequest**](UpdateAccountSitelinksRequest.md)|  | |

### Return type

[**UpdateAccountCallouts200Response**](UpdateAccountCallouts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## updateAccountSitelinksWithHttpInfo

> ApiResponse<UpdateAccountCallouts200Response> updateAccountSitelinks updateAccountSitelinksWithHttpInfo(updateAccountSitelinksRequest)

Update account sitelinks

Edits existing Google assets in place. Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists.

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
        UpdateAccountSitelinksRequest updateAccountSitelinksRequest = new UpdateAccountSitelinksRequest(); // UpdateAccountSitelinksRequest | 
        try {
            ApiResponse<UpdateAccountCallouts200Response> response = apiInstance.updateAccountSitelinksWithHttpInfo(updateAccountSitelinksRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAccountSitelinks");
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
| **updateAccountSitelinksRequest** | [**UpdateAccountSitelinksRequest**](UpdateAccountSitelinksRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAccountCallouts200Response**](UpdateAccountCallouts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## updateAccountStructuredSnippets

> UpdateAccountCallouts200Response updateAccountStructuredSnippets(updateAccountStructuredSnippetsRequest)

Update account snippets

Edits existing Google assets in place. Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists.

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
        UpdateAccountStructuredSnippetsRequest updateAccountStructuredSnippetsRequest = new UpdateAccountStructuredSnippetsRequest(); // UpdateAccountStructuredSnippetsRequest | 
        try {
            UpdateAccountCallouts200Response result = apiInstance.updateAccountStructuredSnippets(updateAccountStructuredSnippetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAccountStructuredSnippets");
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
| **updateAccountStructuredSnippetsRequest** | [**UpdateAccountStructuredSnippetsRequest**](UpdateAccountStructuredSnippetsRequest.md)|  | |

### Return type

[**UpdateAccountCallouts200Response**](UpdateAccountCallouts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## updateAccountStructuredSnippetsWithHttpInfo

> ApiResponse<UpdateAccountCallouts200Response> updateAccountStructuredSnippets updateAccountStructuredSnippetsWithHttpInfo(updateAccountStructuredSnippetsRequest)

Update account snippets

Edits existing Google assets in place. Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists.

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
        UpdateAccountStructuredSnippetsRequest updateAccountStructuredSnippetsRequest = new UpdateAccountStructuredSnippetsRequest(); // UpdateAccountStructuredSnippetsRequest | 
        try {
            ApiResponse<UpdateAccountCallouts200Response> response = apiInstance.updateAccountStructuredSnippetsWithHttpInfo(updateAccountStructuredSnippetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAccountStructuredSnippets");
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
| **updateAccountStructuredSnippetsRequest** | [**UpdateAccountStructuredSnippetsRequest**](UpdateAccountStructuredSnippetsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAccountCallouts200Response**](UpdateAccountCallouts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access is required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | DSA defaults updated (re-read from Meta after the write) |  -  |
| **400** | Unsupported platform (non-Meta account) or invalid adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |

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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | DSA defaults updated (re-read from Meta after the write) |  -  |
| **400** | Unsupported platform (non-Meta account) or invalid adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |


## updateAdNegativeKeywordList

> UpdateAdNegativeKeywordList200Response updateAdNegativeKeywordList(listId, updateAdNegativeKeywordListRequest)

Rename a negative keyword list

Renames a shared negative keyword list. Keywords and campaign associations are unchanged. Use the keywords endpoint to edit the desired keyword set.

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
        String listId = "listId_example"; // String | 
        UpdateAdNegativeKeywordListRequest updateAdNegativeKeywordListRequest = new UpdateAdNegativeKeywordListRequest(); // UpdateAdNegativeKeywordListRequest | 
        try {
            UpdateAdNegativeKeywordList200Response result = apiInstance.updateAdNegativeKeywordList(listId, updateAdNegativeKeywordListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAdNegativeKeywordList");
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
| **listId** | **String**|  | |
| **updateAdNegativeKeywordListRequest** | [**UpdateAdNegativeKeywordListRequest**](UpdateAdNegativeKeywordListRequest.md)|  | |

### Return type

[**UpdateAdNegativeKeywordList200Response**](UpdateAdNegativeKeywordList200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## updateAdNegativeKeywordListWithHttpInfo

> ApiResponse<UpdateAdNegativeKeywordList200Response> updateAdNegativeKeywordList updateAdNegativeKeywordListWithHttpInfo(listId, updateAdNegativeKeywordListRequest)

Rename a negative keyword list

Renames a shared negative keyword list. Keywords and campaign associations are unchanged. Use the keywords endpoint to edit the desired keyword set.

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
        String listId = "listId_example"; // String | 
        UpdateAdNegativeKeywordListRequest updateAdNegativeKeywordListRequest = new UpdateAdNegativeKeywordListRequest(); // UpdateAdNegativeKeywordListRequest | 
        try {
            ApiResponse<UpdateAdNegativeKeywordList200Response> response = apiInstance.updateAdNegativeKeywordListWithHttpInfo(listId, updateAdNegativeKeywordListRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateAdNegativeKeywordList");
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
| **listId** | **String**|  | |
| **updateAdNegativeKeywordListRequest** | [**UpdateAdNegativeKeywordListRequest**](UpdateAdNegativeKeywordListRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdNegativeKeywordList200Response**](UpdateAdNegativeKeywordList200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access and permission to the selected account are required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


## updateValueRuleSet

> UpdateValueRuleSet200Response updateValueRuleSet(valueRuleSetId, updateValueRuleSetRequest)

Replace a value rule set

**THIS IS A FULL REPLACE, NOT A PATCH.** Meta&#39;s update is declarative: the body you send becomes the rule set.  - &#x60;GET /v1/ads/value-rule-sets/{valueRuleSetId}&#x60; FIRST. - Keep a rule or criterion by echoing its &#x60;id&#x60;. - Create one by including the object WITHOUT an &#x60;id&#x60;. - Delete one by OMITTING it from the array. There is no warning and no undo.  &#x60;name&#x60; and &#x60;rules&#x60; are both required for exactly this reason: a partial body would silently destroy every rule left out.  **Rule order is semantic**: the array order you send is the evaluation order, and only the first matching rule adjusts the bid for an overlapping audience.  Existing rule sets created elsewhere may contain &#x60;LOCATION_DMA&#x60; criteria. Those went inert on 2026-06-22 and are rejected here; migrate them to &#x60;LOCATION_COMSCORE_MARKET&#x60;.

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
        String valueRuleSetId = "valueRuleSetId_example"; // String | Platform value rule set id.
        UpdateValueRuleSetRequest updateValueRuleSetRequest = new UpdateValueRuleSetRequest(); // UpdateValueRuleSetRequest | 
        try {
            UpdateValueRuleSet200Response result = apiInstance.updateValueRuleSet(valueRuleSetId, updateValueRuleSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateValueRuleSet");
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
| **valueRuleSetId** | **String**| Platform value rule set id. | |
| **updateValueRuleSetRequest** | [**UpdateValueRuleSetRequest**](UpdateValueRuleSetRequest.md)|  | |

### Return type

[**UpdateValueRuleSet200Response**](UpdateValueRuleSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule set replaced |  -  |
| **400** | Invalid input, or Meta rejected the update |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## updateValueRuleSetWithHttpInfo

> ApiResponse<UpdateValueRuleSet200Response> updateValueRuleSet updateValueRuleSetWithHttpInfo(valueRuleSetId, updateValueRuleSetRequest)

Replace a value rule set

**THIS IS A FULL REPLACE, NOT A PATCH.** Meta&#39;s update is declarative: the body you send becomes the rule set.  - &#x60;GET /v1/ads/value-rule-sets/{valueRuleSetId}&#x60; FIRST. - Keep a rule or criterion by echoing its &#x60;id&#x60;. - Create one by including the object WITHOUT an &#x60;id&#x60;. - Delete one by OMITTING it from the array. There is no warning and no undo.  &#x60;name&#x60; and &#x60;rules&#x60; are both required for exactly this reason: a partial body would silently destroy every rule left out.  **Rule order is semantic**: the array order you send is the evaluation order, and only the first matching rule adjusts the bid for an overlapping audience.  Existing rule sets created elsewhere may contain &#x60;LOCATION_DMA&#x60; criteria. Those went inert on 2026-06-22 and are rejected here; migrate them to &#x60;LOCATION_COMSCORE_MARKET&#x60;.

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
        String valueRuleSetId = "valueRuleSetId_example"; // String | Platform value rule set id.
        UpdateValueRuleSetRequest updateValueRuleSetRequest = new UpdateValueRuleSetRequest(); // UpdateValueRuleSetRequest | 
        try {
            ApiResponse<UpdateValueRuleSet200Response> response = apiInstance.updateValueRuleSetWithHttpInfo(valueRuleSetId, updateValueRuleSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAccountsApi#updateValueRuleSet");
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
| **valueRuleSetId** | **String**| Platform value rule set id. | |
| **updateValueRuleSetRequest** | [**UpdateValueRuleSetRequest**](UpdateValueRuleSetRequest.md)|  | |

### Return type

ApiResponse<[**UpdateValueRuleSet200Response**](UpdateValueRuleSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Value rule set replaced |  -  |
| **400** | Invalid input, or Meta rejected the update |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

