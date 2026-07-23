# LeadGenApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**archiveLeadForm**](LeadGenApi.md#archiveLeadForm) | **DELETE** /v1/ads/lead-forms/{formId} | Archive a lead form |
| [**archiveLeadFormWithHttpInfo**](LeadGenApi.md#archiveLeadFormWithHttpInfo) | **DELETE** /v1/ads/lead-forms/{formId} | Archive a lead form |
| [**createLeadForm**](LeadGenApi.md#createLeadForm) | **POST** /v1/ads/lead-forms | Create a lead form |
| [**createLeadFormWithHttpInfo**](LeadGenApi.md#createLeadFormWithHttpInfo) | **POST** /v1/ads/lead-forms | Create a lead form |
| [**createTestLead**](LeadGenApi.md#createTestLead) | **POST** /v1/ads/lead-forms/{formId}/test-leads | Create a test lead |
| [**createTestLeadWithHttpInfo**](LeadGenApi.md#createTestLeadWithHttpInfo) | **POST** /v1/ads/lead-forms/{formId}/test-leads | Create a test lead |
| [**getLeadForm**](LeadGenApi.md#getLeadForm) | **GET** /v1/ads/lead-forms/{formId} | Get a lead form |
| [**getLeadFormWithHttpInfo**](LeadGenApi.md#getLeadFormWithHttpInfo) | **GET** /v1/ads/lead-forms/{formId} | Get a lead form |
| [**listFormLeads**](LeadGenApi.md#listFormLeads) | **GET** /v1/ads/lead-forms/{formId}/leads | List leads for a single form |
| [**listFormLeadsWithHttpInfo**](LeadGenApi.md#listFormLeadsWithHttpInfo) | **GET** /v1/ads/lead-forms/{formId}/leads | List leads for a single form |
| [**listLeadForms**](LeadGenApi.md#listLeadForms) | **GET** /v1/ads/lead-forms | List lead forms |
| [**listLeadFormsWithHttpInfo**](LeadGenApi.md#listLeadFormsWithHttpInfo) | **GET** /v1/ads/lead-forms | List lead forms |
| [**listLeads**](LeadGenApi.md#listLeads) | **GET** /v1/ads/leads | List submitted leads |
| [**listLeadsWithHttpInfo**](LeadGenApi.md#listLeadsWithHttpInfo) | **GET** /v1/ads/leads | List submitted leads |



## archiveLeadForm

> ArchiveLeadForm200Response archiveLeadForm(formId, accountId)

Archive a lead form

Meta has no hard delete for forms; this archives the form (status&#x3D;ARCHIVED).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ArchiveLeadForm200Response result = apiInstance.archiveLeadForm(formId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#archiveLeadForm");
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
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**ArchiveLeadForm200Response**](ArchiveLeadForm200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archived. |  -  |
| **401** | Unauthorized |  -  |

## archiveLeadFormWithHttpInfo

> ApiResponse<ArchiveLeadForm200Response> archiveLeadForm archiveLeadFormWithHttpInfo(formId, accountId)

Archive a lead form

Meta has no hard delete for forms; this archives the form (status&#x3D;ARCHIVED).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<ArchiveLeadForm200Response> response = apiInstance.archiveLeadFormWithHttpInfo(formId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#archiveLeadForm");
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
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**ArchiveLeadForm200Response**](ArchiveLeadForm200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archived. |  -  |
| **401** | Unauthorized |  -  |


## createLeadForm

> CreateLeadForm200Response createLeadForm(createLeadFormRequest)

Create a lead form

Creates a Lead Gen form on the connected Facebook Page (POST /{page-id}/leadgen_forms). NOT idempotent — a retry creates a second form. Prefilled question types (EMAIL, PHONE, FULL_NAME, …) must omit label/key; CUSTOM questions require both. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        CreateLeadFormRequest createLeadFormRequest = new CreateLeadFormRequest(); // CreateLeadFormRequest | 
        try {
            CreateLeadForm200Response result = apiInstance.createLeadForm(createLeadFormRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#createLeadForm");
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
| **createLeadFormRequest** | [**CreateLeadFormRequest**](CreateLeadFormRequest.md)|  | |

### Return type

[**CreateLeadForm200Response**](CreateLeadForm200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created form. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

## createLeadFormWithHttpInfo

> ApiResponse<CreateLeadForm200Response> createLeadForm createLeadFormWithHttpInfo(createLeadFormRequest)

Create a lead form

Creates a Lead Gen form on the connected Facebook Page (POST /{page-id}/leadgen_forms). NOT idempotent — a retry creates a second form. Prefilled question types (EMAIL, PHONE, FULL_NAME, …) must omit label/key; CUSTOM questions require both. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        CreateLeadFormRequest createLeadFormRequest = new CreateLeadFormRequest(); // CreateLeadFormRequest | 
        try {
            ApiResponse<CreateLeadForm200Response> response = apiInstance.createLeadFormWithHttpInfo(createLeadFormRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#createLeadForm");
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
| **createLeadFormRequest** | [**CreateLeadFormRequest**](CreateLeadFormRequest.md)|  | |

### Return type

ApiResponse<[**CreateLeadForm200Response**](CreateLeadForm200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created form. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |


## createTestLead

> CreateTestLead200Response createTestLead(formId, createTestLeadRequest)

Create a test lead

Submits a test lead against the form (POST /{form-id}/test_leads) to exercise retrieval without waiting for real ad impressions. Meta allows one test lead per form at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        CreateTestLeadRequest createTestLeadRequest = new CreateTestLeadRequest(); // CreateTestLeadRequest | 
        try {
            CreateTestLead200Response result = apiInstance.createTestLead(formId, createTestLeadRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#createTestLead");
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
| **formId** | **String**|  | |
| **createTestLeadRequest** | [**CreateTestLeadRequest**](CreateTestLeadRequest.md)|  | |

### Return type

[**CreateTestLead200Response**](CreateTestLead200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test lead created. |  -  |
| **401** | Unauthorized |  -  |

## createTestLeadWithHttpInfo

> ApiResponse<CreateTestLead200Response> createTestLead createTestLeadWithHttpInfo(formId, createTestLeadRequest)

Create a test lead

Submits a test lead against the form (POST /{form-id}/test_leads) to exercise retrieval without waiting for real ad impressions. Meta allows one test lead per form at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        CreateTestLeadRequest createTestLeadRequest = new CreateTestLeadRequest(); // CreateTestLeadRequest | 
        try {
            ApiResponse<CreateTestLead200Response> response = apiInstance.createTestLeadWithHttpInfo(formId, createTestLeadRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#createTestLead");
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
| **formId** | **String**|  | |
| **createTestLeadRequest** | [**CreateTestLeadRequest**](CreateTestLeadRequest.md)|  | |

### Return type

ApiResponse<[**CreateTestLead200Response**](CreateTestLead200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test lead created. |  -  |
| **401** | Unauthorized |  -  |


## getLeadForm

> GetLeadForm200Response getLeadForm(formId, accountId)

Get a lead form

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            GetLeadForm200Response result = apiInstance.getLeadForm(formId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#getLeadForm");
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
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**GetLeadForm200Response**](GetLeadForm200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form metadata. |  -  |
| **401** | Unauthorized |  -  |

## getLeadFormWithHttpInfo

> ApiResponse<GetLeadForm200Response> getLeadForm getLeadFormWithHttpInfo(formId, accountId)

Get a lead form

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetLeadForm200Response> response = apiInstance.getLeadFormWithHttpInfo(formId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#getLeadForm");
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
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**GetLeadForm200Response**](GetLeadForm200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form metadata. |  -  |
| **401** | Unauthorized |  -  |


## listFormLeads

> ListFormLeads200Response listFormLeads(formId, accountId, limit, cursor, since)

List leads for a single form

Returns leads for one form. Serves persisted leads (ingested via the leadgen webhook) when available, falling back to a live Graph read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        Integer since = 56; // Integer | Unix seconds.
        try {
            ListFormLeads200Response result = apiInstance.listFormLeads(formId, accountId, limit, cursor, since);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#listFormLeads");
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
| **formId** | **String**|  | |
| **accountId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |
| **since** | **Integer**| Unix seconds. | [optional] |

### Return type

[**ListFormLeads200Response**](ListFormLeads200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Leads for the form. |  -  |
| **401** | Unauthorized |  -  |

## listFormLeadsWithHttpInfo

> ApiResponse<ListFormLeads200Response> listFormLeads listFormLeadsWithHttpInfo(formId, accountId, limit, cursor, since)

List leads for a single form

Returns leads for one form. Serves persisted leads (ingested via the leadgen webhook) when available, falling back to a live Graph read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        Integer since = 56; // Integer | Unix seconds.
        try {
            ApiResponse<ListFormLeads200Response> response = apiInstance.listFormLeadsWithHttpInfo(formId, accountId, limit, cursor, since);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#listFormLeads");
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
| **formId** | **String**|  | |
| **accountId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |
| **since** | **Integer**| Unix seconds. | [optional] |

### Return type

ApiResponse<[**ListFormLeads200Response**](ListFormLeads200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Leads for the form. |  -  |
| **401** | Unauthorized |  -  |


## listLeadForms

> ListLeadForms200Response listLeadForms(accountId, limit, cursor)

List lead forms

Lists the Lead Gen forms owned by the connected Facebook Page. Requires the Ads add-on.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected facebook account id.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ListLeadForms200Response result = apiInstance.listLeadForms(accountId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#listLeadForms");
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
| **accountId** | **String**| Connected facebook account id. | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |

### Return type

[**ListLeadForms200Response**](ListLeadForms200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forms list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

## listLeadFormsWithHttpInfo

> ApiResponse<ListLeadForms200Response> listLeadForms listLeadFormsWithHttpInfo(accountId, limit, cursor)

List lead forms

Lists the Lead Gen forms owned by the connected Facebook Page. Requires the Ads add-on.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected facebook account id.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ApiResponse<ListLeadForms200Response> response = apiInstance.listLeadFormsWithHttpInfo(accountId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#listLeadForms");
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
| **accountId** | **String**| Connected facebook account id. | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListLeadForms200Response**](ListLeadForms200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forms list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |


## listLeads

> ListLeads200Response listLeads(formId, accountId, limit, since, cursor)

List submitted leads

Returns persisted Meta Lead Gen leads for your team, newest-first, with keyset pagination on &#x60;cursor&#x60;. Leads are ingested in real time from the &#x60;leadgen&#x60; webhook. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | Filter to a single lead form.
        String accountId = "accountId_example"; // String | Filter to a single connected account.
        Integer limit = 25; // Integer | 
        Integer since = 56; // Integer | Unix seconds; only leads created at/after this Meta timestamp.
        String cursor = "cursor_example"; // String | Keyset cursor from a previous response's pagination.cursor.
        try {
            ListLeads200Response result = apiInstance.listLeads(formId, accountId, limit, since, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#listLeads");
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
| **formId** | **String**| Filter to a single lead form. | [optional] |
| **accountId** | **String**| Filter to a single connected account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **Integer**| Unix seconds; only leads created at/after this Meta timestamp. | [optional] |
| **cursor** | **String**| Keyset cursor from a previous response&#39;s pagination.cursor. | [optional] |

### Return type

[**ListLeads200Response**](ListLeads200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lead list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

## listLeadsWithHttpInfo

> ApiResponse<ListLeads200Response> listLeads listLeadsWithHttpInfo(formId, accountId, limit, since, cursor)

List submitted leads

Returns persisted Meta Lead Gen leads for your team, newest-first, with keyset pagination on &#x60;cursor&#x60;. Leads are ingested in real time from the &#x60;leadgen&#x60; webhook. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.LeadGenApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        LeadGenApi apiInstance = new LeadGenApi(defaultClient);
        String formId = "formId_example"; // String | Filter to a single lead form.
        String accountId = "accountId_example"; // String | Filter to a single connected account.
        Integer limit = 25; // Integer | 
        Integer since = 56; // Integer | Unix seconds; only leads created at/after this Meta timestamp.
        String cursor = "cursor_example"; // String | Keyset cursor from a previous response's pagination.cursor.
        try {
            ApiResponse<ListLeads200Response> response = apiInstance.listLeadsWithHttpInfo(formId, accountId, limit, since, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling LeadGenApi#listLeads");
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
| **formId** | **String**| Filter to a single lead form. | [optional] |
| **accountId** | **String**| Filter to a single connected account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **Integer**| Unix seconds; only leads created at/after this Meta timestamp. | [optional] |
| **cursor** | **String**| Keyset cursor from a previous response&#39;s pagination.cursor. | [optional] |

### Return type

ApiResponse<[**ListLeads200Response**](ListLeads200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lead list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

