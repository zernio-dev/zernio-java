# MentionsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listInboxMentions**](MentionsApi.md#listInboxMentions) | **GET** /v1/inbox/mentions | List mentions |
| [**listInboxMentionsWithHttpInfo**](MentionsApi.md#listInboxMentionsWithHttpInfo) | **GET** /v1/inbox/mentions | List mentions |
| [**replyToMention**](MentionsApi.md#replyToMention) | **POST** /v1/inbox/mentions/reply | Reply to a mention |
| [**replyToMentionWithHttpInfo**](MentionsApi.md#replyToMentionWithHttpInfo) | **POST** /v1/inbox/mentions/reply | Reply to a mention |



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


## replyToMention

> ReplyToMention200Response replyToMention(replyToMentionRequest)

Reply to a mention

Reply to a mention of the connected account. Supported on Instagram only.  Two shapes, selected by whether &#x60;commentId&#x60; is present:  - **Comment mention** (someone @mentioned the account inside a comment): pass both   &#x60;mediaId&#x60; and &#x60;commentId&#x60;. Instagram posts a reply under that comment. - **Caption mention** (someone @mentioned the account in their media caption, so no   comment exists): pass &#x60;mediaId&#x60; only. Instagram posts a comment on their media.  Story mentions are not supported by Instagram&#39;s API.  Note that &#x60;GET /v1/inbox/mentions&#x60; currently returns LinkedIn mentions only and does not surface Instagram mentions. Source &#x60;mediaId&#x60; and &#x60;commentId&#x60; from Instagram&#39;s &#x60;comments&#x60; webhook, which is where mention notifications are delivered for accounts connected through Instagram Login. 

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
        ReplyToMentionRequest replyToMentionRequest = new ReplyToMentionRequest(); // ReplyToMentionRequest | 
        try {
            ReplyToMention200Response result = apiInstance.replyToMention(replyToMentionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MentionsApi#replyToMention");
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
| **replyToMentionRequest** | [**ReplyToMentionRequest**](ReplyToMentionRequest.md)|  | |

### Return type

[**ReplyToMention200Response**](ReplyToMention200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reply posted |  -  |
| **400** | Platform does not support replying to mentions (code: platform_not_supported), or missing mediaId/message. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram was unreachable or returned an unclassified error. Instagram 4xx statuses are forwarded as-is. |  -  |

## replyToMentionWithHttpInfo

> ApiResponse<ReplyToMention200Response> replyToMention replyToMentionWithHttpInfo(replyToMentionRequest)

Reply to a mention

Reply to a mention of the connected account. Supported on Instagram only.  Two shapes, selected by whether &#x60;commentId&#x60; is present:  - **Comment mention** (someone @mentioned the account inside a comment): pass both   &#x60;mediaId&#x60; and &#x60;commentId&#x60;. Instagram posts a reply under that comment. - **Caption mention** (someone @mentioned the account in their media caption, so no   comment exists): pass &#x60;mediaId&#x60; only. Instagram posts a comment on their media.  Story mentions are not supported by Instagram&#39;s API.  Note that &#x60;GET /v1/inbox/mentions&#x60; currently returns LinkedIn mentions only and does not surface Instagram mentions. Source &#x60;mediaId&#x60; and &#x60;commentId&#x60; from Instagram&#39;s &#x60;comments&#x60; webhook, which is where mention notifications are delivered for accounts connected through Instagram Login. 

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
        ReplyToMentionRequest replyToMentionRequest = new ReplyToMentionRequest(); // ReplyToMentionRequest | 
        try {
            ApiResponse<ReplyToMention200Response> response = apiInstance.replyToMentionWithHttpInfo(replyToMentionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MentionsApi#replyToMention");
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
| **replyToMentionRequest** | [**ReplyToMentionRequest**](ReplyToMentionRequest.md)|  | |

### Return type

ApiResponse<[**ReplyToMention200Response**](ReplyToMention200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reply posted |  -  |
| **400** | Platform does not support replying to mentions (code: platform_not_supported), or missing mediaId/message. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account not found |  -  |
| **502** | Instagram was unreachable or returned an unclassified error. Instagram 4xx statuses are forwarded as-is. |  -  |

