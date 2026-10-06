# CommentAutomationsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCommentAutomation**](CommentAutomationsApi.md#createCommentAutomation) | **POST** /v1/comment-automations | Create comment-to-DM automation |
| [**createCommentAutomationWithHttpInfo**](CommentAutomationsApi.md#createCommentAutomationWithHttpInfo) | **POST** /v1/comment-automations | Create comment-to-DM automation |
| [**deleteCommentAutomation**](CommentAutomationsApi.md#deleteCommentAutomation) | **DELETE** /v1/comment-automations/{automationId} | Delete automation |
| [**deleteCommentAutomationWithHttpInfo**](CommentAutomationsApi.md#deleteCommentAutomationWithHttpInfo) | **DELETE** /v1/comment-automations/{automationId} | Delete automation |
| [**getCommentAutomation**](CommentAutomationsApi.md#getCommentAutomation) | **GET** /v1/comment-automations/{automationId} | Get automation details |
| [**getCommentAutomationWithHttpInfo**](CommentAutomationsApi.md#getCommentAutomationWithHttpInfo) | **GET** /v1/comment-automations/{automationId} | Get automation details |
| [**listCommentAutomationLogs**](CommentAutomationsApi.md#listCommentAutomationLogs) | **GET** /v1/comment-automations/{automationId}/logs | List automation logs |
| [**listCommentAutomationLogsWithHttpInfo**](CommentAutomationsApi.md#listCommentAutomationLogsWithHttpInfo) | **GET** /v1/comment-automations/{automationId}/logs | List automation logs |
| [**listCommentAutomations**](CommentAutomationsApi.md#listCommentAutomations) | **GET** /v1/comment-automations | List comment-to-DM automations |
| [**listCommentAutomationsWithHttpInfo**](CommentAutomationsApi.md#listCommentAutomationsWithHttpInfo) | **GET** /v1/comment-automations | List comment-to-DM automations |
| [**updateCommentAutomation**](CommentAutomationsApi.md#updateCommentAutomation) | **PATCH** /v1/comment-automations/{automationId} | Update automation settings |
| [**updateCommentAutomationWithHttpInfo**](CommentAutomationsApi.md#updateCommentAutomationWithHttpInfo) | **PATCH** /v1/comment-automations/{automationId} | Update automation settings |



## createCommentAutomation

> CreateCommentAutomation200Response createCommentAutomation(createCommentAutomationRequest)

Create comment-to-DM automation

Create a keyword-triggered automation. On Instagram and Facebook, when someone comments a matching keyword (or, with &#x60;trigger: story_reply&#x60;, replies to your Instagram story with one), they automatically receive a DM.  Platforms:   * &#x60;instagram&#x60;, &#x60;facebook&#x60;: the full DM automation (private reply, buttons,     product card, audience rules, follow gate) plus the optional public reply.   * &#x60;tiktok&#x60;, &#x60;threads&#x60;, &#x60;linkedin&#x60;, &#x60;youtube&#x60;: public reply only. These     platforms have no private reply to a comment, so the automation answers a     matching comment with &#x60;commentReply&#x60; and nothing else. &#x60;commentReply&#x60; is     required and the DM fields (&#x60;dmMessage&#x60;, &#x60;dmMessageVariations&#x60;, &#x60;buttons&#x60;,     &#x60;template&#x60;, &#x60;quickReplies&#x60;, &#x60;alsoMatchInDms&#x60;, &#x60;audience&#x60;, &#x60;followGate&#x60;,     &#x60;dmDelaySeconds&#x60;, &#x60;commentReplyDelaySeconds&#x60;) are rejected with a 400 naming the     field. TikTok comments arrive by webhook (TikTok business accounts only); the     others are read by the comment poll, so a reply follows the comment by up to the     poll interval (10 minutes on posts from the last 24 hours, longer on older posts).     &#x60;repeatPolicy&#x60; applies there too: with the default &#x60;once&#x60;, a person gets one public     reply per automation, and their later comments get none.   * X accounts are refused with a 400 (&#x60;platform_not_supported&#x60;): X comment polling is     off, so an X automation could never fire.  To continue into a specific workflow after the recipient taps a button, use &#x60;{\&quot;type\&quot;:\&quot;postback\&quot;,\&quot;title\&quot;:\&quot;Send it\&quot;,\&quot;payload\&quot;:\&quot;zernio:workflow:&lt;workflowId&gt;\&quot;}&#x60;. The target must be active and belong to the same account and profile. This also works for product-card buttons. The tap starts that workflow directly, without matching its keyword or first-message condition. A tap on a workflow that is waiting on &#x60;wait_for_reply&#x60; in that conversation answers that wait and resumes the run. A tap on a different active workflow starts it and exits the other live runs. Stale or invalid targets still do nothing. The initial comment DM alone does not start the workflow: the recipient must tap.  Triggers (&#x60;trigger&#x60;):   * &#x60;comment&#x60; (default): fires on keyword comments on a post or reel.   * &#x60;story_reply&#x60;: fires when someone replies to your Instagram story with a keyword,     and answers them with a DM. Set &#x60;platformPostId&#x60; to a story media id to scope to     one story, or omit it to match replies to any story.   * &#x60;live_comment&#x60; (Instagram only): fires on keyword comments made during one of     your Instagram live broadcasts and answers them with a private reply. &#x60;comment&#x60;     automations never fire on live comments, and &#x60;live_comment&#x60; ones never fire on     post comments. Meta only accepts the private reply while the broadcast is live.   * &#x60;story_mention&#x60; (Instagram only): fires when someone mentions your account in     their story, and answers them with a DM. A mention carries no text and Meta does     not identify the story, so &#x60;keywords&#x60; must be empty and &#x60;platformPostId&#x60; omitted.  Comments on Instagram and Facebook arrive by webhook. Every 10 minutes Zernio also reads the latest comments and replies back (the bound post, or the 5 newest posts for an account-wide automation, up to 20 Graph reads per account per run; a post not fully read is picked up again on the next run) and runs any comment the webhook did not deliver, so a dropped webhook still fires. A comment is answered at most once whichever path sees it first.  Targeting (comment trigger):   * Per-post: set &#x60;platformPostId&#x60; to scope to one specific post (only one active     per-post automation is allowed per post).   * Account-wide (\&quot;any post\&quot;): omit &#x60;platformPostId&#x60; (and &#x60;postId&#x60;). The automation     evaluates every comment on every post on the account. You can stack unlimited     account-wide automations, each with its own keyword set, and they all run     independently. Per-post automations take priority on their post.  Audience (&#x60;audience&#x60;, Instagram only): restrict the automation to followers or non-followers, and/or to accounts above a follower count. Instagram only reveals the follow relationship for people who have messaged the account, so &#x60;audience.whenUnknown&#x60; decides what happens for everyone else - including &#x60;verify&#x60;, which sends a one-tap confirmation DM (&#x60;followGate&#x60;) and then delivers the real DM automatically. People we already know follow you skip the tap entirely. Set &#x60;audience.tapToUnlock: true&#x60; instead to send that button DM to every commenter and deliver the real DM on the tap with no follow check.  Set &#x60;alsoMatchInDms: true&#x60; on a &#x60;comment&#x60; automation to also answer people who send a keyword as a direct message instead of commenting it. One automation then covers both doors, and each door is deduplicated separately (someone who already got the DM from their comment still gets it if they later DM the keyword). Requires at least one keyword.  Links in the DM&#39;s buttons can be click-tracked (&#x60;linkTracking&#x60;, on by default) and clickers optionally tagged (&#x60;clickTag&#x60;) for segmentation. Stats returned include delivered, read, and link clicks.  Personalisation: &#x60;{{first_name}}&#x60;, &#x60;{{name}}&#x60; and &#x60;{{username}}&#x60; in &#x60;dmMessage&#x60;, &#x60;commentReply&#x60;, their variations and button titles resolve from the commenter (first word of the display name, the display name, the platform username). A value the platform does not give us resolves to an empty string.  Behaviour: &#x60;repeatPolicy&#x60; decides whether a person can get the DM again, &#x60;dedupeSameTextHours&#x60; stops two automations sending the same text to one person, &#x60;publicReplyPolicy&#x60; decides whether the public reply waits for the DM, and &#x60;actions&#x60; likes or hides the matched comment. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        CreateCommentAutomationRequest createCommentAutomationRequest = new CreateCommentAutomationRequest(); // CreateCommentAutomationRequest | 
        try {
            CreateCommentAutomation200Response result = apiInstance.createCommentAutomation(createCommentAutomationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#createCommentAutomation");
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
| **createCommentAutomationRequest** | [**CreateCommentAutomationRequest**](CreateCommentAutomationRequest.md)|  | |

### Return type

[**CreateCommentAutomation200Response**](CreateCommentAutomation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation created |  -  |
| **400** | Validation error. Includes an account on an unsupported platform such as X (code platform_not_supported), a DM field (dmMessage, buttons, template, quickReplies, alsoMatchInDms, audience, followGate, a delay, dmMedia, dedupeSameTextHours, actions) sent for a TikTok, Threads, LinkedIn or YouTube account (code invalid_field_value, param names the field), a missing commentReply there or a missing dmMessage on Instagram and Facebook (code missing_required_field), and a live_comment, story_reply or story_mention trigger outside Instagram. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **409** | Active per-post automation already exists for this platformPostId. Does not apply to account-wide automations. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## createCommentAutomationWithHttpInfo

> ApiResponse<CreateCommentAutomation200Response> createCommentAutomation createCommentAutomationWithHttpInfo(createCommentAutomationRequest)

Create comment-to-DM automation

Create a keyword-triggered automation. On Instagram and Facebook, when someone comments a matching keyword (or, with &#x60;trigger: story_reply&#x60;, replies to your Instagram story with one), they automatically receive a DM.  Platforms:   * &#x60;instagram&#x60;, &#x60;facebook&#x60;: the full DM automation (private reply, buttons,     product card, audience rules, follow gate) plus the optional public reply.   * &#x60;tiktok&#x60;, &#x60;threads&#x60;, &#x60;linkedin&#x60;, &#x60;youtube&#x60;: public reply only. These     platforms have no private reply to a comment, so the automation answers a     matching comment with &#x60;commentReply&#x60; and nothing else. &#x60;commentReply&#x60; is     required and the DM fields (&#x60;dmMessage&#x60;, &#x60;dmMessageVariations&#x60;, &#x60;buttons&#x60;,     &#x60;template&#x60;, &#x60;quickReplies&#x60;, &#x60;alsoMatchInDms&#x60;, &#x60;audience&#x60;, &#x60;followGate&#x60;,     &#x60;dmDelaySeconds&#x60;, &#x60;commentReplyDelaySeconds&#x60;) are rejected with a 400 naming the     field. TikTok comments arrive by webhook (TikTok business accounts only); the     others are read by the comment poll, so a reply follows the comment by up to the     poll interval (10 minutes on posts from the last 24 hours, longer on older posts).     &#x60;repeatPolicy&#x60; applies there too: with the default &#x60;once&#x60;, a person gets one public     reply per automation, and their later comments get none.   * X accounts are refused with a 400 (&#x60;platform_not_supported&#x60;): X comment polling is     off, so an X automation could never fire.  To continue into a specific workflow after the recipient taps a button, use &#x60;{\&quot;type\&quot;:\&quot;postback\&quot;,\&quot;title\&quot;:\&quot;Send it\&quot;,\&quot;payload\&quot;:\&quot;zernio:workflow:&lt;workflowId&gt;\&quot;}&#x60;. The target must be active and belong to the same account and profile. This also works for product-card buttons. The tap starts that workflow directly, without matching its keyword or first-message condition. A tap on a workflow that is waiting on &#x60;wait_for_reply&#x60; in that conversation answers that wait and resumes the run. A tap on a different active workflow starts it and exits the other live runs. Stale or invalid targets still do nothing. The initial comment DM alone does not start the workflow: the recipient must tap.  Triggers (&#x60;trigger&#x60;):   * &#x60;comment&#x60; (default): fires on keyword comments on a post or reel.   * &#x60;story_reply&#x60;: fires when someone replies to your Instagram story with a keyword,     and answers them with a DM. Set &#x60;platformPostId&#x60; to a story media id to scope to     one story, or omit it to match replies to any story.   * &#x60;live_comment&#x60; (Instagram only): fires on keyword comments made during one of     your Instagram live broadcasts and answers them with a private reply. &#x60;comment&#x60;     automations never fire on live comments, and &#x60;live_comment&#x60; ones never fire on     post comments. Meta only accepts the private reply while the broadcast is live.   * &#x60;story_mention&#x60; (Instagram only): fires when someone mentions your account in     their story, and answers them with a DM. A mention carries no text and Meta does     not identify the story, so &#x60;keywords&#x60; must be empty and &#x60;platformPostId&#x60; omitted.  Comments on Instagram and Facebook arrive by webhook. Every 10 minutes Zernio also reads the latest comments and replies back (the bound post, or the 5 newest posts for an account-wide automation, up to 20 Graph reads per account per run; a post not fully read is picked up again on the next run) and runs any comment the webhook did not deliver, so a dropped webhook still fires. A comment is answered at most once whichever path sees it first.  Targeting (comment trigger):   * Per-post: set &#x60;platformPostId&#x60; to scope to one specific post (only one active     per-post automation is allowed per post).   * Account-wide (\&quot;any post\&quot;): omit &#x60;platformPostId&#x60; (and &#x60;postId&#x60;). The automation     evaluates every comment on every post on the account. You can stack unlimited     account-wide automations, each with its own keyword set, and they all run     independently. Per-post automations take priority on their post.  Audience (&#x60;audience&#x60;, Instagram only): restrict the automation to followers or non-followers, and/or to accounts above a follower count. Instagram only reveals the follow relationship for people who have messaged the account, so &#x60;audience.whenUnknown&#x60; decides what happens for everyone else - including &#x60;verify&#x60;, which sends a one-tap confirmation DM (&#x60;followGate&#x60;) and then delivers the real DM automatically. People we already know follow you skip the tap entirely. Set &#x60;audience.tapToUnlock: true&#x60; instead to send that button DM to every commenter and deliver the real DM on the tap with no follow check.  Set &#x60;alsoMatchInDms: true&#x60; on a &#x60;comment&#x60; automation to also answer people who send a keyword as a direct message instead of commenting it. One automation then covers both doors, and each door is deduplicated separately (someone who already got the DM from their comment still gets it if they later DM the keyword). Requires at least one keyword.  Links in the DM&#39;s buttons can be click-tracked (&#x60;linkTracking&#x60;, on by default) and clickers optionally tagged (&#x60;clickTag&#x60;) for segmentation. Stats returned include delivered, read, and link clicks.  Personalisation: &#x60;{{first_name}}&#x60;, &#x60;{{name}}&#x60; and &#x60;{{username}}&#x60; in &#x60;dmMessage&#x60;, &#x60;commentReply&#x60;, their variations and button titles resolve from the commenter (first word of the display name, the display name, the platform username). A value the platform does not give us resolves to an empty string.  Behaviour: &#x60;repeatPolicy&#x60; decides whether a person can get the DM again, &#x60;dedupeSameTextHours&#x60; stops two automations sending the same text to one person, &#x60;publicReplyPolicy&#x60; decides whether the public reply waits for the DM, and &#x60;actions&#x60; likes or hides the matched comment. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        CreateCommentAutomationRequest createCommentAutomationRequest = new CreateCommentAutomationRequest(); // CreateCommentAutomationRequest | 
        try {
            ApiResponse<CreateCommentAutomation200Response> response = apiInstance.createCommentAutomationWithHttpInfo(createCommentAutomationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#createCommentAutomation");
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
| **createCommentAutomationRequest** | [**CreateCommentAutomationRequest**](CreateCommentAutomationRequest.md)|  | |

### Return type

ApiResponse<[**CreateCommentAutomation200Response**](CreateCommentAutomation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation created |  -  |
| **400** | Validation error. Includes an account on an unsupported platform such as X (code platform_not_supported), a DM field (dmMessage, buttons, template, quickReplies, alsoMatchInDms, audience, followGate, a delay, dmMedia, dedupeSameTextHours, actions) sent for a TikTok, Threads, LinkedIn or YouTube account (code invalid_field_value, param names the field), a missing commentReply there or a missing dmMessage on Instagram and Facebook (code missing_required_field), and a live_comment, story_reply or story_mention trigger outside Instagram. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **409** | Active per-post automation already exists for this platformPostId. Does not apply to account-wide automations. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## deleteCommentAutomation

> void deleteCommentAutomation(automationId)

Delete automation

Permanently delete an automation and all its trigger logs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            apiInstance.deleteCommentAutomation(automationId);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#deleteCommentAutomation");
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
| **automationId** | **String**|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## deleteCommentAutomationWithHttpInfo

> ApiResponse<Void> deleteCommentAutomation deleteCommentAutomationWithHttpInfo(automationId)

Delete automation

Permanently delete an automation and all its trigger logs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.deleteCommentAutomationWithHttpInfo(automationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#deleteCommentAutomation");
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
| **automationId** | **String**|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getCommentAutomation

> GetCommentAutomation200Response getCommentAutomation(automationId)

Get automation details

Returns an automation with its configuration, stats, and recent trigger logs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            GetCommentAutomation200Response result = apiInstance.getCommentAutomation(automationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#getCommentAutomation");
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
| **automationId** | **String**|  | |

### Return type

[**GetCommentAutomation200Response**](GetCommentAutomation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation details with stats and recent trigger logs |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getCommentAutomationWithHttpInfo

> ApiResponse<GetCommentAutomation200Response> getCommentAutomation getCommentAutomationWithHttpInfo(automationId)

Get automation details

Returns an automation with its configuration, stats, and recent trigger logs.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            ApiResponse<GetCommentAutomation200Response> response = apiInstance.getCommentAutomationWithHttpInfo(automationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#getCommentAutomation");
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
| **automationId** | **String**|  | |

### Return type

ApiResponse<[**GetCommentAutomation200Response**](GetCommentAutomation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation details with stats and recent trigger logs |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## listCommentAutomationLogs

> ListCommentAutomationLogs200Response listCommentAutomationLogs(automationId, status, limit, skip)

List automation logs

Paginated list of every comment that triggered this automation, with send status and commenter info.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String status = "pending"; // String | Filter by result status
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListCommentAutomationLogs200Response result = apiInstance.listCommentAutomationLogs(automationId, status, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#listCommentAutomationLogs");
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
| **automationId** | **String**|  | |
| **status** | **String**| Filter by result status | [optional] [enum: pending, sent, failed, skipped, gated] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListCommentAutomationLogs200Response**](ListCommentAutomationLogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trigger logs with pagination |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## listCommentAutomationLogsWithHttpInfo

> ApiResponse<ListCommentAutomationLogs200Response> listCommentAutomationLogs listCommentAutomationLogsWithHttpInfo(automationId, status, limit, skip)

List automation logs

Paginated list of every comment that triggered this automation, with send status and commenter info.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String status = "pending"; // String | Filter by result status
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListCommentAutomationLogs200Response> response = apiInstance.listCommentAutomationLogsWithHttpInfo(automationId, status, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#listCommentAutomationLogs");
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
| **automationId** | **String**|  | |
| **status** | **String**| Filter by result status | [optional] [enum: pending, sent, failed, skipped, gated] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListCommentAutomationLogs200Response**](ListCommentAutomationLogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trigger logs with pagination |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## listCommentAutomations

> ListCommentAutomations200Response listCommentAutomations(profileId)

List comment-to-DM automations

List all comment-to-DM automations for a profile. Returns automations with their stats.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile. Omit to list across all profiles
        try {
            ListCommentAutomations200Response result = apiInstance.listCommentAutomations(profileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#listCommentAutomations");
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
| **profileId** | **String**| Filter by profile. Omit to list across all profiles | [optional] |

### Return type

[**ListCommentAutomations200Response**](ListCommentAutomations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automations list |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## listCommentAutomationsWithHttpInfo

> ApiResponse<ListCommentAutomations200Response> listCommentAutomations listCommentAutomationsWithHttpInfo(profileId)

List comment-to-DM automations

List all comment-to-DM automations for a profile. Returns automations with their stats.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile. Omit to list across all profiles
        try {
            ApiResponse<ListCommentAutomations200Response> response = apiInstance.listCommentAutomationsWithHttpInfo(profileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#listCommentAutomations");
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
| **profileId** | **String**| Filter by profile. Omit to list across all profiles | [optional] |

### Return type

ApiResponse<[**ListCommentAutomations200Response**](ListCommentAutomations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automations list |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## updateCommentAutomation

> UpdateCommentAutomation200Response updateCommentAutomation(automationId, updateCommentAutomationRequest)

Update automation settings

Update an automation&#39;s keywords, DM message, inline buttons, comment reply, post binding, or active status. Pass &#x60;buttons: []&#x60; to clear all buttons. When &#x60;buttons&#x60; is non-empty, &#x60;dmMessage&#x60; (the new one if you&#39;re changing it, otherwise the stored one) must be 640 characters or less. On a TikTok, Threads, LinkedIn or YouTube automation (public reply only) the DM fields are rejected with a 400 naming the field (&#x60;code&#x60; invalid_field_value, &#x60;param&#x60; the field), and &#x60;commentReply&#x60; cannot be cleared. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        UpdateCommentAutomationRequest updateCommentAutomationRequest = new UpdateCommentAutomationRequest(); // UpdateCommentAutomationRequest | 
        try {
            UpdateCommentAutomation200Response result = apiInstance.updateCommentAutomation(automationId, updateCommentAutomationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#updateCommentAutomation");
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
| **automationId** | **String**|  | |
| **updateCommentAutomationRequest** | [**UpdateCommentAutomationRequest**](UpdateCommentAutomationRequest.md)|  | [optional] |

### Return type

[**UpdateCommentAutomation200Response**](UpdateCommentAutomation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | An active automation already exists for the post this request re-binds to |  -  |

## updateCommentAutomationWithHttpInfo

> ApiResponse<UpdateCommentAutomation200Response> updateCommentAutomation updateCommentAutomationWithHttpInfo(automationId, updateCommentAutomationRequest)

Update automation settings

Update an automation&#39;s keywords, DM message, inline buttons, comment reply, post binding, or active status. Pass &#x60;buttons: []&#x60; to clear all buttons. When &#x60;buttons&#x60; is non-empty, &#x60;dmMessage&#x60; (the new one if you&#39;re changing it, otherwise the stored one) must be 640 characters or less. On a TikTok, Threads, LinkedIn or YouTube automation (public reply only) the DM fields are rejected with a 400 naming the field (&#x60;code&#x60; invalid_field_value, &#x60;param&#x60; the field), and &#x60;commentReply&#x60; cannot be cleared. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CommentAutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CommentAutomationsApi apiInstance = new CommentAutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        UpdateCommentAutomationRequest updateCommentAutomationRequest = new UpdateCommentAutomationRequest(); // UpdateCommentAutomationRequest | 
        try {
            ApiResponse<UpdateCommentAutomation200Response> response = apiInstance.updateCommentAutomationWithHttpInfo(automationId, updateCommentAutomationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CommentAutomationsApi#updateCommentAutomation");
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
| **automationId** | **String**|  | |
| **updateCommentAutomationRequest** | [**UpdateCommentAutomationRequest**](UpdateCommentAutomationRequest.md)|  | [optional] |

### Return type

ApiResponse<[**UpdateCommentAutomation200Response**](UpdateCommentAutomation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | An active automation already exists for the post this request re-binds to |  -  |

