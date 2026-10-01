# ChangelogApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listChangelog**](ChangelogApi.md#listChangelog) | **GET** /v1/changelog | List API changelog entries |
| [**listChangelogWithHttpInfo**](ChangelogApi.md#listChangelogWithHttpInfo) | **GET** /v1/changelog | List API changelog entries |



## listChangelog

> ListChangelog200Response listChangelog(type, platform, before, limit)

List API changelog entries

The API changelog, newest first. Each entry is what the &#x60;api.changelog.published&#x60; webhook delivered: the announcement in &#x60;message&#x60;, and in &#x60;changes&#x60; the deterministic diff of the OpenAPI spec (operations and schemas added, removed and modified) for automation to act on. Page with &#x60;before&#x60; set to the previous page&#39;s &#x60;nextCursor&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ChangelogApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ChangelogApi apiInstance = new ChangelogApi(defaultClient);
        String type = "new_feature"; // String | Only entries of this type.
        String platform = "whatsapp"; // String | Only entries tagged with this platform or area slug (see `platforms` on the entry). One slug per request.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Only entries published strictly before this instant. Pass the previous page's `nextCursor`.
        Integer limit = 20; // Integer | 
        try {
            ListChangelog200Response result = apiInstance.listChangelog(type, platform, before, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ChangelogApi#listChangelog");
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
| **type** | **String**| Only entries of this type. | [optional] [enum: new_feature, breaking_change, improvement, deprecation, minor] |
| **platform** | **String**| Only entries tagged with this platform or area slug (see &#x60;platforms&#x60; on the entry). One slug per request. | [optional] |
| **before** | **OffsetDateTime**| Only entries published strictly before this instant. Pass the previous page&#39;s &#x60;nextCursor&#x60;. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**ListChangelog200Response**](ListChangelog200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Changelog entries |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## listChangelogWithHttpInfo

> ApiResponse<ListChangelog200Response> listChangelog listChangelogWithHttpInfo(type, platform, before, limit)

List API changelog entries

The API changelog, newest first. Each entry is what the &#x60;api.changelog.published&#x60; webhook delivered: the announcement in &#x60;message&#x60;, and in &#x60;changes&#x60; the deterministic diff of the OpenAPI spec (operations and schemas added, removed and modified) for automation to act on. Page with &#x60;before&#x60; set to the previous page&#39;s &#x60;nextCursor&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ChangelogApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ChangelogApi apiInstance = new ChangelogApi(defaultClient);
        String type = "new_feature"; // String | Only entries of this type.
        String platform = "whatsapp"; // String | Only entries tagged with this platform or area slug (see `platforms` on the entry). One slug per request.
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Only entries published strictly before this instant. Pass the previous page's `nextCursor`.
        Integer limit = 20; // Integer | 
        try {
            ApiResponse<ListChangelog200Response> response = apiInstance.listChangelogWithHttpInfo(type, platform, before, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ChangelogApi#listChangelog");
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
| **type** | **String**| Only entries of this type. | [optional] [enum: new_feature, breaking_change, improvement, deprecation, minor] |
| **platform** | **String**| Only entries tagged with this platform or area slug (see &#x60;platforms&#x60; on the entry). One slug per request. | [optional] |
| **before** | **OffsetDateTime**| Only entries published strictly before this instant. Pass the previous page&#39;s &#x60;nextCursor&#x60;. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

ApiResponse<[**ListChangelog200Response**](ListChangelog200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Changelog entries |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

