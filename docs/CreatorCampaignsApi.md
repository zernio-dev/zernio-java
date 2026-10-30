# CreatorCampaignsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateCreatorCampaign**](CreatorCampaignsApi.md#activateCreatorCampaign) | **POST** /v1/creator-campaigns/{campaignId}/activate | Activate creator campaign |
| [**activateCreatorCampaignWithHttpInfo**](CreatorCampaignsApi.md#activateCreatorCampaignWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/activate | Activate creator campaign |
| [**approveCampaignSubmission**](CreatorCampaignsApi.md#approveCampaignSubmission) | **POST** /v1/creator-campaigns/{campaignId}/submissions/{submissionId}/approve | Approve campaign submission |
| [**approveCampaignSubmissionWithHttpInfo**](CreatorCampaignsApi.md#approveCampaignSubmissionWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/submissions/{submissionId}/approve | Approve campaign submission |
| [**closeCreatorCampaign**](CreatorCampaignsApi.md#closeCreatorCampaign) | **POST** /v1/creator-campaigns/{campaignId}/close | Close creator campaign |
| [**closeCreatorCampaignWithHttpInfo**](CreatorCampaignsApi.md#closeCreatorCampaignWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/close | Close creator campaign |
| [**createCampaignAdjustment**](CreatorCampaignsApi.md#createCampaignAdjustment) | **POST** /v1/creator-campaigns/{campaignId}/adjustments | Create campaign adjustment |
| [**createCampaignAdjustmentWithHttpInfo**](CreatorCampaignsApi.md#createCampaignAdjustmentWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/adjustments | Create campaign adjustment |
| [**createCampaignInviteLink**](CreatorCampaignsApi.md#createCampaignInviteLink) | **POST** /v1/creator-campaigns/{campaignId}/invite-link | Create campaign invite link |
| [**createCampaignInviteLinkWithHttpInfo**](CreatorCampaignsApi.md#createCampaignInviteLinkWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/invite-link | Create campaign invite link |
| [**createCampaignParticipant**](CreatorCampaignsApi.md#createCampaignParticipant) | **POST** /v1/creator-campaigns/{campaignId}/participants | Invite campaign participant |
| [**createCampaignParticipantWithHttpInfo**](CreatorCampaignsApi.md#createCampaignParticipantWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/participants | Invite campaign participant |
| [**createCampaignPayoutBatch**](CreatorCampaignsApi.md#createCampaignPayoutBatch) | **POST** /v1/creator-campaigns/{campaignId}/payout-batches | Pay creators with one card payment |
| [**createCampaignPayoutBatchWithHttpInfo**](CreatorCampaignsApi.md#createCampaignPayoutBatchWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/payout-batches | Pay creators with one card payment |
| [**createCreatorCampaign**](CreatorCampaignsApi.md#createCreatorCampaign) | **POST** /v1/creator-campaigns | Create creator campaign |
| [**createCreatorCampaignWithHttpInfo**](CreatorCampaignsApi.md#createCreatorCampaignWithHttpInfo) | **POST** /v1/creator-campaigns | Create creator campaign |
| [**getCampaignParticipant**](CreatorCampaignsApi.md#getCampaignParticipant) | **GET** /v1/creator-campaigns/{campaignId}/participants/{participantId} | Get campaign participant |
| [**getCampaignParticipantWithHttpInfo**](CreatorCampaignsApi.md#getCampaignParticipantWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/participants/{participantId} | Get campaign participant |
| [**getCampaignReport**](CreatorCampaignsApi.md#getCampaignReport) | **GET** /v1/creator-campaigns/{campaignId}/report | Get campaign report |
| [**getCampaignReportWithHttpInfo**](CreatorCampaignsApi.md#getCampaignReportWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/report | Get campaign report |
| [**getCampaignSubmission**](CreatorCampaignsApi.md#getCampaignSubmission) | **GET** /v1/creator-campaigns/{campaignId}/submissions/{submissionId} | Get campaign submission |
| [**getCampaignSubmissionWithHttpInfo**](CreatorCampaignsApi.md#getCampaignSubmissionWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/submissions/{submissionId} | Get campaign submission |
| [**getCreatorCampaign**](CreatorCampaignsApi.md#getCreatorCampaign) | **GET** /v1/creator-campaigns/{campaignId} | Get creator campaign |
| [**getCreatorCampaignWithHttpInfo**](CreatorCampaignsApi.md#getCreatorCampaignWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId} | Get creator campaign |
| [**listCampaignLedger**](CreatorCampaignsApi.md#listCampaignLedger) | **GET** /v1/creator-campaigns/{campaignId}/ledger | List campaign ledger |
| [**listCampaignLedgerWithHttpInfo**](CreatorCampaignsApi.md#listCampaignLedgerWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/ledger | List campaign ledger |
| [**listCampaignParticipants**](CreatorCampaignsApi.md#listCampaignParticipants) | **GET** /v1/creator-campaigns/{campaignId}/participants | List campaign participants |
| [**listCampaignParticipantsWithHttpInfo**](CreatorCampaignsApi.md#listCampaignParticipantsWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/participants | List campaign participants |
| [**listCampaignPayables**](CreatorCampaignsApi.md#listCampaignPayables) | **GET** /v1/creator-campaigns/{campaignId}/payables | List campaign payables |
| [**listCampaignPayablesWithHttpInfo**](CreatorCampaignsApi.md#listCampaignPayablesWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/payables | List campaign payables |
| [**listCampaignPayoutBatches**](CreatorCampaignsApi.md#listCampaignPayoutBatches) | **GET** /v1/creator-campaigns/{campaignId}/payout-batches | List payout batches |
| [**listCampaignPayoutBatchesWithHttpInfo**](CreatorCampaignsApi.md#listCampaignPayoutBatchesWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/payout-batches | List payout batches |
| [**listCampaignSubmissions**](CreatorCampaignsApi.md#listCampaignSubmissions) | **GET** /v1/creator-campaigns/{campaignId}/submissions | List campaign submissions |
| [**listCampaignSubmissionsWithHttpInfo**](CreatorCampaignsApi.md#listCampaignSubmissionsWithHttpInfo) | **GET** /v1/creator-campaigns/{campaignId}/submissions | List campaign submissions |
| [**listCreatorCampaigns**](CreatorCampaignsApi.md#listCreatorCampaigns) | **GET** /v1/creator-campaigns | List creator campaigns |
| [**listCreatorCampaignsWithHttpInfo**](CreatorCampaignsApi.md#listCreatorCampaignsWithHttpInfo) | **GET** /v1/creator-campaigns | List creator campaigns |
| [**pauseCreatorCampaign**](CreatorCampaignsApi.md#pauseCreatorCampaign) | **POST** /v1/creator-campaigns/{campaignId}/pause | Pause creator campaign |
| [**pauseCreatorCampaignWithHttpInfo**](CreatorCampaignsApi.md#pauseCreatorCampaignWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/pause | Pause creator campaign |
| [**raiseCreatorCampaignBudget**](CreatorCampaignsApi.md#raiseCreatorCampaignBudget) | **POST** /v1/creator-campaigns/{campaignId}/budget | Raise creator campaign budget |
| [**raiseCreatorCampaignBudgetWithHttpInfo**](CreatorCampaignsApi.md#raiseCreatorCampaignBudgetWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/budget | Raise creator campaign budget |
| [**reinstateCampaignParticipant**](CreatorCampaignsApi.md#reinstateCampaignParticipant) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/reinstate | Reinstate campaign participant |
| [**reinstateCampaignParticipantWithHttpInfo**](CreatorCampaignsApi.md#reinstateCampaignParticipantWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/reinstate | Reinstate campaign participant |
| [**rejectCampaignSubmission**](CreatorCampaignsApi.md#rejectCampaignSubmission) | **POST** /v1/creator-campaigns/{campaignId}/submissions/{submissionId}/reject | Reject campaign submission |
| [**rejectCampaignSubmissionWithHttpInfo**](CreatorCampaignsApi.md#rejectCampaignSubmissionWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/submissions/{submissionId}/reject | Reject campaign submission |
| [**removeCampaignParticipant**](CreatorCampaignsApi.md#removeCampaignParticipant) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/remove | Remove campaign participant |
| [**removeCampaignParticipantWithHttpInfo**](CreatorCampaignsApi.md#removeCampaignParticipantWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/remove | Remove campaign participant |
| [**reopenCampaignSubmission**](CreatorCampaignsApi.md#reopenCampaignSubmission) | **POST** /v1/creator-campaigns/{campaignId}/submissions/{submissionId}/reopen | Reopen campaign submission |
| [**reopenCampaignSubmissionWithHttpInfo**](CreatorCampaignsApi.md#reopenCampaignSubmissionWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/submissions/{submissionId}/reopen | Reopen campaign submission |
| [**resendCampaignParticipantInvite**](CreatorCampaignsApi.md#resendCampaignParticipantInvite) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/resend-invite | Resend campaign participant invite |
| [**resendCampaignParticipantInviteWithHttpInfo**](CreatorCampaignsApi.md#resendCampaignParticipantInviteWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/resend-invite | Resend campaign participant invite |
| [**settleCampaignParticipant**](CreatorCampaignsApi.md#settleCampaignParticipant) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/settle | Settle campaign participant |
| [**settleCampaignParticipantWithHttpInfo**](CreatorCampaignsApi.md#settleCampaignParticipantWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/settle | Settle campaign participant |
| [**suspendCampaignParticipant**](CreatorCampaignsApi.md#suspendCampaignParticipant) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/suspend | Suspend campaign participant |
| [**suspendCampaignParticipantWithHttpInfo**](CreatorCampaignsApi.md#suspendCampaignParticipantWithHttpInfo) | **POST** /v1/creator-campaigns/{campaignId}/participants/{participantId}/suspend | Suspend campaign participant |
| [**updateCreatorCampaign**](CreatorCampaignsApi.md#updateCreatorCampaign) | **PATCH** /v1/creator-campaigns/{campaignId} | Update creator campaign |
| [**updateCreatorCampaignWithHttpInfo**](CreatorCampaignsApi.md#updateCreatorCampaignWithHttpInfo) | **PATCH** /v1/creator-campaigns/{campaignId} | Update creator campaign |



## activateCreatorCampaign

> CreateCreatorCampaign201Response activateCreatorCampaign(campaignId)

Activate creator campaign

Moves a &#x60;draft&#x60; or &#x60;paused&#x60; campaign to &#x60;active&#x60;, where creators can join and submit posts and tracked views accrue earnings. Needs at least one platform and a budget above zero; any other starting state answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            CreateCreatorCampaign201Response result = apiInstance.activateCreatorCampaign(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#activateCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## activateCreatorCampaignWithHttpInfo

> ApiResponse<CreateCreatorCampaign201Response> activateCreatorCampaign activateCreatorCampaignWithHttpInfo(campaignId)

Activate creator campaign

Moves a &#x60;draft&#x60; or &#x60;paused&#x60; campaign to &#x60;active&#x60;, where creators can join and submit posts and tracked views accrue earnings. Needs at least one platform and a budget above zero; any other starting state answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ApiResponse<CreateCreatorCampaign201Response> response = apiInstance.activateCreatorCampaignWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#activateCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

ApiResponse<[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## approveCampaignSubmission

> ApproveCampaignSubmission200Response approveCampaignSubmission(campaignId, submissionId, idempotencyKey)

Approve campaign submission

Approves a &#x60;tracking&#x60; or &#x60;pending_review&#x60; submission of an active campaign and fires &#x60;campaign_submission.approved&#x60;.  The Zernio dashboard offers Approve only on &#x60;pending_review&#x60; (a post that needs a decision) and waits for &#x60;tracking&#x60; posts to get there. The API accepts &#x60;tracking&#x60; so an integration can approve early.  ### Earnings  - What the post earned so far moves to owed and is held for the campaign&#39;s &#x60;holdDays&#x60;. - Later earnings post straight to owed. - A per-post campaign pays &#x60;perApprovedPostCents&#x60; here.  ### Errors  - 409: the submission is in any other state. - 409 (&#x60;invalid_resource_state&#x60;, \&quot;This post is already approved in another campaign of yours.\&quot;): the same post was approved in another of your campaigns, so one post never earns twice. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApproveCampaignSubmission200Response result = apiInstance.approveCampaignSubmission(campaignId, submissionId, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#approveCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**ApproveCampaignSubmission200Response**](ApproveCampaignSubmission200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission approved |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign or submission is not in a state that allows approval, or the same post is already approved in another of your campaigns (&#x60;invalid_resource_state&#x60;, \&quot;This post is already approved in another campaign of yours.\&quot;). Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## approveCampaignSubmissionWithHttpInfo

> ApiResponse<ApproveCampaignSubmission200Response> approveCampaignSubmission approveCampaignSubmissionWithHttpInfo(campaignId, submissionId, idempotencyKey)

Approve campaign submission

Approves a &#x60;tracking&#x60; or &#x60;pending_review&#x60; submission of an active campaign and fires &#x60;campaign_submission.approved&#x60;.  The Zernio dashboard offers Approve only on &#x60;pending_review&#x60; (a post that needs a decision) and waits for &#x60;tracking&#x60; posts to get there. The API accepts &#x60;tracking&#x60; so an integration can approve early.  ### Earnings  - What the post earned so far moves to owed and is held for the campaign&#39;s &#x60;holdDays&#x60;. - Later earnings post straight to owed. - A per-post campaign pays &#x60;perApprovedPostCents&#x60; here.  ### Errors  - 409: the submission is in any other state. - 409 (&#x60;invalid_resource_state&#x60;, \&quot;This post is already approved in another campaign of yours.\&quot;): the same post was approved in another of your campaigns, so one post never earns twice. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<ApproveCampaignSubmission200Response> response = apiInstance.approveCampaignSubmissionWithHttpInfo(campaignId, submissionId, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#approveCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**ApproveCampaignSubmission200Response**](ApproveCampaignSubmission200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission approved |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign or submission is not in a state that allows approval, or the same post is already approved in another of your campaigns (&#x60;invalid_resource_state&#x60;, \&quot;This post is already approved in another campaign of yours.\&quot;). Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## closeCreatorCampaign

> CreateCreatorCampaign201Response closeCreatorCampaign(campaignId)

Close creator campaign

Closes an &#x60;active&#x60; or &#x60;paused&#x60; campaign for good and fires &#x60;creator_campaign.closed&#x60;. Open tracking windows are cancelled.  A pool campaign is split among participants at this moment by their approved eligible views. Closing a pool campaign therefore answers 409 while any post still awaits review.  A campaign also closes by itself once &#x60;endsAt&#x60; passed and every tracking window had its final read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            CreateCreatorCampaign201Response result = apiInstance.closeCreatorCampaign(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#closeCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## closeCreatorCampaignWithHttpInfo

> ApiResponse<CreateCreatorCampaign201Response> closeCreatorCampaign closeCreatorCampaignWithHttpInfo(campaignId)

Close creator campaign

Closes an &#x60;active&#x60; or &#x60;paused&#x60; campaign for good and fires &#x60;creator_campaign.closed&#x60;. Open tracking windows are cancelled.  A pool campaign is split among participants at this moment by their approved eligible views. Closing a pool campaign therefore answers 409 while any post still awaits review.  A campaign also closes by itself once &#x60;endsAt&#x60; passed and every tracking window had its final read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ApiResponse<CreateCreatorCampaign201Response> response = apiInstance.closeCreatorCampaignWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#closeCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

ApiResponse<[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## createCampaignAdjustment

> CreateCampaignAdjustment201Response createCampaignAdjustment(campaignId, createCampaignAdjustmentRequest, idempotencyKey)

Create campaign adjustment

Posts a manual adjustment to a participant&#39;s payable balance against the campaign budget: a positive amount credits the participant (a bonus), a negative one claws back. &#x60;cause&#x60; is kept on the ledger entry. A claw-back larger than the payable balance answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        CreateCampaignAdjustmentRequest createCampaignAdjustmentRequest = new CreateCampaignAdjustmentRequest(); // CreateCampaignAdjustmentRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            CreateCampaignAdjustment201Response result = apiInstance.createCampaignAdjustment(campaignId, createCampaignAdjustmentRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignAdjustment");
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
| **campaignId** | **String**| Campaign ID. | |
| **createCampaignAdjustmentRequest** | [**CreateCampaignAdjustmentRequest**](CreateCampaignAdjustmentRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**CreateCampaignAdjustment201Response**](CreateCampaignAdjustment201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Adjustment posted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createCampaignAdjustmentWithHttpInfo

> ApiResponse<CreateCampaignAdjustment201Response> createCampaignAdjustment createCampaignAdjustmentWithHttpInfo(campaignId, createCampaignAdjustmentRequest, idempotencyKey)

Create campaign adjustment

Posts a manual adjustment to a participant&#39;s payable balance against the campaign budget: a positive amount credits the participant (a bonus), a negative one claws back. &#x60;cause&#x60; is kept on the ledger entry. A claw-back larger than the payable balance answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        CreateCampaignAdjustmentRequest createCampaignAdjustmentRequest = new CreateCampaignAdjustmentRequest(); // CreateCampaignAdjustmentRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<CreateCampaignAdjustment201Response> response = apiInstance.createCampaignAdjustmentWithHttpInfo(campaignId, createCampaignAdjustmentRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignAdjustment");
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
| **campaignId** | **String**| Campaign ID. | |
| **createCampaignAdjustmentRequest** | [**CreateCampaignAdjustmentRequest**](CreateCampaignAdjustmentRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**CreateCampaignAdjustment201Response**](CreateCampaignAdjustment201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Adjustment posted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## createCampaignInviteLink

> CreateCampaignInviteLink201Response createCampaignInviteLink(campaignId)

Create campaign invite link

Creates the campaign&#39;s open invite link: anyone with it can join as a participant (up to &#x60;caps.maxParticipants&#x60;). Creating a new link revokes the previous one. The URL is returned only here. Answers 409 on a closed campaign. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            CreateCampaignInviteLink201Response result = apiInstance.createCampaignInviteLink(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignInviteLink");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

[**CreateCampaignInviteLink201Response**](CreateCampaignInviteLink201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invite link created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## createCampaignInviteLinkWithHttpInfo

> ApiResponse<CreateCampaignInviteLink201Response> createCampaignInviteLink createCampaignInviteLinkWithHttpInfo(campaignId)

Create campaign invite link

Creates the campaign&#39;s open invite link: anyone with it can join as a participant (up to &#x60;caps.maxParticipants&#x60;). Creating a new link revokes the previous one. The URL is returned only here. Answers 409 on a closed campaign. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ApiResponse<CreateCampaignInviteLink201Response> response = apiInstance.createCampaignInviteLinkWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignInviteLink");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

ApiResponse<[**CreateCampaignInviteLink201Response**](CreateCampaignInviteLink201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invite link created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## createCampaignParticipant

> CreateCampaignParticipant201Response createCampaignParticipant(campaignId, createCampaignParticipantRequest, idempotencyKey)

Invite campaign participant

Invites one creator and returns their personal invite URL.  Send the URL to the creator. On that page they connect their accounts (read-only), submit posts and see their earnings.  ### Invite rules  - The URL is returned only here; inviting again creates no second link. - A creator is matched by email within your workspace, so the same person keeps one identity across your campaigns.  ### Errors  - 409: the creator is already in the campaign, or the campaign is closed. - 403 &#x60;feature_not_available&#x60;: &#x60;caps.maxParticipants&#x60; is reached. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        CreateCampaignParticipantRequest createCampaignParticipantRequest = new CreateCampaignParticipantRequest(); // CreateCampaignParticipantRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            CreateCampaignParticipant201Response result = apiInstance.createCampaignParticipant(campaignId, createCampaignParticipantRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **createCampaignParticipantRequest** | [**CreateCampaignParticipantRequest**](CreateCampaignParticipantRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**CreateCampaignParticipant201Response**](CreateCampaignParticipant201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Participant invited |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createCampaignParticipantWithHttpInfo

> ApiResponse<CreateCampaignParticipant201Response> createCampaignParticipant createCampaignParticipantWithHttpInfo(campaignId, createCampaignParticipantRequest, idempotencyKey)

Invite campaign participant

Invites one creator and returns their personal invite URL.  Send the URL to the creator. On that page they connect their accounts (read-only), submit posts and see their earnings.  ### Invite rules  - The URL is returned only here; inviting again creates no second link. - A creator is matched by email within your workspace, so the same person keeps one identity across your campaigns.  ### Errors  - 409: the creator is already in the campaign, or the campaign is closed. - 403 &#x60;feature_not_available&#x60;: &#x60;caps.maxParticipants&#x60; is reached. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        CreateCampaignParticipantRequest createCampaignParticipantRequest = new CreateCampaignParticipantRequest(); // CreateCampaignParticipantRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<CreateCampaignParticipant201Response> response = apiInstance.createCampaignParticipantWithHttpInfo(campaignId, createCampaignParticipantRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **createCampaignParticipantRequest** | [**CreateCampaignParticipantRequest**](CreateCampaignParticipantRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**CreateCampaignParticipant201Response**](CreateCampaignParticipant201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Participant invited |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## createCampaignPayoutBatch

> CreateCampaignPayoutBatch201Response createCampaignPayoutBatch(campaignId, idempotencyKey, createCampaignPayoutBatchRequest)

Pay creators with one card payment

Pays exactly what is owed to the creators of a &#x60;treasury&#x60; campaign by charging the billing owner&#39;s saved card, with no redirect.  ### How it works  1. Every payable creator who finished payout setup (or only &#x60;participantIds&#x60;, minus &#x60;excludeParticipantIds&#x60;) is held in &#x60;settling&#x60;. 2. The saved card (the default one, or &#x60;paymentMethodId&#x60;) is charged the total plus the fee (4% per creator, 50 cent minimum) while the payer is present. 3. Once the charge succeeds, each creator gets a transfer funded by it, and the batch ends &#x60;paid&#x60; or &#x60;partially_failed&#x60;.  A creator whose payouts were disabled before the payment landed is skipped and stays payable.  ### 3D Secure  &#x60;payment.status: requires_action&#x60; means the bank asked the payer to confirm. Complete it with Stripe.js &#x60;handleNextAction({ clientSecret })&#x60;, then call &#x60;POST /v1/payout-batches/{batchId}/confirm&#x60;.  One left unfinished is cancelled after 30 minutes and every amount is payable again. Cancel it sooner with &#x60;POST /v1/payout-batches/{batchId}/cancel&#x60;.  ### Limits and errors  - 402 &#x60;payment_required&#x60;: no saved card. Nothing is held. - 402 &#x60;card_declined&#x60;: the bank&#39;s reason; every amount is payable again. - 402: card payouts are limited to $10,000.00 gross per rolling 30 days by default. Over it the call answers \&quot;Over your instant payout limit. Top up your balance to pay more this month, or contact support to raise the limit.\&quot; - 400: nothing payable (\&quot;Nothing is payable.\&quot;).  ### Access and retries  Needs an owner, admin or billing admin, signed in or through a full-access key they created.  Send an &#x60;Idempotency-Key&#x60; so a retry never opens a second batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        CreateCampaignPayoutBatchRequest createCampaignPayoutBatchRequest = new CreateCampaignPayoutBatchRequest(); // CreateCampaignPayoutBatchRequest | 
        try {
            CreateCampaignPayoutBatch201Response result = apiInstance.createCampaignPayoutBatch(campaignId, idempotencyKey, createCampaignPayoutBatchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignPayoutBatch");
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
| **campaignId** | **String**| Campaign ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |
| **createCampaignPayoutBatchRequest** | [**CreateCampaignPayoutBatchRequest**](CreateCampaignPayoutBatchRequest.md)|  | [optional] |

### Return type

[**CreateCampaignPayoutBatch201Response**](CreateCampaignPayoutBatch201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Batch created and the card charged, or the bank asked for 3D Secure. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Over the instant payout limit or no saved card (code &#x60;payment_required&#x60;), or the bank declined the charge (code &#x60;card_declined&#x60;). |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## createCampaignPayoutBatchWithHttpInfo

> ApiResponse<CreateCampaignPayoutBatch201Response> createCampaignPayoutBatch createCampaignPayoutBatchWithHttpInfo(campaignId, idempotencyKey, createCampaignPayoutBatchRequest)

Pay creators with one card payment

Pays exactly what is owed to the creators of a &#x60;treasury&#x60; campaign by charging the billing owner&#39;s saved card, with no redirect.  ### How it works  1. Every payable creator who finished payout setup (or only &#x60;participantIds&#x60;, minus &#x60;excludeParticipantIds&#x60;) is held in &#x60;settling&#x60;. 2. The saved card (the default one, or &#x60;paymentMethodId&#x60;) is charged the total plus the fee (4% per creator, 50 cent minimum) while the payer is present. 3. Once the charge succeeds, each creator gets a transfer funded by it, and the batch ends &#x60;paid&#x60; or &#x60;partially_failed&#x60;.  A creator whose payouts were disabled before the payment landed is skipped and stays payable.  ### 3D Secure  &#x60;payment.status: requires_action&#x60; means the bank asked the payer to confirm. Complete it with Stripe.js &#x60;handleNextAction({ clientSecret })&#x60;, then call &#x60;POST /v1/payout-batches/{batchId}/confirm&#x60;.  One left unfinished is cancelled after 30 minutes and every amount is payable again. Cancel it sooner with &#x60;POST /v1/payout-batches/{batchId}/cancel&#x60;.  ### Limits and errors  - 402 &#x60;payment_required&#x60;: no saved card. Nothing is held. - 402 &#x60;card_declined&#x60;: the bank&#39;s reason; every amount is payable again. - 402: card payouts are limited to $10,000.00 gross per rolling 30 days by default. Over it the call answers \&quot;Over your instant payout limit. Top up your balance to pay more this month, or contact support to raise the limit.\&quot; - 400: nothing payable (\&quot;Nothing is payable.\&quot;).  ### Access and retries  Needs an owner, admin or billing admin, signed in or through a full-access key they created.  Send an &#x60;Idempotency-Key&#x60; so a retry never opens a second batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        CreateCampaignPayoutBatchRequest createCampaignPayoutBatchRequest = new CreateCampaignPayoutBatchRequest(); // CreateCampaignPayoutBatchRequest | 
        try {
            ApiResponse<CreateCampaignPayoutBatch201Response> response = apiInstance.createCampaignPayoutBatchWithHttpInfo(campaignId, idempotencyKey, createCampaignPayoutBatchRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCampaignPayoutBatch");
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
| **campaignId** | **String**| Campaign ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |
| **createCampaignPayoutBatchRequest** | [**CreateCampaignPayoutBatchRequest**](CreateCampaignPayoutBatchRequest.md)|  | [optional] |

### Return type

ApiResponse<[**CreateCampaignPayoutBatch201Response**](CreateCampaignPayoutBatch201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Batch created and the card charged, or the bank asked for 3D Secure. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **402** | Over the instant payout limit or no saved card (code &#x60;payment_required&#x60;), or the bank declined the charge (code &#x60;card_declined&#x60;). |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## createCreatorCampaign

> CreateCreatorCampaign201Response createCreatorCampaign(createCreatorCampaignRequest, idempotencyKey)

Create creator campaign

Creates a campaign in &#x60;draft&#x60;. Creators are paid for verified performance of the posts they submit: Zernio tracks each post through a tracking window, scores its authenticity and records every earning in a ledger. Activate the campaign to start accepting submissions.  Creator campaigns run on usage-based billing; a workspace not on it gets 403 &#x60;feature_not_available&#x60;. &#x60;profileId&#x60; must be a profile this key can reach, otherwise 404. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        CreateCreatorCampaignRequest createCreatorCampaignRequest = new CreateCreatorCampaignRequest(); // CreateCreatorCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            CreateCreatorCampaign201Response result = apiInstance.createCreatorCampaign(createCreatorCampaignRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCreatorCampaign");
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
| **createCreatorCampaignRequest** | [**CreateCreatorCampaignRequest**](CreateCreatorCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Campaign created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createCreatorCampaignWithHttpInfo

> ApiResponse<CreateCreatorCampaign201Response> createCreatorCampaign createCreatorCampaignWithHttpInfo(createCreatorCampaignRequest, idempotencyKey)

Create creator campaign

Creates a campaign in &#x60;draft&#x60;. Creators are paid for verified performance of the posts they submit: Zernio tracks each post through a tracking window, scores its authenticity and records every earning in a ledger. Activate the campaign to start accepting submissions.  Creator campaigns run on usage-based billing; a workspace not on it gets 403 &#x60;feature_not_available&#x60;. &#x60;profileId&#x60; must be a profile this key can reach, otherwise 404. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        CreateCreatorCampaignRequest createCreatorCampaignRequest = new CreateCreatorCampaignRequest(); // CreateCreatorCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<CreateCreatorCampaign201Response> response = apiInstance.createCreatorCampaignWithHttpInfo(createCreatorCampaignRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#createCreatorCampaign");
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
| **createCreatorCampaignRequest** | [**CreateCreatorCampaignRequest**](CreateCreatorCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Campaign created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## getCampaignParticipant

> GetCampaignParticipant200Response getCampaignParticipant(campaignId, participantId)

Get campaign participant

Returns one participant with connected accounts, balances by state, flags and submission counts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            GetCampaignParticipant200Response result = apiInstance.getCampaignParticipant(campaignId, participantId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## getCampaignParticipantWithHttpInfo

> ApiResponse<GetCampaignParticipant200Response> getCampaignParticipant getCampaignParticipantWithHttpInfo(campaignId, participantId)

Get campaign participant

Returns one participant with connected accounts, balances by state, flags and submission counts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            ApiResponse<GetCampaignParticipant200Response> response = apiInstance.getCampaignParticipantWithHttpInfo(campaignId, participantId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

ApiResponse<[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## getCampaignReport

> GetCampaignReport200Response getCampaignReport(campaignId)

Get campaign report

Returns spend against budget, views, submission counts, the top ten participants by earnings and the authenticity score distribution. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            GetCampaignReport200Response result = apiInstance.getCampaignReport(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCampaignReport");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

[**GetCampaignReport200Response**](GetCampaignReport200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign report |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## getCampaignReportWithHttpInfo

> ApiResponse<GetCampaignReport200Response> getCampaignReport getCampaignReportWithHttpInfo(campaignId)

Get campaign report

Returns spend against budget, views, submission counts, the top ten participants by earnings and the authenticity score distribution. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ApiResponse<GetCampaignReport200Response> response = apiInstance.getCampaignReportWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCampaignReport");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

ApiResponse<[**GetCampaignReport200Response**](GetCampaignReport200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign report |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## getCampaignSubmission

> GetCampaignSubmission200Response getCampaignSubmission(campaignId, submissionId)

Get campaign submission

Returns one submission with its per-sync samples (views, likes, comments, shares, saves). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        try {
            GetCampaignSubmission200Response result = apiInstance.getCampaignSubmission(campaignId, submissionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |

### Return type

[**GetCampaignSubmission200Response**](GetCampaignSubmission200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## getCampaignSubmissionWithHttpInfo

> ApiResponse<GetCampaignSubmission200Response> getCampaignSubmission getCampaignSubmissionWithHttpInfo(campaignId, submissionId)

Get campaign submission

Returns one submission with its per-sync samples (views, likes, comments, shares, saves). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        try {
            ApiResponse<GetCampaignSubmission200Response> response = apiInstance.getCampaignSubmissionWithHttpInfo(campaignId, submissionId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |

### Return type

ApiResponse<[**GetCampaignSubmission200Response**](GetCampaignSubmission200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## getCreatorCampaign

> CreateCreatorCampaign201Response getCreatorCampaign(campaignId)

Get creator campaign

Returns the campaign with its budget consumption, participant count and submission counts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            CreateCreatorCampaign201Response result = apiInstance.getCreatorCampaign(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## getCreatorCampaignWithHttpInfo

> ApiResponse<CreateCreatorCampaign201Response> getCreatorCampaign getCreatorCampaignWithHttpInfo(campaignId)

Get creator campaign

Returns the campaign with its budget consumption, participant count and submission counts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ApiResponse<CreateCreatorCampaign201Response> response = apiInstance.getCreatorCampaignWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#getCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

ApiResponse<[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## listCampaignLedger

> ListCampaignLedger200Response listCampaignLedger(campaignId, participantId, kind, limit, skip)

List campaign ledger

Lists ledger entries, newest first.  Without &#x60;participantId&#x60; it lists every entry of the campaign:  - earnings drawn from the budget (accruals, per-post payments, pool shares, adjustments) - the approvals, hold releases and settlements that move money between its participants&#39; buckets - their reversals  Pass &#x60;participantId&#x60; to narrow the list to one participant&#39;s entries. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | List only this participant's entries.
        String kind = "accrual"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListCampaignLedger200Response result = apiInstance.listCampaignLedger(campaignId, participantId, kind, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignLedger");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| List only this participant&#39;s entries. | [optional] |
| **kind** | **String**|  | [optional] [enum: accrual, approval, hold_release, adjustment, settling, settlement, reversal, topup, transfer, fee] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListCampaignLedger200Response**](ListCampaignLedger200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ledger entries |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## listCampaignLedgerWithHttpInfo

> ApiResponse<ListCampaignLedger200Response> listCampaignLedger listCampaignLedgerWithHttpInfo(campaignId, participantId, kind, limit, skip)

List campaign ledger

Lists ledger entries, newest first.  Without &#x60;participantId&#x60; it lists every entry of the campaign:  - earnings drawn from the budget (accruals, per-post payments, pool shares, adjustments) - the approvals, hold releases and settlements that move money between its participants&#39; buckets - their reversals  Pass &#x60;participantId&#x60; to narrow the list to one participant&#39;s entries. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | List only this participant's entries.
        String kind = "accrual"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListCampaignLedger200Response> response = apiInstance.listCampaignLedgerWithHttpInfo(campaignId, participantId, kind, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignLedger");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| List only this participant&#39;s entries. | [optional] |
| **kind** | **String**|  | [optional] [enum: accrual, approval, hold_release, adjustment, settling, settlement, reversal, topup, transfer, fee] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListCampaignLedger200Response**](ListCampaignLedger200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ledger entries |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## listCampaignParticipants

> ListCampaignParticipants200Response listCampaignParticipants(campaignId, status, limit, skip)

List campaign participants

Lists the campaign&#39;s participants with their balances, flags and submission counts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String status = "invited"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListCampaignParticipants200Response result = apiInstance.listCampaignParticipants(campaignId, status, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignParticipants");
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
| **campaignId** | **String**| Campaign ID. | |
| **status** | **String**|  | [optional] [enum: invited, active, suspended, removed] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListCampaignParticipants200Response**](ListCampaignParticipants200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## listCampaignParticipantsWithHttpInfo

> ApiResponse<ListCampaignParticipants200Response> listCampaignParticipants listCampaignParticipantsWithHttpInfo(campaignId, status, limit, skip)

List campaign participants

Lists the campaign&#39;s participants with their balances, flags and submission counts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String status = "invited"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListCampaignParticipants200Response> response = apiInstance.listCampaignParticipantsWithHttpInfo(campaignId, status, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignParticipants");
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
| **campaignId** | **String**| Campaign ID. | |
| **status** | **String**|  | [optional] [enum: invited, active, suspended, removed] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListCampaignParticipants200Response**](ListCampaignParticipants200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## listCampaignPayables

> ListCampaignPayables200Response listCampaignPayables(campaignId)

List campaign payables

Lists every participant with a payable balance (earnings past their hold), with the ledger entries behind it. Pay these, then record each payout with the settle endpoint. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ListCampaignPayables200Response result = apiInstance.listCampaignPayables(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignPayables");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

[**ListCampaignPayables200Response**](ListCampaignPayables200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payables |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## listCampaignPayablesWithHttpInfo

> ApiResponse<ListCampaignPayables200Response> listCampaignPayables listCampaignPayablesWithHttpInfo(campaignId)

List campaign payables

Lists every participant with a payable balance (earnings past their hold), with the ledger entries behind it. Pay these, then record each payout with the settle endpoint. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ApiResponse<ListCampaignPayables200Response> response = apiInstance.listCampaignPayablesWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignPayables");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

ApiResponse<[**ListCampaignPayables200Response**](ListCampaignPayables200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payables |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## listCampaignPayoutBatches

> ListCampaignPayoutBatches200Response listCampaignPayoutBatches(campaignId, limit, skip)

List payout batches

The campaign&#39;s payout batches, newest first, with each creator&#39;s item.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        Integer limit = 20; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListCampaignPayoutBatches200Response result = apiInstance.listCampaignPayoutBatches(campaignId, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignPayoutBatches");
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
| **campaignId** | **String**| Campaign ID. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListCampaignPayoutBatches200Response**](ListCampaignPayoutBatches200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payout batches. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## listCampaignPayoutBatchesWithHttpInfo

> ApiResponse<ListCampaignPayoutBatches200Response> listCampaignPayoutBatches listCampaignPayoutBatchesWithHttpInfo(campaignId, limit, skip)

List payout batches

The campaign&#39;s payout batches, newest first, with each creator&#39;s item.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        Integer limit = 20; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListCampaignPayoutBatches200Response> response = apiInstance.listCampaignPayoutBatchesWithHttpInfo(campaignId, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignPayoutBatches");
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
| **campaignId** | **String**| Campaign ID. | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListCampaignPayoutBatches200Response**](ListCampaignPayoutBatches200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payout batches. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## listCampaignSubmissions

> ListCampaignSubmissions200Response listCampaignSubmissions(campaignId, status, participantId, flag, platform, minScore, maxScore, q, sort, order, limit, skip)

List campaign submissions

Lists submitted posts with views, earnings, authenticity score and flags. Filter by status, participant, flag, platform or score range to build a review queue, for example &#x60;status&#x3D;pending_review&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String status = "received"; // String | 
        String participantId = "participantId_example"; // String | 
        String flag = "duplicate_media"; // String | 
        String platform = "tiktok"; // String | 
        Integer minScore = 56; // Integer | 
        Integer maxScore = 56; // Integer | 
        String q = "q_example"; // String | Only submissions whose creator name or post link contains this text, ignoring case.
        String sort = "submittedAt"; // String | What to sort by. Posts with no value to sort by (not read yet, not scored) come last in either direction.
        String order = "asc"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListCampaignSubmissions200Response result = apiInstance.listCampaignSubmissions(campaignId, status, participantId, flag, platform, minScore, maxScore, q, sort, order, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignSubmissions");
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
| **campaignId** | **String**| Campaign ID. | |
| **status** | **String**|  | [optional] [enum: received, tracking, pending_review, approved, rejected, expired, withdrawn] |
| **participantId** | **String**|  | [optional] |
| **flag** | **String**|  | [optional] [enum: duplicate_media, duplicate_post, view_spike, linked_accounts, cross_operator, unreachable, post_deleted, account_restricted, low_authenticity, x_read_cap] |
| **platform** | **String**|  | [optional] [enum: tiktok, instagram, youtube, threads, pinterest, facebook, twitter] |
| **minScore** | **Integer**|  | [optional] |
| **maxScore** | **Integer**|  | [optional] |
| **q** | **String**| Only submissions whose creator name or post link contains this text, ignoring case. | [optional] |
| **sort** | **String**| What to sort by. Posts with no value to sort by (not read yet, not scored) come last in either direction. | [optional] [default to submittedAt] [enum: submittedAt, viewsEligible, engagementsLatest, earnedCents, authenticityScore] |
| **order** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListCampaignSubmissions200Response**](ListCampaignSubmissions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submissions |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## listCampaignSubmissionsWithHttpInfo

> ApiResponse<ListCampaignSubmissions200Response> listCampaignSubmissions listCampaignSubmissionsWithHttpInfo(campaignId, status, participantId, flag, platform, minScore, maxScore, q, sort, order, limit, skip)

List campaign submissions

Lists submitted posts with views, earnings, authenticity score and flags. Filter by status, participant, flag, platform or score range to build a review queue, for example &#x60;status&#x3D;pending_review&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String status = "received"; // String | 
        String participantId = "participantId_example"; // String | 
        String flag = "duplicate_media"; // String | 
        String platform = "tiktok"; // String | 
        Integer minScore = 56; // Integer | 
        Integer maxScore = 56; // Integer | 
        String q = "q_example"; // String | Only submissions whose creator name or post link contains this text, ignoring case.
        String sort = "submittedAt"; // String | What to sort by. Posts with no value to sort by (not read yet, not scored) come last in either direction.
        String order = "asc"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListCampaignSubmissions200Response> response = apiInstance.listCampaignSubmissionsWithHttpInfo(campaignId, status, participantId, flag, platform, minScore, maxScore, q, sort, order, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCampaignSubmissions");
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
| **campaignId** | **String**| Campaign ID. | |
| **status** | **String**|  | [optional] [enum: received, tracking, pending_review, approved, rejected, expired, withdrawn] |
| **participantId** | **String**|  | [optional] |
| **flag** | **String**|  | [optional] [enum: duplicate_media, duplicate_post, view_spike, linked_accounts, cross_operator, unreachable, post_deleted, account_restricted, low_authenticity, x_read_cap] |
| **platform** | **String**|  | [optional] [enum: tiktok, instagram, youtube, threads, pinterest, facebook, twitter] |
| **minScore** | **Integer**|  | [optional] |
| **maxScore** | **Integer**|  | [optional] |
| **q** | **String**| Only submissions whose creator name or post link contains this text, ignoring case. | [optional] |
| **sort** | **String**| What to sort by. Posts with no value to sort by (not read yet, not scored) come last in either direction. | [optional] [default to submittedAt] [enum: submittedAt, viewsEligible, engagementsLatest, earnedCents, authenticityScore] |
| **order** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListCampaignSubmissions200Response**](ListCampaignSubmissions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submissions |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## listCreatorCampaigns

> ListCreatorCampaigns200Response listCreatorCampaigns(status, profileId, q, limit, skip)

List creator campaigns

Lists the team&#39;s campaigns in the profiles this key can reach, newest first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String status = "draft"; // String | 
        String profileId = "profileId_example"; // String | Only campaigns in this profile.
        String q = "q_example"; // String | Only campaigns whose name or brand name contains this text, ignoring case.
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListCreatorCampaigns200Response result = apiInstance.listCreatorCampaigns(status, profileId, q, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCreatorCampaigns");
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
| **status** | **String**|  | [optional] [enum: draft, active, paused, closed] |
| **profileId** | **String**| Only campaigns in this profile. | [optional] |
| **q** | **String**| Only campaigns whose name or brand name contains this text, ignoring case. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListCreatorCampaigns200Response**](ListCreatorCampaigns200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaigns |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## listCreatorCampaignsWithHttpInfo

> ApiResponse<ListCreatorCampaigns200Response> listCreatorCampaigns listCreatorCampaignsWithHttpInfo(status, profileId, q, limit, skip)

List creator campaigns

Lists the team&#39;s campaigns in the profiles this key can reach, newest first. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String status = "draft"; // String | 
        String profileId = "profileId_example"; // String | Only campaigns in this profile.
        String q = "q_example"; // String | Only campaigns whose name or brand name contains this text, ignoring case.
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListCreatorCampaigns200Response> response = apiInstance.listCreatorCampaignsWithHttpInfo(status, profileId, q, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#listCreatorCampaigns");
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
| **status** | **String**|  | [optional] [enum: draft, active, paused, closed] |
| **profileId** | **String**| Only campaigns in this profile. | [optional] |
| **q** | **String**| Only campaigns whose name or brand name contains this text, ignoring case. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListCreatorCampaigns200Response**](ListCreatorCampaigns200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaigns |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## pauseCreatorCampaign

> CreateCreatorCampaign201Response pauseCreatorCampaign(campaignId)

Pause creator campaign

Moves an &#x60;active&#x60; campaign to &#x60;paused&#x60;: no new submissions, and approvals answer 409 until the campaign is activated again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            CreateCreatorCampaign201Response result = apiInstance.pauseCreatorCampaign(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#pauseCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## pauseCreatorCampaignWithHttpInfo

> ApiResponse<CreateCreatorCampaign201Response> pauseCreatorCampaign pauseCreatorCampaignWithHttpInfo(campaignId)

Pause creator campaign

Moves an &#x60;active&#x60; campaign to &#x60;paused&#x60;: no new submissions, and approvals answer 409 until the campaign is activated again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        try {
            ApiResponse<CreateCreatorCampaign201Response> response = apiInstance.pauseCreatorCampaignWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#pauseCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |

### Return type

ApiResponse<[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## raiseCreatorCampaignBudget

> CreateCreatorCampaign201Response raiseCreatorCampaignBudget(campaignId, raiseCreatorCampaignBudgetRequest, idempotencyKey)

Raise creator campaign budget

Raises the budget of a campaign that is &#x60;draft&#x60;, &#x60;active&#x60; or &#x60;paused&#x60;.  Only the budget changes. The pay terms stay as creators joined them, which &#x60;PATCH&#x60; refuses to change once the campaign is live.  - The new &#x60;budgetCents&#x60; must be above the current budget, otherwise 400 &#x60;invalid_field_value&#x60;. - When it is also above what the campaign has spent, &#x60;budgetExhaustedAt&#x60; is cleared and earnings that stopped at the old budget resume. - A closed campaign answers 409 &#x60;invalid_resource_state&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        RaiseCreatorCampaignBudgetRequest raiseCreatorCampaignBudgetRequest = new RaiseCreatorCampaignBudgetRequest(); // RaiseCreatorCampaignBudgetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            CreateCreatorCampaign201Response result = apiInstance.raiseCreatorCampaignBudget(campaignId, raiseCreatorCampaignBudgetRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#raiseCreatorCampaignBudget");
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
| **campaignId** | **String**| Campaign ID. | |
| **raiseCreatorCampaignBudgetRequest** | [**RaiseCreatorCampaignBudgetRequest**](RaiseCreatorCampaignBudgetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budget raised |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## raiseCreatorCampaignBudgetWithHttpInfo

> ApiResponse<CreateCreatorCampaign201Response> raiseCreatorCampaignBudget raiseCreatorCampaignBudgetWithHttpInfo(campaignId, raiseCreatorCampaignBudgetRequest, idempotencyKey)

Raise creator campaign budget

Raises the budget of a campaign that is &#x60;draft&#x60;, &#x60;active&#x60; or &#x60;paused&#x60;.  Only the budget changes. The pay terms stay as creators joined them, which &#x60;PATCH&#x60; refuses to change once the campaign is live.  - The new &#x60;budgetCents&#x60; must be above the current budget, otherwise 400 &#x60;invalid_field_value&#x60;. - When it is also above what the campaign has spent, &#x60;budgetExhaustedAt&#x60; is cleared and earnings that stopped at the old budget resume. - A closed campaign answers 409 &#x60;invalid_resource_state&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        RaiseCreatorCampaignBudgetRequest raiseCreatorCampaignBudgetRequest = new RaiseCreatorCampaignBudgetRequest(); // RaiseCreatorCampaignBudgetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<CreateCreatorCampaign201Response> response = apiInstance.raiseCreatorCampaignBudgetWithHttpInfo(campaignId, raiseCreatorCampaignBudgetRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#raiseCreatorCampaignBudget");
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
| **campaignId** | **String**| Campaign ID. | |
| **raiseCreatorCampaignBudgetRequest** | [**RaiseCreatorCampaignBudgetRequest**](RaiseCreatorCampaignBudgetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budget raised |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## reinstateCampaignParticipant

> GetCampaignParticipant200Response reinstateCampaignParticipant(campaignId, participantId)

Reinstate campaign participant

Reinstates a &#x60;suspended&#x60; participant: they can submit posts again. Any other status answers 409; a removed participant stays removed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            GetCampaignParticipant200Response result = apiInstance.reinstateCampaignParticipant(campaignId, participantId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#reinstateCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant reinstated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## reinstateCampaignParticipantWithHttpInfo

> ApiResponse<GetCampaignParticipant200Response> reinstateCampaignParticipant reinstateCampaignParticipantWithHttpInfo(campaignId, participantId)

Reinstate campaign participant

Reinstates a &#x60;suspended&#x60; participant: they can submit posts again. Any other status answers 409; a removed participant stays removed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            ApiResponse<GetCampaignParticipant200Response> response = apiInstance.reinstateCampaignParticipantWithHttpInfo(campaignId, participantId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#reinstateCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

ApiResponse<[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant reinstated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## rejectCampaignSubmission

> ApproveCampaignSubmission200Response rejectCampaignSubmission(campaignId, submissionId, rejectCampaignSubmissionRequest, idempotencyKey)

Reject campaign submission

Rejects a submission (also one already approved) and fires &#x60;campaign_submission.rejected&#x60;. Its tracking window is cancelled and its unsettled earnings return to the campaign budget. Rejecting a rejected submission returns it unchanged; an expired or withdrawn one answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        RejectCampaignSubmissionRequest rejectCampaignSubmissionRequest = new RejectCampaignSubmissionRequest(); // RejectCampaignSubmissionRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApproveCampaignSubmission200Response result = apiInstance.rejectCampaignSubmission(campaignId, submissionId, rejectCampaignSubmissionRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#rejectCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |
| **rejectCampaignSubmissionRequest** | [**RejectCampaignSubmissionRequest**](RejectCampaignSubmissionRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**ApproveCampaignSubmission200Response**](ApproveCampaignSubmission200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission rejected |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## rejectCampaignSubmissionWithHttpInfo

> ApiResponse<ApproveCampaignSubmission200Response> rejectCampaignSubmission rejectCampaignSubmissionWithHttpInfo(campaignId, submissionId, rejectCampaignSubmissionRequest, idempotencyKey)

Reject campaign submission

Rejects a submission (also one already approved) and fires &#x60;campaign_submission.rejected&#x60;. Its tracking window is cancelled and its unsettled earnings return to the campaign budget. Rejecting a rejected submission returns it unchanged; an expired or withdrawn one answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        RejectCampaignSubmissionRequest rejectCampaignSubmissionRequest = new RejectCampaignSubmissionRequest(); // RejectCampaignSubmissionRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<ApproveCampaignSubmission200Response> response = apiInstance.rejectCampaignSubmissionWithHttpInfo(campaignId, submissionId, rejectCampaignSubmissionRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#rejectCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |
| **rejectCampaignSubmissionRequest** | [**RejectCampaignSubmissionRequest**](RejectCampaignSubmissionRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**ApproveCampaignSubmission200Response**](ApproveCampaignSubmission200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission rejected |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## removeCampaignParticipant

> GetCampaignParticipant200Response removeCampaignParticipant(campaignId, participantId)

Remove campaign participant

Removes the participant from the campaign. Their earnings stay in the ledger. Removing an &#x60;invited&#x60; participant revokes their invite: the link stops working. Removing an already removed participant returns it unchanged. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            GetCampaignParticipant200Response result = apiInstance.removeCampaignParticipant(campaignId, participantId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#removeCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |

## removeCampaignParticipantWithHttpInfo

> ApiResponse<GetCampaignParticipant200Response> removeCampaignParticipant removeCampaignParticipantWithHttpInfo(campaignId, participantId)

Remove campaign participant

Removes the participant from the campaign. Their earnings stay in the ledger. Removing an &#x60;invited&#x60; participant revokes their invite: the link stops working. Removing an already removed participant returns it unchanged. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            ApiResponse<GetCampaignParticipant200Response> response = apiInstance.removeCampaignParticipantWithHttpInfo(campaignId, participantId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#removeCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

ApiResponse<[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |


## reopenCampaignSubmission

> ApproveCampaignSubmission200Response reopenCampaignSubmission(campaignId, submissionId, idempotencyKey)

Reopen campaign submission

Puts a rejected submission back to &#x60;pending_review&#x60; so it can be decided again. No webhook fires.  Its tracking window resumes, so it works only while that window has not ended.  ### When it can&#39;t be reopened  - The tracking window has ended: 409 &#x60;invalid_resource_state&#x60; (\&quot;This post&#39;s tracking window has ended.\&quot;). - A post that earned money which was already paid out cannot be reopened. - A post of a closed campaign cannot be reopened. - Any status other than rejected or &#x60;pending_review&#x60; answers 409.  Reopening a submission that is already &#x60;pending_review&#x60; returns it unchanged. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApproveCampaignSubmission200Response result = apiInstance.reopenCampaignSubmission(campaignId, submissionId, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#reopenCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**ApproveCampaignSubmission200Response**](ApproveCampaignSubmission200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission reopened |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## reopenCampaignSubmissionWithHttpInfo

> ApiResponse<ApproveCampaignSubmission200Response> reopenCampaignSubmission reopenCampaignSubmissionWithHttpInfo(campaignId, submissionId, idempotencyKey)

Reopen campaign submission

Puts a rejected submission back to &#x60;pending_review&#x60; so it can be decided again. No webhook fires.  Its tracking window resumes, so it works only while that window has not ended.  ### When it can&#39;t be reopened  - The tracking window has ended: 409 &#x60;invalid_resource_state&#x60; (\&quot;This post&#39;s tracking window has ended.\&quot;). - A post that earned money which was already paid out cannot be reopened. - A post of a closed campaign cannot be reopened. - Any status other than rejected or &#x60;pending_review&#x60; answers 409.  Reopening a submission that is already &#x60;pending_review&#x60; returns it unchanged. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String submissionId = "submissionId_example"; // String | Submission ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<ApproveCampaignSubmission200Response> response = apiInstance.reopenCampaignSubmissionWithHttpInfo(campaignId, submissionId, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#reopenCampaignSubmission");
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
| **campaignId** | **String**| Campaign ID. | |
| **submissionId** | **String**| Submission ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**ApproveCampaignSubmission200Response**](ApproveCampaignSubmission200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Submission reopened |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## resendCampaignParticipantInvite

> GetCampaignParticipant200Response resendCampaignParticipantInvite(campaignId, participantId, idempotencyKey)

Resend campaign participant invite

Emails an &#x60;invited&#x60; participant their personal invite link again. The link does not change, so a link you already sent keeps working. The email counts toward the daily invite email cap of your workspace.  Answers 409 when the participant has already joined, was suspended or removed, has no email, or the campaign is closed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            GetCampaignParticipant200Response result = apiInstance.resendCampaignParticipantInvite(campaignId, participantId, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#resendCampaignParticipantInvite");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invite email sent again |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## resendCampaignParticipantInviteWithHttpInfo

> ApiResponse<GetCampaignParticipant200Response> resendCampaignParticipantInvite resendCampaignParticipantInviteWithHttpInfo(campaignId, participantId, idempotencyKey)

Resend campaign participant invite

Emails an &#x60;invited&#x60; participant their personal invite link again. The link does not change, so a link you already sent keeps working. The email counts toward the daily invite email cap of your workspace.  Answers 409 when the participant has already joined, was suspended or removed, has no email, or the campaign is closed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<GetCampaignParticipant200Response> response = apiInstance.resendCampaignParticipantInviteWithHttpInfo(campaignId, participantId, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#resendCampaignParticipantInvite");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invite email sent again |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## settleCampaignParticipant

> SettleCampaignParticipant201Response settleCampaignParticipant(campaignId, participantId, settleCampaignParticipantRequest, idempotencyKey)

Settle campaign participant

Records a payout of the participant&#39;s payable balance and fires &#x60;campaign_payout.settled&#x60;.  Omit &#x60;amountCents&#x60; to settle the whole payable balance. An amount above it answers 400, and nothing payable answers 409. Send an &#x60;Idempotency-Key&#x60; so a retry never records the payout twice.  ### Settlement modes  - &#x60;none&#x60; settlement: records a payout you made elsewhere. - &#x60;external&#x60; settlement: pay from your own rails when &#x60;campaign_payout.payable&#x60; fires, then call this with your payout id in &#x60;externalReference&#x60; (required in this mode). - &#x60;treasury&#x60; settlement: transfers the amount from your Zernio balance to the creator&#39;s connected Stripe account, then records it with the Stripe transfer id as &#x60;externalReference&#x60;.  ### Treasury payouts  The transfer fee (4%, $0.50 minimum) is added on top: the creator receives the full amount and your balance is debited &#x60;totalCents&#x60;.  - The creator must have finished payout setup from their campaign page (409 otherwise). - A balance that does not cover the amount plus the fee answers 402. - Money from a card top-up charged under 7 days ago cannot be paid out yet: a payout that needs it answers 409 &#x60;payout_funds_locked&#x60; with the day it can be sent.  Set &#x60;recordOnly: true&#x60; to record a payout you made yourself instead of moving money through the treasury (the webhook then carries &#x60;recorded: true&#x60;).  A treasury payout needs an owner, admin or billing admin, signed in or through a full-access key they created (403 otherwise). Recording with &#x60;recordOnly&#x60; does not.  #### While Stripe confirms the transfer  The amount sits in the participant&#39;s &#x60;settling&#x60; balance; a reject in that window cannot reverse it.  - If Stripe refuses the transfer, the amount returns to payable. - If Stripe does not answer, the amount stays in &#x60;settling&#x60;. The next settle call for this participant finishes that payout first (even with nothing payable left).  #### Conflicts (409)  - A retry asking for a different &#x60;amountCents&#x60; than the payout in progress answers 409 with the amount in progress. - A settle while another request is still waiting on Stripe for the same payout answers 409 (\&quot;This payout is being sent to Stripe right now. Try again in a minute.\&quot;). - A payout Stripe has not confirmed after 24 hours answers 409 (\&quot;This payout is being confirmed with Stripe. Try again after the next reconciliation (within 24 hours).\&quot;) until the daily reconciliation finishes it: settled if Stripe made the transfer, returned to payable if it did not. - A creator held by an unfinished payout batch answers 409 (\&quot;This creator is in a card payout that is not finished yet.\&quot;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        SettleCampaignParticipantRequest settleCampaignParticipantRequest = new SettleCampaignParticipantRequest(); // SettleCampaignParticipantRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            SettleCampaignParticipant201Response result = apiInstance.settleCampaignParticipant(campaignId, participantId, settleCampaignParticipantRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#settleCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |
| **settleCampaignParticipantRequest** | [**SettleCampaignParticipantRequest**](SettleCampaignParticipantRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**SettleCampaignParticipant201Response**](SettleCampaignParticipant201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Settlement recorded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **402** | Your Zernio balance does not cover the amount plus the fee on top (code &#x60;payment_required&#x60;). Top up and retry. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **502** | Stripe did not confirm the transfer (code &#x60;temporarily_unavailable&#x60;). Retry the settle call: the transfer is not made twice within Stripe&#39;s 24-hour idempotency window; after that, retries answer 409 until the daily reconciliation settles the payout or returns it to payable. |  -  |

## settleCampaignParticipantWithHttpInfo

> ApiResponse<SettleCampaignParticipant201Response> settleCampaignParticipant settleCampaignParticipantWithHttpInfo(campaignId, participantId, settleCampaignParticipantRequest, idempotencyKey)

Settle campaign participant

Records a payout of the participant&#39;s payable balance and fires &#x60;campaign_payout.settled&#x60;.  Omit &#x60;amountCents&#x60; to settle the whole payable balance. An amount above it answers 400, and nothing payable answers 409. Send an &#x60;Idempotency-Key&#x60; so a retry never records the payout twice.  ### Settlement modes  - &#x60;none&#x60; settlement: records a payout you made elsewhere. - &#x60;external&#x60; settlement: pay from your own rails when &#x60;campaign_payout.payable&#x60; fires, then call this with your payout id in &#x60;externalReference&#x60; (required in this mode). - &#x60;treasury&#x60; settlement: transfers the amount from your Zernio balance to the creator&#39;s connected Stripe account, then records it with the Stripe transfer id as &#x60;externalReference&#x60;.  ### Treasury payouts  The transfer fee (4%, $0.50 minimum) is added on top: the creator receives the full amount and your balance is debited &#x60;totalCents&#x60;.  - The creator must have finished payout setup from their campaign page (409 otherwise). - A balance that does not cover the amount plus the fee answers 402. - Money from a card top-up charged under 7 days ago cannot be paid out yet: a payout that needs it answers 409 &#x60;payout_funds_locked&#x60; with the day it can be sent.  Set &#x60;recordOnly: true&#x60; to record a payout you made yourself instead of moving money through the treasury (the webhook then carries &#x60;recorded: true&#x60;).  A treasury payout needs an owner, admin or billing admin, signed in or through a full-access key they created (403 otherwise). Recording with &#x60;recordOnly&#x60; does not.  #### While Stripe confirms the transfer  The amount sits in the participant&#39;s &#x60;settling&#x60; balance; a reject in that window cannot reverse it.  - If Stripe refuses the transfer, the amount returns to payable. - If Stripe does not answer, the amount stays in &#x60;settling&#x60;. The next settle call for this participant finishes that payout first (even with nothing payable left).  #### Conflicts (409)  - A retry asking for a different &#x60;amountCents&#x60; than the payout in progress answers 409 with the amount in progress. - A settle while another request is still waiting on Stripe for the same payout answers 409 (\&quot;This payout is being sent to Stripe right now. Try again in a minute.\&quot;). - A payout Stripe has not confirmed after 24 hours answers 409 (\&quot;This payout is being confirmed with Stripe. Try again after the next reconciliation (within 24 hours).\&quot;) until the daily reconciliation finishes it: settled if Stripe made the transfer, returned to payable if it did not. - A creator held by an unfinished payout batch answers 409 (\&quot;This creator is in a card payout that is not finished yet.\&quot;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        SettleCampaignParticipantRequest settleCampaignParticipantRequest = new SettleCampaignParticipantRequest(); // SettleCampaignParticipantRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<SettleCampaignParticipant201Response> response = apiInstance.settleCampaignParticipantWithHttpInfo(campaignId, participantId, settleCampaignParticipantRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#settleCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |
| **settleCampaignParticipantRequest** | [**SettleCampaignParticipantRequest**](SettleCampaignParticipantRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**SettleCampaignParticipant201Response**](SettleCampaignParticipant201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Settlement recorded |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |
| **402** | Your Zernio balance does not cover the amount plus the fee on top (code &#x60;payment_required&#x60;). Top up and retry. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |
| **502** | Stripe did not confirm the transfer (code &#x60;temporarily_unavailable&#x60;). Retry the settle call: the transfer is not made twice within Stripe&#39;s 24-hour idempotency window; after that, retries answer 409 until the daily reconciliation settles the payout or returns it to payable. |  -  |


## suspendCampaignParticipant

> GetCampaignParticipant200Response suspendCampaignParticipant(campaignId, participantId)

Suspend campaign participant

Suspends an &#x60;active&#x60; participant: they can no longer submit posts. Any other status answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            GetCampaignParticipant200Response result = apiInstance.suspendCampaignParticipant(campaignId, participantId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#suspendCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant suspended |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## suspendCampaignParticipantWithHttpInfo

> ApiResponse<GetCampaignParticipant200Response> suspendCampaignParticipant suspendCampaignParticipantWithHttpInfo(campaignId, participantId)

Suspend campaign participant

Suspends an &#x60;active&#x60; participant: they can no longer submit posts. Any other status answers 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        String participantId = "participantId_example"; // String | Participant ID.
        try {
            ApiResponse<GetCampaignParticipant200Response> response = apiInstance.suspendCampaignParticipantWithHttpInfo(campaignId, participantId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#suspendCampaignParticipant");
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
| **campaignId** | **String**| Campaign ID. | |
| **participantId** | **String**| Participant ID. | |

### Return type

ApiResponse<[**GetCampaignParticipant200Response**](GetCampaignParticipant200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participant suspended |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |


## updateCreatorCampaign

> CreateCreatorCampaign201Response updateCreatorCampaign(campaignId, updateCreatorCampaignRequest)

Update creator campaign

Updates any subset of the campaign&#39;s settings. &#x60;economics&#x60; (and with it the campaign type) can only change while the campaign is a draft; afterwards that answers 409, and a live campaign&#39;s budget is raised with &#x60;POST /v1/creator-campaigns/{campaignId}/budget&#x60;. An empty body answers 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        UpdateCreatorCampaignRequest updateCreatorCampaignRequest = new UpdateCreatorCampaignRequest(); // UpdateCreatorCampaignRequest | 
        try {
            CreateCreatorCampaign201Response result = apiInstance.updateCreatorCampaign(campaignId, updateCreatorCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#updateCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |
| **updateCreatorCampaignRequest** | [**UpdateCreatorCampaignRequest**](UpdateCreatorCampaignRequest.md)|  | |

### Return type

[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

## updateCreatorCampaignWithHttpInfo

> ApiResponse<CreateCreatorCampaign201Response> updateCreatorCampaign updateCreatorCampaignWithHttpInfo(campaignId, updateCreatorCampaignRequest)

Update creator campaign

Updates any subset of the campaign&#39;s settings. &#x60;economics&#x60; (and with it the campaign type) can only change while the campaign is a draft; afterwards that answers 409, and a live campaign&#39;s budget is raised with &#x60;POST /v1/creator-campaigns/{campaignId}/budget&#x60;. An empty body answers 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CreatorCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CreatorCampaignsApi apiInstance = new CreatorCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Campaign ID.
        UpdateCreatorCampaignRequest updateCreatorCampaignRequest = new UpdateCreatorCampaignRequest(); // UpdateCreatorCampaignRequest | 
        try {
            ApiResponse<CreateCreatorCampaign201Response> response = apiInstance.updateCreatorCampaignWithHttpInfo(campaignId, updateCreatorCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorCampaignsApi#updateCreatorCampaign");
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
| **campaignId** | **String**| Campaign ID. | |
| **updateCreatorCampaignRequest** | [**UpdateCreatorCampaignRequest**](UpdateCreatorCampaignRequest.md)|  | |

### Return type

ApiResponse<[**CreateCreatorCampaign201Response**](CreateCreatorCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused. Code &#x60;feature_not_available&#x60;: creator campaigns run on usage-based billing and the workspace that owns the campaign is not on it yet (\&quot;Creator campaigns require usage-based billing...\&quot;; contact support to switch), or the campaign reached &#x60;caps.maxParticipants&#x60; (invites and joins only). Code &#x60;insufficient_permissions&#x60;: a restricted API key without the &#x60;creator_campaigns&#x60; resource group.  |  -  |
| **404** | The campaign, participant or submission does not exist, belongs to another team, or sits in a profile this key cannot reach (code &#x60;resource_not_found&#x60;). |  -  |
| **409** | The campaign, participant or submission is not in a state that allows this action (code &#x60;invalid_resource_state&#x60;); the message names the current state. Also returned while the same &#x60;Idempotency-Key&#x60; is still processing. |  -  |

