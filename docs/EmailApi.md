# EmailApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelScheduledEmail**](EmailApi.md#cancelScheduledEmail) | **DELETE** /v1/email/messages/scheduled/{scheduleId} | Cancel a scheduled email |
| [**cancelScheduledEmailWithHttpInfo**](EmailApi.md#cancelScheduledEmailWithHttpInfo) | **DELETE** /v1/email/messages/scheduled/{scheduleId} | Cancel a scheduled email |
| [**createEmailDraft**](EmailApi.md#createEmailDraft) | **POST** /v1/email/drafts | Create a draft |
| [**createEmailDraftWithHttpInfo**](EmailApi.md#createEmailDraftWithHttpInfo) | **POST** /v1/email/drafts | Create a draft |
| [**createEmailLabel**](EmailApi.md#createEmailLabel) | **POST** /v1/email/labels | Create a label |
| [**createEmailLabelWithHttpInfo**](EmailApi.md#createEmailLabelWithHttpInfo) | **POST** /v1/email/labels | Create a label |
| [**createEmailSignature**](EmailApi.md#createEmailSignature) | **POST** /v1/email/signatures | Create a signature |
| [**createEmailSignatureWithHttpInfo**](EmailApi.md#createEmailSignatureWithHttpInfo) | **POST** /v1/email/signatures | Create a signature |
| [**createImapAccount**](EmailApi.md#createImapAccount) | **POST** /v1/email/imap/accounts | Connect an IMAP mailbox |
| [**createImapAccountWithHttpInfo**](EmailApi.md#createImapAccountWithHttpInfo) | **POST** /v1/email/imap/accounts | Connect an IMAP mailbox |
| [**declareEmailSendAs**](EmailApi.md#declareEmailSendAs) | **POST** /v1/email/send-as | Declare a send-as address |
| [**declareEmailSendAsWithHttpInfo**](EmailApi.md#declareEmailSendAsWithHttpInfo) | **POST** /v1/email/send-as | Declare a send-as address |
| [**deleteEmailDraft**](EmailApi.md#deleteEmailDraft) | **DELETE** /v1/email/drafts/{draftId} | Delete a draft |
| [**deleteEmailDraftWithHttpInfo**](EmailApi.md#deleteEmailDraftWithHttpInfo) | **DELETE** /v1/email/drafts/{draftId} | Delete a draft |
| [**deleteEmailLabel**](EmailApi.md#deleteEmailLabel) | **DELETE** /v1/email/labels/{labelId} | Delete a label |
| [**deleteEmailLabelWithHttpInfo**](EmailApi.md#deleteEmailLabelWithHttpInfo) | **DELETE** /v1/email/labels/{labelId} | Delete a label |
| [**deleteEmailSendAs**](EmailApi.md#deleteEmailSendAs) | **DELETE** /v1/email/send-as/{email} | Remove a declared send-as address |
| [**deleteEmailSendAsWithHttpInfo**](EmailApi.md#deleteEmailSendAsWithHttpInfo) | **DELETE** /v1/email/send-as/{email} | Remove a declared send-as address |
| [**deleteEmailSignature**](EmailApi.md#deleteEmailSignature) | **DELETE** /v1/email/signatures/{signatureId} | Delete a signature |
| [**deleteEmailSignatureWithHttpInfo**](EmailApi.md#deleteEmailSignatureWithHttpInfo) | **DELETE** /v1/email/signatures/{signatureId} | Delete a signature |
| [**discoverImapSettings**](EmailApi.md#discoverImapSettings) | **POST** /v1/email/imap/discover | Find the mail settings for an address |
| [**discoverImapSettingsWithHttpInfo**](EmailApi.md#discoverImapSettingsWithHttpInfo) | **POST** /v1/email/imap/discover | Find the mail settings for an address |
| [**downloadEmailAttachment**](EmailApi.md#downloadEmailAttachment) | **GET** /v1/email/attachments/{attachmentId} | Download an attachment |
| [**downloadEmailAttachmentWithHttpInfo**](EmailApi.md#downloadEmailAttachmentWithHttpInfo) | **GET** /v1/email/attachments/{attachmentId} | Download an attachment |
| [**forwardEmailMessage**](EmailApi.md#forwardEmailMessage) | **POST** /v1/email/messages/{messageId}/forward | Forward a message |
| [**forwardEmailMessageWithHttpInfo**](EmailApi.md#forwardEmailMessageWithHttpInfo) | **POST** /v1/email/messages/{messageId}/forward | Forward a message |
| [**getEmailDraft**](EmailApi.md#getEmailDraft) | **GET** /v1/email/drafts/{draftId} | Get a draft |
| [**getEmailDraftWithHttpInfo**](EmailApi.md#getEmailDraftWithHttpInfo) | **GET** /v1/email/drafts/{draftId} | Get a draft |
| [**getEmailMessage**](EmailApi.md#getEmailMessage) | **GET** /v1/email/messages/{messageId} | Get an email message |
| [**getEmailMessageWithHttpInfo**](EmailApi.md#getEmailMessageWithHttpInfo) | **GET** /v1/email/messages/{messageId} | Get an email message |
| [**getEmailSignature**](EmailApi.md#getEmailSignature) | **GET** /v1/email/signatures/{signatureId} | Get a signature |
| [**getEmailSignatureWithHttpInfo**](EmailApi.md#getEmailSignatureWithHttpInfo) | **GET** /v1/email/signatures/{signatureId} | Get a signature |
| [**getEmailThread**](EmailApi.md#getEmailThread) | **GET** /v1/email/threads/{threadId} | Get an email thread with its messages |
| [**getEmailThreadWithHttpInfo**](EmailApi.md#getEmailThreadWithHttpInfo) | **GET** /v1/email/threads/{threadId} | Get an email thread with its messages |
| [**getScheduledEmail**](EmailApi.md#getScheduledEmail) | **GET** /v1/email/messages/scheduled/{scheduleId} | Get a scheduled email |
| [**getScheduledEmailWithHttpInfo**](EmailApi.md#getScheduledEmailWithHttpInfo) | **GET** /v1/email/messages/scheduled/{scheduleId} | Get a scheduled email |
| [**importEmailSignatures**](EmailApi.md#importEmailSignatures) | **POST** /v1/email/signatures/import | Import Gmail signatures |
| [**importEmailSignaturesWithHttpInfo**](EmailApi.md#importEmailSignaturesWithHttpInfo) | **POST** /v1/email/signatures/import | Import Gmail signatures |
| [**listEmailDrafts**](EmailApi.md#listEmailDrafts) | **GET** /v1/email/drafts | List drafts |
| [**listEmailDraftsWithHttpInfo**](EmailApi.md#listEmailDraftsWithHttpInfo) | **GET** /v1/email/drafts | List drafts |
| [**listEmailFolders**](EmailApi.md#listEmailFolders) | **GET** /v1/email/folders | List mailbox folders |
| [**listEmailFoldersWithHttpInfo**](EmailApi.md#listEmailFoldersWithHttpInfo) | **GET** /v1/email/folders | List mailbox folders |
| [**listEmailLabels**](EmailApi.md#listEmailLabels) | **GET** /v1/email/labels | List labels |
| [**listEmailLabelsWithHttpInfo**](EmailApi.md#listEmailLabelsWithHttpInfo) | **GET** /v1/email/labels | List labels |
| [**listEmailMessages**](EmailApi.md#listEmailMessages) | **GET** /v1/email/messages | List email messages |
| [**listEmailMessagesWithHttpInfo**](EmailApi.md#listEmailMessagesWithHttpInfo) | **GET** /v1/email/messages | List email messages |
| [**listEmailSendAs**](EmailApi.md#listEmailSendAs) | **GET** /v1/email/send-as | List send-as addresses |
| [**listEmailSendAsWithHttpInfo**](EmailApi.md#listEmailSendAsWithHttpInfo) | **GET** /v1/email/send-as | List send-as addresses |
| [**listEmailSignatures**](EmailApi.md#listEmailSignatures) | **GET** /v1/email/signatures | List signatures |
| [**listEmailSignaturesWithHttpInfo**](EmailApi.md#listEmailSignaturesWithHttpInfo) | **GET** /v1/email/signatures | List signatures |
| [**listEmailThreads**](EmailApi.md#listEmailThreads) | **GET** /v1/email/threads | List email threads |
| [**listEmailThreadsWithHttpInfo**](EmailApi.md#listEmailThreadsWithHttpInfo) | **GET** /v1/email/threads | List email threads |
| [**listScheduledEmails**](EmailApi.md#listScheduledEmails) | **GET** /v1/email/messages/scheduled | List scheduled emails |
| [**listScheduledEmailsWithHttpInfo**](EmailApi.md#listScheduledEmailsWithHttpInfo) | **GET** /v1/email/messages/scheduled | List scheduled emails |
| [**replyEmailMessage**](EmailApi.md#replyEmailMessage) | **POST** /v1/email/messages/{messageId}/reply | Reply to a message |
| [**replyEmailMessageWithHttpInfo**](EmailApi.md#replyEmailMessageWithHttpInfo) | **POST** /v1/email/messages/{messageId}/reply | Reply to a message |
| [**sendEmailDraft**](EmailApi.md#sendEmailDraft) | **POST** /v1/email/drafts/{draftId}/send | Send a draft |
| [**sendEmailDraftWithHttpInfo**](EmailApi.md#sendEmailDraftWithHttpInfo) | **POST** /v1/email/drafts/{draftId}/send | Send a draft |
| [**sendEmailMessage**](EmailApi.md#sendEmailMessage) | **POST** /v1/email/messages | Send an email |
| [**sendEmailMessageWithHttpInfo**](EmailApi.md#sendEmailMessageWithHttpInfo) | **POST** /v1/email/messages | Send an email |
| [**trashEmailMessage**](EmailApi.md#trashEmailMessage) | **DELETE** /v1/email/messages/{messageId} | Move a message to trash |
| [**trashEmailMessageWithHttpInfo**](EmailApi.md#trashEmailMessageWithHttpInfo) | **DELETE** /v1/email/messages/{messageId} | Move a message to trash |
| [**updateEmailDraft**](EmailApi.md#updateEmailDraft) | **PATCH** /v1/email/drafts/{draftId} | Update a draft |
| [**updateEmailDraftWithHttpInfo**](EmailApi.md#updateEmailDraftWithHttpInfo) | **PATCH** /v1/email/drafts/{draftId} | Update a draft |
| [**updateEmailMessage**](EmailApi.md#updateEmailMessage) | **PATCH** /v1/email/messages/{messageId} | Mark read or starred, label, or move a message |
| [**updateEmailMessageWithHttpInfo**](EmailApi.md#updateEmailMessageWithHttpInfo) | **PATCH** /v1/email/messages/{messageId} | Mark read or starred, label, or move a message |
| [**updateEmailSignature**](EmailApi.md#updateEmailSignature) | **PATCH** /v1/email/signatures/{signatureId} | Update a signature |
| [**updateEmailSignatureWithHttpInfo**](EmailApi.md#updateEmailSignatureWithHttpInfo) | **PATCH** /v1/email/signatures/{signatureId} | Update a signature |
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


## createEmailDraft

> CreateEmailDraft201Response createEmailDraft(createEmailDraftRequest, idempotencyKey)

Create a draft

Saves a draft in the user&#39;s mailbox, where they see it in Gmail or Outlook. Recipients and subject can come later. &#x60;inReplyTo&#x60; makes a reply draft in that thread and &#x60;forwardOf&#x60; a forward draft with the original&#39;s attachments; the &#x60;kind&#x60; is fixed for the life of the draft.  Send it with &#x60;POST /v1/email/drafts/{draftId}/send&#x60;. Edits the user makes in their mail client are what goes out. Store the draft &#x60;id&#x60;, and pass its &#x60;version&#x60; as &#x60;If-Match&#x60; so an update or send applies only to the version you saw. 

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
        CreateEmailDraftRequest createEmailDraftRequest = new CreateEmailDraftRequest(); // CreateEmailDraftRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            CreateEmailDraft201Response result = apiInstance.createEmailDraft(createEmailDraftRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createEmailDraft");
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
| **createEmailDraftRequest** | [**CreateEmailDraftRequest**](CreateEmailDraftRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

[**CreateEmailDraft201Response**](CreateEmailDraft201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The saved draft |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## createEmailDraftWithHttpInfo

> ApiResponse<CreateEmailDraft201Response> createEmailDraft createEmailDraftWithHttpInfo(createEmailDraftRequest, idempotencyKey)

Create a draft

Saves a draft in the user&#39;s mailbox, where they see it in Gmail or Outlook. Recipients and subject can come later. &#x60;inReplyTo&#x60; makes a reply draft in that thread and &#x60;forwardOf&#x60; a forward draft with the original&#39;s attachments; the &#x60;kind&#x60; is fixed for the life of the draft.  Send it with &#x60;POST /v1/email/drafts/{draftId}/send&#x60;. Edits the user makes in their mail client are what goes out. Store the draft &#x60;id&#x60;, and pass its &#x60;version&#x60; as &#x60;If-Match&#x60; so an update or send applies only to the version you saw. 

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
        CreateEmailDraftRequest createEmailDraftRequest = new CreateEmailDraftRequest(); // CreateEmailDraftRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<CreateEmailDraft201Response> response = apiInstance.createEmailDraftWithHttpInfo(createEmailDraftRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createEmailDraft");
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
| **createEmailDraftRequest** | [**CreateEmailDraftRequest**](CreateEmailDraftRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

ApiResponse<[**CreateEmailDraft201Response**](CreateEmailDraft201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The saved draft |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


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


## createEmailSignature

> CreateEmailSignature201Response createEmailSignature(createEmailSignatureRequest)

Create a signature

Stores a signature Zernio appends on any provider. Without &#x60;accountId&#x60; it is workspace-wide. &#x60;defaultFor&#x60; makes it what &#x60;appendSignature&#x60; uses for those sending addresses. Up to 50 per workspace, 100 KB of html, no scripts.

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
        CreateEmailSignatureRequest createEmailSignatureRequest = new CreateEmailSignatureRequest(); // CreateEmailSignatureRequest | 
        try {
            CreateEmailSignature201Response result = apiInstance.createEmailSignature(createEmailSignatureRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createEmailSignature");
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
| **createEmailSignatureRequest** | [**CreateEmailSignatureRequest**](CreateEmailSignatureRequest.md)|  | |

### Return type

[**CreateEmailSignature201Response**](CreateEmailSignature201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The signature was created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## createEmailSignatureWithHttpInfo

> ApiResponse<CreateEmailSignature201Response> createEmailSignature createEmailSignatureWithHttpInfo(createEmailSignatureRequest)

Create a signature

Stores a signature Zernio appends on any provider. Without &#x60;accountId&#x60; it is workspace-wide. &#x60;defaultFor&#x60; makes it what &#x60;appendSignature&#x60; uses for those sending addresses. Up to 50 per workspace, 100 KB of html, no scripts.

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
        CreateEmailSignatureRequest createEmailSignatureRequest = new CreateEmailSignatureRequest(); // CreateEmailSignatureRequest | 
        try {
            ApiResponse<CreateEmailSignature201Response> response = apiInstance.createEmailSignatureWithHttpInfo(createEmailSignatureRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createEmailSignature");
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
| **createEmailSignatureRequest** | [**CreateEmailSignatureRequest**](CreateEmailSignatureRequest.md)|  | |

### Return type

ApiResponse<[**CreateEmailSignature201Response**](CreateEmailSignature201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The signature was created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## createImapAccount

> ImapConnectResult createImapAccount(createImapAccountRequest)

Connect an IMAP mailbox

Connects any IMAP/SMTP mailbox without the hosted page. Email and password are enough when discovery finds the servers. Every check runs before anything is stored; a failure answers 422 with the failing stage&#39;s code. An address already on the profile is updated in place and keeps its accountId.  Send &#x60;Accept: application/x-ndjson&#x60; to stream one line per check as it runs, ending with a &#x60;result&#x60; line that holds the status and this body.

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
        CreateImapAccountRequest createImapAccountRequest = new CreateImapAccountRequest(); // CreateImapAccountRequest | 
        try {
            ImapConnectResult result = apiInstance.createImapAccount(createImapAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createImapAccount");
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
| **createImapAccountRequest** | [**CreateImapAccountRequest**](CreateImapAccountRequest.md)|  | |

### Return type

[**ImapConnectResult**](ImapConnectResult.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A dry run passed, or an existing account was updated in place |  -  |
| **201** | The mailbox was connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **422** | A check failed. code names the stage (imap_auth_failed, app_password_required, use_oauth, imap_disabled, imap_unreachable, tls_hostname_mismatch, tls_untrusted, smtp_unreachable, smtp_auth_failed, provider_unsupported, discovery_failed); details.stages says which checks passed. |  -  |
| **429** | too_many_attempts: the provider is refusing sign-ins; wait before retrying. |  -  |

## createImapAccountWithHttpInfo

> ApiResponse<ImapConnectResult> createImapAccount createImapAccountWithHttpInfo(createImapAccountRequest)

Connect an IMAP mailbox

Connects any IMAP/SMTP mailbox without the hosted page. Email and password are enough when discovery finds the servers. Every check runs before anything is stored; a failure answers 422 with the failing stage&#39;s code. An address already on the profile is updated in place and keeps its accountId.  Send &#x60;Accept: application/x-ndjson&#x60; to stream one line per check as it runs, ending with a &#x60;result&#x60; line that holds the status and this body.

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
        CreateImapAccountRequest createImapAccountRequest = new CreateImapAccountRequest(); // CreateImapAccountRequest | 
        try {
            ApiResponse<ImapConnectResult> response = apiInstance.createImapAccountWithHttpInfo(createImapAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#createImapAccount");
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
| **createImapAccountRequest** | [**CreateImapAccountRequest**](CreateImapAccountRequest.md)|  | |

### Return type

ApiResponse<[**ImapConnectResult**](ImapConnectResult.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A dry run passed, or an existing account was updated in place |  -  |
| **201** | The mailbox was connected |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **422** | A check failed. code names the stage (imap_auth_failed, app_password_required, use_oauth, imap_disabled, imap_unreachable, tls_hostname_mismatch, tls_untrusted, smtp_unreachable, smtp_auth_failed, provider_unsupported, discovery_failed); details.stages says which checks passed. |  -  |
| **429** | too_many_attempts: the provider is refusing sign-ins; wait before retrying. |  -  |


## declareEmailSendAs

> DeclareEmailSendAs200Response declareEmailSendAs(declareEmailSendAsRequest)

Declare a send-as address

Adds an address the provider cannot list, such as an Outlook shared mailbox, so &#x60;from&#x60; accepts it. It starts &#x60;unverified&#x60; and becomes &#x60;accepted&#x60; after its first send. Gmail answers 400: add aliases in Gmail settings instead. An address already listed comes back with 200.

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
        DeclareEmailSendAsRequest declareEmailSendAsRequest = new DeclareEmailSendAsRequest(); // DeclareEmailSendAsRequest | 
        try {
            DeclareEmailSendAs200Response result = apiInstance.declareEmailSendAs(declareEmailSendAsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#declareEmailSendAs");
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
| **declareEmailSendAsRequest** | [**DeclareEmailSendAsRequest**](DeclareEmailSendAsRequest.md)|  | |

### Return type

[**DeclareEmailSendAs200Response**](DeclareEmailSendAs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The address was already listed |  -  |
| **201** | The address was declared |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## declareEmailSendAsWithHttpInfo

> ApiResponse<DeclareEmailSendAs200Response> declareEmailSendAs declareEmailSendAsWithHttpInfo(declareEmailSendAsRequest)

Declare a send-as address

Adds an address the provider cannot list, such as an Outlook shared mailbox, so &#x60;from&#x60; accepts it. It starts &#x60;unverified&#x60; and becomes &#x60;accepted&#x60; after its first send. Gmail answers 400: add aliases in Gmail settings instead. An address already listed comes back with 200.

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
        DeclareEmailSendAsRequest declareEmailSendAsRequest = new DeclareEmailSendAsRequest(); // DeclareEmailSendAsRequest | 
        try {
            ApiResponse<DeclareEmailSendAs200Response> response = apiInstance.declareEmailSendAsWithHttpInfo(declareEmailSendAsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#declareEmailSendAs");
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
| **declareEmailSendAsRequest** | [**DeclareEmailSendAsRequest**](DeclareEmailSendAsRequest.md)|  | |

### Return type

ApiResponse<[**DeclareEmailSendAs200Response**](DeclareEmailSendAs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The address was already listed |  -  |
| **201** | The address was declared |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## deleteEmailDraft

> DeleteEmailDraft200Response deleteEmailDraft(draftId, accountId)

Delete a draft

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
        String draftId = "draftId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            DeleteEmailDraft200Response result = apiInstance.deleteEmailDraft(draftId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailDraft");
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
| **draftId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**DeleteEmailDraft200Response**](DeleteEmailDraft200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## deleteEmailDraftWithHttpInfo

> ApiResponse<DeleteEmailDraft200Response> deleteEmailDraft deleteEmailDraftWithHttpInfo(draftId, accountId)

Delete a draft

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
        String draftId = "draftId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<DeleteEmailDraft200Response> response = apiInstance.deleteEmailDraftWithHttpInfo(draftId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailDraft");
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
| **draftId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**DeleteEmailDraft200Response**](DeleteEmailDraft200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## deleteEmailLabel

> DeleteEmailDraft200Response deleteEmailLabel(labelId, accountId)

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
            DeleteEmailDraft200Response result = apiInstance.deleteEmailLabel(labelId, accountId);
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

[**DeleteEmailDraft200Response**](DeleteEmailDraft200Response.md)


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

> ApiResponse<DeleteEmailDraft200Response> deleteEmailLabel deleteEmailLabelWithHttpInfo(labelId, accountId)

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
            ApiResponse<DeleteEmailDraft200Response> response = apiInstance.deleteEmailLabelWithHttpInfo(labelId, accountId);
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

ApiResponse<[**DeleteEmailDraft200Response**](DeleteEmailDraft200Response.md)>


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


## deleteEmailSendAs

> DeleteEmailSendAs200Response deleteEmailSendAs(email, accountId)

Remove a declared send-as address

Removes an address declared with &#x60;POST /v1/email/send-as&#x60;. Addresses the provider lists cannot be removed here. URL-encode the &#x60;@&#x60;.

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
        String email = "email_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            DeleteEmailSendAs200Response result = apiInstance.deleteEmailSendAs(email, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailSendAs");
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
| **email** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**DeleteEmailSendAs200Response**](DeleteEmailSendAs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The declaration was removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## deleteEmailSendAsWithHttpInfo

> ApiResponse<DeleteEmailSendAs200Response> deleteEmailSendAs deleteEmailSendAsWithHttpInfo(email, accountId)

Remove a declared send-as address

Removes an address declared with &#x60;POST /v1/email/send-as&#x60;. Addresses the provider lists cannot be removed here. URL-encode the &#x60;@&#x60;.

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
        String email = "email_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<DeleteEmailSendAs200Response> response = apiInstance.deleteEmailSendAsWithHttpInfo(email, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailSendAs");
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
| **email** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**DeleteEmailSendAs200Response**](DeleteEmailSendAs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The declaration was removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## deleteEmailSignature

> DeleteEmailDraft200Response deleteEmailSignature(signatureId)

Delete a signature

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
        String signatureId = "signatureId_example"; // String | 
        try {
            DeleteEmailDraft200Response result = apiInstance.deleteEmailSignature(signatureId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailSignature");
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
| **signatureId** | **String**|  | |

### Return type

[**DeleteEmailDraft200Response**](DeleteEmailDraft200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The signature was deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## deleteEmailSignatureWithHttpInfo

> ApiResponse<DeleteEmailDraft200Response> deleteEmailSignature deleteEmailSignatureWithHttpInfo(signatureId)

Delete a signature

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
        String signatureId = "signatureId_example"; // String | 
        try {
            ApiResponse<DeleteEmailDraft200Response> response = apiInstance.deleteEmailSignatureWithHttpInfo(signatureId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#deleteEmailSignature");
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
| **signatureId** | **String**|  | |

### Return type

ApiResponse<[**DeleteEmailDraft200Response**](DeleteEmailDraft200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The signature was deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## discoverImapSettings

> DiscoverImapSettings200Response discoverImapSettings(discoverImapSettingsRequest)

Find the mail settings for an address

The routing decision the hosted page makes, for your own connect form: Google or Microsoft OAuth, IMAP with the servers and the provider&#39;s app-password steps, or unsupported. Sources run in parallel inside 15 seconds: presets, MX, autoconfig, Thunderbird&#39;s ISPDB (sent the domain only), SRV records, then a probe.

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
        DiscoverImapSettingsRequest discoverImapSettingsRequest = new DiscoverImapSettingsRequest(); // DiscoverImapSettingsRequest | 
        try {
            DiscoverImapSettings200Response result = apiInstance.discoverImapSettings(discoverImapSettingsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#discoverImapSettings");
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
| **discoverImapSettingsRequest** | [**DiscoverImapSettingsRequest**](DiscoverImapSettingsRequest.md)|  | |

### Return type

[**DiscoverImapSettings200Response**](DiscoverImapSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Where this address connects, and how |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## discoverImapSettingsWithHttpInfo

> ApiResponse<DiscoverImapSettings200Response> discoverImapSettings discoverImapSettingsWithHttpInfo(discoverImapSettingsRequest)

Find the mail settings for an address

The routing decision the hosted page makes, for your own connect form: Google or Microsoft OAuth, IMAP with the servers and the provider&#39;s app-password steps, or unsupported. Sources run in parallel inside 15 seconds: presets, MX, autoconfig, Thunderbird&#39;s ISPDB (sent the domain only), SRV records, then a probe.

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
        DiscoverImapSettingsRequest discoverImapSettingsRequest = new DiscoverImapSettingsRequest(); // DiscoverImapSettingsRequest | 
        try {
            ApiResponse<DiscoverImapSettings200Response> response = apiInstance.discoverImapSettingsWithHttpInfo(discoverImapSettingsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#discoverImapSettings");
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
| **discoverImapSettingsRequest** | [**DiscoverImapSettingsRequest**](DiscoverImapSettingsRequest.md)|  | |

### Return type

ApiResponse<[**DiscoverImapSettings200Response**](DiscoverImapSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Where this address connects, and how |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


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


## forwardEmailMessage

> SendEmailMessage201Response forwardEmailMessage(messageId, forwardEmailRequest, idempotencyKey)

Forward a message

Forwards the message with its attachments. Your &#x60;text&#x60; or &#x60;html&#x60; goes above the forwarded mail, and the subject defaults to \&quot;Fwd: \&quot; plus the original&#39;s. On Google the forward stays in the original thread; on Microsoft it goes through Outlook&#39;s own forward.  &#x60;includeAttachments: false&#x60; keeps only the original&#39;s inline images, and &#x60;excludeAttachmentIds&#x60; leaves out the ones you name. Everything together stays under 25 MB.  &#x60;trackOpens&#x60;, &#x60;trackLinks&#x60; and &#x60;trackReplies&#x60; work as on send. Same protection, caps and headers as sending. The response carries &#x60;forwardedFrom&#x60;, and &#x60;email.sent&#x60; fires with &#x60;source: forward&#x60;. 

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
        ForwardEmailRequest forwardEmailRequest = new ForwardEmailRequest(); // ForwardEmailRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            SendEmailMessage201Response result = apiInstance.forwardEmailMessage(messageId, forwardEmailRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#forwardEmailMessage");
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
| **forwardEmailRequest** | [**ForwardEmailRequest**](ForwardEmailRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **201** | The sent forward |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **413** | attachment_too_large: the forwarded and added attachments pass 25 MB; details.limitBytes |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |

## forwardEmailMessageWithHttpInfo

> ApiResponse<SendEmailMessage201Response> forwardEmailMessage forwardEmailMessageWithHttpInfo(messageId, forwardEmailRequest, idempotencyKey)

Forward a message

Forwards the message with its attachments. Your &#x60;text&#x60; or &#x60;html&#x60; goes above the forwarded mail, and the subject defaults to \&quot;Fwd: \&quot; plus the original&#39;s. On Google the forward stays in the original thread; on Microsoft it goes through Outlook&#39;s own forward.  &#x60;includeAttachments: false&#x60; keeps only the original&#39;s inline images, and &#x60;excludeAttachmentIds&#x60; leaves out the ones you name. Everything together stays under 25 MB.  &#x60;trackOpens&#x60;, &#x60;trackLinks&#x60; and &#x60;trackReplies&#x60; work as on send. Same protection, caps and headers as sending. The response carries &#x60;forwardedFrom&#x60;, and &#x60;email.sent&#x60; fires with &#x60;source: forward&#x60;. 

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
        ForwardEmailRequest forwardEmailRequest = new ForwardEmailRequest(); // ForwardEmailRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.forwardEmailMessageWithHttpInfo(messageId, forwardEmailRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#forwardEmailMessage");
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
| **forwardEmailRequest** | [**ForwardEmailRequest**](ForwardEmailRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **201** | The sent forward |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **413** | attachment_too_large: the forwarded and added attachments pass 25 MB; details.limitBytes |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |


## getEmailDraft

> CreateEmailDraft201Response getEmailDraft(draftId, accountId)

Get a draft

The draft as it stands in the mailbox now, with its bodies. A draft deleted in the mail client answers 404.

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
        String draftId = "draftId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            CreateEmailDraft201Response result = apiInstance.getEmailDraft(draftId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailDraft");
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
| **draftId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**CreateEmailDraft201Response**](CreateEmailDraft201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The draft |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## getEmailDraftWithHttpInfo

> ApiResponse<CreateEmailDraft201Response> getEmailDraft getEmailDraftWithHttpInfo(draftId, accountId)

Get a draft

The draft as it stands in the mailbox now, with its bodies. A draft deleted in the mail client answers 404.

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
        String draftId = "draftId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<CreateEmailDraft201Response> response = apiInstance.getEmailDraftWithHttpInfo(draftId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailDraft");
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
| **draftId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**CreateEmailDraft201Response**](CreateEmailDraft201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The draft |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## getEmailMessage

> SendEmailMessage201Response getEmailMessage(messageId, accountId, includeHeaders, raw, clean)

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
        Boolean clean = false; // Boolean | Add `cleanText`: the new text only, without quoted replies, forwarded history, signature or tracking pixels. Ready to hand to an LLM.
        try {
            SendEmailMessage201Response result = apiInstance.getEmailMessage(messageId, accountId, includeHeaders, raw, clean);
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
| **clean** | **Boolean**| Add &#x60;cleanText&#x60;: the new text only, without quoted replies, forwarded history, signature or tracking pixels. Ready to hand to an LLM. | [optional] [default to false] |

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

> ApiResponse<SendEmailMessage201Response> getEmailMessage getEmailMessageWithHttpInfo(messageId, accountId, includeHeaders, raw, clean)

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
        Boolean clean = false; // Boolean | Add `cleanText`: the new text only, without quoted replies, forwarded history, signature or tracking pixels. Ready to hand to an LLM.
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.getEmailMessageWithHttpInfo(messageId, accountId, includeHeaders, raw, clean);
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
| **clean** | **Boolean**| Add &#x60;cleanText&#x60;: the new text only, without quoted replies, forwarded history, signature or tracking pixels. Ready to hand to an LLM. | [optional] [default to false] |

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


## getEmailSignature

> CreateEmailSignature201Response getEmailSignature(signatureId)

Get a signature

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
        String signatureId = "signatureId_example"; // String | 
        try {
            CreateEmailSignature201Response result = apiInstance.getEmailSignature(signatureId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailSignature");
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
| **signatureId** | **String**|  | |

### Return type

[**CreateEmailSignature201Response**](CreateEmailSignature201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The signature |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getEmailSignatureWithHttpInfo

> ApiResponse<CreateEmailSignature201Response> getEmailSignature getEmailSignatureWithHttpInfo(signatureId)

Get a signature

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
        String signatureId = "signatureId_example"; // String | 
        try {
            ApiResponse<CreateEmailSignature201Response> response = apiInstance.getEmailSignatureWithHttpInfo(signatureId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#getEmailSignature");
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
| **signatureId** | **String**|  | |

### Return type

ApiResponse<[**CreateEmailSignature201Response**](CreateEmailSignature201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The signature |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getEmailThread

> GetEmailThread200Response getEmailThread(threadId, accountId, clean)

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
        Boolean clean = false; // Boolean | Add `cleanText` to every message: what each one added to the conversation, without the quoted history.
        try {
            GetEmailThread200Response result = apiInstance.getEmailThread(threadId, accountId, clean);
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
| **clean** | **Boolean**| Add &#x60;cleanText&#x60; to every message: what each one added to the conversation, without the quoted history. | [optional] [default to false] |

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

> ApiResponse<GetEmailThread200Response> getEmailThread getEmailThreadWithHttpInfo(threadId, accountId, clean)

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
        Boolean clean = false; // Boolean | Add `cleanText` to every message: what each one added to the conversation, without the quoted history.
        try {
            ApiResponse<GetEmailThread200Response> response = apiInstance.getEmailThreadWithHttpInfo(threadId, accountId, clean);
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
| **clean** | **Boolean**| Add &#x60;cleanText&#x60; to every message: what each one added to the conversation, without the quoted history. | [optional] [default to false] |

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


## importEmailSignatures

> ListEmailSignatures200Response importEmailSignatures(accountId)

Import Gmail signatures

Copies each Gmail send-as signature into a Zernio signature on that account, the default for its address. Repeating it refreshes the copies. Outlook answers 400: Microsoft Graph does not expose signatures.

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
            ListEmailSignatures200Response result = apiInstance.importEmailSignatures(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#importEmailSignatures");
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

[**ListEmailSignatures200Response**](ListEmailSignatures200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The imported signatures |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## importEmailSignaturesWithHttpInfo

> ApiResponse<ListEmailSignatures200Response> importEmailSignatures importEmailSignaturesWithHttpInfo(accountId)

Import Gmail signatures

Copies each Gmail send-as signature into a Zernio signature on that account, the default for its address. Repeating it refreshes the copies. Outlook answers 400: Microsoft Graph does not expose signatures.

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
            ApiResponse<ListEmailSignatures200Response> response = apiInstance.importEmailSignaturesWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#importEmailSignatures");
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

ApiResponse<[**ListEmailSignatures200Response**](ListEmailSignatures200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The imported signatures |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## listEmailDrafts

> ListEmailDrafts200Response listEmailDrafts(accountId, limit, cursor)

List drafts

The mailbox&#39;s drafts, newest first, including drafts the user wrote in Gmail or Outlook. Drafts in the trash are left out. Rows carry no bodies on Google; get a draft to read them.

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
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ListEmailDrafts200Response result = apiInstance.listEmailDrafts(accountId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailDrafts");
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
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |

### Return type

[**ListEmailDrafts200Response**](ListEmailDrafts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of drafts |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## listEmailDraftsWithHttpInfo

> ApiResponse<ListEmailDrafts200Response> listEmailDrafts listEmailDraftsWithHttpInfo(accountId, limit, cursor)

List drafts

The mailbox&#39;s drafts, newest first, including drafts the user wrote in Gmail or Outlook. Drafts in the trash are left out. Rows carry no bodies on Google; get a draft to read them.

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
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ApiResponse<ListEmailDrafts200Response> response = apiInstance.listEmailDraftsWithHttpInfo(accountId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailDrafts");
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
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListEmailDrafts200Response**](ListEmailDrafts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of drafts |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:  - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;. - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval. &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one; it opens in a browser with no API key and stays valid for one hour. &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


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

The addresses a mailbox can send from, for &#x60;from&#x60;, each with the signature &#x60;appendSignature&#x60; would add. Gmail lists every alias itself. Outlook lists the mailbox address and its aliases, plus any address declared with &#x60;POST /v1/email/send-as&#x60;.

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

The addresses a mailbox can send from, for &#x60;from&#x60;, each with the signature &#x60;appendSignature&#x60; would add. Gmail lists every alias itself. Outlook lists the mailbox address and its aliases, plus any address declared with &#x60;POST /v1/email/send-as&#x60;.

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


## listEmailSignatures

> ListEmailSignatures200Response listEmailSignatures(accountId)

List signatures

Zernio-stored signatures: workspace-wide ones plus those of the accounts you can see. With &#x60;accountId&#x60;, only workspace-wide ones and that account&#39;s.

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
        String accountId = "accountId_example"; // String | 
        try {
            ListEmailSignatures200Response result = apiInstance.listEmailSignatures(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailSignatures");
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
| **accountId** | **String**|  | [optional] |

### Return type

[**ListEmailSignatures200Response**](ListEmailSignatures200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The signatures |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listEmailSignaturesWithHttpInfo

> ApiResponse<ListEmailSignatures200Response> listEmailSignatures listEmailSignaturesWithHttpInfo(accountId)

List signatures

Zernio-stored signatures: workspace-wide ones plus those of the accounts you can see. With &#x60;accountId&#x60;, only workspace-wide ones and that account&#39;s.

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
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<ListEmailSignatures200Response> response = apiInstance.listEmailSignaturesWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#listEmailSignatures");
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
| **accountId** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListEmailSignatures200Response**](ListEmailSignatures200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The signatures |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


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

> SendEmailMessage201Response replyEmailMessage(messageId, replyEmailMessageRequest, idempotencyKey)

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            SendEmailMessage201Response result = apiInstance.replyEmailMessage(messageId, replyEmailMessageRequest, idempotencyKey);
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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

> ApiResponse<SendEmailMessage201Response> replyEmailMessage replyEmailMessageWithHttpInfo(messageId, replyEmailMessageRequest, idempotencyKey)

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.replyEmailMessageWithHttpInfo(messageId, replyEmailMessageRequest, idempotencyKey);
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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


## sendEmailDraft

> SendEmailMessage201Response sendEmailDraft(draftId, sendEmailDraftRequest, ifMatch, idempotencyKey)

Send a draft

Sends the draft as it stands in the mailbox now, edits made in Gmail or Outlook included, and returns the sent message with &#x60;draftId&#x60;. The draft needs at least one recipient. A draft the user deleted or already sent answers 404 &#x60;draft_not_found&#x60;.  With &#x60;If-Match&#x60; it goes out only if it is still the version the approver saw (412 &#x60;draft_conflict&#x60; otherwise). If the user removed the open pixel or rewrote links, tracking is put back before it is sent. Fires &#x60;email.sent&#x60; with &#x60;source: draft&#x60;.  Tracking set when the draft was created applies, and its &#x60;metadata&#x60; comes back on the sent message. Same protection, caps and headers as sending. 

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
        String draftId = "draftId_example"; // String | 
        SendEmailDraftRequest sendEmailDraftRequest = new SendEmailDraftRequest(); // SendEmailDraftRequest | 
        String ifMatch = "ifMatch_example"; // String | The draft `version` (also its `ETag`). The request applies only if the draft is still that version; otherwise 412 `draft_conflict` with the current draft in `details.draft`.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            SendEmailMessage201Response result = apiInstance.sendEmailDraft(draftId, sendEmailDraftRequest, ifMatch, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#sendEmailDraft");
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
| **draftId** | **String**|  | |
| **sendEmailDraftRequest** | [**SendEmailDraftRequest**](SendEmailDraftRequest.md)|  | |
| **ifMatch** | **String**| The draft &#x60;version&#x60; (also its &#x60;ETag&#x60;). The request applies only if the draft is still that version; otherwise 412 &#x60;draft_conflict&#x60; with the current draft in &#x60;details.draft&#x60;. | [optional] |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **201** | The sent message |  -  |
| **202** | Scheduled with &#x60;sendAt&#x60; |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **404** | Resource not found |  -  |
| **409** | draft_sending: a send of this draft is in flight |  -  |
| **412** | draft_conflict (the draft is no longer the If-Match version; the current draft is in details.draft), or the mailbox precondition failed |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |

## sendEmailDraftWithHttpInfo

> ApiResponse<SendEmailMessage201Response> sendEmailDraft sendEmailDraftWithHttpInfo(draftId, sendEmailDraftRequest, ifMatch, idempotencyKey)

Send a draft

Sends the draft as it stands in the mailbox now, edits made in Gmail or Outlook included, and returns the sent message with &#x60;draftId&#x60;. The draft needs at least one recipient. A draft the user deleted or already sent answers 404 &#x60;draft_not_found&#x60;.  With &#x60;If-Match&#x60; it goes out only if it is still the version the approver saw (412 &#x60;draft_conflict&#x60; otherwise). If the user removed the open pixel or rewrote links, tracking is put back before it is sent. Fires &#x60;email.sent&#x60; with &#x60;source: draft&#x60;.  Tracking set when the draft was created applies, and its &#x60;metadata&#x60; comes back on the sent message. Same protection, caps and headers as sending. 

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
        String draftId = "draftId_example"; // String | 
        SendEmailDraftRequest sendEmailDraftRequest = new SendEmailDraftRequest(); // SendEmailDraftRequest | 
        String ifMatch = "ifMatch_example"; // String | The draft `version` (also its `ETag`). The request applies only if the draft is still that version; otherwise 412 `draft_conflict` with the current draft in `details.draft`.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.sendEmailDraftWithHttpInfo(draftId, sendEmailDraftRequest, ifMatch, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#sendEmailDraft");
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
| **draftId** | **String**|  | |
| **sendEmailDraftRequest** | [**SendEmailDraftRequest**](SendEmailDraftRequest.md)|  | |
| **ifMatch** | **String**| The draft &#x60;version&#x60; (also its &#x60;ETag&#x60;). The request applies only if the draft is still that version; otherwise 412 &#x60;draft_conflict&#x60; with the current draft in &#x60;details.draft&#x60;. | [optional] |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **201** | The sent message |  -  |
| **202** | Scheduled with &#x60;sendAt&#x60; |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file, even the 1st one, because X API calls are passed through per call. Prepaid-balance accounts never get it: they pay X calls from the balance. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **404** | Resource not found |  -  |
| **409** | draft_sending: a send of this draft is in flight |  -  |
| **412** | draft_conflict (the draft is no longer the If-Match version; the current draft is in details.draft), or the mailbox precondition failed |  -  |
| **429** | The send was refused before reaching the provider.  - &#x60;email_send_cap_reached&#x60;: today&#39;s cap for the mailbox is spent. &#x60;details.cap&#x60; names the limit and &#x60;resetsAt&#x60;; &#x60;retryAfterSeconds&#x60; counts to midnight UTC. - &#x60;rate_limited&#x60;: the mailbox is in a sending cooldown, either from a same-body burst to more than 50 recipients in an hour (&#x60;details.cap.kind: recipient_burst&#x60;) or an earlier trigger. &#x60;retryAfterSeconds&#x60; says when it lifts, and &#x60;account.rate_limited&#x60; fired when it started.  |  -  |


## sendEmailMessage

> SendEmailMessage201Response sendEmailMessage(sendEmailRequest, idempotencyKey)

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            SendEmailMessage201Response result = apiInstance.sendEmailMessage(sendEmailRequest, idempotencyKey);
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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

> ApiResponse<SendEmailMessage201Response> sendEmailMessage sendEmailMessageWithHttpInfo(sendEmailRequest, idempotencyKey)

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<SendEmailMessage201Response> response = apiInstance.sendEmailMessageWithHttpInfo(sendEmailRequest, idempotencyKey);
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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


## updateEmailDraft

> CreateEmailDraft201Response updateEmailDraft(draftId, updateEmailDraftRequest, ifMatch)

Update a draft

Changes the fields you send and keeps the rest. A reply draft stays in its thread, and a new body on a reply or forward draft goes above the quoted original. With &#x60;If-Match&#x60;, a draft someone edited since answers 412 &#x60;draft_conflict&#x60; with the current draft.

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
        String draftId = "draftId_example"; // String | 
        UpdateEmailDraftRequest updateEmailDraftRequest = new UpdateEmailDraftRequest(); // UpdateEmailDraftRequest | 
        String ifMatch = "ifMatch_example"; // String | The draft `version` (also its `ETag`). The request applies only if the draft is still that version; otherwise 412 `draft_conflict` with the current draft in `details.draft`.
        try {
            CreateEmailDraft201Response result = apiInstance.updateEmailDraft(draftId, updateEmailDraftRequest, ifMatch);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailDraft");
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
| **draftId** | **String**|  | |
| **updateEmailDraftRequest** | [**UpdateEmailDraftRequest**](UpdateEmailDraftRequest.md)|  | |
| **ifMatch** | **String**| The draft &#x60;version&#x60; (also its &#x60;ETag&#x60;). The request applies only if the draft is still that version; otherwise 412 &#x60;draft_conflict&#x60; with the current draft in &#x60;details.draft&#x60;. | [optional] |

### Return type

[**CreateEmailDraft201Response**](CreateEmailDraft201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated draft. On Google &#x60;messageId&#x60; changes on every update; the draft &#x60;id&#x60; does not. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | draft_sending: a send of this draft is in flight |  -  |
| **412** | draft_conflict (stale If-Match, current draft in details.draft), or the mailbox precondition failed |  -  |

## updateEmailDraftWithHttpInfo

> ApiResponse<CreateEmailDraft201Response> updateEmailDraft updateEmailDraftWithHttpInfo(draftId, updateEmailDraftRequest, ifMatch)

Update a draft

Changes the fields you send and keeps the rest. A reply draft stays in its thread, and a new body on a reply or forward draft goes above the quoted original. With &#x60;If-Match&#x60;, a draft someone edited since answers 412 &#x60;draft_conflict&#x60; with the current draft.

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
        String draftId = "draftId_example"; // String | 
        UpdateEmailDraftRequest updateEmailDraftRequest = new UpdateEmailDraftRequest(); // UpdateEmailDraftRequest | 
        String ifMatch = "ifMatch_example"; // String | The draft `version` (also its `ETag`). The request applies only if the draft is still that version; otherwise 412 `draft_conflict` with the current draft in `details.draft`.
        try {
            ApiResponse<CreateEmailDraft201Response> response = apiInstance.updateEmailDraftWithHttpInfo(draftId, updateEmailDraftRequest, ifMatch);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailDraft");
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
| **draftId** | **String**|  | |
| **updateEmailDraftRequest** | [**UpdateEmailDraftRequest**](UpdateEmailDraftRequest.md)|  | |
| **ifMatch** | **String**| The draft &#x60;version&#x60; (also its &#x60;ETag&#x60;). The request applies only if the draft is still that version; otherwise 412 &#x60;draft_conflict&#x60; with the current draft in &#x60;details.draft&#x60;. | [optional] |

### Return type

ApiResponse<[**CreateEmailDraft201Response**](CreateEmailDraft201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated draft. On Google &#x60;messageId&#x60; changes on every update; the draft &#x60;id&#x60; does not. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | draft_sending: a send of this draft is in flight |  -  |
| **412** | draft_conflict (stale If-Match, current draft in details.draft), or the mailbox precondition failed |  -  |


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


## updateEmailSignature

> CreateEmailSignature201Response updateEmailSignature(signatureId, updateEmailSignatureRequest)

Update a signature

Changes the name, html, text or &#x60;defaultFor&#x60;. Taking an address in &#x60;defaultFor&#x60; removes it from the other signatures of the same scope.

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
        String signatureId = "signatureId_example"; // String | 
        UpdateEmailSignatureRequest updateEmailSignatureRequest = new UpdateEmailSignatureRequest(); // UpdateEmailSignatureRequest | 
        try {
            CreateEmailSignature201Response result = apiInstance.updateEmailSignature(signatureId, updateEmailSignatureRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailSignature");
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
| **signatureId** | **String**|  | |
| **updateEmailSignatureRequest** | [**UpdateEmailSignatureRequest**](UpdateEmailSignatureRequest.md)|  | |

### Return type

[**CreateEmailSignature201Response**](CreateEmailSignature201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated signature |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## updateEmailSignatureWithHttpInfo

> ApiResponse<CreateEmailSignature201Response> updateEmailSignature updateEmailSignatureWithHttpInfo(signatureId, updateEmailSignatureRequest)

Update a signature

Changes the name, html, text or &#x60;defaultFor&#x60;. Taking an address in &#x60;defaultFor&#x60; removes it from the other signatures of the same scope.

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
        String signatureId = "signatureId_example"; // String | 
        UpdateEmailSignatureRequest updateEmailSignatureRequest = new UpdateEmailSignatureRequest(); // UpdateEmailSignatureRequest | 
        try {
            ApiResponse<CreateEmailSignature201Response> response = apiInstance.updateEmailSignatureWithHttpInfo(signatureId, updateEmailSignatureRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling EmailApi#updateEmailSignature");
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
| **signatureId** | **String**|  | |
| **updateEmailSignatureRequest** | [**UpdateEmailSignatureRequest**](UpdateEmailSignatureRequest.md)|  | |

### Return type

ApiResponse<[**CreateEmailSignature201Response**](CreateEmailSignature201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated signature |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


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

