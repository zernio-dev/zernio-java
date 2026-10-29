# AdRulesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdRule**](AdRulesApi.md#createAdRule) | **POST** /v1/ads/rules | Create an ad rule |
| [**createAdRuleWithHttpInfo**](AdRulesApi.md#createAdRuleWithHttpInfo) | **POST** /v1/ads/rules | Create an ad rule |
| [**deleteAdRule**](AdRulesApi.md#deleteAdRule) | **DELETE** /v1/ads/rules/{ruleId} | Delete an ad rule |
| [**deleteAdRuleWithHttpInfo**](AdRulesApi.md#deleteAdRuleWithHttpInfo) | **DELETE** /v1/ads/rules/{ruleId} | Delete an ad rule |
| [**getAdRule**](AdRulesApi.md#getAdRule) | **GET** /v1/ads/rules/{ruleId} | Get an ad rule |
| [**getAdRuleWithHttpInfo**](AdRulesApi.md#getAdRuleWithHttpInfo) | **GET** /v1/ads/rules/{ruleId} | Get an ad rule |
| [**listAdRuleActivity**](AdRulesApi.md#listAdRuleActivity) | **GET** /v1/ads/rules/activity | List every change ad rules made |
| [**listAdRuleActivityWithHttpInfo**](AdRulesApi.md#listAdRuleActivityWithHttpInfo) | **GET** /v1/ads/rules/activity | List every change ad rules made |
| [**listAdRuleRuns**](AdRulesApi.md#listAdRuleRuns) | **GET** /v1/ads/rules/{ruleId}/runs | List an ad rule&#39;s runs |
| [**listAdRuleRunsWithHttpInfo**](AdRulesApi.md#listAdRuleRunsWithHttpInfo) | **GET** /v1/ads/rules/{ruleId}/runs | List an ad rule&#39;s runs |
| [**listAdRules**](AdRulesApi.md#listAdRules) | **GET** /v1/ads/rules | List ad rules |
| [**listAdRulesWithHttpInfo**](AdRulesApi.md#listAdRulesWithHttpInfo) | **GET** /v1/ads/rules | List ad rules |
| [**previewAdRule**](AdRulesApi.md#previewAdRule) | **POST** /v1/ads/rules/{ruleId}/preview | Preview an ad rule |
| [**previewAdRuleWithHttpInfo**](AdRulesApi.md#previewAdRuleWithHttpInfo) | **POST** /v1/ads/rules/{ruleId}/preview | Preview an ad rule |
| [**updateAdRule**](AdRulesApi.md#updateAdRule) | **PATCH** /v1/ads/rules/{ruleId} | Update an ad rule |
| [**updateAdRuleWithHttpInfo**](AdRulesApi.md#updateAdRuleWithHttpInfo) | **PATCH** /v1/ads/rules/{ruleId} | Update an ad rule |



## createAdRule

> CreateAdRule201Response createAdRule(createAdRuleRequest)

Create an ad rule

Creates a rule that checks the campaigns or ad sets of one ad account on a schedule and acts on each one that meets every condition.  Rules support Meta, Google, TikTok, LinkedIn, Pinterest, X and Reddit ads connections. Use &#x60;POST /v1/ads/rules/{ruleId}/preview&#x60; to see what a rule would match before enabling it.  ### Evaluation  Each campaign or ad set is evaluated on its own, over the ad account&#39;s calendar days, from the metrics Zernio syncs.  ### Actions  A rule can notify (the &#x60;ad_rule.triggered&#x60; webhook), and take at most one of:  - &#x60;pause&#x60; - &#x60;activate&#x60; - &#x60;adjust_budget&#x60;  ### Cooldown  After acting on an object, the rule leaves that object alone for &#x60;cooldownMinutes&#x60;. A rule that pauses, activates or adjusts budgets needs a cooldown at least as long as its schedule.  ### How &#x60;activate&#x60; works  &#x60;activate&#x60; only reactivates objects a rule paused, never ones you paused yourself, and only once the cooldown has passed since that pause.  If you reactivate and pause such an object yourself between two runs of a rule, Zernio cannot tell your pause from the rule&#39;s, and an &#x60;activate&#x60; rule may reactivate it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        CreateAdRuleRequest createAdRuleRequest = new CreateAdRuleRequest(); // CreateAdRuleRequest | 
        try {
            CreateAdRule201Response result = apiInstance.createAdRule(createAdRuleRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#createAdRule");
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
| **createAdRuleRequest** | [**CreateAdRuleRequest**](CreateAdRuleRequest.md)|  | |

### Return type

[**CreateAdRule201Response**](CreateAdRule201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Rule created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the team has no ads access (legacy plans need the Ads add-on), &#x60;ad_account_not_selected&#x60; when &#x60;adAccountId&#x60; is not in the connection&#39;s selected ad accounts, or &#x60;ads_allowance_exceeded&#x60; when a rule that reactivates or raises budgets is created for a team past its free live-ads allowance with no payment method. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |

## createAdRuleWithHttpInfo

> ApiResponse<CreateAdRule201Response> createAdRule createAdRuleWithHttpInfo(createAdRuleRequest)

Create an ad rule

Creates a rule that checks the campaigns or ad sets of one ad account on a schedule and acts on each one that meets every condition.  Rules support Meta, Google, TikTok, LinkedIn, Pinterest, X and Reddit ads connections. Use &#x60;POST /v1/ads/rules/{ruleId}/preview&#x60; to see what a rule would match before enabling it.  ### Evaluation  Each campaign or ad set is evaluated on its own, over the ad account&#39;s calendar days, from the metrics Zernio syncs.  ### Actions  A rule can notify (the &#x60;ad_rule.triggered&#x60; webhook), and take at most one of:  - &#x60;pause&#x60; - &#x60;activate&#x60; - &#x60;adjust_budget&#x60;  ### Cooldown  After acting on an object, the rule leaves that object alone for &#x60;cooldownMinutes&#x60;. A rule that pauses, activates or adjusts budgets needs a cooldown at least as long as its schedule.  ### How &#x60;activate&#x60; works  &#x60;activate&#x60; only reactivates objects a rule paused, never ones you paused yourself, and only once the cooldown has passed since that pause.  If you reactivate and pause such an object yourself between two runs of a rule, Zernio cannot tell your pause from the rule&#39;s, and an &#x60;activate&#x60; rule may reactivate it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        CreateAdRuleRequest createAdRuleRequest = new CreateAdRuleRequest(); // CreateAdRuleRequest | 
        try {
            ApiResponse<CreateAdRule201Response> response = apiInstance.createAdRuleWithHttpInfo(createAdRuleRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#createAdRule");
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
| **createAdRuleRequest** | [**CreateAdRuleRequest**](CreateAdRuleRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdRule201Response**](CreateAdRule201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Rule created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the team has no ads access (legacy plans need the Ads add-on), &#x60;ad_account_not_selected&#x60; when &#x60;adAccountId&#x60; is not in the connection&#39;s selected ad accounts, or &#x60;ads_allowance_exceeded&#x60; when a rule that reactivates or raises budgets is created for a team past its free live-ads allowance with no payment method. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |


## deleteAdRule

> UpdateYoutubeDefaultPlaylist200Response deleteAdRule(ruleId)

Delete an ad rule

Deletes a rule and its run history. Changes the rule already made on the platform stay. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteAdRule(ruleId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#deleteAdRule");
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
| **ruleId** | **String**|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## deleteAdRuleWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteAdRule deleteAdRuleWithHttpInfo(ruleId)

Delete an ad rule

Deletes a rule and its run history. Changes the rule already made on the platform stay. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteAdRuleWithHttpInfo(ruleId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#deleteAdRule");
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
| **ruleId** | **String**|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## getAdRule

> CreateAdRule201Response getAdRule(ruleId)

Get an ad rule

Returns one ad rule. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        try {
            CreateAdRule201Response result = apiInstance.getAdRule(ruleId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#getAdRule");
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
| **ruleId** | **String**|  | |

### Return type

[**CreateAdRule201Response**](CreateAdRule201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## getAdRuleWithHttpInfo

> ApiResponse<CreateAdRule201Response> getAdRule getAdRuleWithHttpInfo(ruleId)

Get an ad rule

Returns one ad rule. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        try {
            ApiResponse<CreateAdRule201Response> response = apiInstance.getAdRuleWithHttpInfo(ruleId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#getAdRule");
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
| **ruleId** | **String**|  | |

### Return type

ApiResponse<[**CreateAdRule201Response**](CreateAdRule201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## listAdRuleActivity

> ListAdRuleActivity200Response listAdRuleActivity(ruleId, accountId, type, from, to, limit, cursor)

List every change ad rules made

The permanent record of what your rules did: one entry per pause, reactivation or budget change (including skipped and failed attempts), newest first, across all rules of the profiles the key can reach. Entries stay after a rule is renamed or deleted; &#x60;ruleName&#x60; is the rule&#39;s name when it acted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        String accountId = "accountId_example"; // String | Only changes of rules on this ads connection.
        String type = "pause"; // String | 
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 date-time, inclusive.
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 date-time, inclusive.
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ListAdRuleActivity200Response result = apiInstance.listAdRuleActivity(ruleId, accountId, type, from, to, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#listAdRuleActivity");
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
| **ruleId** | **String**|  | [optional] |
| **accountId** | **String**| Only changes of rules on this ads connection. | [optional] |
| **type** | **String**|  | [optional] [enum: pause, activate, adjust_budget] |
| **from** | **OffsetDateTime**| ISO 8601 date-time, inclusive. | [optional] |
| **to** | **OffsetDateTime**| ISO 8601 date-time, inclusive. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

[**ListAdRuleActivity200Response**](ListAdRuleActivity200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Changes, newest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdRuleActivityWithHttpInfo

> ApiResponse<ListAdRuleActivity200Response> listAdRuleActivity listAdRuleActivityWithHttpInfo(ruleId, accountId, type, from, to, limit, cursor)

List every change ad rules made

The permanent record of what your rules did: one entry per pause, reactivation or budget change (including skipped and failed attempts), newest first, across all rules of the profiles the key can reach. Entries stay after a rule is renamed or deleted; &#x60;ruleName&#x60; is the rule&#39;s name when it acted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        String accountId = "accountId_example"; // String | Only changes of rules on this ads connection.
        String type = "pause"; // String | 
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 date-time, inclusive.
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 date-time, inclusive.
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ApiResponse<ListAdRuleActivity200Response> response = apiInstance.listAdRuleActivityWithHttpInfo(ruleId, accountId, type, from, to, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#listAdRuleActivity");
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
| **ruleId** | **String**|  | [optional] |
| **accountId** | **String**| Only changes of rules on this ads connection. | [optional] |
| **type** | **String**|  | [optional] [enum: pause, activate, adjust_budget] |
| **from** | **OffsetDateTime**| ISO 8601 date-time, inclusive. | [optional] |
| **to** | **OffsetDateTime**| ISO 8601 date-time, inclusive. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdRuleActivity200Response**](ListAdRuleActivity200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Changes, newest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdRuleRuns

> ListAdRuleRuns200Response listAdRuleRuns(ruleId, limit, skip)

List an ad rule&#39;s runs

Lists a rule&#39;s scheduled runs, newest first: what each run evaluated, matched and did. Runs that changed something (or tried to) are kept permanently, also after the rule is deleted; runs that changed nothing are dropped after about 31 days. For every change across all rules, use &#x60;GET /v1/ads/rules/activity&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        Integer limit = 20; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListAdRuleRuns200Response result = apiInstance.listAdRuleRuns(ruleId, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#listAdRuleRuns");
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
| **ruleId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListAdRuleRuns200Response**](ListAdRuleRuns200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Runs |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## listAdRuleRunsWithHttpInfo

> ApiResponse<ListAdRuleRuns200Response> listAdRuleRuns listAdRuleRunsWithHttpInfo(ruleId, limit, skip)

List an ad rule&#39;s runs

Lists a rule&#39;s scheduled runs, newest first: what each run evaluated, matched and did. Runs that changed something (or tried to) are kept permanently, also after the rule is deleted; runs that changed nothing are dropped after about 31 days. For every change across all rules, use &#x60;GET /v1/ads/rules/activity&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        Integer limit = 20; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListAdRuleRuns200Response> response = apiInstance.listAdRuleRunsWithHttpInfo(ruleId, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#listAdRuleRuns");
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
| **ruleId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListAdRuleRuns200Response**](ListAdRuleRuns200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Runs |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## listAdRules

> ListAdRules200Response listAdRules(accountId, adAccountId, limit, skip)

List ad rules

Lists the ad rules on the profiles your key can reach, newest first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String accountId = "accountId_example"; // String | Only rules on this ads connection.
        String adAccountId = "adAccountId_example"; // String | Only rules watching this platform ad account.
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListAdRules200Response result = apiInstance.listAdRules(accountId, adAccountId, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#listAdRules");
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
| **accountId** | **String**| Only rules on this ads connection. | [optional] |
| **adAccountId** | **String**| Only rules watching this platform ad account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListAdRules200Response**](ListAdRules200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdRulesWithHttpInfo

> ApiResponse<ListAdRules200Response> listAdRules listAdRulesWithHttpInfo(accountId, adAccountId, limit, skip)

List ad rules

Lists the ad rules on the profiles your key can reach, newest first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String accountId = "accountId_example"; // String | Only rules on this ads connection.
        String adAccountId = "adAccountId_example"; // String | Only rules watching this platform ad account.
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListAdRules200Response> response = apiInstance.listAdRulesWithHttpInfo(accountId, adAccountId, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#listAdRules");
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
| **accountId** | **String**| Only rules on this ads connection. | [optional] |
| **adAccountId** | **String**| Only rules watching this platform ad account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListAdRules200Response**](ListAdRules200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rules |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## previewAdRule

> AdRuleEvaluation previewAdRule(ruleId)

Preview an ad rule

Evaluates a rule against current metrics and returns what it would match right now, without acting on anything, sending a webhook or starting a cooldown. Works on disabled rules. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        try {
            AdRuleEvaluation result = apiInstance.previewAdRule(ruleId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#previewAdRule");
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
| **ruleId** | **String**|  | |

### Return type

[**AdRuleEvaluation**](AdRuleEvaluation.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Evaluation |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## previewAdRuleWithHttpInfo

> ApiResponse<AdRuleEvaluation> previewAdRule previewAdRuleWithHttpInfo(ruleId)

Preview an ad rule

Evaluates a rule against current metrics and returns what it would match right now, without acting on anything, sending a webhook or starting a cooldown. Works on disabled rules. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        try {
            ApiResponse<AdRuleEvaluation> response = apiInstance.previewAdRuleWithHttpInfo(ruleId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#previewAdRule");
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
| **ruleId** | **String**|  | |

### Return type

ApiResponse<[**AdRuleEvaluation**](AdRuleEvaluation.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Evaluation |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## updateAdRule

> CreateAdRule201Response updateAdRule(ruleId, updateAdRuleRequest)

Update an ad rule

Changes any field of a rule except its connection and ad account. Send &#x60;campaignIds: null&#x60; to check the whole ad account again. Changing the schedule, or enabling a disabled rule, moves the next run; re-sending &#x60;enabled: true&#x60; on an enabled rule does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        UpdateAdRuleRequest updateAdRuleRequest = new UpdateAdRuleRequest(); // UpdateAdRuleRequest | 
        try {
            CreateAdRule201Response result = apiInstance.updateAdRule(ruleId, updateAdRuleRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#updateAdRule");
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
| **ruleId** | **String**|  | |
| **updateAdRuleRequest** | [**UpdateAdRuleRequest**](UpdateAdRuleRequest.md)|  | |

### Return type

[**CreateAdRule201Response**](CreateAdRule201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the team has no ads access, or &#x60;ads_allowance_exceeded&#x60; when the change enables a rule that reactivates or raises budgets for a team past its free live-ads allowance with no payment method. |  -  |
| **404** | Resource not found |  -  |

## updateAdRuleWithHttpInfo

> ApiResponse<CreateAdRule201Response> updateAdRule updateAdRuleWithHttpInfo(ruleId, updateAdRuleRequest)

Update an ad rule

Changes any field of a rule except its connection and ad account. Send &#x60;campaignIds: null&#x60; to check the whole ad account again. Changing the schedule, or enabling a disabled rule, moves the next run; re-sending &#x60;enabled: true&#x60; on an enabled rule does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdRulesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdRulesApi apiInstance = new AdRulesApi(defaultClient);
        String ruleId = "ruleId_example"; // String | 
        UpdateAdRuleRequest updateAdRuleRequest = new UpdateAdRuleRequest(); // UpdateAdRuleRequest | 
        try {
            ApiResponse<CreateAdRule201Response> response = apiInstance.updateAdRuleWithHttpInfo(ruleId, updateAdRuleRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdRulesApi#updateAdRule");
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
| **ruleId** | **String**|  | |
| **updateAdRuleRequest** | [**UpdateAdRuleRequest**](UpdateAdRuleRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdRule201Response**](CreateAdRule201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rule updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the team has no ads access, or &#x60;ads_allowance_exceeded&#x60; when the change enables a rule that reactivates or raises budgets for a team past its free live-ads allowance with no payment method. |  -  |
| **404** | Resource not found |  -  |

