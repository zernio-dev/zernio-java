# AdCampaignsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkUpdateAdCampaignStatus**](AdCampaignsApi.md#bulkUpdateAdCampaignStatus) | **POST** /v1/ads/campaigns/bulk-status | Pause or resume many campaigns |
| [**bulkUpdateAdCampaignStatusWithHttpInfo**](AdCampaignsApi.md#bulkUpdateAdCampaignStatusWithHttpInfo) | **POST** /v1/ads/campaigns/bulk-status | Pause or resume many campaigns |
| [**createAdCampaign**](AdCampaignsApi.md#createAdCampaign) | **POST** /v1/ads/campaigns | Create a standalone campaign (Meta) |
| [**createAdCampaignWithHttpInfo**](AdCampaignsApi.md#createAdCampaignWithHttpInfo) | **POST** /v1/ads/campaigns | Create a standalone campaign (Meta) |
| [**deleteAdCampaign**](AdCampaignsApi.md#deleteAdCampaign) | **DELETE** /v1/ads/campaigns/{campaignId} | Delete a campaign |
| [**deleteAdCampaignWithHttpInfo**](AdCampaignsApi.md#deleteAdCampaignWithHttpInfo) | **DELETE** /v1/ads/campaigns/{campaignId} | Delete a campaign |
| [**duplicateAdCampaign**](AdCampaignsApi.md#duplicateAdCampaign) | **POST** /v1/ads/campaigns/{campaignId}/duplicate | Duplicate a campaign |
| [**duplicateAdCampaignWithHttpInfo**](AdCampaignsApi.md#duplicateAdCampaignWithHttpInfo) | **POST** /v1/ads/campaigns/{campaignId}/duplicate | Duplicate a campaign |
| [**duplicateAdSet**](AdCampaignsApi.md#duplicateAdSet) | **POST** /v1/ads/ad-sets/{adSetId}/duplicate | Duplicate an ad set (Meta) |
| [**duplicateAdSetWithHttpInfo**](AdCampaignsApi.md#duplicateAdSetWithHttpInfo) | **POST** /v1/ads/ad-sets/{adSetId}/duplicate | Duplicate an ad set (Meta) |
| [**getAdSetDetails**](AdCampaignsApi.md#getAdSetDetails) | **GET** /v1/ads/ad-sets/{adSetId} | Live ad-set details incl. learning phase (Meta) |
| [**getAdSetDetailsWithHttpInfo**](AdCampaignsApi.md#getAdSetDetailsWithHttpInfo) | **GET** /v1/ads/ad-sets/{adSetId} | Live ad-set details incl. learning phase (Meta) |
| [**getAdTree**](AdCampaignsApi.md#getAdTree) | **GET** /v1/ads/tree | Get campaign tree |
| [**getAdTreeWithHttpInfo**](AdCampaignsApi.md#getAdTreeWithHttpInfo) | **GET** /v1/ads/tree | Get campaign tree |
| [**getAdsTimeline**](AdCampaignsApi.md#getAdsTimeline) | **GET** /v1/ads/timeline | Get daily account metrics |
| [**getAdsTimelineWithHttpInfo**](AdCampaignsApi.md#getAdsTimelineWithHttpInfo) | **GET** /v1/ads/timeline | Get daily account metrics |
| [**listAdCampaigns**](AdCampaignsApi.md#listAdCampaigns) | **GET** /v1/ads/campaigns | List campaigns |
| [**listAdCampaignsWithHttpInfo**](AdCampaignsApi.md#listAdCampaignsWithHttpInfo) | **GET** /v1/ads/campaigns | List campaigns |
| [**updateAdCampaign**](AdCampaignsApi.md#updateAdCampaign) | **PUT** /v1/ads/campaigns/{campaignId} | Update a campaign |
| [**updateAdCampaignWithHttpInfo**](AdCampaignsApi.md#updateAdCampaignWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId} | Update a campaign |
| [**updateAdCampaignStatus**](AdCampaignsApi.md#updateAdCampaignStatus) | **PUT** /v1/ads/campaigns/{campaignId}/status | Pause or resume a campaign |
| [**updateAdCampaignStatusWithHttpInfo**](AdCampaignsApi.md#updateAdCampaignStatusWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/status | Pause or resume a campaign |
| [**updateAdSet**](AdCampaignsApi.md#updateAdSet) | **PUT** /v1/ads/ad-sets/{adSetId} | Update an ad set |
| [**updateAdSetWithHttpInfo**](AdCampaignsApi.md#updateAdSetWithHttpInfo) | **PUT** /v1/ads/ad-sets/{adSetId} | Update an ad set |
| [**updateAdSetStatus**](AdCampaignsApi.md#updateAdSetStatus) | **PUT** /v1/ads/ad-sets/{adSetId}/status | Pause or resume a single ad set |
| [**updateAdSetStatusWithHttpInfo**](AdCampaignsApi.md#updateAdSetStatusWithHttpInfo) | **PUT** /v1/ads/ad-sets/{adSetId}/status | Pause or resume a single ad set |



## bulkUpdateAdCampaignStatus

> BulkUpdateAdCampaignStatus200Response bulkUpdateAdCampaignStatus(bulkUpdateAdCampaignStatusRequest)

Pause or resume many campaigns

Process up to 50 campaigns in one call. Each campaign is updated concurrently and the response contains a per-campaign result so a single bad row does not fail the whole batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BulkUpdateAdCampaignStatusRequest bulkUpdateAdCampaignStatusRequest = new BulkUpdateAdCampaignStatusRequest(); // BulkUpdateAdCampaignStatusRequest | 
        try {
            BulkUpdateAdCampaignStatus200Response result = apiInstance.bulkUpdateAdCampaignStatus(bulkUpdateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#bulkUpdateAdCampaignStatus");
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
| **bulkUpdateAdCampaignStatusRequest** | [**BulkUpdateAdCampaignStatusRequest**](BulkUpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**BulkUpdateAdCampaignStatus200Response**](BulkUpdateAdCampaignStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign results |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |

## bulkUpdateAdCampaignStatusWithHttpInfo

> ApiResponse<BulkUpdateAdCampaignStatus200Response> bulkUpdateAdCampaignStatus bulkUpdateAdCampaignStatusWithHttpInfo(bulkUpdateAdCampaignStatusRequest)

Pause or resume many campaigns

Process up to 50 campaigns in one call. Each campaign is updated concurrently and the response contains a per-campaign result so a single bad row does not fail the whole batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BulkUpdateAdCampaignStatusRequest bulkUpdateAdCampaignStatusRequest = new BulkUpdateAdCampaignStatusRequest(); // BulkUpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<BulkUpdateAdCampaignStatus200Response> response = apiInstance.bulkUpdateAdCampaignStatusWithHttpInfo(bulkUpdateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#bulkUpdateAdCampaignStatus");
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
| **bulkUpdateAdCampaignStatusRequest** | [**BulkUpdateAdCampaignStatusRequest**](BulkUpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**BulkUpdateAdCampaignStatus200Response**](BulkUpdateAdCampaignStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign results |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |


## createAdCampaign

> CreateAdCampaign201Response createAdCampaign(createAdCampaignRequest)

Create a standalone campaign (Meta)

Creates a campaign WITHOUT its first ad set / ad (the ODAX shell only). Ad sets join it later via &#x60;existingCampaignId&#x60; on the create endpoints. A budget here is campaign-level (CBO) by definition; omit it for ABO (each ad set carries its own budget). Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60;. The campaign materializes in &#x60;/v1/ads/tree&#x60; via the next sync discovery pass. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdCampaignRequest createAdCampaignRequest = new CreateAdCampaignRequest(); // CreateAdCampaignRequest | 
        try {
            CreateAdCampaign201Response result = apiInstance.createAdCampaign(createAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdCampaign");
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
| **createAdCampaignRequest** | [**CreateAdCampaignRequest**](CreateAdCampaignRequest.md)|  | |

### Return type

[**CreateAdCampaign201Response**](CreateAdCampaign201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Campaign created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createAdCampaignWithHttpInfo

> ApiResponse<CreateAdCampaign201Response> createAdCampaign createAdCampaignWithHttpInfo(createAdCampaignRequest)

Create a standalone campaign (Meta)

Creates a campaign WITHOUT its first ad set / ad (the ODAX shell only). Ad sets join it later via &#x60;existingCampaignId&#x60; on the create endpoints. A budget here is campaign-level (CBO) by definition; omit it for ABO (each ad set carries its own budget). Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60;. The campaign materializes in &#x60;/v1/ads/tree&#x60; via the next sync discovery pass. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdCampaignRequest createAdCampaignRequest = new CreateAdCampaignRequest(); // CreateAdCampaignRequest | 
        try {
            ApiResponse<CreateAdCampaign201Response> response = apiInstance.createAdCampaignWithHttpInfo(createAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdCampaign");
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
| **createAdCampaignRequest** | [**CreateAdCampaignRequest**](CreateAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCampaign201Response**](CreateAdCampaign201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Campaign created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## deleteAdCampaign

> DeleteAdCampaign200Response deleteAdCampaign(campaignId, deleteAdCampaignRequest)

Delete a campaign

Deletes the whole campaign on the platform, cascading to its ad sets and ads. Locally, all Ad documents for this campaign are marked &#x60;status: cancelled&#x60;.  Meta-only for now. Other platforms return 501 Not Implemented — fall back to DELETE /v1/ads/{adId} per ad in the meantime. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        DeleteAdCampaignRequest deleteAdCampaignRequest = new DeleteAdCampaignRequest(); // DeleteAdCampaignRequest | 
        try {
            DeleteAdCampaign200Response result = apiInstance.deleteAdCampaign(campaignId, deleteAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **deleteAdCampaignRequest** | [**DeleteAdCampaignRequest**](DeleteAdCampaignRequest.md)|  | |

### Return type

[**DeleteAdCampaign200Response**](DeleteAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |

## deleteAdCampaignWithHttpInfo

> ApiResponse<DeleteAdCampaign200Response> deleteAdCampaign deleteAdCampaignWithHttpInfo(campaignId, deleteAdCampaignRequest)

Delete a campaign

Deletes the whole campaign on the platform, cascading to its ad sets and ads. Locally, all Ad documents for this campaign are marked &#x60;status: cancelled&#x60;.  Meta-only for now. Other platforms return 501 Not Implemented — fall back to DELETE /v1/ads/{adId} per ad in the meantime. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        DeleteAdCampaignRequest deleteAdCampaignRequest = new DeleteAdCampaignRequest(); // DeleteAdCampaignRequest | 
        try {
            ApiResponse<DeleteAdCampaign200Response> response = apiInstance.deleteAdCampaignWithHttpInfo(campaignId, deleteAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **deleteAdCampaignRequest** | [**DeleteAdCampaignRequest**](DeleteAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**DeleteAdCampaign200Response**](DeleteAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |


## duplicateAdCampaign

> DuplicateAdCampaign200Response duplicateAdCampaign(campaignId, duplicateAdCampaignRequest)

Duplicate a campaign

Duplicates a campaign, including its ad sets, ads, creatives, and targeting by default (&#x60;deepCopy: true&#x60;). The copy is created paused so callers can review before launching.  Per-platform implementation: - **Meta** uses the native &#x60;POST /{campaign-id}/copies&#x60; endpoint. - **TikTok** has no native copy primitive; Zernio walks the source   graph (&#x60;/v2/campaign/get/&#x60;, &#x60;/v2/adgroup/get/&#x60;, &#x60;/v2/ad/get/&#x60;) and   recreates each entity via the corresponding &#x60;/create/&#x60; endpoints,   carrying over budget / targeting / bid_type / bid_price /   deep_bid_type / creative fields. Spark Ad linkage (&#x60;tiktok_item_id&#x60;)   is preserved. - **LinkedIn** has no native copy primitive; Zernio walks the source   CampaignGroup → Campaigns → Creatives and recreates each entity,   carrying over &#x60;type&#x60; / &#x60;costType&#x60; / &#x60;unitCost&#x60; /   &#x60;optimizationTargetType&#x60; / &#x60;creativeSelection&#x60; / &#x60;objectiveType&#x60; /   &#x60;format&#x60; / &#x60;dailyBudget&#x60; / &#x60;totalBudget&#x60; / &#x60;targetingCriteria&#x60; /   &#x60;runSchedule&#x60; and every Creative&#39;s &#x60;content&#x60; object verbatim.   &#x60;statusOption: INHERITED_FROM_SOURCE&#x60; is evaluated **per entity**:   any Group / Campaign / Creative whose source is &#x60;ACTIVE&#x60; gets its   clone activated too. Duplicating an ACTIVE campaign with   &#x60;INHERITED_FROM_SOURCE&#x60; starts a second front of spend the moment   the clone activates — the safe default is &#x60;PAUSED&#x60;.  The new hierarchy is asynchronous to materialize in our DB — we trigger sync discovery automatically. Set &#x60;syncAfter: false&#x60; to skip and poll &#x60;/v1/ads/tree&#x60; on your own cadence.  Other platforms return 501 Not Implemented. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Source platform campaign ID
        DuplicateAdCampaignRequest duplicateAdCampaignRequest = new DuplicateAdCampaignRequest(); // DuplicateAdCampaignRequest | 
        try {
            DuplicateAdCampaign200Response result = apiInstance.duplicateAdCampaign(campaignId, duplicateAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdCampaign");
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
| **campaignId** | **String**| Source platform campaign ID | |
| **duplicateAdCampaignRequest** | [**DuplicateAdCampaignRequest**](DuplicateAdCampaignRequest.md)|  | |

### Return type

[**DuplicateAdCampaign200Response**](DuplicateAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Source campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |

## duplicateAdCampaignWithHttpInfo

> ApiResponse<DuplicateAdCampaign200Response> duplicateAdCampaign duplicateAdCampaignWithHttpInfo(campaignId, duplicateAdCampaignRequest)

Duplicate a campaign

Duplicates a campaign, including its ad sets, ads, creatives, and targeting by default (&#x60;deepCopy: true&#x60;). The copy is created paused so callers can review before launching.  Per-platform implementation: - **Meta** uses the native &#x60;POST /{campaign-id}/copies&#x60; endpoint. - **TikTok** has no native copy primitive; Zernio walks the source   graph (&#x60;/v2/campaign/get/&#x60;, &#x60;/v2/adgroup/get/&#x60;, &#x60;/v2/ad/get/&#x60;) and   recreates each entity via the corresponding &#x60;/create/&#x60; endpoints,   carrying over budget / targeting / bid_type / bid_price /   deep_bid_type / creative fields. Spark Ad linkage (&#x60;tiktok_item_id&#x60;)   is preserved. - **LinkedIn** has no native copy primitive; Zernio walks the source   CampaignGroup → Campaigns → Creatives and recreates each entity,   carrying over &#x60;type&#x60; / &#x60;costType&#x60; / &#x60;unitCost&#x60; /   &#x60;optimizationTargetType&#x60; / &#x60;creativeSelection&#x60; / &#x60;objectiveType&#x60; /   &#x60;format&#x60; / &#x60;dailyBudget&#x60; / &#x60;totalBudget&#x60; / &#x60;targetingCriteria&#x60; /   &#x60;runSchedule&#x60; and every Creative&#39;s &#x60;content&#x60; object verbatim.   &#x60;statusOption: INHERITED_FROM_SOURCE&#x60; is evaluated **per entity**:   any Group / Campaign / Creative whose source is &#x60;ACTIVE&#x60; gets its   clone activated too. Duplicating an ACTIVE campaign with   &#x60;INHERITED_FROM_SOURCE&#x60; starts a second front of spend the moment   the clone activates — the safe default is &#x60;PAUSED&#x60;.  The new hierarchy is asynchronous to materialize in our DB — we trigger sync discovery automatically. Set &#x60;syncAfter: false&#x60; to skip and poll &#x60;/v1/ads/tree&#x60; on your own cadence.  Other platforms return 501 Not Implemented. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Source platform campaign ID
        DuplicateAdCampaignRequest duplicateAdCampaignRequest = new DuplicateAdCampaignRequest(); // DuplicateAdCampaignRequest | 
        try {
            ApiResponse<DuplicateAdCampaign200Response> response = apiInstance.duplicateAdCampaignWithHttpInfo(campaignId, duplicateAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdCampaign");
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
| **campaignId** | **String**| Source platform campaign ID | |
| **duplicateAdCampaignRequest** | [**DuplicateAdCampaignRequest**](DuplicateAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**DuplicateAdCampaign200Response**](DuplicateAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Source campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |


## duplicateAdSet

> DuplicateAdSet200Response duplicateAdSet(adSetId, duplicateAdSetRequest)

Duplicate an ad set (Meta)

Duplicates an ad set, including its ads and creatives by default (&#x60;deepCopy: true&#x60;), via Meta&#39;s native &#x60;POST /{adset-id}/copies&#x60;. The copy is created paused so callers can review before launching. &#x60;campaignId&#x60; retargets the copy into another campaign; omitted &#x3D; the source&#39;s own campaign. The new hierarchy materializes asynchronously — sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Source platform ad set ID
        DuplicateAdSetRequest duplicateAdSetRequest = new DuplicateAdSetRequest(); // DuplicateAdSetRequest | 
        try {
            DuplicateAdSet200Response result = apiInstance.duplicateAdSet(adSetId, duplicateAdSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdSet");
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
| **adSetId** | **String**| Source platform ad set ID | |
| **duplicateAdSetRequest** | [**DuplicateAdSetRequest**](DuplicateAdSetRequest.md)|  | |

### Return type

[**DuplicateAdSet200Response**](DuplicateAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Source ad set not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## duplicateAdSetWithHttpInfo

> ApiResponse<DuplicateAdSet200Response> duplicateAdSet duplicateAdSetWithHttpInfo(adSetId, duplicateAdSetRequest)

Duplicate an ad set (Meta)

Duplicates an ad set, including its ads and creatives by default (&#x60;deepCopy: true&#x60;), via Meta&#39;s native &#x60;POST /{adset-id}/copies&#x60;. The copy is created paused so callers can review before launching. &#x60;campaignId&#x60; retargets the copy into another campaign; omitted &#x3D; the source&#39;s own campaign. The new hierarchy materializes asynchronously — sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Source platform ad set ID
        DuplicateAdSetRequest duplicateAdSetRequest = new DuplicateAdSetRequest(); // DuplicateAdSetRequest | 
        try {
            ApiResponse<DuplicateAdSet200Response> response = apiInstance.duplicateAdSetWithHttpInfo(adSetId, duplicateAdSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdSet");
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
| **adSetId** | **String**| Source platform ad set ID | |
| **duplicateAdSetRequest** | [**DuplicateAdSetRequest**](DuplicateAdSetRequest.md)|  | |

### Return type

ApiResponse<[**DuplicateAdSet200Response**](DuplicateAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Source ad set not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdSetDetails

> GetAdSetDetails200Response getAdSetDetails(adSetId, accountId, fields)

Live ad-set details incl. learning phase (Meta)

Reads the ad set live from Meta, returned verbatim. The default projection includes &#x60;learning_stage_info&#x60; (learning-phase status: LEARNING / SUCCESS / FAIL / WAIVING — Meta omits its &#x60;status&#x60; key on paused ad sets), delivery settings, budgets, schedule and targeting. &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Meta ad set id (platformAdSetId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            GetAdSetDetails200Response result = apiInstance.getAdSetDetails(adSetId, accountId, fields);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetDetails");
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
| **adSetId** | **String**| Meta ad set id (platformAdSetId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

[**GetAdSetDetails200Response**](GetAdSetDetails200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ad set as returned by Meta |  -  |
| **400** | Invalid input, or Meta rejected the query — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdSetDetailsWithHttpInfo

> ApiResponse<GetAdSetDetails200Response> getAdSetDetails getAdSetDetailsWithHttpInfo(adSetId, accountId, fields)

Live ad-set details incl. learning phase (Meta)

Reads the ad set live from Meta, returned verbatim. The default projection includes &#x60;learning_stage_info&#x60; (learning-phase status: LEARNING / SUCCESS / FAIL / WAIVING — Meta omits its &#x60;status&#x60; key on paused ad sets), delivery settings, budgets, schedule and targeting. &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Meta ad set id (platformAdSetId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            ApiResponse<GetAdSetDetails200Response> response = apiInstance.getAdSetDetailsWithHttpInfo(adSetId, accountId, fields);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetDetails");
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
| **adSetId** | **String**| Meta ad set id (platformAdSetId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

ApiResponse<[**GetAdSetDetails200Response**](GetAdSetDetails200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ad set as returned by Meta |  -  |
| **400** | Invalid input, or Meta rejected the query — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdTree

> GetAdTree200Response getAdTree(page, limit, source, platform, status, adAccountId, accountId, profileId, campaignId, fromDate, toDate, sort, timeIncrement, dailyLevel)

Get campaign tree

Returns a nested Campaign &gt; Ad Set &gt; Ad hierarchy with rolled-up metrics at each level. Uses a two-stage aggregation: ads are grouped into ad sets, then ad sets into campaigns. Metrics are computed over an optional date range, then rolled up from ad level to ad set and campaign levels. Pagination is at the campaign level. Ads without a campaign or ad set ID are grouped into synthetic \&quot;Ungrouped\&quot; buckets. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  Pass &#x60;timeIncrement&#x3D;1&#x60; to also get a daily breakdown: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) in the same call. Use &#x60;dailyLevel&#x60; (&#x60;campaign&#x60; default, or &#x60;adset&#x60; / &#x60;ad&#x60;) to choose which levels carry the series. This replaces calling the tree once per day for per-campaign daily trends. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | Campaigns per page
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager — matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default — use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID
        String accountId = "accountId_example"; // String | Social account ID
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta's numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination — pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the `campaignId` filter on GET /v1/ads.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of the METRICS date range (YYYY-MM-DD). Affects only the spend/impression numbers overlaid on each node, NOT which campaigns are returned. Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String sort = "newest"; // String | Campaign-level sort order. `newest` (default) / `oldest` order by the campaign's newest-ad createdAt. `spend_desc` / `spend_asc` order by aggregated spend in the requested date range; campaigns with no spend land at the end.
        Integer timeIncrement = 1; // Integer | Set to `1` to also return a daily breakdown. Mirrors Meta Insights' `time_increment=1`: each node gains a `daily[]` array of per-day metrics (same fields as the aggregated `metrics`) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only `1` (daily) is supported. The daily series covers the same date range and uses the same source data as `metrics`. See `dailyLevel` to control which levels carry it.
        String dailyLevel = "campaign"; // String | Which tree levels get the `daily[]` series when `timeIncrement=1`. `campaign` (default) attaches it on campaign nodes only — the common per-campaign-trend case, and the smallest payload. `adset` adds it on ad sets too; `ad` adds it on every ad in `ads[]` as well (heaviest — a long range × up to 100 ads per ad set). Scope with `campaignId` to keep `ad`-level responses small. Ignored when `timeIncrement` is unset.
        try {
            GetAdTree200Response result = apiInstance.getAdTree(page, limit, source, platform, status, adAccountId, accountId, profileId, campaignId, fromDate, toDate, sort, timeIncrement, dailyLevel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdTree");
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
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**| Campaigns per page | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager — matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default — use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID | [optional] |
| **accountId** | **String**| Social account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta&#39;s numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination — pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the &#x60;campaignId&#x60; filter on GET /v1/ads. | [optional] |
| **fromDate** | **LocalDate**| Start of the METRICS date range (YYYY-MM-DD). Affects only the spend/impression numbers overlaid on each node, NOT which campaigns are returned. Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **sort** | **String**| Campaign-level sort order. &#x60;newest&#x60; (default) / &#x60;oldest&#x60; order by the campaign&#39;s newest-ad createdAt. &#x60;spend_desc&#x60; / &#x60;spend_asc&#x60; order by aggregated spend in the requested date range; campaigns with no spend land at the end. | [optional] [default to newest] [enum: newest, oldest, spend_desc, spend_asc] |
| **timeIncrement** | **Integer**| Set to &#x60;1&#x60; to also return a daily breakdown. Mirrors Meta Insights&#39; &#x60;time_increment&#x3D;1&#x60;: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only &#x60;1&#x60; (daily) is supported. The daily series covers the same date range and uses the same source data as &#x60;metrics&#x60;. See &#x60;dailyLevel&#x60; to control which levels carry it. | [optional] [enum: 1] |
| **dailyLevel** | **String**| Which tree levels get the &#x60;daily[]&#x60; series when &#x60;timeIncrement&#x3D;1&#x60;. &#x60;campaign&#x60; (default) attaches it on campaign nodes only — the common per-campaign-trend case, and the smallest payload. &#x60;adset&#x60; adds it on ad sets too; &#x60;ad&#x60; adds it on every ad in &#x60;ads[]&#x60; as well (heaviest — a long range × up to 100 ads per ad set). Scope with &#x60;campaignId&#x60; to keep &#x60;ad&#x60;-level responses small. Ignored when &#x60;timeIncrement&#x60; is unset. | [optional] [default to campaign] [enum: campaign, adset, ad] |

### Return type

[**GetAdTree200Response**](GetAdTree200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nested campaign tree with pagination |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## getAdTreeWithHttpInfo

> ApiResponse<GetAdTree200Response> getAdTree getAdTreeWithHttpInfo(page, limit, source, platform, status, adAccountId, accountId, profileId, campaignId, fromDate, toDate, sort, timeIncrement, dailyLevel)

Get campaign tree

Returns a nested Campaign &gt; Ad Set &gt; Ad hierarchy with rolled-up metrics at each level. Uses a two-stage aggregation: ads are grouped into ad sets, then ad sets into campaigns. Metrics are computed over an optional date range, then rolled up from ad level to ad set and campaign levels. Pagination is at the campaign level. Ads without a campaign or ad set ID are grouped into synthetic \&quot;Ungrouped\&quot; buckets. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  Pass &#x60;timeIncrement&#x3D;1&#x60; to also get a daily breakdown: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) in the same call. Use &#x60;dailyLevel&#x60; (&#x60;campaign&#x60; default, or &#x60;adset&#x60; / &#x60;ad&#x60;) to choose which levels carry the series. This replaces calling the tree once per day for per-campaign daily trends. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | Campaigns per page
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager — matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default — use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID
        String accountId = "accountId_example"; // String | Social account ID
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta's numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination — pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the `campaignId` filter on GET /v1/ads.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of the METRICS date range (YYYY-MM-DD). Affects only the spend/impression numbers overlaid on each node, NOT which campaigns are returned. Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String sort = "newest"; // String | Campaign-level sort order. `newest` (default) / `oldest` order by the campaign's newest-ad createdAt. `spend_desc` / `spend_asc` order by aggregated spend in the requested date range; campaigns with no spend land at the end.
        Integer timeIncrement = 1; // Integer | Set to `1` to also return a daily breakdown. Mirrors Meta Insights' `time_increment=1`: each node gains a `daily[]` array of per-day metrics (same fields as the aggregated `metrics`) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only `1` (daily) is supported. The daily series covers the same date range and uses the same source data as `metrics`. See `dailyLevel` to control which levels carry it.
        String dailyLevel = "campaign"; // String | Which tree levels get the `daily[]` series when `timeIncrement=1`. `campaign` (default) attaches it on campaign nodes only — the common per-campaign-trend case, and the smallest payload. `adset` adds it on ad sets too; `ad` adds it on every ad in `ads[]` as well (heaviest — a long range × up to 100 ads per ad set). Scope with `campaignId` to keep `ad`-level responses small. Ignored when `timeIncrement` is unset.
        try {
            ApiResponse<GetAdTree200Response> response = apiInstance.getAdTreeWithHttpInfo(page, limit, source, platform, status, adAccountId, accountId, profileId, campaignId, fromDate, toDate, sort, timeIncrement, dailyLevel);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdTree");
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
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**| Campaigns per page | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager — matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default — use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID | [optional] |
| **accountId** | **String**| Social account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Restrict the tree to a single campaign by its platform campaign id (the id the platform assigns, e.g. Meta&#39;s numeric campaign id). Filters the campaign set itself, so it works regardless of account size and pagination — pass this when you already hold a campaign id instead of paging the tree to find it. Mirrors the &#x60;campaignId&#x60; filter on GET /v1/ads. | [optional] |
| **fromDate** | **LocalDate**| Start of the METRICS date range (YYYY-MM-DD). Affects only the spend/impression numbers overlaid on each node, NOT which campaigns are returned. Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **sort** | **String**| Campaign-level sort order. &#x60;newest&#x60; (default) / &#x60;oldest&#x60; order by the campaign&#39;s newest-ad createdAt. &#x60;spend_desc&#x60; / &#x60;spend_asc&#x60; order by aggregated spend in the requested date range; campaigns with no spend land at the end. | [optional] [default to newest] [enum: newest, oldest, spend_desc, spend_asc] |
| **timeIncrement** | **Integer**| Set to &#x60;1&#x60; to also return a daily breakdown. Mirrors Meta Insights&#39; &#x60;time_increment&#x3D;1&#x60;: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) alongside the range total, so you get per-entity daily trends in ONE call instead of calling the tree once per day. Only &#x60;1&#x60; (daily) is supported. The daily series covers the same date range and uses the same source data as &#x60;metrics&#x60;. See &#x60;dailyLevel&#x60; to control which levels carry it. | [optional] [enum: 1] |
| **dailyLevel** | **String**| Which tree levels get the &#x60;daily[]&#x60; series when &#x60;timeIncrement&#x3D;1&#x60;. &#x60;campaign&#x60; (default) attaches it on campaign nodes only — the common per-campaign-trend case, and the smallest payload. &#x60;adset&#x60; adds it on ad sets too; &#x60;ad&#x60; adds it on every ad in &#x60;ads[]&#x60; as well (heaviest — a long range × up to 100 ads per ad set). Scope with &#x60;campaignId&#x60; to keep &#x60;ad&#x60;-level responses small. Ignored when &#x60;timeIncrement&#x60; is unset. | [optional] [default to campaign] [enum: campaign, adset, ad] |

### Return type

ApiResponse<[**GetAdTree200Response**](GetAdTree200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nested campaign tree with pagination |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## getAdsTimeline

> GetAdsTimeline200Response getAdsTimeline(accountId, adAccountId, fromDate, toDate, platform)

Get daily account metrics

Returns daily aggregate metrics across all ads in a SocialAccount as a single time series — one row per calendar day in the requested range. Use this for dashboards that draw a daily-spend or daily-conversions chart, instead of calling &#x60;/v1/ads/tree&#x60; once per day.  &#x60;accountId&#x60; is required. The lookup is sibling-expanded so passing the &#x60;metaads&#x60; ID also includes ads under the linked &#x60;facebook&#x60; / &#x60;instagram&#x60; posting account (and vice-versa) — same convention as &#x60;/v1/ads/tree&#x60; and &#x60;/v1/ads&#x60;.  Date range defaults to the last 90 days. Capped at 730 days. Ranges older than the ingested history return a &#x60;202&#x60; immediately with the covered part and &#x60;backfillPending: true&#x60; while the rest is backfilled in the background; repeat the request shortly until it returns 200 with full data. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID. Sibling-expanded to its linked posting↔ads pair.
        String adAccountId = "adAccountId_example"; // String | Optional platform-native ad account ID (e.g. Meta `act_…`, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don't carry this column; the recurring 7-day re-sync repopulates them naturally.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String platform = "facebook"; // String | Restrict to one platform.
        try {
            GetAdsTimeline200Response result = apiInstance.getAdsTimeline(accountId, adAccountId, fromDate, toDate, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdsTimeline");
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
| **accountId** | **String**| Social account ID. Sibling-expanded to its linked posting↔ads pair. | |
| **adAccountId** | **String**| Optional platform-native ad account ID (e.g. Meta &#x60;act_…&#x60;, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don&#39;t carry this column; the recurring 7-day re-sync repopulates them naturally. | [optional] |
| **fromDate** | **LocalDate**| Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **platform** | **String**| Restrict to one platform. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |

### Return type

[**GetAdsTimeline200Response**](GetAdsTimeline200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily time series of aggregate metrics. Empty &#x60;rows&#x60; means the account has no ad activity in the range. |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## getAdsTimelineWithHttpInfo

> ApiResponse<GetAdsTimeline200Response> getAdsTimeline getAdsTimelineWithHttpInfo(accountId, adAccountId, fromDate, toDate, platform)

Get daily account metrics

Returns daily aggregate metrics across all ads in a SocialAccount as a single time series — one row per calendar day in the requested range. Use this for dashboards that draw a daily-spend or daily-conversions chart, instead of calling &#x60;/v1/ads/tree&#x60; once per day.  &#x60;accountId&#x60; is required. The lookup is sibling-expanded so passing the &#x60;metaads&#x60; ID also includes ads under the linked &#x60;facebook&#x60; / &#x60;instagram&#x60; posting account (and vice-versa) — same convention as &#x60;/v1/ads/tree&#x60; and &#x60;/v1/ads&#x60;.  Date range defaults to the last 90 days. Capped at 730 days. Ranges older than the ingested history return a &#x60;202&#x60; immediately with the covered part and &#x60;backfillPending: true&#x60; while the rest is backfilled in the background; repeat the request shortly until it returns 200 with full data. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID. Sibling-expanded to its linked posting↔ads pair.
        String adAccountId = "adAccountId_example"; // String | Optional platform-native ad account ID (e.g. Meta `act_…`, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don't carry this column; the recurring 7-day re-sync repopulates them naturally.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String platform = "facebook"; // String | Restrict to one platform.
        try {
            ApiResponse<GetAdsTimeline200Response> response = apiInstance.getAdsTimelineWithHttpInfo(accountId, adAccountId, fromDate, toDate, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdsTimeline");
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
| **accountId** | **String**| Social account ID. Sibling-expanded to its linked posting↔ads pair. | |
| **adAccountId** | **String**| Optional platform-native ad account ID (e.g. Meta &#x60;act_…&#x60;, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don&#39;t carry this column; the recurring 7-day re-sync repopulates them naturally. | [optional] |
| **fromDate** | **LocalDate**| Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **platform** | **String**| Restrict to one platform. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |

### Return type

ApiResponse<[**GetAdsTimeline200Response**](GetAdsTimeline200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily time series of aggregate metrics. Empty &#x60;rows&#x60; means the account has no ad activity in the range. |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdCampaigns

> ListAdCampaigns200Response listAdCampaigns(page, limit, source, platform, status, adAccountId, accountId, profileId, fromDate, toDate)

List campaigns

Returns campaigns as virtual aggregations over ad documents grouped by platform campaign ID. Metrics (spend, impressions, clicks, etc.) are summed across all ads in each campaign. Campaign status is derived from child ad statuses (active &gt; pending_review &gt; paused &gt; error &gt; completed &gt; cancelled &gt; rejected). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | 
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager — matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default — use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta)
        String accountId = "accountId_example"; // String | Social account ID
        String profileId = "profileId_example"; // String | Profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range.
        try {
            ListAdCampaigns200Response result = apiInstance.listAdCampaigns(page, limit, source, platform, status, adAccountId, accountId, profileId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdCampaigns");
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
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager — matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default — use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta) | [optional] |
| **accountId** | **String**| Social account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range. | [optional] |

### Return type

[**ListAdCampaigns200Response**](ListAdCampaigns200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated campaigns |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdCampaignsWithHttpInfo

> ApiResponse<ListAdCampaigns200Response> listAdCampaigns listAdCampaignsWithHttpInfo(page, limit, source, platform, status, adAccountId, accountId, profileId, fromDate, toDate)

List campaigns

Returns campaigns as virtual aggregations over ad documents grouped by platform campaign ID. Metrics (spend, impressions, clicks, etc.) are summed across all ads in each campaign. Campaign status is derived from child ad statuses (active &gt; pending_review &gt; paused &gt; error &gt; completed &gt; cancelled &gt; rejected). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | 
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager — matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default — use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta)
        String accountId = "accountId_example"; // String | Social account ID
        String profileId = "profileId_example"; // String | Profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range.
        try {
            ApiResponse<ListAdCampaigns200Response> response = apiInstance.listAdCampaignsWithHttpInfo(page, limit, source, platform, status, adAccountId, accountId, profileId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdCampaigns");
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
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager — matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default — use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta) | [optional] |
| **accountId** | **String**| Social account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range. | [optional] |

### Return type

ApiResponse<[**ListAdCampaigns200Response**](ListAdCampaigns200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated campaigns |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## updateAdCampaign

> UpdateAdCampaign200Response updateAdCampaign(campaignId, updateAdCampaignRequest)

Update a campaign

Campaign-level edits. At least one of &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;name&#x60; or &#x60;platformSpecificData&#x60; is required.  - &#x60;budget&#x60; updates the CBO (Campaign Budget Optimization) budget. For ABO campaigns   (where the budget lives on the ad set), use PUT /v1/ads/ad-sets/{adSetId} instead — this endpoint   will return 409 with code BUDGET_LEVEL_MISMATCH. - &#x60;bidStrategy&#x60; sets the campaign-level default bid strategy. Per Meta&#39;s spec, &#x60;bid_amount&#x60; and   &#x60;bid_constraints&#x60; do NOT exist at the campaign level — pass them via PUT /v1/ads/ad-sets/{adSetId}. - &#x60;platformSpecificData.spendCap&#x60; (Meta only) sets the campaign&#39;s lifetime spend cap, in the ad   account&#39;s currency.  Meta-only for now. Other platforms return 501 Not Implemented. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignRequest updateAdCampaignRequest = new UpdateAdCampaignRequest(); // UpdateAdCampaignRequest | 
        try {
            UpdateAdCampaign200Response result = apiInstance.updateAdCampaign(campaignId, updateAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignRequest** | [**UpdateAdCampaignRequest**](UpdateAdCampaignRequest.md)|  | |

### Return type

[**UpdateAdCampaign200Response**](UpdateAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign is ABO — route to /v1/ads/ad-sets/{adSetId} instead |  -  |
| **501** | Operation not supported on this platform |  -  |

## updateAdCampaignWithHttpInfo

> ApiResponse<UpdateAdCampaign200Response> updateAdCampaign updateAdCampaignWithHttpInfo(campaignId, updateAdCampaignRequest)

Update a campaign

Campaign-level edits. At least one of &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;name&#x60; or &#x60;platformSpecificData&#x60; is required.  - &#x60;budget&#x60; updates the CBO (Campaign Budget Optimization) budget. For ABO campaigns   (where the budget lives on the ad set), use PUT /v1/ads/ad-sets/{adSetId} instead — this endpoint   will return 409 with code BUDGET_LEVEL_MISMATCH. - &#x60;bidStrategy&#x60; sets the campaign-level default bid strategy. Per Meta&#39;s spec, &#x60;bid_amount&#x60; and   &#x60;bid_constraints&#x60; do NOT exist at the campaign level — pass them via PUT /v1/ads/ad-sets/{adSetId}. - &#x60;platformSpecificData.spendCap&#x60; (Meta only) sets the campaign&#39;s lifetime spend cap, in the ad   account&#39;s currency.  Meta-only for now. Other platforms return 501 Not Implemented. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignRequest updateAdCampaignRequest = new UpdateAdCampaignRequest(); // UpdateAdCampaignRequest | 
        try {
            ApiResponse<UpdateAdCampaign200Response> response = apiInstance.updateAdCampaignWithHttpInfo(campaignId, updateAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaign");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignRequest** | [**UpdateAdCampaignRequest**](UpdateAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCampaign200Response**](UpdateAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign is ABO — route to /v1/ads/ad-sets/{adSetId} instead |  -  |
| **501** | Operation not supported on this platform |  -  |


## updateAdCampaignStatus

> UpdateAdCampaignStatus200Response updateAdCampaignStatus(campaignId, updateAdCampaignStatusRequest)

Pause or resume a campaign

Updates the status of all ads in a campaign. Makes one platform API call (not per-ad) since status cascades through the campaign hierarchy. Ads in terminal statuses (rejected, completed, cancelled) are automatically skipped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            UpdateAdCampaignStatus200Response result = apiInstance.updateAdCampaignStatus(campaignId, updateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaignStatus");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**UpdateAdCampaignStatus200Response**](UpdateAdCampaignStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign status updated |  -  |
| **400** | Invalid input or campaign spans multiple social accounts |  -  |
| **401** | Unauthorized |  -  |
| **404** | No ads found for this campaign |  -  |

## updateAdCampaignStatusWithHttpInfo

> ApiResponse<UpdateAdCampaignStatus200Response> updateAdCampaignStatus updateAdCampaignStatusWithHttpInfo(campaignId, updateAdCampaignStatusRequest)

Pause or resume a campaign

Updates the status of all ads in a campaign. Makes one platform API call (not per-ad) since status cascades through the campaign hierarchy. Ads in terminal statuses (rejected, completed, cancelled) are automatically skipped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<UpdateAdCampaignStatus200Response> response = apiInstance.updateAdCampaignStatusWithHttpInfo(campaignId, updateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaignStatus");
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
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCampaignStatus200Response**](UpdateAdCampaignStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign status updated |  -  |
| **400** | Invalid input or campaign spans multiple social accounts |  -  |
| **401** | Unauthorized |  -  |
| **404** | No ads found for this campaign |  -  |


## updateAdSet

> UpdateAdSet200Response updateAdSet(adSetId, updateAdSetRequest)

Update an ad set

Ad-set-level writes. Use this for ABO budget updates, ad-set-scoped pause/resume, bid-strategy edits, and Meta-only post-launch delivery settings via &#x60;platformSpecificData&#x60;. At least one updatable field is required.  Bid strategy compatibility (per Meta&#39;s spec): - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: no &#x60;bidAmount&#x60;, no &#x60;roasAverageFloor&#x60;. - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; / &#x60;COST_CAP&#x60;: &#x60;bidAmount&#x60; REQUIRED (whole currency units). - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60;: &#x60;roasAverageFloor&#x60; REQUIRED (decimal multiplier, e.g. 2.0 &#x3D; 2.0x ROAS).  Delivery settings are validated by Meta against the campaign objective; incompatible combinations (e.g. a billingEvent the optimization goal doesn&#39;t allow) surface as 400s from Meta.  When updating &#x60;budget&#x60; on an ABO campaign: if the parent campaign is CBO, the response is 409 with code BUDGET_LEVEL_MISMATCH — route to PUT /v1/ads/campaigns/{campaignId} instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdSetRequest updateAdSetRequest = new UpdateAdSetRequest(); // UpdateAdSetRequest | 
        try {
            UpdateAdSet200Response result = apiInstance.updateAdSet(adSetId, updateAdSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSet");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdSetRequest** | [**UpdateAdSetRequest**](UpdateAdSetRequest.md)|  | |

### Return type

[**UpdateAdSet200Response**](UpdateAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad set not found |  -  |
| **409** | Campaign is CBO — route to /v1/ads/campaigns/{campaignId} instead |  -  |
| **501** | bidStrategy not supported on the platform (Meta + TikTok only) |  -  |

## updateAdSetWithHttpInfo

> ApiResponse<UpdateAdSet200Response> updateAdSet updateAdSetWithHttpInfo(adSetId, updateAdSetRequest)

Update an ad set

Ad-set-level writes. Use this for ABO budget updates, ad-set-scoped pause/resume, bid-strategy edits, and Meta-only post-launch delivery settings via &#x60;platformSpecificData&#x60;. At least one updatable field is required.  Bid strategy compatibility (per Meta&#39;s spec): - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: no &#x60;bidAmount&#x60;, no &#x60;roasAverageFloor&#x60;. - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; / &#x60;COST_CAP&#x60;: &#x60;bidAmount&#x60; REQUIRED (whole currency units). - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60;: &#x60;roasAverageFloor&#x60; REQUIRED (decimal multiplier, e.g. 2.0 &#x3D; 2.0x ROAS).  Delivery settings are validated by Meta against the campaign objective; incompatible combinations (e.g. a billingEvent the optimization goal doesn&#39;t allow) surface as 400s from Meta.  When updating &#x60;budget&#x60; on an ABO campaign: if the parent campaign is CBO, the response is 409 with code BUDGET_LEVEL_MISMATCH — route to PUT /v1/ads/campaigns/{campaignId} instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdSetRequest updateAdSetRequest = new UpdateAdSetRequest(); // UpdateAdSetRequest | 
        try {
            ApiResponse<UpdateAdSet200Response> response = apiInstance.updateAdSetWithHttpInfo(adSetId, updateAdSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSet");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdSetRequest** | [**UpdateAdSetRequest**](UpdateAdSetRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdSet200Response**](UpdateAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad set not found |  -  |
| **409** | Campaign is CBO — route to /v1/ads/campaigns/{campaignId} instead |  -  |
| **501** | bidStrategy not supported on the platform (Meta + TikTok only) |  -  |


## updateAdSetStatus

> UpdateAdSetStatus200Response updateAdSetStatus(adSetId, updateAdCampaignStatusRequest)

Pause or resume a single ad set

Ad-set-scoped pause/resume (doesn&#39;t touch sibling ad sets). Thin wrapper over PUT /v1/ads/ad-sets/{adSetId} for callers that only want the status toggle and prefer a symmetric URL to /v1/ads/campaigns/{campaignId}/status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            UpdateAdSetStatus200Response result = apiInstance.updateAdSetStatus(adSetId, updateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSetStatus");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**UpdateAdSetStatus200Response**](UpdateAdSetStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set status updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad set not found |  -  |

## updateAdSetStatusWithHttpInfo

> ApiResponse<UpdateAdSetStatus200Response> updateAdSetStatus updateAdSetStatusWithHttpInfo(adSetId, updateAdCampaignStatusRequest)

Pause or resume a single ad set

Ad-set-scoped pause/resume (doesn&#39;t touch sibling ad sets). Thin wrapper over PUT /v1/ads/ad-sets/{adSetId} for callers that only want the status toggle and prefer a symmetric URL to /v1/ads/campaigns/{campaignId}/status. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<UpdateAdSetStatus200Response> response = apiInstance.updateAdSetStatusWithHttpInfo(adSetId, updateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSetStatus");
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
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdSetStatus200Response**](UpdateAdSetStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set status updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad set not found |  -  |

