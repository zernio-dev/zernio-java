# IMessageApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addImessageGroupParticipant**](IMessageApi.md#addImessageGroupParticipant) | **POST** /v1/imessage/groups/{conversationId}/participants | Add a participant to an iMessage group |
| [**addImessageGroupParticipantWithHttpInfo**](IMessageApi.md#addImessageGroupParticipantWithHttpInfo) | **POST** /v1/imessage/groups/{conversationId}/participants | Add a participant to an iMessage group |
| [**cancelImessageSender**](IMessageApi.md#cancelImessageSender) | **DELETE** /v1/imessage/senders/{senderId} | Cancel an iMessage sender |
| [**cancelImessageSenderWithHttpInfo**](IMessageApi.md#cancelImessageSenderWithHttpInfo) | **DELETE** /v1/imessage/senders/{senderId} | Cancel an iMessage sender |
| [**createImessageGroup**](IMessageApi.md#createImessageGroup) | **POST** /v1/imessage/groups | Start an iMessage group chat |
| [**createImessageGroupWithHttpInfo**](IMessageApi.md#createImessageGroupWithHttpInfo) | **POST** /v1/imessage/groups | Start an iMessage group chat |
| [**createImessageOptInLink**](IMessageApi.md#createImessageOptInLink) | **POST** /v1/imessage/senders/{senderId}/opt-in-links | Create a tracked iMessage opt-in link |
| [**createImessageOptInLinkWithHttpInfo**](IMessageApi.md#createImessageOptInLinkWithHttpInfo) | **POST** /v1/imessage/senders/{senderId}/opt-in-links | Create a tracked iMessage opt-in link |
| [**getImessageGroup**](IMessageApi.md#getImessageGroup) | **GET** /v1/imessage/groups/{conversationId} | Get an iMessage group |
| [**getImessageGroupWithHttpInfo**](IMessageApi.md#getImessageGroupWithHttpInfo) | **GET** /v1/imessage/groups/{conversationId} | Get an iMessage group |
| [**getImessageSender**](IMessageApi.md#getImessageSender) | **GET** /v1/imessage/senders/{senderId} | Get iMessage sender status |
| [**getImessageSenderWithHttpInfo**](IMessageApi.md#getImessageSenderWithHttpInfo) | **GET** /v1/imessage/senders/{senderId} | Get iMessage sender status |
| [**listImessageAudience**](IMessageApi.md#listImessageAudience) | **GET** /v1/imessage/audience | List iMessage audience |
| [**listImessageAudienceWithHttpInfo**](IMessageApi.md#listImessageAudienceWithHttpInfo) | **GET** /v1/imessage/audience | List iMessage audience |
| [**listImessageAvailableNumbers**](IMessageApi.md#listImessageAvailableNumbers) | **GET** /v1/imessage/senders/available-numbers | List instantly available iMessage numbers |
| [**listImessageAvailableNumbersWithHttpInfo**](IMessageApi.md#listImessageAvailableNumbersWithHttpInfo) | **GET** /v1/imessage/senders/available-numbers | List instantly available iMessage numbers |
| [**listImessageSenderOrders**](IMessageApi.md#listImessageSenderOrders) | **GET** /v1/imessage/senders/order | List iMessage sender orders |
| [**listImessageSenderOrdersWithHttpInfo**](IMessageApi.md#listImessageSenderOrdersWithHttpInfo) | **GET** /v1/imessage/senders/order | List iMessage sender orders |
| [**listImessageSenders**](IMessageApi.md#listImessageSenders) | **GET** /v1/imessage/senders | List iMessage senders |
| [**listImessageSendersWithHttpInfo**](IMessageApi.md#listImessageSendersWithHttpInfo) | **GET** /v1/imessage/senders | List iMessage senders |
| [**orderImessageSender**](IMessageApi.md#orderImessageSender) | **POST** /v1/imessage/senders/order | Order a new iMessage sender |
| [**orderImessageSenderWithHttpInfo**](IMessageApi.md#orderImessageSenderWithHttpInfo) | **POST** /v1/imessage/senders/order | Order a new iMessage sender |
| [**registerImessageSender**](IMessageApi.md#registerImessageSender) | **POST** /v1/imessage/senders | Register an iMessage sender |
| [**registerImessageSenderWithHttpInfo**](IMessageApi.md#registerImessageSenderWithHttpInfo) | **POST** /v1/imessage/senders | Register an iMessage sender |
| [**removeImessageGroupParticipant**](IMessageApi.md#removeImessageGroupParticipant) | **DELETE** /v1/imessage/groups/{conversationId}/participants | Remove a participant from an iMessage group |
| [**removeImessageGroupParticipantWithHttpInfo**](IMessageApi.md#removeImessageGroupParticipantWithHttpInfo) | **DELETE** /v1/imessage/groups/{conversationId}/participants | Remove a participant from an iMessage group |
| [**reserveImessageAvailableNumber**](IMessageApi.md#reserveImessageAvailableNumber) | **POST** /v1/imessage/senders/available-numbers/{numberId}/reserve | Reserve an available iMessage number |
| [**reserveImessageAvailableNumberWithHttpInfo**](IMessageApi.md#reserveImessageAvailableNumberWithHttpInfo) | **POST** /v1/imessage/senders/available-numbers/{numberId}/reserve | Reserve an available iMessage number |
| [**setImessageSubscription**](IMessageApi.md#setImessageSubscription) | **POST** /v1/imessage/audience/subscription | Subscribe or opt out an iMessage contact |
| [**setImessageSubscriptionWithHttpInfo**](IMessageApi.md#setImessageSubscriptionWithHttpInfo) | **POST** /v1/imessage/audience/subscription | Subscribe or opt out an iMessage contact |
| [**updateImessageGroup**](IMessageApi.md#updateImessageGroup) | **PATCH** /v1/imessage/groups/{conversationId} | Rename an iMessage group or change its photo |
| [**updateImessageGroupWithHttpInfo**](IMessageApi.md#updateImessageGroupWithHttpInfo) | **PATCH** /v1/imessage/groups/{conversationId} | Rename an iMessage group or change its photo |
| [**updateImessageSender**](IMessageApi.md#updateImessageSender) | **PATCH** /v1/imessage/senders/{senderId} | Update an iMessage sender |
| [**updateImessageSenderWithHttpInfo**](IMessageApi.md#updateImessageSenderWithHttpInfo) | **PATCH** /v1/imessage/senders/{senderId} | Update an iMessage sender |



## addImessageGroupParticipant

> AddImessageGroupParticipant200Response addImessageGroupParticipant(conversationId, addImessageGroupParticipantRequest)

Add a participant to an iMessage group

Applied asynchronously by the provider; the participant list on the next group webhook reflects it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | 
        AddImessageGroupParticipantRequest addImessageGroupParticipantRequest = new AddImessageGroupParticipantRequest(); // AddImessageGroupParticipantRequest | 
        try {
            AddImessageGroupParticipant200Response result = apiInstance.addImessageGroupParticipant(conversationId, addImessageGroupParticipantRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#addImessageGroupParticipant");
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
| **conversationId** | **String**|  | |
| **addImessageGroupParticipantRequest** | [**AddImessageGroupParticipantRequest**](AddImessageGroupParticipantRequest.md)|  | |

### Return type

[**AddImessageGroupParticipant200Response**](AddImessageGroupParticipant200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change accepted |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |

## addImessageGroupParticipantWithHttpInfo

> ApiResponse<AddImessageGroupParticipant200Response> addImessageGroupParticipant addImessageGroupParticipantWithHttpInfo(conversationId, addImessageGroupParticipantRequest)

Add a participant to an iMessage group

Applied asynchronously by the provider; the participant list on the next group webhook reflects it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | 
        AddImessageGroupParticipantRequest addImessageGroupParticipantRequest = new AddImessageGroupParticipantRequest(); // AddImessageGroupParticipantRequest | 
        try {
            ApiResponse<AddImessageGroupParticipant200Response> response = apiInstance.addImessageGroupParticipantWithHttpInfo(conversationId, addImessageGroupParticipantRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#addImessageGroupParticipant");
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
| **conversationId** | **String**|  | |
| **addImessageGroupParticipantRequest** | [**AddImessageGroupParticipantRequest**](AddImessageGroupParticipantRequest.md)|  | |

### Return type

ApiResponse<[**AddImessageGroupParticipant200Response**](AddImessageGroupParticipant200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change accepted |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |


## cancelImessageSender

> OrderImessageSender202Response cancelImessageSender(senderId)

Cancel an iMessage sender

Cancels the sender at the provider and deactivates its messaging account. Billing stops with the current month (no proration or refunds, matching phone numbers). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        try {
            OrderImessageSender202Response result = apiInstance.cancelImessageSender(senderId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#cancelImessageSender");
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
| **senderId** | **String**|  | |

### Return type

[**OrderImessageSender202Response**](OrderImessageSender202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender canceled |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |

## cancelImessageSenderWithHttpInfo

> ApiResponse<OrderImessageSender202Response> cancelImessageSender cancelImessageSenderWithHttpInfo(senderId)

Cancel an iMessage sender

Cancels the sender at the provider and deactivates its messaging account. Billing stops with the current month (no proration or refunds, matching phone numbers). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        try {
            ApiResponse<OrderImessageSender202Response> response = apiInstance.cancelImessageSenderWithHttpInfo(senderId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#cancelImessageSender");
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
| **senderId** | **String**|  | |

### Return type

ApiResponse<[**OrderImessageSender202Response**](OrderImessageSender202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender canceled |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |


## createImessageGroup

> CreateImessageGroup202Response createImessageGroup(createImessageGroupRequest)

Start an iMessage group chat

Creates a group chat from one of your senders and sends its first message. The provider processes it asynchronously: the response carries the request id, and the thread appears in the inbox (with its group conversation id) on the first webhook. Starting a group counts as messaging new contacts, so the sender needs the provider&#39;s init-conversations add-on and the same sending intervals apply; without it the request fails with 409 &#x60;recipient_must_message_first&#x60;. WhatsApp groups need a &#x60;name&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        CreateImessageGroupRequest createImessageGroupRequest = new CreateImessageGroupRequest(); // CreateImessageGroupRequest | 
        try {
            CreateImessageGroup202Response result = apiInstance.createImessageGroup(createImessageGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#createImessageGroup");
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
| **createImessageGroupRequest** | [**CreateImessageGroupRequest**](CreateImessageGroupRequest.md)|  | |

### Return type

[**CreateImessageGroup202Response**](CreateImessageGroup202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Group creation accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account not found |  -  |
| **409** | The sender cannot start conversations (code: recipient_must_message_first) |  -  |

## createImessageGroupWithHttpInfo

> ApiResponse<CreateImessageGroup202Response> createImessageGroup createImessageGroupWithHttpInfo(createImessageGroupRequest)

Start an iMessage group chat

Creates a group chat from one of your senders and sends its first message. The provider processes it asynchronously: the response carries the request id, and the thread appears in the inbox (with its group conversation id) on the first webhook. Starting a group counts as messaging new contacts, so the sender needs the provider&#39;s init-conversations add-on and the same sending intervals apply; without it the request fails with 409 &#x60;recipient_must_message_first&#x60;. WhatsApp groups need a &#x60;name&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        CreateImessageGroupRequest createImessageGroupRequest = new CreateImessageGroupRequest(); // CreateImessageGroupRequest | 
        try {
            ApiResponse<CreateImessageGroup202Response> response = apiInstance.createImessageGroupWithHttpInfo(createImessageGroupRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#createImessageGroup");
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
| **createImessageGroupRequest** | [**CreateImessageGroupRequest**](CreateImessageGroupRequest.md)|  | |

### Return type

ApiResponse<[**CreateImessageGroup202Response**](CreateImessageGroup202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Group creation accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account not found |  -  |
| **409** | The sender cannot start conversations (code: recipient_must_message_first) |  -  |


## createImessageOptInLink

> CreateImessageOptInLink200Response createImessageOptInLink(senderId, createImessageOptInLinkRequest)

Create a tracked iMessage opt-in link

Generates a per-campaign link that opens Messages on this sender with &#x60;body&#x60; prefilled. iMessage is send-first: a sender can only message a contact who has written to it (a send to anyone else fails with &#x60;recipient_must_message_first&#x60;), and the contact&#39;s tap-and-send is what opens that door.  Each link carries a unique code in place of the &#x60;[opt-in-code]&#x60; placeholder; when the contact sends it, the resulting &#x60;message.received&#x60; webhook (and the stored inbox message&#39;s &#x60;metadata&#x60;) has &#x60;optIn: true&#x60; and your &#x60;parameters&#x60; under &#x60;optInParameters&#x60;, so you can attribute the conversation to the campaign or lead that produced it.  For an untracked link, use the sender&#39;s &#x60;optInLink&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        CreateImessageOptInLinkRequest createImessageOptInLinkRequest = new CreateImessageOptInLinkRequest(); // CreateImessageOptInLinkRequest | 
        try {
            CreateImessageOptInLink200Response result = apiInstance.createImessageOptInLink(senderId, createImessageOptInLinkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#createImessageOptInLink");
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
| **senderId** | **String**|  | |
| **createImessageOptInLinkRequest** | [**CreateImessageOptInLinkRequest**](CreateImessageOptInLinkRequest.md)|  | |

### Return type

[**CreateImessageOptInLink200Response**](CreateImessageOptInLink200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Opt-in link created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |
| **409** | The sender is not active yet |  -  |

## createImessageOptInLinkWithHttpInfo

> ApiResponse<CreateImessageOptInLink200Response> createImessageOptInLink createImessageOptInLinkWithHttpInfo(senderId, createImessageOptInLinkRequest)

Create a tracked iMessage opt-in link

Generates a per-campaign link that opens Messages on this sender with &#x60;body&#x60; prefilled. iMessage is send-first: a sender can only message a contact who has written to it (a send to anyone else fails with &#x60;recipient_must_message_first&#x60;), and the contact&#39;s tap-and-send is what opens that door.  Each link carries a unique code in place of the &#x60;[opt-in-code]&#x60; placeholder; when the contact sends it, the resulting &#x60;message.received&#x60; webhook (and the stored inbox message&#39;s &#x60;metadata&#x60;) has &#x60;optIn: true&#x60; and your &#x60;parameters&#x60; under &#x60;optInParameters&#x60;, so you can attribute the conversation to the campaign or lead that produced it.  For an untracked link, use the sender&#39;s &#x60;optInLink&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        CreateImessageOptInLinkRequest createImessageOptInLinkRequest = new CreateImessageOptInLinkRequest(); // CreateImessageOptInLinkRequest | 
        try {
            ApiResponse<CreateImessageOptInLink200Response> response = apiInstance.createImessageOptInLinkWithHttpInfo(senderId, createImessageOptInLinkRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#createImessageOptInLink");
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
| **senderId** | **String**|  | |
| **createImessageOptInLinkRequest** | [**CreateImessageOptInLinkRequest**](CreateImessageOptInLinkRequest.md)|  | |

### Return type

ApiResponse<[**CreateImessageOptInLink200Response**](CreateImessageOptInLink200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Opt-in link created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |
| **409** | The sender is not active yet |  -  |


## getImessageGroup

> GetImessageGroup200Response getImessageGroup(conversationId, accountId)

Get an iMessage group

The group&#39;s name, participants and channel as the provider currently sees them. The conversation must be a group thread of the given account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The inbox conversation id (or the provider group id)
        String accountId = "accountId_example"; // String | 
        try {
            GetImessageGroup200Response result = apiInstance.getImessageGroup(conversationId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#getImessageGroup");
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
| **conversationId** | **String**| The inbox conversation id (or the provider group id) | |
| **accountId** | **String**|  | |

### Return type

[**GetImessageGroup200Response**](GetImessageGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group details |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |

## getImessageGroupWithHttpInfo

> ApiResponse<GetImessageGroup200Response> getImessageGroup getImessageGroupWithHttpInfo(conversationId, accountId)

Get an iMessage group

The group&#39;s name, participants and channel as the provider currently sees them. The conversation must be a group thread of the given account.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | The inbox conversation id (or the provider group id)
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetImessageGroup200Response> response = apiInstance.getImessageGroupWithHttpInfo(conversationId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#getImessageGroup");
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
| **conversationId** | **String**| The inbox conversation id (or the provider group id) | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**GetImessageGroup200Response**](GetImessageGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group details |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |


## getImessageSender

> GetImessageSender200Response getImessageSender(senderId)

Get iMessage sender status

Lifecycle status of an ordered or registered sender (poll while an order activates), plus the provider&#39;s live platform health for it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        try {
            GetImessageSender200Response result = apiInstance.getImessageSender(senderId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#getImessageSender");
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
| **senderId** | **String**|  | |

### Return type

[**GetImessageSender200Response**](GetImessageSender200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender lifecycle |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |

## getImessageSenderWithHttpInfo

> ApiResponse<GetImessageSender200Response> getImessageSender getImessageSenderWithHttpInfo(senderId)

Get iMessage sender status

Lifecycle status of an ordered or registered sender (poll while an order activates), plus the provider&#39;s live platform health for it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        try {
            ApiResponse<GetImessageSender200Response> response = apiInstance.getImessageSenderWithHttpInfo(senderId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#getImessageSender");
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
| **senderId** | **String**|  | |

### Return type

ApiResponse<[**GetImessageSender200Response**](GetImessageSender200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender lifecycle |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |


## listImessageAudience

> ListImessageAudience200Response listImessageAudience(accountId, status, search, limit, skip)

List iMessage audience

Contacts who have messaged your iMessage senders (1:1 threads), with subscription state and, for threads opened through a tracked opt-in link, the parameters that brought them in. Newest activity first.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String accountId = "accountId_example"; // String | Limit to one sender account
        String status = "subscribed"; // String | 
        String search = "search_example"; // String | Matches the contact handle or name
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListImessageAudience200Response result = apiInstance.listImessageAudience(accountId, status, search, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageAudience");
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
| **accountId** | **String**| Limit to one sender account | [optional] |
| **status** | **String**|  | [optional] [enum: subscribed, unsubscribed] |
| **search** | **String**| Matches the contact handle or name | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListImessageAudience200Response**](ListImessageAudience200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience page |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |

## listImessageAudienceWithHttpInfo

> ApiResponse<ListImessageAudience200Response> listImessageAudience listImessageAudienceWithHttpInfo(accountId, status, search, limit, skip)

List iMessage audience

Contacts who have messaged your iMessage senders (1:1 threads), with subscription state and, for threads opened through a tracked opt-in link, the parameters that brought them in. Newest activity first.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String accountId = "accountId_example"; // String | Limit to one sender account
        String status = "subscribed"; // String | 
        String search = "search_example"; // String | Matches the contact handle or name
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListImessageAudience200Response> response = apiInstance.listImessageAudienceWithHttpInfo(accountId, status, search, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageAudience");
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
| **accountId** | **String**| Limit to one sender account | [optional] |
| **status** | **String**|  | [optional] [enum: subscribed, unsubscribed] |
| **search** | **String**| Matches the contact handle or name | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListImessageAudience200Response**](ListImessageAudience200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience page |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |


## listImessageAvailableNumbers

> ListImessageAvailableNumbers200Response listImessageAvailableNumbers(region)

List instantly available iMessage numbers

Phone numbers the provider has already registered and can assign on the spot. Order one by passing its &#x60;id&#x60; as &#x60;availableNumberId&#x60; to POST /v1/imessage/senders/order: the sender activates immediately instead of after the usual provisioning wait. Reserve it first with POST /v1/imessage/senders/available-numbers/{numberId}/reserve while the buyer decides. The list is a snapshot; a number can be taken between listing and ordering. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String region = "US"; // String | 
        try {
            ListImessageAvailableNumbers200Response result = apiInstance.listImessageAvailableNumbers(region);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageAvailableNumbers");
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
| **region** | **String**|  | [optional] [enum: US, GB] |

### Return type

[**ListImessageAvailableNumbers200Response**](ListImessageAvailableNumbers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Available numbers |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |

## listImessageAvailableNumbersWithHttpInfo

> ApiResponse<ListImessageAvailableNumbers200Response> listImessageAvailableNumbers listImessageAvailableNumbersWithHttpInfo(region)

List instantly available iMessage numbers

Phone numbers the provider has already registered and can assign on the spot. Order one by passing its &#x60;id&#x60; as &#x60;availableNumberId&#x60; to POST /v1/imessage/senders/order: the sender activates immediately instead of after the usual provisioning wait. Reserve it first with POST /v1/imessage/senders/available-numbers/{numberId}/reserve while the buyer decides. The list is a snapshot; a number can be taken between listing and ordering. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String region = "US"; // String | 
        try {
            ApiResponse<ListImessageAvailableNumbers200Response> response = apiInstance.listImessageAvailableNumbersWithHttpInfo(region);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageAvailableNumbers");
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
| **region** | **String**|  | [optional] [enum: US, GB] |

### Return type

ApiResponse<[**ListImessageAvailableNumbers200Response**](ListImessageAvailableNumbers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Available numbers |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |


## listImessageSenderOrders

> ListImessageSenderOrders200Response listImessageSenderOrders(includeCanceled)

List iMessage sender orders

Every sender lifecycle doc your team owns (ordered or registered), across statuses. Canceled senders are omitted unless &#x60;includeCanceled&#x3D;true&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        Boolean includeCanceled = false; // Boolean | 
        try {
            ListImessageSenderOrders200Response result = apiInstance.listImessageSenderOrders(includeCanceled);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageSenderOrders");
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
| **includeCanceled** | **Boolean**|  | [optional] [default to false] |

### Return type

[**ListImessageSenderOrders200Response**](ListImessageSenderOrders200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender lifecycle docs, newest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |

## listImessageSenderOrdersWithHttpInfo

> ApiResponse<ListImessageSenderOrders200Response> listImessageSenderOrders listImessageSenderOrdersWithHttpInfo(includeCanceled)

List iMessage sender orders

Every sender lifecycle doc your team owns (ordered or registered), across statuses. Canceled senders are omitted unless &#x60;includeCanceled&#x3D;true&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        Boolean includeCanceled = false; // Boolean | 
        try {
            ApiResponse<ListImessageSenderOrders200Response> response = apiInstance.listImessageSenderOrdersWithHttpInfo(includeCanceled);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageSenderOrders");
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
| **includeCanceled** | **Boolean**|  | [optional] [default to false] |

### Return type

ApiResponse<[**ListImessageSenderOrders200Response**](ListImessageSenderOrders200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender lifecycle docs, newest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |


## listImessageSenders

> ListImessageSenders200Response listImessageSenders()

List iMessage senders

Lists the iMessage senders registered across your accessible profiles.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        try {
            ListImessageSenders200Response result = apiInstance.listImessageSenders();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageSenders");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListImessageSenders200Response**](ListImessageSenders200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registered iMessage senders |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |

## listImessageSendersWithHttpInfo

> ApiResponse<ListImessageSenders200Response> listImessageSenders listImessageSendersWithHttpInfo()

List iMessage senders

Lists the iMessage senders registered across your accessible profiles.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        try {
            ApiResponse<ListImessageSenders200Response> response = apiInstance.listImessageSendersWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#listImessageSenders");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

ApiResponse<[**ListImessageSenders200Response**](ListImessageSenders200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registered iMessage senders |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |


## orderImessageSender

> OrderImessageSender202Response orderImessageSender(orderImessageSenderRequest)

Order a new iMessage sender

Orders a NEW dedicated iMessage sender from the delivery provider (compare with POST /v1/imessage/senders, which registers a sender you already own). Activation is asynchronous (minutes to a few hours): the response is 202 with the lifecycle object; poll GET /v1/imessage/senders/{senderId} or subscribe to the account.connected webhook. Billing starts at activation (monthly per sender, no proration). Requires usage-based billing and a valid payment method. Pass purchaseIntentId to make retries idempotent — the provider-side order is never retried automatically. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        OrderImessageSenderRequest orderImessageSenderRequest = new OrderImessageSenderRequest(); // OrderImessageSenderRequest | 
        try {
            OrderImessageSender202Response result = apiInstance.orderImessageSender(orderImessageSenderRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#orderImessageSender");
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
| **orderImessageSenderRequest** | [**OrderImessageSenderRequest**](OrderImessageSenderRequest.md)|  | |

### Return type

[**OrderImessageSender202Response**](OrderImessageSender202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Order accepted; activation continues asynchronously |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | A valid payment method is required (code: payment_method_required) |  -  |
| **403** | Sender limit reached (code: imessage_sender_limit), or iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Profile not found or access denied |  -  |
| **409** | This profile already has a live iMessage sender (code: imessage_sender_conflict) |  -  |
| **422** | Workspace is not on usage-based billing (code: usage_billing_required) |  -  |
| **502** | The provider rejected the order; nothing was charged |  -  |

## orderImessageSenderWithHttpInfo

> ApiResponse<OrderImessageSender202Response> orderImessageSender orderImessageSenderWithHttpInfo(orderImessageSenderRequest)

Order a new iMessage sender

Orders a NEW dedicated iMessage sender from the delivery provider (compare with POST /v1/imessage/senders, which registers a sender you already own). Activation is asynchronous (minutes to a few hours): the response is 202 with the lifecycle object; poll GET /v1/imessage/senders/{senderId} or subscribe to the account.connected webhook. Billing starts at activation (monthly per sender, no proration). Requires usage-based billing and a valid payment method. Pass purchaseIntentId to make retries idempotent — the provider-side order is never retried automatically. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        OrderImessageSenderRequest orderImessageSenderRequest = new OrderImessageSenderRequest(); // OrderImessageSenderRequest | 
        try {
            ApiResponse<OrderImessageSender202Response> response = apiInstance.orderImessageSenderWithHttpInfo(orderImessageSenderRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#orderImessageSender");
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
| **orderImessageSenderRequest** | [**OrderImessageSenderRequest**](OrderImessageSenderRequest.md)|  | |

### Return type

ApiResponse<[**OrderImessageSender202Response**](OrderImessageSender202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Order accepted; activation continues asynchronously |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **402** | A valid payment method is required (code: payment_method_required) |  -  |
| **403** | Sender limit reached (code: imessage_sender_limit), or iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Profile not found or access denied |  -  |
| **409** | This profile already has a live iMessage sender (code: imessage_sender_conflict) |  -  |
| **422** | Workspace is not on usage-based billing (code: usage_billing_required) |  -  |
| **502** | The provider rejected the order; nothing was charged |  -  |


## registerImessageSender

> RegisterImessageSender200Response registerImessageSender(registerImessageSenderRequest)

Register an iMessage sender

Registers a provider-provisioned iMessage sender (a phone number or an email handle) that YOU already own on a profile, creating an &#x60;imessage&#x60; account that sends and receives through the inbox conversation endpoints. To have Zernio order a new sender for you, use POST /v1/imessage/senders/order instead. Registration attaches the monthly sender fee (billed while active) and requires a payment method (402 without one). One sender per profile: re-registering the SAME handle refreshes it; a different handle returns 409 until the existing sender is canceled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        RegisterImessageSenderRequest registerImessageSenderRequest = new RegisterImessageSenderRequest(); // RegisterImessageSenderRequest | 
        try {
            RegisterImessageSender200Response result = apiInstance.registerImessageSender(registerImessageSenderRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#registerImessageSender");
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
| **registerImessageSenderRequest** | [**RegisterImessageSenderRequest**](RegisterImessageSenderRequest.md)|  | |

### Return type

[**RegisterImessageSender200Response**](RegisterImessageSender200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender registered |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **402** | Payment method or plan upgrade required to connect another account |  -  |
| **404** | Profile not found or access denied |  -  |
| **409** | Sender already registered to another profile (code: imessage_sender_conflict) |  -  |

## registerImessageSenderWithHttpInfo

> ApiResponse<RegisterImessageSender200Response> registerImessageSender registerImessageSenderWithHttpInfo(registerImessageSenderRequest)

Register an iMessage sender

Registers a provider-provisioned iMessage sender (a phone number or an email handle) that YOU already own on a profile, creating an &#x60;imessage&#x60; account that sends and receives through the inbox conversation endpoints. To have Zernio order a new sender for you, use POST /v1/imessage/senders/order instead. Registration attaches the monthly sender fee (billed while active) and requires a payment method (402 without one). One sender per profile: re-registering the SAME handle refreshes it; a different handle returns 409 until the existing sender is canceled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        RegisterImessageSenderRequest registerImessageSenderRequest = new RegisterImessageSenderRequest(); // RegisterImessageSenderRequest | 
        try {
            ApiResponse<RegisterImessageSender200Response> response = apiInstance.registerImessageSenderWithHttpInfo(registerImessageSenderRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#registerImessageSender");
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
| **registerImessageSenderRequest** | [**RegisterImessageSenderRequest**](RegisterImessageSenderRequest.md)|  | |

### Return type

ApiResponse<[**RegisterImessageSender200Response**](RegisterImessageSender200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender registered |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **402** | Payment method or plan upgrade required to connect another account |  -  |
| **404** | Profile not found or access denied |  -  |
| **409** | Sender already registered to another profile (code: imessage_sender_conflict) |  -  |


## removeImessageGroupParticipant

> AddImessageGroupParticipant200Response removeImessageGroupParticipant(conversationId, accountId, contact)

Remove a participant from an iMessage group

Applied asynchronously by the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String contact = "contact_example"; // String | E.164 phone or iMessage email
        try {
            AddImessageGroupParticipant200Response result = apiInstance.removeImessageGroupParticipant(conversationId, accountId, contact);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#removeImessageGroupParticipant");
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
| **conversationId** | **String**|  | |
| **accountId** | **String**|  | |
| **contact** | **String**| E.164 phone or iMessage email | |

### Return type

[**AddImessageGroupParticipant200Response**](AddImessageGroupParticipant200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change accepted |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |

## removeImessageGroupParticipantWithHttpInfo

> ApiResponse<AddImessageGroupParticipant200Response> removeImessageGroupParticipant removeImessageGroupParticipantWithHttpInfo(conversationId, accountId, contact)

Remove a participant from an iMessage group

Applied asynchronously by the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String contact = "contact_example"; // String | E.164 phone or iMessage email
        try {
            ApiResponse<AddImessageGroupParticipant200Response> response = apiInstance.removeImessageGroupParticipantWithHttpInfo(conversationId, accountId, contact);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#removeImessageGroupParticipant");
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
| **conversationId** | **String**|  | |
| **accountId** | **String**|  | |
| **contact** | **String**| E.164 phone or iMessage email | |

### Return type

ApiResponse<[**AddImessageGroupParticipant200Response**](AddImessageGroupParticipant200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change accepted |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |


## reserveImessageAvailableNumber

> ReserveImessageAvailableNumber200Response reserveImessageAvailableNumber(numberId)

Reserve an available iMessage number

Holds the number for 3 minutes so nobody else can order it while the buyer decides. Place the order (POST /v1/imessage/senders/order with availableNumberId) before the hold expires. No request body.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String numberId = "numberId_example"; // String | 
        try {
            ReserveImessageAvailableNumber200Response result = apiInstance.reserveImessageAvailableNumber(numberId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#reserveImessageAvailableNumber");
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
| **numberId** | **String**|  | |

### Return type

[**ReserveImessageAvailableNumber200Response**](ReserveImessageAvailableNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number reserved |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **409** | The number could not be reserved (already taken) |  -  |

## reserveImessageAvailableNumberWithHttpInfo

> ApiResponse<ReserveImessageAvailableNumber200Response> reserveImessageAvailableNumber reserveImessageAvailableNumberWithHttpInfo(numberId)

Reserve an available iMessage number

Holds the number for 3 minutes so nobody else can order it while the buyer decides. Place the order (POST /v1/imessage/senders/order with availableNumberId) before the hold expires. No request body.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String numberId = "numberId_example"; // String | 
        try {
            ApiResponse<ReserveImessageAvailableNumber200Response> response = apiInstance.reserveImessageAvailableNumberWithHttpInfo(numberId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#reserveImessageAvailableNumber");
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
| **numberId** | **String**|  | |

### Return type

ApiResponse<[**ReserveImessageAvailableNumber200Response**](ReserveImessageAvailableNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number reserved |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **409** | The number could not be reserved (already taken) |  -  |


## setImessageSubscription

> SetImessageSubscription200Response setImessageSubscription(setImessageSubscriptionRequest)

Subscribe or opt out an iMessage contact

Opted-out contacts are refused at send time (409 recipient_opted_out) until re-subscribed. Their inbound messages still arrive. Scoped to your account: it does not change the contact&#39;s state with other businesses.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        SetImessageSubscriptionRequest setImessageSubscriptionRequest = new SetImessageSubscriptionRequest(); // SetImessageSubscriptionRequest | 
        try {
            SetImessageSubscription200Response result = apiInstance.setImessageSubscription(setImessageSubscriptionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#setImessageSubscription");
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
| **setImessageSubscriptionRequest** | [**SetImessageSubscriptionRequest**](SetImessageSubscriptionRequest.md)|  | |

### Return type

[**SetImessageSubscription200Response**](SetImessageSubscription200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |

## setImessageSubscriptionWithHttpInfo

> ApiResponse<SetImessageSubscription200Response> setImessageSubscription setImessageSubscriptionWithHttpInfo(setImessageSubscriptionRequest)

Subscribe or opt out an iMessage contact

Opted-out contacts are refused at send time (409 recipient_opted_out) until re-subscribed. Their inbound messages still arrive. Scoped to your account: it does not change the contact&#39;s state with other businesses.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        SetImessageSubscriptionRequest setImessageSubscriptionRequest = new SetImessageSubscriptionRequest(); // SetImessageSubscriptionRequest | 
        try {
            ApiResponse<SetImessageSubscription200Response> response = apiInstance.setImessageSubscriptionWithHttpInfo(setImessageSubscriptionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#setImessageSubscription");
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
| **setImessageSubscriptionRequest** | [**SetImessageSubscriptionRequest**](SetImessageSubscriptionRequest.md)|  | |

### Return type

ApiResponse<[**SetImessageSubscription200Response**](SetImessageSubscription200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |


## updateImessageGroup

> UpdateImessageGroup200Response updateImessageGroup(conversationId, updateImessageGroupRequest)

Rename an iMessage group or change its photo

One change per call: either &#x60;name&#x60; or &#x60;photoUrl&#x60; (an empty &#x60;photoUrl&#x60; removes the photo). Applied asynchronously by the provider; a rename is mirrored on the inbox conversation right away.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | 
        UpdateImessageGroupRequest updateImessageGroupRequest = new UpdateImessageGroupRequest(); // UpdateImessageGroupRequest | 
        try {
            UpdateImessageGroup200Response result = apiInstance.updateImessageGroup(conversationId, updateImessageGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#updateImessageGroup");
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
| **conversationId** | **String**|  | |
| **updateImessageGroupRequest** | [**UpdateImessageGroupRequest**](UpdateImessageGroupRequest.md)|  | |

### Return type

[**UpdateImessageGroup200Response**](UpdateImessageGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change accepted |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |

## updateImessageGroupWithHttpInfo

> ApiResponse<UpdateImessageGroup200Response> updateImessageGroup updateImessageGroupWithHttpInfo(conversationId, updateImessageGroupRequest)

Rename an iMessage group or change its photo

One change per call: either &#x60;name&#x60; or &#x60;photoUrl&#x60; (an empty &#x60;photoUrl&#x60; removes the photo). Applied asynchronously by the provider; a rename is mirrored on the inbox conversation right away.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String conversationId = "conversationId_example"; // String | 
        UpdateImessageGroupRequest updateImessageGroupRequest = new UpdateImessageGroupRequest(); // UpdateImessageGroupRequest | 
        try {
            ApiResponse<UpdateImessageGroup200Response> response = apiInstance.updateImessageGroupWithHttpInfo(conversationId, updateImessageGroupRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#updateImessageGroup");
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
| **conversationId** | **String**|  | |
| **updateImessageGroupRequest** | [**UpdateImessageGroupRequest**](UpdateImessageGroupRequest.md)|  | |

### Return type

ApiResponse<[**UpdateImessageGroup200Response**](UpdateImessageGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change accepted |  -  |
| **400** | Bad request, or the conversation is not a group thread |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Account or conversation not found |  -  |


## updateImessageSender

> OrderImessageSender202Response updateImessageSender(senderId, updateImessageSenderRequest)

Update an iMessage sender

Display name (inbox and API responses) and the contact card (vCard) recipients see when they save the sender. The contact card is what a contactCard send shares.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        UpdateImessageSenderRequest updateImessageSenderRequest = new UpdateImessageSenderRequest(); // UpdateImessageSenderRequest | 
        try {
            OrderImessageSender202Response result = apiInstance.updateImessageSender(senderId, updateImessageSenderRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#updateImessageSender");
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
| **senderId** | **String**|  | |
| **updateImessageSenderRequest** | [**UpdateImessageSenderRequest**](UpdateImessageSenderRequest.md)|  | |

### Return type

[**OrderImessageSender202Response**](OrderImessageSender202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |

## updateImessageSenderWithHttpInfo

> ApiResponse<OrderImessageSender202Response> updateImessageSender updateImessageSenderWithHttpInfo(senderId, updateImessageSenderRequest)

Update an iMessage sender

Display name (inbox and API responses) and the contact card (vCard) recipients see when they save the sender. The contact card is what a contactCard send shares.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.IMessageApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        IMessageApi apiInstance = new IMessageApi(defaultClient);
        String senderId = "senderId_example"; // String | 
        UpdateImessageSenderRequest updateImessageSenderRequest = new UpdateImessageSenderRequest(); // UpdateImessageSenderRequest | 
        try {
            ApiResponse<OrderImessageSender202Response> response = apiInstance.updateImessageSenderWithHttpInfo(senderId, updateImessageSenderRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling IMessageApi#updateImessageSender");
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
| **senderId** | **String**|  | |
| **updateImessageSenderRequest** | [**UpdateImessageSenderRequest**](UpdateImessageSenderRequest.md)|  | |

### Return type

ApiResponse<[**OrderImessageSender202Response**](OrderImessageSender202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sender updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | iMessage is in private beta and not enabled for this account (code: PLATFORM_BETA_RESTRICTED) |  -  |
| **404** | Sender not found |  -  |

