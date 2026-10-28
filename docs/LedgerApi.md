# LedgerApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLedgerBalances**](LedgerApi.md#getLedgerBalances) | **GET** /v1/ledger/balances | Get ledger balances |
| [**getLedgerBalancesWithHttpInfo**](LedgerApi.md#getLedgerBalancesWithHttpInfo) | **GET** /v1/ledger/balances | Get ledger balances |
| [**listLedgerEntries**](LedgerApi.md#listLedgerEntries) | **GET** /v1/ledger/entries | List ledger entries |
| [**listLedgerEntriesWithHttpInfo**](LedgerApi.md#listLedgerEntriesWithHttpInfo) | **GET** /v1/ledger/entries | List ledger entries |



## getLedgerBalances

> GetLedgerBalances200Response getLedgerBalances(scopeType, scopeId, currency)

Get ledger balances

Returns the balance of each bucket (for example accruing, owed, payable) for one ledger scope. A scope owned by another team returns an empty balances object. A profile-scoped key (or a member limited to some profiles) only reads &#x60;campaign&#x60; and &#x60;participant&#x60; scopes of campaigns under its profiles; any other scope returns an empty balances object. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LedgerApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LedgerApi apiInstance = new LedgerApi(defaultClient);
        String scopeType = "scopeType_example"; // String | Scope type, for example participant or campaign.
        String scopeId = "scopeId_example"; // String | Scope identifier.
        String currency = "usd"; // String | Lowercase ISO 4217 currency code.
        try {
            GetLedgerBalances200Response result = apiInstance.getLedgerBalances(scopeType, scopeId, currency);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LedgerApi#getLedgerBalances");
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
| **scopeType** | **String**| Scope type, for example participant or campaign. | |
| **scopeId** | **String**| Scope identifier. | |
| **currency** | **String**| Lowercase ISO 4217 currency code. | [optional] [default to usd] |

### Return type

[**GetLedgerBalances200Response**](GetLedgerBalances200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Balances per bucket in cents |  -  |
| **400** | Invalid request |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## getLedgerBalancesWithHttpInfo

> ApiResponse<GetLedgerBalances200Response> getLedgerBalances getLedgerBalancesWithHttpInfo(scopeType, scopeId, currency)

Get ledger balances

Returns the balance of each bucket (for example accruing, owed, payable) for one ledger scope. A scope owned by another team returns an empty balances object. A profile-scoped key (or a member limited to some profiles) only reads &#x60;campaign&#x60; and &#x60;participant&#x60; scopes of campaigns under its profiles; any other scope returns an empty balances object. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LedgerApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LedgerApi apiInstance = new LedgerApi(defaultClient);
        String scopeType = "scopeType_example"; // String | Scope type, for example participant or campaign.
        String scopeId = "scopeId_example"; // String | Scope identifier.
        String currency = "usd"; // String | Lowercase ISO 4217 currency code.
        try {
            ApiResponse<GetLedgerBalances200Response> response = apiInstance.getLedgerBalancesWithHttpInfo(scopeType, scopeId, currency);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LedgerApi#getLedgerBalances");
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
| **scopeType** | **String**| Scope type, for example participant or campaign. | |
| **scopeId** | **String**| Scope identifier. | |
| **currency** | **String**| Lowercase ISO 4217 currency code. | [optional] [default to usd] |

### Return type

ApiResponse<[**GetLedgerBalances200Response**](GetLedgerBalances200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Balances per bucket in cents |  -  |
| **400** | Invalid request |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## listLedgerEntries

> ListLedgerEntries200Response listLedgerEntries(scopeType, scopeId, kind, referenceType, referenceId, limit, skip)

List ledger entries

Lists ledger entries for your team, newest first. Filter by scope (matches either side of the entry), kind, or the reference that caused the entry. A profile-scoped key (or a member limited to some profiles) only sees entries of campaigns under its profiles and of their participants; operator and platform scopes stay hidden from it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LedgerApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LedgerApi apiInstance = new LedgerApi(defaultClient);
        String scopeType = "scopeType_example"; // String | 
        String scopeId = "scopeId_example"; // String | 
        String kind = "accrual"; // String | 
        String referenceType = "referenceType_example"; // String | 
        String referenceId = "referenceId_example"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListLedgerEntries200Response result = apiInstance.listLedgerEntries(scopeType, scopeId, kind, referenceType, referenceId, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LedgerApi#listLedgerEntries");
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
| **scopeType** | **String**|  | [optional] |
| **scopeId** | **String**|  | [optional] |
| **kind** | **String**|  | [optional] [enum: accrual, approval, hold_release, adjustment, settling, settlement, reversal, topup, transfer, fee] |
| **referenceType** | **String**|  | [optional] |
| **referenceId** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListLedgerEntries200Response**](ListLedgerEntries200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ledger entries |  -  |
| **400** | Invalid request |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## listLedgerEntriesWithHttpInfo

> ApiResponse<ListLedgerEntries200Response> listLedgerEntries listLedgerEntriesWithHttpInfo(scopeType, scopeId, kind, referenceType, referenceId, limit, skip)

List ledger entries

Lists ledger entries for your team, newest first. Filter by scope (matches either side of the entry), kind, or the reference that caused the entry. A profile-scoped key (or a member limited to some profiles) only sees entries of campaigns under its profiles and of their participants; operator and platform scopes stay hidden from it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LedgerApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LedgerApi apiInstance = new LedgerApi(defaultClient);
        String scopeType = "scopeType_example"; // String | 
        String scopeId = "scopeId_example"; // String | 
        String kind = "accrual"; // String | 
        String referenceType = "referenceType_example"; // String | 
        String referenceId = "referenceId_example"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListLedgerEntries200Response> response = apiInstance.listLedgerEntriesWithHttpInfo(scopeType, scopeId, kind, referenceType, referenceId, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LedgerApi#listLedgerEntries");
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
| **scopeType** | **String**|  | [optional] |
| **scopeId** | **String**|  | [optional] |
| **kind** | **String**|  | [optional] [enum: accrual, approval, hold_release, adjustment, settling, settlement, reversal, topup, transfer, fee] |
| **referenceType** | **String**|  | [optional] |
| **referenceId** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListLedgerEntries200Response**](ListLedgerEntries200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ledger entries |  -  |
| **400** | Invalid request |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

