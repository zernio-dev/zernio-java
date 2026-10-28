# TreasuryApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelPayoutBatch**](TreasuryApi.md#cancelPayoutBatch) | **POST** /v1/payout-batches/{batchId}/cancel | Cancel an unpaid payout batch |
| [**cancelPayoutBatchWithHttpInfo**](TreasuryApi.md#cancelPayoutBatchWithHttpInfo) | **POST** /v1/payout-batches/{batchId}/cancel | Cancel an unpaid payout batch |
| [**createPayeeOnboardingLink**](TreasuryApi.md#createPayeeOnboardingLink) | **POST** /v1/payees/{payeeId}/onboarding-link | Create a payee onboarding link |
| [**createPayeeOnboardingLinkWithHttpInfo**](TreasuryApi.md#createPayeeOnboardingLinkWithHttpInfo) | **POST** /v1/payees/{payeeId}/onboarding-link | Create a payee onboarding link |
| [**createTopup**](TreasuryApi.md#createTopup) | **POST** /v1/balance/top-ups | Create a top-up |
| [**createTopupWithHttpInfo**](TreasuryApi.md#createTopupWithHttpInfo) | **POST** /v1/balance/top-ups | Create a top-up |
| [**createTransfer**](TreasuryApi.md#createTransfer) | **POST** /v1/transfers | Create a transfer |
| [**createTransferWithHttpInfo**](TreasuryApi.md#createTransferWithHttpInfo) | **POST** /v1/transfers | Create a transfer |
| [**getBalance**](TreasuryApi.md#getBalance) | **GET** /v1/balance | Get balance |
| [**getBalanceWithHttpInfo**](TreasuryApi.md#getBalanceWithHttpInfo) | **GET** /v1/balance | Get balance |
| [**getPayoutBatch**](TreasuryApi.md#getPayoutBatch) | **GET** /v1/payout-batches/{batchId} | Get a payout batch |
| [**getPayoutBatchWithHttpInfo**](TreasuryApi.md#getPayoutBatchWithHttpInfo) | **GET** /v1/payout-batches/{batchId} | Get a payout batch |
| [**getTopupReceipt**](TreasuryApi.md#getTopupReceipt) | **GET** /v1/balance/top-ups/{topupId}/receipt | Get a top-up receipt |
| [**getTopupReceiptWithHttpInfo**](TreasuryApi.md#getTopupReceiptWithHttpInfo) | **GET** /v1/balance/top-ups/{topupId}/receipt | Get a top-up receipt |
| [**getTransfer**](TreasuryApi.md#getTransfer) | **GET** /v1/transfers/{transferId} | Get a transfer |
| [**getTransferWithHttpInfo**](TreasuryApi.md#getTransferWithHttpInfo) | **GET** /v1/transfers/{transferId} | Get a transfer |
| [**listPayees**](TreasuryApi.md#listPayees) | **GET** /v1/payees | List payees |
| [**listPayeesWithHttpInfo**](TreasuryApi.md#listPayeesWithHttpInfo) | **GET** /v1/payees | List payees |
| [**listTopups**](TreasuryApi.md#listTopups) | **GET** /v1/balance/top-ups | List top-ups |
| [**listTopupsWithHttpInfo**](TreasuryApi.md#listTopupsWithHttpInfo) | **GET** /v1/balance/top-ups | List top-ups |
| [**listTransfers**](TreasuryApi.md#listTransfers) | **GET** /v1/transfers | List transfers |
| [**listTransfersWithHttpInfo**](TreasuryApi.md#listTransfersWithHttpInfo) | **GET** /v1/transfers | List transfers |



## cancelPayoutBatch

> GetPayoutBatch200Response cancelPayoutBatch(batchId)

Cancel an unpaid payout batch

Ends the Stripe Checkout of a batch that is still &#x60;awaiting_payment&#x60; and makes every amount payable again right away, instead of after Stripe&#39;s 24-hour expiry. A batch that was already paid is returned unchanged. Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String batchId = "batchId_example"; // String | Payout batch ID.
        try {
            GetPayoutBatch200Response result = apiInstance.cancelPayoutBatch(batchId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#cancelPayoutBatch");
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
| **batchId** | **String**| Payout batch ID. | |

### Return type

[**GetPayoutBatch200Response**](GetPayoutBatch200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The payout batch after the cancel. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). Either a restricted API key without the &#x60;money&#x60; resource group, or a profile-scoped API key: money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). A member or viewer is refused too, signed in or through a key they created: only an owner, admin or billing admin moves money.  |  -  |
| **404** | No payout batch with this id in a campaign you can see. |  -  |

## cancelPayoutBatchWithHttpInfo

> ApiResponse<GetPayoutBatch200Response> cancelPayoutBatch cancelPayoutBatchWithHttpInfo(batchId)

Cancel an unpaid payout batch

Ends the Stripe Checkout of a batch that is still &#x60;awaiting_payment&#x60; and makes every amount payable again right away, instead of after Stripe&#39;s 24-hour expiry. A batch that was already paid is returned unchanged. Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String batchId = "batchId_example"; // String | Payout batch ID.
        try {
            ApiResponse<GetPayoutBatch200Response> response = apiInstance.cancelPayoutBatchWithHttpInfo(batchId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#cancelPayoutBatch");
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
| **batchId** | **String**| Payout batch ID. | |

### Return type

ApiResponse<[**GetPayoutBatch200Response**](GetPayoutBatch200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The payout batch after the cancel. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). Either a restricted API key without the &#x60;money&#x60; resource group, or a profile-scoped API key: money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). A member or viewer is refused too, signed in or through a key they created: only an owner, admin or billing admin moves money.  |  -  |
| **404** | No payout batch with this id in a campaign you can see. |  -  |


## createPayeeOnboardingLink

> CreatePayeeOnboardingLink200Response createPayeeOnboardingLink(payeeId)

Create a payee onboarding link

Returns a Stripe-hosted link where the payee completes identity and bank details so they can receive payouts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String payeeId = "payeeId_example"; // String | 
        try {
            CreatePayeeOnboardingLink200Response result = apiInstance.createPayeeOnboardingLink(payeeId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#createPayeeOnboardingLink");
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
| **payeeId** | **String**|  | |

### Return type

[**CreatePayeeOnboardingLink200Response**](CreatePayeeOnboardingLink200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Onboarding link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Resource not found |  -  |

## createPayeeOnboardingLinkWithHttpInfo

> ApiResponse<CreatePayeeOnboardingLink200Response> createPayeeOnboardingLink createPayeeOnboardingLinkWithHttpInfo(payeeId)

Create a payee onboarding link

Returns a Stripe-hosted link where the payee completes identity and bank details so they can receive payouts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String payeeId = "payeeId_example"; // String | 
        try {
            ApiResponse<CreatePayeeOnboardingLink200Response> response = apiInstance.createPayeeOnboardingLinkWithHttpInfo(payeeId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#createPayeeOnboardingLink");
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
| **payeeId** | **String**|  | |

### Return type

ApiResponse<[**CreatePayeeOnboardingLink200Response**](CreatePayeeOnboardingLink200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Onboarding link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Resource not found |  -  |


## createTopup

> CreateTopup201Response createTopup(createTopupRequest, idempotencyKey)

Create a top-up

Starts a Stripe Checkout session to fund your balance by card. Card top-ups pay Stripe&#39;s processing fee and become available after 7 days. Bank transfers are not available yet; &#x60;method: bank_transfer&#x60; returns 400. Needs an owner, admin or billing admin, signed in or through a full-access key they created.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        CreateTopupRequest createTopupRequest = new CreateTopupRequest(); // CreateTopupRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.
        try {
            CreateTopup201Response result = apiInstance.createTopup(createTopupRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#createTopup");
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
| **createTopupRequest** | [**CreateTopupRequest**](CreateTopupRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. | [optional] |

### Return type

[**CreateTopup201Response**](CreateTopup201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Checkout session created |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). Either a restricted API key without the &#x60;money&#x60; resource group, or a profile-scoped API key: money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). A member or viewer is refused too, signed in or through a key they created: only an owner, admin or billing admin moves money.  |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createTopupWithHttpInfo

> ApiResponse<CreateTopup201Response> createTopup createTopupWithHttpInfo(createTopupRequest, idempotencyKey)

Create a top-up

Starts a Stripe Checkout session to fund your balance by card. Card top-ups pay Stripe&#39;s processing fee and become available after 7 days. Bank transfers are not available yet; &#x60;method: bank_transfer&#x60; returns 400. Needs an owner, admin or billing admin, signed in or through a full-access key they created.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        CreateTopupRequest createTopupRequest = new CreateTopupRequest(); // CreateTopupRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.
        try {
            ApiResponse<CreateTopup201Response> response = apiInstance.createTopupWithHttpInfo(createTopupRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#createTopup");
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
| **createTopupRequest** | [**CreateTopupRequest**](CreateTopupRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. | [optional] |

### Return type

ApiResponse<[**CreateTopup201Response**](CreateTopup201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Checkout session created |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). Either a restricted API key without the &#x60;money&#x60; resource group, or a profile-scoped API key: money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). A member or viewer is refused too, signed in or through a key they created: only an owner, admin or billing admin moves money.  |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## createTransfer

> TreasuryTransfer createTransfer(createTransferRequest, idempotencyKey)

Create a transfer

Moves money from your balance to a payee. The payee receives the full &#x60;amountCents&#x60;; Zernio&#39;s fee (4%, 50 cent minimum) is added on top, so your balance is debited &#x60;totalCents&#x60; &#x3D; &#x60;amountCents&#x60; + &#x60;feeCents&#x60;. Returns 402 when the balance does not cover the amount plus the fee, or when it is negative after a dispute or refund of a card top-up (\&quot;Your balance is negative after a dispute or refund of a card top-up. Add funds to cover it before sending transfers.\&quot;), and 409 when the payee has not finished onboarding or the Idempotency-Key is still processing. Needs an owner, admin or billing admin, signed in or through a full-access key they created: a profile-scoped key answers 403. A same-key retry never makes the transfer twice within Stripe&#39;s 24-hour idempotency window and answers 409 while another request is still waiting on Stripe for it; a transfer Stripe has not confirmed after 24 hours answers 409 until the daily reconciliation marks it paid (Stripe made it) or failed (it did not). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        CreateTransferRequest createTransferRequest = new CreateTransferRequest(); // CreateTransferRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.
        try {
            TreasuryTransfer result = apiInstance.createTransfer(createTransferRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#createTransfer");
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
| **createTransferRequest** | [**CreateTransferRequest**](CreateTransferRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. | [optional] |

### Return type

[**TreasuryTransfer**](TreasuryTransfer.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transfer created |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). Either a restricted API key without the &#x60;money&#x60; resource group, or a profile-scoped API key: money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). A member or viewer is refused too, signed in or through a key they created: only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |
| **409** | Payee has not finished payout onboarding, the Idempotency-Key is still processing, another request is waiting on Stripe for this transfer, or Stripe has not confirmed it within 24 hours |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createTransferWithHttpInfo

> ApiResponse<TreasuryTransfer> createTransfer createTransferWithHttpInfo(createTransferRequest, idempotencyKey)

Create a transfer

Moves money from your balance to a payee. The payee receives the full &#x60;amountCents&#x60;; Zernio&#39;s fee (4%, 50 cent minimum) is added on top, so your balance is debited &#x60;totalCents&#x60; &#x3D; &#x60;amountCents&#x60; + &#x60;feeCents&#x60;. Returns 402 when the balance does not cover the amount plus the fee, or when it is negative after a dispute or refund of a card top-up (\&quot;Your balance is negative after a dispute or refund of a card top-up. Add funds to cover it before sending transfers.\&quot;), and 409 when the payee has not finished onboarding or the Idempotency-Key is still processing. Needs an owner, admin or billing admin, signed in or through a full-access key they created: a profile-scoped key answers 403. A same-key retry never makes the transfer twice within Stripe&#39;s 24-hour idempotency window and answers 409 while another request is still waiting on Stripe for it; a transfer Stripe has not confirmed after 24 hours answers 409 until the daily reconciliation marks it paid (Stripe made it) or failed (it did not). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        CreateTransferRequest createTransferRequest = new CreateTransferRequest(); // CreateTransferRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.
        try {
            ApiResponse<TreasuryTransfer> response = apiInstance.createTransferWithHttpInfo(createTransferRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#createTransfer");
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
| **createTransferRequest** | [**CreateTransferRequest**](CreateTransferRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. A request cut off mid-handler (for example by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. | [optional] |

### Return type

ApiResponse<[**TreasuryTransfer**](TreasuryTransfer.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transfer created |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). Either a restricted API key without the &#x60;money&#x60; resource group, or a profile-scoped API key: money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). A member or viewer is refused too, signed in or through a key they created: only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |
| **409** | Payee has not finished payout onboarding, the Idempotency-Key is still processing, another request is waiting on Stripe for this transfer, or Stripe has not confirmed it within 24 hours |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## getBalance

> GetBalance200Response getBalance()

Get balance

Returns the balance you can transfer, card top-ups still on hold, top-ups still waiting for payment, and your latest top-ups. Card top-ups become available after 7 days. A transfer debits its amount plus the fee added on top; the payee receives the full amount. A card dispute or refund on a top-up is debited from the available balance and can make it negative; transfers are refused until it is positive again. A profile-scoped key answers 403, since the balance belongs to the whole team.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        try {
            GetBalance200Response result = apiInstance.getBalance();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getBalance");
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

[**GetBalance200Response**](GetBalance200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Balance in cents |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## getBalanceWithHttpInfo

> ApiResponse<GetBalance200Response> getBalance getBalanceWithHttpInfo()

Get balance

Returns the balance you can transfer, card top-ups still on hold, top-ups still waiting for payment, and your latest top-ups. Card top-ups become available after 7 days. A transfer debits its amount plus the fee added on top; the payee receives the full amount. A card dispute or refund on a top-up is debited from the available balance and can make it negative; transfers are refused until it is positive again. A profile-scoped key answers 403, since the balance belongs to the whole team.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        try {
            ApiResponse<GetBalance200Response> response = apiInstance.getBalanceWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getBalance");
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

ApiResponse<[**GetBalance200Response**](GetBalance200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Balance in cents |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## getPayoutBatch

> GetPayoutBatch200Response getPayoutBatch(batchId)

Get a payout batch

One payout batch with its status and each creator&#39;s item. Poll it after the card payment to see when every creator is paid.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String batchId = "batchId_example"; // String | Payout batch ID.
        try {
            GetPayoutBatch200Response result = apiInstance.getPayoutBatch(batchId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getPayoutBatch");
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
| **batchId** | **String**| Payout batch ID. | |

### Return type

[**GetPayoutBatch200Response**](GetPayoutBatch200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The payout batch. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No payout batch with this id in a campaign you can see. |  -  |

## getPayoutBatchWithHttpInfo

> ApiResponse<GetPayoutBatch200Response> getPayoutBatch getPayoutBatchWithHttpInfo(batchId)

Get a payout batch

One payout batch with its status and each creator&#39;s item. Poll it after the card payment to see when every creator is paid.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String batchId = "batchId_example"; // String | Payout batch ID.
        try {
            ApiResponse<GetPayoutBatch200Response> response = apiInstance.getPayoutBatchWithHttpInfo(batchId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getPayoutBatch");
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
| **batchId** | **String**| Payout batch ID. | |

### Return type

ApiResponse<[**GetPayoutBatch200Response**](GetPayoutBatch200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The payout batch. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No payout batch with this id in a campaign you can see. |  -  |


## getTopupReceipt

> GetTopupReceipt200Response getTopupReceipt(topupId)

Get a top-up receipt

The receipt for a paid top-up or creator payout payment (&#x60;purpose: payout_batch&#x60;). &#x60;format: pdf&#x60; is the Stripe invoice PDF; &#x60;format: page&#x60; is Stripe&#39;s receipt page, for payments that have no invoice. The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String topupId = "topupId_example"; // String | 
        try {
            GetTopupReceipt200Response result = apiInstance.getTopupReceipt(topupId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTopupReceipt");
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
| **topupId** | **String**|  | |

### Return type

[**GetTopupReceipt200Response**](GetTopupReceipt200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Receipt link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Resource not found |  -  |

## getTopupReceiptWithHttpInfo

> ApiResponse<GetTopupReceipt200Response> getTopupReceipt getTopupReceiptWithHttpInfo(topupId)

Get a top-up receipt

The receipt for a paid top-up or creator payout payment (&#x60;purpose: payout_batch&#x60;). &#x60;format: pdf&#x60; is the Stripe invoice PDF; &#x60;format: page&#x60; is Stripe&#39;s receipt page, for payments that have no invoice. The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String topupId = "topupId_example"; // String | 
        try {
            ApiResponse<GetTopupReceipt200Response> response = apiInstance.getTopupReceiptWithHttpInfo(topupId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTopupReceipt");
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
| **topupId** | **String**|  | |

### Return type

ApiResponse<[**GetTopupReceipt200Response**](GetTopupReceipt200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Receipt link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Resource not found |  -  |


## getTransfer

> TreasuryTransfer getTransfer(transferId)

Get a transfer

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String transferId = "transferId_example"; // String | 
        try {
            TreasuryTransfer result = apiInstance.getTransfer(transferId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTransfer");
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
| **transferId** | **String**|  | |

### Return type

[**TreasuryTransfer**](TreasuryTransfer.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transfer |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Resource not found |  -  |

## getTransferWithHttpInfo

> ApiResponse<TreasuryTransfer> getTransfer getTransferWithHttpInfo(transferId)

Get a transfer

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        String transferId = "transferId_example"; // String | 
        try {
            ApiResponse<TreasuryTransfer> response = apiInstance.getTransferWithHttpInfo(transferId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTransfer");
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
| **transferId** | **String**|  | |

### Return type

ApiResponse<[**TreasuryTransfer**](TreasuryTransfer.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transfer |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |
| **404** | Resource not found |  -  |


## listPayees

> ListPayees200Response listPayees()

List payees

Payees you can transfer to. A payee can receive transfers once &#x60;payoutsEnabled&#x60; is true. A profile-scoped key answers 403.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        try {
            ListPayees200Response result = apiInstance.listPayees();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#listPayees");
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

[**ListPayees200Response**](ListPayees200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payees |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## listPayeesWithHttpInfo

> ApiResponse<ListPayees200Response> listPayees listPayeesWithHttpInfo()

List payees

Payees you can transfer to. A payee can receive transfers once &#x60;payoutsEnabled&#x60; is true. A profile-scoped key answers 403.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        try {
            ApiResponse<ListPayees200Response> response = apiInstance.listPayeesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#listPayees");
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

ApiResponse<[**ListPayees200Response**](ListPayees200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Payees |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## listTopups

> ListTopups200Response listTopups(limit, skip)

List top-ups

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListTopups200Response result = apiInstance.listTopups(limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#listTopups");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListTopups200Response**](ListTopups200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top-ups, newest first |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## listTopupsWithHttpInfo

> ApiResponse<ListTopups200Response> listTopups listTopupsWithHttpInfo(limit, skip)

List top-ups

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListTopups200Response> response = apiInstance.listTopupsWithHttpInfo(limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#listTopups");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListTopups200Response**](ListTopups200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top-ups, newest first |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |


## listTransfers

> ListTransfers200Response listTransfers(limit, skip)

List transfers

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListTransfers200Response result = apiInstance.listTransfers(limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#listTransfers");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListTransfers200Response**](ListTransfers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transfers, newest first |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

## listTransfersWithHttpInfo

> ApiResponse<ListTransfers200Response> listTransfers listTransfersWithHttpInfo(limit, skip)

List transfers

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.TreasuryApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        TreasuryApi apiInstance = new TreasuryApi(defaultClient);
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListTransfers200Response> response = apiInstance.listTransfersWithHttpInfo(limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#listTransfers");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListTransfers200Response**](ListTransfers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transfers, newest first |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required. The authenticated account hit a billing gate before the connection could proceed. Three reasons:    - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts     than the free tier allows. Add a payment method on the     dashboard to continue (the user will be billed per     additional connected account).    - &#x60;twitter_passthrough&#x60;: connecting an X account     requires a card on file from day one because X API calls     incur real per-call pass-through costs. Applies to the 1st     X account, not only the 3rd+.    - &#x60;enterprise_required&#x60;: the team is on an enterprise     contract with a negotiated connected-account cap and has     reached it. Self-service teams have NO connected-account cap (the     $1/account rate continues at any scale), so this reason can     only fire for teams whose contract sets an explicit limit.     &#x60;dashboard_url&#x60; deep-links to the enterprise contact page     rather than the billing tab. The end-user already has a     card on file; this gate is about contract terms, not card     collection.    - &#x60;card_verification_required&#x60;: the card on file was flagged     at add time (prepaid, or issued in a different country than     the billing address) and a one-time verification charge of     &#x60;details.verification_amount_cents&#x60; (USD) is pending. The     charge is credited to the team&#39;s usage balance, not a fee.     &#x60;dashboard_url&#x60; opens the billing page on the verification     step; the request succeeds once it is paid.  SDK consumers should switch on &#x60;reason&#x60; to render the right prompt. For &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60; and &#x60;card_verification_required&#x60;, redirect the end-user to &#x60;dashboard_url&#x60;: it opens the add-payment-method drawer on the Zernio billing page, and the request succeeds once the card is on file (or verified). For &#x60;enterprise_required&#x60;, redirect to &#x60;dashboard_url&#x60; (the enterprise contact form) to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases. (1) The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key: fix it by creating a key with the group enabled in the dashboard API keys tab and revoking the old one. (2) The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), which is never grantable to restricted keys; the error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; and the fix is a full-access key or the dashboard, never a new restricted key. (3) On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold, so a restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events). |  -  |

