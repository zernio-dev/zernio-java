# SlackApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSlackMembers**](SlackApi.md#listSlackMembers) | **GET** /v1/accounts/{accountId}/slack-members | List Slack workspace members |
| [**listSlackMembersWithHttpInfo**](SlackApi.md#listSlackMembersWithHttpInfo) | **GET** /v1/accounts/{accountId}/slack-members | List Slack workspace members |



## listSlackMembers

> ListSlackMembers200Response listSlackMembers(accountId, query, limit)

List Slack workspace members

Members of the connected Slack workspace that can receive a direct message, for populating a recipient picker. Bots, deactivated members and Slackbot are excluded. Start a DM by passing a member id as &#x60;participantId&#x60; to POST /v1/inbox/conversations.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SlackApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SlackApi apiInstance = new SlackApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String query = "query_example"; // String | Case-insensitive filter over display name and handle.
        Integer limit = 50; // Integer | 
        try {
            ListSlackMembers200Response result = apiInstance.listSlackMembers(accountId, query, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SlackApi#listSlackMembers");
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
| **query** | **String**| Case-insensitive filter over display name and handle. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**ListSlackMembers200Response**](ListSlackMembers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspace members |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Slack account not found |  -  |

## listSlackMembersWithHttpInfo

> ApiResponse<ListSlackMembers200Response> listSlackMembers listSlackMembersWithHttpInfo(accountId, query, limit)

List Slack workspace members

Members of the connected Slack workspace that can receive a direct message, for populating a recipient picker. Bots, deactivated members and Slackbot are excluded. Start a DM by passing a member id as &#x60;participantId&#x60; to POST /v1/inbox/conversations.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SlackApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SlackApi apiInstance = new SlackApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String query = "query_example"; // String | Case-insensitive filter over display name and handle.
        Integer limit = 50; // Integer | 
        try {
            ApiResponse<ListSlackMembers200Response> response = apiInstance.listSlackMembersWithHttpInfo(accountId, query, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SlackApi#listSlackMembers");
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
| **query** | **String**| Case-insensitive filter over display name and handle. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

ApiResponse<[**ListSlackMembers200Response**](ListSlackMembers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspace members |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Slack account not found |  -  |

