# MentionsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listInboxMentions**](MentionsApi.md#listInboxMentions) | **GET** /v1/inbox/mentions | List mentions |
| [**listInboxMentionsWithHttpInfo**](MentionsApi.md#listInboxMentionsWithHttpInfo) | **GET** /v1/inbox/mentions | List mentions |



## listInboxMentions

> ListInboxMentions200Response listInboxMentions(accountId, profileId, sortOrder, limit, cursor)

List mentions

Returns mentions of your connected organization accounts, delivered via platform webhooks. Currently supports LinkedIn organization mentions.  Requires Inbox addon. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MentionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MentionsApi apiInstance = new MentionsApi(defaultClient);
        String accountId = "accountId_example"; // String | Filter by social account ID
        String profileId = "profileId_example"; // String | Filter by profile ID
        String sortOrder = "asc"; // String | Sort order by publishedAt
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | Cursor for pagination (ID of the last item from the previous page)
        try {
            ListInboxMentions200Response result = apiInstance.listInboxMentions(accountId, profileId, sortOrder, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MentionsApi#listInboxMentions");
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
| **accountId** | **String**| Filter by social account ID | [optional] |
| **profileId** | **String**| Filter by profile ID | [optional] |
| **sortOrder** | **String**| Sort order by publishedAt | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| Cursor for pagination (ID of the last item from the previous page) | [optional] |

### Return type

[**ListInboxMentions200Response**](ListInboxMentions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of mentions |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## listInboxMentionsWithHttpInfo

> ApiResponse<ListInboxMentions200Response> listInboxMentions listInboxMentionsWithHttpInfo(accountId, profileId, sortOrder, limit, cursor)

List mentions

Returns mentions of your connected organization accounts, delivered via platform webhooks. Currently supports LinkedIn organization mentions.  Requires Inbox addon. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MentionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MentionsApi apiInstance = new MentionsApi(defaultClient);
        String accountId = "accountId_example"; // String | Filter by social account ID
        String profileId = "profileId_example"; // String | Filter by profile ID
        String sortOrder = "asc"; // String | Sort order by publishedAt
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | Cursor for pagination (ID of the last item from the previous page)
        try {
            ApiResponse<ListInboxMentions200Response> response = apiInstance.listInboxMentionsWithHttpInfo(accountId, profileId, sortOrder, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MentionsApi#listInboxMentions");
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
| **accountId** | **String**| Filter by social account ID | [optional] |
| **profileId** | **String**| Filter by profile ID | [optional] |
| **sortOrder** | **String**| Sort order by publishedAt | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| Cursor for pagination (ID of the last item from the previous page) | [optional] |

### Return type

ApiResponse<[**ListInboxMentions200Response**](ListInboxMentions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of mentions |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

