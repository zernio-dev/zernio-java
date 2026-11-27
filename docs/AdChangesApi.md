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
| [**listAdChanges**](AdChangesApi.md#listAdChanges) | **GET** /v1/ads/changes | List staged ad changes |
| [**listAdChangesWithHttpInfo**](AdChangesApi.md#listAdChangesWithHttpInfo) | **GET** /v1/ads/changes | List staged ad changes |
| [**restageAdChange**](AdChangesApi.md#restageAdChange) | **POST** /v1/ads/changes/{changeId}/restage | Stage a failed ad change again |
| [**restageAdChangeWithHttpInfo**](AdChangesApi.md#restageAdChangeWithHttpInfo) | **POST** /v1/ads/changes/{changeId}/restage | Stage a failed ad change again |
| [**updateAdChange**](AdChangesApi.md#updateAdChange) | **PATCH** /v1/ads/changes/{changeId} | Edit or refresh a staged ad change |
| [**updateAdChangeWithHttpInfo**](AdChangesApi.md#updateAdChangeWithHttpInfo) | **PATCH** /v1/ads/changes/{changeId} | Edit or refresh a staged ad change |



## confirmAdChange

> Map<String, Object> confirmAdChange(changeId)

Confirm a staged ad change

Applies a staged change and returns what the direct write returns: the response body of the route the change was staged on.  The caller needs the same access to the object as for the direct write, and the checks of that write run here, including the live ads allowance.  ### Changed since staging  Before writing, the object is read from the ad network again and compared with what it held when the change was staged.  If it changed in between, nothing is written and the answer is &#x60;409&#x60; &#x60;change_target_changed&#x60; with the current values in &#x60;details.current&#x60;. The change stays &#x60;staged&#x60; and reads &#x60;stale: true&#x60;. Refresh it with PATCH /v1/ads/changes/{changeId}, or discard it and stage the change again from those values.  A change of type &#x60;operation&#x60; has no such check: its request is sent through its own route as it was stored.  After a confirm, the other staged changes on the same object are read again, so confirming one of two changes on an object does not refuse the other.  ### Retrying  A change is applied at most once. Confirming a change that is already &#x60;confirmed&#x60; returns its stored result again. A change that failed answers &#x60;409&#x60; &#x60;change_not_staged&#x60;: stage a new one.  A refusal before anything is written leaves the change &#x60;staged&#x60;, so the confirm can be sent again: &#x60;403&#x60; &#x60;ads_allowance_exceeded&#x60;, or on a one-field change a &#x60;429&#x60; from Zernio&#39;s own limits. Any other failed write ends the change as &#x60;failed&#x60;.  ### Creates  A staged create is sent once. The ad network checks at confirm whatever it did not check at staging, and media is fetched here. A create that fails ends as &#x60;failed&#x60; and is not retried: &#x60;error.details&#x60; keeps what the create reported about objects it had already made. 

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
| **409** | The change was not applied. The code says why:  - &#x60;change_target_changed&#x60;: the object changed on the ad network after the change was staged. &#x60;details.current&#x60; carries its current values. - &#x60;change_not_staged&#x60;: the change has already failed. - &#x60;change_outcome_unknown&#x60;: another confirm of this change is running, or one started and never recorded how it ended. Read the change, and check the object on the ad network before staging a new one. - &#x60;change_partly_applied&#x60;: a write on a list was sent and some items failed. The change ends as &#x60;failed&#x60;, and &#x60;details&#x60; holds the result of each item. - &#x60;invalid_resource_state&#x60;: the change was edited while this confirm started. Nothing was sent and it is still staged. Read it and confirm again.  |  -  |

## confirmAdChangeWithHttpInfo

> ApiResponse<Map<String, Object>> confirmAdChange confirmAdChangeWithHttpInfo(changeId)

Confirm a staged ad change

Applies a staged change and returns what the direct write returns: the response body of the route the change was staged on.  The caller needs the same access to the object as for the direct write, and the checks of that write run here, including the live ads allowance.  ### Changed since staging  Before writing, the object is read from the ad network again and compared with what it held when the change was staged.  If it changed in between, nothing is written and the answer is &#x60;409&#x60; &#x60;change_target_changed&#x60; with the current values in &#x60;details.current&#x60;. The change stays &#x60;staged&#x60; and reads &#x60;stale: true&#x60;. Refresh it with PATCH /v1/ads/changes/{changeId}, or discard it and stage the change again from those values.  A change of type &#x60;operation&#x60; has no such check: its request is sent through its own route as it was stored.  After a confirm, the other staged changes on the same object are read again, so confirming one of two changes on an object does not refuse the other.  ### Retrying  A change is applied at most once. Confirming a change that is already &#x60;confirmed&#x60; returns its stored result again. A change that failed answers &#x60;409&#x60; &#x60;change_not_staged&#x60;: stage a new one.  A refusal before anything is written leaves the change &#x60;staged&#x60;, so the confirm can be sent again: &#x60;403&#x60; &#x60;ads_allowance_exceeded&#x60;, or on a one-field change a &#x60;429&#x60; from Zernio&#39;s own limits. Any other failed write ends the change as &#x60;failed&#x60;.  ### Creates  A staged create is sent once. The ad network checks at confirm whatever it did not check at staging, and media is fetched here. A create that fails ends as &#x60;failed&#x60; and is not retried: &#x60;error.details&#x60; keeps what the create reported about objects it had already made. 

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
| **409** | The change was not applied. The code says why:  - &#x60;change_target_changed&#x60;: the object changed on the ad network after the change was staged. &#x60;details.current&#x60; carries its current values. - &#x60;change_not_staged&#x60;: the change has already failed. - &#x60;change_outcome_unknown&#x60;: another confirm of this change is running, or one started and never recorded how it ended. Read the change, and check the object on the ad network before staging a new one. - &#x60;change_partly_applied&#x60;: a write on a list was sent and some items failed. The change ends as &#x60;failed&#x60;, and &#x60;details&#x60; holds the result of each item. - &#x60;invalid_resource_state&#x60;: the change was edited while this confirm started. Nothing was sent and it is still staged. Read it and confirm again.  |  -  |


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

Returns one ad change with its before/after diff. A change is created by sending a supported ad write with &#x60;stage: true&#x60;.  Campaign, ad set and ad edits, status changes and creates stage with a live read and a diff against the current values.  Every other write listed under &#x60;request.operation&#x60; stages as its request. Send &#x60;stage: true&#x60; in its body, or &#x60;?stage&#x3D;true&#x60; on a write without a body. The answer is &#x60;202&#x60; with the change.  A staged change does not expire. A confirmed or failed change stays readable for 7 days, a failed create for 30 days. Disconnecting the connection of a staged change deletes it. 

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

Returns one ad change with its before/after diff. A change is created by sending a supported ad write with &#x60;stage: true&#x60;.  Campaign, ad set and ad edits, status changes and creates stage with a live read and a diff against the current values.  Every other write listed under &#x60;request.operation&#x60; stages as its request. Send &#x60;stage: true&#x60; in its body, or &#x60;?stage&#x3D;true&#x60; on a write without a body. The answer is &#x60;202&#x60; with the change.  A staged change does not expire. A confirmed or failed change stays readable for 7 days, a failed create for 30 days. Disconnecting the connection of a staged change deletes it. 

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


## listAdChanges

> ListAdChanges200Response listAdChanges(status, accountId, platform, type, createdBy, limit, cursor)

List staged ad changes

Lists the ad changes waiting to be confirmed or discarded, newest first. With &#x60;status&#x3D;failed&#x60; it lists the changes a confirm could not apply, each with its error, until they are deleted (7 days, 30 for a failed create). A confirmed change is not listed; read it by id.  Each item is a summary without the diff. Read one change to get its before/after values. 

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
        String status = "staged"; // String | Which changes to list.
        String accountId = "accountId_example"; // String | Only the changes of this connected account.
        String platform = "platform_example"; // String | Only the changes on this ad platform, as the change names it (for example `facebook` or `google`).
        String type = "campaign_status"; // String | Only the changes of this type.
        String createdBy = "createdBy_example"; // String | Only the changes this user staged.
        Integer limit = 50; // Integer | How many changes to return.
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            ListAdChanges200Response result = apiInstance.listAdChanges(status, accountId, platform, type, createdBy, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#listAdChanges");
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
| **status** | **String**| Which changes to list. | [optional] [default to staged] [enum: staged, failed] |
| **accountId** | **String**| Only the changes of this connected account. | [optional] |
| **platform** | **String**| Only the changes on this ad platform, as the change names it (for example &#x60;facebook&#x60; or &#x60;google&#x60;). | [optional] |
| **type** | **String**| Only the changes of this type. | [optional] [enum: campaign_status, ad_set_status, ad_status, campaign_update, ad_set_update, ad_update, campaign_targeting, ad_create, campaign_create, ad_set_create, operation] |
| **createdBy** | **String**| Only the changes this user staged. | [optional] |
| **limit** | **Integer**| How many changes to return. | [optional] [default to 50] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

[**ListAdChanges200Response**](ListAdChanges200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of staged changes |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdChangesWithHttpInfo

> ApiResponse<ListAdChanges200Response> listAdChanges listAdChangesWithHttpInfo(status, accountId, platform, type, createdBy, limit, cursor)

List staged ad changes

Lists the ad changes waiting to be confirmed or discarded, newest first. With &#x60;status&#x3D;failed&#x60; it lists the changes a confirm could not apply, each with its error, until they are deleted (7 days, 30 for a failed create). A confirmed change is not listed; read it by id.  Each item is a summary without the diff. Read one change to get its before/after values. 

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
        String status = "staged"; // String | Which changes to list.
        String accountId = "accountId_example"; // String | Only the changes of this connected account.
        String platform = "platform_example"; // String | Only the changes on this ad platform, as the change names it (for example `facebook` or `google`).
        String type = "campaign_status"; // String | Only the changes of this type.
        String createdBy = "createdBy_example"; // String | Only the changes this user staged.
        Integer limit = 50; // Integer | How many changes to return.
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            ApiResponse<ListAdChanges200Response> response = apiInstance.listAdChangesWithHttpInfo(status, accountId, platform, type, createdBy, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#listAdChanges");
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
| **status** | **String**| Which changes to list. | [optional] [default to staged] [enum: staged, failed] |
| **accountId** | **String**| Only the changes of this connected account. | [optional] |
| **platform** | **String**| Only the changes on this ad platform, as the change names it (for example &#x60;facebook&#x60; or &#x60;google&#x60;). | [optional] |
| **type** | **String**| Only the changes of this type. | [optional] [enum: campaign_status, ad_set_status, ad_status, campaign_update, ad_set_update, ad_update, campaign_targeting, ad_create, campaign_create, ad_set_create, operation] |
| **createdBy** | **String**| Only the changes this user staged. | [optional] |
| **limit** | **Integer**| How many changes to return. | [optional] [default to 50] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

ApiResponse<[**ListAdChanges200Response**](ListAdChanges200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of staged changes |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## restageAdChange

> GetAdChange200Response restageAdChange(changeId)

Stage a failed ad change again

Makes a new staged change from a change that failed at confirm. Nothing is written to the ad network.  The new change holds the same request. It is checked for the calling user, and an edit is read against the current values of its object. The failed change stays readable until it is deleted.  A failed create cannot be staged again (&#x60;409&#x60;): it may have made part of its objects on the ad network, which its &#x60;error.details&#x60; lists. Stage a new create instead. This covers every change with &#x60;creates: true&#x60;.  Also refused with &#x60;409&#x60;: a change that failed as &#x60;change_outcome_unknown&#x60;, and a change whose kept uploads were deleted or moved to an earlier restage. 

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
        String changeId = "changeId_example"; // String | The id of the failed change.
        try {
            GetAdChange200Response result = apiInstance.restageAdChange(changeId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#restageAdChange");
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
| **changeId** | **String**| The id of the failed change. | |

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
| **201** | The new staged change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;. The change did not fail, it creates an object, nobody knows how it ended, or its kept uploads are gone. |  -  |

## restageAdChangeWithHttpInfo

> ApiResponse<GetAdChange200Response> restageAdChange restageAdChangeWithHttpInfo(changeId)

Stage a failed ad change again

Makes a new staged change from a change that failed at confirm. Nothing is written to the ad network.  The new change holds the same request. It is checked for the calling user, and an edit is read against the current values of its object. The failed change stays readable until it is deleted.  A failed create cannot be staged again (&#x60;409&#x60;): it may have made part of its objects on the ad network, which its &#x60;error.details&#x60; lists. Stage a new create instead. This covers every change with &#x60;creates: true&#x60;.  Also refused with &#x60;409&#x60;: a change that failed as &#x60;change_outcome_unknown&#x60;, and a change whose kept uploads were deleted or moved to an earlier restage. 

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
        String changeId = "changeId_example"; // String | The id of the failed change.
        try {
            ApiResponse<GetAdChange200Response> response = apiInstance.restageAdChangeWithHttpInfo(changeId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#restageAdChange");
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
| **changeId** | **String**| The id of the failed change. | |

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
| **201** | The new staged change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;. The change did not fail, it creates an object, nobody knows how it ended, or its kept uploads are gone. |  -  |


## updateAdChange

> GetAdChange200Response updateAdChange(changeId, requestBody)

Edit or refresh a staged ad change

Replaces the request body of a staged change, or reads its object again when no body is sent. The change keeps its id. Nothing is written to the ad network.  ### Edit  Send the new body: the same kind of body as the route the change was staged on, without &#x60;stage&#x60;. It passes the checks of staging again for the calling user. The object is read again, so the diff and the changed-since check start from its current values.  A change of type &#x60;operation&#x60; stores a whole request and cannot be edited in place (&#x60;409&#x60;): discard it and stage the request again.  ### Refresh  Send no body. The object is read again with the body the change already holds. Use it on a change that reads &#x60;stale: true&#x60; after a confirm answered &#x60;409&#x60; &#x60;change_target_changed&#x60;: once refreshed it can be confirmed. 

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
        Map<String, Object> requestBody = {"budget":{"amount":25,"type":"daily"}}; // Map<String, Object> | 
        try {
            GetAdChange200Response result = apiInstance.updateAdChange(changeId, requestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#updateAdChange");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | [optional] |

### Return type

[**GetAdChange200Response**](GetAdChange200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The change as it is now |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **409** | The change is no longer staged (&#x60;change_not_staged&#x60;, or &#x60;change_outcome_unknown&#x60; while a confirm is running), or it is a write staged as its request and a body was sent (&#x60;invalid_resource_state&#x60;). |  -  |

## updateAdChangeWithHttpInfo

> ApiResponse<GetAdChange200Response> updateAdChange updateAdChangeWithHttpInfo(changeId, requestBody)

Edit or refresh a staged ad change

Replaces the request body of a staged change, or reads its object again when no body is sent. The change keeps its id. Nothing is written to the ad network.  ### Edit  Send the new body: the same kind of body as the route the change was staged on, without &#x60;stage&#x60;. It passes the checks of staging again for the calling user. The object is read again, so the diff and the changed-since check start from its current values.  A change of type &#x60;operation&#x60; stores a whole request and cannot be edited in place (&#x60;409&#x60;): discard it and stage the request again.  ### Refresh  Send no body. The object is read again with the body the change already holds. Use it on a change that reads &#x60;stale: true&#x60; after a confirm answered &#x60;409&#x60; &#x60;change_target_changed&#x60;: once refreshed it can be confirmed. 

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
        Map<String, Object> requestBody = {"budget":{"amount":25,"type":"daily"}}; // Map<String, Object> | 
        try {
            ApiResponse<GetAdChange200Response> response = apiInstance.updateAdChangeWithHttpInfo(changeId, requestBody);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdChangesApi#updateAdChange");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | [optional] |

### Return type

ApiResponse<[**GetAdChange200Response**](GetAdChange200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The change as it is now |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (code &#x60;ads_addon_required&#x60;). Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **409** | The change is no longer staged (&#x60;change_not_staged&#x60;, or &#x60;change_outcome_unknown&#x60; while a confirm is running), or it is a write staged as its request and a body was sent (&#x60;invalid_resource_state&#x60;). |  -  |

