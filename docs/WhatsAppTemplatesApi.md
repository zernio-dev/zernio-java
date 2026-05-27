# WhatsAppTemplatesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWhatsAppLibraryTemplate**](WhatsAppTemplatesApi.md#getWhatsAppLibraryTemplate) | **GET** /v1/whatsapp/template-library | Look up a library template |
| [**getWhatsAppLibraryTemplateWithHttpInfo**](WhatsAppTemplatesApi.md#getWhatsAppLibraryTemplateWithHttpInfo) | **GET** /v1/whatsapp/template-library | Look up a library template |



## getWhatsAppLibraryTemplate

> GetWhatsAppLibraryTemplate200Response getWhatsAppLibraryTemplate(accountId, name)

Look up a library template

Look up a single pre-approved Template Library template by its exact name, to introspect its structure before importing it. Most importantly it returns the template&#39;s &#x60;buttons&#x60;: a library template with &#x60;URL&#x60; / &#x60;PHONE_NUMBER&#x60; buttons must be created with a matching &#x60;library_template_button_inputs&#x60; array (see Create Template), or Meta rejects it. Use this to discover which inputs to collect. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppTemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppTemplatesApi apiInstance = new WhatsAppTemplatesApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        String name = "name_example"; // String | Exact library template name
        try {
            GetWhatsAppLibraryTemplate200Response result = apiInstance.getWhatsAppLibraryTemplate(accountId, name);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppTemplatesApi#getWhatsAppLibraryTemplate");
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
| **name** | **String**| Exact library template name | |

### Return type

[**GetWhatsAppLibraryTemplate200Response**](GetWhatsAppLibraryTemplate200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Library template (or null if no exact match) |  -  |
| **400** | Missing or invalid query params |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppLibraryTemplateWithHttpInfo

> ApiResponse<GetWhatsAppLibraryTemplate200Response> getWhatsAppLibraryTemplate getWhatsAppLibraryTemplateWithHttpInfo(accountId, name)

Look up a library template

Look up a single pre-approved Template Library template by its exact name, to introspect its structure before importing it. Most importantly it returns the template&#39;s &#x60;buttons&#x60;: a library template with &#x60;URL&#x60; / &#x60;PHONE_NUMBER&#x60; buttons must be created with a matching &#x60;library_template_button_inputs&#x60; array (see Create Template), or Meta rejects it. Use this to discover which inputs to collect. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppTemplatesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppTemplatesApi apiInstance = new WhatsAppTemplatesApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        String name = "name_example"; // String | Exact library template name
        try {
            ApiResponse<GetWhatsAppLibraryTemplate200Response> response = apiInstance.getWhatsAppLibraryTemplateWithHttpInfo(accountId, name);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppTemplatesApi#getWhatsAppLibraryTemplate");
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
| **name** | **String**| Exact library template name | |

### Return type

ApiResponse<[**GetWhatsAppLibraryTemplate200Response**](GetWhatsAppLibraryTemplate200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Library template (or null if no exact match) |  -  |
| **400** | Missing or invalid query params |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

