# MessagingAdsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCallAd**](MessagingAdsApi.md#createCallAd) | **POST** /v1/ads/call | Create Click-to-Call ad |
| [**createCallAdWithHttpInfo**](MessagingAdsApi.md#createCallAdWithHttpInfo) | **POST** /v1/ads/call | Create Click-to-Call ad |
| [**createCtwaAd**](MessagingAdsApi.md#createCtwaAd) | **POST** /v1/ads/ctwa | Create Click-to-WhatsApp ad (deprecated) |
| [**createCtwaAdWithHttpInfo**](MessagingAdsApi.md#createCtwaAdWithHttpInfo) | **POST** /v1/ads/ctwa | Create Click-to-WhatsApp ad (deprecated) |
| [**createMessagingAd**](MessagingAdsApi.md#createMessagingAd) | **POST** /v1/ads/messaging | Create click-to-message ad (WhatsApp / Messenger / Instagram Direct) |
| [**createMessagingAdWithHttpInfo**](MessagingAdsApi.md#createMessagingAdWithHttpInfo) | **POST** /v1/ads/messaging | Create click-to-message ad (WhatsApp / Messenger / Instagram Direct) |



## createCallAd

> void createCallAd(createCallAdRequest)

Create Click-to-Call ad

Same shape and flow as POST /v1/ads/ctwa, but the CTA is CALL_NOW dialing &#x60;phoneNumber&#x60; via a tel: link. The ad set is destination_type PHONE_CALL optimizing QUALITY_CALL and the campaign objective defaults to OUTCOME_LEADS. Supports the same single-creative and multi-creative shapes as CTWA.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagingAdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagingAdsApi apiInstance = new MessagingAdsApi(defaultClient);
        CreateCallAdRequest createCallAdRequest = new CreateCallAdRequest(); // CreateCallAdRequest | 
        try {
            apiInstance.createCallAd(createCallAdRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagingAdsApi#createCallAd");
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
| **createCallAdRequest** | [**CreateCallAdRequest**](CreateCallAdRequest.md)|  | |

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
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |

## createCallAdWithHttpInfo

> ApiResponse<Void> createCallAd createCallAdWithHttpInfo(createCallAdRequest)

Create Click-to-Call ad

Same shape and flow as POST /v1/ads/ctwa, but the CTA is CALL_NOW dialing &#x60;phoneNumber&#x60; via a tel: link. The ad set is destination_type PHONE_CALL optimizing QUALITY_CALL and the campaign objective defaults to OUTCOME_LEADS. Supports the same single-creative and multi-creative shapes as CTWA.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagingAdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagingAdsApi apiInstance = new MessagingAdsApi(defaultClient);
        CreateCallAdRequest createCallAdRequest = new CreateCallAdRequest(); // CreateCallAdRequest | 
        try {
            ApiResponse<Void> response = apiInstance.createCallAdWithHttpInfo(createCallAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagingAdsApi#createCallAd");
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
| **createCallAdRequest** | [**CreateCallAdRequest**](CreateCallAdRequest.md)|  | |

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
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |


## createCtwaAd

> CreateCtwaAd201Response createCtwaAd(ctwaAdRequestBody)

Create Click-to-WhatsApp ad (deprecated)

Deprecated: use POST /v1/ads/messaging with &#x60;destination: whatsapp&#x60;. This endpoint stays available for back-compat; no removal planned.  Creates one or more Click-to-WhatsApp (CTWA) ads on Meta under a single campaign and ad set. When tapped, each ad opens a WhatsApp conversation with the business attached to the supplied Facebook Page. The full hierarchy (campaign, ad set, creative(s), ad(s)) is created and activated in one call. The CTA is locked to WHATSAPP_MESSAGE and the destination is hard-coded to api.whatsapp.com/send; Meta resolves the actual WhatsApp number from the Page-to-WA pairing configured in Page settings or Business Manager.  Supports two mutually-exclusive shapes:  - **Single-creative**: supply top-level &#x60;headline&#x60;, &#x60;body&#x60;, and one of &#x60;imageUrl&#x60; / &#x60;video&#x60;. Creates 1 campaign + 1 ad set + 1 ad.  - **Multi-creative**: supply a &#x60;creatives[]&#x60; array with N entries (each carrying its own headline, body, and image/video). Creates 1 campaign + 1 ad set + N ads sharing budget and targeting so Meta A/Bs the creatives inside a single auction instead of fragmenting budget across N parallel campaigns. Recommended when launching multiple creative variants for the same campaign.  Prerequisites enforced by Meta (surfaced as platform_error on failure): the Facebook Page must be paired with a verified WhatsApp Business number, the WhatsApp Business Account must be business-verified, and the Meta access token must carry ads_management.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagingAdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagingAdsApi apiInstance = new MessagingAdsApi(defaultClient);
        CtwaAdRequestBody ctwaAdRequestBody = new CtwaAdRequestBody(); // CtwaAdRequestBody | 
        try {
            CreateCtwaAd201Response result = apiInstance.createCtwaAd(ctwaAdRequestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagingAdsApi#createCtwaAd");
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
| **ctwaAdRequestBody** | [**CtwaAdRequestBody**](CtwaAdRequestBody.md)|  | |

### Return type

[**CreateCtwaAd201Response**](CreateCtwaAd201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | CTWA ad(s) created and submitted to Meta for review. Response is a tagged union discriminated by &#x60;adType&#x60;:  - &#x60;adType: \&quot;single\&quot;&#x60; → single-creative request: &#x60;{ adType, ad,   message }&#x60; where &#x60;ad&#x60; is the persisted Ad document. - &#x60;adType: \&quot;multi\&quot;&#x60; → multi-creative request: &#x60;{ adType, ads,   platformCampaignId, platformAdSetId, message }&#x60; where &#x60;ads&#x60; is   the array of N persisted Ad documents all sharing the returned   campaign and ad set IDs.  Generated SDK clients can narrow on &#x60;adType&#x60; instead of sniffing for field presence.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | SocialAccount not found. |  -  |
| **422** | Page is not connected to a verified WhatsApp number. |  -  |
| **502** | Meta rejected the request (e.g. WABA business verification missing). Inspect &#x60;platformError&#x60; for the upstream Meta payload.  |  -  |

## createCtwaAdWithHttpInfo

> ApiResponse<CreateCtwaAd201Response> createCtwaAd createCtwaAdWithHttpInfo(ctwaAdRequestBody)

Create Click-to-WhatsApp ad (deprecated)

Deprecated: use POST /v1/ads/messaging with &#x60;destination: whatsapp&#x60;. This endpoint stays available for back-compat; no removal planned.  Creates one or more Click-to-WhatsApp (CTWA) ads on Meta under a single campaign and ad set. When tapped, each ad opens a WhatsApp conversation with the business attached to the supplied Facebook Page. The full hierarchy (campaign, ad set, creative(s), ad(s)) is created and activated in one call. The CTA is locked to WHATSAPP_MESSAGE and the destination is hard-coded to api.whatsapp.com/send; Meta resolves the actual WhatsApp number from the Page-to-WA pairing configured in Page settings or Business Manager.  Supports two mutually-exclusive shapes:  - **Single-creative**: supply top-level &#x60;headline&#x60;, &#x60;body&#x60;, and one of &#x60;imageUrl&#x60; / &#x60;video&#x60;. Creates 1 campaign + 1 ad set + 1 ad.  - **Multi-creative**: supply a &#x60;creatives[]&#x60; array with N entries (each carrying its own headline, body, and image/video). Creates 1 campaign + 1 ad set + N ads sharing budget and targeting so Meta A/Bs the creatives inside a single auction instead of fragmenting budget across N parallel campaigns. Recommended when launching multiple creative variants for the same campaign.  Prerequisites enforced by Meta (surfaced as platform_error on failure): the Facebook Page must be paired with a verified WhatsApp Business number, the WhatsApp Business Account must be business-verified, and the Meta access token must carry ads_management.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagingAdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagingAdsApi apiInstance = new MessagingAdsApi(defaultClient);
        CtwaAdRequestBody ctwaAdRequestBody = new CtwaAdRequestBody(); // CtwaAdRequestBody | 
        try {
            ApiResponse<CreateCtwaAd201Response> response = apiInstance.createCtwaAdWithHttpInfo(ctwaAdRequestBody);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagingAdsApi#createCtwaAd");
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
| **ctwaAdRequestBody** | [**CtwaAdRequestBody**](CtwaAdRequestBody.md)|  | |

### Return type

ApiResponse<[**CreateCtwaAd201Response**](CreateCtwaAd201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | CTWA ad(s) created and submitted to Meta for review. Response is a tagged union discriminated by &#x60;adType&#x60;:  - &#x60;adType: \&quot;single\&quot;&#x60; → single-creative request: &#x60;{ adType, ad,   message }&#x60; where &#x60;ad&#x60; is the persisted Ad document. - &#x60;adType: \&quot;multi\&quot;&#x60; → multi-creative request: &#x60;{ adType, ads,   platformCampaignId, platformAdSetId, message }&#x60; where &#x60;ads&#x60; is   the array of N persisted Ad documents all sharing the returned   campaign and ad set IDs.  Generated SDK clients can narrow on &#x60;adType&#x60; instead of sniffing for field presence.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | SocialAccount not found. |  -  |
| **422** | Page is not connected to a verified WhatsApp number. |  -  |
| **502** | Meta rejected the request (e.g. WABA business verification missing). Inspect &#x60;platformError&#x60; for the upstream Meta payload.  |  -  |


## createMessagingAd

> void createMessagingAd(createMessagingAdRequest)

Create click-to-message ad (WhatsApp / Messenger / Instagram Direct)

Creates a click-to-message ad; &#x60;destination&#x60; selects where the tapped ad opens a conversation: WhatsApp, the Page&#39;s Messenger inbox or the linked Instagram account&#39;s Direct inbox. The ad set is created with the matching destination_type and CONVERSATIONS optimization; the campaign objective defaults to OUTCOME_ENGAGEMENT. Supports single-creative and multi-creative shapes. Supersedes POST /v1/ads/ctwa (deprecated, equivalent to &#x60;destination: whatsapp&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagingAdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagingAdsApi apiInstance = new MessagingAdsApi(defaultClient);
        CreateMessagingAdRequest createMessagingAdRequest = new CreateMessagingAdRequest(); // CreateMessagingAdRequest | 
        try {
            apiInstance.createMessagingAd(createMessagingAdRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagingAdsApi#createMessagingAd");
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
| **createMessagingAdRequest** | [**CreateMessagingAdRequest**](CreateMessagingAdRequest.md)|  | |

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
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |

## createMessagingAdWithHttpInfo

> ApiResponse<Void> createMessagingAd createMessagingAdWithHttpInfo(createMessagingAdRequest)

Create click-to-message ad (WhatsApp / Messenger / Instagram Direct)

Creates a click-to-message ad; &#x60;destination&#x60; selects where the tapped ad opens a conversation: WhatsApp, the Page&#39;s Messenger inbox or the linked Instagram account&#39;s Direct inbox. The ad set is created with the matching destination_type and CONVERSATIONS optimization; the campaign objective defaults to OUTCOME_ENGAGEMENT. Supports single-creative and multi-creative shapes. Supersedes POST /v1/ads/ctwa (deprecated, equivalent to &#x60;destination: whatsapp&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.MessagingAdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        MessagingAdsApi apiInstance = new MessagingAdsApi(defaultClient);
        CreateMessagingAdRequest createMessagingAdRequest = new CreateMessagingAdRequest(); // CreateMessagingAdRequest | 
        try {
            ApiResponse<Void> response = apiInstance.createMessagingAdWithHttpInfo(createMessagingAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling MessagingAdsApi#createMessagingAd");
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
| **createMessagingAdRequest** | [**CreateMessagingAdRequest**](CreateMessagingAdRequest.md)|  | |

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
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |

