# TreasuryApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelPayoutBatch**](TreasuryApi.md#cancelPayoutBatch) | **POST** /v1/payout-batches/{batchId}/cancel | Cancel an unpaid payout batch |
| [**cancelPayoutBatchWithHttpInfo**](TreasuryApi.md#cancelPayoutBatchWithHttpInfo) | **POST** /v1/payout-batches/{batchId}/cancel | Cancel an unpaid payout batch |
| [**cancelTopup**](TreasuryApi.md#cancelTopup) | **POST** /v1/balance/top-ups/{topupId}/cancel | Cancel a top-up |
| [**cancelTopupWithHttpInfo**](TreasuryApi.md#cancelTopupWithHttpInfo) | **POST** /v1/balance/top-ups/{topupId}/cancel | Cancel a top-up |
| [**confirmPayoutBatch**](TreasuryApi.md#confirmPayoutBatch) | **POST** /v1/payout-batches/{batchId}/confirm | Confirm a payout batch payment |
| [**confirmPayoutBatchWithHttpInfo**](TreasuryApi.md#confirmPayoutBatchWithHttpInfo) | **POST** /v1/payout-batches/{batchId}/confirm | Confirm a payout batch payment |
| [**confirmTopup**](TreasuryApi.md#confirmTopup) | **POST** /v1/balance/top-ups/{topupId}/confirm | Confirm a top-up |
| [**confirmTopupWithHttpInfo**](TreasuryApi.md#confirmTopupWithHttpInfo) | **POST** /v1/balance/top-ups/{topupId}/confirm | Confirm a top-up |
| [**createPayeeOnboardingLink**](TreasuryApi.md#createPayeeOnboardingLink) | **POST** /v1/payees/{payeeId}/onboarding-link | Create a payee onboarding link |
| [**createPayeeOnboardingLinkWithHttpInfo**](TreasuryApi.md#createPayeeOnboardingLinkWithHttpInfo) | **POST** /v1/payees/{payeeId}/onboarding-link | Create a payee onboarding link |
| [**createTopup**](TreasuryApi.md#createTopup) | **POST** /v1/balance/top-ups | Create a top-up |
| [**createTopupWithHttpInfo**](TreasuryApi.md#createTopupWithHttpInfo) | **POST** /v1/balance/top-ups | Create a top-up |
| [**createTransfer**](TreasuryApi.md#createTransfer) | **POST** /v1/transfers | Create a transfer (removed) |
| [**createTransferWithHttpInfo**](TreasuryApi.md#createTransferWithHttpInfo) | **POST** /v1/transfers | Create a transfer (removed) |
| [**getAutoRecharge**](TreasuryApi.md#getAutoRecharge) | **GET** /v1/balance/auto-recharge | Get auto-recharge settings |
| [**getAutoRechargeWithHttpInfo**](TreasuryApi.md#getAutoRechargeWithHttpInfo) | **GET** /v1/balance/auto-recharge | Get auto-recharge settings |
| [**getBalance**](TreasuryApi.md#getBalance) | **GET** /v1/balance | Get balance |
| [**getBalanceWithHttpInfo**](TreasuryApi.md#getBalanceWithHttpInfo) | **GET** /v1/balance | Get balance |
| [**getPayoutBatch**](TreasuryApi.md#getPayoutBatch) | **GET** /v1/payout-batches/{batchId} | Get a payout batch |
| [**getPayoutBatchWithHttpInfo**](TreasuryApi.md#getPayoutBatchWithHttpInfo) | **GET** /v1/payout-batches/{batchId} | Get a payout batch |
| [**getTopupInvoice**](TreasuryApi.md#getTopupInvoice) | **GET** /v1/balance/top-ups/{topupId}/invoice | Get a top-up invoice |
| [**getTopupInvoiceWithHttpInfo**](TreasuryApi.md#getTopupInvoiceWithHttpInfo) | **GET** /v1/balance/top-ups/{topupId}/invoice | Get a top-up invoice |
| [**getTopupReceipt**](TreasuryApi.md#getTopupReceipt) | **GET** /v1/balance/top-ups/{topupId}/receipt | Get a top-up receipt |
| [**getTopupReceiptWithHttpInfo**](TreasuryApi.md#getTopupReceiptWithHttpInfo) | **GET** /v1/balance/top-ups/{topupId}/receipt | Get a top-up receipt |
| [**getTopupStatement**](TreasuryApi.md#getTopupStatement) | **GET** /v1/balance/top-ups/{topupId}/statement | Get a top-up invoice (alias) |
| [**getTopupStatementWithHttpInfo**](TreasuryApi.md#getTopupStatementWithHttpInfo) | **GET** /v1/balance/top-ups/{topupId}/statement | Get a top-up invoice (alias) |
| [**getTransfer**](TreasuryApi.md#getTransfer) | **GET** /v1/transfers/{transferId} | Get a transfer |
| [**getTransferWithHttpInfo**](TreasuryApi.md#getTransferWithHttpInfo) | **GET** /v1/transfers/{transferId} | Get a transfer |
| [**listPayees**](TreasuryApi.md#listPayees) | **GET** /v1/payees | List payees |
| [**listPayeesWithHttpInfo**](TreasuryApi.md#listPayeesWithHttpInfo) | **GET** /v1/payees | List payees |
| [**listTopups**](TreasuryApi.md#listTopups) | **GET** /v1/balance/top-ups | List top-ups |
| [**listTopupsWithHttpInfo**](TreasuryApi.md#listTopupsWithHttpInfo) | **GET** /v1/balance/top-ups | List top-ups |
| [**listTransfers**](TreasuryApi.md#listTransfers) | **GET** /v1/transfers | List transfers |
| [**listTransfersWithHttpInfo**](TreasuryApi.md#listTransfersWithHttpInfo) | **GET** /v1/transfers | List transfers |
| [**previewTopup**](TreasuryApi.md#previewTopup) | **POST** /v1/balance/top-ups/preview | Preview a top-up&#39;s tax |
| [**previewTopupWithHttpInfo**](TreasuryApi.md#previewTopupWithHttpInfo) | **POST** /v1/balance/top-ups/preview | Preview a top-up&#39;s tax |
| [**updateAutoRecharge**](TreasuryApi.md#updateAutoRecharge) | **PATCH** /v1/balance/auto-recharge | Update auto-recharge settings |
| [**updateAutoRechargeWithHttpInfo**](TreasuryApi.md#updateAutoRechargeWithHttpInfo) | **PATCH** /v1/balance/auto-recharge | Update auto-recharge settings |



## cancelPayoutBatch

> GetPayoutBatch200Response cancelPayoutBatch(batchId)

Cancel an unpaid payout batch

Ends the payment of a batch that is still &#x60;awaiting_payment&#x60; (3D Secure left unfinished) and makes every amount payable again right away.  - When Stripe reports the charge already made, the batch is paid out instead. - A batch that was already paid is returned unchanged.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | No payout batch with this id in a campaign you can see. |  -  |

## cancelPayoutBatchWithHttpInfo

> ApiResponse<GetPayoutBatch200Response> cancelPayoutBatch cancelPayoutBatchWithHttpInfo(batchId)

Cancel an unpaid payout batch

Ends the payment of a batch that is still &#x60;awaiting_payment&#x60; (3D Secure left unfinished) and makes every amount payable again right away.  - When Stripe reports the charge already made, the batch is paid out instead. - A batch that was already paid is returned unchanged.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | No payout batch with this id in a campaign you can see. |  -  |


## cancelTopup

> TreasuryTopup cancelTopup(topupId)

Cancel a top-up

Ends the payment of a pending top-up (3D Secure left unfinished), so it stops counting toward &#x60;pendingTopupCents&#x60;, and returns it as &#x60;expired&#x60;.  - When Stripe reports it already paid, the top-up is credited and comes back &#x60;succeeded&#x60;. - A top-up that is no longer pending comes back unchanged. - A creator payout payment (&#x60;purpose: payout_batch&#x60;) answers 409; cancel it from its campaign.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
            TreasuryTopup result = apiInstance.cancelTopup(topupId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#cancelTopup");
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

[**TreasuryTopup**](TreasuryTopup.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The top-up after cancelling |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |
| **409** | The top-up is a creator payout payment (code &#x60;invalid_resource_state&#x60;); cancel it from its campaign. |  -  |

## cancelTopupWithHttpInfo

> ApiResponse<TreasuryTopup> cancelTopup cancelTopupWithHttpInfo(topupId)

Cancel a top-up

Ends the payment of a pending top-up (3D Secure left unfinished), so it stops counting toward &#x60;pendingTopupCents&#x60;, and returns it as &#x60;expired&#x60;.  - When Stripe reports it already paid, the top-up is credited and comes back &#x60;succeeded&#x60;. - A top-up that is no longer pending comes back unchanged. - A creator payout payment (&#x60;purpose: payout_batch&#x60;) answers 409; cancel it from its campaign.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
            ApiResponse<TreasuryTopup> response = apiInstance.cancelTopupWithHttpInfo(topupId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#cancelTopup");
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

ApiResponse<[**TreasuryTopup**](TreasuryTopup.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The top-up after cancelling |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |
| **409** | The top-up is a creator payout payment (code &#x60;invalid_resource_state&#x60;); cancel it from its campaign. |  -  |


## confirmPayoutBatch

> GetPayoutBatch200Response confirmPayoutBatch(batchId)

Confirm a payout batch payment

Call after 3D Secure. Reads the batch&#39;s payment from Stripe, then:  - charge succeeded: pays the creators (&#x60;paying&#x60;, then &#x60;paid&#x60;). - bank refused: ends the batch (&#x60;failed&#x60;) and makes every amount payable again. - still settling: leaves it &#x60;awaiting_payment&#x60;.  Safe to repeat. Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
            GetPayoutBatch200Response result = apiInstance.confirmPayoutBatch(batchId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#confirmPayoutBatch");
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
| **200** | The payout batch after confirming. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |

## confirmPayoutBatchWithHttpInfo

> ApiResponse<GetPayoutBatch200Response> confirmPayoutBatch confirmPayoutBatchWithHttpInfo(batchId)

Confirm a payout batch payment

Call after 3D Secure. Reads the batch&#39;s payment from Stripe, then:  - charge succeeded: pays the creators (&#x60;paying&#x60;, then &#x60;paid&#x60;). - bank refused: ends the batch (&#x60;failed&#x60;) and makes every amount payable again. - still settling: leaves it &#x60;awaiting_payment&#x60;.  Safe to repeat. Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
            ApiResponse<GetPayoutBatch200Response> response = apiInstance.confirmPayoutBatchWithHttpInfo(batchId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#confirmPayoutBatch");
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
| **200** | The payout batch after confirming. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |


## confirmTopup

> TreasuryTopup confirmTopup(topupId)

Confirm a top-up

Call after 3D Secure. Reads the payment from Stripe, then:  - &#x60;succeeded&#x60;: paid, the top-up is credited. - &#x60;failed&#x60;: the bank refused it. - &#x60;pending&#x60;: Stripe is still settling the charge.  Safe to repeat. Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
            TreasuryTopup result = apiInstance.confirmTopup(topupId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#confirmTopup");
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

[**TreasuryTopup**](TreasuryTopup.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The top-up after confirming |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |

## confirmTopupWithHttpInfo

> ApiResponse<TreasuryTopup> confirmTopup confirmTopupWithHttpInfo(topupId)

Confirm a top-up

Call after 3D Secure. Reads the payment from Stripe, then:  - &#x60;succeeded&#x60;: paid, the top-up is credited. - &#x60;failed&#x60;: the bank refused it. - &#x60;pending&#x60;: Stripe is still settling the charge.  Safe to repeat. Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
            ApiResponse<TreasuryTopup> response = apiInstance.confirmTopupWithHttpInfo(topupId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#confirmTopup");
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

ApiResponse<[**TreasuryTopup**](TreasuryTopup.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The top-up after confirming |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |


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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |


## createTopup

> CreateTopup201Response createTopup(createTopupRequest, idempotencyKey)

Create a top-up

Charges the billing owner&#39;s saved card (the default one, or &#x60;paymentMethodId&#x60;) &#x60;amountCents&#x60; plus tax, while the payer is present, and credits your balance &#x60;amountCents&#x60;. There is no card fee.  Tax is added on top of the amount (&#x60;taxCents&#x60;, &#x60;totalCents&#x60;): VAT at 21% in Spain, at the customer&#39;s country rate for EU consumers; an EU business whose VAT id VIES confirms is reverse charged (no VAT, &#x60;reverseCharge: true&#x60;); outside the EU there is none.  The invoice also states the VAT in euros at the ECB rate of its date. Usage paid from the balance carries no further VAT. Get the figures before paying with &#x60;POST /v1/balance/top-ups/preview&#x60;.  Each top-up has an invoice, with VAT where it applies (&#x60;GET /v1/balance/top-ups/{topupId}/invoice&#x60;), and a card receipt (&#x60;GET /v1/balance/top-ups/{topupId}/receipt&#x60;).  - &#x60;status: succeeded&#x60;: the card was charged. &#x60;amountCents&#x60; is credited to &#x60;availableCents&#x60; within seconds. Transfers to payees can use it from 7 days after the charge. - &#x60;status: requires_action&#x60;: the bank asked for 3D Secure. Complete it with Stripe.js &#x60;handleNextAction({ clientSecret })&#x60;, then call &#x60;POST /v1/balance/top-ups/{topupId}/confirm&#x60;. One left unconfirmed is cancelled after 30 minutes.  ### Errors  - 402 &#x60;payment_required&#x60;: no saved card. - 402 &#x60;card_declined&#x60;: the bank&#39;s reason. - 400: &#x60;method: bank_transfer&#x60; (bank transfers are not available yet). - 400 &#x60;invalid_billing_address&#x60;: the billing address gives no tax location. Add it in Billing, then retry. - 429 &#x60;payment_attempts_limited&#x60;: five card payments were declined in 24 hours. Nothing reaches the bank until &#x60;Retry-After&#x60; runs out.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **201** | The card was charged, or the bank asked for 3D Secure |  -  |
| **400** | Invalid request |  -  |
| **402** | No saved card (code &#x60;payment_required&#x60;), or the bank declined the charge (code &#x60;card_declined&#x60;, the message is the reason), or a billing gate. |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **429** | Code &#x60;payment_attempts_limited&#x60;: five card payments of the billing owner (top-ups, auto top-ups, payout batches paid by card, cards that failed to save) were declined within 24 hours, so new card payments are refused without reaching the bank until 24 hours after the fifth decline. Nothing was charged.  The message is \&quot;Too many declined payments. Try again tomorrow or contact support.\&quot; &#x60;Retry-After&#x60; and &#x60;details.retryAt&#x60; say when card payments are tried again.  |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createTopupWithHttpInfo

> ApiResponse<CreateTopup201Response> createTopup createTopupWithHttpInfo(createTopupRequest, idempotencyKey)

Create a top-up

Charges the billing owner&#39;s saved card (the default one, or &#x60;paymentMethodId&#x60;) &#x60;amountCents&#x60; plus tax, while the payer is present, and credits your balance &#x60;amountCents&#x60;. There is no card fee.  Tax is added on top of the amount (&#x60;taxCents&#x60;, &#x60;totalCents&#x60;): VAT at 21% in Spain, at the customer&#39;s country rate for EU consumers; an EU business whose VAT id VIES confirms is reverse charged (no VAT, &#x60;reverseCharge: true&#x60;); outside the EU there is none.  The invoice also states the VAT in euros at the ECB rate of its date. Usage paid from the balance carries no further VAT. Get the figures before paying with &#x60;POST /v1/balance/top-ups/preview&#x60;.  Each top-up has an invoice, with VAT where it applies (&#x60;GET /v1/balance/top-ups/{topupId}/invoice&#x60;), and a card receipt (&#x60;GET /v1/balance/top-ups/{topupId}/receipt&#x60;).  - &#x60;status: succeeded&#x60;: the card was charged. &#x60;amountCents&#x60; is credited to &#x60;availableCents&#x60; within seconds. Transfers to payees can use it from 7 days after the charge. - &#x60;status: requires_action&#x60;: the bank asked for 3D Secure. Complete it with Stripe.js &#x60;handleNextAction({ clientSecret })&#x60;, then call &#x60;POST /v1/balance/top-ups/{topupId}/confirm&#x60;. One left unconfirmed is cancelled after 30 minutes.  ### Errors  - 402 &#x60;payment_required&#x60;: no saved card. - 402 &#x60;card_declined&#x60;: the bank&#39;s reason. - 400: &#x60;method: bank_transfer&#x60; (bank transfers are not available yet). - 400 &#x60;invalid_billing_address&#x60;: the billing address gives no tax location. Add it in Billing, then retry. - 429 &#x60;payment_attempts_limited&#x60;: five card payments were declined in 24 hours. Nothing reaches the bank until &#x60;Retry-After&#x60; runs out.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

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
| **201** | The card was charged, or the bank asked for 3D Secure |  -  |
| **400** | Invalid request |  -  |
| **402** | No saved card (code &#x60;payment_required&#x60;), or the bank declined the charge (code &#x60;card_declined&#x60;, the message is the reason), or a billing gate. |  -  |
| **403** | Refused (&#x60;insufficient_permissions&#x60;). One of:  - A restricted API key without the &#x60;money&#x60; resource group. - A profile-scoped API key. Money leaves the whole team&#39;s balance, so moving it needs a full-access key or a signed-in session (\&quot;Moving money needs a full-access key or a signed-in session.\&quot;). - A member or viewer, signed in or through a key they created. Only an owner, admin or billing admin moves money.  |  -  |
| **404** | Resource not found |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **429** | Code &#x60;payment_attempts_limited&#x60;: five card payments of the billing owner (top-ups, auto top-ups, payout batches paid by card, cards that failed to save) were declined within 24 hours, so new card payments are refused without reaching the bank until 24 hours after the fifth decline. Nothing was charged.  The message is \&quot;Too many declined payments. Try again tomorrow or contact support.\&quot; &#x60;Retry-After&#x60; and &#x60;details.retryAt&#x60; say when card payments are tried again.  |  * Retry-After - Seconds until card payments are tried again. <br>  |
| **422** | Idempotency-Key reused with a different request |  -  |


## createTransfer

> void createTransfer(createTransferRequest, idempotencyKey)

Create a transfer (removed)

Removed on 2026-11-06: the balance no longer pays creators. Every call answers 410.  Pay creators with one card payment per payout batch: &#x60;POST /v1/creator-campaigns/{campaignId}/payout-batches&#x60;. &#x60;GET /v1/transfers&#x60; still lists the transfers payout batches made. 

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            apiInstance.createTransfer(createTransferRequest, idempotencyKey);
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **410** | Transfers from the balance are no longer available (code &#x60;invalid_resource_state&#x60;). Pay creators with &#x60;POST /v1/creator-campaigns/{campaignId}/payout-batches&#x60;. |  -  |

## createTransferWithHttpInfo

> ApiResponse<Void> createTransfer createTransferWithHttpInfo(createTransferRequest, idempotencyKey)

Create a transfer (removed)

Removed on 2026-11-06: the balance no longer pays creators. Every call answers 410.  Pay creators with one card payment per payout batch: &#x60;POST /v1/creator-campaigns/{campaignId}/payout-batches&#x60;. &#x60;GET /v1/transfers&#x60; still lists the transfers payout batches made. 

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
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<Void> response = apiInstance.createTransferWithHttpInfo(createTransferRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **410** | Transfers from the balance are no longer available (code &#x60;invalid_resource_state&#x60;). Pay creators with &#x60;POST /v1/creator-campaigns/{campaignId}/payout-batches&#x60;. |  -  |


## getAutoRecharge

> AutoRecharge getAutoRecharge()

Get auto-recharge settings

Your balance&#39;s auto-recharge rule: when the balance drops below &#x60;belowCents&#x60;, the billing owner&#39;s saved card is charged back up to &#x60;toCents&#x60;, tax added on top as for any top-up.  Account credit you held when you moved to the balance pays a recharge first, without a card charge or invoice (see &#x60;recentCreditRecharges&#x60; on &#x60;GET /v1/balance&#x60;). The card is charged only once that credit is used up, and only while the balance is still below &#x60;belowCents&#x60;.  The first read gives the default rule, sized from your last 30 days of pay-per-use: below about a week of spend (at least $5), back up by about two more weeks (at least $20).  - 409 &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance.  A profile-scoped key answers 403. 

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
            AutoRecharge result = apiInstance.getAutoRecharge();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getAutoRecharge");
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

[**AutoRecharge**](AutoRecharge.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Auto-recharge settings |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **409** | Code &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance. |  -  |

## getAutoRechargeWithHttpInfo

> ApiResponse<AutoRecharge> getAutoRecharge getAutoRechargeWithHttpInfo()

Get auto-recharge settings

Your balance&#39;s auto-recharge rule: when the balance drops below &#x60;belowCents&#x60;, the billing owner&#39;s saved card is charged back up to &#x60;toCents&#x60;, tax added on top as for any top-up.  Account credit you held when you moved to the balance pays a recharge first, without a card charge or invoice (see &#x60;recentCreditRecharges&#x60; on &#x60;GET /v1/balance&#x60;). The card is charged only once that credit is used up, and only while the balance is still below &#x60;belowCents&#x60;.  The first read gives the default rule, sized from your last 30 days of pay-per-use: below about a week of spend (at least $5), back up by about two more weeks (at least $20).  - 409 &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance.  A profile-scoped key answers 403. 

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
            ApiResponse<AutoRecharge> response = apiInstance.getAutoRechargeWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getAutoRecharge");
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

ApiResponse<[**AutoRecharge**](AutoRecharge.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Auto-recharge settings |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **409** | Code &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance. |  -  |


## getBalance

> GetBalance200Response getBalance()

Get balance

Returns your team&#39;s balance:  - the balance pay-per-use draws on - top-ups still waiting for payment - your latest top-ups and payout batch payments  A card top-up is in &#x60;availableCents&#x60; as soon as it is paid. The balance never pays creators: payouts are charged to your card per payout batch.  A card dispute or refund is debited from the available balance and can make it negative. New payout batches are refused until it is positive again.  A profile-scoped key answers 403, since the balance belongs to the whole team. 

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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

## getBalanceWithHttpInfo

> ApiResponse<GetBalance200Response> getBalance getBalanceWithHttpInfo()

Get balance

Returns your team&#39;s balance:  - the balance pay-per-use draws on - top-ups still waiting for payment - your latest top-ups and payout batch payments  A card top-up is in &#x60;availableCents&#x60; as soon as it is paid. The balance never pays creators: payouts are charged to your card per payout batch.  A card dispute or refund is debited from the available balance and can make it negative. New payout batches are refused until it is positive again.  A profile-scoped key answers 403, since the balance belongs to the whole team. 

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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |


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


## getTopupInvoice

> GetTopupInvoice200Response getTopupInvoice(topupId)

Get a top-up invoice

The invoice for a paid balance top-up: the PDF of the Stripe invoice it was paid through.  It shows the amount added to your balance and the tax charged on top: VAT where it applies, or a reverse charge note for an EU business with a valid VAT id. Usage paid from the balance carries no further VAT.  - &#x60;format: pdf&#x60; is the invoice PDF; &#x60;format: page&#x60; is its Stripe-hosted page when the PDF is not ready. - 404 before the top-up is paid, and for a payment with no invoice (top-ups before 2026-11-05, creator payout payments). Its card receipt is at getTopupReceipt.  The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403. 

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
            GetTopupInvoice200Response result = apiInstance.getTopupInvoice(topupId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTopupInvoice");
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

[**GetTopupInvoice200Response**](GetTopupInvoice200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |

## getTopupInvoiceWithHttpInfo

> ApiResponse<GetTopupInvoice200Response> getTopupInvoice getTopupInvoiceWithHttpInfo(topupId)

Get a top-up invoice

The invoice for a paid balance top-up: the PDF of the Stripe invoice it was paid through.  It shows the amount added to your balance and the tax charged on top: VAT where it applies, or a reverse charge note for an EU business with a valid VAT id. Usage paid from the balance carries no further VAT.  - &#x60;format: pdf&#x60; is the invoice PDF; &#x60;format: page&#x60; is its Stripe-hosted page when the PDF is not ready. - 404 before the top-up is paid, and for a payment with no invoice (top-ups before 2026-11-05, creator payout payments). Its card receipt is at getTopupReceipt.  The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403. 

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
            ApiResponse<GetTopupInvoice200Response> response = apiInstance.getTopupInvoiceWithHttpInfo(topupId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTopupInvoice");
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

ApiResponse<[**GetTopupInvoice200Response**](GetTopupInvoice200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |


## getTopupReceipt

> File getTopupReceipt(topupId, download)

Get a top-up receipt

The receipt for a paid top-up or creator payout payment (&#x60;purpose: payout_batch&#x60;). &#x60;url&#x60; is the payment&#39;s invoice PDF when it has one (&#x60;format: pdf&#x60;), else Stripe&#39;s card receipt page (&#x60;format: page&#x60;); &#x60;invoiceUrl&#x60; and &#x60;receiptUrl&#x60; give each on its own.  The invoice alone is at getTopupInvoice. The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403.

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
        Boolean download = true; // Boolean | true answers the card receipt itself as a PDF file (application/pdf, as an attachment) instead of the JSON links.
        try {
            File result = apiInstance.getTopupReceipt(topupId, download);
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
| **download** | **Boolean**| true answers the card receipt itself as a PDF file (application/pdf, as an attachment) instead of the JSON links. | [optional] |

### Return type

[**File**](File.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Receipt link, or the receipt PDF with download&#x3D;true |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |

## getTopupReceiptWithHttpInfo

> ApiResponse<File> getTopupReceipt getTopupReceiptWithHttpInfo(topupId, download)

Get a top-up receipt

The receipt for a paid top-up or creator payout payment (&#x60;purpose: payout_batch&#x60;). &#x60;url&#x60; is the payment&#39;s invoice PDF when it has one (&#x60;format: pdf&#x60;), else Stripe&#39;s card receipt page (&#x60;format: page&#x60;); &#x60;invoiceUrl&#x60; and &#x60;receiptUrl&#x60; give each on its own.  The invoice alone is at getTopupInvoice. The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403.

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
        Boolean download = true; // Boolean | true answers the card receipt itself as a PDF file (application/pdf, as an attachment) instead of the JSON links.
        try {
            ApiResponse<File> response = apiInstance.getTopupReceiptWithHttpInfo(topupId, download);
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
| **download** | **Boolean**| true answers the card receipt itself as a PDF file (application/pdf, as an attachment) instead of the JSON links. | [optional] |

### Return type

ApiResponse<[**File**](File.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Receipt link, or the receipt PDF with download&#x3D;true |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |


## getTopupStatement

> GetTopupInvoice200Response getTopupStatement(topupId)

Get a top-up invoice (alias)

Alias of getTopupInvoice, kept for clients written against its first name.  The invoice for a paid balance top-up: the PDF of the Stripe invoice it was paid through.  It shows the amount added to your balance and the tax charged on top: VAT where it applies, or a reverse charge note for an EU business with a valid VAT id. Usage paid from the balance carries no further VAT.  - &#x60;format: pdf&#x60; is the invoice PDF; &#x60;format: page&#x60; is its Stripe-hosted page when the PDF is not ready. - 404 before the top-up is paid, and for a payment with no invoice (top-ups before 2026-11-05, creator payout payments). Its card receipt is at getTopupReceipt.  The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403. 

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
            GetTopupInvoice200Response result = apiInstance.getTopupStatement(topupId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTopupStatement");
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

[**GetTopupInvoice200Response**](GetTopupInvoice200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **404** | Resource not found |  -  |

## getTopupStatementWithHttpInfo

> ApiResponse<GetTopupInvoice200Response> getTopupStatement getTopupStatementWithHttpInfo(topupId)

Get a top-up invoice (alias)

Alias of getTopupInvoice, kept for clients written against its first name.  The invoice for a paid balance top-up: the PDF of the Stripe invoice it was paid through.  It shows the amount added to your balance and the tax charged on top: VAT where it applies, or a reverse charge note for an EU business with a valid VAT id. Usage paid from the balance carries no further VAT.  - &#x60;format: pdf&#x60; is the invoice PDF; &#x60;format: page&#x60; is its Stripe-hosted page when the PDF is not ready. - 404 before the top-up is paid, and for a payment with no invoice (top-ups before 2026-11-05, creator payout payments). Its card receipt is at getTopupReceipt.  The link is short-lived, so fetch it when you need it. A profile-scoped key answers 403. 

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
            ApiResponse<GetTopupInvoice200Response> response = apiInstance.getTopupStatementWithHttpInfo(topupId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#getTopupStatement");
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

ApiResponse<[**GetTopupInvoice200Response**](GetTopupInvoice200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice link |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |


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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |


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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

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
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |


## previewTopup

> PreviewTopup200Response previewTopup(previewTopupRequest)

Preview a top-up&#39;s tax

The tax a top-up of &#x60;amountCents&#x60; will carry and the total the card is charged, calculated by Stripe Tax from the billing owner&#39;s billing address and tax ids, as the top-up&#39;s invoice will be. Charges nothing.  - 400 &#x60;invalid_billing_address&#x60;: the billing address gives no tax location, so a top-up would be refused too.  Needs a full-access key or a signed-in session; a profile-scoped key answers 403. 

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
        PreviewTopupRequest previewTopupRequest = new PreviewTopupRequest(); // PreviewTopupRequest | 
        try {
            PreviewTopup200Response result = apiInstance.previewTopup(previewTopupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#previewTopup");
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
| **previewTopupRequest** | [**PreviewTopupRequest**](PreviewTopupRequest.md)|  | |

### Return type

[**PreviewTopup200Response**](PreviewTopup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tax and total for the amount |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |

## previewTopupWithHttpInfo

> ApiResponse<PreviewTopup200Response> previewTopup previewTopupWithHttpInfo(previewTopupRequest)

Preview a top-up&#39;s tax

The tax a top-up of &#x60;amountCents&#x60; will carry and the total the card is charged, calculated by Stripe Tax from the billing owner&#39;s billing address and tax ids, as the top-up&#39;s invoice will be. Charges nothing.  - 400 &#x60;invalid_billing_address&#x60;: the billing address gives no tax location, so a top-up would be refused too.  Needs a full-access key or a signed-in session; a profile-scoped key answers 403. 

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
        PreviewTopupRequest previewTopupRequest = new PreviewTopupRequest(); // PreviewTopupRequest | 
        try {
            ApiResponse<PreviewTopup200Response> response = apiInstance.previewTopupWithHttpInfo(previewTopupRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#previewTopup");
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
| **previewTopupRequest** | [**PreviewTopupRequest**](PreviewTopupRequest.md)|  | |

### Return type

ApiResponse<[**PreviewTopup200Response**](PreviewTopup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tax and total for the amount |  -  |
| **400** | Invalid request |  -  |
| **402** | Payment method or enterprise contract required: the authenticated account hit a billing gate before the connection could proceed. Switch on &#x60;reason&#x60; to render the right prompt:  - &#x60;free_tier_exceeded&#x60;: the team has connected more accounts than the free tier allows. Add a payment method to continue (billed per additional connected account). - &#x60;twitter_passthrough&#x60;: connecting an X account requires a card on file from day one, because X API calls incur real per-call pass-through costs. Applies to the 1st X account, not only the 3rd+. - &#x60;enterprise_required&#x60;: the team&#39;s enterprise contract sets a connected-account cap and it has been reached. Self-service teams have NO cap (the $1/account rate continues at any scale). The user already has a card on file; this gate is about contract terms. - &#x60;card_verification_required&#x60;: the card on file was flagged at add time (prepaid, or issued in a different country than the billing address). A one-time verification charge of &#x60;details.verification_amount_cents&#x60; (USD) is pending; it is credited to the team&#39;s usage balance, not a fee.  **What to do:** redirect the end-user to &#x60;dashboard_url&#x60;.  - &#x60;free_tier_exceeded&#x60;, &#x60;twitter_passthrough&#x60;, &#x60;card_verification_required&#x60;: it opens the Zernio billing page (the add-payment-method drawer, or the verification step). The request succeeds once the card is on file (or verified, or paid). - &#x60;enterprise_required&#x60;: it opens the enterprise contact form (not the billing tab), to adjust the contract&#39;s limit.  |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |


## updateAutoRecharge

> AutoRecharge updateAutoRecharge(updateAutoRechargeRequest)

Update auto-recharge settings

Changes the auto-recharge rule. Omitted fields keep their value.  A declined recharge is retried 1 hour, 1 day and 3 days later, with an email each time. After the last retry fails, auto-recharge switches off (&#x60;disabledReason: payment_failed&#x60;) until the card is updated. A top-up you make yourself resets the retries.  A bank asking for 3D Secure counts as a decline: the charge happens while you are away, so the email asks you to top up in Billing.  A pay-per-use request that finds the balance at $0 runs the recharge first (with the rule on, a saved card and no retry pending) and goes through when the charge lands, so a new balance at $0 is charged on first use.  When this month&#39;s auto-recharges plus the next one would pass &#x60;monthlyLimitCents&#x60;, the card is not charged and you get one email that month. At $0, pay-per-use then answers 402 &#x60;usage_limit_reached&#x60;.  - 400: a field is out of range, or &#x60;toCents&#x60; is not more than $5 above &#x60;belowCents&#x60;. - 409 &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
        UpdateAutoRechargeRequest updateAutoRechargeRequest = new UpdateAutoRechargeRequest(); // UpdateAutoRechargeRequest | 
        try {
            AutoRecharge result = apiInstance.updateAutoRecharge(updateAutoRechargeRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#updateAutoRecharge");
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
| **updateAutoRechargeRequest** | [**UpdateAutoRechargeRequest**](UpdateAutoRechargeRequest.md)|  | |

### Return type

[**AutoRecharge**](AutoRecharge.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **409** | Code &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance. |  -  |

## updateAutoRechargeWithHttpInfo

> ApiResponse<AutoRecharge> updateAutoRecharge updateAutoRechargeWithHttpInfo(updateAutoRechargeRequest)

Update auto-recharge settings

Changes the auto-recharge rule. Omitted fields keep their value.  A declined recharge is retried 1 hour, 1 day and 3 days later, with an email each time. After the last retry fails, auto-recharge switches off (&#x60;disabledReason: payment_failed&#x60;) until the card is updated. A top-up you make yourself resets the retries.  A bank asking for 3D Secure counts as a decline: the charge happens while you are away, so the email asks you to top up in Billing.  A pay-per-use request that finds the balance at $0 runs the recharge first (with the rule on, a saved card and no retry pending) and goes through when the charge lands, so a new balance at $0 is charged on first use.  When this month&#39;s auto-recharges plus the next one would pass &#x60;monthlyLimitCents&#x60;, the card is not charged and you get one email that month. At $0, pay-per-use then answers 402 &#x60;usage_limit_reached&#x60;.  - 400: a field is out of range, or &#x60;toCents&#x60; is not more than $5 above &#x60;belowCents&#x60;. - 409 &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance.  Needs an owner, admin or billing admin, signed in or through a full-access key they created. 

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
        UpdateAutoRechargeRequest updateAutoRechargeRequest = new UpdateAutoRechargeRequest(); // UpdateAutoRechargeRequest | 
        try {
            ApiResponse<AutoRecharge> response = apiInstance.updateAutoRechargeWithHttpInfo(updateAutoRechargeRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling TreasuryApi#updateAutoRecharge");
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
| **updateAutoRechargeRequest** | [**UpdateAutoRechargeRequest**](UpdateAutoRechargeRequest.md)|  | |

### Return type

ApiResponse<[**AutoRecharge**](AutoRecharge.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **403** | The API key is a restricted key (zrk_ prefix) and may not perform this operation. Three cases:  1. The operation&#39;s resource group (see the operation&#39;s x-resource-group) is disabled on the key. Fix: create a key with the group enabled in the dashboard API keys tab and revoke the old one. 2. The operation is admin-plane (x-resource-group admin-plane: API keys, invites, connected apps, member identity), never grantable to restricted keys. The error reads \&quot;Restricted API keys cannot manage API keys, invites, or member identity.\&quot; Fix: a full-access key or the dashboard, never a new restricted key. 3. On webhook subscription writes, delivery-log reads and replays, a named event maps to a resource group the key does not hold. A restricted key can never create or edit a subscription broader than itself (a no-messages key cannot subscribe to, test-fire, redeliver or read logs for message.* events).  |  -  |
| **409** | Code &#x60;balance_billing_required&#x60;: the account is not on the prepaid balance. |  -  |

