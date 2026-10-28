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
| [**recoverCreatorPortalLinks**](CreatorPortalApi.md#recoverCreatorPortalLinks) | **POST** /public/creator-campaigns/recover-link | Email a creator their campaign links |
| [**recoverCreatorPortalLinksWithHttpInfo**](CreatorPortalApi.md#recoverCreatorPortalLinksWithHttpInfo) | **POST** /public/creator-campaigns/recover-link | Email a creator their campaign links |
| [**startCreatorConnect**](CreatorPortalApi.md#startCreatorConnect) | **POST** /public/creator-campaigns/{token}/connect | Start connecting a creator account |
| [**startCreatorConnectWithHttpInfo**](CreatorPortalApi.md#startCreatorConnectWithHttpInfo) | **POST** /public/creator-campaigns/{token}/connect | Start connecting a creator account |
| [**startCreatorPayouts**](CreatorPortalApi.md#startCreatorPayouts) | **POST** /public/creator-campaigns/{token}/payouts | Start payout onboarding |
| [**startCreatorPayoutsWithHttpInfo**](CreatorPortalApi.md#startCreatorPayoutsWithHttpInfo) | **POST** /public/creator-campaigns/{token}/payouts | Start payout onboarding |
| [**submitCreatorPost**](CreatorPortalApi.md#submitCreatorPost) | **POST** /public/creator-campaigns/{token}/submissions | Submit a post |
| [**submitCreatorPostWithHttpInfo**](CreatorPortalApi.md#submitCreatorPostWithHttpInfo) | **POST** /public/creator-campaigns/{token}/submissions | Submit a post |



## createCreatorPayoutLogin

> StartCreatorPayouts200Response createCreatorPayoutLogin(token)

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
            StartCreatorPayouts200Response result = apiInstance.createCreatorPayoutLogin(token);
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

[**StartCreatorPayouts200Response**](StartCreatorPayouts200Response.md)


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

> ApiResponse<StartCreatorPayouts200Response> createCreatorPayoutLogin createCreatorPayoutLoginWithHttpInfo(token)

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
            ApiResponse<StartCreatorPayouts200Response> response = apiInstance.createCreatorPayoutLoginWithHttpInfo(token);
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

ApiResponse<[**StartCreatorPayouts200Response**](StartCreatorPayouts200Response.md)>


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

A PDF statement of one paid payout to this creator: who paid, the campaign, the date, the amount and the Stripe transfer id. It is a statement of a payment, not a tax invoice. Only for a paid payout of this participant; anything else answers 404. About 60 downloads per participant every 10 minutes. 

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

A PDF statement of one paid payout to this creator: who paid, the campaign, the date, the amount and the Stripe transfer id. It is a statement of a payment, not a tax invoice. Only for a paid payout of this participant; anything else answers 404. About 60 downloads per participant every 10 minutes. 

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

What a creator sees behind a campaign link, with no API key. &#x60;token&#x60; is either an open invite token (from &#x60;POST /v1/creator-campaigns/{campaignId}/invite-link&#x60;), which answers &#x60;kind: invite&#x60; with the campaign only, or a participant token (from an invite or a join), which answers &#x60;kind: participant&#x60; with the creator&#39;s connected accounts, latest 100 submissions, earnings and payout setup. Reading a participant page also re-checks the creator&#39;s connected accounts. Never cached. 

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

What a creator sees behind a campaign link, with no API key. &#x60;token&#x60; is either an open invite token (from &#x60;POST /v1/creator-campaigns/{campaignId}/invite-link&#x60;), which answers &#x60;kind: invite&#x60; with the campaign only, or a participant token (from an invite or a join), which answers &#x60;kind: participant&#x60; with the creator&#39;s connected accounts, latest 100 submissions, earnings and payout setup. Reading a participant page also re-checks the creator&#39;s connected accounts. Never cached. 

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

Accepts a participant invite, or joins through an open invite link. With a participant token the body is ignored and the invite is accepted. With an open invite token a new participant is created from &#x60;displayName&#x60; (required) and &#x60;email&#x60; (optional), and a fresh participant token comes back: keep it, it is the creator&#39;s only key to their page. Open-link joins are limited to about 20 per IP address and 60 per link every 10 minutes. 

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
| **403** | The campaign is not taking new creators (&#x60;feature_not_available&#x60;, \&quot;This campaign is not taking new creators right now. Ask the campaign team.\&quot;), for example because it reached its participant cap. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

## joinCreatorCampaignWithHttpInfo

> ApiResponse<JoinCreatorCampaign201Response> joinCreatorCampaign joinCreatorCampaignWithHttpInfo(token, joinCreatorCampaignRequest)

Join a campaign

Accepts a participant invite, or joins through an open invite link. With a participant token the body is ignored and the invite is accepted. With an open invite token a new participant is created from &#x60;displayName&#x60; (required) and &#x60;email&#x60; (optional), and a fresh participant token comes back: keep it, it is the creator&#39;s only key to their page. Open-link joins are limited to about 20 per IP address and 60 per link every 10 minutes. 

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
| **403** | The campaign is not taking new creators (&#x60;feature_not_available&#x60;, \&quot;This campaign is not taking new creators right now. Ask the campaign team.\&quot;), for example because it reached its participant cap. |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |


## recoverCreatorPortalLinks

> RecoverCreatorPortalLinks202Response recoverCreatorPortalLinks(recoverCreatorPortalLinksRequest)

Email a creator their campaign links

For a creator who lost their link. Emails every personal participant link held by &#x60;email&#x60; in one message, optionally only the one for &#x60;campaignId&#x60;. Removed participants and draft campaigns are left out. Always answers 202 with the same body, so the answer never tells whether the address has links. Limited to 5 requests per hour per email address and 5 per hour per IP address. 

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

For a creator who lost their link. Emails every personal participant link held by &#x60;email&#x60; in one message, optionally only the one for &#x60;campaignId&#x60;. Removed participants and draft campaigns are left out. Always answers 202 with the same body, so the answer never tells whether the address has links. Limited to 5 requests per hour per email address and 5 per hour per IP address. 

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


## startCreatorConnect

> StartCreatorConnect200Response startCreatorConnect(token, startCreatorConnectRequest)

Start connecting a creator account

Returns the authorization URL that connects one of the creator&#39;s own social accounts, read-only, so their posts can be verified. Send the creator&#39;s browser to &#x60;authUrl&#x60;; they come back to their participant page. Only the campaign&#39;s platforms are accepted. 

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
| **400** | The platform is not part of the campaign (&#x60;invalid_field_value&#x60;), the campaign allows no more connected accounts (\&quot;This campaign allows N connected accounts.\&quot;), or the campaign has ended (&#x60;invalid_resource_state&#x60;). |  -  |
| **404** | The token is malformed, unknown or expired. Every case answers the same, so a link can never be probed. |  -  |
| **409** | The creator&#39;s participation was suspended or removed (&#x60;invalid_resource_state&#x60;). |  -  |

## startCreatorConnectWithHttpInfo

> ApiResponse<StartCreatorConnect200Response> startCreatorConnect startCreatorConnectWithHttpInfo(token, startCreatorConnectRequest)

Start connecting a creator account

Returns the authorization URL that connects one of the creator&#39;s own social accounts, read-only, so their posts can be verified. Send the creator&#39;s browser to &#x60;authUrl&#x60;; they come back to their participant page. Only the campaign&#39;s platforms are accepted. 

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
| **400** | The platform is not part of the campaign (&#x60;invalid_field_value&#x60;), the campaign allows no more connected accounts (\&quot;This campaign allows N connected accounts.\&quot;), or the campaign has ended (&#x60;invalid_resource_state&#x60;). |  -  |
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
| **400** | The link is not a post of an accepted platform, or the post was published before the campaign started or longer ago than the campaign accepts (&#x60;invalid_field_value&#x60;, &#x60;param: url&#x60;). Also 400 &#x60;invalid_field_value&#x60; when the post is from an account past the campaign&#39;s &#x60;caps.maxAccountsPerParticipant&#x60; (\&quot;This campaign allows 2 connected accounts.\&quot;): only the first accounts the creator connected, up to that count, can submit. |  -  |
| **403** | The creator has not connected an account on that platform yet (&#x60;insufficient_permissions&#x60;, \&quot;Connect your TikTok account first, then submit the post again\&quot;). |  -  |
| **404** | The link is invalid or expired, or the post is not from an account the creator connected (&#x60;resource_not_found&#x60;). |  -  |
| **409** | The invite is not accepted yet, the campaign is not accepting posts (not started, paused or ended), the post was already submitted, today&#39;s per-participant post limit is reached, or the participation was suspended or removed (&#x60;invalid_resource_state&#x60;; the message says which). |  -  |
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
| **400** | The link is not a post of an accepted platform, or the post was published before the campaign started or longer ago than the campaign accepts (&#x60;invalid_field_value&#x60;, &#x60;param: url&#x60;). Also 400 &#x60;invalid_field_value&#x60; when the post is from an account past the campaign&#39;s &#x60;caps.maxAccountsPerParticipant&#x60; (\&quot;This campaign allows 2 connected accounts.\&quot;): only the first accounts the creator connected, up to that count, can submit. |  -  |
| **403** | The creator has not connected an account on that platform yet (&#x60;insufficient_permissions&#x60;, \&quot;Connect your TikTok account first, then submit the post again\&quot;). |  -  |
| **404** | The link is invalid or expired, or the post is not from an account the creator connected (&#x60;resource_not_found&#x60;). |  -  |
| **409** | The invite is not accepted yet, the campaign is not accepting posts (not started, paused or ended), the post was already submitted, today&#39;s per-participant post limit is reached, or the participation was suspended or removed (&#x60;invalid_resource_state&#x60;; the message says which). |  -  |
| **429** | Too many attempts from this link or IP address (&#x60;rate_limited&#x60;). Wait a few minutes and try again. |  -  |

