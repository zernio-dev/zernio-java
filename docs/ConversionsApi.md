# ConversionsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addConversionAssociations**](ConversionsApi.md#addConversionAssociations) | **POST** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Associate campaigns |
| [**addConversionAssociationsWithHttpInfo**](ConversionsApi.md#addConversionAssociationsWithHttpInfo) | **POST** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Associate campaigns |
| [**adjustConversions**](ConversionsApi.md#adjustConversions) | **POST** /v1/ads/conversions/adjustments | Adjust uploaded conversions |
| [**adjustConversionsWithHttpInfo**](ConversionsApi.md#adjustConversionsWithHttpInfo) | **POST** /v1/ads/conversions/adjustments | Adjust uploaded conversions |
| [**createConversionDestination**](ConversionsApi.md#createConversionDestination) | **POST** /v1/accounts/{accountId}/conversion-destinations | Create a conversion destination |
| [**createConversionDestinationWithHttpInfo**](ConversionsApi.md#createConversionDestinationWithHttpInfo) | **POST** /v1/accounts/{accountId}/conversion-destinations | Create a conversion destination |
| [**deleteConversionDestination**](ConversionsApi.md#deleteConversionDestination) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Delete a conversion destination |
| [**deleteConversionDestinationWithHttpInfo**](ConversionsApi.md#deleteConversionDestinationWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Delete a conversion destination |
| [**getConversionDestination**](ConversionsApi.md#getConversionDestination) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Get a conversion destination |
| [**getConversionDestinationWithHttpInfo**](ConversionsApi.md#getConversionDestinationWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Get a conversion destination |
| [**getConversionMetrics**](ConversionsApi.md#getConversionMetrics) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/metrics | Get attribution metrics |
| [**getConversionMetricsWithHttpInfo**](ConversionsApi.md#getConversionMetricsWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/metrics | Get attribution metrics |
| [**getConversionsQuality**](ConversionsApi.md#getConversionsQuality) | **GET** /v1/ads/conversions/quality | Get Event Match Quality |
| [**getConversionsQualityWithHttpInfo**](ConversionsApi.md#getConversionsQualityWithHttpInfo) | **GET** /v1/ads/conversions/quality | Get Event Match Quality |
| [**listConversionAssociations**](ConversionsApi.md#listConversionAssociations) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | List associated campaigns |
| [**listConversionAssociationsWithHttpInfo**](ConversionsApi.md#listConversionAssociationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | List associated campaigns |
| [**listConversionDestinations**](ConversionsApi.md#listConversionDestinations) | **GET** /v1/accounts/{accountId}/conversion-destinations | List conversion destinations |
| [**listConversionDestinationsWithHttpInfo**](ConversionsApi.md#listConversionDestinationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations | List conversion destinations |
| [**removeConversionAssociations**](ConversionsApi.md#removeConversionAssociations) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Remove associated campaigns |
| [**removeConversionAssociationsWithHttpInfo**](ConversionsApi.md#removeConversionAssociationsWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Remove associated campaigns |
| [**sendConversions**](ConversionsApi.md#sendConversions) | **POST** /v1/ads/conversions | Send conversion events |
| [**sendConversionsWithHttpInfo**](ConversionsApi.md#sendConversionsWithHttpInfo) | **POST** /v1/ads/conversions | Send conversion events |
| [**updateConversionDestination**](ConversionsApi.md#updateConversionDestination) | **PATCH** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Update a conversion destination |
| [**updateConversionDestinationWithHttpInfo**](ConversionsApi.md#updateConversionDestinationWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Update a conversion destination |



## addConversionAssociations

> AddConversionAssociations200Response addConversionAssociations(accountId, destinationId, addConversionAssociationsRequest)

Associate campaigns

Associate one or more campaigns with this conversion rule. Returns a per-campaign success/failure result so callers can retry only the rows that failed (e.g. wrong campaign type for the rule&#39;s objective). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        AddConversionAssociationsRequest addConversionAssociationsRequest = new AddConversionAssociationsRequest(); // AddConversionAssociationsRequest | 
        try {
            AddConversionAssociations200Response result = apiInstance.addConversionAssociations(accountId, destinationId, addConversionAssociationsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#addConversionAssociations");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **addConversionAssociationsRequest** | [**AddConversionAssociationsRequest**](AddConversionAssociationsRequest.md)|  | |

### Return type

[**AddConversionAssociations200Response**](AddConversionAssociations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details. Inputs that fail local URN validation are bucketed into &#x60;failed&#x60; without ever hitting LinkedIn.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## addConversionAssociationsWithHttpInfo

> ApiResponse<AddConversionAssociations200Response> addConversionAssociations addConversionAssociationsWithHttpInfo(accountId, destinationId, addConversionAssociationsRequest)

Associate campaigns

Associate one or more campaigns with this conversion rule. Returns a per-campaign success/failure result so callers can retry only the rows that failed (e.g. wrong campaign type for the rule&#39;s objective). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        AddConversionAssociationsRequest addConversionAssociationsRequest = new AddConversionAssociationsRequest(); // AddConversionAssociationsRequest | 
        try {
            ApiResponse<AddConversionAssociations200Response> response = apiInstance.addConversionAssociationsWithHttpInfo(accountId, destinationId, addConversionAssociationsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#addConversionAssociations");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **addConversionAssociationsRequest** | [**AddConversionAssociationsRequest**](AddConversionAssociationsRequest.md)|  | |

### Return type

ApiResponse<[**AddConversionAssociations200Response**](AddConversionAssociations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details. Inputs that fail local URN validation are bucketed into &#x60;failed&#x60; without ever hitting LinkedIn.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## adjustConversions

> AdjustConversions200Response adjustConversions(adjustConversionsRequest)

Adjust uploaded conversions

Adjust conversions that were previously uploaded via &#x60;POST /v1/ads/conversions&#x60; — retract them, restate their value, or enhance them with first-party data. Requires the Ads add-on.  **Google Ads only.** Google handles adjustments through the classic Google Ads API (&#x60;ConversionAdjustmentUploadService&#x60;); the Data Manager &#x60;ingestEvents&#x60; path used for sending conversions is ingest-only. Meta and LinkedIn have no equivalent, so this endpoint returns &#x60;405&#x60; for those platforms.  Adjustment types:  - &#x60;RETRACTION&#x60; — remove the conversion entirely (refund, chargeback, cancelled order, churn). - &#x60;RESTATEMENT&#x60; — change the conversion&#39;s value (upgrade / downgrade / partial refund). Send the corrected **total** value in &#x60;restatementValue&#x60; (not a delta). - &#x60;ENHANCEMENT&#x60; — attach first-party identifiers (hashed email / phone) to an existing conversion (enhanced conversions applied after the fact).  Identifying the original conversion (per adjustment):  - &#x60;orderId&#x60; — the transaction ID you sent as &#x60;eventId&#x60; on the original conversion. Recommended, and **required** for &#x60;ENHANCEMENT&#x60;. - or &#x60;gclid&#x60; + &#x60;conversionTime&#x60; — the click ID and the original conversion&#39;s time (unix seconds). Not available for &#x60;ENHANCEMENT&#x60;.  &#x60;destinationId&#x60; is the conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; (same value you send to &#x60;POST /v1/ads/conversions&#x60;). PII in &#x60;user&#x60; is hashed with SHA-256 server-side (Gmail-specific normalization included). Send plaintext.  Times are unix seconds; we convert to Google&#39;s required &#x60;yyyy-MM-dd HH:mm:ss+00:00&#x60; format. Up to 2000 adjustments per request; partial failure is supported (inspect &#x60;adjustmentsFailed&#x60; / &#x60;failures[]&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        AdjustConversionsRequest adjustConversionsRequest = new AdjustConversionsRequest(); // AdjustConversionsRequest | 
        try {
            AdjustConversions200Response result = apiInstance.adjustConversions(adjustConversionsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#adjustConversions");
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
| **adjustConversionsRequest** | [**AdjustConversionsRequest**](AdjustConversionsRequest.md)|  | |

### Return type

[**AdjustConversions200Response**](AdjustConversions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Adjustments processed. Inspect &#x60;adjustmentsFailed&#x60; and &#x60;failures[]&#x60; for partial failure (Google reports per-row errors via partial failure).  |  -  |
| **400** | Invalid body, or a malformed adjustment (missing key, missing restatementValue for RESTATEMENT, missing identifiers for ENHANCEMENT). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Conversion adjustments are only available for Google Ads (the account&#39;s platform is not &#x60;googleads&#x60;). |  -  |

## adjustConversionsWithHttpInfo

> ApiResponse<AdjustConversions200Response> adjustConversions adjustConversionsWithHttpInfo(adjustConversionsRequest)

Adjust uploaded conversions

Adjust conversions that were previously uploaded via &#x60;POST /v1/ads/conversions&#x60; — retract them, restate their value, or enhance them with first-party data. Requires the Ads add-on.  **Google Ads only.** Google handles adjustments through the classic Google Ads API (&#x60;ConversionAdjustmentUploadService&#x60;); the Data Manager &#x60;ingestEvents&#x60; path used for sending conversions is ingest-only. Meta and LinkedIn have no equivalent, so this endpoint returns &#x60;405&#x60; for those platforms.  Adjustment types:  - &#x60;RETRACTION&#x60; — remove the conversion entirely (refund, chargeback, cancelled order, churn). - &#x60;RESTATEMENT&#x60; — change the conversion&#39;s value (upgrade / downgrade / partial refund). Send the corrected **total** value in &#x60;restatementValue&#x60; (not a delta). - &#x60;ENHANCEMENT&#x60; — attach first-party identifiers (hashed email / phone) to an existing conversion (enhanced conversions applied after the fact).  Identifying the original conversion (per adjustment):  - &#x60;orderId&#x60; — the transaction ID you sent as &#x60;eventId&#x60; on the original conversion. Recommended, and **required** for &#x60;ENHANCEMENT&#x60;. - or &#x60;gclid&#x60; + &#x60;conversionTime&#x60; — the click ID and the original conversion&#39;s time (unix seconds). Not available for &#x60;ENHANCEMENT&#x60;.  &#x60;destinationId&#x60; is the conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; (same value you send to &#x60;POST /v1/ads/conversions&#x60;). PII in &#x60;user&#x60; is hashed with SHA-256 server-side (Gmail-specific normalization included). Send plaintext.  Times are unix seconds; we convert to Google&#39;s required &#x60;yyyy-MM-dd HH:mm:ss+00:00&#x60; format. Up to 2000 adjustments per request; partial failure is supported (inspect &#x60;adjustmentsFailed&#x60; / &#x60;failures[]&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        AdjustConversionsRequest adjustConversionsRequest = new AdjustConversionsRequest(); // AdjustConversionsRequest | 
        try {
            ApiResponse<AdjustConversions200Response> response = apiInstance.adjustConversionsWithHttpInfo(adjustConversionsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#adjustConversions");
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
| **adjustConversionsRequest** | [**AdjustConversionsRequest**](AdjustConversionsRequest.md)|  | |

### Return type

ApiResponse<[**AdjustConversions200Response**](AdjustConversions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Adjustments processed. Inspect &#x60;adjustmentsFailed&#x60; and &#x60;failures[]&#x60; for partial failure (Google reports per-row errors via partial failure).  |  -  |
| **400** | Invalid body, or a malformed adjustment (missing key, missing restatementValue for RESTATEMENT, missing identifiers for ENHANCEMENT). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Conversion adjustments are only available for Google Ads (the account&#39;s platform is not &#x60;googleads&#x60;). |  -  |


## createConversionDestination

> CreateConversionDestination201Response createConversionDestination(accountId, createConversionDestinationRequest)

Create a conversion destination

Create a new conversion destination on the platform. Supported for LinkedIn (conversion rule) and Google Ads (conversion action). Meta manages destinations in its own UI and returns 405.  **LinkedIn:** creation is NOT idempotent. A retry creates a second destination. Deduplicate before retrying.  **Google Ads:** calling with a name that already exists reuses the existing conversion action transparently (the response is identical to a fresh create). Calling with the same name but a different category returns a typed &#x60;IDEMPOTENCY_CONFLICT&#x60; (409) rather than silently returning the mismatched action.  **LinkedIn:** the rule is created with &#x60;conversionMethod&#x3D;CONVERSIONS_API&#x60; and (by default) auto-associated with all of the ad account&#39;s campaigns via &#x60;autoAssociationType&#x3D;ALL_CAMPAIGNS&#x60;. Pass &#x60;autoAssociationType: NONE&#x60; to opt out and manage associations explicitly via the associations endpoints below.  365-day attribution windows are only valid for &#x60;SUBMIT_APPLICATION&#x60;, &#x60;PURCHASE&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;QUALIFIED_LEAD&#x60;, and &#x60;LEAD&#x60; rule types; the API rejects other combinations locally.  **Google Ads:** the conversion action is created with &#x60;type&#x3D;UPLOAD_CLICKS&#x60; (required for API-uploaded offline conversions, immutable after creation). The &#x60;type&#x60; field carries the Google &#x60;ConversionActionCategory&#x60; enum value, e.g. &#x60;PURCHASE&#x60;, &#x60;SUBSCRIBE_PAID&#x60;, &#x60;SIGNUP&#x60;, &#x60;IMPORTED_LEAD&#x60;, &#x60;BOOK_APPOINTMENT&#x60;. Unified standard event names (e.g. &#x60;Purchase&#x60;, &#x60;Subscribe&#x60;, &#x60;CompleteRegistration&#x60;, &#x60;Lead&#x60;, &#x60;Schedule&#x60;) are resolved to their Google category equivalents automatically. The action defaults to secondary (non-primary) to avoid immediately steering Smart Bidding; pass &#x60;primaryForGoal: true&#x60; to opt in. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (linkedinads or googleads).
        CreateConversionDestinationRequest createConversionDestinationRequest = new CreateConversionDestinationRequest(); // CreateConversionDestinationRequest | 
        try {
            CreateConversionDestination201Response result = apiInstance.createConversionDestination(accountId, createConversionDestinationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#createConversionDestination");
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
| **accountId** | **String**| SocialAccount ID (linkedinads or googleads). | |
| **createConversionDestinationRequest** | [**CreateConversionDestinationRequest**](CreateConversionDestinationRequest.md)|  | |

### Return type

[**CreateConversionDestination201Response**](CreateConversionDestination201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Destination created |  -  |
| **400** | Invalid body or platform validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the connected LinkedIn account lacks the &#x60;rw_conversions&#x60; scope (reconnect required).  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support destination creation. |  -  |
| **409** | Google Ads only. A conversion action with the given name already exists but has a different category. Use a different name or use the existing destination. Error code: &#x60;IDEMPOTENCY_CONFLICT&#x60;.  |  -  |
| **429** | Rate limit hit. Retry with backoff. |  -  |

## createConversionDestinationWithHttpInfo

> ApiResponse<CreateConversionDestination201Response> createConversionDestination createConversionDestinationWithHttpInfo(accountId, createConversionDestinationRequest)

Create a conversion destination

Create a new conversion destination on the platform. Supported for LinkedIn (conversion rule) and Google Ads (conversion action). Meta manages destinations in its own UI and returns 405.  **LinkedIn:** creation is NOT idempotent. A retry creates a second destination. Deduplicate before retrying.  **Google Ads:** calling with a name that already exists reuses the existing conversion action transparently (the response is identical to a fresh create). Calling with the same name but a different category returns a typed &#x60;IDEMPOTENCY_CONFLICT&#x60; (409) rather than silently returning the mismatched action.  **LinkedIn:** the rule is created with &#x60;conversionMethod&#x3D;CONVERSIONS_API&#x60; and (by default) auto-associated with all of the ad account&#39;s campaigns via &#x60;autoAssociationType&#x3D;ALL_CAMPAIGNS&#x60;. Pass &#x60;autoAssociationType: NONE&#x60; to opt out and manage associations explicitly via the associations endpoints below.  365-day attribution windows are only valid for &#x60;SUBMIT_APPLICATION&#x60;, &#x60;PURCHASE&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;QUALIFIED_LEAD&#x60;, and &#x60;LEAD&#x60; rule types; the API rejects other combinations locally.  **Google Ads:** the conversion action is created with &#x60;type&#x3D;UPLOAD_CLICKS&#x60; (required for API-uploaded offline conversions, immutable after creation). The &#x60;type&#x60; field carries the Google &#x60;ConversionActionCategory&#x60; enum value, e.g. &#x60;PURCHASE&#x60;, &#x60;SUBSCRIBE_PAID&#x60;, &#x60;SIGNUP&#x60;, &#x60;IMPORTED_LEAD&#x60;, &#x60;BOOK_APPOINTMENT&#x60;. Unified standard event names (e.g. &#x60;Purchase&#x60;, &#x60;Subscribe&#x60;, &#x60;CompleteRegistration&#x60;, &#x60;Lead&#x60;, &#x60;Schedule&#x60;) are resolved to their Google category equivalents automatically. The action defaults to secondary (non-primary) to avoid immediately steering Smart Bidding; pass &#x60;primaryForGoal: true&#x60; to opt in. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (linkedinads or googleads).
        CreateConversionDestinationRequest createConversionDestinationRequest = new CreateConversionDestinationRequest(); // CreateConversionDestinationRequest | 
        try {
            ApiResponse<CreateConversionDestination201Response> response = apiInstance.createConversionDestinationWithHttpInfo(accountId, createConversionDestinationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#createConversionDestination");
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
| **accountId** | **String**| SocialAccount ID (linkedinads or googleads). | |
| **createConversionDestinationRequest** | [**CreateConversionDestinationRequest**](CreateConversionDestinationRequest.md)|  | |

### Return type

ApiResponse<[**CreateConversionDestination201Response**](CreateConversionDestination201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Destination created |  -  |
| **400** | Invalid body or platform validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the connected LinkedIn account lacks the &#x60;rw_conversions&#x60; scope (reconnect required).  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support destination creation. |  -  |
| **409** | Google Ads only. A conversion action with the given name already exists but has a different category. Use a different name or use the existing destination. Error code: &#x60;IDEMPOTENCY_CONFLICT&#x60;.  |  -  |
| **429** | Rate limit hit. Retry with backoff. |  -  |


## deleteConversionDestination

> void deleteConversionDestination(accountId, destinationId, adAccountId)

Delete a conversion destination

LinkedIn-only today. LinkedIn does not expose hard-delete on conversion rules — what their UI calls \&quot;delete\&quot; is the same &#x60;enabled: false&#x60; flip we apply here. The rule remains fetchable via GET with &#x60;status: &#39;inactive&#39;&#x60;; the unified discovery endpoint hides it by default.  &#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Required as query OR in JSON body.
        try {
            apiInstance.deleteConversionDestination(accountId, destinationId, adAccountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#deleteConversionDestination");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Required as query OR in JSON body. | [optional] |

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
| **204** | Soft-deleted. |  -  |
| **400** | adAccountId missing. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support deleting destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## deleteConversionDestinationWithHttpInfo

> ApiResponse<Void> deleteConversionDestination deleteConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId)

Delete a conversion destination

LinkedIn-only today. LinkedIn does not expose hard-delete on conversion rules — what their UI calls \&quot;delete\&quot; is the same &#x60;enabled: false&#x60; flip we apply here. The rule remains fetchable via GET with &#x60;status: &#39;inactive&#39;&#x60;; the unified discovery endpoint hides it by default.  &#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Required as query OR in JSON body.
        try {
            ApiResponse<Void> response = apiInstance.deleteConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#deleteConversionDestination");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Required as query OR in JSON body. | [optional] |

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
| **204** | Soft-deleted. |  -  |
| **400** | adAccountId missing. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support deleting destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## getConversionDestination

> GetConversionDestination200Response getConversionDestination(accountId, destinationId, adAccountId)

Get a conversion destination

LinkedIn-only today. Returns the full destination record for one conversion rule. The &#x60;adAccountId&#x60; query parameter is required because LinkedIn rules are scoped to a sponsored ad account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Numeric ID or full `urn:li:sponsoredAccount:{id}` URN.
        try {
            GetConversionDestination200Response result = apiInstance.getConversionDestination(accountId, destinationId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#getConversionDestination");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Numeric ID or full &#x60;urn:li:sponsoredAccount:{id}&#x60; URN. | |

### Return type

[**GetConversionDestination200Response**](GetConversionDestination200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination fetched |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support fetching a single destination. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## getConversionDestinationWithHttpInfo

> ApiResponse<GetConversionDestination200Response> getConversionDestination getConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId)

Get a conversion destination

LinkedIn-only today. Returns the full destination record for one conversion rule. The &#x60;adAccountId&#x60; query parameter is required because LinkedIn rules are scoped to a sponsored ad account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Numeric ID or full `urn:li:sponsoredAccount:{id}` URN.
        try {
            ApiResponse<GetConversionDestination200Response> response = apiInstance.getConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#getConversionDestination");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Numeric ID or full &#x60;urn:li:sponsoredAccount:{id}&#x60; URN. | |

### Return type

ApiResponse<[**GetConversionDestination200Response**](GetConversionDestination200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination fetched |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support fetching a single destination. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## getConversionMetrics

> GetConversionMetrics200Response getConversionMetrics(accountId, destinationId, adAccountId, startDate, endDate, granularity)

Get attribution metrics

LinkedIn-only today. Returns conversion-attribution metrics (&#x60;externalWebsiteConversions&#x60;, &#x60;externalWebsitePostClickConversions&#x60;, &#x60;externalWebsitePostViewConversions&#x60;, &#x60;conversionValueInLocalCurrency&#x60;, &#x60;qualifiedLeads&#x60;, &#x60;costInLocalCurrency&#x60;) bucketed by date.  Date-range constraints (passed through from LinkedIn): - &#x60;granularity&#x3D;DAILY&#x60; is retained for ~6 months only - &#x60;granularity&#x3D;ALL&#x60; with a range &gt; 6 months auto-rounds to month boundaries - &#x60;granularity&#x3D;MONTHLY&#x60;/&#x60;YEARLY&#x60; retains 24 months  Throttle: LinkedIn caps adAnalytics at 45M metric values per 5-minute window across the calling token. Single-rule queries are well within that limit; surfaces as 429 if hit. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String startDate = "startDate_example"; // String | 
        String endDate = "endDate_example"; // String | 
        String granularity = "ALL"; // String | 
        try {
            GetConversionMetrics200Response result = apiInstance.getConversionMetrics(accountId, destinationId, adAccountId, startDate, endDate, granularity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#getConversionMetrics");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **startDate** | **String**|  | |
| **endDate** | **String**|  | [optional] |
| **granularity** | **String**|  | [optional] [default to DAILY] [enum: ALL, DAILY, MONTHLY, YEARLY] |

### Return type

[**GetConversionMetrics200Response**](GetConversionMetrics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metrics rows |  -  |
| **400** | Validation error or invalid date range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support metrics readback. |  -  |
| **429** | LinkedIn analytics rate limit hit. |  -  |

## getConversionMetricsWithHttpInfo

> ApiResponse<GetConversionMetrics200Response> getConversionMetrics getConversionMetricsWithHttpInfo(accountId, destinationId, adAccountId, startDate, endDate, granularity)

Get attribution metrics

LinkedIn-only today. Returns conversion-attribution metrics (&#x60;externalWebsiteConversions&#x60;, &#x60;externalWebsitePostClickConversions&#x60;, &#x60;externalWebsitePostViewConversions&#x60;, &#x60;conversionValueInLocalCurrency&#x60;, &#x60;qualifiedLeads&#x60;, &#x60;costInLocalCurrency&#x60;) bucketed by date.  Date-range constraints (passed through from LinkedIn): - &#x60;granularity&#x3D;DAILY&#x60; is retained for ~6 months only - &#x60;granularity&#x3D;ALL&#x60; with a range &gt; 6 months auto-rounds to month boundaries - &#x60;granularity&#x3D;MONTHLY&#x60;/&#x60;YEARLY&#x60; retains 24 months  Throttle: LinkedIn caps adAnalytics at 45M metric values per 5-minute window across the calling token. Single-rule queries are well within that limit; surfaces as 429 if hit. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String startDate = "startDate_example"; // String | 
        String endDate = "endDate_example"; // String | 
        String granularity = "ALL"; // String | 
        try {
            ApiResponse<GetConversionMetrics200Response> response = apiInstance.getConversionMetricsWithHttpInfo(accountId, destinationId, adAccountId, startDate, endDate, granularity);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#getConversionMetrics");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **startDate** | **String**|  | |
| **endDate** | **String**|  | [optional] |
| **granularity** | **String**|  | [optional] [default to DAILY] [enum: ALL, DAILY, MONTHLY, YEARLY] |

### Return type

ApiResponse<[**GetConversionMetrics200Response**](GetConversionMetrics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metrics rows |  -  |
| **400** | Validation error or invalid date range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support metrics readback. |  -  |
| **429** | LinkedIn analytics rate limit hit. |  -  |


## getConversionsQuality

> GetConversionsQuality200Response getConversionsQuality(accountId, destinationId)

Get Event Match Quality

Reads Meta Event Match Quality (EMQ) and pixel↔CAPI event coverage for a pixel/dataset, live from Meta&#39;s Dataset Quality API. Web events only (a Meta limitation). Meta-only; other platforms return 405. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount _id (must be a metaads account).
        String destinationId = "destinationId_example"; // String | Meta pixel/dataset ID.
        try {
            GetConversionsQuality200Response result = apiInstance.getConversionsQuality(accountId, destinationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#getConversionsQuality");
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
| **accountId** | **String**| SocialAccount _id (must be a metaads account). | |
| **destinationId** | **String**| Meta pixel/dataset ID. | |

### Return type

[**GetConversionsQuality200Response**](GetConversionsQuality200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Match-quality rows, one per event name. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **405** | Platform does not expose Event Match Quality (non-Meta). |  -  |

## getConversionsQualityWithHttpInfo

> ApiResponse<GetConversionsQuality200Response> getConversionsQuality getConversionsQualityWithHttpInfo(accountId, destinationId)

Get Event Match Quality

Reads Meta Event Match Quality (EMQ) and pixel↔CAPI event coverage for a pixel/dataset, live from Meta&#39;s Dataset Quality API. Web events only (a Meta limitation). Meta-only; other platforms return 405. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount _id (must be a metaads account).
        String destinationId = "destinationId_example"; // String | Meta pixel/dataset ID.
        try {
            ApiResponse<GetConversionsQuality200Response> response = apiInstance.getConversionsQualityWithHttpInfo(accountId, destinationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#getConversionsQuality");
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
| **accountId** | **String**| SocialAccount _id (must be a metaads account). | |
| **destinationId** | **String**| Meta pixel/dataset ID. | |

### Return type

ApiResponse<[**GetConversionsQuality200Response**](GetConversionsQuality200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Match-quality rows, one per event name. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **405** | Platform does not expose Event Match Quality (non-Meta). |  -  |


## listConversionAssociations

> ListConversionAssociations200Response listConversionAssociations(accountId, destinationId, adAccountId)

List associated campaigns

LinkedIn-only today. Returns the campaigns currently associated with this conversion rule. Note that auto-association on rule creation runs once at create time; campaigns created after the rule still need explicit association. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ListConversionAssociations200Response result = apiInstance.listConversionAssociations(accountId, destinationId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#listConversionAssociations");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

[**ListConversionAssociations200Response**](ListConversionAssociations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Associations listed |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## listConversionAssociationsWithHttpInfo

> ApiResponse<ListConversionAssociations200Response> listConversionAssociations listConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId)

List associated campaigns

LinkedIn-only today. Returns the campaigns currently associated with this conversion rule. Note that auto-association on rule creation runs once at create time; campaigns created after the rule still need explicit association. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ApiResponse<ListConversionAssociations200Response> response = apiInstance.listConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#listConversionAssociations");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

ApiResponse<[**ListConversionAssociations200Response**](ListConversionAssociations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Associations listed |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## listConversionDestinations

> ListConversionDestinations200Response listConversionDestinations(accountId)

List conversion destinations

Returns the list of pixels (Meta), conversion actions (Google), or conversion rules (LinkedIn) accessible to the connected ads account. Use the returned &#x60;id&#x60; as &#x60;destinationId&#x60; when posting to &#x60;POST /v1/ads/conversions&#x60;.  For Google and LinkedIn, each destination&#39;s &#x60;type&#x60; reflects the conversion type (PURCHASE, LEAD, SIGN_UP, etc.) — the event type is locked to the destination. For Meta, &#x60;type&#x60; is absent: pixels accept any event name per request.  For LinkedIn, destinations are returned across every sponsored ad account the connected token can access; the &#x60;adAccountId&#x60; field on each destination identifies the parent ad account and is required for subsequent CRUD calls (update, delete, associations, metrics). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (metaads, googleads, linkedinads, or tiktokads).
        try {
            ListConversionDestinations200Response result = apiInstance.listConversionDestinations(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#listConversionDestinations");
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
| **accountId** | **String**| SocialAccount ID (metaads, googleads, linkedinads, or tiktokads). | |

### Return type

[**ListConversionDestinations200Response**](ListConversionDestinations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destinations listed |  -  |
| **400** | Account&#39;s platform is not supported by the Conversions API. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## listConversionDestinationsWithHttpInfo

> ApiResponse<ListConversionDestinations200Response> listConversionDestinations listConversionDestinationsWithHttpInfo(accountId)

List conversion destinations

Returns the list of pixels (Meta), conversion actions (Google), or conversion rules (LinkedIn) accessible to the connected ads account. Use the returned &#x60;id&#x60; as &#x60;destinationId&#x60; when posting to &#x60;POST /v1/ads/conversions&#x60;.  For Google and LinkedIn, each destination&#39;s &#x60;type&#x60; reflects the conversion type (PURCHASE, LEAD, SIGN_UP, etc.) — the event type is locked to the destination. For Meta, &#x60;type&#x60; is absent: pixels accept any event name per request.  For LinkedIn, destinations are returned across every sponsored ad account the connected token can access; the &#x60;adAccountId&#x60; field on each destination identifies the parent ad account and is required for subsequent CRUD calls (update, delete, associations, metrics). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (metaads, googleads, linkedinads, or tiktokads).
        try {
            ApiResponse<ListConversionDestinations200Response> response = apiInstance.listConversionDestinationsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#listConversionDestinations");
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
| **accountId** | **String**| SocialAccount ID (metaads, googleads, linkedinads, or tiktokads). | |

### Return type

ApiResponse<[**ListConversionDestinations200Response**](ListConversionDestinations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destinations listed |  -  |
| **400** | Account&#39;s platform is not supported by the Conversions API. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## removeConversionAssociations

> RemoveConversionAssociations200Response removeConversionAssociations(accountId, destinationId, adAccountId, campaignIds)

Remove associated campaigns

Remove one or more campaign associations from this conversion rule. Pass &#x60;adAccountId&#x60; and &#x60;campaignIds&#x60; as query parameters (&#x60;campaignIds&#x60; is comma-separated). The route also accepts a JSON body with the same fields for clients that prefer DELETE-with-body, but the documented surface is query-only because some SDK code generators (e.g. Python) collapse query + body parameters with the same name into a single kwarg. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String campaignIds = "campaignIds_example"; // String | Comma-separated list of campaign IDs.
        try {
            RemoveConversionAssociations200Response result = apiInstance.removeConversionAssociations(accountId, destinationId, adAccountId, campaignIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#removeConversionAssociations");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **campaignIds** | **String**| Comma-separated list of campaign IDs. | |

### Return type

[**RemoveConversionAssociations200Response**](RemoveConversionAssociations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details.  |  -  |
| **400** | Validation error: missing &#x60;adAccountId&#x60; or &#x60;campaignIds&#x60;, or campaignIds exceeds 100 entries per request.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## removeConversionAssociationsWithHttpInfo

> ApiResponse<RemoveConversionAssociations200Response> removeConversionAssociations removeConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId, campaignIds)

Remove associated campaigns

Remove one or more campaign associations from this conversion rule. Pass &#x60;adAccountId&#x60; and &#x60;campaignIds&#x60; as query parameters (&#x60;campaignIds&#x60; is comma-separated). The route also accepts a JSON body with the same fields for clients that prefer DELETE-with-body, but the documented surface is query-only because some SDK code generators (e.g. Python) collapse query + body parameters with the same name into a single kwarg. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String campaignIds = "campaignIds_example"; // String | Comma-separated list of campaign IDs.
        try {
            ApiResponse<RemoveConversionAssociations200Response> response = apiInstance.removeConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId, campaignIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#removeConversionAssociations");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **campaignIds** | **String**| Comma-separated list of campaign IDs. | |

### Return type

ApiResponse<[**RemoveConversionAssociations200Response**](RemoveConversionAssociations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details.  |  -  |
| **400** | Validation error: missing &#x60;adAccountId&#x60; or &#x60;campaignIds&#x60;, or campaignIds exceeds 100 entries per request.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## sendConversions

> SendConversions200Response sendConversions(sendConversionsRequest)

Send conversion events

Relay one or more conversion events to the target ad platform&#39;s native Conversions API. Platform is inferred from the provided &#x60;accountId&#x60;. Requires the Ads add-on.  Supported platforms:  - Meta (&#x60;metaads&#x60;) via Graph API - Google Ads (&#x60;googleads&#x60;) via Data Manager API &#x60;ingestEvents&#x60; - LinkedIn (&#x60;linkedinads&#x60;) via &#x60;/rest/conversionEvents&#x60; - TikTok (&#x60;tiktokads&#x60;) via the Offline Events API &#x60;/offline/batch/&#x60; — OFFLINE conversions only  &#x60;destinationId&#x60; semantics differ per platform:  - Meta: pixel (dataset) ID, e.g. &#x60;123456789012345&#x60; - Google: conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; - LinkedIn: conversion rule ID or URN, e.g. &#x60;104012&#x60; or &#x60;urn:lla:llaPartnerConversion:104012&#x60; - TikTok: Offline Event Set ID, e.g. &#x60;7057103914977558530&#x60;  TikTok notes: this path sends OFFLINE conversions (in-store / CRM / call-center), not web-pixel events. Each event must carry an email or phone (TikTok requires at least one). The connected TikTok ads account must have granted the Offline Events permission; older grants must reconnect.  Callers can list valid destinations via &#x60;GET /v1/accounts/{accountId}/conversion-destinations&#x60;.  All PII (email, phone, names, external IDs) is hashed with SHA-256 server-side per each platform&#39;s normalization spec, including Google&#39;s Gmail-specific dot/plus-suffix stripping. Send plaintext. LinkedIn &#x60;externalIds&#x60; are passed through as plaintext per LinkedIn&#39;s spec; only emails and phones are hashed.  For LinkedIn, the connected account must have been authorized after the Conversions API rollout (i.e. the OAuth grant must include &#x60;rw_conversions&#x60;). Older accounts must reconnect.  Batching is handled automatically. Meta caps at 1000 events per request and rejects the entire batch if any event is malformed. Google caps at 2000. LinkedIn caps at 5000 and is also all-or-nothing per chunk.  Dedup: pass a stable &#x60;eventId&#x60; on every event. Meta and LinkedIn use it to dedupe against browser-side pixel/Insight Tag events; Google maps it to &#x60;transactionId&#x60;.  Per-platform &#x60;eventName&#x60; semantics:  - Meta: free-form. Standard names (Purchase, Lead, ...) match Meta&#39;s built-in events; custom strings are accepted. - Google: ignored. The conversion action&#39;s category determines the event type. Send the standard name closest to your action for documentation, but the platform will not branch on it. - LinkedIn: ignored. The conversion rule&#39;s &#x60;type&#x60; (LEAD, PURCHASE, etc.) is locked to the destination at rule-creation time. Send the standard name for documentation; LinkedIn does not branch on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        SendConversionsRequest sendConversionsRequest = new SendConversionsRequest(); // SendConversionsRequest | 
        try {
            SendConversions200Response result = apiInstance.sendConversions(sendConversionsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#sendConversions");
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
| **sendConversionsRequest** | [**SendConversionsRequest**](SendConversionsRequest.md)|  | |

### Return type

[**SendConversions200Response**](SendConversions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Events processed. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failure. For Meta, a batch is all-or-nothing (either every event in a chunk succeeds, or every event in the chunk is listed in failures). For Google, the API returns success/failure at the request level only.  |  -  |
| **400** | Invalid body (missing accountId/destinationId/events, malformed event shape). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn token-level rate limit hit (600 requests/min, 300k/day per token). Retry with backoff. Meta and Google have their own rate-limit semantics surfaced via platform-specific 4xx responses.  |  -  |

## sendConversionsWithHttpInfo

> ApiResponse<SendConversions200Response> sendConversions sendConversionsWithHttpInfo(sendConversionsRequest)

Send conversion events

Relay one or more conversion events to the target ad platform&#39;s native Conversions API. Platform is inferred from the provided &#x60;accountId&#x60;. Requires the Ads add-on.  Supported platforms:  - Meta (&#x60;metaads&#x60;) via Graph API - Google Ads (&#x60;googleads&#x60;) via Data Manager API &#x60;ingestEvents&#x60; - LinkedIn (&#x60;linkedinads&#x60;) via &#x60;/rest/conversionEvents&#x60; - TikTok (&#x60;tiktokads&#x60;) via the Offline Events API &#x60;/offline/batch/&#x60; — OFFLINE conversions only  &#x60;destinationId&#x60; semantics differ per platform:  - Meta: pixel (dataset) ID, e.g. &#x60;123456789012345&#x60; - Google: conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; - LinkedIn: conversion rule ID or URN, e.g. &#x60;104012&#x60; or &#x60;urn:lla:llaPartnerConversion:104012&#x60; - TikTok: Offline Event Set ID, e.g. &#x60;7057103914977558530&#x60;  TikTok notes: this path sends OFFLINE conversions (in-store / CRM / call-center), not web-pixel events. Each event must carry an email or phone (TikTok requires at least one). The connected TikTok ads account must have granted the Offline Events permission; older grants must reconnect.  Callers can list valid destinations via &#x60;GET /v1/accounts/{accountId}/conversion-destinations&#x60;.  All PII (email, phone, names, external IDs) is hashed with SHA-256 server-side per each platform&#39;s normalization spec, including Google&#39;s Gmail-specific dot/plus-suffix stripping. Send plaintext. LinkedIn &#x60;externalIds&#x60; are passed through as plaintext per LinkedIn&#39;s spec; only emails and phones are hashed.  For LinkedIn, the connected account must have been authorized after the Conversions API rollout (i.e. the OAuth grant must include &#x60;rw_conversions&#x60;). Older accounts must reconnect.  Batching is handled automatically. Meta caps at 1000 events per request and rejects the entire batch if any event is malformed. Google caps at 2000. LinkedIn caps at 5000 and is also all-or-nothing per chunk.  Dedup: pass a stable &#x60;eventId&#x60; on every event. Meta and LinkedIn use it to dedupe against browser-side pixel/Insight Tag events; Google maps it to &#x60;transactionId&#x60;.  Per-platform &#x60;eventName&#x60; semantics:  - Meta: free-form. Standard names (Purchase, Lead, ...) match Meta&#39;s built-in events; custom strings are accepted. - Google: ignored. The conversion action&#39;s category determines the event type. Send the standard name closest to your action for documentation, but the platform will not branch on it. - LinkedIn: ignored. The conversion rule&#39;s &#x60;type&#x60; (LEAD, PURCHASE, etc.) is locked to the destination at rule-creation time. Send the standard name for documentation; LinkedIn does not branch on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        SendConversionsRequest sendConversionsRequest = new SendConversionsRequest(); // SendConversionsRequest | 
        try {
            ApiResponse<SendConversions200Response> response = apiInstance.sendConversionsWithHttpInfo(sendConversionsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#sendConversions");
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
| **sendConversionsRequest** | [**SendConversionsRequest**](SendConversionsRequest.md)|  | |

### Return type

ApiResponse<[**SendConversions200Response**](SendConversions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Events processed. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failure. For Meta, a batch is all-or-nothing (either every event in a chunk succeeds, or every event in the chunk is listed in failures). For Google, the API returns success/failure at the request level only.  |  -  |
| **400** | Invalid body (missing accountId/destinationId/events, malformed event shape). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn token-level rate limit hit (600 requests/min, 300k/day per token). Retry with backoff. Meta and Google have their own rate-limit semantics surfaced via platform-specific 4xx responses.  |  -  |


## updateConversionDestination

> GetConversionDestination200Response updateConversionDestination(accountId, destinationId, updateConversionDestinationRequest)

Update a conversion destination

Partial-update a conversion rule. LinkedIn-only today. Whitelisted fields: &#x60;name&#x60;, &#x60;enabled&#x60;, attribution windows, &#x60;valueType&#x60;, &#x60;value&#x60;, &#x60;attributionType&#x60;. The rule&#39;s &#x60;type&#x60; and parent ad account are intentionally not exposed for update — recreate the rule if those need to change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        UpdateConversionDestinationRequest updateConversionDestinationRequest = new UpdateConversionDestinationRequest(); // UpdateConversionDestinationRequest | 
        try {
            GetConversionDestination200Response result = apiInstance.updateConversionDestination(accountId, destinationId, updateConversionDestinationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#updateConversionDestination");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **updateConversionDestinationRequest** | [**UpdateConversionDestinationRequest**](UpdateConversionDestinationRequest.md)|  | |

### Return type

[**GetConversionDestination200Response**](GetConversionDestination200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination updated (re-fetched canonical state) |  -  |
| **400** | Invalid body or LinkedIn validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support updating destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## updateConversionDestinationWithHttpInfo

> ApiResponse<GetConversionDestination200Response> updateConversionDestination updateConversionDestinationWithHttpInfo(accountId, destinationId, updateConversionDestinationRequest)

Update a conversion destination

Partial-update a conversion rule. LinkedIn-only today. Whitelisted fields: &#x60;name&#x60;, &#x60;enabled&#x60;, attribution windows, &#x60;valueType&#x60;, &#x60;value&#x60;, &#x60;attributionType&#x60;. The rule&#39;s &#x60;type&#x60; and parent ad account are intentionally not exposed for update — recreate the rule if those need to change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ConversionsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ConversionsApi apiInstance = new ConversionsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        UpdateConversionDestinationRequest updateConversionDestinationRequest = new UpdateConversionDestinationRequest(); // UpdateConversionDestinationRequest | 
        try {
            ApiResponse<GetConversionDestination200Response> response = apiInstance.updateConversionDestinationWithHttpInfo(accountId, destinationId, updateConversionDestinationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ConversionsApi#updateConversionDestination");
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
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **updateConversionDestinationRequest** | [**UpdateConversionDestinationRequest**](UpdateConversionDestinationRequest.md)|  | |

### Return type

ApiResponse<[**GetConversionDestination200Response**](GetConversionDestination200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination updated (re-fetched canonical state) |  -  |
| **400** | Invalid body or LinkedIn validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support updating destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

