# CreatorPortalApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCreatorPayoutLogin**](CreatorPortalApi.md#createCreatorPayoutLogin) | **POST** /public/creator-campaigns/{token}/payout-login | Open the creator&#39;s Stripe dashboard |
| [**createCreatorPayoutLoginWithHttpInfo**](CreatorPortalApi.md#createCreatorPayoutLoginWithHttpInfo) | **POST** /public/creator-campaigns/{token}/payout-login | Open the creator&#39;s Stripe dashboard |
| [**getCreatorPayoutStatement**](CreatorPortalApi.md#getCreatorPayoutStatement) | **GET** /public/creator-campaigns/{token}/payouts/{transferId}/statement | Download a payout statement |
| [**getCreatorPayoutStatementWithHttpInfo**](CreatorPortalApi.md#getCreatorPayoutStatementWithHttpInfo) | **GET** /public/creator-campaigns/{token}/payouts/{transferId}/statement | Download a payout statement |
| [**getCreatorPayouts**](CreatorPortalApi.md#getCreatorPayouts) | **GET** /public/creator-campaigns/{token}/payouts | List a creator&#39;s earnings history |
| [**getCreatorPayoutsWithHttpInfo**](CreatorPortalApi.md#getCreatorPayoutsWithHttpInfo) | **GET** /public/creator-campaigns/{token}/payouts | List a creator&#39;s earnings history |
| [**getCreatorPortal**](CreatorPortalApi.md#getCreatorPortal) | **GET** /public/creator-campaigns/{token} | Read a creator invite or participant page |
| [**getCreatorPortalWithHttpInfo**](CreatorPortalApi.md#getCreatorPortalWithHttpInfo) | **GET** /public/creator-campaigns/{token} | Read a creator invite or participant page |
| [**joinCreatorCampaign**](CreatorPortalApi.md#joinCreatorCampaign) | **POST** /public/creator-campaigns/{token} | Join a campaign |
| [**joinCreatorCampaignWithHttpInfo**](CreatorPortalApi.md#joinCreatorCampaignWithHttpInfo) | **POST** /public/creator-campaigns/{token} | Join a campaign |
| [**presignCreatorDraftUpload**](CreatorPortalApi.md#presignCreatorDraftUpload) | **POST** /public/creator-campaigns/{token}/drafts/upload | Get an upload URL for a draft |
| [**presignCreatorDraftUploadWithHttpInfo**](CreatorPortalApi.md#presignCreatorDraftUploadWithHttpInfo) | **POST** /public/creator-campaigns/{token}/drafts/upload | Get an upload URL for a draft |
| [**recoverCreatorPortalLinks**](CreatorPortalApi.md#recoverCreatorPortalLinks) | **POST** /public/creator-campaigns/recover-link | Email a creator their campaign links |
| [**recoverCreatorPortalLinksWithHttpInfo**](CreatorPortalApi.md#recoverCreatorPortalLinksWithHttpInfo) | **POST** /public/creator-campaigns/recover-link | Email a creator their campaign links |
| [**removeCreatorAccount**](CreatorPortalApi.md#removeCreatorAccount) | **DELETE** /public/creator-campaigns/{token}/accounts/{accountId} | Remove a connected account |
| [**removeCreatorAccountWithHttpInfo**](CreatorPortalApi.md#removeCreatorAccountWithHttpInfo) | **DELETE** /public/creator-campaigns/{token}/accounts/{accountId} | Remove a connected account |
| [**requestCreatorSample**](CreatorPortalApi.md#requestCreatorSample) | **POST** /public/creator-campaigns/{token}/samples | Request a product sample |
| [**requestCreatorSampleWithHttpInfo**](CreatorPortalApi.md#requestCreatorSampleWithHttpInfo) | **POST** /public/creator-campaigns/{token}/samples | Request a product sample |
| [**setCreatorSparkCode**](CreatorPortalApi.md#setCreatorSparkCode) | **PUT** /public/creator-campaigns/{token}/submissions/{submissionId}/spark-code | Set a post&#39;s Spark code |
| [**setCreatorSparkCodeWithHttpInfo**](CreatorPortalApi.md#setCreatorSparkCodeWithHttpInfo) | **PUT** /public/creator-campaigns/{token}/submissions/{submissionId}/spark-code | Set a post&#39;s Spark code |
| [**startCreatorConnect**](CreatorPortalApi.md#startCreatorConnect) | **POST** /public/creator-campaigns/{token}/connect | Start connecting a creator account |
| [**startCreatorConnectWithHttpInfo**](CreatorPortalApi.md#startCreatorConnectWithHttpInfo) | **POST** /public/creator-campaigns/{token}/connect | Start connecting a creator account |
| [**startCreatorPayouts**](CreatorPortalApi.md#startCreatorPayouts) | **POST** /public/creator-campaigns/{token}/payouts | Start payout onboarding |
| [**startCreatorPayoutsWithHttpInfo**](CreatorPortalApi.md#startCreatorPayoutsWithHttpInfo) | **POST** /public/creator-campaigns/{token}/payouts | Start payout onboarding |
| [**submitCreatorDraft**](CreatorPortalApi.md#submitCreatorDraft) | **POST** /public/creator-campaigns/{token}/drafts | Submit a draft for review |
| [**submitCreatorDraftWithHttpInfo**](CreatorPortalApi.md#submitCreatorDraftWithHttpInfo) | **POST** /public/creator-campaigns/{token}/drafts | Submit a draft for review |
| [**submitCreatorPost**](CreatorPortalApi.md#submitCreatorPost) | **POST** /public/creator-campaigns/{token}/submissions | Submit a post |
| [**submitCreatorPostWithHttpInfo**](CreatorPortalApi.md#submitCreatorPostWithHttpInfo) | **POST** /public/creator-campaigns/{token}/submissions | Submit a post |



## createCreatorPayoutLogin

> CreateCreatorPayoutLogin200Response createCreatorPayoutLogin(token)

Open the creator&#39;s Stripe dashboard

Returns a one-time link into the creator&#39;s Stripe Express dashboard, where they change bank details and see each payout. Only after the creator submitted their payout details. About 20 attempts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        try {
            CreateCreatorPayoutLogin200Response result = apiInstance.createCreatorPayoutLogin(token);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#createCreatorPayoutLogin");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |

### Return type

[**CreateCreatorPayoutLogin200Response**](CreateCreatorPayoutLogin200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stripe login link. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The creator has not submitted payout details yet, or the campaign team pays them directly (\&quot;Finish payout setup first.\&quot;, &#x60;invalid_resource_state&#x60;). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## createCreatorPayoutLoginWithHttpInfo

> ApiResponse<CreateCreatorPayoutLogin200Response> createCreatorPayoutLogin createCreatorPayoutLoginWithHttpInfo(token)

Open the creator&#39;s Stripe dashboard

Returns a one-time link into the creator&#39;s Stripe Express dashboard, where they change bank details and see each payout. Only after the creator submitted their payout details. About 20 attempts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        try {
            ApiResponse<CreateCreatorPayoutLogin200Response> response = apiInstance.createCreatorPayoutLoginWithHttpInfo(token);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#createCreatorPayoutLogin");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |

### Return type

ApiResponse<[**CreateCreatorPayoutLogin200Response**](CreateCreatorPayoutLogin200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stripe login link. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The creator has not submitted payout details yet, or the campaign team pays them directly (\&quot;Finish payout setup first.\&quot;, &#x60;invalid_resource_state&#x60;). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## getCreatorPayoutStatement

> File getCreatorPayoutStatement(token, transferId)

Download a payout statement

A PDF statement of one paid payout to this creator: who paid, the campaign, the date, the amount and the Stripe transfer id. It is a statement of a payment, not a tax invoice.  Only for a paid payout of this participant; anything else answers 404.  About 60 downloads per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        String transferId = "transferId_example"; // String | 
        try {
            File result = apiInstance.getCreatorPayoutStatement(token, transferId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#getCreatorPayoutStatement");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **transferId** | **String**|  | |

### Return type

[**File**](File.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The statement, as an attachment. |  -  |
| **404** | The link is invalid, or no paid payout of this participant has this id (\&quot;Payout not found.\&quot;). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## getCreatorPayoutStatementWithHttpInfo

> ApiResponse<File> getCreatorPayoutStatement getCreatorPayoutStatementWithHttpInfo(token, transferId)

Download a payout statement

A PDF statement of one paid payout to this creator: who paid, the campaign, the date, the amount and the Stripe transfer id. It is a statement of a payment, not a tax invoice.  Only for a paid payout of this participant; anything else answers 404.  About 60 downloads per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        String transferId = "transferId_example"; // String | 
        try {
            ApiResponse<File> response = apiInstance.getCreatorPayoutStatementWithHttpInfo(token, transferId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#getCreatorPayoutStatement");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **transferId** | **String**|  | |

### Return type

ApiResponse<[**File**](File.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The statement, as an attachment. |  -  |
| **404** | The link is invalid, or no paid payout of this participant has this id (\&quot;Payout not found.\&quot;). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## getCreatorPayouts

> GetCreatorPayouts200Response getCreatorPayouts(token, limit, skip)

List a creator&#39;s earnings history

The participant&#39;s ledger entries, newest first, with the bucket each one moved money from and to (&#x60;accruing&#x60;, &#x60;owed&#x60;, &#x60;payable&#x60;, &#x60;settling&#x60;, &#x60;settled&#x60;; null for the other side), plus the payout setup. Never cached. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            GetCreatorPayouts200Response result = apiInstance.getCreatorPayouts(token, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#getCreatorPayouts");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**GetCreatorPayouts200Response**](GetCreatorPayouts200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Earnings history and payout setup. |  -  |
| **400** | Invalid request |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |

## getCreatorPayoutsWithHttpInfo

> ApiResponse<GetCreatorPayouts200Response> getCreatorPayouts getCreatorPayoutsWithHttpInfo(token, limit, skip)

List a creator&#39;s earnings history

The participant&#39;s ledger entries, newest first, with the bucket each one moved money from and to (&#x60;accruing&#x60;, &#x60;owed&#x60;, &#x60;payable&#x60;, &#x60;settling&#x60;, &#x60;settled&#x60;; null for the other side), plus the payout setup. Never cached. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<GetCreatorPayouts200Response> response = apiInstance.getCreatorPayoutsWithHttpInfo(token, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#getCreatorPayouts");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**GetCreatorPayouts200Response**](GetCreatorPayouts200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Earnings history and payout setup. |  -  |
| **400** | Invalid request |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |


## getCreatorPortal

> GetCreatorPortal200Response getCreatorPortal(token)

Read a creator invite or participant page

What a creator sees behind a campaign link, with no API key. Never cached.  &#x60;token&#x60; is one of:  - An open invite token (from &#x60;POST /v1/creator-campaigns/{campaignId}/invite-link&#x60;): answers &#x60;kind: invite&#x60; with the campaign only. - A participant token (from an invite or a join): answers &#x60;kind: participant&#x60; with the creator&#39;s connected accounts, latest 100 submissions, draft versions, sample requests, earnings and payout setup. A creator held for approval reads it with &#x60;participant.status&#x60; &#x60;pending&#x60; (or &#x60;denied&#x60; once turned away).  Reading a participant page also re-checks the creator&#39;s connected accounts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        try {
            GetCreatorPortal200Response result = apiInstance.getCreatorPortal(token);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#getCreatorPortal");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |

### Return type

[**GetCreatorPortal200Response**](GetCreatorPortal200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The invite or participant page. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |

## getCreatorPortalWithHttpInfo

> ApiResponse<GetCreatorPortal200Response> getCreatorPortal getCreatorPortalWithHttpInfo(token)

Read a creator invite or participant page

What a creator sees behind a campaign link, with no API key. Never cached.  &#x60;token&#x60; is one of:  - An open invite token (from &#x60;POST /v1/creator-campaigns/{campaignId}/invite-link&#x60;): answers &#x60;kind: invite&#x60; with the campaign only. - A participant token (from an invite or a join): answers &#x60;kind: participant&#x60; with the creator&#39;s connected accounts, latest 100 submissions, draft versions, sample requests, earnings and payout setup. A creator held for approval reads it with &#x60;participant.status&#x60; &#x60;pending&#x60; (or &#x60;denied&#x60; once turned away).  Reading a participant page also re-checks the creator&#39;s connected accounts. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        try {
            ApiResponse<GetCreatorPortal200Response> response = apiInstance.getCreatorPortalWithHttpInfo(token);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#getCreatorPortal");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |

### Return type

ApiResponse<[**GetCreatorPortal200Response**](GetCreatorPortal200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The invite or participant page. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |


## joinCreatorCampaign

> JoinCreatorCampaign201Response joinCreatorCampaign(token, joinCreatorCampaignRequest)

Join a campaign

Accepts a participant invite, or joins through an open invite link.  - Participant token: the body is ignored and the invite is accepted. - Open invite token: a new participant is created from &#x60;displayName&#x60; (required) and &#x60;email&#x60; (optional), and a fresh participant token comes back. Keep it: it is the creator&#39;s only key to their page. - On a campaign with &#x60;joinApproval: manual&#x60;, an open-link joiner lands &#x60;pending&#x60; and &#x60;campaign_participant.pending&#x60; fires instead of &#x60;campaign_participant.joined&#x60;. A pending creator holds no place under &#x60;caps.maxParticipants&#x60; (the limit is checked when the operator approves them) and cannot submit posts, drafts or sample requests until approved. Personal invites always get straight in.  Open-link joins are limited to about 20 per IP address and 60 per link every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        JoinCreatorCampaignRequest joinCreatorCampaignRequest = new JoinCreatorCampaignRequest(); // JoinCreatorCampaignRequest | 
        try {
            JoinCreatorCampaign201Response result = apiInstance.joinCreatorCampaign(token, joinCreatorCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#joinCreatorCampaign");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **joinCreatorCampaignRequest** | [**JoinCreatorCampaignRequest**](JoinCreatorCampaignRequest.md)|  | [optional] |

### Return type

[**JoinCreatorCampaign201Response**](JoinCreatorCampaign201Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Joined. Use &#x60;participantToken&#x60; for every later call. |  -  |
| **400** | Missing &#x60;displayName&#x60; on an open-link join (\&quot;Add your name to join.\&quot;, &#x60;missing_required_field&#x60;), an invalid field, or the campaign has ended (&#x60;invalid_resource_state&#x60;, \&quot;This campaign has ended.\&quot;). |  -  |
| **403** | The campaign is not taking new creators (&#x60;feature_not_available&#x60;, \&quot;This campaign is not taking new creators right now. Ask the campaign team.\&quot;), for example because it reached its participant cap. Not returned for the cap on a &#x60;joinApproval: manual&#x60; campaign, where the cap is checked on approval. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## joinCreatorCampaignWithHttpInfo

> ApiResponse<JoinCreatorCampaign201Response> joinCreatorCampaign joinCreatorCampaignWithHttpInfo(token, joinCreatorCampaignRequest)

Join a campaign

Accepts a participant invite, or joins through an open invite link.  - Participant token: the body is ignored and the invite is accepted. - Open invite token: a new participant is created from &#x60;displayName&#x60; (required) and &#x60;email&#x60; (optional), and a fresh participant token comes back. Keep it: it is the creator&#39;s only key to their page. - On a campaign with &#x60;joinApproval: manual&#x60;, an open-link joiner lands &#x60;pending&#x60; and &#x60;campaign_participant.pending&#x60; fires instead of &#x60;campaign_participant.joined&#x60;. A pending creator holds no place under &#x60;caps.maxParticipants&#x60; (the limit is checked when the operator approves them) and cannot submit posts, drafts or sample requests until approved. Personal invites always get straight in.  Open-link joins are limited to about 20 per IP address and 60 per link every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        JoinCreatorCampaignRequest joinCreatorCampaignRequest = new JoinCreatorCampaignRequest(); // JoinCreatorCampaignRequest | 
        try {
            ApiResponse<JoinCreatorCampaign201Response> response = apiInstance.joinCreatorCampaignWithHttpInfo(token, joinCreatorCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#joinCreatorCampaign");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **joinCreatorCampaignRequest** | [**JoinCreatorCampaignRequest**](JoinCreatorCampaignRequest.md)|  | [optional] |

### Return type

ApiResponse<[**JoinCreatorCampaign201Response**](JoinCreatorCampaign201Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Joined. Use &#x60;participantToken&#x60; for every later call. |  -  |
| **400** | Missing &#x60;displayName&#x60; on an open-link join (\&quot;Add your name to join.\&quot;, &#x60;missing_required_field&#x60;), an invalid field, or the campaign has ended (&#x60;invalid_resource_state&#x60;, \&quot;This campaign has ended.\&quot;). |  -  |
| **403** | The campaign is not taking new creators (&#x60;feature_not_available&#x60;, \&quot;This campaign is not taking new creators right now. Ask the campaign team.\&quot;), for example because it reached its participant cap. Not returned for the cap on a &#x60;joinApproval: manual&#x60; campaign, where the cap is checked on approval. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## presignCreatorDraftUpload

> PresignCreatorDraftUpload200Response presignCreatorDraftUpload(token, presignCreatorDraftUploadRequest)

Get an upload URL for a draft

Returns a presigned URL to upload one draft file to, on a campaign with &#x60;requireDraftApproval&#x60;. &#x60;PUT&#x60; the file to &#x60;uploadUrl&#x60; with the same &#x60;Content-Type&#x60;, then pass &#x60;publicUrl&#x60; as &#x60;mediaUrl&#x60; to &#x60;POST /public/creator-campaigns/{token}/drafts&#x60;. The URL expires after &#x60;expiresIn&#x60; seconds.  Accepted files: MP4, MOV or WebM video, JPG, PNG or WebP image, up to 500 MB. About 20 uploads per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        PresignCreatorDraftUploadRequest presignCreatorDraftUploadRequest = new PresignCreatorDraftUploadRequest(); // PresignCreatorDraftUploadRequest | 
        try {
            PresignCreatorDraftUpload200Response result = apiInstance.presignCreatorDraftUpload(token, presignCreatorDraftUploadRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#presignCreatorDraftUpload");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **presignCreatorDraftUploadRequest** | [**PresignCreatorDraftUploadRequest**](PresignCreatorDraftUploadRequest.md)|  | |

### Return type

[**PresignCreatorDraftUpload200Response**](PresignCreatorDraftUpload200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upload URL. |  -  |
| **400** | An invalid field: an unsupported &#x60;contentType&#x60; or a &#x60;size&#x60; over 500 MB. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The campaign does not review drafts, is not accepting posts (not started, paused or ended), the invite is not accepted yet, or the creator is pending, denied, suspended or removed (&#x60;invalid_resource_state&#x60;; the message says which). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## presignCreatorDraftUploadWithHttpInfo

> ApiResponse<PresignCreatorDraftUpload200Response> presignCreatorDraftUpload presignCreatorDraftUploadWithHttpInfo(token, presignCreatorDraftUploadRequest)

Get an upload URL for a draft

Returns a presigned URL to upload one draft file to, on a campaign with &#x60;requireDraftApproval&#x60;. &#x60;PUT&#x60; the file to &#x60;uploadUrl&#x60; with the same &#x60;Content-Type&#x60;, then pass &#x60;publicUrl&#x60; as &#x60;mediaUrl&#x60; to &#x60;POST /public/creator-campaigns/{token}/drafts&#x60;. The URL expires after &#x60;expiresIn&#x60; seconds.  Accepted files: MP4, MOV or WebM video, JPG, PNG or WebP image, up to 500 MB. About 20 uploads per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        PresignCreatorDraftUploadRequest presignCreatorDraftUploadRequest = new PresignCreatorDraftUploadRequest(); // PresignCreatorDraftUploadRequest | 
        try {
            ApiResponse<PresignCreatorDraftUpload200Response> response = apiInstance.presignCreatorDraftUploadWithHttpInfo(token, presignCreatorDraftUploadRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#presignCreatorDraftUpload");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **presignCreatorDraftUploadRequest** | [**PresignCreatorDraftUploadRequest**](PresignCreatorDraftUploadRequest.md)|  | |

### Return type

ApiResponse<[**PresignCreatorDraftUpload200Response**](PresignCreatorDraftUpload200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upload URL. |  -  |
| **400** | An invalid field: an unsupported &#x60;contentType&#x60; or a &#x60;size&#x60; over 500 MB. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The campaign does not review drafts, is not accepting posts (not started, paused or ended), the invite is not accepted yet, or the creator is pending, denied, suspended or removed (&#x60;invalid_resource_state&#x60;; the message says which). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## recoverCreatorPortalLinks

> RecoverCreatorPortalLinks202Response recoverCreatorPortalLinks(recoverCreatorPortalLinksRequest)

Email a creator their campaign links

For a creator who lost their link. Emails every personal participant link held by &#x60;email&#x60; in one message, optionally only the one for &#x60;campaignId&#x60;.  - Removed participants and draft campaigns are left out. - Always answers 202 with the same body, so the answer never tells whether the address has links. - Limited to 5 requests per hour per email address and 5 per hour per IP address. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        RecoverCreatorPortalLinksRequest recoverCreatorPortalLinksRequest = new RecoverCreatorPortalLinksRequest(); // RecoverCreatorPortalLinksRequest | 
        try {
            RecoverCreatorPortalLinks202Response result = apiInstance.recoverCreatorPortalLinks(recoverCreatorPortalLinksRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#recoverCreatorPortalLinks");
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
| **recoverCreatorPortalLinksRequest** | [**RecoverCreatorPortalLinksRequest**](RecoverCreatorPortalLinksRequest.md)|  | |

### Return type

[**RecoverCreatorPortalLinks202Response**](RecoverCreatorPortalLinks202Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. If the address has links, they are on their way. |  -  |
| **400** | The email is missing or not a valid address. |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## recoverCreatorPortalLinksWithHttpInfo

> ApiResponse<RecoverCreatorPortalLinks202Response> recoverCreatorPortalLinks recoverCreatorPortalLinksWithHttpInfo(recoverCreatorPortalLinksRequest)

Email a creator their campaign links

For a creator who lost their link. Emails every personal participant link held by &#x60;email&#x60; in one message, optionally only the one for &#x60;campaignId&#x60;.  - Removed participants and draft campaigns are left out. - Always answers 202 with the same body, so the answer never tells whether the address has links. - Limited to 5 requests per hour per email address and 5 per hour per IP address. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        RecoverCreatorPortalLinksRequest recoverCreatorPortalLinksRequest = new RecoverCreatorPortalLinksRequest(); // RecoverCreatorPortalLinksRequest | 
        try {
            ApiResponse<RecoverCreatorPortalLinks202Response> response = apiInstance.recoverCreatorPortalLinksWithHttpInfo(recoverCreatorPortalLinksRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#recoverCreatorPortalLinks");
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
| **recoverCreatorPortalLinksRequest** | [**RecoverCreatorPortalLinksRequest**](RecoverCreatorPortalLinksRequest.md)|  | |

### Return type

ApiResponse<[**RecoverCreatorPortalLinks202Response**](RecoverCreatorPortalLinks202Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. If the address has links, they are on their way. |  -  |
| **400** | The email is missing or not a valid address. |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## removeCreatorAccount

> RemoveCreatorAccount200Response removeCreatorAccount(token, accountId)

Remove a connected account

Disconnects one of the creator&#39;s accounts. The account belongs to the creator, not to one campaign, so it stops counting in every campaign of this brand they joined.  What its posts already earned stays: accrued, approved and paid amounts are not touched.  Refused while a post from the account is still counting views, because those views are read through the account. It can be removed once their tracking ends. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        String accountId = "accountId_example"; // String | The `id` of one of the participant's `accounts`.
        try {
            RemoveCreatorAccount200Response result = apiInstance.removeCreatorAccount(token, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#removeCreatorAccount");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **accountId** | **String**| The &#x60;id&#x60; of one of the participant&#39;s &#x60;accounts&#x60;. | |

### Return type

[**RemoveCreatorAccount200Response**](RemoveCreatorAccount200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Removed. |  -  |
| **400** | Invalid request |  -  |
| **404** | The link is invalid or expired, or the account is not one of the participant&#39;s accounts on the campaign&#39;s platforms (&#x60;resource_not_found&#x60;). |  -  |
| **409** | A post from the account is still counting views (&#x60;invalid_resource_state&#x60;; the message says how many). |  -  |

## removeCreatorAccountWithHttpInfo

> ApiResponse<RemoveCreatorAccount200Response> removeCreatorAccount removeCreatorAccountWithHttpInfo(token, accountId)

Remove a connected account

Disconnects one of the creator&#39;s accounts. The account belongs to the creator, not to one campaign, so it stops counting in every campaign of this brand they joined.  What its posts already earned stays: accrued, approved and paid amounts are not touched.  Refused while a post from the account is still counting views, because those views are read through the account. It can be removed once their tracking ends. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        String accountId = "accountId_example"; // String | The `id` of one of the participant's `accounts`.
        try {
            ApiResponse<RemoveCreatorAccount200Response> response = apiInstance.removeCreatorAccountWithHttpInfo(token, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#removeCreatorAccount");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **accountId** | **String**| The &#x60;id&#x60; of one of the participant&#39;s &#x60;accounts&#x60;. | |

### Return type

ApiResponse<[**RemoveCreatorAccount200Response**](RemoveCreatorAccount200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Removed. |  -  |
| **400** | Invalid request |  -  |
| **404** | The link is invalid or expired, or the account is not one of the participant&#39;s accounts on the campaign&#39;s platforms (&#x60;resource_not_found&#x60;). |  -  |
| **409** | A post from the account is still counting views (&#x60;invalid_resource_state&#x60;; the message says how many). |  -  |


## requestCreatorSample

> RequestCreatorSample201Response requestCreatorSample(token, requestCreatorSampleRequest)

Request a product sample

Asks for a free sample of one of the campaign&#39;s &#x60;sampleProducts&#x60;, shipped to &#x60;shippingAddress&#x60;, and fires &#x60;campaign_sample.requested&#x60;. The request waits for the campaign team; on approval the creator gets a single-use discount code for the product.  - A product with &#x60;variants&#x60; needs &#x60;variantId&#x60;. - One open request per product: asking again while one is pending, approved or shipped answers 409. A declined product can be asked again.  About 10 requests per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        RequestCreatorSampleRequest requestCreatorSampleRequest = new RequestCreatorSampleRequest(); // RequestCreatorSampleRequest | 
        try {
            RequestCreatorSample201Response result = apiInstance.requestCreatorSample(token, requestCreatorSampleRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#requestCreatorSample");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **requestCreatorSampleRequest** | [**RequestCreatorSampleRequest**](RequestCreatorSampleRequest.md)|  | |

### Return type

[**RequestCreatorSample201Response**](RequestCreatorSample201Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Sample requested. |  -  |
| **400** | An invalid field, a product the campaign does not offer (&#x60;invalid_field_value&#x60;, &#x60;param: productId&#x60;), or a missing or unknown option (&#x60;param: variantId&#x60;, \&quot;Pick one of the options for this product\&quot;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The campaign offers no samples or is not accepting posts, the creator is not active in it (invite not accepted, pending, denied, suspended or removed), or the creator already has an open request for this product (&#x60;invalid_resource_state&#x60;; the message says which). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## requestCreatorSampleWithHttpInfo

> ApiResponse<RequestCreatorSample201Response> requestCreatorSample requestCreatorSampleWithHttpInfo(token, requestCreatorSampleRequest)

Request a product sample

Asks for a free sample of one of the campaign&#39;s &#x60;sampleProducts&#x60;, shipped to &#x60;shippingAddress&#x60;, and fires &#x60;campaign_sample.requested&#x60;. The request waits for the campaign team; on approval the creator gets a single-use discount code for the product.  - A product with &#x60;variants&#x60; needs &#x60;variantId&#x60;. - One open request per product: asking again while one is pending, approved or shipped answers 409. A declined product can be asked again.  About 10 requests per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        RequestCreatorSampleRequest requestCreatorSampleRequest = new RequestCreatorSampleRequest(); // RequestCreatorSampleRequest | 
        try {
            ApiResponse<RequestCreatorSample201Response> response = apiInstance.requestCreatorSampleWithHttpInfo(token, requestCreatorSampleRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#requestCreatorSample");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **requestCreatorSampleRequest** | [**RequestCreatorSampleRequest**](RequestCreatorSampleRequest.md)|  | |

### Return type

ApiResponse<[**RequestCreatorSample201Response**](RequestCreatorSample201Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Sample requested. |  -  |
| **400** | An invalid field, a product the campaign does not offer (&#x60;invalid_field_value&#x60;, &#x60;param: productId&#x60;), or a missing or unknown option (&#x60;param: variantId&#x60;, \&quot;Pick one of the options for this product\&quot;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The campaign offers no samples or is not accepting posts, the creator is not active in it (invite not accepted, pending, denied, suspended or removed), or the creator already has an open request for this product (&#x60;invalid_resource_state&#x60;; the message says which). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## setCreatorSparkCode

> SetCreatorSparkCode200Response setCreatorSparkCode(token, submissionId, setCreatorSparkCodeRequest)

Set a post&#39;s Spark code

The creator pastes the Spark code of one of their TikTok posts (generated in the TikTok app under the post&#39;s ad settings), so the brand can run the post as a Spark Ad under the creator&#39;s handle.  Send &#x60;null&#x60; to clear it. The code is never returned: submissions only expose &#x60;hasSparkCode&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        String submissionId = "submissionId_example"; // String | The `id` of one of the participant's `submissions`.
        SetCreatorSparkCodeRequest setCreatorSparkCodeRequest = new SetCreatorSparkCodeRequest(); // SetCreatorSparkCodeRequest | 
        try {
            SetCreatorSparkCode200Response result = apiInstance.setCreatorSparkCode(token, submissionId, setCreatorSparkCodeRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#setCreatorSparkCode");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **submissionId** | **String**| The &#x60;id&#x60; of one of the participant&#39;s &#x60;submissions&#x60;. | |
| **setCreatorSparkCodeRequest** | [**SetCreatorSparkCodeRequest**](SetCreatorSparkCodeRequest.md)|  | |

### Return type

[**SetCreatorSparkCode200Response**](SetCreatorSparkCode200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Saved. |  -  |
| **400** | Invalid input, or the post is not a TikTok post (&#x60;invalid_field_value&#x60;). |  -  |
| **404** | The link is invalid or expired, or the post is not one of the participant&#39;s submissions (&#x60;resource_not_found&#x60;). |  -  |
| **409** | The post was rejected or withdrawn (&#x60;invalid_resource_state&#x60;). |  -  |

## setCreatorSparkCodeWithHttpInfo

> ApiResponse<SetCreatorSparkCode200Response> setCreatorSparkCode setCreatorSparkCodeWithHttpInfo(token, submissionId, setCreatorSparkCodeRequest)

Set a post&#39;s Spark code

The creator pastes the Spark code of one of their TikTok posts (generated in the TikTok app under the post&#39;s ad settings), so the brand can run the post as a Spark Ad under the creator&#39;s handle.  Send &#x60;null&#x60; to clear it. The code is never returned: submissions only expose &#x60;hasSparkCode&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        String submissionId = "submissionId_example"; // String | The `id` of one of the participant's `submissions`.
        SetCreatorSparkCodeRequest setCreatorSparkCodeRequest = new SetCreatorSparkCodeRequest(); // SetCreatorSparkCodeRequest | 
        try {
            ApiResponse<SetCreatorSparkCode200Response> response = apiInstance.setCreatorSparkCodeWithHttpInfo(token, submissionId, setCreatorSparkCodeRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#setCreatorSparkCode");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **submissionId** | **String**| The &#x60;id&#x60; of one of the participant&#39;s &#x60;submissions&#x60;. | |
| **setCreatorSparkCodeRequest** | [**SetCreatorSparkCodeRequest**](SetCreatorSparkCodeRequest.md)|  | |

### Return type

ApiResponse<[**SetCreatorSparkCode200Response**](SetCreatorSparkCode200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Saved. |  -  |
| **400** | Invalid input, or the post is not a TikTok post (&#x60;invalid_field_value&#x60;). |  -  |
| **404** | The link is invalid or expired, or the post is not one of the participant&#39;s submissions (&#x60;resource_not_found&#x60;). |  -  |
| **409** | The post was rejected or withdrawn (&#x60;invalid_resource_state&#x60;). |  -  |


## startCreatorConnect

> StartCreatorConnect200Response startCreatorConnect(token, startCreatorConnectRequest)

Start connecting a creator account

Returns the URL that connects one of the creator&#39;s own social accounts, read-only, so their posts can be verified. Only the campaign&#39;s platforms are accepted.  &#x60;authUrl&#x60; opens the welcome screen in the campaign&#39;s brand, then the platform&#39;s sign-in.  The creator comes back to their participant page, or to the connect window&#39;s result screen when &#x60;windowUrl&#x60; is sent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        StartCreatorConnectRequest startCreatorConnectRequest = new StartCreatorConnectRequest(); // StartCreatorConnectRequest | 
        try {
            StartCreatorConnect200Response result = apiInstance.startCreatorConnect(token, startCreatorConnectRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#startCreatorConnect");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **startCreatorConnectRequest** | [**StartCreatorConnectRequest**](StartCreatorConnectRequest.md)|  | |

### Return type

[**StartCreatorConnect200Response**](StartCreatorConnect200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization URL. |  -  |
| **400** | The platform or &#x60;windowUrl&#x60; is not accepted (&#x60;invalid_field_value&#x60;), the campaign allows no more connected accounts, or the campaign has ended (&#x60;invalid_resource_state&#x60;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The creator&#39;s participation was suspended or removed (&#x60;invalid_resource_state&#x60;). |  -  |

## startCreatorConnectWithHttpInfo

> ApiResponse<StartCreatorConnect200Response> startCreatorConnect startCreatorConnectWithHttpInfo(token, startCreatorConnectRequest)

Start connecting a creator account

Returns the URL that connects one of the creator&#39;s own social accounts, read-only, so their posts can be verified. Only the campaign&#39;s platforms are accepted.  &#x60;authUrl&#x60; opens the welcome screen in the campaign&#39;s brand, then the platform&#39;s sign-in.  The creator comes back to their participant page, or to the connect window&#39;s result screen when &#x60;windowUrl&#x60; is sent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        StartCreatorConnectRequest startCreatorConnectRequest = new StartCreatorConnectRequest(); // StartCreatorConnectRequest | 
        try {
            ApiResponse<StartCreatorConnect200Response> response = apiInstance.startCreatorConnectWithHttpInfo(token, startCreatorConnectRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#startCreatorConnect");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **startCreatorConnectRequest** | [**StartCreatorConnectRequest**](StartCreatorConnectRequest.md)|  | |

### Return type

ApiResponse<[**StartCreatorConnect200Response**](StartCreatorConnect200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization URL. |  -  |
| **400** | The platform or &#x60;windowUrl&#x60; is not accepted (&#x60;invalid_field_value&#x60;), the campaign allows no more connected accounts, or the campaign has ended (&#x60;invalid_resource_state&#x60;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The creator&#39;s participation was suspended or removed (&#x60;invalid_resource_state&#x60;). |  -  |


## startCreatorPayouts

> StartCreatorPayouts200Response startCreatorPayouts(token, startCreatorPayoutsRequest)

Start payout onboarding

For a campaign that pays through the Zernio treasury: creates the creator&#39;s payee on first use and returns a Stripe-hosted onboarding link where they enter identity and bank details. &#x60;country&#x60; is required the first time and cannot change afterwards. About 20 attempts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        StartCreatorPayoutsRequest startCreatorPayoutsRequest = new StartCreatorPayoutsRequest(); // StartCreatorPayoutsRequest | 
        try {
            StartCreatorPayouts200Response result = apiInstance.startCreatorPayouts(token, startCreatorPayoutsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#startCreatorPayouts");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **startCreatorPayoutsRequest** | [**StartCreatorPayoutsRequest**](StartCreatorPayoutsRequest.md)|  | |

### Return type

[**StartCreatorPayouts200Response**](StartCreatorPayouts200Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stripe onboarding link. |  -  |
| **400** | &#x60;country&#x60; is missing on the first call (\&quot;Choose the country you live in.\&quot;) or differs from the one already saved (\&quot;Payout country cannot be changed.\&quot;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The campaign team pays the creator directly, so there is nothing to set up (&#x60;invalid_resource_state&#x60;). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## startCreatorPayoutsWithHttpInfo

> ApiResponse<StartCreatorPayouts200Response> startCreatorPayouts startCreatorPayoutsWithHttpInfo(token, startCreatorPayoutsRequest)

Start payout onboarding

For a campaign that pays through the Zernio treasury: creates the creator&#39;s payee on first use and returns a Stripe-hosted onboarding link where they enter identity and bank details. &#x60;country&#x60; is required the first time and cannot change afterwards. About 20 attempts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        StartCreatorPayoutsRequest startCreatorPayoutsRequest = new StartCreatorPayoutsRequest(); // StartCreatorPayoutsRequest | 
        try {
            ApiResponse<StartCreatorPayouts200Response> response = apiInstance.startCreatorPayoutsWithHttpInfo(token, startCreatorPayoutsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#startCreatorPayouts");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **startCreatorPayoutsRequest** | [**StartCreatorPayoutsRequest**](StartCreatorPayoutsRequest.md)|  | |

### Return type

ApiResponse<[**StartCreatorPayouts200Response**](StartCreatorPayouts200Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stripe onboarding link. |  -  |
| **400** | &#x60;country&#x60; is missing on the first call (\&quot;Choose the country you live in.\&quot;) or differs from the one already saved (\&quot;Payout country cannot be changed.\&quot;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The campaign team pays the creator directly, so there is nothing to set up (&#x60;invalid_resource_state&#x60;). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## submitCreatorDraft

> SubmitCreatorDraft201Response submitCreatorDraft(token, submitCreatorDraftRequest)

Submit a draft for review

Sends a draft for the campaign team to review before the creator publishes, on a campaign with &#x60;requireDraftApproval&#x60;, and fires &#x60;campaign_draft.submitted&#x60;. &#x60;mediaUrl&#x60; must be a &#x60;publicUrl&#x60; from &#x60;POST /public/creator-campaigns/{token}/drafts/upload&#x60;.  ### Revisions  - Without &#x60;revisionOf&#x60; the draft starts a new chain at version 1. - With &#x60;revisionOf&#x60; it is the next version of that chain. Only one of the creator&#39;s own versions marked &#x60;revision_requested&#x60; takes a new version, and only once.  About 20 drafts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        SubmitCreatorDraftRequest submitCreatorDraftRequest = new SubmitCreatorDraftRequest(); // SubmitCreatorDraftRequest | 
        try {
            SubmitCreatorDraft201Response result = apiInstance.submitCreatorDraft(token, submitCreatorDraftRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#submitCreatorDraft");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **submitCreatorDraftRequest** | [**SubmitCreatorDraftRequest**](SubmitCreatorDraftRequest.md)|  | |

### Return type

[**SubmitCreatorDraft201Response**](SubmitCreatorDraft201Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Draft submitted. |  -  |
| **400** | An invalid field, or &#x60;mediaUrl&#x60; is not a file uploaded for this campaign (&#x60;invalid_field_value&#x60;, &#x60;param: mediaUrl&#x60;, \&quot;Upload the file from your campaign page first\&quot;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | &#x60;invalid_resource_state&#x60;, and the message says which:  - The campaign does not review drafts or is not accepting posts. - The creator is not active in it (invite not accepted, pending, denied, suspended or removed). - &#x60;revisionOf&#x60; is not one of the creator&#39;s versions or is not &#x60;revision_requested&#x60;, or a newer version of it was already uploaded.  |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## submitCreatorDraftWithHttpInfo

> ApiResponse<SubmitCreatorDraft201Response> submitCreatorDraft submitCreatorDraftWithHttpInfo(token, submitCreatorDraftRequest)

Submit a draft for review

Sends a draft for the campaign team to review before the creator publishes, on a campaign with &#x60;requireDraftApproval&#x60;, and fires &#x60;campaign_draft.submitted&#x60;. &#x60;mediaUrl&#x60; must be a &#x60;publicUrl&#x60; from &#x60;POST /public/creator-campaigns/{token}/drafts/upload&#x60;.  ### Revisions  - Without &#x60;revisionOf&#x60; the draft starts a new chain at version 1. - With &#x60;revisionOf&#x60; it is the next version of that chain. Only one of the creator&#39;s own versions marked &#x60;revision_requested&#x60; takes a new version, and only once.  About 20 drafts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        SubmitCreatorDraftRequest submitCreatorDraftRequest = new SubmitCreatorDraftRequest(); // SubmitCreatorDraftRequest | 
        try {
            ApiResponse<SubmitCreatorDraft201Response> response = apiInstance.submitCreatorDraftWithHttpInfo(token, submitCreatorDraftRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#submitCreatorDraft");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **submitCreatorDraftRequest** | [**SubmitCreatorDraftRequest**](SubmitCreatorDraftRequest.md)|  | |

### Return type

ApiResponse<[**SubmitCreatorDraft201Response**](SubmitCreatorDraft201Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Draft submitted. |  -  |
| **400** | An invalid field, or &#x60;mediaUrl&#x60; is not a file uploaded for this campaign (&#x60;invalid_field_value&#x60;, &#x60;param: mediaUrl&#x60;, \&quot;Upload the file from your campaign page first\&quot;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | &#x60;invalid_resource_state&#x60;, and the message says which:  - The campaign does not review drafts or is not accepting posts. - The creator is not active in it (invite not accepted, pending, denied, suspended or removed). - &#x60;revisionOf&#x60; is not one of the creator&#39;s versions or is not &#x60;revision_requested&#x60;, or a newer version of it was already uploaded.  |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## submitCreatorPost

> SubmitCreatorPost201Response submitCreatorPost(token, submitCreatorPostRequest)

Submit a post

Submits the link to a post the creator published from a connected account. The post opens a tracking window and fires &#x60;campaign_submission.received&#x60; to the operator. About 30 attempts and 10 accepted posts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        SubmitCreatorPostRequest submitCreatorPostRequest = new SubmitCreatorPostRequest(); // SubmitCreatorPostRequest | 
        try {
            SubmitCreatorPost201Response result = apiInstance.submitCreatorPost(token, submitCreatorPostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#submitCreatorPost");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **submitCreatorPostRequest** | [**SubmitCreatorPostRequest**](SubmitCreatorPostRequest.md)|  | |

### Return type

[**SubmitCreatorPost201Response**](SubmitCreatorPost201Response.md)


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Submitted. |  -  |
| **400** | The post cannot be submitted: 400 &#x60;invalid_field_value&#x60;.  - &#x60;param: url&#x60;: the link is not a post of an accepted platform, or the post was published before the campaign started or longer ago than the campaign accepts. - TikTok and X post ids carry their creation time, so a post from before the campaign is refused as such even when no connected account has it. - The post is from an account past the campaign&#39;s &#x60;caps.maxAccountsPerParticipant&#x60; (\&quot;This campaign allows 2 connected accounts.\&quot;). Only the first accounts the creator connected, up to that count, can submit. - &#x60;param: draftId&#x60; (&#x60;missing_required_field&#x60;): the campaign requires draft approval and no &#x60;draftId&#x60; was sent.  |  -  |
| **403** | The creator has not connected an account on that platform yet (&#x60;insufficient_permissions&#x60;, \&quot;Connect your TikTok account first, then submit the post again\&quot;). |  -  |
| **404** | The link is invalid or expired, or no connected account has the post (&#x60;resource_not_found&#x60;, &#x60;param: url&#x60;).  - When the link names its author (TikTok, Instagram, Threads, X) and that is not one of the creator&#39;s accounts, the message names both handles. - Otherwise it says the post was not found yet, for example because it was published moments ago.  |  -  |
| **409** | &#x60;invalid_resource_state&#x60;, and the message says which:  - The invite is not accepted yet, the creator is still pending approval or was denied, or the participation was suspended or removed. - The campaign is not accepting posts (not started, paused or ended). - The post was already submitted, or today&#39;s per-participant post limit is reached. - &#x60;draftId&#x60; is not one of the creator&#39;s approved drafts or already backs another post.  |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## submitCreatorPostWithHttpInfo

> ApiResponse<SubmitCreatorPost201Response> submitCreatorPost submitCreatorPostWithHttpInfo(token, submitCreatorPostRequest)

Submit a post

Submits the link to a post the creator published from a connected account. The post opens a tracking window and fires &#x60;campaign_submission.received&#x60; to the operator. About 30 attempts and 10 accepted posts per participant every 10 minutes. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.models.*;
import dev.zernio.api.CreatorPortalApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");

        CreatorPortalApi apiInstance = new CreatorPortalApi(defaultClient);
        String token = "token_example"; // String | A participant token or an open invite token. A malformed token answers 404 like an unknown one.
        SubmitCreatorPostRequest submitCreatorPostRequest = new SubmitCreatorPostRequest(); // SubmitCreatorPostRequest | 
        try {
            ApiResponse<SubmitCreatorPost201Response> response = apiInstance.submitCreatorPostWithHttpInfo(token, submitCreatorPostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CreatorPortalApi#submitCreatorPost");
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
| **token** | **String**| A participant token or an open invite token. A malformed token answers 404 like an unknown one. | |
| **submitCreatorPostRequest** | [**SubmitCreatorPostRequest**](SubmitCreatorPostRequest.md)|  | |

### Return type

ApiResponse<[**SubmitCreatorPost201Response**](SubmitCreatorPost201Response.md)>


### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Submitted. |  -  |
| **400** | The post cannot be submitted: 400 &#x60;invalid_field_value&#x60;.  - &#x60;param: url&#x60;: the link is not a post of an accepted platform, or the post was published before the campaign started or longer ago than the campaign accepts. - TikTok and X post ids carry their creation time, so a post from before the campaign is refused as such even when no connected account has it. - The post is from an account past the campaign&#39;s &#x60;caps.maxAccountsPerParticipant&#x60; (\&quot;This campaign allows 2 connected accounts.\&quot;). Only the first accounts the creator connected, up to that count, can submit. - &#x60;param: draftId&#x60; (&#x60;missing_required_field&#x60;): the campaign requires draft approval and no &#x60;draftId&#x60; was sent.  |  -  |
| **403** | The creator has not connected an account on that platform yet (&#x60;insufficient_permissions&#x60;, \&quot;Connect your TikTok account first, then submit the post again\&quot;). |  -  |
| **404** | The link is invalid or expired, or no connected account has the post (&#x60;resource_not_found&#x60;, &#x60;param: url&#x60;).  - When the link names its author (TikTok, Instagram, Threads, X) and that is not one of the creator&#39;s accounts, the message names both handles. - Otherwise it says the post was not found yet, for example because it was published moments ago.  |  -  |
| **409** | &#x60;invalid_resource_state&#x60;, and the message says which:  - The invite is not accepted yet, the creator is still pending approval or was denied, or the participation was suspended or removed. - The campaign is not accepting posts (not started, paused or ended). - The post was already submitted, or today&#39;s per-participant post limit is reached. - &#x60;draftId&#x60; is not one of the creator&#39;s approved drafts or already backs another post.  |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

