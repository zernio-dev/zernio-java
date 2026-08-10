# AdAccountsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomConversion**](AdAccountsApi.md#createCustomConversion) | **POST** /v1/accounts/{accountId}/custom-conversions | Create or reuse a custom conversion |
| [**createCustomConversionWithHttpInfo**](AdAccountsApi.md#createCustomConversionWithHttpInfo) | **POST** /v1/accounts/{accountId}/custom-conversions | Create or reuse a custom conversion |
| [**createHighDemandPeriod**](AdAccountsApi.md#createHighDemandPeriod) | **POST** /v1/ads/high-demand-periods | Schedule a budget increase |
| [**createHighDemandPeriodWithHttpInfo**](AdAccountsApi.md#createHighDemandPeriodWithHttpInfo) | **POST** /v1/ads/high-demand-periods | Schedule a budget increase |
| [**createValueRuleSet**](AdAccountsApi.md#createValueRuleSet) | **POST** /v1/ads/value-rule-sets | Create a value rule set |
| [**createValueRuleSetWithHttpInfo**](AdAccountsApi.md#createValueRuleSetWithHttpInfo) | **POST** /v1/ads/value-rule-sets | Create a value rule set |
| [**deleteValueRuleSet**](AdAccountsApi.md#deleteValueRuleSet) | **DELETE** /v1/ads/value-rule-sets/{valueRuleSetId} | Delete a value rule set |
| [**deleteValueRuleSetWithHttpInfo**](AdAccountsApi.md#deleteValueRuleSetWithHttpInfo) | **DELETE** /v1/ads/value-rule-sets/{valueRuleSetId} | Delete a value rule set |
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
| [**getValueRuleSet**](AdAccountsApi.md#getValueRuleSet) | **GET** /v1/ads/value-rule-sets/{valueRuleSetId} | Read a value rule set |
| [**getValueRuleSetWithHttpInfo**](AdAccountsApi.md#getValueRuleSetWithHttpInfo) | **GET** /v1/ads/value-rule-sets/{valueRuleSetId} | Read a value rule set |
| [**listAdAccounts**](AdAccountsApi.md#listAdAccounts) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdAccountsWithHttpInfo**](AdAccountsApi.md#listAdAccountsWithHttpInfo) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdLabels**](AdAccountsApi.md#listAdLabels) | **GET** /v1/ads/labels | Ad labels |
| [**listAdLabelsWithHttpInfo**](AdAccountsApi.md#listAdLabelsWithHttpInfo) | **GET** /v1/ads/labels | Ad labels |
| [**listAdStudies**](AdAccountsApi.md#listAdStudies) | **GET** /v1/ads/studies | A/B tests and lift studies |
| [**listAdStudiesWithHttpInfo**](AdAccountsApi.md#listAdStudiesWithHttpInfo) | **GET** /v1/ads/studies | A/B tests and lift studies |
| [**listAdsBusinessCenters**](AdAccountsApi.md#listAdsBusinessCenters) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listAdsBusinessCentersWithHttpInfo**](AdAccountsApi.md#listAdsBusinessCentersWithHttpInfo) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listCustomConversions**](AdAccountsApi.md#listCustomConversions) | **GET** /v1/accounts/{accountId}/custom-conversions | List custom conversions |
| [**listCustomConversionsWithHttpInfo**](AdAccountsApi.md#listCustomConversionsWithHttpInfo) | **GET** /v1/accounts/{accountId}/custom-conversions | List custom conversions |
| [**listHighDemandPeriods**](AdAccountsApi.md#listHighDemandPeriods) | **GET** /v1/ads/high-demand-periods | High demand periods / budget schedules |
| [**listHighDemandPeriodsWithHttpInfo**](AdAccountsApi.md#listHighDemandPeriodsWithHttpInfo) | **GET** /v1/ads/high-demand-periods | High demand periods / budget schedules |
| [**listMetaBusinesses**](AdAccountsApi.md#listMetaBusinesses) | **GET** /v1/ads/businesses | Businesses list |
| [**listMetaBusinessesWithHttpInfo**](AdAccountsApi.md#listMetaBusinessesWithHttpInfo) | **GET** /v1/ads/businesses | Businesses list |
| [**listValueRuleSets**](AdAccountsApi.md#listValueRuleSets) | **GET** /v1/ads/value-rule-sets | List value rule sets |
| [**listValueRuleSetsWithHttpInfo**](AdAccountsApi.md#listValueRuleSetsWithHttpInfo) | **GET** /v1/ads/value-rule-sets | List value rule sets |
| [**updateAdAccount**](AdAccountsApi.md#updateAdAccount) | **PATCH** /v1/ads/accounts | Update ad account settings |
| [**updateAdAccountWithHttpInfo**](AdAccountsApi.md#updateAdAccountWithHttpInfo) | **PATCH** /v1/ads/accounts | Update ad account settings |
| [**updateValueRuleSet**](AdAccountsApi.md#updateValueRuleSet) | **PUT** /v1/ads/value-rule-sets/{valueRuleSetId} | Replace a value rule set |
| [**updateValueRuleSetWithHttpInfo**](AdAccountsApi.md#updateValueRuleSetWithHttpInfo) | **PUT** /v1/ads/value-rule-sets/{valueRuleSetId} | Replace a value rule set |



## createCustomConversion

> CustomConversionResult createCustomConversion(accountId, createCustomConversionRequest)

Create or reuse a custom conversion

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
| **200** | An existing custom conversion was reused |  -  |
| **201** | Custom conversion created |  -  |
| **400** | Invalid input, or Meta rejected the conversion (bad rule, per-account cap reached) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the token lacks the ads permissions. |  -  |

## createCustomConversionWithHttpInfo

> ApiResponse<CustomConversionResult> createCustomConversion createCustomConversionWithHttpInfo(accountId, createCustomConversionRequest)

Create or reuse a custom conversion

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
| **200** | An existing custom conversion was reused |  -  |
| **201** | Custom conversion created |  -  |
| **400** | Invalid input, or Meta rejected the conversion (bad rule, per-account cap reached) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the token lacks the ads permissions. |  -  |


## createHighDemandPeriod

> CreateHighDemandPeriod201Response createHighDemandPeriod(createHighDemandPeriodRequest)

Schedule a budget increase

Pre-schedule a temporary budget increase (Black Friday, a launch, a sale) instead of editing the budget by hand on the day. Same target rule as the GET: exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60;.  Two Meta constraints worth knowing before you call it. &#x60;timeStart&#x60; / &#x60;timeEnd&#x60; must fall on a 15-minute boundary, and a campaign cannot mix &#x60;ABSOLUTE&#x60; and &#x60;MULTIPLIER&#x60; across its schedules — the second type is rejected with \&quot;Can&#39;t mix your budget scaling selection\&quot;. Window rules (must sit inside the campaign&#39;s run dates, minimum lead time, no overlap) are Meta&#39;s and its message is forwarded verbatim.

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
| **201** | Budget schedule created |  -  |
| **400** | Invalid input, or Meta rejected the schedule |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createHighDemandPeriodWithHttpInfo

> ApiResponse<CreateHighDemandPeriod201Response> createHighDemandPeriod createHighDemandPeriodWithHttpInfo(createHighDemandPeriodRequest)

Schedule a budget increase

Pre-schedule a temporary budget increase (Black Friday, a launch, a sale) instead of editing the budget by hand on the day. Same target rule as the GET: exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60;.  Two Meta constraints worth knowing before you call it. &#x60;timeStart&#x60; / &#x60;timeEnd&#x60; must fall on a 15-minute boundary, and a campaign cannot mix &#x60;ABSOLUTE&#x60; and &#x60;MULTIPLIER&#x60; across its schedules — the second type is rejected with \&quot;Can&#39;t mix your budget scaling selection\&quot;. Window rules (must sit inside the campaign&#39;s run dates, minimum lead time, no overlap) are Meta&#39;s and its message is forwarded verbatim.

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
| **201** | Value rule set created |  -  |
| **400** | Invalid input, or Meta rejected the create (per-account rule-set cap, ineligible criteria, or an account that is not enabled for value rules) |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


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
| **200** | Value rule set |  -  |
| **400** | Invalid input, or Meta rejected the read. A bad id comes back as GraphMethodException code 100 / subcode 33, which cannot be told apart from a permission problem. |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdAccounts

> ListAdAccounts200Response listAdAccounts(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given social account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs).  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry.  For Google Ads: responds &#x60;429&#x60; when Google&#39;s API quota is temporarily exhausted (instead of an empty list). Retry after a delay. 

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
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## listAdAccountsWithHttpInfo

> ApiResponse<ListAdAccounts200Response> listAdAccounts listAdAccountsWithHttpInfo(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given social account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs).  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry.  For Google Ads: responds &#x60;429&#x60; when Google&#39;s API quota is temporarily exhausted (instead of an empty list). Retry after a delay. 

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
| **400** | Invalid request |  -  |
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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | TikTok account not found |  -  |
| **422** | TikTok Ads not connected |  -  |


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
| **200** | Custom conversions |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required, or the token lacks the ads permissions. |  -  |


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
| **200** | Value rule sets |  -  |
| **400** | Invalid input, or Meta rejected the query. Meta answers a bad rule-set id with GraphMethodException code 100 / subcode 33, which is indistinguishable between not-found, no-permission, and account-not-enabled. |  -  |
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
| **200** | Value rule set replaced |  -  |
| **400** | Invalid input, or Meta rejected the update |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

