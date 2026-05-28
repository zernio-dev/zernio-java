# WhatsAppFlowsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWhatsAppFlow**](WhatsAppFlowsApi.md#createWhatsAppFlow) | **POST** /v1/whatsapp/flows | Create flow |
| [**createWhatsAppFlowWithHttpInfo**](WhatsAppFlowsApi.md#createWhatsAppFlowWithHttpInfo) | **POST** /v1/whatsapp/flows | Create flow |
| [**deleteWhatsAppFlow**](WhatsAppFlowsApi.md#deleteWhatsAppFlow) | **DELETE** /v1/whatsapp/flows/{flowId} | Delete flow |
| [**deleteWhatsAppFlowWithHttpInfo**](WhatsAppFlowsApi.md#deleteWhatsAppFlowWithHttpInfo) | **DELETE** /v1/whatsapp/flows/{flowId} | Delete flow |
| [**deprecateWhatsAppFlow**](WhatsAppFlowsApi.md#deprecateWhatsAppFlow) | **POST** /v1/whatsapp/flows/{flowId}/deprecate | Deprecate flow |
| [**deprecateWhatsAppFlowWithHttpInfo**](WhatsAppFlowsApi.md#deprecateWhatsAppFlowWithHttpInfo) | **POST** /v1/whatsapp/flows/{flowId}/deprecate | Deprecate flow |
| [**getWhatsAppFlow**](WhatsAppFlowsApi.md#getWhatsAppFlow) | **GET** /v1/whatsapp/flows/{flowId} | Get flow |
| [**getWhatsAppFlowWithHttpInfo**](WhatsAppFlowsApi.md#getWhatsAppFlowWithHttpInfo) | **GET** /v1/whatsapp/flows/{flowId} | Get flow |
| [**getWhatsAppFlowJson**](WhatsAppFlowsApi.md#getWhatsAppFlowJson) | **GET** /v1/whatsapp/flows/{flowId}/json | Get flow JSON asset |
| [**getWhatsAppFlowJsonWithHttpInfo**](WhatsAppFlowsApi.md#getWhatsAppFlowJsonWithHttpInfo) | **GET** /v1/whatsapp/flows/{flowId}/json | Get flow JSON asset |
| [**getWhatsAppFlowPreview**](WhatsAppFlowsApi.md#getWhatsAppFlowPreview) | **GET** /v1/whatsapp/flows/{flowId}/preview | Get flow preview URL |
| [**getWhatsAppFlowPreviewWithHttpInfo**](WhatsAppFlowsApi.md#getWhatsAppFlowPreviewWithHttpInfo) | **GET** /v1/whatsapp/flows/{flowId}/preview | Get flow preview URL |
| [**listWhatsAppFlowResponses**](WhatsAppFlowsApi.md#listWhatsAppFlowResponses) | **GET** /v1/whatsapp/flow-responses | List flow responses |
| [**listWhatsAppFlowResponsesWithHttpInfo**](WhatsAppFlowsApi.md#listWhatsAppFlowResponsesWithHttpInfo) | **GET** /v1/whatsapp/flow-responses | List flow responses |
| [**listWhatsAppFlowVersions**](WhatsAppFlowsApi.md#listWhatsAppFlowVersions) | **GET** /v1/whatsapp/flows/{flowId}/versions | List flow versions |
| [**listWhatsAppFlowVersionsWithHttpInfo**](WhatsAppFlowsApi.md#listWhatsAppFlowVersionsWithHttpInfo) | **GET** /v1/whatsapp/flows/{flowId}/versions | List flow versions |
| [**listWhatsAppFlows**](WhatsAppFlowsApi.md#listWhatsAppFlows) | **GET** /v1/whatsapp/flows | List flows |
| [**listWhatsAppFlowsWithHttpInfo**](WhatsAppFlowsApi.md#listWhatsAppFlowsWithHttpInfo) | **GET** /v1/whatsapp/flows | List flows |
| [**publishWhatsAppFlow**](WhatsAppFlowsApi.md#publishWhatsAppFlow) | **POST** /v1/whatsapp/flows/{flowId}/publish | Publish flow |
| [**publishWhatsAppFlowWithHttpInfo**](WhatsAppFlowsApi.md#publishWhatsAppFlowWithHttpInfo) | **POST** /v1/whatsapp/flows/{flowId}/publish | Publish flow |
| [**sendWhatsAppFlowMessage**](WhatsAppFlowsApi.md#sendWhatsAppFlowMessage) | **POST** /v1/whatsapp/flows/send | Send flow message |
| [**sendWhatsAppFlowMessageWithHttpInfo**](WhatsAppFlowsApi.md#sendWhatsAppFlowMessageWithHttpInfo) | **POST** /v1/whatsapp/flows/send | Send flow message |
| [**updateWhatsAppFlow**](WhatsAppFlowsApi.md#updateWhatsAppFlow) | **PATCH** /v1/whatsapp/flows/{flowId} | Update flow |
| [**updateWhatsAppFlowWithHttpInfo**](WhatsAppFlowsApi.md#updateWhatsAppFlowWithHttpInfo) | **PATCH** /v1/whatsapp/flows/{flowId} | Update flow |
| [**uploadWhatsAppFlowJson**](WhatsAppFlowsApi.md#uploadWhatsAppFlowJson) | **PUT** /v1/whatsapp/flows/{flowId}/json | Upload flow JSON |
| [**uploadWhatsAppFlowJsonWithHttpInfo**](WhatsAppFlowsApi.md#uploadWhatsAppFlowJsonWithHttpInfo) | **PUT** /v1/whatsapp/flows/{flowId}/json | Upload flow JSON |



## createWhatsAppFlow

> CreateWhatsAppFlow200Response createWhatsAppFlow(createWhatsAppFlowRequest)

Create flow

Create a new WhatsApp Flow in DRAFT status. Optionally clone an existing flow. After creating, upload a Flow JSON definition, then publish to make it sendable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        CreateWhatsAppFlowRequest createWhatsAppFlowRequest = new CreateWhatsAppFlowRequest(); // CreateWhatsAppFlowRequest | 
        try {
            CreateWhatsAppFlow200Response result = apiInstance.createWhatsAppFlow(createWhatsAppFlowRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#createWhatsAppFlow");
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
| **createWhatsAppFlowRequest** | [**CreateWhatsAppFlowRequest**](CreateWhatsAppFlowRequest.md)|  | |

### Return type

[**CreateWhatsAppFlow200Response**](CreateWhatsAppFlow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow created |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## createWhatsAppFlowWithHttpInfo

> ApiResponse<CreateWhatsAppFlow200Response> createWhatsAppFlow createWhatsAppFlowWithHttpInfo(createWhatsAppFlowRequest)

Create flow

Create a new WhatsApp Flow in DRAFT status. Optionally clone an existing flow. After creating, upload a Flow JSON definition, then publish to make it sendable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        CreateWhatsAppFlowRequest createWhatsAppFlowRequest = new CreateWhatsAppFlowRequest(); // CreateWhatsAppFlowRequest | 
        try {
            ApiResponse<CreateWhatsAppFlow200Response> response = apiInstance.createWhatsAppFlowWithHttpInfo(createWhatsAppFlowRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#createWhatsAppFlow");
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
| **createWhatsAppFlowRequest** | [**CreateWhatsAppFlowRequest**](CreateWhatsAppFlowRequest.md)|  | |

### Return type

ApiResponse<[**CreateWhatsAppFlow200Response**](CreateWhatsAppFlow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow created |  -  |
| **400** | Validation error |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## deleteWhatsAppFlow

> UpdateYoutubeDefaultPlaylist200Response deleteWhatsAppFlow(flowId, accountId)

Delete flow

Delete a DRAFT flow. This is irreversible. Only flows in DRAFT status can be deleted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteWhatsAppFlow(flowId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#deleteWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow deleted |  -  |
| **400** | Flow is not in DRAFT status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account or flow not found |  -  |

## deleteWhatsAppFlowWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteWhatsAppFlow deleteWhatsAppFlowWithHttpInfo(flowId, accountId)

Delete flow

Delete a DRAFT flow. This is irreversible. Only flows in DRAFT status can be deleted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteWhatsAppFlowWithHttpInfo(flowId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#deleteWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow deleted |  -  |
| **400** | Flow is not in DRAFT status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account or flow not found |  -  |


## deprecateWhatsAppFlow

> UpdateYoutubeDefaultPlaylist200Response deprecateWhatsAppFlow(flowId, createWhatsAppDatasetRequest)

Deprecate flow

Deprecate a PUBLISHED flow. This is irreversible. Deprecated flows cannot be sent or opened, but existing active sessions may continue until they complete. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        CreateWhatsAppDatasetRequest createWhatsAppDatasetRequest = new CreateWhatsAppDatasetRequest(); // CreateWhatsAppDatasetRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deprecateWhatsAppFlow(flowId, createWhatsAppDatasetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#deprecateWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **createWhatsAppDatasetRequest** | [**CreateWhatsAppDatasetRequest**](CreateWhatsAppDatasetRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow deprecated |  -  |
| **400** | Flow is not in PUBLISHED status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## deprecateWhatsAppFlowWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deprecateWhatsAppFlow deprecateWhatsAppFlowWithHttpInfo(flowId, createWhatsAppDatasetRequest)

Deprecate flow

Deprecate a PUBLISHED flow. This is irreversible. Deprecated flows cannot be sent or opened, but existing active sessions may continue until they complete. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        CreateWhatsAppDatasetRequest createWhatsAppDatasetRequest = new CreateWhatsAppDatasetRequest(); // CreateWhatsAppDatasetRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deprecateWhatsAppFlowWithHttpInfo(flowId, createWhatsAppDatasetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#deprecateWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **createWhatsAppDatasetRequest** | [**CreateWhatsAppDatasetRequest**](CreateWhatsAppDatasetRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow deprecated |  -  |
| **400** | Flow is not in PUBLISHED status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppFlow

> GetWhatsAppFlow200Response getWhatsAppFlow(flowId, accountId, fields)

Get flow

Get details for a specific flow, including status, categories, validation errors, and preview URL. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        String fields = "fields_example"; // String | Comma-separated fields to return (default: id,name,status,categories,validation_errors,json_version,preview,data_api_version,endpoint_uri)
        try {
            GetWhatsAppFlow200Response result = apiInstance.getWhatsAppFlow(flowId, accountId, fields);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#getWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **fields** | **String**| Comma-separated fields to return (default: id,name,status,categories,validation_errors,json_version,preview,data_api_version,endpoint_uri) | [optional] |

### Return type

[**GetWhatsAppFlow200Response**](GetWhatsAppFlow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow details |  -  |
| **401** | Unauthorized |  -  |
| **404** | Flow or account not found |  -  |

## getWhatsAppFlowWithHttpInfo

> ApiResponse<GetWhatsAppFlow200Response> getWhatsAppFlow getWhatsAppFlowWithHttpInfo(flowId, accountId, fields)

Get flow

Get details for a specific flow, including status, categories, validation errors, and preview URL. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        String fields = "fields_example"; // String | Comma-separated fields to return (default: id,name,status,categories,validation_errors,json_version,preview,data_api_version,endpoint_uri)
        try {
            ApiResponse<GetWhatsAppFlow200Response> response = apiInstance.getWhatsAppFlowWithHttpInfo(flowId, accountId, fields);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#getWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **fields** | **String**| Comma-separated fields to return (default: id,name,status,categories,validation_errors,json_version,preview,data_api_version,endpoint_uri) | [optional] |

### Return type

ApiResponse<[**GetWhatsAppFlow200Response**](GetWhatsAppFlow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow details |  -  |
| **401** | Unauthorized |  -  |
| **404** | Flow or account not found |  -  |


## getWhatsAppFlowJson

> GetWhatsAppFlowJson200Response getWhatsAppFlowJson(flowId, accountId)

Get flow JSON asset

Get the flow JSON asset metadata, including a temporary download URL for the Flow JSON file. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppFlowJson200Response result = apiInstance.getWhatsAppFlowJson(flowId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#getWhatsAppFlowJson");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**GetWhatsAppFlowJson200Response**](GetWhatsAppFlowJson200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow JSON asset |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppFlowJsonWithHttpInfo

> ApiResponse<GetWhatsAppFlowJson200Response> getWhatsAppFlowJson getWhatsAppFlowJsonWithHttpInfo(flowId, accountId)

Get flow JSON asset

Get the flow JSON asset metadata, including a temporary download URL for the Flow JSON file. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppFlowJson200Response> response = apiInstance.getWhatsAppFlowJsonWithHttpInfo(flowId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#getWhatsAppFlowJson");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**GetWhatsAppFlowJson200Response**](GetWhatsAppFlowJson200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow JSON asset |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppFlowPreview

> GetWhatsAppFlowPreview200Response getWhatsAppFlowPreview(flowId, accountId, invalidate)

Get flow preview URL

Get Meta&#39;s public web-preview URL for a flow (drafts included), embeddable as an interactive iframe. The link is reused across calls (valid ~30 days); pass invalidate&#x3D;true to mint a fresh one (the previous link stops working). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Boolean invalidate = true; // Boolean | Mint a fresh preview link (default false)
        try {
            GetWhatsAppFlowPreview200Response result = apiInstance.getWhatsAppFlowPreview(flowId, accountId, invalidate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#getWhatsAppFlowPreview");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **invalidate** | **Boolean**| Mint a fresh preview link (default false) | [optional] |

### Return type

[**GetWhatsAppFlowPreview200Response**](GetWhatsAppFlowPreview200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Preview URL |  -  |
| **401** | Unauthorized |  -  |
| **404** | Flow or account not found |  -  |

## getWhatsAppFlowPreviewWithHttpInfo

> ApiResponse<GetWhatsAppFlowPreview200Response> getWhatsAppFlowPreview getWhatsAppFlowPreviewWithHttpInfo(flowId, accountId, invalidate)

Get flow preview URL

Get Meta&#39;s public web-preview URL for a flow (drafts included), embeddable as an interactive iframe. The link is reused across calls (valid ~30 days); pass invalidate&#x3D;true to mint a fresh one (the previous link stops working). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Boolean invalidate = true; // Boolean | Mint a fresh preview link (default false)
        try {
            ApiResponse<GetWhatsAppFlowPreview200Response> response = apiInstance.getWhatsAppFlowPreviewWithHttpInfo(flowId, accountId, invalidate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#getWhatsAppFlowPreview");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **invalidate** | **Boolean**| Mint a fresh preview link (default false) | [optional] |

### Return type

ApiResponse<[**GetWhatsAppFlowPreview200Response**](GetWhatsAppFlowPreview200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Preview URL |  -  |
| **401** | Unauthorized |  -  |
| **404** | Flow or account not found |  -  |


## listWhatsAppFlowResponses

> ListWhatsAppFlowResponses200Response listWhatsAppFlowResponses(accountId, flowId, limit)

List flow responses

List the responses customers submitted when completing a flow (parsed from the nfm_reply messages received via webhook), newest first. Scope to a single flow with &#x60;flowId&#x60; — this matches responses whose flow_token carries the &#x60;&lt;flowId&gt;:&#x60; prefix that Zernio stamps on auto-generated tokens at send time. Responses sent with a custom integrator-supplied flow_token are not attributed to a flow. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        String flowId = "flowId_example"; // String | Scope to responses for this flow
        Integer limit = 50; // Integer | Max responses to return
        try {
            ListWhatsAppFlowResponses200Response result = apiInstance.listWhatsAppFlowResponses(accountId, flowId, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#listWhatsAppFlowResponses");
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
| **accountId** | **String**| WhatsApp social account ID | |
| **flowId** | **String**| Scope to responses for this flow | [optional] |
| **limit** | **Integer**| Max responses to return | [optional] [default to 50] |

### Return type

[**ListWhatsAppFlowResponses200Response**](ListWhatsAppFlowResponses200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow responses |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## listWhatsAppFlowResponsesWithHttpInfo

> ApiResponse<ListWhatsAppFlowResponses200Response> listWhatsAppFlowResponses listWhatsAppFlowResponsesWithHttpInfo(accountId, flowId, limit)

List flow responses

List the responses customers submitted when completing a flow (parsed from the nfm_reply messages received via webhook), newest first. Scope to a single flow with &#x60;flowId&#x60; — this matches responses whose flow_token carries the &#x60;&lt;flowId&gt;:&#x60; prefix that Zernio stamps on auto-generated tokens at send time. Responses sent with a custom integrator-supplied flow_token are not attributed to a flow. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        String flowId = "flowId_example"; // String | Scope to responses for this flow
        Integer limit = 50; // Integer | Max responses to return
        try {
            ApiResponse<ListWhatsAppFlowResponses200Response> response = apiInstance.listWhatsAppFlowResponsesWithHttpInfo(accountId, flowId, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#listWhatsAppFlowResponses");
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
| **accountId** | **String**| WhatsApp social account ID | |
| **flowId** | **String**| Scope to responses for this flow | [optional] |
| **limit** | **Integer**| Max responses to return | [optional] [default to 50] |

### Return type

ApiResponse<[**ListWhatsAppFlowResponses200Response**](ListWhatsAppFlowResponses200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow responses |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## listWhatsAppFlowVersions

> ListWhatsAppFlowVersions200Response listWhatsAppFlowVersions(flowId, accountId)

List flow versions

List the flow&#39;s version history (the clone lineage Zernio tracks, since Meta has no native versioning), newest version first. Each entry is enriched with the version&#39;s live name and status from Meta. A flow with no lineage returns just itself as version 1. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ListWhatsAppFlowVersions200Response result = apiInstance.listWhatsAppFlowVersions(flowId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#listWhatsAppFlowVersions");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**ListWhatsAppFlowVersions200Response**](ListWhatsAppFlowVersions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Version history |  -  |
| **401** | Unauthorized |  -  |
| **404** | Flow or account not found |  -  |

## listWhatsAppFlowVersionsWithHttpInfo

> ApiResponse<ListWhatsAppFlowVersions200Response> listWhatsAppFlowVersions listWhatsAppFlowVersionsWithHttpInfo(flowId, accountId)

List flow versions

List the flow&#39;s version history (the clone lineage Zernio tracks, since Meta has no native versioning), newest version first. Each entry is enriched with the version&#39;s live name and status from Meta. A flow with no lineage returns just itself as version 1. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<ListWhatsAppFlowVersions200Response> response = apiInstance.listWhatsAppFlowVersionsWithHttpInfo(flowId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#listWhatsAppFlowVersions");
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
| **flowId** | **String**| Flow ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**ListWhatsAppFlowVersions200Response**](ListWhatsAppFlowVersions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Version history |  -  |
| **401** | Unauthorized |  -  |
| **404** | Flow or account not found |  -  |


## listWhatsAppFlows

> ListWhatsAppFlows200Response listWhatsAppFlows(accountId)

List flows

List all WhatsApp Flows for the Business Account (WABA) associated with the given account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ListWhatsAppFlows200Response result = apiInstance.listWhatsAppFlows(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#listWhatsAppFlows");
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
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**ListWhatsAppFlows200Response**](ListWhatsAppFlows200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flows retrieved |  -  |
| **400** | WABA ID not found on account |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## listWhatsAppFlowsWithHttpInfo

> ApiResponse<ListWhatsAppFlows200Response> listWhatsAppFlows listWhatsAppFlowsWithHttpInfo(accountId)

List flows

List all WhatsApp Flows for the Business Account (WABA) associated with the given account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<ListWhatsAppFlows200Response> response = apiInstance.listWhatsAppFlowsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#listWhatsAppFlows");
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
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**ListWhatsAppFlows200Response**](ListWhatsAppFlows200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flows retrieved |  -  |
| **400** | WABA ID not found on account |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## publishWhatsAppFlow

> UpdateYoutubeDefaultPlaylist200Response publishWhatsAppFlow(flowId, createWhatsAppDatasetRequest)

Publish flow

Publish a DRAFT flow. This is irreversible. Once published, the flow and its JSON become immutable and the flow can be sent to users. To update a published flow, create a new flow (optionally cloning this one via cloneFlowId). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        CreateWhatsAppDatasetRequest createWhatsAppDatasetRequest = new CreateWhatsAppDatasetRequest(); // CreateWhatsAppDatasetRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.publishWhatsAppFlow(flowId, createWhatsAppDatasetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#publishWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **createWhatsAppDatasetRequest** | [**CreateWhatsAppDatasetRequest**](CreateWhatsAppDatasetRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow published |  -  |
| **400** | Flow is not in DRAFT status or has validation errors |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## publishWhatsAppFlowWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> publishWhatsAppFlow publishWhatsAppFlowWithHttpInfo(flowId, createWhatsAppDatasetRequest)

Publish flow

Publish a DRAFT flow. This is irreversible. Once published, the flow and its JSON become immutable and the flow can be sent to users. To update a published flow, create a new flow (optionally cloning this one via cloneFlowId). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        CreateWhatsAppDatasetRequest createWhatsAppDatasetRequest = new CreateWhatsAppDatasetRequest(); // CreateWhatsAppDatasetRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.publishWhatsAppFlowWithHttpInfo(flowId, createWhatsAppDatasetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#publishWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **createWhatsAppDatasetRequest** | [**CreateWhatsAppDatasetRequest**](CreateWhatsAppDatasetRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow published |  -  |
| **400** | Flow is not in DRAFT status or has validation errors |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## sendWhatsAppFlowMessage

> SendWhatsAppFlowMessage200Response sendWhatsAppFlowMessage(sendWhatsAppFlowMessageRequest)

Send flow message

Send a published flow as an interactive message with a CTA button. When the recipient taps the button, the flow opens natively in WhatsApp. Flow responses are received via webhooks. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        SendWhatsAppFlowMessageRequest sendWhatsAppFlowMessageRequest = new SendWhatsAppFlowMessageRequest(); // SendWhatsAppFlowMessageRequest | 
        try {
            SendWhatsAppFlowMessage200Response result = apiInstance.sendWhatsAppFlowMessage(sendWhatsAppFlowMessageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#sendWhatsAppFlowMessage");
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
| **sendWhatsAppFlowMessageRequest** | [**SendWhatsAppFlowMessageRequest**](SendWhatsAppFlowMessageRequest.md)|  | |

### Return type

[**SendWhatsAppFlowMessage200Response**](SendWhatsAppFlowMessage200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow message sent |  -  |
| **400** | Validation error or missing phone number ID |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## sendWhatsAppFlowMessageWithHttpInfo

> ApiResponse<SendWhatsAppFlowMessage200Response> sendWhatsAppFlowMessage sendWhatsAppFlowMessageWithHttpInfo(sendWhatsAppFlowMessageRequest)

Send flow message

Send a published flow as an interactive message with a CTA button. When the recipient taps the button, the flow opens natively in WhatsApp. Flow responses are received via webhooks. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        SendWhatsAppFlowMessageRequest sendWhatsAppFlowMessageRequest = new SendWhatsAppFlowMessageRequest(); // SendWhatsAppFlowMessageRequest | 
        try {
            ApiResponse<SendWhatsAppFlowMessage200Response> response = apiInstance.sendWhatsAppFlowMessageWithHttpInfo(sendWhatsAppFlowMessageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#sendWhatsAppFlowMessage");
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
| **sendWhatsAppFlowMessageRequest** | [**SendWhatsAppFlowMessageRequest**](SendWhatsAppFlowMessageRequest.md)|  | |

### Return type

ApiResponse<[**SendWhatsAppFlowMessage200Response**](SendWhatsAppFlowMessage200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow message sent |  -  |
| **400** | Validation error or missing phone number ID |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## updateWhatsAppFlow

> UpdateYoutubeDefaultPlaylist200Response updateWhatsAppFlow(flowId, updateWhatsAppFlowRequest)

Update flow

Update metadata (name, categories) of a DRAFT flow. Published flows are immutable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        UpdateWhatsAppFlowRequest updateWhatsAppFlowRequest = new UpdateWhatsAppFlowRequest(); // UpdateWhatsAppFlowRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.updateWhatsAppFlow(flowId, updateWhatsAppFlowRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#updateWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **updateWhatsAppFlowRequest** | [**UpdateWhatsAppFlowRequest**](UpdateWhatsAppFlowRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow updated |  -  |
| **400** | At least one of name or categories is required, or flow is not in DRAFT status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account or flow not found |  -  |

## updateWhatsAppFlowWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> updateWhatsAppFlow updateWhatsAppFlowWithHttpInfo(flowId, updateWhatsAppFlowRequest)

Update flow

Update metadata (name, categories) of a DRAFT flow. Published flows are immutable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        UpdateWhatsAppFlowRequest updateWhatsAppFlowRequest = new UpdateWhatsAppFlowRequest(); // UpdateWhatsAppFlowRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.updateWhatsAppFlowWithHttpInfo(flowId, updateWhatsAppFlowRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#updateWhatsAppFlow");
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
| **flowId** | **String**| Flow ID | |
| **updateWhatsAppFlowRequest** | [**UpdateWhatsAppFlowRequest**](UpdateWhatsAppFlowRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow updated |  -  |
| **400** | At least one of name or categories is required, or flow is not in DRAFT status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account or flow not found |  -  |


## uploadWhatsAppFlowJson

> UploadWhatsAppFlowJson200Response uploadWhatsAppFlowJson(flowId, uploadWhatsAppFlowJsonRequest)

Upload flow JSON

Upload or update the Flow JSON for a DRAFT flow. The Flow JSON defines all screens, components (text inputs, dropdowns, date pickers, etc.), and navigation.  Meta validates the JSON on upload and returns any validation errors. See: https://developers.facebook.com/docs/whatsapp/flows/reference/flowjson 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        UploadWhatsAppFlowJsonRequest uploadWhatsAppFlowJsonRequest = new UploadWhatsAppFlowJsonRequest(); // UploadWhatsAppFlowJsonRequest | 
        try {
            UploadWhatsAppFlowJson200Response result = apiInstance.uploadWhatsAppFlowJson(flowId, uploadWhatsAppFlowJsonRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#uploadWhatsAppFlowJson");
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
| **flowId** | **String**| Flow ID | |
| **uploadWhatsAppFlowJsonRequest** | [**UploadWhatsAppFlowJsonRequest**](UploadWhatsAppFlowJsonRequest.md)|  | |

### Return type

[**UploadWhatsAppFlowJson200Response**](UploadWhatsAppFlowJson200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow JSON uploaded |  -  |
| **400** | Invalid JSON or flow is not in DRAFT status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## uploadWhatsAppFlowJsonWithHttpInfo

> ApiResponse<UploadWhatsAppFlowJson200Response> uploadWhatsAppFlowJson uploadWhatsAppFlowJsonWithHttpInfo(flowId, uploadWhatsAppFlowJsonRequest)

Upload flow JSON

Upload or update the Flow JSON for a DRAFT flow. The Flow JSON defines all screens, components (text inputs, dropdowns, date pickers, etc.), and navigation.  Meta validates the JSON on upload and returns any validation errors. See: https://developers.facebook.com/docs/whatsapp/flows/reference/flowjson 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppFlowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppFlowsApi apiInstance = new WhatsAppFlowsApi(defaultClient);
        String flowId = "flowId_example"; // String | Flow ID
        UploadWhatsAppFlowJsonRequest uploadWhatsAppFlowJsonRequest = new UploadWhatsAppFlowJsonRequest(); // UploadWhatsAppFlowJsonRequest | 
        try {
            ApiResponse<UploadWhatsAppFlowJson200Response> response = apiInstance.uploadWhatsAppFlowJsonWithHttpInfo(flowId, uploadWhatsAppFlowJsonRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppFlowsApi#uploadWhatsAppFlowJson");
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
| **flowId** | **String**| Flow ID | |
| **uploadWhatsAppFlowJsonRequest** | [**UploadWhatsAppFlowJsonRequest**](UploadWhatsAppFlowJsonRequest.md)|  | |

### Return type

ApiResponse<[**UploadWhatsAppFlowJson200Response**](UploadWhatsAppFlowJson200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flow JSON uploaded |  -  |
| **400** | Invalid JSON or flow is not in DRAFT status |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

