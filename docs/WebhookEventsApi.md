# WebhookEventsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**onAccountAdsInitialSyncCompleted**](WebhookEventsApi.md#onAccountAdsInitialSyncCompleted) | **POST** /account.ads.initial_sync_completed | Ads initial sync completed event |
| [**onAccountAdsInitialSyncCompletedWithHttpInfo**](WebhookEventsApi.md#onAccountAdsInitialSyncCompletedWithHttpInfo) | **POST** /account.ads.initial_sync_completed | Ads initial sync completed event |
| [**onAccountConnected**](WebhookEventsApi.md#onAccountConnected) | **POST** /account.connected | Account connected event |
| [**onAccountConnectedWithHttpInfo**](WebhookEventsApi.md#onAccountConnectedWithHttpInfo) | **POST** /account.connected | Account connected event |
| [**onAccountDisconnected**](WebhookEventsApi.md#onAccountDisconnected) | **POST** /account.disconnected | Account disconnected event |
| [**onAccountDisconnectedWithHttpInfo**](WebhookEventsApi.md#onAccountDisconnectedWithHttpInfo) | **POST** /account.disconnected | Account disconnected event |
| [**onAdStatusChanged**](WebhookEventsApi.md#onAdStatusChanged) | **POST** /ad.status_changed | Ad status changed event |
| [**onAdStatusChangedWithHttpInfo**](WebhookEventsApi.md#onAdStatusChangedWithHttpInfo) | **POST** /ad.status_changed | Ad status changed event |
| [**onCallEnded**](WebhookEventsApi.md#onCallEnded) | **POST** /call.ended | Call ended event |
| [**onCallEndedWithHttpInfo**](WebhookEventsApi.md#onCallEndedWithHttpInfo) | **POST** /call.ended | Call ended event |
| [**onCallFailed**](WebhookEventsApi.md#onCallFailed) | **POST** /call.failed | Call failed event |
| [**onCallFailedWithHttpInfo**](WebhookEventsApi.md#onCallFailedWithHttpInfo) | **POST** /call.failed | Call failed event |
| [**onCallPermissionRequest**](WebhookEventsApi.md#onCallPermissionRequest) | **POST** /call.permission_request | Call permission request reply event |
| [**onCallPermissionRequestWithHttpInfo**](WebhookEventsApi.md#onCallPermissionRequestWithHttpInfo) | **POST** /call.permission_request | Call permission request reply event |
| [**onCallReceived**](WebhookEventsApi.md#onCallReceived) | **POST** /call.received | Call received event |
| [**onCallReceivedWithHttpInfo**](WebhookEventsApi.md#onCallReceivedWithHttpInfo) | **POST** /call.received | Call received event |
| [**onCommentReceived**](WebhookEventsApi.md#onCommentReceived) | **POST** /comment.received | Comment received event |
| [**onCommentReceivedWithHttpInfo**](WebhookEventsApi.md#onCommentReceivedWithHttpInfo) | **POST** /comment.received | Comment received event |
| [**onConversationStarted**](WebhookEventsApi.md#onConversationStarted) | **POST** /conversation.started | Conversation started event |
| [**onConversationStartedWithHttpInfo**](WebhookEventsApi.md#onConversationStartedWithHttpInfo) | **POST** /conversation.started | Conversation started event |
| [**onLeadReceived**](WebhookEventsApi.md#onLeadReceived) | **POST** /lead.received | Lead received event |
| [**onLeadReceivedWithHttpInfo**](WebhookEventsApi.md#onLeadReceivedWithHttpInfo) | **POST** /lead.received | Lead received event |
| [**onMessageDeleted**](WebhookEventsApi.md#onMessageDeleted) | **POST** /message.deleted | Message deleted event |
| [**onMessageDeletedWithHttpInfo**](WebhookEventsApi.md#onMessageDeletedWithHttpInfo) | **POST** /message.deleted | Message deleted event |
| [**onMessageDelivered**](WebhookEventsApi.md#onMessageDelivered) | **POST** /message.delivered | Message delivered event |
| [**onMessageDeliveredWithHttpInfo**](WebhookEventsApi.md#onMessageDeliveredWithHttpInfo) | **POST** /message.delivered | Message delivered event |
| [**onMessageEdited**](WebhookEventsApi.md#onMessageEdited) | **POST** /message.edited | Message edited event |
| [**onMessageEditedWithHttpInfo**](WebhookEventsApi.md#onMessageEditedWithHttpInfo) | **POST** /message.edited | Message edited event |
| [**onMessageFailed**](WebhookEventsApi.md#onMessageFailed) | **POST** /message.failed | Message delivery failed event |
| [**onMessageFailedWithHttpInfo**](WebhookEventsApi.md#onMessageFailedWithHttpInfo) | **POST** /message.failed | Message delivery failed event |
| [**onMessageRead**](WebhookEventsApi.md#onMessageRead) | **POST** /message.read | Message read event |
| [**onMessageReadWithHttpInfo**](WebhookEventsApi.md#onMessageReadWithHttpInfo) | **POST** /message.read | Message read event |
| [**onMessageReceived**](WebhookEventsApi.md#onMessageReceived) | **POST** /message.received | Message received event |
| [**onMessageReceivedWithHttpInfo**](WebhookEventsApi.md#onMessageReceivedWithHttpInfo) | **POST** /message.received | Message received event |
| [**onMessageSent**](WebhookEventsApi.md#onMessageSent) | **POST** /message.sent | Message sent event |
| [**onMessageSentWithHttpInfo**](WebhookEventsApi.md#onMessageSentWithHttpInfo) | **POST** /message.sent | Message sent event |
| [**onPostCancelled**](WebhookEventsApi.md#onPostCancelled) | **POST** /post.cancelled | Post cancelled event |
| [**onPostCancelledWithHttpInfo**](WebhookEventsApi.md#onPostCancelledWithHttpInfo) | **POST** /post.cancelled | Post cancelled event |
| [**onPostExternalCreated**](WebhookEventsApi.md#onPostExternalCreated) | **POST** /post.external.created | External post created event |
| [**onPostExternalCreatedWithHttpInfo**](WebhookEventsApi.md#onPostExternalCreatedWithHttpInfo) | **POST** /post.external.created | External post created event |
| [**onPostExternalDeleted**](WebhookEventsApi.md#onPostExternalDeleted) | **POST** /post.external.deleted | External post deleted event |
| [**onPostExternalDeletedWithHttpInfo**](WebhookEventsApi.md#onPostExternalDeletedWithHttpInfo) | **POST** /post.external.deleted | External post deleted event |
| [**onPostExternalUpdated**](WebhookEventsApi.md#onPostExternalUpdated) | **POST** /post.external.updated | External post updated event |
| [**onPostExternalUpdatedWithHttpInfo**](WebhookEventsApi.md#onPostExternalUpdatedWithHttpInfo) | **POST** /post.external.updated | External post updated event |
| [**onPostFailed**](WebhookEventsApi.md#onPostFailed) | **POST** /post.failed | Post failed event |
| [**onPostFailedWithHttpInfo**](WebhookEventsApi.md#onPostFailedWithHttpInfo) | **POST** /post.failed | Post failed event |
| [**onPostPartial**](WebhookEventsApi.md#onPostPartial) | **POST** /post.partial | Post partial event |
| [**onPostPartialWithHttpInfo**](WebhookEventsApi.md#onPostPartialWithHttpInfo) | **POST** /post.partial | Post partial event |
| [**onPostPlatformFailed**](WebhookEventsApi.md#onPostPlatformFailed) | **POST** /post.platform.failed | Post platform failed event |
| [**onPostPlatformFailedWithHttpInfo**](WebhookEventsApi.md#onPostPlatformFailedWithHttpInfo) | **POST** /post.platform.failed | Post platform failed event |
| [**onPostPlatformPublished**](WebhookEventsApi.md#onPostPlatformPublished) | **POST** /post.platform.published | Post platform published event |
| [**onPostPlatformPublishedWithHttpInfo**](WebhookEventsApi.md#onPostPlatformPublishedWithHttpInfo) | **POST** /post.platform.published | Post platform published event |
| [**onPostPublished**](WebhookEventsApi.md#onPostPublished) | **POST** /post.published | Post published event |
| [**onPostPublishedWithHttpInfo**](WebhookEventsApi.md#onPostPublishedWithHttpInfo) | **POST** /post.published | Post published event |
| [**onPostRecycled**](WebhookEventsApi.md#onPostRecycled) | **POST** /post.recycled | Post recycled event |
| [**onPostRecycledWithHttpInfo**](WebhookEventsApi.md#onPostRecycledWithHttpInfo) | **POST** /post.recycled | Post recycled event |
| [**onPostScheduled**](WebhookEventsApi.md#onPostScheduled) | **POST** /post.scheduled | Post scheduled event |
| [**onPostScheduledWithHttpInfo**](WebhookEventsApi.md#onPostScheduledWithHttpInfo) | **POST** /post.scheduled | Post scheduled event |
| [**onReactionReceived**](WebhookEventsApi.md#onReactionReceived) | **POST** /reaction.received | Reaction received event |
| [**onReactionReceivedWithHttpInfo**](WebhookEventsApi.md#onReactionReceivedWithHttpInfo) | **POST** /reaction.received | Reaction received event |
| [**onReviewNew**](WebhookEventsApi.md#onReviewNew) | **POST** /review.new | Review new event |
| [**onReviewNewWithHttpInfo**](WebhookEventsApi.md#onReviewNewWithHttpInfo) | **POST** /review.new | Review new event |
| [**onReviewUpdated**](WebhookEventsApi.md#onReviewUpdated) | **POST** /review.updated | Review updated event |
| [**onReviewUpdatedWithHttpInfo**](WebhookEventsApi.md#onReviewUpdatedWithHttpInfo) | **POST** /review.updated | Review updated event |
| [**onWebhookTest**](WebhookEventsApi.md#onWebhookTest) | **POST** /webhook.test | Webhook test event |
| [**onWebhookTestWithHttpInfo**](WebhookEventsApi.md#onWebhookTestWithHttpInfo) | **POST** /webhook.test | Webhook test event |
| [**onWhatsAppNumberActivated**](WebhookEventsApi.md#onWhatsAppNumberActivated) | **POST** /whatsapp.number.activated | WhatsApp number activated event |
| [**onWhatsAppNumberActivatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberActivatedWithHttpInfo) | **POST** /whatsapp.number.activated | WhatsApp number activated event |
| [**onWhatsAppNumberDeclined**](WebhookEventsApi.md#onWhatsAppNumberDeclined) | **POST** /whatsapp.number.declined | WhatsApp number declined event |
| [**onWhatsAppNumberDeclinedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberDeclinedWithHttpInfo) | **POST** /whatsapp.number.declined | WhatsApp number declined event |
| [**onWhatsAppNumberReactivated**](WebhookEventsApi.md#onWhatsAppNumberReactivated) | **POST** /whatsapp.number.reactivated | WhatsApp number reactivated event |
| [**onWhatsAppNumberReactivatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberReactivatedWithHttpInfo) | **POST** /whatsapp.number.reactivated | WhatsApp number reactivated event |
| [**onWhatsAppNumberReleased**](WebhookEventsApi.md#onWhatsAppNumberReleased) | **POST** /whatsapp.number.released | WhatsApp number released event |
| [**onWhatsAppNumberReleasedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberReleasedWithHttpInfo) | **POST** /whatsapp.number.released | WhatsApp number released event |
| [**onWhatsAppNumberSuspended**](WebhookEventsApi.md#onWhatsAppNumberSuspended) | **POST** /whatsapp.number.suspended | WhatsApp number suspended event |
| [**onWhatsAppNumberSuspendedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberSuspendedWithHttpInfo) | **POST** /whatsapp.number.suspended | WhatsApp number suspended event |
| [**onWhatsAppNumberVerificationRequired**](WebhookEventsApi.md#onWhatsAppNumberVerificationRequired) | **POST** /whatsapp.number.verification_required | WhatsApp number verification-required event |
| [**onWhatsAppNumberVerificationRequiredWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberVerificationRequiredWithHttpInfo) | **POST** /whatsapp.number.verification_required | WhatsApp number verification-required event |
| [**onWhatsAppTemplateStatusUpdated**](WebhookEventsApi.md#onWhatsAppTemplateStatusUpdated) | **POST** /whatsapp.template.status_updated | WhatsApp template status updated event |
| [**onWhatsAppTemplateStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppTemplateStatusUpdatedWithHttpInfo) | **POST** /whatsapp.template.status_updated | WhatsApp template status updated event |



## onAccountAdsInitialSyncCompleted

> void onAccountAdsInitialSyncCompleted(webhookPayloadAccountAdsInitialSyncCompleted)

Ads initial sync completed event

Fired once per ads-enabled account when the initial sync (ad-account discovery + 90-day historical ad backfill) completes. The &#x60;sync&#x60; block reports whether the backfill succeeded and how many ads were synced. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsInitialSyncCompleted webhookPayloadAccountAdsInitialSyncCompleted = new WebhookPayloadAccountAdsInitialSyncCompleted(); // WebhookPayloadAccountAdsInitialSyncCompleted | 
        try {
            apiInstance.onAccountAdsInitialSyncCompleted(webhookPayloadAccountAdsInitialSyncCompleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsInitialSyncCompleted");
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
| **webhookPayloadAccountAdsInitialSyncCompleted** | [**WebhookPayloadAccountAdsInitialSyncCompleted**](WebhookPayloadAccountAdsInitialSyncCompleted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountAdsInitialSyncCompletedWithHttpInfo

> ApiResponse<Void> onAccountAdsInitialSyncCompleted onAccountAdsInitialSyncCompletedWithHttpInfo(webhookPayloadAccountAdsInitialSyncCompleted)

Ads initial sync completed event

Fired once per ads-enabled account when the initial sync (ad-account discovery + 90-day historical ad backfill) completes. The &#x60;sync&#x60; block reports whether the backfill succeeded and how many ads were synced. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsInitialSyncCompleted webhookPayloadAccountAdsInitialSyncCompleted = new WebhookPayloadAccountAdsInitialSyncCompleted(); // WebhookPayloadAccountAdsInitialSyncCompleted | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountAdsInitialSyncCompletedWithHttpInfo(webhookPayloadAccountAdsInitialSyncCompleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsInitialSyncCompleted");
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
| **webhookPayloadAccountAdsInitialSyncCompleted** | [**WebhookPayloadAccountAdsInitialSyncCompleted**](WebhookPayloadAccountAdsInitialSyncCompleted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountConnected

> void onAccountConnected(webhookPayloadAccountConnected)

Account connected event

Fired when a social account is successfully connected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountConnected webhookPayloadAccountConnected = new WebhookPayloadAccountConnected(); // WebhookPayloadAccountConnected | 
        try {
            apiInstance.onAccountConnected(webhookPayloadAccountConnected);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountConnected");
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
| **webhookPayloadAccountConnected** | [**WebhookPayloadAccountConnected**](WebhookPayloadAccountConnected.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountConnectedWithHttpInfo

> ApiResponse<Void> onAccountConnected onAccountConnectedWithHttpInfo(webhookPayloadAccountConnected)

Account connected event

Fired when a social account is successfully connected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountConnected webhookPayloadAccountConnected = new WebhookPayloadAccountConnected(); // WebhookPayloadAccountConnected | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountConnectedWithHttpInfo(webhookPayloadAccountConnected);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountConnected");
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
| **webhookPayloadAccountConnected** | [**WebhookPayloadAccountConnected**](WebhookPayloadAccountConnected.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountDisconnected

> void onAccountDisconnected(webhookPayloadAccountDisconnected)

Account disconnected event

Fired when a connected social account becomes disconnected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountDisconnected webhookPayloadAccountDisconnected = new WebhookPayloadAccountDisconnected(); // WebhookPayloadAccountDisconnected | 
        try {
            apiInstance.onAccountDisconnected(webhookPayloadAccountDisconnected);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountDisconnected");
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
| **webhookPayloadAccountDisconnected** | [**WebhookPayloadAccountDisconnected**](WebhookPayloadAccountDisconnected.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountDisconnectedWithHttpInfo

> ApiResponse<Void> onAccountDisconnected onAccountDisconnectedWithHttpInfo(webhookPayloadAccountDisconnected)

Account disconnected event

Fired when a connected social account becomes disconnected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountDisconnected webhookPayloadAccountDisconnected = new WebhookPayloadAccountDisconnected(); // WebhookPayloadAccountDisconnected | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountDisconnectedWithHttpInfo(webhookPayloadAccountDisconnected);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountDisconnected");
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
| **webhookPayloadAccountDisconnected** | [**WebhookPayloadAccountDisconnected**](WebhookPayloadAccountDisconnected.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdStatusChanged

> void onAdStatusChanged(webhookPayloadAdStatusChanged)

Ad status changed event

Fired when a campaign, ad set, or ad on a connected ad platform changes status. Currently emitted only for Meta (&#x60;metaads&#x60;).  Subscribed to two Meta &#x60;ad_account&#x60; webhook fields:   - &#x60;in_process_ad_objects&#x60; - the ad object finished processing and exited     the &#x60;IN_PROCESS&#x60; state. &#x60;status.raw&#x60; carries Meta&#39;s &#x60;status_name&#x60;     (e.g. &#x60;ACTIVE&#x60;, &#x60;PAUSED&#x60;, &#x60;ARCHIVED&#x60;, &#x60;DELETED&#x60;).   - &#x60;with_issues_ad_objects&#x60; - the ad object entered the &#x60;WITH_ISSUES&#x60;     state. &#x60;status.raw&#x60; is set to &#x60;WITH_ISSUES&#x60; and the &#x60;error&#x60; block is     populated from Meta&#39;s &#x60;error_code&#x60; / &#x60;error_summary&#x60; / &#x60;error_message&#x60;.  &#x60;adObject.level&#x60; mirrors Meta&#39;s &#x60;level&#x60; and is one of &#x60;CAMPAIGN&#x60;, &#x60;AD_SET&#x60;, or &#x60;AD&#x60;. Creative-level events are not forwarded.  Branch on &#x60;status.raw&#x60; to handle each transition; use &#x60;error.code&#x60; (when present) as the stable discriminator — &#x60;error.summary&#x60; and &#x60;error.message&#x60; are localized to the ad-account owner&#39;s Meta locale.  The &#x60;error&#x60; block is optional. It&#39;s present on most &#x60;WITH_ISSUES&#x60; events but can be absent (Meta does not always include diagnostics), and is never present on any other status. Always null-check &#x60;error&#x60; before reading &#x60;error.code&#x60;.  **Fan-out:** matching is keyed on &#x60;adObject.platformAdAccountId&#x60;. When multiple connected Zernio &#x60;metaads&#x60; accounts are linked to the same Meta ad account, each receives its own delivery. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdStatusChanged webhookPayloadAdStatusChanged = new WebhookPayloadAdStatusChanged(); // WebhookPayloadAdStatusChanged | 
        try {
            apiInstance.onAdStatusChanged(webhookPayloadAdStatusChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdStatusChanged");
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
| **webhookPayloadAdStatusChanged** | [**WebhookPayloadAdStatusChanged**](WebhookPayloadAdStatusChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdStatusChangedWithHttpInfo

> ApiResponse<Void> onAdStatusChanged onAdStatusChangedWithHttpInfo(webhookPayloadAdStatusChanged)

Ad status changed event

Fired when a campaign, ad set, or ad on a connected ad platform changes status. Currently emitted only for Meta (&#x60;metaads&#x60;).  Subscribed to two Meta &#x60;ad_account&#x60; webhook fields:   - &#x60;in_process_ad_objects&#x60; - the ad object finished processing and exited     the &#x60;IN_PROCESS&#x60; state. &#x60;status.raw&#x60; carries Meta&#39;s &#x60;status_name&#x60;     (e.g. &#x60;ACTIVE&#x60;, &#x60;PAUSED&#x60;, &#x60;ARCHIVED&#x60;, &#x60;DELETED&#x60;).   - &#x60;with_issues_ad_objects&#x60; - the ad object entered the &#x60;WITH_ISSUES&#x60;     state. &#x60;status.raw&#x60; is set to &#x60;WITH_ISSUES&#x60; and the &#x60;error&#x60; block is     populated from Meta&#39;s &#x60;error_code&#x60; / &#x60;error_summary&#x60; / &#x60;error_message&#x60;.  &#x60;adObject.level&#x60; mirrors Meta&#39;s &#x60;level&#x60; and is one of &#x60;CAMPAIGN&#x60;, &#x60;AD_SET&#x60;, or &#x60;AD&#x60;. Creative-level events are not forwarded.  Branch on &#x60;status.raw&#x60; to handle each transition; use &#x60;error.code&#x60; (when present) as the stable discriminator — &#x60;error.summary&#x60; and &#x60;error.message&#x60; are localized to the ad-account owner&#39;s Meta locale.  The &#x60;error&#x60; block is optional. It&#39;s present on most &#x60;WITH_ISSUES&#x60; events but can be absent (Meta does not always include diagnostics), and is never present on any other status. Always null-check &#x60;error&#x60; before reading &#x60;error.code&#x60;.  **Fan-out:** matching is keyed on &#x60;adObject.platformAdAccountId&#x60;. When multiple connected Zernio &#x60;metaads&#x60; accounts are linked to the same Meta ad account, each receives its own delivery. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdStatusChanged webhookPayloadAdStatusChanged = new WebhookPayloadAdStatusChanged(); // WebhookPayloadAdStatusChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onAdStatusChangedWithHttpInfo(webhookPayloadAdStatusChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdStatusChanged");
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
| **webhookPayloadAdStatusChanged** | [**WebhookPayloadAdStatusChanged**](WebhookPayloadAdStatusChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallEnded

> void onCallEnded(webhookPayloadCallEnded)

Call ended event

Fired on call hangup with the duration and a zero-markup billing breakdown (Meta cost, Telnyx cost, recording surcharge, total). Costs are pass-through; no margin is applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallEnded webhookPayloadCallEnded = new WebhookPayloadCallEnded(); // WebhookPayloadCallEnded | 
        try {
            apiInstance.onCallEnded(webhookPayloadCallEnded);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallEnded");
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
| **webhookPayloadCallEnded** | [**WebhookPayloadCallEnded**](WebhookPayloadCallEnded.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallEndedWithHttpInfo

> ApiResponse<Void> onCallEnded onCallEndedWithHttpInfo(webhookPayloadCallEnded)

Call ended event

Fired on call hangup with the duration and a zero-markup billing breakdown (Meta cost, Telnyx cost, recording surcharge, total). Costs are pass-through; no margin is applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallEnded webhookPayloadCallEnded = new WebhookPayloadCallEnded(); // WebhookPayloadCallEnded | 
        try {
            ApiResponse<Void> response = apiInstance.onCallEndedWithHttpInfo(webhookPayloadCallEnded);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallEnded");
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
| **webhookPayloadCallEnded** | [**WebhookPayloadCallEnded**](WebhookPayloadCallEnded.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallFailed

> void onCallFailed(webhookPayloadCallFailed)

Call failed event

Fired when a call setup or in-progress call fails (Meta rejected the connect, Telnyx returned an error, etc.). Payload carries the upstream error code and message. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallFailed webhookPayloadCallFailed = new WebhookPayloadCallFailed(); // WebhookPayloadCallFailed | 
        try {
            apiInstance.onCallFailed(webhookPayloadCallFailed);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallFailed");
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
| **webhookPayloadCallFailed** | [**WebhookPayloadCallFailed**](WebhookPayloadCallFailed.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallFailedWithHttpInfo

> ApiResponse<Void> onCallFailed onCallFailedWithHttpInfo(webhookPayloadCallFailed)

Call failed event

Fired when a call setup or in-progress call fails (Meta rejected the connect, Telnyx returned an error, etc.). Payload carries the upstream error code and message. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallFailed webhookPayloadCallFailed = new WebhookPayloadCallFailed(); // WebhookPayloadCallFailed | 
        try {
            ApiResponse<Void> response = apiInstance.onCallFailedWithHttpInfo(webhookPayloadCallFailed);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallFailed");
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
| **webhookPayloadCallFailed** | [**WebhookPayloadCallFailed**](WebhookPayloadCallFailed.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallPermissionRequest

> void onCallPermissionRequest(webhookPayloadCallPermissionRequest)

Call permission request reply event

Fired when a consumer replies to a &#x60;call_permission_request&#x60; interactive message (or its marketing-template variant). Carries the response (&#x60;accept&#x60; / &#x60;reject&#x60;), whether the grant is permanent, and the expiration timestamp when it is temporary. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallPermissionRequest webhookPayloadCallPermissionRequest = new WebhookPayloadCallPermissionRequest(); // WebhookPayloadCallPermissionRequest | 
        try {
            apiInstance.onCallPermissionRequest(webhookPayloadCallPermissionRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallPermissionRequest");
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
| **webhookPayloadCallPermissionRequest** | [**WebhookPayloadCallPermissionRequest**](WebhookPayloadCallPermissionRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallPermissionRequestWithHttpInfo

> ApiResponse<Void> onCallPermissionRequest onCallPermissionRequestWithHttpInfo(webhookPayloadCallPermissionRequest)

Call permission request reply event

Fired when a consumer replies to a &#x60;call_permission_request&#x60; interactive message (or its marketing-template variant). Carries the response (&#x60;accept&#x60; / &#x60;reject&#x60;), whether the grant is permanent, and the expiration timestamp when it is temporary. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallPermissionRequest webhookPayloadCallPermissionRequest = new WebhookPayloadCallPermissionRequest(); // WebhookPayloadCallPermissionRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onCallPermissionRequestWithHttpInfo(webhookPayloadCallPermissionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallPermissionRequest");
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
| **webhookPayloadCallPermissionRequest** | [**WebhookPayloadCallPermissionRequest**](WebhookPayloadCallPermissionRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallReceived

> void onCallReceived(webhookPayloadCallReceived)

Call received event

Fired when a WhatsApp Business Call connects. For inbound (UIC) calls the event fires at the moment our Telnyx trunk bridges the consumer leg to the customer&amp;apos;s forward-to destination; for outbound (BIC) calls it fires immediately after Meta accepts the connect. Branch on &#x60;call.direction&#x60; to distinguish. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallReceived webhookPayloadCallReceived = new WebhookPayloadCallReceived(); // WebhookPayloadCallReceived | 
        try {
            apiInstance.onCallReceived(webhookPayloadCallReceived);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallReceived");
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
| **webhookPayloadCallReceived** | [**WebhookPayloadCallReceived**](WebhookPayloadCallReceived.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallReceivedWithHttpInfo

> ApiResponse<Void> onCallReceived onCallReceivedWithHttpInfo(webhookPayloadCallReceived)

Call received event

Fired when a WhatsApp Business Call connects. For inbound (UIC) calls the event fires at the moment our Telnyx trunk bridges the consumer leg to the customer&amp;apos;s forward-to destination; for outbound (BIC) calls it fires immediately after Meta accepts the connect. Branch on &#x60;call.direction&#x60; to distinguish. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallReceived webhookPayloadCallReceived = new WebhookPayloadCallReceived(); // WebhookPayloadCallReceived | 
        try {
            ApiResponse<Void> response = apiInstance.onCallReceivedWithHttpInfo(webhookPayloadCallReceived);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallReceived");
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
| **webhookPayloadCallReceived** | [**WebhookPayloadCallReceived**](WebhookPayloadCallReceived.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommentReceived

> void onCommentReceived(webhookPayloadComment)

Comment received event

Fired when a new comment is received on a tracked post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadComment webhookPayloadComment = new WebhookPayloadComment(); // WebhookPayloadComment | 
        try {
            apiInstance.onCommentReceived(webhookPayloadComment);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommentReceived");
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
| **webhookPayloadComment** | [**WebhookPayloadComment**](WebhookPayloadComment.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommentReceivedWithHttpInfo

> ApiResponse<Void> onCommentReceived onCommentReceivedWithHttpInfo(webhookPayloadComment)

Comment received event

Fired when a new comment is received on a tracked post.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadComment webhookPayloadComment = new WebhookPayloadComment(); // WebhookPayloadComment | 
        try {
            ApiResponse<Void> response = apiInstance.onCommentReceivedWithHttpInfo(webhookPayloadComment);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommentReceived");
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
| **webhookPayloadComment** | [**WebhookPayloadComment**](WebhookPayloadComment.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onConversationStarted

> void onConversationStarted(webhookPayloadConversationStarted)

Conversation started event

Fired once when a new conversation begins between one of your connected accounts and a contact, in either direction. Works across every DM platform (Instagram, Messenger/Facebook, Telegram, WhatsApp, Twitter, Reddit, Bluesky). Naturally deduped — a given conversation only fires this event the very first time it appears. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadConversationStarted webhookPayloadConversationStarted = new WebhookPayloadConversationStarted(); // WebhookPayloadConversationStarted | 
        try {
            apiInstance.onConversationStarted(webhookPayloadConversationStarted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onConversationStarted");
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
| **webhookPayloadConversationStarted** | [**WebhookPayloadConversationStarted**](WebhookPayloadConversationStarted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onConversationStartedWithHttpInfo

> ApiResponse<Void> onConversationStarted onConversationStartedWithHttpInfo(webhookPayloadConversationStarted)

Conversation started event

Fired once when a new conversation begins between one of your connected accounts and a contact, in either direction. Works across every DM platform (Instagram, Messenger/Facebook, Telegram, WhatsApp, Twitter, Reddit, Bluesky). Naturally deduped — a given conversation only fires this event the very first time it appears. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadConversationStarted webhookPayloadConversationStarted = new WebhookPayloadConversationStarted(); // WebhookPayloadConversationStarted | 
        try {
            ApiResponse<Void> response = apiInstance.onConversationStartedWithHttpInfo(webhookPayloadConversationStarted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onConversationStarted");
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
| **webhookPayloadConversationStarted** | [**WebhookPayloadConversationStarted**](WebhookPayloadConversationStarted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onLeadReceived

> void onLeadReceived(webhookPayloadLead)

Lead received event

Fired when a new lead is submitted against a Meta Lead Gen (Instant) Form and ingested via the Page &#x60;leadgen&#x60; webhook. &#x60;lead.fields&#x60; is the question-key to answer map; &#x60;lead.formId&#x60; / &#x60;lead.adId&#x60; give provenance. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadLead webhookPayloadLead = new WebhookPayloadLead(); // WebhookPayloadLead | 
        try {
            apiInstance.onLeadReceived(webhookPayloadLead);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onLeadReceived");
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
| **webhookPayloadLead** | [**WebhookPayloadLead**](WebhookPayloadLead.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onLeadReceivedWithHttpInfo

> ApiResponse<Void> onLeadReceived onLeadReceivedWithHttpInfo(webhookPayloadLead)

Lead received event

Fired when a new lead is submitted against a Meta Lead Gen (Instant) Form and ingested via the Page &#x60;leadgen&#x60; webhook. &#x60;lead.fields&#x60; is the question-key to answer map; &#x60;lead.formId&#x60; / &#x60;lead.adId&#x60; give provenance. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadLead webhookPayloadLead = new WebhookPayloadLead(); // WebhookPayloadLead | 
        try {
            ApiResponse<Void> response = apiInstance.onLeadReceivedWithHttpInfo(webhookPayloadLead);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onLeadReceived");
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
| **webhookPayloadLead** | [**WebhookPayloadLead**](WebhookPayloadLead.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageDeleted

> void onMessageDeleted(webhookPayloadMessageDeleted)

Message deleted event

Fired when a sender deletes (unsends) a message. Supported on Instagram (incoming unsend) and WhatsApp (when the business deletes an outgoing message via the Cloud API). The payload retains the pre-delete text and attachments so API consumers can access the original content for moderation or compliance — the Zernio dashboard UI hides it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeleted webhookPayloadMessageDeleted = new WebhookPayloadMessageDeleted(); // WebhookPayloadMessageDeleted | 
        try {
            apiInstance.onMessageDeleted(webhookPayloadMessageDeleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDeleted");
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
| **webhookPayloadMessageDeleted** | [**WebhookPayloadMessageDeleted**](WebhookPayloadMessageDeleted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageDeletedWithHttpInfo

> ApiResponse<Void> onMessageDeleted onMessageDeletedWithHttpInfo(webhookPayloadMessageDeleted)

Message deleted event

Fired when a sender deletes (unsends) a message. Supported on Instagram (incoming unsend) and WhatsApp (when the business deletes an outgoing message via the Cloud API). The payload retains the pre-delete text and attachments so API consumers can access the original content for moderation or compliance — the Zernio dashboard UI hides it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeleted webhookPayloadMessageDeleted = new WebhookPayloadMessageDeleted(); // WebhookPayloadMessageDeleted | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageDeletedWithHttpInfo(webhookPayloadMessageDeleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDeleted");
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
| **webhookPayloadMessageDeleted** | [**WebhookPayloadMessageDeleted**](WebhookPayloadMessageDeleted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageDelivered

> void onMessageDelivered(webhookPayloadMessageDeliveryStatus)

Message delivered event

Fired when an outgoing message is delivered to the recipient. Supported on WhatsApp and Facebook Messenger. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            apiInstance.onMessageDelivered(webhookPayloadMessageDeliveryStatus);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDelivered");
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
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageDeliveredWithHttpInfo

> ApiResponse<Void> onMessageDelivered onMessageDeliveredWithHttpInfo(webhookPayloadMessageDeliveryStatus)

Message delivered event

Fired when an outgoing message is delivered to the recipient. Supported on WhatsApp and Facebook Messenger. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageDeliveredWithHttpInfo(webhookPayloadMessageDeliveryStatus);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDelivered");
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
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageEdited

> void onMessageEdited(webhookPayloadMessageEdited)

Message edited event

Fired when a sender edits a previously-sent message. Supported on Instagram, Facebook Messenger, and Telegram. The payload includes the full editHistory so consumers can show prior versions. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageEdited webhookPayloadMessageEdited = new WebhookPayloadMessageEdited(); // WebhookPayloadMessageEdited | 
        try {
            apiInstance.onMessageEdited(webhookPayloadMessageEdited);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageEdited");
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
| **webhookPayloadMessageEdited** | [**WebhookPayloadMessageEdited**](WebhookPayloadMessageEdited.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageEditedWithHttpInfo

> ApiResponse<Void> onMessageEdited onMessageEditedWithHttpInfo(webhookPayloadMessageEdited)

Message edited event

Fired when a sender edits a previously-sent message. Supported on Instagram, Facebook Messenger, and Telegram. The payload includes the full editHistory so consumers can show prior versions. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageEdited webhookPayloadMessageEdited = new WebhookPayloadMessageEdited(); // WebhookPayloadMessageEdited | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageEditedWithHttpInfo(webhookPayloadMessageEdited);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageEdited");
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
| **webhookPayloadMessageEdited** | [**WebhookPayloadMessageEdited**](WebhookPayloadMessageEdited.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageFailed

> void onMessageFailed(webhookPayloadMessageDeliveryStatus)

Message delivery failed event

Fired when an outgoing message fails to deliver. Currently only emitted for WhatsApp (other platforms don&#39;t expose per-message failure via webhook). The payload error object contains code, title, and message from the platform. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            apiInstance.onMessageFailed(webhookPayloadMessageDeliveryStatus);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageFailed");
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
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageFailedWithHttpInfo

> ApiResponse<Void> onMessageFailed onMessageFailedWithHttpInfo(webhookPayloadMessageDeliveryStatus)

Message delivery failed event

Fired when an outgoing message fails to deliver. Currently only emitted for WhatsApp (other platforms don&#39;t expose per-message failure via webhook). The payload error object contains code, title, and message from the platform. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageFailedWithHttpInfo(webhookPayloadMessageDeliveryStatus);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageFailed");
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
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageRead

> void onMessageRead(webhookPayloadMessageDeliveryStatus)

Message read event

Fired when an outgoing message is read by the recipient. Supported on WhatsApp, Facebook Messenger, and Instagram. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            apiInstance.onMessageRead(webhookPayloadMessageDeliveryStatus);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageRead");
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
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageReadWithHttpInfo

> ApiResponse<Void> onMessageRead onMessageReadWithHttpInfo(webhookPayloadMessageDeliveryStatus)

Message read event

Fired when an outgoing message is read by the recipient. Supported on WhatsApp, Facebook Messenger, and Instagram. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageReadWithHttpInfo(webhookPayloadMessageDeliveryStatus);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageRead");
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
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageReceived

> void onMessageReceived(webhookPayloadMessage)

Message received event

Fired when a new inbox message is received.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessage webhookPayloadMessage = new WebhookPayloadMessage(); // WebhookPayloadMessage | 
        try {
            apiInstance.onMessageReceived(webhookPayloadMessage);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageReceived");
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
| **webhookPayloadMessage** | [**WebhookPayloadMessage**](WebhookPayloadMessage.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageReceivedWithHttpInfo

> ApiResponse<Void> onMessageReceived onMessageReceivedWithHttpInfo(webhookPayloadMessage)

Message received event

Fired when a new inbox message is received.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessage webhookPayloadMessage = new WebhookPayloadMessage(); // WebhookPayloadMessage | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageReceivedWithHttpInfo(webhookPayloadMessage);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageReceived");
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
| **webhookPayloadMessage** | [**WebhookPayloadMessage**](WebhookPayloadMessage.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageSent

> void onMessageSent(webhookPayloadMessageSent)

Message sent event

Fired when a message is sent via the API.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageSent webhookPayloadMessageSent = new WebhookPayloadMessageSent(); // WebhookPayloadMessageSent | 
        try {
            apiInstance.onMessageSent(webhookPayloadMessageSent);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageSent");
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
| **webhookPayloadMessageSent** | [**WebhookPayloadMessageSent**](WebhookPayloadMessageSent.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageSentWithHttpInfo

> ApiResponse<Void> onMessageSent onMessageSentWithHttpInfo(webhookPayloadMessageSent)

Message sent event

Fired when a message is sent via the API.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageSent webhookPayloadMessageSent = new WebhookPayloadMessageSent(); // WebhookPayloadMessageSent | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageSentWithHttpInfo(webhookPayloadMessageSent);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageSent");
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
| **webhookPayloadMessageSent** | [**WebhookPayloadMessageSent**](WebhookPayloadMessageSent.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostCancelled

> void onPostCancelled(webhookPayloadPost)

Post cancelled event

Fired when a post publishing job is cancelled.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostCancelled(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostCancelled");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostCancelledWithHttpInfo

> ApiResponse<Void> onPostCancelled onPostCancelledWithHttpInfo(webhookPayloadPost)

Post cancelled event

Fired when a post publishing job is cancelled.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostCancelledWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostCancelled");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostExternalCreated

> void onPostExternalCreated(webhookPayloadExternalPost)

External post created event

Fired when Zernio&#39;s background sync detects a natively-authored post (created outside Zernio, e.g. a Google Business Profile localPost made in the Google UI) for the first time. Poll-driven (~hourly), not real-time. &#x60;post.source&#x60; is always \&quot;external\&quot;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            apiInstance.onPostExternalCreated(webhookPayloadExternalPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalCreated");
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
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostExternalCreatedWithHttpInfo

> ApiResponse<Void> onPostExternalCreated onPostExternalCreatedWithHttpInfo(webhookPayloadExternalPost)

External post created event

Fired when Zernio&#39;s background sync detects a natively-authored post (created outside Zernio, e.g. a Google Business Profile localPost made in the Google UI) for the first time. Poll-driven (~hourly), not real-time. &#x60;post.source&#x60; is always \&quot;external\&quot;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostExternalCreatedWithHttpInfo(webhookPayloadExternalPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalCreated");
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
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostExternalDeleted

> void onPostExternalDeleted(webhookPayloadExternalPost)

External post deleted event

Fired when a tracked native post is detected as removed from the platform. &#x60;post.deletedAt&#x60; carries the detection time. Coverage is bounded to the most recent posts the platform listing returns. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            apiInstance.onPostExternalDeleted(webhookPayloadExternalPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalDeleted");
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
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostExternalDeletedWithHttpInfo

> ApiResponse<Void> onPostExternalDeleted onPostExternalDeletedWithHttpInfo(webhookPayloadExternalPost)

External post deleted event

Fired when a tracked native post is detected as removed from the platform. &#x60;post.deletedAt&#x60; carries the detection time. Coverage is bounded to the most recent posts the platform listing returns. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostExternalDeletedWithHttpInfo(webhookPayloadExternalPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalDeleted");
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
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostExternalUpdated

> void onPostExternalUpdated(webhookPayloadExternalPost)

External post updated event

Fired when a tracked native post&#39;s text or media changed on the platform. Detected by comparing text/media structure and, where available, the platform&#39;s own edit timestamp; a media-URL-only refresh does not fire this. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            apiInstance.onPostExternalUpdated(webhookPayloadExternalPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalUpdated");
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
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostExternalUpdatedWithHttpInfo

> ApiResponse<Void> onPostExternalUpdated onPostExternalUpdatedWithHttpInfo(webhookPayloadExternalPost)

External post updated event

Fired when a tracked native post&#39;s text or media changed on the platform. Detected by comparing text/media structure and, where available, the platform&#39;s own edit timestamp; a media-URL-only refresh does not fire this. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostExternalUpdatedWithHttpInfo(webhookPayloadExternalPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalUpdated");
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
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostFailed

> void onPostFailed(webhookPayloadPost)

Post failed event

Fired when a post fails to publish on all target platforms.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostFailed(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostFailed");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostFailedWithHttpInfo

> ApiResponse<Void> onPostFailed onPostFailedWithHttpInfo(webhookPayloadPost)

Post failed event

Fired when a post fails to publish on all target platforms.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostFailedWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostFailed");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPartial

> void onPostPartial(webhookPayloadPost)

Post partial event

Fired when a post publishes on some platforms and fails on others.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostPartial(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPartial");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPartialWithHttpInfo

> ApiResponse<Void> onPostPartial onPostPartialWithHttpInfo(webhookPayloadPost)

Post partial event

Fired when a post publishes on some platforms and fails on others.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPartialWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPartial");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPlatformFailed

> void onPostPlatformFailed(webhookPayloadPostPlatform)

Post platform failed event

Fired once per platform target inside a post as that platform fails permanently. Temporary/retryable failures do NOT fire this event — only permanent ones, so retry loops stay quiet. The envelope event (&#x60;post.failed&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            apiInstance.onPostPlatformFailed(webhookPayloadPostPlatform);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformFailed");
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
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPlatformFailedWithHttpInfo

> ApiResponse<Void> onPostPlatformFailed onPostPlatformFailedWithHttpInfo(webhookPayloadPostPlatform)

Post platform failed event

Fired once per platform target inside a post as that platform fails permanently. Temporary/retryable failures do NOT fire this event — only permanent ones, so retry loops stay quiet. The envelope event (&#x60;post.failed&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPlatformFailedWithHttpInfo(webhookPayloadPostPlatform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformFailed");
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
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPlatformPublished

> void onPostPlatformPublished(webhookPayloadPostPlatform)

Post platform published event

Fired once per platform target inside a post as that platform finishes publishing successfully. Does NOT wait for the post-level rollup — consumers building incremental UIs get notified immediately, even when other platforms on the same post are still processing. The envelope event (&#x60;post.published&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            apiInstance.onPostPlatformPublished(webhookPayloadPostPlatform);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformPublished");
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
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPlatformPublishedWithHttpInfo

> ApiResponse<Void> onPostPlatformPublished onPostPlatformPublishedWithHttpInfo(webhookPayloadPostPlatform)

Post platform published event

Fired once per platform target inside a post as that platform finishes publishing successfully. Does NOT wait for the post-level rollup — consumers building incremental UIs get notified immediately, even when other platforms on the same post are still processing. The envelope event (&#x60;post.published&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPlatformPublishedWithHttpInfo(webhookPayloadPostPlatform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformPublished");
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
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPublished

> void onPostPublished(webhookPayloadPost)

Post published event

Fired when a post is successfully published.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostPublished(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPublished");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPublishedWithHttpInfo

> ApiResponse<Void> onPostPublished onPostPublishedWithHttpInfo(webhookPayloadPost)

Post published event

Fired when a post is successfully published.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPublishedWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPublished");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostRecycled

> void onPostRecycled(webhookPayloadPost)

Post recycled event

Fired when a post is recycled (cloned and re-scheduled for publishing).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostRecycled(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostRecycled");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostRecycledWithHttpInfo

> ApiResponse<Void> onPostRecycled onPostRecycledWithHttpInfo(webhookPayloadPost)

Post recycled event

Fired when a post is recycled (cloned and re-scheduled for publishing).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostRecycledWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostRecycled");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostScheduled

> void onPostScheduled(webhookPayloadPost)

Post scheduled event

Fired when a post is created and scheduled for publishing.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostScheduled(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostScheduled");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostScheduledWithHttpInfo

> ApiResponse<Void> onPostScheduled onPostScheduledWithHttpInfo(webhookPayloadPost)

Post scheduled event

Fired when a post is created and scheduled for publishing.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostScheduledWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostScheduled");
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
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onReactionReceived

> void onReactionReceived(webhookPayloadReaction)

Reaction received event

Fired when a participant adds or removes an emoji reaction on a message. Supported on WhatsApp and Telegram. Distinct from message.received so a reaction (e.g. a thumbs-up) is not mistaken for an inbound message. The &#x60;reaction.action&#x60; field is &#x60;added&#x60; or &#x60;removed&#x60;. On WhatsApp removals the platform does not report which emoji was removed, so &#x60;reaction.emoji&#x60; may be an empty string. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReaction webhookPayloadReaction = new WebhookPayloadReaction(); // WebhookPayloadReaction | 
        try {
            apiInstance.onReactionReceived(webhookPayloadReaction);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReactionReceived");
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
| **webhookPayloadReaction** | [**WebhookPayloadReaction**](WebhookPayloadReaction.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onReactionReceivedWithHttpInfo

> ApiResponse<Void> onReactionReceived onReactionReceivedWithHttpInfo(webhookPayloadReaction)

Reaction received event

Fired when a participant adds or removes an emoji reaction on a message. Supported on WhatsApp and Telegram. Distinct from message.received so a reaction (e.g. a thumbs-up) is not mistaken for an inbound message. The &#x60;reaction.action&#x60; field is &#x60;added&#x60; or &#x60;removed&#x60;. On WhatsApp removals the platform does not report which emoji was removed, so &#x60;reaction.emoji&#x60; may be an empty string. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReaction webhookPayloadReaction = new WebhookPayloadReaction(); // WebhookPayloadReaction | 
        try {
            ApiResponse<Void> response = apiInstance.onReactionReceivedWithHttpInfo(webhookPayloadReaction);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReactionReceived");
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
| **webhookPayloadReaction** | [**WebhookPayloadReaction**](WebhookPayloadReaction.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onReviewNew

> void onReviewNew(webhookPayloadReviewNew)

Review new event

Fired when a new review is posted on a connected account. Currently supported for Google Business Profile (real-time via Pub/Sub). Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewNew webhookPayloadReviewNew = new WebhookPayloadReviewNew(); // WebhookPayloadReviewNew | 
        try {
            apiInstance.onReviewNew(webhookPayloadReviewNew);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewNew");
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
| **webhookPayloadReviewNew** | [**WebhookPayloadReviewNew**](WebhookPayloadReviewNew.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onReviewNewWithHttpInfo

> ApiResponse<Void> onReviewNew onReviewNewWithHttpInfo(webhookPayloadReviewNew)

Review new event

Fired when a new review is posted on a connected account. Currently supported for Google Business Profile (real-time via Pub/Sub). Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewNew webhookPayloadReviewNew = new WebhookPayloadReviewNew(); // WebhookPayloadReviewNew | 
        try {
            ApiResponse<Void> response = apiInstance.onReviewNewWithHttpInfo(webhookPayloadReviewNew);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewNew");
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
| **webhookPayloadReviewNew** | [**WebhookPayloadReviewNew**](WebhookPayloadReviewNew.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onReviewUpdated

> void onReviewUpdated(webhookPayloadReviewUpdated)

Review updated event

Fired when a review changes: the reviewer edits their text or rating, or a reply is added (via the API or directly through the Google Business dashboard). Payload shape matches review.new. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewUpdated webhookPayloadReviewUpdated = new WebhookPayloadReviewUpdated(); // WebhookPayloadReviewUpdated | 
        try {
            apiInstance.onReviewUpdated(webhookPayloadReviewUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewUpdated");
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
| **webhookPayloadReviewUpdated** | [**WebhookPayloadReviewUpdated**](WebhookPayloadReviewUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onReviewUpdatedWithHttpInfo

> ApiResponse<Void> onReviewUpdated onReviewUpdatedWithHttpInfo(webhookPayloadReviewUpdated)

Review updated event

Fired when a review changes: the reviewer edits their text or rating, or a reply is added (via the API or directly through the Google Business dashboard). Payload shape matches review.new. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewUpdated webhookPayloadReviewUpdated = new WebhookPayloadReviewUpdated(); // WebhookPayloadReviewUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onReviewUpdatedWithHttpInfo(webhookPayloadReviewUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewUpdated");
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
| **webhookPayloadReviewUpdated** | [**WebhookPayloadReviewUpdated**](WebhookPayloadReviewUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWebhookTest

> void onWebhookTest(webhookPayloadTest)

Webhook test event

Fired when sending a test webhook to verify the endpoint configuration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadTest webhookPayloadTest = new WebhookPayloadTest(); // WebhookPayloadTest | 
        try {
            apiInstance.onWebhookTest(webhookPayloadTest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWebhookTest");
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
| **webhookPayloadTest** | [**WebhookPayloadTest**](WebhookPayloadTest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWebhookTestWithHttpInfo

> ApiResponse<Void> onWebhookTest onWebhookTestWithHttpInfo(webhookPayloadTest)

Webhook test event

Fired when sending a test webhook to verify the endpoint configuration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadTest webhookPayloadTest = new WebhookPayloadTest(); // WebhookPayloadTest | 
        try {
            ApiResponse<Void> response = apiInstance.onWebhookTestWithHttpInfo(webhookPayloadTest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWebhookTest");
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
| **webhookPayloadTest** | [**WebhookPayloadTest**](WebhookPayloadTest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberActivated

> void onWhatsAppNumberActivated(onWhatsAppNumberActivatedRequest)

WhatsApp number activated event

Fired when a purchased WhatsApp number becomes active and usable — both the synchronous (Tier 1/2) path and the asynchronous regulated (Tier 3/4) path land here. Lets integrators react without polling GET /v1/whatsapp/phone-numbers. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberActivatedRequest onWhatsAppNumberActivatedRequest = new OnWhatsAppNumberActivatedRequest(); // OnWhatsAppNumberActivatedRequest | 
        try {
            apiInstance.onWhatsAppNumberActivated(onWhatsAppNumberActivatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberActivated");
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
| **onWhatsAppNumberActivatedRequest** | [**OnWhatsAppNumberActivatedRequest**](OnWhatsAppNumberActivatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberActivatedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberActivated onWhatsAppNumberActivatedWithHttpInfo(onWhatsAppNumberActivatedRequest)

WhatsApp number activated event

Fired when a purchased WhatsApp number becomes active and usable — both the synchronous (Tier 1/2) path and the asynchronous regulated (Tier 3/4) path land here. Lets integrators react without polling GET /v1/whatsapp/phone-numbers. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberActivatedRequest onWhatsAppNumberActivatedRequest = new OnWhatsAppNumberActivatedRequest(); // OnWhatsAppNumberActivatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberActivatedWithHttpInfo(onWhatsAppNumberActivatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberActivated");
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
| **onWhatsAppNumberActivatedRequest** | [**OnWhatsAppNumberActivatedRequest**](OnWhatsAppNumberActivatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberDeclined

> void onWhatsAppNumberDeclined(onWhatsAppNumberDeclinedRequest)

WhatsApp number declined event

Fired when a regulated (Tier 3/4) number order is declined or fails review. The number is never billed. &#x60;reason&#x60; carries the reviewer&#39;s rejection reason when available. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberDeclinedRequest onWhatsAppNumberDeclinedRequest = new OnWhatsAppNumberDeclinedRequest(); // OnWhatsAppNumberDeclinedRequest | 
        try {
            apiInstance.onWhatsAppNumberDeclined(onWhatsAppNumberDeclinedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberDeclined");
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
| **onWhatsAppNumberDeclinedRequest** | [**OnWhatsAppNumberDeclinedRequest**](OnWhatsAppNumberDeclinedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberDeclinedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberDeclined onWhatsAppNumberDeclinedWithHttpInfo(onWhatsAppNumberDeclinedRequest)

WhatsApp number declined event

Fired when a regulated (Tier 3/4) number order is declined or fails review. The number is never billed. &#x60;reason&#x60; carries the reviewer&#39;s rejection reason when available. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberDeclinedRequest onWhatsAppNumberDeclinedRequest = new OnWhatsAppNumberDeclinedRequest(); // OnWhatsAppNumberDeclinedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberDeclinedWithHttpInfo(onWhatsAppNumberDeclinedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberDeclined");
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
| **onWhatsAppNumberDeclinedRequest** | [**OnWhatsAppNumberDeclinedRequest**](OnWhatsAppNumberDeclinedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberReactivated

> void onWhatsAppNumberReactivated(onWhatsAppNumberReactivatedRequest)

WhatsApp number reactivated event

Fired when a suspended number is reactivated (e.g. the payment recovered) and is usable again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReactivatedRequest onWhatsAppNumberReactivatedRequest = new OnWhatsAppNumberReactivatedRequest(); // OnWhatsAppNumberReactivatedRequest | 
        try {
            apiInstance.onWhatsAppNumberReactivated(onWhatsAppNumberReactivatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReactivated");
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
| **onWhatsAppNumberReactivatedRequest** | [**OnWhatsAppNumberReactivatedRequest**](OnWhatsAppNumberReactivatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberReactivatedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberReactivated onWhatsAppNumberReactivatedWithHttpInfo(onWhatsAppNumberReactivatedRequest)

WhatsApp number reactivated event

Fired when a suspended number is reactivated (e.g. the payment recovered) and is usable again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReactivatedRequest onWhatsAppNumberReactivatedRequest = new OnWhatsAppNumberReactivatedRequest(); // OnWhatsAppNumberReactivatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberReactivatedWithHttpInfo(onWhatsAppNumberReactivatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReactivated");
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
| **onWhatsAppNumberReactivatedRequest** | [**OnWhatsAppNumberReactivatedRequest**](OnWhatsAppNumberReactivatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberReleased

> void onWhatsAppNumberReleased(onWhatsAppNumberReleasedRequest)

WhatsApp number released event

Fired when a number is released and is no longer usable (by the user, a billing cleanup, or an admin). Terminal. &#x60;reason&#x60; carries the cause (e.g. &#x60;user_requested&#x60;, &#x60;cleanup_suspended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReleasedRequest onWhatsAppNumberReleasedRequest = new OnWhatsAppNumberReleasedRequest(); // OnWhatsAppNumberReleasedRequest | 
        try {
            apiInstance.onWhatsAppNumberReleased(onWhatsAppNumberReleasedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReleased");
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
| **onWhatsAppNumberReleasedRequest** | [**OnWhatsAppNumberReleasedRequest**](OnWhatsAppNumberReleasedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberReleasedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberReleased onWhatsAppNumberReleasedWithHttpInfo(onWhatsAppNumberReleasedRequest)

WhatsApp number released event

Fired when a number is released and is no longer usable (by the user, a billing cleanup, or an admin). Terminal. &#x60;reason&#x60; carries the cause (e.g. &#x60;user_requested&#x60;, &#x60;cleanup_suspended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReleasedRequest onWhatsAppNumberReleasedRequest = new OnWhatsAppNumberReleasedRequest(); // OnWhatsAppNumberReleasedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberReleasedWithHttpInfo(onWhatsAppNumberReleasedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReleased");
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
| **onWhatsAppNumberReleasedRequest** | [**OnWhatsAppNumberReleasedRequest**](OnWhatsAppNumberReleasedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberSuspended

> void onWhatsAppNumberSuspended(onWhatsAppNumberSuspendedRequest)

WhatsApp number suspended event

Fired when an active number is suspended (e.g. a failed payment). The number stops working until the issue is resolved, after which a &#x60;whatsapp.number.reactivated&#x60; event is sent. &#x60;reason&#x60; carries the cause (e.g. &#x60;payment_failed&#x60;, &#x60;subscription_ended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberSuspendedRequest onWhatsAppNumberSuspendedRequest = new OnWhatsAppNumberSuspendedRequest(); // OnWhatsAppNumberSuspendedRequest | 
        try {
            apiInstance.onWhatsAppNumberSuspended(onWhatsAppNumberSuspendedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberSuspended");
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
| **onWhatsAppNumberSuspendedRequest** | [**OnWhatsAppNumberSuspendedRequest**](OnWhatsAppNumberSuspendedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberSuspendedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberSuspended onWhatsAppNumberSuspendedWithHttpInfo(onWhatsAppNumberSuspendedRequest)

WhatsApp number suspended event

Fired when an active number is suspended (e.g. a failed payment). The number stops working until the issue is resolved, after which a &#x60;whatsapp.number.reactivated&#x60; event is sent. &#x60;reason&#x60; carries the cause (e.g. &#x60;payment_failed&#x60;, &#x60;subscription_ended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberSuspendedRequest onWhatsAppNumberSuspendedRequest = new OnWhatsAppNumberSuspendedRequest(); // OnWhatsAppNumberSuspendedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberSuspendedWithHttpInfo(onWhatsAppNumberSuspendedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberSuspended");
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
| **onWhatsAppNumberSuspendedRequest** | [**OnWhatsAppNumberSuspendedRequest**](OnWhatsAppNumberSuspendedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberVerificationRequired

> void onWhatsAppNumberVerificationRequired(onWhatsAppNumberVerificationRequiredRequest)

WhatsApp number verification-required event

Fired when a regulated number has an out-of-band identity-verification step (e.g. Onfido). &#x60;verificationUrl&#x60; is the link to forward to the number&#39;s end user; the order completes once they pass. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberVerificationRequiredRequest onWhatsAppNumberVerificationRequiredRequest = new OnWhatsAppNumberVerificationRequiredRequest(); // OnWhatsAppNumberVerificationRequiredRequest | 
        try {
            apiInstance.onWhatsAppNumberVerificationRequired(onWhatsAppNumberVerificationRequiredRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberVerificationRequired");
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
| **onWhatsAppNumberVerificationRequiredRequest** | [**OnWhatsAppNumberVerificationRequiredRequest**](OnWhatsAppNumberVerificationRequiredRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberVerificationRequiredWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberVerificationRequired onWhatsAppNumberVerificationRequiredWithHttpInfo(onWhatsAppNumberVerificationRequiredRequest)

WhatsApp number verification-required event

Fired when a regulated number has an out-of-band identity-verification step (e.g. Onfido). &#x60;verificationUrl&#x60; is the link to forward to the number&#39;s end user; the order completes once they pass. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberVerificationRequiredRequest onWhatsAppNumberVerificationRequiredRequest = new OnWhatsAppNumberVerificationRequiredRequest(); // OnWhatsAppNumberVerificationRequiredRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberVerificationRequiredWithHttpInfo(onWhatsAppNumberVerificationRequiredRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberVerificationRequired");
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
| **onWhatsAppNumberVerificationRequiredRequest** | [**OnWhatsAppNumberVerificationRequiredRequest**](OnWhatsAppNumberVerificationRequiredRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppTemplateStatusUpdated

> void onWhatsAppTemplateStatusUpdated(webhookPayloadWhatsAppTemplateStatusUpdated)

WhatsApp template status updated event

Fired when Meta finishes (re)reviewing a WhatsApp Business template attached to a connected WABA. Forwarded from Meta&#39;s &#x60;message_template_status_update&#x60; webhook field on the WhatsApp Business Account. Consumers branch on &#x60;template.status&#x60; (APPROVED, REJECTED, PENDING, PAUSED, DISABLED, IN_APPEAL, PENDING_DELETION). Meta does not include the previous status or the template&#39;s category in this event. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppTemplateStatusUpdated webhookPayloadWhatsAppTemplateStatusUpdated = new WebhookPayloadWhatsAppTemplateStatusUpdated(); // WebhookPayloadWhatsAppTemplateStatusUpdated | 
        try {
            apiInstance.onWhatsAppTemplateStatusUpdated(webhookPayloadWhatsAppTemplateStatusUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppTemplateStatusUpdated");
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
| **webhookPayloadWhatsAppTemplateStatusUpdated** | [**WebhookPayloadWhatsAppTemplateStatusUpdated**](WebhookPayloadWhatsAppTemplateStatusUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppTemplateStatusUpdatedWithHttpInfo

> ApiResponse<Void> onWhatsAppTemplateStatusUpdated onWhatsAppTemplateStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppTemplateStatusUpdated)

WhatsApp template status updated event

Fired when Meta finishes (re)reviewing a WhatsApp Business template attached to a connected WABA. Forwarded from Meta&#39;s &#x60;message_template_status_update&#x60; webhook field on the WhatsApp Business Account. Consumers branch on &#x60;template.status&#x60; (APPROVED, REJECTED, PENDING, PAUSED, DISABLED, IN_APPEAL, PENDING_DELETION). Meta does not include the previous status or the template&#39;s category in this event. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppTemplateStatusUpdated webhookPayloadWhatsAppTemplateStatusUpdated = new WebhookPayloadWhatsAppTemplateStatusUpdated(); // WebhookPayloadWhatsAppTemplateStatusUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppTemplateStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppTemplateStatusUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppTemplateStatusUpdated");
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
| **webhookPayloadWhatsAppTemplateStatusUpdated** | [**WebhookPayloadWhatsAppTemplateStatusUpdated**](WebhookPayloadWhatsAppTemplateStatusUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

