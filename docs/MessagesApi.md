# MessagesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMessageReaction**](MessagesApi.md#addMessageReaction) | **POST** /v1/inbox/conversations/{conversationId}/messages/{messageId}/reactions | Add reaction |
| [**addMessageReactionWithHttpInfo**](MessagesApi.md#addMessageReactionWithHttpInfo) | **POST** /v1/inbox/conversations/{conversationId}/messages/{messageId}/reactions | Add reaction |
| [**deleteInboxMessage**](MessagesApi.md#deleteInboxMessage) | **DELETE** /v1/inbox/conversations/{conversationId}/messages/{messageId} | Delete message |
| [**deleteInboxMessageWithHttpInfo**](MessagesApi.md#deleteInboxMessageWithHttpInfo) | **DELETE** /v1/inbox/conversations/{conversationId}/messages/{messageId} | Delete message |
| [**editInboxMessage**](MessagesApi.md#editInboxMessage) | **PATCH** /v1/inbox/conversations/{conversationId}/messages/{messageId} | Edit message |
| [**editInboxMessageWithHttpInfo**](MessagesApi.md#editInboxMessageWithHttpInfo) | **PATCH** /v1/inbox/conversations/{conversationId}/messages/{messageId} | Edit message |
| [**getInboxConversation**](MessagesApi.md#getInboxConversation) | **GET** /v1/inbox/conversations/{conversationId} | Get conversation |
| [**getInboxConversationWithHttpInfo**](MessagesApi.md#getInboxConversationWithHttpInfo) | **GET** /v1/inbox/conversations/{conversationId} | Get conversation |
| [**getInboxConversationMessages**](MessagesApi.md#getInboxConversationMessages) | **GET** /v1/inbox/conversations/{conversationId}/messages | List messages |
| [**getInboxConversationMessagesWithHttpInfo**](MessagesApi.md#getInboxConversationMessagesWithHttpInfo) | **GET** /v1/inbox/conversations/{conversationId}/messages | List messages |
| [**listInboxConversations**](MessagesApi.md#listInboxConversations) | **GET** /v1/inbox/conversations | List conversations |
| [**listInboxConversationsWithHttpInfo**](MessagesApi.md#listInboxConversationsWithHttpInfo) | **GET** /v1/inbox/conversations | List conversations |
| [**removeMessageReaction**](MessagesApi.md#removeMessageReaction) | **DELETE** /v1/inbox/conversations/{conversationId}/messages/{messageId}/reactions | Remove reaction |
| [**removeMessageReactionWithHttpInfo**](MessagesApi.md#removeMessageReactionWithHttpInfo) | **DELETE** /v1/inbox/conversations/{conversationId}/messages/{messageId}/reactions | Remove reaction |
| [**sendInboxMessage**](MessagesApi.md#sendInboxMessage) | **POST** /v1/inbox/conversations/{conversationId}/messages | Send message |
| [**sendInboxMessageWithHttpInfo**](MessagesApi.md#sendInboxMessageWithHttpInfo) | **POST** /v1/inbox/conversations/{conversationId}/messages | Send message |
| [**sendTypingIndicator**](MessagesApi.md#sendTypingIndicator) | **POST** /v1/inbox/conversations/{conversationId}/typing | Send typing indicator |
| [**sendTypingIndicatorWithHttpInfo**](MessagesApi.md#sendTypingIndicatorWithHttpInfo) | **POST** /v1/inbox/conversations/{conversationId}/typing | Send typing indicator |
| [**updateInboxConversation**](MessagesApi.md#updateInboxConversation) | **PUT** /v1/inbox/conversations/{conversationId} | Update conversation status |
| [**updateInboxConversationWithHttpInfo**](MessagesApi.md#updateInboxConversationWithHttpInfo) | **PUT** /v1/inbox/conversations/{conversationId} | Update conversation status |
| [**uploadMediaDirect**](MessagesApi.md#uploadMediaDirect) | **POST** /v1/media/upload-direct | Upload media file |
| [**uploadMediaDirectWithHttpInfo**](MessagesApi.md#uploadMediaDirectWithHttpInfo) | **POST** /v1/media/upload-direct | Upload media file |



## addMessageReaction

> UpdateRedditSubreddits200Response addMessageReaction(conversationId, messageId, addMessageReactionRequest)

Add reaction

Add an emoji reaction to a message. Platform support: - **Telegram**: Supports a subset of Unicode emoji reactions - **WhatsApp**: Supports any standard emoji (one reaction per message per sender) - **All others**: Returns 400 (not supported) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The platform message ID to react to
        AddMessageReactionRequest addMessageReactionRequest = new AddMessageReactionRequest(); // AddMessageReactionRequest | 
        try {
            UpdateRedditSubreddits200Response result = apiInstance.addMessageReaction(conversationId, messageId, addMessageReactionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#addMessageReaction");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The platform message ID to react to | |
| **addMessageReactionRequest** | [**AddMessageReactionRequest**](AddMessageReactionRequest.md)|  | |

### Return type

[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reaction added |  -  |
| **400** | Platform does not support reactions or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |

## addMessageReactionWithHttpInfo

> ApiResponse<UpdateRedditSubreddits200Response> addMessageReaction addMessageReactionWithHttpInfo(conversationId, messageId, addMessageReactionRequest)

Add reaction

Add an emoji reaction to a message. Platform support: - **Telegram**: Supports a subset of Unicode emoji reactions - **WhatsApp**: Supports any standard emoji (one reaction per message per sender) - **All others**: Returns 400 (not supported) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The platform message ID to react to
        AddMessageReactionRequest addMessageReactionRequest = new AddMessageReactionRequest(); // AddMessageReactionRequest | 
        try {
            ApiResponse<UpdateRedditSubreddits200Response> response = apiInstance.addMessageReactionWithHttpInfo(conversationId, messageId, addMessageReactionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#addMessageReaction");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The platform message ID to react to | |
| **addMessageReactionRequest** | [**AddMessageReactionRequest**](AddMessageReactionRequest.md)|  | |

### Return type

ApiResponse<[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reaction added |  -  |
| **400** | Platform does not support reactions or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |


## deleteInboxMessage

> UpdateRedditSubreddits200Response deleteInboxMessage(conversationId, messageId, accountId)

Delete message

Delete a message from a conversation. Platform support varies: - **Telegram**: Full delete (bot&#39;s own messages anytime, others if admin) - **X/Twitter**: Full delete (own DM events only) - **Bluesky**: Delete for self only (recipient still sees it) - **Reddit**: Delete from sender&#39;s view only - **Facebook, Instagram, WhatsApp**: Not supported (returns 400) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The platform message ID to delete
        String accountId = "accountId_example"; // String | Social account ID
        try {
            UpdateRedditSubreddits200Response result = apiInstance.deleteInboxMessage(conversationId, messageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#deleteInboxMessage");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The platform message ID to delete | |
| **accountId** | **String**| Social account ID | |

### Return type

[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message deleted |  -  |
| **400** | Platform does not support deletion or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |

## deleteInboxMessageWithHttpInfo

> ApiResponse<UpdateRedditSubreddits200Response> deleteInboxMessage deleteInboxMessageWithHttpInfo(conversationId, messageId, accountId)

Delete message

Delete a message from a conversation. Platform support varies: - **Telegram**: Full delete (bot&#39;s own messages anytime, others if admin) - **X/Twitter**: Full delete (own DM events only) - **Bluesky**: Delete for self only (recipient still sees it) - **Reddit**: Delete from sender&#39;s view only - **Facebook, Instagram, WhatsApp**: Not supported (returns 400) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The platform message ID to delete
        String accountId = "accountId_example"; // String | Social account ID
        try {
            ApiResponse<UpdateRedditSubreddits200Response> response = apiInstance.deleteInboxMessageWithHttpInfo(conversationId, messageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#deleteInboxMessage");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The platform message ID to delete | |
| **accountId** | **String**| Social account ID | |

### Return type

ApiResponse<[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message deleted |  -  |
| **400** | Platform does not support deletion or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |


## editInboxMessage

> EditInboxMessage200Response editInboxMessage(conversationId, messageId, editInboxMessageRequest)

Edit message

Edit the text and/or reply markup of a previously sent Telegram message. Only supported for Telegram. Returns 400 for other platforms. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The Telegram message ID to edit
        EditInboxMessageRequest editInboxMessageRequest = new EditInboxMessageRequest(); // EditInboxMessageRequest | 
        try {
            EditInboxMessage200Response result = apiInstance.editInboxMessage(conversationId, messageId, editInboxMessageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#editInboxMessage");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The Telegram message ID to edit | |
| **editInboxMessageRequest** | [**EditInboxMessageRequest**](EditInboxMessageRequest.md)|  | |

### Return type

[**EditInboxMessage200Response**](EditInboxMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message edited |  -  |
| **400** | Not supported or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## editInboxMessageWithHttpInfo

> ApiResponse<EditInboxMessage200Response> editInboxMessage editInboxMessageWithHttpInfo(conversationId, messageId, editInboxMessageRequest)

Edit message

Edit the text and/or reply markup of a previously sent Telegram message. Only supported for Telegram. Returns 400 for other platforms. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The Telegram message ID to edit
        EditInboxMessageRequest editInboxMessageRequest = new EditInboxMessageRequest(); // EditInboxMessageRequest | 
        try {
            ApiResponse<EditInboxMessage200Response> response = apiInstance.editInboxMessageWithHttpInfo(conversationId, messageId, editInboxMessageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#editInboxMessage");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The Telegram message ID to edit | |
| **editInboxMessageRequest** | [**EditInboxMessageRequest**](EditInboxMessageRequest.md)|  | |

### Return type

ApiResponse<[**EditInboxMessage200Response**](EditInboxMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message edited |  -  |
| **400** | Not supported or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## getInboxConversation

> GetInboxConversation200Response getInboxConversation(conversationId, accountId)

Get conversation

Retrieve details and metadata for a specific conversation. Requires accountId query parameter.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        String accountId = "accountId_example"; // String | The social account ID
        try {
            GetInboxConversation200Response result = apiInstance.getInboxConversation(conversationId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#getInboxConversation");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **accountId** | **String**| The social account ID | |

### Return type

[**GetInboxConversation200Response**](GetInboxConversation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversation details |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Conversation not found |  -  |

## getInboxConversationWithHttpInfo

> ApiResponse<GetInboxConversation200Response> getInboxConversation getInboxConversationWithHttpInfo(conversationId, accountId)

Get conversation

Retrieve details and metadata for a specific conversation. Requires accountId query parameter.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        String accountId = "accountId_example"; // String | The social account ID
        try {
            ApiResponse<GetInboxConversation200Response> response = apiInstance.getInboxConversationWithHttpInfo(conversationId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#getInboxConversation");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **accountId** | **String**| The social account ID | |

### Return type

ApiResponse<[**GetInboxConversation200Response**](GetInboxConversation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversation details |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Conversation not found |  -  |


## getInboxConversationMessages

> GetInboxConversationMessages200Response getInboxConversationMessages(conversationId, accountId)

List messages

Fetch messages for a specific conversation. Requires accountId query parameter.  **Twitter/X limitation:** X&#39;s encrypted \&quot;X Chat\&quot; messages are not accessible via the API. Conversations where the other participant uses encrypted X Chat may only show your outgoing messages. See the [list conversations endpoint](#/Messages/listInboxConversations) for more details. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        String accountId = "accountId_example"; // String | Social account ID
        try {
            GetInboxConversationMessages200Response result = apiInstance.getInboxConversationMessages(conversationId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#getInboxConversationMessages");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **accountId** | **String**| Social account ID | |

### Return type

[**GetInboxConversationMessages200Response**](GetInboxConversationMessages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Messages in conversation |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## getInboxConversationMessagesWithHttpInfo

> ApiResponse<GetInboxConversationMessages200Response> getInboxConversationMessages getInboxConversationMessagesWithHttpInfo(conversationId, accountId)

List messages

Fetch messages for a specific conversation. Requires accountId query parameter.  **Twitter/X limitation:** X&#39;s encrypted \&quot;X Chat\&quot; messages are not accessible via the API. Conversations where the other participant uses encrypted X Chat may only show your outgoing messages. See the [list conversations endpoint](#/Messages/listInboxConversations) for more details. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        String accountId = "accountId_example"; // String | Social account ID
        try {
            ApiResponse<GetInboxConversationMessages200Response> response = apiInstance.getInboxConversationMessagesWithHttpInfo(conversationId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#getInboxConversationMessages");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **accountId** | **String**| Social account ID | |

### Return type

ApiResponse<[**GetInboxConversationMessages200Response**](GetInboxConversationMessages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Messages in conversation |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## listInboxConversations

> ListInboxConversations200Response listInboxConversations(profileId, platform, status, sortOrder, limit, cursor, accountId)

List conversations

Fetch conversations (DMs) from all connected messaging accounts in a single API call. Supports filtering by profile and platform. Results are aggregated and deduplicated. Supported platforms: Facebook, Instagram, Twitter/X, Bluesky, Reddit, Telegram.  **Twitter/X limitation:** X has replaced traditional DMs with encrypted \&quot;X Chat\&quot; for many accounts. Messages sent or received through encrypted X Chat are not accessible via X&#39;s API (the &#x60;/2/dm_events&#x60; endpoint only returns legacy unencrypted DMs). This means some Twitter/X conversations may show only outgoing messages or appear empty. This is an X platform limitation that affects all third-party applications. See [X&#39;s docs on encrypted messaging](https://help.x.com/en/using-x/about-chat) for more details. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile ID
        String platform = "facebook"; // String | Filter by platform
        String status = "active"; // String | Filter by conversation status
        String sortOrder = "asc"; // String | Sort order by updated time
        Integer limit = 50; // Integer | Maximum number of conversations to return
        String cursor = "cursor_example"; // String | Pagination cursor for next page
        String accountId = "accountId_example"; // String | Filter by specific social account ID
        try {
            ListInboxConversations200Response result = apiInstance.listInboxConversations(profileId, platform, status, sortOrder, limit, cursor, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#listInboxConversations");
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
| **profileId** | **String**| Filter by profile ID | [optional] |
| **platform** | **String**| Filter by platform | [optional] [enum: facebook, instagram, twitter, bluesky, reddit, telegram] |
| **status** | **String**| Filter by conversation status | [optional] [enum: active, archived] |
| **sortOrder** | **String**| Sort order by updated time | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**| Maximum number of conversations to return | [optional] [default to 50] |
| **cursor** | **String**| Pagination cursor for next page | [optional] |
| **accountId** | **String**| Filter by specific social account ID | [optional] |

### Return type

[**ListInboxConversations200Response**](ListInboxConversations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated conversations |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## listInboxConversationsWithHttpInfo

> ApiResponse<ListInboxConversations200Response> listInboxConversations listInboxConversationsWithHttpInfo(profileId, platform, status, sortOrder, limit, cursor, accountId)

List conversations

Fetch conversations (DMs) from all connected messaging accounts in a single API call. Supports filtering by profile and platform. Results are aggregated and deduplicated. Supported platforms: Facebook, Instagram, Twitter/X, Bluesky, Reddit, Telegram.  **Twitter/X limitation:** X has replaced traditional DMs with encrypted \&quot;X Chat\&quot; for many accounts. Messages sent or received through encrypted X Chat are not accessible via X&#39;s API (the &#x60;/2/dm_events&#x60; endpoint only returns legacy unencrypted DMs). This means some Twitter/X conversations may show only outgoing messages or appear empty. This is an X platform limitation that affects all third-party applications. See [X&#39;s docs on encrypted messaging](https://help.x.com/en/using-x/about-chat) for more details. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile ID
        String platform = "facebook"; // String | Filter by platform
        String status = "active"; // String | Filter by conversation status
        String sortOrder = "asc"; // String | Sort order by updated time
        Integer limit = 50; // Integer | Maximum number of conversations to return
        String cursor = "cursor_example"; // String | Pagination cursor for next page
        String accountId = "accountId_example"; // String | Filter by specific social account ID
        try {
            ApiResponse<ListInboxConversations200Response> response = apiInstance.listInboxConversationsWithHttpInfo(profileId, platform, status, sortOrder, limit, cursor, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#listInboxConversations");
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
| **profileId** | **String**| Filter by profile ID | [optional] |
| **platform** | **String**| Filter by platform | [optional] [enum: facebook, instagram, twitter, bluesky, reddit, telegram] |
| **status** | **String**| Filter by conversation status | [optional] [enum: active, archived] |
| **sortOrder** | **String**| Sort order by updated time | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**| Maximum number of conversations to return | [optional] [default to 50] |
| **cursor** | **String**| Pagination cursor for next page | [optional] |
| **accountId** | **String**| Filter by specific social account ID | [optional] |

### Return type

ApiResponse<[**ListInboxConversations200Response**](ListInboxConversations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated conversations |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## removeMessageReaction

> UpdateRedditSubreddits200Response removeMessageReaction(conversationId, messageId, accountId)

Remove reaction

Remove a reaction from a message. Platform support: - **Telegram**: Send empty reaction array to clear - **WhatsApp**: Send empty emoji to remove - **All others**: Returns 400 (not supported) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The platform message ID
        String accountId = "accountId_example"; // String | Social account ID
        try {
            UpdateRedditSubreddits200Response result = apiInstance.removeMessageReaction(conversationId, messageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#removeMessageReaction");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The platform message ID | |
| **accountId** | **String**| Social account ID | |

### Return type

[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reaction removed |  -  |
| **400** | Platform does not support reactions or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |

## removeMessageReactionWithHttpInfo

> ApiResponse<UpdateRedditSubreddits200Response> removeMessageReaction removeMessageReactionWithHttpInfo(conversationId, messageId, accountId)

Remove reaction

Remove a reaction from a message. Platform support: - **Telegram**: Send empty reaction array to clear - **WhatsApp**: Send empty emoji to remove - **All others**: Returns 400 (not supported) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        String messageId = "messageId_example"; // String | The platform message ID
        String accountId = "accountId_example"; // String | Social account ID
        try {
            ApiResponse<UpdateRedditSubreddits200Response> response = apiInstance.removeMessageReactionWithHttpInfo(conversationId, messageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#removeMessageReaction");
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
| **conversationId** | **String**| The conversation ID | |
| **messageId** | **String**| The platform message ID | |
| **accountId** | **String**| Social account ID | |

### Return type

ApiResponse<[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reaction removed |  -  |
| **400** | Platform does not support reactions or invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |


## sendInboxMessage

> SendInboxMessage200Response sendInboxMessage(conversationId, sendInboxMessageRequest)

Send message

Send a message in a conversation. Supports text, attachments, quick replies, buttons, and message tags. Attachment and interactive message support varies by platform.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        SendInboxMessageRequest sendInboxMessageRequest = new SendInboxMessageRequest(); // SendInboxMessageRequest | 
        try {
            SendInboxMessage200Response result = apiInstance.sendInboxMessage(conversationId, sendInboxMessageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#sendInboxMessage");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **sendInboxMessageRequest** | [**SendInboxMessageRequest**](SendInboxMessageRequest.md)|  | |

### Return type

[**SendInboxMessage200Response**](SendInboxMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message sent |  -  |
| **400** | Bad request (e.g., attachment not supported for platform, validation error) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## sendInboxMessageWithHttpInfo

> ApiResponse<SendInboxMessage200Response> sendInboxMessage sendInboxMessageWithHttpInfo(conversationId, sendInboxMessageRequest)

Send message

Send a message in a conversation. Supports text, attachments, quick replies, buttons, and message tags. Attachment and interactive message support varies by platform.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        SendInboxMessageRequest sendInboxMessageRequest = new SendInboxMessageRequest(); // SendInboxMessageRequest | 
        try {
            ApiResponse<SendInboxMessage200Response> response = apiInstance.sendInboxMessageWithHttpInfo(conversationId, sendInboxMessageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#sendInboxMessage");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **sendInboxMessageRequest** | [**SendInboxMessageRequest**](SendInboxMessageRequest.md)|  | |

### Return type

ApiResponse<[**SendInboxMessage200Response**](SendInboxMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message sent |  -  |
| **400** | Bad request (e.g., attachment not supported for platform, validation error) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## sendTypingIndicator

> UpdateRedditSubreddits200Response sendTypingIndicator(conversationId, sendTypingIndicatorRequest)

Send typing indicator

Show a typing indicator in a conversation. Platform support: - **Facebook Messenger**: Shows \&quot;Page is typing...\&quot; for 20 seconds - **Telegram**: Shows \&quot;Bot is typing...\&quot; for 5 seconds - **All others**: Returns 200 but no-op (platform doesn&#39;t support it)  Typing indicators are best-effort. The endpoint always returns 200 even if the platform call fails. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        SendTypingIndicatorRequest sendTypingIndicatorRequest = new SendTypingIndicatorRequest(); // SendTypingIndicatorRequest | 
        try {
            UpdateRedditSubreddits200Response result = apiInstance.sendTypingIndicator(conversationId, sendTypingIndicatorRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#sendTypingIndicator");
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
| **conversationId** | **String**| The conversation ID | |
| **sendTypingIndicatorRequest** | [**SendTypingIndicatorRequest**](SendTypingIndicatorRequest.md)|  | |

### Return type

[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typing indicator sent (or no-op on unsupported platforms) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |

## sendTypingIndicatorWithHttpInfo

> ApiResponse<UpdateRedditSubreddits200Response> sendTypingIndicator sendTypingIndicatorWithHttpInfo(conversationId, sendTypingIndicatorRequest)

Send typing indicator

Show a typing indicator in a conversation. Platform support: - **Facebook Messenger**: Shows \&quot;Page is typing...\&quot; for 20 seconds - **Telegram**: Shows \&quot;Bot is typing...\&quot; for 5 seconds - **All others**: Returns 200 but no-op (platform doesn&#39;t support it)  Typing indicators are best-effort. The endpoint always returns 200 even if the platform call fails. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID
        SendTypingIndicatorRequest sendTypingIndicatorRequest = new SendTypingIndicatorRequest(); // SendTypingIndicatorRequest | 
        try {
            ApiResponse<UpdateRedditSubreddits200Response> response = apiInstance.sendTypingIndicatorWithHttpInfo(conversationId, sendTypingIndicatorRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#sendTypingIndicator");
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
| **conversationId** | **String**| The conversation ID | |
| **sendTypingIndicatorRequest** | [**SendTypingIndicatorRequest**](SendTypingIndicatorRequest.md)|  | |

### Return type

ApiResponse<[**UpdateRedditSubreddits200Response**](UpdateRedditSubreddits200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typing indicator sent (or no-op on unsupported platforms) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |
| **404** | Account or conversation not found |  -  |


## updateInboxConversation

> UpdateInboxConversation200Response updateInboxConversation(conversationId, updateInboxConversationRequest)

Update conversation status

Archive or activate a conversation. Requires accountId in request body.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        UpdateInboxConversationRequest updateInboxConversationRequest = new UpdateInboxConversationRequest(); // UpdateInboxConversationRequest | 
        try {
            UpdateInboxConversation200Response result = apiInstance.updateInboxConversation(conversationId, updateInboxConversationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#updateInboxConversation");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **updateInboxConversationRequest** | [**UpdateInboxConversationRequest**](UpdateInboxConversationRequest.md)|  | |

### Return type

[**UpdateInboxConversation200Response**](UpdateInboxConversation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversation updated |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |

## updateInboxConversationWithHttpInfo

> ApiResponse<UpdateInboxConversation200Response> updateInboxConversation updateInboxConversationWithHttpInfo(conversationId, updateInboxConversationRequest)

Update conversation status

Archive or activate a conversation. Requires accountId in request body.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID.
        UpdateInboxConversationRequest updateInboxConversationRequest = new UpdateInboxConversationRequest(); // UpdateInboxConversationRequest | 
        try {
            ApiResponse<UpdateInboxConversation200Response> response = apiInstance.updateInboxConversationWithHttpInfo(conversationId, updateInboxConversationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#updateInboxConversation");
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
| **conversationId** | **String**| The conversation ID (id field from list conversations endpoint). This is the platform-specific conversation identifier, not an internal database ID. | |
| **updateInboxConversationRequest** | [**UpdateInboxConversationRequest**](UpdateInboxConversationRequest.md)|  | |

### Return type

ApiResponse<[**UpdateInboxConversation200Response**](UpdateInboxConversation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Conversation updated |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox addon required |  -  |


## uploadMediaDirect

> UploadMediaDirect200Response uploadMediaDirect(_file, contentType)

Upload media file

Upload a media file using API key authentication and get back a publicly accessible URL. The URL can be used as &#x60;attachmentUrl&#x60; when sending inbox messages.  Files are stored in temporary storage and auto-delete after 7 days. Maximum file size is 25MB.  Unlike &#x60;/v1/media/upload&#x60; (which uses upload tokens for end-user flows), this endpoint uses standard Bearer token authentication for programmatic use. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        File _file = new File("/path/to/file"); // File | The file to upload (max 25MB)
        String contentType = "contentType_example"; // String | Override MIME type (e.g. \\\"image/jpeg\\\"). Auto-detected from file if not provided.
        try {
            UploadMediaDirect200Response result = apiInstance.uploadMediaDirect(_file, contentType);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#uploadMediaDirect");
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
| **_file** | **File**| The file to upload (max 25MB) | |
| **contentType** | **String**| Override MIME type (e.g. \\\&quot;image/jpeg\\\&quot;). Auto-detected from file if not provided. | [optional] |

### Return type

[**UploadMediaDirect200Response**](UploadMediaDirect200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File uploaded successfully |  -  |
| **400** | No file provided or file too large |  -  |
| **401** | Unauthorized |  -  |

## uploadMediaDirectWithHttpInfo

> ApiResponse<UploadMediaDirect200Response> uploadMediaDirect uploadMediaDirectWithHttpInfo(_file, contentType)

Upload media file

Upload a media file using API key authentication and get back a publicly accessible URL. The URL can be used as &#x60;attachmentUrl&#x60; when sending inbox messages.  Files are stored in temporary storage and auto-delete after 7 days. Maximum file size is 25MB.  Unlike &#x60;/v1/media/upload&#x60; (which uses upload tokens for end-user flows), this endpoint uses standard Bearer token authentication for programmatic use. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagesApi apiInstance = new MessagesApi(defaultClient);
        File _file = new File("/path/to/file"); // File | The file to upload (max 25MB)
        String contentType = "contentType_example"; // String | Override MIME type (e.g. \\\"image/jpeg\\\"). Auto-detected from file if not provided.
        try {
            ApiResponse<UploadMediaDirect200Response> response = apiInstance.uploadMediaDirectWithHttpInfo(_file, contentType);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagesApi#uploadMediaDirect");
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
| **_file** | **File**| The file to upload (max 25MB) | |
| **contentType** | **String**| Override MIME type (e.g. \\\&quot;image/jpeg\\\&quot;). Auto-detected from file if not provided. | [optional] |

### Return type

ApiResponse<[**UploadMediaDirect200Response**](UploadMediaDirect200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File uploaded successfully |  -  |
| **400** | No file provided or file too large |  -  |
| **401** | Unauthorized |  -  |

