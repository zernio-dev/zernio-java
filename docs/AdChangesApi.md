# AdChangesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**confirmAdChange**](AdChangesApi.md#confirmAdChange) | **POST** /v1/ads/changes/{changeId}/confirm | Confirm a staged ad change |
| [**confirmAdChangeWithHttpInfo**](AdChangesApi.md#confirmAdChangeWithHttpInfo) | **POST** /v1/ads/changes/{changeId}/confirm | Confirm a staged ad change |
| [**discardAdChange**](AdChangesApi.md#discardAdChange) | **DELETE** /v1/ads/changes/{changeId} | Discard a staged ad change |
| [**discardAdChangeWithHttpInfo**](AdChangesApi.md#discardAdChangeWithHttpInfo) | **DELETE** /v1/ads/changes/{changeId} | Discard a staged ad change |
| [**getAdChange**](AdChangesApi.md#getAdChange) | **GET** /v1/ads/changes/{changeId} | Get a staged ad change |
| [**getAdChangeWithHttpInfo**](AdChangesApi.md#getAdChangeWithHttpInfo) | **GET** /v1/ads/changes/{changeId} | Get a staged ad change |



## confirmAdChange

> Map<String, Object> confirmAdChange(changeId)

Confirm a staged ad change

Applies a staged change and returns what the direct write returns: the response body of the route the change was staged on.  The caller needs the same access to the object as for the direct write, and the checks of that write run here, including the live ads allowance.  ### Changed since staging  Before writing, the object is read from the ad network again and compared with what it held when the change was staged.  If it changed in between, nothing is written, the change ends as &#x60;failed&#x60; and the answer is &#x60;409&#x60; &#x60;change_target_changed&#x60; with the current values in &#x60;details.current&#x60;. Stage the change again from those values.  ### Retrying  A change is applied at most once. Confirming a change that is already &#x60;confirmed&#x60; returns its stored result again. A change that failed answers &#x60;409&#x60; &#x60;change_not_staged&#x60;: stage a new one.  A refusal before anything is written leaves the change &#x60;staged&#x60;, so the confirm can be sent again: &#x60;403&#x60; &#x60;ads_allowance_exceeded&#x60;, or on a one-field change a &#x60;429&#x60; from Zernio&#39;s own limits. Any other failed write ends the change as &#x60;failed&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdChangesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdChangesApi apiInstance = new AdChangesApi(defaultClient);
        String changeId = "changeId_example"; // String | The id of the staged change.
        try {
            Map<String, Object> result = apiInstance.confirmAdChange(changeId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#confirmAdChange");
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
| **changeId** | **String**| The id of the staged change. | |

### Return type

**Map&lt;String, Object&gt;**


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The change was applied. The body is the response of the staged write, for example the body of PUT /v1/ads/campaigns/{campaignId}/status. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The refusals of the staged write: &#x60;ads_addon_required&#x60;, &#x60;ads_allowance_exceeded&#x60; or &#x60;ad_account_not_selected&#x60;. None of them writes anything, and the change stays &#x60;staged&#x60;. |  -  |
| **404** | Resource not found |  -  |
| **429** | Code &#x60;rate_limited&#x60;. A refusal by Zernio&#39;s own limit (&#x60;details.reason&#x60; on Meta, &#x60;details.budgetScope&#x60; on Google) on a change of one field wrote nothing and leaves the change &#x60;staged&#x60;. Any other &#x60;429&#x60;, including one from the ad network, ends the change as &#x60;failed&#x60;. |  -  |
| **409** | The change was not applied. The code says why:  - &#x60;change_target_changed&#x60;: the object changed on the ad network after the change was staged. &#x60;details.current&#x60; carries its current values. - &#x60;change_not_staged&#x60;: the change has already failed. - &#x60;change_outcome_unknown&#x60;: another confirm of this change is running, or one started and never recorded how it ended. Read the change, and check the object on the ad network before staging a new one.  |  -  |

## confirmAdChangeWithHttpInfo

> ApiResponse<Map<String, Object>> confirmAdChange confirmAdChangeWithHttpInfo(changeId)

Confirm a staged ad change

Applies a staged change and returns what the direct write returns: the response body of the route the change was staged on.  The caller needs the same access to the object as for the direct write, and the checks of that write run here, including the live ads allowance.  ### Changed since staging  Before writing, the object is read from the ad network again and compared with what it held when the change was staged.  If it changed in between, nothing is written, the change ends as &#x60;failed&#x60; and the answer is &#x60;409&#x60; &#x60;change_target_changed&#x60; with the current values in &#x60;details.current&#x60;. Stage the change again from those values.  ### Retrying  A change is applied at most once. Confirming a change that is already &#x60;confirmed&#x60; returns its stored result again. A change that failed answers &#x60;409&#x60; &#x60;change_not_staged&#x60;: stage a new one.  A refusal before anything is written leaves the change &#x60;staged&#x60;, so the confirm can be sent again: &#x60;403&#x60; &#x60;ads_allowance_exceeded&#x60;, or on a one-field change a &#x60;429&#x60; from Zernio&#39;s own limits. Any other failed write ends the change as &#x60;failed&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdChangesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdChangesApi apiInstance = new AdChangesApi(defaultClient);
        String changeId = "changeId_example"; // String | The id of the staged change.
        try {
            ApiResponse<Map<String, Object>> response = apiInstance.confirmAdChangeWithHttpInfo(changeId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#confirmAdChange");
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
| **changeId** | **String**| The id of the staged change. | |

### Return type

ApiResponse<**Map&lt;String, Object&gt;**>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The change was applied. The body is the response of the staged write, for example the body of PUT /v1/ads/campaigns/{campaignId}/status. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | The refusals of the staged write: &#x60;ads_addon_required&#x60;, &#x60;ads_allowance_exceeded&#x60; or &#x60;ad_account_not_selected&#x60;. None of them writes anything, and the change stays &#x60;staged&#x60;. |  -  |
| **404** | Resource not found |  -  |
| **429** | Code &#x60;rate_limited&#x60;. A refusal by Zernio&#39;s own limit (&#x60;details.reason&#x60; on Meta, &#x60;details.budgetScope&#x60; on Google) on a change of one field wrote nothing and leaves the change &#x60;staged&#x60;. Any other &#x60;429&#x60;, including one from the ad network, ends the change as &#x60;failed&#x60;. |  -  |
| **409** | The change was not applied. The code says why:  - &#x60;change_target_changed&#x60;: the object changed on the ad network after the change was staged. &#x60;details.current&#x60; carries its current values. - &#x60;change_not_staged&#x60;: the change has already failed. - &#x60;change_outcome_unknown&#x60;: another confirm of this change is running, or one started and never recorded how it ended. Read the change, and check the object on the ad network before staging a new one.  |  -  |


## discardAdChange

> void discardAdChange(changeId)

Discard a staged ad change

Deletes a change that is still staged. Nothing was written to the ad network, so there is nothing to undo.  A change that was already confirmed or has failed cannot be discarded. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdChangesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdChangesApi apiInstance = new AdChangesApi(defaultClient);
        String changeId = "changeId_example"; // String | The id of the staged change.
        try {
            apiInstance.discardAdChange(changeId);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#discardAdChange");
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
| **changeId** | **String**| The id of the staged change. | |

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
| **204** | Change discarded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **409** | The change is no longer staged: &#x60;change_not_staged&#x60; when it was confirmed or has failed, &#x60;change_outcome_unknown&#x60; while a confirm is running. |  -  |

## discardAdChangeWithHttpInfo

> ApiResponse<Void> discardAdChange discardAdChangeWithHttpInfo(changeId)

Discard a staged ad change

Deletes a change that is still staged. Nothing was written to the ad network, so there is nothing to undo.  A change that was already confirmed or has failed cannot be discarded. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdChangesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdChangesApi apiInstance = new AdChangesApi(defaultClient);
        String changeId = "changeId_example"; // String | The id of the staged change.
        try {
            ApiResponse<Void> response = apiInstance.discardAdChangeWithHttpInfo(changeId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#discardAdChange");
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
| **changeId** | **String**| The id of the staged change. | |

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
| **204** | Change discarded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **409** | The change is no longer staged: &#x60;change_not_staged&#x60; when it was confirmed or has failed, &#x60;change_outcome_unknown&#x60; while a confirm is running. |  -  |


## getAdChange

> GetAdChange200Response getAdChange(changeId)

Get a staged ad change

Returns one ad change with its before/after diff. A change is created by sending a supported ad write with &#x60;stage: true&#x60;.  A staged change does not expire. A confirmed or failed change stays readable for 7 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdChangesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdChangesApi apiInstance = new AdChangesApi(defaultClient);
        String changeId = "changeId_example"; // String | The id of the staged change.
        try {
            GetAdChange200Response result = apiInstance.getAdChange(changeId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#getAdChange");
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
| **changeId** | **String**| The id of the staged change. | |

### Return type

[**GetAdChange200Response**](GetAdChange200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## getAdChangeWithHttpInfo

> ApiResponse<GetAdChange200Response> getAdChange getAdChangeWithHttpInfo(changeId)

Get a staged ad change

Returns one ad change with its before/after diff. A change is created by sending a supported ad write with &#x60;stage: true&#x60;.  A staged change does not expire. A confirmed or failed change stays readable for 7 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdChangesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdChangesApi apiInstance = new AdChangesApi(defaultClient);
        String changeId = "changeId_example"; // String | The id of the staged change.
        try {
            ApiResponse<GetAdChange200Response> response = apiInstance.getAdChangeWithHttpInfo(changeId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#getAdChange");
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
| **changeId** | **String**| The id of the staged change. | |

### Return type

ApiResponse<[**GetAdChange200Response**](GetAdChange200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

