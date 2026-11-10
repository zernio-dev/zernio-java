# EmailApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelScheduledEmail**](EmailApi.md#cancelScheduledEmail) | **DELETE** /v1/email/messages/scheduled/{scheduleId} | Cancel a scheduled email |
| [**cancelScheduledEmailWithHttpInfo**](EmailApi.md#cancelScheduledEmailWithHttpInfo) | **DELETE** /v1/email/messages/scheduled/{scheduleId} | Cancel a scheduled email |
| [**createEmailLabel**](EmailApi.md#createEmailLabel) | **POST** /v1/email/labels | Create a label |
| [**createEmailLabelWithHttpInfo**](EmailApi.md#createEmailLabelWithHttpInfo) | **POST** /v1/email/labels | Create a label |
| [**deleteEmailLabel**](EmailApi.md#deleteEmailLabel) | **DELETE** /v1/email/labels/{labelId} | Delete a label |
| [**deleteEmailLabelWithHttpInfo**](EmailApi.md#deleteEmailLabelWithHttpInfo) | **DELETE** /v1/email/labels/{labelId} | Delete a label |
| [**downloadEmailAttachment**](EmailApi.md#downloadEmailAttachment) | **GET** /v1/email/attachments/{attachmentId} | Download an attachment |
| [**downloadEmailAttachmentWithHttpInfo**](EmailApi.md#downloadEmailAttachmentWithHttpInfo) | **GET** /v1/email/attachments/{attachmentId} | Download an attachment |
| [**getEmailMessage**](EmailApi.md#getEmailMessage) | **GET** /v1/email/messages/{messageId} | Get an email message |
| [**getEmailMessageWithHttpInfo**](EmailApi.md#getEmailMessageWithHttpInfo) | **GET** /v1/email/messages/{messageId} | Get an email message |
| [**getEmailThread**](EmailApi.md#getEmailThread) | **GET** /v1/email/threads/{threadId} | Get an email thread with its messages |
| [**getEmailThreadWithHttpInfo**](EmailApi.md#getEmailThreadWithHttpInfo) | **GET** /v1/email/threads/{threadId} | Get an email thread with its messages |
| [**getScheduledEmail**](EmailApi.md#getScheduledEmail) | **GET** /v1/email/messages/scheduled/{scheduleId} | Get a scheduled email |
| [**getScheduledEmailWithHttpInfo**](EmailApi.md#getScheduledEmailWithHttpInfo) | **GET** /v1/email/messages/scheduled/{scheduleId} | Get a scheduled email |
| [**listEmailFolders**](EmailApi.md#listEmailFolders) | **GET** /v1/email/folders | List mailbox folders |
| [**listEmailFoldersWithHttpInfo**](EmailApi.md#listEmailFoldersWithHttpInfo) | **GET** /v1/email/folders | List mailbox folders |
| [**listEmailLabels**](EmailApi.md#listEmailLabels) | **GET** /v1/email/labels | List labels |
| [**listEmailLabelsWithHttpInfo**](EmailApi.md#listEmailLabelsWithHttpInfo) | **GET** /v1/email/labels | List labels |
| [**listEmailMessages**](EmailApi.md#listEmailMessages) | **GET** /v1/email/messages | List email messages |
| [**listEmailMessagesWithHttpInfo**](EmailApi.md#listEmailMessagesWithHttpInfo) | **GET** /v1/email/messages | List email messages |
| [**listEmailSendAs**](EmailApi.md#listEmailSendAs) | **GET** /v1/email/send-as | List send-as addresses |
| [**listEmailSendAsWithHttpInfo**](EmailApi.md#listEmailSendAsWithHttpInfo) | **GET** /v1/email/send-as | List send-as addresses |
| [**listEmailThreads**](EmailApi.md#listEmailThreads) | **GET** /v1/email/threads | List email threads |
| [**listEmailThreadsWithHttpInfo**](EmailApi.md#listEmailThreadsWithHttpInfo) | **GET** /v1/email/threads | List email threads |
| [**listScheduledEmails**](EmailApi.md#listScheduledEmails) | **GET** /v1/email/messages/scheduled | List scheduled emails |
| [**listScheduledEmailsWithHttpInfo**](EmailApi.md#listScheduledEmailsWithHttpInfo) | **GET** /v1/email/messages/scheduled | List scheduled emails |
| [**replyEmailMessage**](EmailApi.md#replyEmailMessage) | **POST** /v1/email/messages/{messageId}/reply | Reply to a message |
| [**replyEmailMessageWithHttpInfo**](EmailApi.md#replyEmailMessageWithHttpInfo) | **POST** /v1/email/messages/{messageId}/reply | Reply to a message |
| [**sendEmailMessage**](EmailApi.md#sendEmailMessage) | **POST** /v1/email/messages | Send an email |
| [**sendEmailMessageWithHttpInfo**](EmailApi.md#sendEmailMessageWithHttpInfo) | **POST** /v1/email/messages | Send an email |
| [**trashEmailMessage**](EmailApi.md#trashEmailMessage) | **DELETE** /v1/email/messages/{messageId} | Move a message to trash |
| [**trashEmailMessageWithHttpInfo**](EmailApi.md#trashEmailMessageWithHttpInfo) | **DELETE** /v1/email/messages/{messageId} | Move a message to trash |
| [**updateEmailMessage**](EmailApi.md#updateEmailMessage) | **PATCH** /v1/email/messages/{messageId} | Mark read or starred, label, or move a message |
| [**updateEmailMessageWithHttpInfo**](EmailApi.md#updateEmailMessageWithHttpInfo) | **PATCH** /v1/email/messages/{messageId} | Mark read or starred, label, or move a message |
| [**updateEmailThread**](EmailApi.md#updateEmailThread) | **PATCH** /v1/email/threads/{threadId} | Update every message in a thread |
| [**updateEmailThreadWithHttpInfo**](EmailApi.md#updateEmailThreadWithHttpInfo) | **PATCH** /v1/email/threads/{threadId} | Update every message in a thread |



## cancelScheduledEmail

> SendEmailMessage202Response cancelScheduledEmail(scheduleId, accountId)

Cancel a scheduled email

Cancels a send still waiting for its time and returns it with &#x60;status: cancelled&#x60;. One that is sending, sent or failed answers 409.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String scheduleId = "scheduleId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            SendEmailMessage202Response result = apiInstance.cancelScheduledEmail(scheduleId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#cancelScheduledEmail");
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
| **scheduleId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**SendEmailMessage202Response**](SendEmailMessage202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cancelled email |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | The send already left, failed or was cancelled; the message names its status. |  -  |

## cancelScheduledEmailWithHttpInfo

> ApiResponse<SendEmailMessage202Response> cancelScheduledEmail cancelScheduledEmailWithHttpInfo(scheduleId, accountId)

Cancel a scheduled email

Cancels a send still waiting for its time and returns it with &#x60;status: cancelled&#x60;. One that is sending, sent or failed answers 409.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String scheduleId = "scheduleId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<SendEmailMessage202Response> response = apiInstance.cancelScheduledEmailWithHttpInfo(scheduleId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#cancelScheduledEmail");
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
| **scheduleId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**SendEmailMessage202Response**](SendEmailMessage202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cancelled email |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | The send already left, failed or was cancelled; the message names its status. |  -  |


## createEmailLabel

> CreateEmailLabel200Response createEmailLabel(createEmailLabelRequest)

Create a label

Creates a Gmail label or an Outlook category. Safe to repeat: when the name already exists (case-insensitive) the existing label comes back with 200.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        CreateEmailLabelRequest createEmailLabelRequest = new CreateEmailLabelRequest(); // CreateEmailLabelRequest | 
        try {
            CreateEmailLabel200Response result = apiInstance.createEmailLabel(createEmailLabelRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createEmailLabel");
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
| **createEmailLabelRequest** | [**CreateEmailLabelRequest**](CreateEmailLabelRequest.md)|  | |

### Return type

[**CreateEmailLabel200Response**](CreateEmailLabel200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A label with this name already existed |  -  |
| **201** | The label was created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## createEmailLabelWithHttpInfo

> ApiResponse<CreateEmailLabel200Response> createEmailLabel createEmailLabelWithHttpInfo(createEmailLabelRequest)

Create a label

Creates a Gmail label or an Outlook category. Safe to repeat: when the name already exists (case-insensitive) the existing label comes back with 200.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        CreateEmailLabelRequest createEmailLabelRequest = new CreateEmailLabelRequest(); // CreateEmailLabelRequest | 
        try {
            ApiResponse<CreateEmailLabel200Response> response = apiInstance.createEmailLabelWithHttpInfo(createEmailLabelRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createEmailLabel");
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
| **createEmailLabelRequest** | [**CreateEmailLabelRequest**](CreateEmailLabelRequest.md)|  | |

### Return type

ApiResponse<[**CreateEmailLabel200Response**](CreateEmailLabel200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A label with this name already existed |  -  |
| **201** | The label was created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## deleteEmailLabel

> DeleteEmailLabel200Response deleteEmailLabel(labelId, accountId)

Delete a label

Deletes a Gmail user label or an Outlook category, by id or name (URL-encode a slash). Gmail removes the label from every message. Outlook keeps a deleted category on messages that already carry it; 412 when the organization blocks the category list.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String labelId = "labelId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            DeleteEmailLabel200Response result = apiInstance.deleteEmailLabel(labelId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailLabel");
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
| **labelId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**DeleteEmailLabel200Response**](DeleteEmailLabel200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The label was deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## deleteEmailLabelWithHttpInfo

> ApiResponse<DeleteEmailLabel200Response> deleteEmailLabel deleteEmailLabelWithHttpInfo(labelId, accountId)

Delete a label

Deletes a Gmail user label or an Outlook category, by id or name (URL-encode a slash). Gmail removes the label from every message. Outlook keeps a deleted category on messages that already carry it; 412 when the organization blocks the category list.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String labelId = "labelId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<DeleteEmailLabel200Response> response = apiInstance.deleteEmailLabelWithHttpInfo(labelId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailLabel");
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
| **labelId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**DeleteEmailLabel200Response**](DeleteEmailLabel200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The label was deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## downloadEmailAttachment

> File downloadEmailAttachment(attachmentId, accountId, messageId)

Download an attachment

Streams the attachment bytes with its &#x60;Content-Type&#x60; and a &#x60;Content-Disposition&#x60; carrying the filename.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String attachmentId = "attachmentId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String messageId = "messageId_example"; // String | 
        try {
            File result = apiInstance.downloadEmailAttachment(attachmentId, accountId, messageId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#downloadEmailAttachment");
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
| **attachmentId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **messageId** | **String**|  | |

### Return type

[**File**](File.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The attachment bytes |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## downloadEmailAttachmentWithHttpInfo

> ApiResponse<File> downloadEmailAttachment downloadEmailAttachmentWithHttpInfo(attachmentId, accountId, messageId)

Download an attachment

Streams the attachment bytes with its &#x60;Content-Type&#x60; and a &#x60;Content-Disposition&#x60; carrying the filename.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String attachmentId = "attachmentId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String messageId = "messageId_example"; // String | 
        try {
            ApiResponse<File> response = apiInstance.downloadEmailAttachmentWithHttpInfo(attachmentId, accountId, messageId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#downloadEmailAttachment");
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
| **attachmentId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **messageId** | **String**|  | |

### Return type

ApiResponse<[**File**](File.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The attachment bytes |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## getEmailMessage

> SendEmailMessage201Response getEmailMessage(messageId, accountId, includeHeaders, raw)

Get an email message

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        Boolean includeHeaders = false; // Boolean | Include the raw internet headers under `headers`.
        Boolean raw = false; // Boolean | Include the MIME source under `raw`.
        try {
            SendEmailMessage201Response result = apiInstance.getEmailMessage(messageId, accountId, includeHeaders, raw);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailMessage");
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
| **messageId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **includeHeaders** | **Boolean**| Include the raw internet headers under &#x60;headers&#x60;. | [optional] [default to false] |
| **raw** | **Boolean**| Include the MIME source under &#x60;raw&#x60;. | [optional] [default to false] |

### Return type

[**SendEmailMessage201Response**](SendEmailMessage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The message with its bodies |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## getEmailMessageWithHttpInfo

> ApiResponse<SendEmailMessage201Response> getEmailMessage getEmailMessageWithHttpInfo(messageId, accountId, includeHeaders, raw)

Get an email message

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        Boolean includeHeaders = false; // Boolean | Include the raw internet headers under `headers`.
        Boolean raw = false; // Boolean | Include the MIME source under `raw`.
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.getEmailMessageWithHttpInfo(messageId, accountId, includeHeaders, raw);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailMessage");
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
| **messageId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **includeHeaders** | **Boolean**| Include the raw internet headers under &#x60;headers&#x60;. | [optional] [default to false] |
| **raw** | **Boolean**| Include the MIME source under &#x60;raw&#x60;. | [optional] [default to false] |

### Return type

ApiResponse<[**SendEmailMessage201Response**](SendEmailMessage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The message with its bodies |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## getEmailThread

> GetEmailThread200Response getEmailThread(threadId, accountId)

Get an email thread with its messages

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String threadId = "threadId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            GetEmailThread200Response result = apiInstance.getEmailThread(threadId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailThread");
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
| **threadId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**GetEmailThread200Response**](GetEmailThread200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thread and every message in it, oldest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## getEmailThreadWithHttpInfo

> ApiResponse<GetEmailThread200Response> getEmailThread getEmailThreadWithHttpInfo(threadId, accountId)

Get an email thread with its messages

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String threadId = "threadId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<GetEmailThread200Response> response = apiInstance.getEmailThreadWithHttpInfo(threadId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailThread");
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
| **threadId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**GetEmailThread200Response**](GetEmailThread200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The thread and every message in it, oldest first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## getScheduledEmail

> SendEmailMessage202Response getScheduledEmail(scheduleId, accountId)

Get a scheduled email

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String scheduleId = "scheduleId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            SendEmailMessage202Response result = apiInstance.getScheduledEmail(scheduleId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getScheduledEmail");
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
| **scheduleId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**SendEmailMessage202Response**](SendEmailMessage202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The scheduled email |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getScheduledEmailWithHttpInfo

> ApiResponse<SendEmailMessage202Response> getScheduledEmail getScheduledEmailWithHttpInfo(scheduleId, accountId)

Get a scheduled email

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String scheduleId = "scheduleId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<SendEmailMessage202Response> response = apiInstance.getScheduledEmailWithHttpInfo(scheduleId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getScheduledEmail");
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
| **scheduleId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**SendEmailMessage202Response**](SendEmailMessage202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The scheduled email |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## listEmailFolders

> ListEmailFolders200Response listEmailFolders(accountId)

List mailbox folders

On Google, folders are Gmail labels (system labels carry &#x60;wellKnown&#x60;; &#x60;unreadCount&#x60; and &#x60;totalCount&#x60; are present only where Gmail reports them). There is no archive folder on Google; archived mail is listed with &#x60;folder&#x3D;archive&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ListEmailFolders200Response result = apiInstance.listEmailFolders(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailFolders");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**ListEmailFolders200Response**](ListEmailFolders200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Folders, with &#x60;wellKnown&#x60; set on the provider&#39;s system folders |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## listEmailFoldersWithHttpInfo

> ApiResponse<ListEmailFolders200Response> listEmailFolders listEmailFoldersWithHttpInfo(accountId)

List mailbox folders

On Google, folders are Gmail labels (system labels carry &#x60;wellKnown&#x60;; &#x60;unreadCount&#x60; and &#x60;totalCount&#x60; are present only where Gmail reports them). There is no archive folder on Google; archived mail is listed with &#x60;folder&#x3D;archive&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<ListEmailFolders200Response> response = apiInstance.listEmailFoldersWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailFolders");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**ListEmailFolders200Response**](ListEmailFolders200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Folders, with &#x60;wellKnown&#x60; set on the provider&#39;s system folders |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## listEmailLabels

> ListEmailLabels200Response listEmailLabels(accountId)

List labels

Gmail labels, system and user, or the Outlook category list. If an organization blocks reading the Outlook list, it comes back empty and categories still apply to messages by name.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ListEmailLabels200Response result = apiInstance.listEmailLabels(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailLabels");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**ListEmailLabels200Response**](ListEmailLabels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The mailbox&#39;s labels |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## listEmailLabelsWithHttpInfo

> ApiResponse<ListEmailLabels200Response> listEmailLabels listEmailLabelsWithHttpInfo(accountId)

List labels

Gmail labels, system and user, or the Outlook category list. If an organization blocks reading the Outlook list, it comes back empty and categories still apply to messages by name.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<ListEmailLabels200Response> response = apiInstance.listEmailLabelsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailLabels");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**ListEmailLabels200Response**](ListEmailLabels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The mailbox&#39;s labels |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## listEmailMessages

> ListEmailMessages200Response listEmailMessages(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit)

List email messages

Same filters and envelope as &#x60;GET /v1/email/threads&#x60;, one row per message. Bodies are omitted; fetch a message to read &#x60;text&#x60; and &#x60;html&#x60;.  ### On Google  - List rows also omit &#x60;attachments&#x60; (Gmail&#39;s metadata pages carry headers only); &#x60;hasAttachment&#x3D;true&#x60; still filters server-side. - &#x60;sortOrder&#x3D;asc&#x60; reverses the fetched page. - &#x60;archive&#x60; means mail without the inbox, trash or spam labels. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String folder = "folder_example"; // String | 
        Boolean unread = true; // Boolean | 
        Boolean starred = true; // Boolean | 
        Boolean hasAttachment = true; // Boolean | 
        String subject = "subject_example"; // String | 
        String from = "from_example"; // String | 
        String to = "to_example"; // String | 
        String cc = "cc_example"; // String | 
        String bcc = "bcc_example"; // String | 
        String anyEmail = "anyEmail_example"; // String | 
        OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
        String searchQueryNative = "searchQueryNative_example"; // String | 
        String sortOrder = "asc"; // String | 
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        try {
            ListEmailMessages200Response result = apiInstance.listEmailMessages(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailMessages");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **folder** | **String**|  | [optional] |
| **unread** | **Boolean**|  | [optional] |
| **starred** | **Boolean**|  | [optional] |
| **hasAttachment** | **Boolean**|  | [optional] |
| **subject** | **String**|  | [optional] |
| **from** | **String**|  | [optional] |
| **to** | **String**|  | [optional] |
| **cc** | **String**|  | [optional] |
| **bcc** | **String**|  | [optional] |
| **anyEmail** | **String**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **searchQueryNative** | **String**|  | [optional] |
| **sortOrder** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**ListEmailMessages200Response**](ListEmailMessages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Messages |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |

## listEmailMessagesWithHttpInfo

> ApiResponse<ListEmailMessages200Response> listEmailMessages listEmailMessagesWithHttpInfo(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit)

List email messages

Same filters and envelope as &#x60;GET /v1/email/threads&#x60;, one row per message. Bodies are omitted; fetch a message to read &#x60;text&#x60; and &#x60;html&#x60;.  ### On Google  - List rows also omit &#x60;attachments&#x60; (Gmail&#39;s metadata pages carry headers only); &#x60;hasAttachment&#x3D;true&#x60; still filters server-side. - &#x60;sortOrder&#x3D;asc&#x60; reverses the fetched page. - &#x60;archive&#x60; means mail without the inbox, trash or spam labels. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String folder = "folder_example"; // String | 
        Boolean unread = true; // Boolean | 
        Boolean starred = true; // Boolean | 
        Boolean hasAttachment = true; // Boolean | 
        String subject = "subject_example"; // String | 
        String from = "from_example"; // String | 
        String to = "to_example"; // String | 
        String cc = "cc_example"; // String | 
        String bcc = "bcc_example"; // String | 
        String anyEmail = "anyEmail_example"; // String | 
        OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
        String searchQueryNative = "searchQueryNative_example"; // String | 
        String sortOrder = "asc"; // String | 
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        try {
            ApiResponse<ListEmailMessages200Response> response = apiInstance.listEmailMessagesWithHttpInfo(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailMessages");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **folder** | **String**|  | [optional] |
| **unread** | **Boolean**|  | [optional] |
| **starred** | **Boolean**|  | [optional] |
| **hasAttachment** | **Boolean**|  | [optional] |
| **subject** | **String**|  | [optional] |
| **from** | **String**|  | [optional] |
| **to** | **String**|  | [optional] |
| **cc** | **String**|  | [optional] |
| **bcc** | **String**|  | [optional] |
| **anyEmail** | **String**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **searchQueryNative** | **String**|  | [optional] |
| **sortOrder** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

ApiResponse<[**ListEmailMessages200Response**](ListEmailMessages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Messages |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |


## listEmailSendAs

> ListEmailSendAs200Response listEmailSendAs(accountId)

List send-as addresses

The addresses a mailbox can send from, for the &#x60;from&#x60; field of a send or reply. Gmail lists every send-as alias with its signature, and &#x60;from&#x60; must be one of them. Outlook lists the mailbox address and its aliases; Exchange checks any other &#x60;from&#x60; at send time.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ListEmailSendAs200Response result = apiInstance.listEmailSendAs(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailSendAs");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**ListEmailSendAs200Response**](ListEmailSendAs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The mailbox&#39;s send-as addresses, the mailbox address first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## listEmailSendAsWithHttpInfo

> ApiResponse<ListEmailSendAs200Response> listEmailSendAs listEmailSendAsWithHttpInfo(accountId)

List send-as addresses

The addresses a mailbox can send from, for the &#x60;from&#x60; field of a send or reply. Gmail lists every send-as alias with its signature, and &#x60;from&#x60; must be one of them. Outlook lists the mailbox address and its aliases; Exchange checks any other &#x60;from&#x60; at send time.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<ListEmailSendAs200Response> response = apiInstance.listEmailSendAsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailSendAs");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**ListEmailSendAs200Response**](ListEmailSendAs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The mailbox&#39;s send-as addresses, the mailbox address first |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## listEmailThreads

> ListEmailThreads200Response listEmailThreads(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit)

List email threads

Threads of a connected Google or Microsoft mailbox, newest first. Every filter that the provider cannot apply server-side is applied to the fetched page instead and named in &#x60;meta.filteredClientSide&#x60;, so a filtered page can hold fewer than &#x60;limit&#x60; items while &#x60;pagination.hasMore&#x60; stays true.  On Google, folders are Gmail labels: &#x60;folder&#x60; takes a well-known name or a label id, &#x60;archive&#x60; means mail carrying none of the inbox, trash or spam labels, and &#x60;sortOrder&#x3D;asc&#x60; reverses the fetched page (Gmail lists newest first only).  The account must have been connected with &#x60;scopes&#x3D;email&#x60; (412 &#x60;account_scope_missing&#x60; otherwise). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String folder = "folder_example"; // String | Well-known folder (`inbox`, `sent`, `drafts`, `trash`, `spam`, `archive`) or a provider folder id from `GET /v1/email/folders`. Default inbox.
        Boolean unread = true; // Boolean | 
        Boolean starred = true; // Boolean | 
        Boolean hasAttachment = true; // Boolean | 
        String subject = "subject_example"; // String | Substring match on the subject.
        String from = "from_example"; // String | Sender address.
        String to = "to_example"; // String | A recipient address.
        String cc = "cc_example"; // String | 
        String bcc = "bcc_example"; // String | Applied client-side on Microsoft.
        String anyEmail = "anyEmail_example"; // String | Matches from, to, cc or bcc. Applied client-side on Microsoft.
        OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
        String searchQueryNative = "searchQueryNative_example"; // String | The provider's own search syntax (Gmail search operators, Microsoft KQL). On Microsoft it cannot be combined with other filters or server-side ordering; those are applied to the page.
        String sortOrder = "asc"; // String | 
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        try {
            ListEmailThreads200Response result = apiInstance.listEmailThreads(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailThreads");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **folder** | **String**| Well-known folder (&#x60;inbox&#x60;, &#x60;sent&#x60;, &#x60;drafts&#x60;, &#x60;trash&#x60;, &#x60;spam&#x60;, &#x60;archive&#x60;) or a provider folder id from &#x60;GET /v1/email/folders&#x60;. Default inbox. | [optional] |
| **unread** | **Boolean**|  | [optional] |
| **starred** | **Boolean**|  | [optional] |
| **hasAttachment** | **Boolean**|  | [optional] |
| **subject** | **String**| Substring match on the subject. | [optional] |
| **from** | **String**| Sender address. | [optional] |
| **to** | **String**| A recipient address. | [optional] |
| **cc** | **String**|  | [optional] |
| **bcc** | **String**| Applied client-side on Microsoft. | [optional] |
| **anyEmail** | **String**| Matches from, to, cc or bcc. Applied client-side on Microsoft. | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **searchQueryNative** | **String**| The provider&#39;s own search syntax (Gmail search operators, Microsoft KQL). On Microsoft it cannot be combined with other filters or server-side ordering; those are applied to the page. | [optional] |
| **sortOrder** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**ListEmailThreads200Response**](ListEmailThreads200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Threads |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |

## listEmailThreadsWithHttpInfo

> ApiResponse<ListEmailThreads200Response> listEmailThreads listEmailThreadsWithHttpInfo(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit)

List email threads

Threads of a connected Google or Microsoft mailbox, newest first. Every filter that the provider cannot apply server-side is applied to the fetched page instead and named in &#x60;meta.filteredClientSide&#x60;, so a filtered page can hold fewer than &#x60;limit&#x60; items while &#x60;pagination.hasMore&#x60; stays true.  On Google, folders are Gmail labels: &#x60;folder&#x60; takes a well-known name or a label id, &#x60;archive&#x60; means mail carrying none of the inbox, trash or spam labels, and &#x60;sortOrder&#x3D;asc&#x60; reverses the fetched page (Gmail lists newest first only).  The account must have been connected with &#x60;scopes&#x3D;email&#x60; (412 &#x60;account_scope_missing&#x60; otherwise). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String folder = "folder_example"; // String | Well-known folder (`inbox`, `sent`, `drafts`, `trash`, `spam`, `archive`) or a provider folder id from `GET /v1/email/folders`. Default inbox.
        Boolean unread = true; // Boolean | 
        Boolean starred = true; // Boolean | 
        Boolean hasAttachment = true; // Boolean | 
        String subject = "subject_example"; // String | Substring match on the subject.
        String from = "from_example"; // String | Sender address.
        String to = "to_example"; // String | A recipient address.
        String cc = "cc_example"; // String | 
        String bcc = "bcc_example"; // String | Applied client-side on Microsoft.
        String anyEmail = "anyEmail_example"; // String | Matches from, to, cc or bcc. Applied client-side on Microsoft.
        OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
        String searchQueryNative = "searchQueryNative_example"; // String | The provider's own search syntax (Gmail search operators, Microsoft KQL). On Microsoft it cannot be combined with other filters or server-side ordering; those are applied to the page.
        String sortOrder = "asc"; // String | 
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        try {
            ApiResponse<ListEmailThreads200Response> response = apiInstance.listEmailThreadsWithHttpInfo(accountId, folder, unread, starred, hasAttachment, subject, from, to, cc, bcc, anyEmail, after, before, searchQueryNative, sortOrder, cursor, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailThreads");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **folder** | **String**| Well-known folder (&#x60;inbox&#x60;, &#x60;sent&#x60;, &#x60;drafts&#x60;, &#x60;trash&#x60;, &#x60;spam&#x60;, &#x60;archive&#x60;) or a provider folder id from &#x60;GET /v1/email/folders&#x60;. Default inbox. | [optional] |
| **unread** | **Boolean**|  | [optional] |
| **starred** | **Boolean**|  | [optional] |
| **hasAttachment** | **Boolean**|  | [optional] |
| **subject** | **String**| Substring match on the subject. | [optional] |
| **from** | **String**| Sender address. | [optional] |
| **to** | **String**| A recipient address. | [optional] |
| **cc** | **String**|  | [optional] |
| **bcc** | **String**| Applied client-side on Microsoft. | [optional] |
| **anyEmail** | **String**| Matches from, to, cc or bcc. Applied client-side on Microsoft. | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **searchQueryNative** | **String**| The provider&#39;s own search syntax (Gmail search operators, Microsoft KQL). On Microsoft it cannot be combined with other filters or server-side ordering; those are applied to the page. | [optional] |
| **sortOrder** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

ApiResponse<[**ListEmailThreads200Response**](ListEmailThreads200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Threads |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds until card payments are tried again. <br>  |


## listScheduledEmails

> ListScheduledEmails200Response listScheduledEmails(accountId, status, cursor, limit)

List scheduled emails

Sends made with &#x60;scheduledFor&#x60; on this mailbox, in send order. Sent, failed and cancelled ones stay listed; filter with &#x60;status&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String status = "scheduled"; // String | 
        String cursor = "cursor_example"; // String | `pagination.nextCursor` of the previous page.
        Integer limit = 50; // Integer | 
        try {
            ListScheduledEmails200Response result = apiInstance.listScheduledEmails(accountId, status, cursor, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listScheduledEmails");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **status** | **String**|  | [optional] [enum: scheduled, sending, sent, failed, cancelled] |
| **cursor** | **String**| &#x60;pagination.nextCursor&#x60; of the previous page. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**ListScheduledEmails200Response**](ListScheduledEmails200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Scheduled emails |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listScheduledEmailsWithHttpInfo

> ApiResponse<ListScheduledEmails200Response> listScheduledEmails listScheduledEmailsWithHttpInfo(accountId, status, cursor, limit)

List scheduled emails

Sends made with &#x60;scheduledFor&#x60; on this mailbox, in send order. Sent, failed and cancelled ones stay listed; filter with &#x60;status&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String status = "scheduled"; // String | 
        String cursor = "cursor_example"; // String | `pagination.nextCursor` of the previous page.
        Integer limit = 50; // Integer | 
        try {
            ApiResponse<ListScheduledEmails200Response> response = apiInstance.listScheduledEmailsWithHttpInfo(accountId, status, cursor, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listScheduledEmails");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **status** | **String**|  | [optional] [enum: scheduled, sending, sent, failed, cancelled] |
| **cursor** | **String**| &#x60;pagination.nextCursor&#x60; of the previous page. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

ApiResponse<[**ListScheduledEmails200Response**](ListScheduledEmails200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Scheduled emails |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## replyEmailMessage

> SendEmailMessage201Response replyEmailMessage(messageId, replyEmailMessageRequest)

Reply to a message

Replies inside the provider&#39;s thread: the provider builds the quoted original and threading headers, your &#x60;html&#x60; or &#x60;text&#x60; goes above the quote. &#x60;to&#x60;, &#x60;cc&#x60;, &#x60;bcc&#x60;, &#x60;replyTo&#x60;, &#x60;subject&#x60;, &#x60;headers&#x60; and &#x60;attachments&#x60; are honoured.  &#x60;scheduledFor&#x60; schedules the reply (202) and &#x60;trackOpens&#x60;, &#x60;trackLinks&#x60; and &#x60;trackReplies&#x60; track it, as on send; &#x60;holdAsDraft&#x60; holds it as a reply draft in the thread until then. Same protection, caps and headers as sending. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        ReplyEmailMessageRequest replyEmailMessageRequest = new ReplyEmailMessageRequest(); // ReplyEmailMessageRequest | 
        try {
            SendEmailMessage201Response result = apiInstance.replyEmailMessage(messageId, replyEmailMessageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#replyEmailMessage");
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
| **messageId** | **String**|  | |
| **replyEmailMessageRequest** | [**ReplyEmailMessageRequest**](ReplyEmailMessageRequest.md)|  | |

### Return type

[**SendEmailMessage201Response**](SendEmailMessage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The sent reply |  -  |
| **202** | Scheduled: the send leaves at &#x60;scheduledFor&#x60; |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Outlook refused &#x60;from&#x60;: the mailbox has no Send As or Send on Behalf right on it. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |

## replyEmailMessageWithHttpInfo

> ApiResponse<SendEmailMessage201Response> replyEmailMessage replyEmailMessageWithHttpInfo(messageId, replyEmailMessageRequest)

Reply to a message

Replies inside the provider&#39;s thread: the provider builds the quoted original and threading headers, your &#x60;html&#x60; or &#x60;text&#x60; goes above the quote. &#x60;to&#x60;, &#x60;cc&#x60;, &#x60;bcc&#x60;, &#x60;replyTo&#x60;, &#x60;subject&#x60;, &#x60;headers&#x60; and &#x60;attachments&#x60; are honoured.  &#x60;scheduledFor&#x60; schedules the reply (202) and &#x60;trackOpens&#x60;, &#x60;trackLinks&#x60; and &#x60;trackReplies&#x60; track it, as on send; &#x60;holdAsDraft&#x60; holds it as a reply draft in the thread until then. Same protection, caps and headers as sending. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        ReplyEmailMessageRequest replyEmailMessageRequest = new ReplyEmailMessageRequest(); // ReplyEmailMessageRequest | 
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.replyEmailMessageWithHttpInfo(messageId, replyEmailMessageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#replyEmailMessage");
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
| **messageId** | **String**|  | |
| **replyEmailMessageRequest** | [**ReplyEmailMessageRequest**](ReplyEmailMessageRequest.md)|  | |

### Return type

ApiResponse<[**SendEmailMessage201Response**](SendEmailMessage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The sent reply |  -  |
| **202** | Scheduled: the send leaves at &#x60;scheduledFor&#x60; |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Outlook refused &#x60;from&#x60;: the mailbox has no Send As or Send on Behalf right on it. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |


## sendEmailMessage

> SendEmailMessage201Response sendEmailMessage(sendEmailRequest)

Send an email

Sends from the connected mailbox and returns the stored sent copy.  The message is mirrored into the inbox (&#x60;message.sent&#x60; fires once) and counted against the mailbox&#39;s daily cap. The cap is reported in the &#x60;X-Zernio-Send-Limit&#x60;, &#x60;X-Zernio-Send-Remaining&#x60; and &#x60;X-Zernio-Send-Reset&#x60; response headers.  ### Sending limits  These mailboxes are for one-to-one mail, not bulk sends. Protection on every mailbox:  - Daily cap: Microsoft 1,000; Google Workspace 500; Gmail consumer 200. Reaching it answers 429 &#x60;email_send_cap_reached&#x60; with &#x60;details.cap&#x60;. - The same body reaching more than 50 distinct recipients within an hour pauses the mailbox with an escalating cooldown (429 &#x60;rate_limited&#x60;, &#x60;account.rate_limited&#x60; webhook).  ### Scheduling  With &#x60;scheduledFor&#x60; the request answers 202 with a &#x60;ScheduledEmail&#x60; instead of sending. The account and payment method are checked now; the caps, cooldowns and the send itself run at &#x60;scheduledFor&#x60;. A send that fails then fires &#x60;email.send_failed&#x60;. List, read and cancel scheduled sends under &#x60;/v1/email/messages/scheduled&#x60;.  ### Tracking  - &#x60;trackOpens&#x60; adds a 1x1 image to the html and fires &#x60;email.opened&#x60;. - &#x60;trackLinks&#x60; rewrites every http(s) link in the html through a Zernio redirect and fires &#x60;email.link_clicked&#x60;. - &#x60;trackReplies&#x60; fires &#x60;email.thread_replied&#x60; when someone else writes in the thread.  Tracking costs nothing extra. Opens are approximate: image proxies prefetch and image blocking hides them.  ### Other errors  - 402: Gmail sends need a payment method on the workspace. Reading, calendar and files do not. - 400: &#x60;holdAsDraft&#x60; without &#x60;scheduledFor&#x60;; &#x60;trackOpens&#x60; or &#x60;trackLinks&#x60; without &#x60;html&#x60;; &#x60;scheduledFor&#x60; outside 1 minute to 30 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        SendEmailRequest sendEmailRequest = new SendEmailRequest(); // SendEmailRequest | 
        try {
            SendEmailMessage201Response result = apiInstance.sendEmailMessage(sendEmailRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#sendEmailMessage");
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
| **sendEmailRequest** | [**SendEmailRequest**](SendEmailRequest.md)|  | |

### Return type

[**SendEmailMessage201Response**](SendEmailMessage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The sent message |  * X-Zernio-Send-Limit - Today&#39;s cap for this mailbox. <br>  * X-Zernio-Send-Remaining -  <br>  * X-Zernio-Send-Reset - When the daily window resets (midnight UTC). <br>  |
| **202** | Scheduled: the send leaves at &#x60;scheduledFor&#x60; |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Outlook refused &#x60;from&#x60;: the mailbox has no Send As or Send on Behalf right on it. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |

## sendEmailMessageWithHttpInfo

> ApiResponse<SendEmailMessage201Response> sendEmailMessage sendEmailMessageWithHttpInfo(sendEmailRequest)

Send an email

Sends from the connected mailbox and returns the stored sent copy.  The message is mirrored into the inbox (&#x60;message.sent&#x60; fires once) and counted against the mailbox&#39;s daily cap. The cap is reported in the &#x60;X-Zernio-Send-Limit&#x60;, &#x60;X-Zernio-Send-Remaining&#x60; and &#x60;X-Zernio-Send-Reset&#x60; response headers.  ### Sending limits  These mailboxes are for one-to-one mail, not bulk sends. Protection on every mailbox:  - Daily cap: Microsoft 1,000; Google Workspace 500; Gmail consumer 200. Reaching it answers 429 &#x60;email_send_cap_reached&#x60; with &#x60;details.cap&#x60;. - The same body reaching more than 50 distinct recipients within an hour pauses the mailbox with an escalating cooldown (429 &#x60;rate_limited&#x60;, &#x60;account.rate_limited&#x60; webhook).  ### Scheduling  With &#x60;scheduledFor&#x60; the request answers 202 with a &#x60;ScheduledEmail&#x60; instead of sending. The account and payment method are checked now; the caps, cooldowns and the send itself run at &#x60;scheduledFor&#x60;. A send that fails then fires &#x60;email.send_failed&#x60;. List, read and cancel scheduled sends under &#x60;/v1/email/messages/scheduled&#x60;.  ### Tracking  - &#x60;trackOpens&#x60; adds a 1x1 image to the html and fires &#x60;email.opened&#x60;. - &#x60;trackLinks&#x60; rewrites every http(s) link in the html through a Zernio redirect and fires &#x60;email.link_clicked&#x60;. - &#x60;trackReplies&#x60; fires &#x60;email.thread_replied&#x60; when someone else writes in the thread.  Tracking costs nothing extra. Opens are approximate: image proxies prefetch and image blocking hides them.  ### Other errors  - 402: Gmail sends need a payment method on the workspace. Reading, calendar and files do not. - 400: &#x60;holdAsDraft&#x60; without &#x60;scheduledFor&#x60;; &#x60;trackOpens&#x60; or &#x60;trackLinks&#x60; without &#x60;html&#x60;; &#x60;scheduledFor&#x60; outside 1 minute to 30 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        SendEmailRequest sendEmailRequest = new SendEmailRequest(); // SendEmailRequest | 
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.sendEmailMessageWithHttpInfo(sendEmailRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#sendEmailMessage");
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
| **sendEmailRequest** | [**SendEmailRequest**](SendEmailRequest.md)|  | |

### Return type

ApiResponse<[**SendEmailMessage201Response**](SendEmailMessage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The sent message |  * X-Zernio-Send-Limit - Today&#39;s cap for this mailbox. <br>  * X-Zernio-Send-Remaining -  <br>  * X-Zernio-Send-Reset - When the daily window resets (midnight UTC). <br>  |
| **202** | Scheduled: the send leaves at &#x60;scheduledFor&#x60; |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Outlook refused &#x60;from&#x60;: the mailbox has no Send As or Send on Behalf right on it. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |


## trashEmailMessage

> TrashEmailMessage200Response trashEmailMessage(messageId, accountId)

Move a message to trash

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            TrashEmailMessage200Response result = apiInstance.trashEmailMessage(messageId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#trashEmailMessage");
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
| **messageId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**TrashEmailMessage200Response**](TrashEmailMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trashed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## trashEmailMessageWithHttpInfo

> ApiResponse<TrashEmailMessage200Response> trashEmailMessage trashEmailMessageWithHttpInfo(messageId, accountId)

Move a message to trash

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<TrashEmailMessage200Response> response = apiInstance.trashEmailMessageWithHttpInfo(messageId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#trashEmailMessage");
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
| **messageId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**TrashEmailMessage200Response**](TrashEmailMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trashed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## updateEmailMessage

> SendEmailMessage201Response updateEmailMessage(messageId, emailMessagePatch)

Mark read or starred, label, or move a message

&#x60;addLabels&#x60; and &#x60;removeLabels&#x60; tag the message without moving it. &#x60;folder&#x60; moves it: on Google a move files the mail in one place, so it drops the inbox, trash, spam and user labels it held; &#x60;archive&#x60; removes the inbox label.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        EmailMessagePatch emailMessagePatch = new EmailMessagePatch(); // EmailMessagePatch | 
        try {
            SendEmailMessage201Response result = apiInstance.updateEmailMessage(messageId, emailMessagePatch);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailMessage");
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
| **messageId** | **String**|  | |
| **emailMessagePatch** | [**EmailMessagePatch**](EmailMessagePatch.md)|  | |

### Return type

[**SendEmailMessage201Response**](SendEmailMessage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated message. A move on Microsoft changes the message id; read it from &#x60;data.id&#x60;. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## updateEmailMessageWithHttpInfo

> ApiResponse<SendEmailMessage201Response> updateEmailMessage updateEmailMessageWithHttpInfo(messageId, emailMessagePatch)

Mark read or starred, label, or move a message

&#x60;addLabels&#x60; and &#x60;removeLabels&#x60; tag the message without moving it. &#x60;folder&#x60; moves it: on Google a move files the mail in one place, so it drops the inbox, trash, spam and user labels it held; &#x60;archive&#x60; removes the inbox label.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String messageId = "messageId_example"; // String | 
        EmailMessagePatch emailMessagePatch = new EmailMessagePatch(); // EmailMessagePatch | 
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.updateEmailMessageWithHttpInfo(messageId, emailMessagePatch);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailMessage");
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
| **messageId** | **String**|  | |
| **emailMessagePatch** | [**EmailMessagePatch**](EmailMessagePatch.md)|  | |

### Return type

ApiResponse<[**SendEmailMessage201Response**](SendEmailMessage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated message. A move on Microsoft changes the message id; read it from &#x60;data.id&#x60;. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## updateEmailThread

> UpdateEmailThread200Response updateEmailThread(threadId, emailMessagePatch)

Update every message in a thread

Applies &#x60;unread&#x60;, &#x60;starred&#x60;, &#x60;addLabels&#x60;, &#x60;removeLabels&#x60; or a &#x60;folder&#x60; move to each message of the thread.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String threadId = "threadId_example"; // String | 
        EmailMessagePatch emailMessagePatch = new EmailMessagePatch(); // EmailMessagePatch | 
        try {
            UpdateEmailThread200Response result = apiInstance.updateEmailThread(threadId, emailMessagePatch);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailThread");
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
| **threadId** | **String**|  | |
| **emailMessagePatch** | [**EmailMessagePatch**](EmailMessagePatch.md)|  | |

### Return type

[**UpdateEmailThread200Response**](UpdateEmailThread200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated thread |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## updateEmailThreadWithHttpInfo

> ApiResponse<UpdateEmailThread200Response> updateEmailThread updateEmailThreadWithHttpInfo(threadId, emailMessagePatch)

Update every message in a thread

Applies &#x60;unread&#x60;, &#x60;starred&#x60;, &#x60;addLabels&#x60;, &#x60;removeLabels&#x60; or a &#x60;folder&#x60; move to each message of the thread.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.EmailApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        EmailApi apiInstance = new EmailApi(defaultClient);
        String threadId = "threadId_example"; // String | 
        EmailMessagePatch emailMessagePatch = new EmailMessagePatch(); // EmailMessagePatch | 
        try {
            ApiResponse<UpdateEmailThread200Response> response = apiInstance.updateEmailThreadWithHttpInfo(threadId, emailMessagePatch);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailThread");
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
| **threadId** | **String**|  | |
| **emailMessagePatch** | [**EmailMessagePatch**](EmailMessagePatch.md)|  | |

### Return type

ApiResponse<[**UpdateEmailThread200Response**](UpdateEmailThread200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated thread |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

