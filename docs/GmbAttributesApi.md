# GmbAttributesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGmbAttributeMetadata**](GmbAttributesApi.md#getGmbAttributeMetadata) | **GET** /v1/accounts/{accountId}/gmb-attribute-metadata | Get attribute metadata |
| [**getGmbAttributeMetadataWithHttpInfo**](GmbAttributesApi.md#getGmbAttributeMetadataWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-attribute-metadata | Get attribute metadata |
| [**getGoogleBusinessAttributes**](GmbAttributesApi.md#getGoogleBusinessAttributes) | **GET** /v1/accounts/{accountId}/gmb-attributes | Get attributes |
| [**getGoogleBusinessAttributesWithHttpInfo**](GmbAttributesApi.md#getGoogleBusinessAttributesWithHttpInfo) | **GET** /v1/accounts/{accountId}/gmb-attributes | Get attributes |
| [**updateGoogleBusinessAttributes**](GmbAttributesApi.md#updateGoogleBusinessAttributes) | **PUT** /v1/accounts/{accountId}/gmb-attributes | Update attributes |
| [**updateGoogleBusinessAttributesWithHttpInfo**](GmbAttributesApi.md#updateGoogleBusinessAttributesWithHttpInfo) | **PUT** /v1/accounts/{accountId}/gmb-attributes | Update attributes |



## getGmbAttributeMetadata

> GetGmbAttributeMetadata200Response getGmbAttributeMetadata(accountId, locationId, categoryName, regionCode, languageCode, pageSize, pageToken)

Get attribute metadata

Returns metadata about which Google Business Profile attributes are available for a location or business category. Use this endpoint to discover valid attribute names, value types, and allowed enum values before reading or writing via gmb-attributes.  Two mutually exclusive query modes:  **Location mode**: pass &#x60;locationId&#x60; (or rely on the account&#39;s stored &#x60;selectedLocationId&#x60;). Google returns attributes valid for that specific location.  **Category mode**: pass &#x60;categoryName&#x60; (must start with &#x60;categories/&#x60;) and &#x60;regionCode&#x60;. Google returns attributes valid for that category across the given region. &#x60;languageCode&#x60; is optional in category mode.  Both modes support &#x60;pageSize&#x60; and &#x60;pageToken&#x60; for pagination. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbAttributesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbAttributesApi apiInstance = new GmbAttributesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | GBP location ID (e.g. \"6257659026299438786\"). If omitted, uses the account's stored selectedLocationId. Mutually exclusive with categoryName. 
        String categoryName = "categoryName_example"; // String | Category resource name, must start with \"categories/\" (e.g. \"categories/gcid:plumber\"). Required together with regionCode. Mutually exclusive with locationId. 
        String regionCode = "regionCode_example"; // String | BCP-47 region code (e.g. \"US\", \"ES\"). Required when categoryName is provided. 
        String languageCode = "languageCode_example"; // String | BCP-47 language code for display names (e.g. \"en\", \"es\"). Optional when categoryName is provided. Omitted from the Google call when not supplied. 
        Integer pageSize = 56; // Integer | Maximum number of attribute metadata items to return. Google defaults to 200.
        String pageToken = "pageToken_example"; // String | Pagination token from a previous response's nextPageToken field.
        try {
            GetGmbAttributeMetadata200Response result = apiInstance.getGmbAttributeMetadata(accountId, locationId, categoryName, regionCode, languageCode, pageSize, pageToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbAttributesApi#getGmbAttributeMetadata");
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
| **locationId** | **String**| GBP location ID (e.g. \&quot;6257659026299438786\&quot;). If omitted, uses the account&#39;s stored selectedLocationId. Mutually exclusive with categoryName.  | [optional] |
| **categoryName** | **String**| Category resource name, must start with \&quot;categories/\&quot; (e.g. \&quot;categories/gcid:plumber\&quot;). Required together with regionCode. Mutually exclusive with locationId.  | [optional] |
| **regionCode** | **String**| BCP-47 region code (e.g. \&quot;US\&quot;, \&quot;ES\&quot;). Required when categoryName is provided.  | [optional] |
| **languageCode** | **String**| BCP-47 language code for display names (e.g. \&quot;en\&quot;, \&quot;es\&quot;). Optional when categoryName is provided. Omitted from the Google call when not supplied.  | [optional] |
| **pageSize** | **Integer**| Maximum number of attribute metadata items to return. Google defaults to 200. | [optional] |
| **pageToken** | **String**| Pagination token from a previous response&#39;s nextPageToken field. | [optional] |

### Return type

[**GetGmbAttributeMetadata200Response**](GetGmbAttributeMetadata200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attribute metadata fetched successfully |  -  |
| **400** | Invalid request (mixed modes, missing required params, wrong platform, or Google returned 4xx) |  -  |
| **401** | Access token is invalid or revoked. Reconnect the Google Business Profile account. |  -  |
| **404** | Account not found |  -  |

## getGmbAttributeMetadataWithHttpInfo

> ApiResponse<GetGmbAttributeMetadata200Response> getGmbAttributeMetadata getGmbAttributeMetadataWithHttpInfo(accountId, locationId, categoryName, regionCode, languageCode, pageSize, pageToken)

Get attribute metadata

Returns metadata about which Google Business Profile attributes are available for a location or business category. Use this endpoint to discover valid attribute names, value types, and allowed enum values before reading or writing via gmb-attributes.  Two mutually exclusive query modes:  **Location mode**: pass &#x60;locationId&#x60; (or rely on the account&#39;s stored &#x60;selectedLocationId&#x60;). Google returns attributes valid for that specific location.  **Category mode**: pass &#x60;categoryName&#x60; (must start with &#x60;categories/&#x60;) and &#x60;regionCode&#x60;. Google returns attributes valid for that category across the given region. &#x60;languageCode&#x60; is optional in category mode.  Both modes support &#x60;pageSize&#x60; and &#x60;pageToken&#x60; for pagination. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbAttributesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbAttributesApi apiInstance = new GmbAttributesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | GBP location ID (e.g. \"6257659026299438786\"). If omitted, uses the account's stored selectedLocationId. Mutually exclusive with categoryName. 
        String categoryName = "categoryName_example"; // String | Category resource name, must start with \"categories/\" (e.g. \"categories/gcid:plumber\"). Required together with regionCode. Mutually exclusive with locationId. 
        String regionCode = "regionCode_example"; // String | BCP-47 region code (e.g. \"US\", \"ES\"). Required when categoryName is provided. 
        String languageCode = "languageCode_example"; // String | BCP-47 language code for display names (e.g. \"en\", \"es\"). Optional when categoryName is provided. Omitted from the Google call when not supplied. 
        Integer pageSize = 56; // Integer | Maximum number of attribute metadata items to return. Google defaults to 200.
        String pageToken = "pageToken_example"; // String | Pagination token from a previous response's nextPageToken field.
        try {
            ApiResponse<GetGmbAttributeMetadata200Response> response = apiInstance.getGmbAttributeMetadataWithHttpInfo(accountId, locationId, categoryName, regionCode, languageCode, pageSize, pageToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbAttributesApi#getGmbAttributeMetadata");
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
| **locationId** | **String**| GBP location ID (e.g. \&quot;6257659026299438786\&quot;). If omitted, uses the account&#39;s stored selectedLocationId. Mutually exclusive with categoryName.  | [optional] |
| **categoryName** | **String**| Category resource name, must start with \&quot;categories/\&quot; (e.g. \&quot;categories/gcid:plumber\&quot;). Required together with regionCode. Mutually exclusive with locationId.  | [optional] |
| **regionCode** | **String**| BCP-47 region code (e.g. \&quot;US\&quot;, \&quot;ES\&quot;). Required when categoryName is provided.  | [optional] |
| **languageCode** | **String**| BCP-47 language code for display names (e.g. \&quot;en\&quot;, \&quot;es\&quot;). Optional when categoryName is provided. Omitted from the Google call when not supplied.  | [optional] |
| **pageSize** | **Integer**| Maximum number of attribute metadata items to return. Google defaults to 200. | [optional] |
| **pageToken** | **String**| Pagination token from a previous response&#39;s nextPageToken field. | [optional] |

### Return type

ApiResponse<[**GetGmbAttributeMetadata200Response**](GetGmbAttributeMetadata200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attribute metadata fetched successfully |  -  |
| **400** | Invalid request (mixed modes, missing required params, wrong platform, or Google returned 4xx) |  -  |
| **401** | Access token is invalid or revoked. Reconnect the Google Business Profile account. |  -  |
| **404** | Account not found |  -  |


## getGoogleBusinessAttributes

> GetGoogleBusinessAttributes200Response getGoogleBusinessAttributes(accountId, locationId)

Get attributes

Returns GBP location attributes (amenities, services, accessibility, payment types). Available attributes vary by business category.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbAttributesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbAttributesApi apiInstance = new GmbAttributesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            GetGoogleBusinessAttributes200Response result = apiInstance.getGoogleBusinessAttributes(accountId, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbAttributesApi#getGoogleBusinessAttributes");
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
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

[**GetGoogleBusinessAttributes200Response**](GetGoogleBusinessAttributes200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attributes fetched successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## getGoogleBusinessAttributesWithHttpInfo

> ApiResponse<GetGoogleBusinessAttributes200Response> getGoogleBusinessAttributes getGoogleBusinessAttributesWithHttpInfo(accountId, locationId)

Get attributes

Returns GBP location attributes (amenities, services, accessibility, payment types). Available attributes vary by business category.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbAttributesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbAttributesApi apiInstance = new GmbAttributesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String locationId = "locationId_example"; // String | Override which location to query. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            ApiResponse<GetGoogleBusinessAttributes200Response> response = apiInstance.getGoogleBusinessAttributesWithHttpInfo(accountId, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbAttributesApi#getGoogleBusinessAttributes");
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
| **locationId** | **String**| Override which location to query. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

ApiResponse<[**GetGoogleBusinessAttributes200Response**](GetGoogleBusinessAttributes200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attributes fetched successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## updateGoogleBusinessAttributes

> UpdateGoogleBusinessAttributes200Response updateGoogleBusinessAttributes(accountId, updateGoogleBusinessAttributesRequest, locationId)

Update attributes

Updates location attributes (amenities, services, etc.).  The attributeMask specifies which attributes to update (comma-separated). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbAttributesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbAttributesApi apiInstance = new GmbAttributesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGoogleBusinessAttributesRequest updateGoogleBusinessAttributesRequest = new UpdateGoogleBusinessAttributesRequest(); // UpdateGoogleBusinessAttributesRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            UpdateGoogleBusinessAttributes200Response result = apiInstance.updateGoogleBusinessAttributes(accountId, updateGoogleBusinessAttributesRequest, locationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbAttributesApi#updateGoogleBusinessAttributes");
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
| **updateGoogleBusinessAttributesRequest** | [**UpdateGoogleBusinessAttributesRequest**](UpdateGoogleBusinessAttributesRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

[**UpdateGoogleBusinessAttributes200Response**](UpdateGoogleBusinessAttributes200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attributes updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## updateGoogleBusinessAttributesWithHttpInfo

> ApiResponse<UpdateGoogleBusinessAttributes200Response> updateGoogleBusinessAttributes updateGoogleBusinessAttributesWithHttpInfo(accountId, updateGoogleBusinessAttributesRequest, locationId)

Update attributes

Updates location attributes (amenities, services, etc.).  The attributeMask specifies which attributes to update (comma-separated). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.GmbAttributesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        GmbAttributesApi apiInstance = new GmbAttributesApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        UpdateGoogleBusinessAttributesRequest updateGoogleBusinessAttributesRequest = new UpdateGoogleBusinessAttributesRequest(); // UpdateGoogleBusinessAttributesRequest | 
        String locationId = "locationId_example"; // String | Override which location to target. If omitted, uses the account's selected location. Use GET /gmb-locations to list valid IDs.
        try {
            ApiResponse<UpdateGoogleBusinessAttributes200Response> response = apiInstance.updateGoogleBusinessAttributesWithHttpInfo(accountId, updateGoogleBusinessAttributesRequest, locationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling GmbAttributesApi#updateGoogleBusinessAttributes");
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
| **updateGoogleBusinessAttributesRequest** | [**UpdateGoogleBusinessAttributesRequest**](UpdateGoogleBusinessAttributesRequest.md)|  | |
| **locationId** | **String**| Override which location to target. If omitted, uses the account&#39;s selected location. Use GET /gmb-locations to list valid IDs. | [optional] |

### Return type

ApiResponse<[**UpdateGoogleBusinessAttributes200Response**](UpdateGoogleBusinessAttributes200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attributes updated successfully |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

