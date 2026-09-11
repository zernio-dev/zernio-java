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

Neither platform hard-deletes a form; this archives it (Meta status&#x3D;ARCHIVED; LinkedIn state&#x3D;ARCHIVED via PARTIAL_UPDATE). Meta forms must belong to the Page the accountId manages.

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
        String formId = "formId_example"; // String | Numeric form id (Meta leadgen_form id or LinkedIn leadForm id).
        String accountId = "accountId_example"; // String | Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile.
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
| **formId** | **String**| Numeric form id (Meta leadgen_form id or LinkedIn leadForm id). | |
| **accountId** | **String**| Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile. | |

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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | No lead form with that id on the Page this account manages. |  -  |

## archiveLeadFormWithHttpInfo

> ApiResponse<ArchiveLeadForm200Response> archiveLeadForm archiveLeadFormWithHttpInfo(formId, accountId)

Archive a lead form

Neither platform hard-deletes a form; this archives it (Meta status&#x3D;ARCHIVED; LinkedIn state&#x3D;ARCHIVED via PARTIAL_UPDATE). Meta forms must belong to the Page the accountId manages.

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
        String formId = "formId_example"; // String | Numeric form id (Meta leadgen_form id or LinkedIn leadForm id).
        String accountId = "accountId_example"; // String | Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile.
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
| **formId** | **String**| Numeric form id (Meta leadgen_form id or LinkedIn leadForm id). | |
| **accountId** | **String**| Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile. | |

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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | No lead form with that id on the Page this account manages. |  -  |


## createLeadForm

> CreateLeadForm200Response createLeadForm(createLeadFormRequest)

Create a lead form

Creates a Lead Gen form. The form content goes inside &#x60;platformSpecificData&#x60; for both platforms (the shape is selected by the accountId&#39;s platform). Meta: created on the connected Facebook Page (POST /{page-id}/leadgen_forms), where &#x60;accountId&#x60; may be the &#x60;metaads&#x60; ads connection (its Page comes from the Facebook account linked to the same profile) or the Facebook account itself; the old top-level Meta fields (questions, thankYou*, contextCard, …) are DEPRECATED but still accepted while platformSpecificData is absent; mixing both shapes is a 400. LinkedIn: created on the ad account&#39;s Company Page. NOT idempotent: a retry creates a second form. Meta prefilled question types (EMAIL, PHONE, FULL_NAME, …) must omit label/key; CUSTOM questions require both. LinkedIn exposes only free-text and multiple-choice questions via API (prefilled-from-profile fields are Campaign Manager UI-only). Requires the Ads add-on. 

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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |
| **422** | Meta rejected the lead form. Code 3 is Meta&#39;s generic app-capability error and does not name a field; when the request set isPhoneSmsVerifyEnabled, the response names that field as the one to drop first. |  -  |

## createLeadFormWithHttpInfo

> ApiResponse<CreateLeadForm200Response> createLeadForm createLeadFormWithHttpInfo(createLeadFormRequest)

Create a lead form

Creates a Lead Gen form. The form content goes inside &#x60;platformSpecificData&#x60; for both platforms (the shape is selected by the accountId&#39;s platform). Meta: created on the connected Facebook Page (POST /{page-id}/leadgen_forms), where &#x60;accountId&#x60; may be the &#x60;metaads&#x60; ads connection (its Page comes from the Facebook account linked to the same profile) or the Facebook account itself; the old top-level Meta fields (questions, thankYou*, contextCard, …) are DEPRECATED but still accepted while platformSpecificData is absent; mixing both shapes is a 400. LinkedIn: created on the ad account&#39;s Company Page. NOT idempotent: a retry creates a second form. Meta prefilled question types (EMAIL, PHONE, FULL_NAME, …) must omit label/key; CUSTOM questions require both. LinkedIn exposes only free-text and multiple-choice questions via API (prefilled-from-profile fields are Campaign Manager UI-only). Requires the Ads add-on. 

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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |
| **422** | Meta rejected the lead form. Code 3 is Meta&#39;s generic app-capability error and does not name a field; when the request set isPhoneSmsVerifyEnabled, the response names that field as the one to drop first. |  -  |


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
| **400** | Invalid request |  -  |
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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## getLeadForm

> GetLeadForm200Response getLeadForm(formId, accountId, fields)

Get a lead form

Returns the full form, including the thank-you page, so a form can be diffed against what was created. Meta forms are scoped to the Page the accountId manages: a form on any other Page is a 404, never a read. 

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
        String formId = "formId_example"; // String | Numeric form id (Meta leadgen_form id or LinkedIn leadForm id).
        String accountId = "accountId_example"; // String | Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile.
        String fields = "name,thank_you_page{title,body,button_type,website_url}"; // String | Meta only. A Graph field selection passed through verbatim to GET /{form-id}, replacing the default projection, so fields Meta adds later are reachable without an API change. Field names, commas and {} expansion only; anything else (Graph field modifiers such as .limit(), or characters that could open another query parameter) is a 400. Ownership of the form is verified before the selection runs, so this cannot reach any Page but the one accountId manages. Unknown field names are rejected by Meta as a 400. 
        try {
            GetLeadForm200Response result = apiInstance.getLeadForm(formId, accountId, fields);
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
| **formId** | **String**| Numeric form id (Meta leadgen_form id or LinkedIn leadForm id). | |
| **accountId** | **String**| Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile. | |
| **fields** | **String**| Meta only. A Graph field selection passed through verbatim to GET /{form-id}, replacing the default projection, so fields Meta adds later are reachable without an API change. Field names, commas and {} expansion only; anything else (Graph field modifiers such as .limit(), or characters that could open another query parameter) is a 400. Ownership of the form is verified before the selection runs, so this cannot reach any Page but the one accountId manages. Unknown field names are rejected by Meta as a 400.  | [optional] |

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
| **200** | Form metadata. Meta forms follow MetaLeadForm; LinkedIn forms return LinkedIn&#39;s own adForm shape. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | No lead form with that id on the Page this account manages. |  -  |

## getLeadFormWithHttpInfo

> ApiResponse<GetLeadForm200Response> getLeadForm getLeadFormWithHttpInfo(formId, accountId, fields)

Get a lead form

Returns the full form, including the thank-you page, so a form can be diffed against what was created. Meta forms are scoped to the Page the accountId manages: a form on any other Page is a 404, never a read. 

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
        String formId = "formId_example"; // String | Numeric form id (Meta leadgen_form id or LinkedIn leadForm id).
        String accountId = "accountId_example"; // String | Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile.
        String fields = "name,thank_you_page{title,body,button_type,website_url}"; // String | Meta only. A Graph field selection passed through verbatim to GET /{form-id}, replacing the default projection, so fields Meta adds later are reachable without an API change. Field names, commas and {} expansion only; anything else (Graph field modifiers such as .limit(), or characters that could open another query parameter) is a 400. Ownership of the form is verified before the selection runs, so this cannot reach any Page but the one accountId manages. Unknown field names are rejected by Meta as a 400. 
        try {
            ApiResponse<GetLeadForm200Response> response = apiInstance.getLeadFormWithHttpInfo(formId, accountId, fields);
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
| **formId** | **String**| Numeric form id (Meta leadgen_form id or LinkedIn leadForm id). | |
| **accountId** | **String**| Connected Meta ads, facebook or linkedin ads account id (selects the platform). A Meta ads connection resolves its Page through the Facebook account linked to the same profile. | |
| **fields** | **String**| Meta only. A Graph field selection passed through verbatim to GET /{form-id}, replacing the default projection, so fields Meta adds later are reachable without an API change. Field names, commas and {} expansion only; anything else (Graph field modifiers such as .limit(), or characters that could open another query parameter) is a 400. Ownership of the form is verified before the selection runs, so this cannot reach any Page but the one accountId manages. Unknown field names are rejected by Meta as a 400.  | [optional] |

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
| **200** | Form metadata. Meta forms follow MetaLeadForm; LinkedIn forms return LinkedIn&#39;s own adForm shape. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | No lead form with that id on the Page this account manages. |  -  |


## listFormLeads

> ListFormLeads200Response listFormLeads(formId, accountId, limit, cursor, since)

List leads for a single form

Returns leads for one form. Serves persisted leads (ingested via the leadgen webhook) when available, falling back to a live Graph read. Accepts a Facebook account or a metaads business-login account with leads_retrieval access to the form; the latter uses its system-user token without a posting parent. 

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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Leads for the form. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## listFormLeadsWithHttpInfo

> ApiResponse<ListFormLeads200Response> listFormLeads listFormLeadsWithHttpInfo(formId, accountId, limit, cursor, since)

List leads for a single form

Returns leads for one form. Serves persisted leads (ingested via the leadgen webhook) when available, falling back to a live Graph read. Accepts a Facebook account or a metaads business-login account with leads_retrieval access to the form; the latter uses its system-user token without a posting parent. 

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
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Leads for the form. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## listLeadForms

> ListLeadForms200Response listLeadForms(accountId, adAccountId, limit, cursor)

List lead forms

Lists the Lead Gen forms owned by the account. Meta: forms on the connected Facebook Page. Pass either the &#x60;metaads&#x60; ads connection (the Page is taken from the Facebook account linked to it) or the Facebook account itself. LinkedIn: forms owned by the ad account&#39;s Company Page. Pass &#x60;adAccountId&#x60; (LinkedIn forms are org-owned). Requires the Ads add-on. 

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
        String accountId = "accountId_example"; // String | Connected Meta ads, Facebook or LinkedIn ads account ID. A Meta ads connection resolves its Page through the Facebook account linked to the same profile.
        String adAccountId = "adAccountId_example"; // String | LinkedIn only: the LinkedIn ad account id (used to resolve the owning organization). Required for LinkedIn.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ListLeadForms200Response result = apiInstance.listLeadForms(accountId, adAccountId, limit, cursor);
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
| **accountId** | **String**| Connected Meta ads, Facebook or LinkedIn ads account ID. A Meta ads connection resolves its Page through the Facebook account linked to the same profile. | |
| **adAccountId** | **String**| LinkedIn only: the LinkedIn ad account id (used to resolve the owning organization). Required for LinkedIn. | [optional] |
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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

## listLeadFormsWithHttpInfo

> ApiResponse<ListLeadForms200Response> listLeadForms listLeadFormsWithHttpInfo(accountId, adAccountId, limit, cursor)

List lead forms

Lists the Lead Gen forms owned by the account. Meta: forms on the connected Facebook Page. Pass either the &#x60;metaads&#x60; ads connection (the Page is taken from the Facebook account linked to it) or the Facebook account itself. LinkedIn: forms owned by the ad account&#39;s Company Page. Pass &#x60;adAccountId&#x60; (LinkedIn forms are org-owned). Requires the Ads add-on. 

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
        String accountId = "accountId_example"; // String | Connected Meta ads, Facebook or LinkedIn ads account ID. A Meta ads connection resolves its Page through the Facebook account linked to the same profile.
        String adAccountId = "adAccountId_example"; // String | LinkedIn only: the LinkedIn ad account id (used to resolve the owning organization). Required for LinkedIn.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ApiResponse<ListLeadForms200Response> response = apiInstance.listLeadFormsWithHttpInfo(accountId, adAccountId, limit, cursor);
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
| **accountId** | **String**| Connected Meta ads, Facebook or LinkedIn ads account ID. A Meta ads connection resolves its Page through the Facebook account linked to the same profile. | |
| **adAccountId** | **String**| LinkedIn only: the LinkedIn ad account id (used to resolve the owning organization). Required for LinkedIn. | [optional] |
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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |


## listLeads

> ListLeads200Response listLeads(formId, accountId, adAccountId, limit, since, cursor)

List submitted leads

Returns submitted Lead Gen leads for your team, newest-first, with keyset pagination on &#x60;cursor&#x60;. For Meta (default) leads are served from the persisted cache, ingested in real time from the &#x60;leadgen&#x60; webhook. When &#x60;accountId&#x60; is a LinkedIn ads account, leads are fetched live from LinkedIn&#39;s &#x60;leadFormResponses&#x60; (LinkedIn has no webhook and enforces 90-day retention, so nothing is persisted) and &#x60;adAccountId&#x60; is required. Reading LinkedIn responses needs the &#x60;r_marketing_leadgen_automation&#x60; permission; accounts connected before it was added must reconnect. Requires the Ads add-on. 

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
        String accountId = "accountId_example"; // String | Filter to a single connected account. LinkedIn ads accounts switch to the live fetch.
        String adAccountId = "adAccountId_example"; // String | LinkedIn only: the LinkedIn ad account id whose responses to read (owner-scoped finder).
        Integer limit = 25; // Integer | 
        Integer since = 1757404800; // Integer | Unix seconds; only leads created at/after this timestamp. Millisecond timestamps return 400 with instructions to divide by 1000.
        String cursor = "cursor_example"; // String | Keyset cursor from a previous response's pagination.cursor (Meta: AdLead id; LinkedIn: numeric start offset).
        try {
            ListLeads200Response result = apiInstance.listLeads(formId, accountId, adAccountId, limit, since, cursor);
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
| **accountId** | **String**| Filter to a single connected account. LinkedIn ads accounts switch to the live fetch. | [optional] |
| **adAccountId** | **String**| LinkedIn only: the LinkedIn ad account id whose responses to read (owner-scoped finder). | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **Integer**| Unix seconds; only leads created at/after this timestamp. Millisecond timestamps return 400 with instructions to divide by 1000. | [optional] |
| **cursor** | **String**| Keyset cursor from a previous response&#39;s pagination.cursor (Meta: AdLead id; LinkedIn: numeric start offset). | [optional] |

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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## listLeadsWithHttpInfo

> ApiResponse<ListLeads200Response> listLeads listLeadsWithHttpInfo(formId, accountId, adAccountId, limit, since, cursor)

List submitted leads

Returns submitted Lead Gen leads for your team, newest-first, with keyset pagination on &#x60;cursor&#x60;. For Meta (default) leads are served from the persisted cache, ingested in real time from the &#x60;leadgen&#x60; webhook. When &#x60;accountId&#x60; is a LinkedIn ads account, leads are fetched live from LinkedIn&#39;s &#x60;leadFormResponses&#x60; (LinkedIn has no webhook and enforces 90-day retention, so nothing is persisted) and &#x60;adAccountId&#x60; is required. Reading LinkedIn responses needs the &#x60;r_marketing_leadgen_automation&#x60; permission; accounts connected before it was added must reconnect. Requires the Ads add-on. 

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
        String accountId = "accountId_example"; // String | Filter to a single connected account. LinkedIn ads accounts switch to the live fetch.
        String adAccountId = "adAccountId_example"; // String | LinkedIn only: the LinkedIn ad account id whose responses to read (owner-scoped finder).
        Integer limit = 25; // Integer | 
        Integer since = 1757404800; // Integer | Unix seconds; only leads created at/after this timestamp. Millisecond timestamps return 400 with instructions to divide by 1000.
        String cursor = "cursor_example"; // String | Keyset cursor from a previous response's pagination.cursor (Meta: AdLead id; LinkedIn: numeric start offset).
        try {
            ApiResponse<ListLeads200Response> response = apiInstance.listLeadsWithHttpInfo(formId, accountId, adAccountId, limit, since, cursor);
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
| **accountId** | **String**| Filter to a single connected account. LinkedIn ads accounts switch to the live fetch. | [optional] |
| **adAccountId** | **String**| LinkedIn only: the LinkedIn ad account id whose responses to read (owner-scoped finder). | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **Integer**| Unix seconds; only leads created at/after this timestamp. Millisecond timestamps return 400 with instructions to divide by 1000. | [optional] |
| **cursor** | **String**| Keyset cursor from a previous response&#39;s pagination.cursor (Meta: AdLead id; LinkedIn: numeric start offset). | [optional] |

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
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

