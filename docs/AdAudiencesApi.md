# AdAudiencesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addUsersToAdAudience**](AdAudiencesApi.md#addUsersToAdAudience) | **POST** /v1/ads/audiences/{audienceId}/users | Add users to audience |
| [**addUsersToAdAudienceWithHttpInfo**](AdAudiencesApi.md#addUsersToAdAudienceWithHttpInfo) | **POST** /v1/ads/audiences/{audienceId}/users | Add users to audience |
| [**createAdAudience**](AdAudiencesApi.md#createAdAudience) | **POST** /v1/ads/audiences | Create custom audience |
| [**createAdAudienceWithHttpInfo**](AdAudiencesApi.md#createAdAudienceWithHttpInfo) | **POST** /v1/ads/audiences | Create custom audience |
| [**deleteAdAudience**](AdAudiencesApi.md#deleteAdAudience) | **DELETE** /v1/ads/audiences/{audienceId} | Delete custom audience |
| [**deleteAdAudienceWithHttpInfo**](AdAudiencesApi.md#deleteAdAudienceWithHttpInfo) | **DELETE** /v1/ads/audiences/{audienceId} | Delete custom audience |
| [**getAdAudience**](AdAudiencesApi.md#getAdAudience) | **GET** /v1/ads/audiences/{audienceId} | Get audience details |
| [**getAdAudienceWithHttpInfo**](AdAudiencesApi.md#getAdAudienceWithHttpInfo) | **GET** /v1/ads/audiences/{audienceId} | Get audience details |
| [**listAdAudiences**](AdAudiencesApi.md#listAdAudiences) | **GET** /v1/ads/audiences | List custom audiences |
| [**listAdAudiencesWithHttpInfo**](AdAudiencesApi.md#listAdAudiencesWithHttpInfo) | **GET** /v1/ads/audiences | List custom audiences |
| [**replaceAdAudienceCompanies**](AdAudiencesApi.md#replaceAdAudienceCompanies) | **POST** /v1/ads/audiences/{audienceId}/companies | Replace audience companies |
| [**replaceAdAudienceCompaniesWithHttpInfo**](AdAudiencesApi.md#replaceAdAudienceCompaniesWithHttpInfo) | **POST** /v1/ads/audiences/{audienceId}/companies | Replace audience companies |
| [**updateAdAudience**](AdAudiencesApi.md#updateAdAudience) | **PUT** /v1/ads/audiences/{audienceId} | Update an audience |
| [**updateAdAudienceWithHttpInfo**](AdAudiencesApi.md#updateAdAudienceWithHttpInfo) | **PUT** /v1/ads/audiences/{audienceId} | Update an audience |



## addUsersToAdAudience

> AddUsersToAdAudience200Response addUsersToAdAudience(audienceId, addUsersToAdAudienceRequest)

Add users to audience

Upload user data to a customer_list audience. Data is SHA256-hashed server-side before sending to the platform. Email is used on every platform; phone is used on Meta only (other platforms ignore it). On TikTok and Pinterest, the first upload also provisions the audience (deferred create). LinkedIn uploads are full-replace. Max 10,000 users per request.  customer_list only. A LinkedIn &#x60;company_list&#x60; audience takes company rows, not people: send those to &#x60;POST /v1/ads/audiences/{audienceId}/companies&#x60;. This endpoint 422s for every other audience type. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        AddUsersToAdAudienceRequest addUsersToAdAudienceRequest = new AddUsersToAdAudienceRequest(); // AddUsersToAdAudienceRequest | 
        try {
            AddUsersToAdAudience200Response result = apiInstance.addUsersToAdAudience(audienceId, addUsersToAdAudienceRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#addUsersToAdAudience");
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
| **audienceId** | **String**|  | |
| **addUsersToAdAudienceRequest** | [**AddUsersToAdAudienceRequest**](AddUsersToAdAudienceRequest.md)|  | |

### Return type

[**AddUsersToAdAudience200Response**](AddUsersToAdAudience200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Users added |  -  |
| **400** | Invalid input (malformed audienceId, empty users array, missing email/phone) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **422** | Audience is not a customer_list type or has no platform ID yet |  -  |

## addUsersToAdAudienceWithHttpInfo

> ApiResponse<AddUsersToAdAudience200Response> addUsersToAdAudience addUsersToAdAudienceWithHttpInfo(audienceId, addUsersToAdAudienceRequest)

Add users to audience

Upload user data to a customer_list audience. Data is SHA256-hashed server-side before sending to the platform. Email is used on every platform; phone is used on Meta only (other platforms ignore it). On TikTok and Pinterest, the first upload also provisions the audience (deferred create). LinkedIn uploads are full-replace. Max 10,000 users per request.  customer_list only. A LinkedIn &#x60;company_list&#x60; audience takes company rows, not people: send those to &#x60;POST /v1/ads/audiences/{audienceId}/companies&#x60;. This endpoint 422s for every other audience type. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        AddUsersToAdAudienceRequest addUsersToAdAudienceRequest = new AddUsersToAdAudienceRequest(); // AddUsersToAdAudienceRequest | 
        try {
            ApiResponse<AddUsersToAdAudience200Response> response = apiInstance.addUsersToAdAudienceWithHttpInfo(audienceId, addUsersToAdAudienceRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#addUsersToAdAudience");
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
| **audienceId** | **String**|  | |
| **addUsersToAdAudienceRequest** | [**AddUsersToAdAudienceRequest**](AddUsersToAdAudienceRequest.md)|  | |

### Return type

ApiResponse<[**AddUsersToAdAudience200Response**](AddUsersToAdAudience200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Users added |  -  |
| **400** | Invalid input (malformed audienceId, empty users array, missing email/phone) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **422** | Audience is not a customer_list type or has no platform ID yet |  -  |


## createAdAudience

> CreateAdAudience201Response createAdAudience(createAdAudienceRequest)

Create custom audience

Create a custom audience. &#x60;customer_list&#x60; is supported on Meta, Google, X, LinkedIn, TikTok, and Pinterest; &#x60;website&#x60; and &#x60;lookalike&#x60; are Meta-only; &#x60;company_list&#x60;, &#x60;engagement&#x60; and &#x60;website_retargeting&#x60; are LinkedIn-only. &#x60;saved_targeting&#x60; stores a reusable TargetingSpec (no member upload, no adAccountId) that you reference later via &#x60;savedTargetingId&#x60; on &#x60;POST /v1/ads/create&#x60;.  How the audience gets filled depends on the type:  - &#x60;customer_list&#x60; is created empty. Add members with &#x60;POST /v1/ads/audiences/{audienceId}/users&#x60;.   On TikTok and Pinterest the audience is provisioned lazily on that first upload (until then its status is &#x60;pending&#x60;). - &#x60;company_list&#x60; is filled AT CREATION from the &#x60;companies&#x60; array below, which is required. To change the list   afterwards send the new full list to &#x60;POST /v1/ads/audiences/{audienceId}/companies&#x60; (a replace, not a merge).   The &#x60;/users&#x60; endpoint rejects these audiences with a 422. - &#x60;website&#x60;, &#x60;website_retargeting&#x60;, &#x60;engagement&#x60;, &#x60;meta_engagement&#x60; and &#x60;lookalike&#x60; fill themselves from the pixel,   engagement source or seed audience you point them at. They take no member upload at all.  Create is not idempotent, never auto-retry. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        CreateAdAudienceRequest createAdAudienceRequest = new CreateAdAudienceRequest(); // CreateAdAudienceRequest | 
        try {
            CreateAdAudience201Response result = apiInstance.createAdAudience(createAdAudienceRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#createAdAudience");
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
| **createAdAudienceRequest** | [**CreateAdAudienceRequest**](CreateAdAudienceRequest.md)|  | |

### Return type

[**CreateAdAudience201Response**](CreateAdAudience201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Audience created |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## createAdAudienceWithHttpInfo

> ApiResponse<CreateAdAudience201Response> createAdAudience createAdAudienceWithHttpInfo(createAdAudienceRequest)

Create custom audience

Create a custom audience. &#x60;customer_list&#x60; is supported on Meta, Google, X, LinkedIn, TikTok, and Pinterest; &#x60;website&#x60; and &#x60;lookalike&#x60; are Meta-only; &#x60;company_list&#x60;, &#x60;engagement&#x60; and &#x60;website_retargeting&#x60; are LinkedIn-only. &#x60;saved_targeting&#x60; stores a reusable TargetingSpec (no member upload, no adAccountId) that you reference later via &#x60;savedTargetingId&#x60; on &#x60;POST /v1/ads/create&#x60;.  How the audience gets filled depends on the type:  - &#x60;customer_list&#x60; is created empty. Add members with &#x60;POST /v1/ads/audiences/{audienceId}/users&#x60;.   On TikTok and Pinterest the audience is provisioned lazily on that first upload (until then its status is &#x60;pending&#x60;). - &#x60;company_list&#x60; is filled AT CREATION from the &#x60;companies&#x60; array below, which is required. To change the list   afterwards send the new full list to &#x60;POST /v1/ads/audiences/{audienceId}/companies&#x60; (a replace, not a merge).   The &#x60;/users&#x60; endpoint rejects these audiences with a 422. - &#x60;website&#x60;, &#x60;website_retargeting&#x60;, &#x60;engagement&#x60;, &#x60;meta_engagement&#x60; and &#x60;lookalike&#x60; fill themselves from the pixel,   engagement source or seed audience you point them at. They take no member upload at all.  Create is not idempotent, never auto-retry. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        CreateAdAudienceRequest createAdAudienceRequest = new CreateAdAudienceRequest(); // CreateAdAudienceRequest | 
        try {
            ApiResponse<CreateAdAudience201Response> response = apiInstance.createAdAudienceWithHttpInfo(createAdAudienceRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#createAdAudience");
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
| **createAdAudienceRequest** | [**CreateAdAudienceRequest**](CreateAdAudienceRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdAudience201Response**](CreateAdAudience201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Audience created |  -  |
| **400** | Missing required fields |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## deleteAdAudience

> DeleteAccountGroup200Response deleteAdAudience(audienceId)

Delete custom audience

Deletes the audience from both the platform and the local database. &#x60;saved_targeting&#x60; audiences exist only on Zernio, so only the local record is removed.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        try {
            DeleteAccountGroup200Response result = apiInstance.deleteAdAudience(audienceId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#deleteAdAudience");
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
| **audienceId** | **String**|  | |

### Return type

[**DeleteAccountGroup200Response**](DeleteAccountGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## deleteAdAudienceWithHttpInfo

> ApiResponse<DeleteAccountGroup200Response> deleteAdAudience deleteAdAudienceWithHttpInfo(audienceId)

Delete custom audience

Deletes the audience from both the platform and the local database. &#x60;saved_targeting&#x60; audiences exist only on Zernio, so only the local record is removed.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        try {
            ApiResponse<DeleteAccountGroup200Response> response = apiInstance.deleteAdAudienceWithHttpInfo(audienceId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#deleteAdAudience");
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
| **audienceId** | **String**|  | |

### Return type

ApiResponse<[**DeleteAccountGroup200Response**](DeleteAccountGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## getAdAudience

> GetAdAudience200Response getAdAudience(audienceId)

Get audience details

Returns the local audience record and fresh data from Meta (if available).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        try {
            GetAdAudience200Response result = apiInstance.getAdAudience(audienceId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#getAdAudience");
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
| **audienceId** | **String**|  | |

### Return type

[**GetAdAudience200Response**](GetAdAudience200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience details |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## getAdAudienceWithHttpInfo

> ApiResponse<GetAdAudience200Response> getAdAudience getAdAudienceWithHttpInfo(audienceId)

Get audience details

Returns the local audience record and fresh data from Meta (if available).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        try {
            ApiResponse<GetAdAudience200Response> response = apiInstance.getAdAudienceWithHttpInfo(audienceId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#getAdAudience");
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
| **audienceId** | **String**|  | |

### Return type

ApiResponse<[**GetAdAudience200Response**](GetAdAudience200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience details |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## listAdAudiences

> ListAdAudiences200Response listAdAudiences(accountId, adAccountId, platform, type)

List custom audiences

Returns custom audiences for the given ad account. Supports Meta, Google, TikTok, Pinterest, LinkedIn, and X (Twitter).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID
        String platform = "facebook"; // String | 
        String type = "customer_list"; // String | Filter to one audience type. `saved_targeting` returns stored TargetingSpec audiences; the other types return uploaded/derived audiences.
        try {
            ListAdAudiences200Response result = apiInstance.listAdAudiences(accountId, adAccountId, platform, type);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#listAdAudiences");
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
| **accountId** | **String**| Social account ID | |
| **adAccountId** | **String**| Platform ad account ID | |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, googleads, tiktok, tiktokads, pinterest, linkedin, linkedinads, twitter, xads] |
| **type** | **String**| Filter to one audience type. &#x60;saved_targeting&#x60; returns stored TargetingSpec audiences; the other types return uploaded/derived audiences. | [optional] [enum: customer_list, company_list, engagement, meta_engagement, website, website_retargeting, lookalike, saved_targeting] |

### Return type

[**ListAdAudiences200Response**](ListAdAudiences200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audiences |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdAudiencesWithHttpInfo

> ApiResponse<ListAdAudiences200Response> listAdAudiences listAdAudiencesWithHttpInfo(accountId, adAccountId, platform, type)

List custom audiences

Returns custom audiences for the given ad account. Supports Meta, Google, TikTok, Pinterest, LinkedIn, and X (Twitter).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID
        String platform = "facebook"; // String | 
        String type = "customer_list"; // String | Filter to one audience type. `saved_targeting` returns stored TargetingSpec audiences; the other types return uploaded/derived audiences.
        try {
            ApiResponse<ListAdAudiences200Response> response = apiInstance.listAdAudiencesWithHttpInfo(accountId, adAccountId, platform, type);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#listAdAudiences");
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
| **accountId** | **String**| Social account ID | |
| **adAccountId** | **String**| Platform ad account ID | |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, googleads, tiktok, tiktokads, pinterest, linkedin, linkedinads, twitter, xads] |
| **type** | **String**| Filter to one audience type. &#x60;saved_targeting&#x60; returns stored TargetingSpec audiences; the other types return uploaded/derived audiences. | [optional] [enum: customer_list, company_list, engagement, meta_engagement, website, website_retargeting, lookalike, saved_targeting] |

### Return type

ApiResponse<[**ListAdAudiences200Response**](ListAdAudiences200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audiences |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## replaceAdAudienceCompanies

> ReplaceAdAudienceCompanies200Response replaceAdAudienceCompanies(audienceId, replaceAdAudienceCompaniesRequest)

Replace audience companies

Upload the company rows of a LinkedIn &#x60;company_list&#x60; audience (account-based marketing). LinkedIn-only, every other platform returns 422.  A LinkedIn audience segment holds exactly one uploaded list, so the list you send here REPLACES the segment&#39;s list instead of being appended to it: always send the full set of companies. LinkedIn returns only the identifier of the uploaded file, never its rows, so the merge cannot be done for you, keep the source list on your side. LinkedIn does not document how quickly companies dropped from the list stop being targeted, so treat removals as eventual rather than immediate. Rows are plain text (not hashed), matched against LinkedIn&#39;s own company graph. Matching is asynchronous: LinkedIn takes up to 48h for a new audience and up to 24h for a later update, and the audience stays &#x60;processing&#x60; meanwhile. LinkedIn recommends at least 1,000 companies for a usable match rate, and caps a list at 300,000.  The initial list is sent with &#x60;companies&#x60; on &#x60;POST /v1/ads/audiences&#x60;; this endpoint is for every change after that. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        ReplaceAdAudienceCompaniesRequest replaceAdAudienceCompaniesRequest = new ReplaceAdAudienceCompaniesRequest(); // ReplaceAdAudienceCompaniesRequest | 
        try {
            ReplaceAdAudienceCompanies200Response result = apiInstance.replaceAdAudienceCompanies(audienceId, replaceAdAudienceCompaniesRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#replaceAdAudienceCompanies");
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
| **audienceId** | **String**|  | |
| **replaceAdAudienceCompaniesRequest** | [**ReplaceAdAudienceCompaniesRequest**](ReplaceAdAudienceCompaniesRequest.md)|  | |

### Return type

[**ReplaceAdAudienceCompanies200Response**](ReplaceAdAudienceCompanies200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Companies uploaded |  -  |
| **400** | Invalid input (malformed audienceId, empty companies array, a row with no identifier) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **422** | Audience is not a company_list type, is not on LinkedIn, or has no platform ID yet |  -  |

## replaceAdAudienceCompaniesWithHttpInfo

> ApiResponse<ReplaceAdAudienceCompanies200Response> replaceAdAudienceCompanies replaceAdAudienceCompaniesWithHttpInfo(audienceId, replaceAdAudienceCompaniesRequest)

Replace audience companies

Upload the company rows of a LinkedIn &#x60;company_list&#x60; audience (account-based marketing). LinkedIn-only, every other platform returns 422.  A LinkedIn audience segment holds exactly one uploaded list, so the list you send here REPLACES the segment&#39;s list instead of being appended to it: always send the full set of companies. LinkedIn returns only the identifier of the uploaded file, never its rows, so the merge cannot be done for you, keep the source list on your side. LinkedIn does not document how quickly companies dropped from the list stop being targeted, so treat removals as eventual rather than immediate. Rows are plain text (not hashed), matched against LinkedIn&#39;s own company graph. Matching is asynchronous: LinkedIn takes up to 48h for a new audience and up to 24h for a later update, and the audience stays &#x60;processing&#x60; meanwhile. LinkedIn recommends at least 1,000 companies for a usable match rate, and caps a list at 300,000.  The initial list is sent with &#x60;companies&#x60; on &#x60;POST /v1/ads/audiences&#x60;; this endpoint is for every change after that. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        ReplaceAdAudienceCompaniesRequest replaceAdAudienceCompaniesRequest = new ReplaceAdAudienceCompaniesRequest(); // ReplaceAdAudienceCompaniesRequest | 
        try {
            ApiResponse<ReplaceAdAudienceCompanies200Response> response = apiInstance.replaceAdAudienceCompaniesWithHttpInfo(audienceId, replaceAdAudienceCompaniesRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#replaceAdAudienceCompanies");
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
| **audienceId** | **String**|  | |
| **replaceAdAudienceCompaniesRequest** | [**ReplaceAdAudienceCompaniesRequest**](ReplaceAdAudienceCompaniesRequest.md)|  | |

### Return type

ApiResponse<[**ReplaceAdAudienceCompanies200Response**](ReplaceAdAudienceCompanies200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Companies uploaded |  -  |
| **400** | Invalid input (malformed audienceId, empty companies array, a row with no identifier) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **422** | Audience is not a company_list type, is not on LinkedIn, or has no platform ID yet |  -  |


## updateAdAudience

> CreateAdAudience201Response updateAdAudience(audienceId, updateAdAudienceRequest)

Update an audience

Update an audience. &#x60;saved_targeting&#x60; audiences accept &#x60;name&#x60;, &#x60;description&#x60;, and &#x60;spec&#x60; (full replacement, no merge, Zernio-only, no platform call). Platform audiences (uploaded/website/lookalike) accept &#x60;name&#x60; and &#x60;description&#x60; only, updated on the platform first and then mirrored locally; their rules are immutable, so &#x60;spec&#x60; returns 400 for them. Platform audience updates are Meta-only for now (other platforms return 501). Ads already created from a saved_targeting audience are unaffected, they snapshot the targeting at creation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        UpdateAdAudienceRequest updateAdAudienceRequest = new UpdateAdAudienceRequest(); // UpdateAdAudienceRequest | 
        try {
            CreateAdAudience201Response result = apiInstance.updateAdAudience(audienceId, updateAdAudienceRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#updateAdAudience");
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
| **audienceId** | **String**|  | |
| **updateAdAudienceRequest** | [**UpdateAdAudienceRequest**](UpdateAdAudienceRequest.md)|  | |

### Return type

[**CreateAdAudience201Response**](CreateAdAudience201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience updated |  -  |
| **400** | Invalid body (no fields provided, malformed spec, or spec on a platform audience) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **422** | The audience has no platform counterpart to update |  -  |
| **501** | Platform audience updates are only supported on Meta |  -  |

## updateAdAudienceWithHttpInfo

> ApiResponse<CreateAdAudience201Response> updateAdAudience updateAdAudienceWithHttpInfo(audienceId, updateAdAudienceRequest)

Update an audience

Update an audience. &#x60;saved_targeting&#x60; audiences accept &#x60;name&#x60;, &#x60;description&#x60;, and &#x60;spec&#x60; (full replacement, no merge, Zernio-only, no platform call). Platform audiences (uploaded/website/lookalike) accept &#x60;name&#x60; and &#x60;description&#x60; only, updated on the platform first and then mirrored locally; their rules are immutable, so &#x60;spec&#x60; returns 400 for them. Platform audience updates are Meta-only for now (other platforms return 501). Ads already created from a saved_targeting audience are unaffected, they snapshot the targeting at creation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdAudiencesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdAudiencesApi apiInstance = new AdAudiencesApi(defaultClient);
        String audienceId = "audienceId_example"; // String | 
        UpdateAdAudienceRequest updateAdAudienceRequest = new UpdateAdAudienceRequest(); // UpdateAdAudienceRequest | 
        try {
            ApiResponse<CreateAdAudience201Response> response = apiInstance.updateAdAudienceWithHttpInfo(audienceId, updateAdAudienceRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdAudiencesApi#updateAdAudience");
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
| **audienceId** | **String**|  | |
| **updateAdAudienceRequest** | [**UpdateAdAudienceRequest**](UpdateAdAudienceRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdAudience201Response**](CreateAdAudience201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audience updated |  -  |
| **400** | Invalid body (no fields provided, malformed spec, or spec on a platform audience) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |
| **422** | The audience has no platform counterpart to update |  -  |
| **501** | Platform audience updates are only supported on Meta |  -  |

