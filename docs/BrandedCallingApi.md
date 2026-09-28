# BrandedCallingApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attachBrandedCallingNumbers**](BrandedCallingApi.md#attachBrandedCallingNumbers) | **POST** /v1/branded-calling/identities/{id}/numbers | Attach numbers to a verified identity |
| [**attachBrandedCallingNumbersWithHttpInfo**](BrandedCallingApi.md#attachBrandedCallingNumbersWithHttpInfo) | **POST** /v1/branded-calling/identities/{id}/numbers | Attach numbers to a verified identity |
| [**confirmBrandedCallingAuthorizerEmail**](BrandedCallingApi.md#confirmBrandedCallingAuthorizerEmail) | **POST** /v1/branded-calling/identities/{id}/verify-email/confirm | Confirm the authorizer&#39;s code |
| [**confirmBrandedCallingAuthorizerEmailWithHttpInfo**](BrandedCallingApi.md#confirmBrandedCallingAuthorizerEmailWithHttpInfo) | **POST** /v1/branded-calling/identities/{id}/verify-email/confirm | Confirm the authorizer&#39;s code |
| [**createBrandedCallingEnterprise**](BrandedCallingApi.md#createBrandedCallingEnterprise) | **POST** /v1/branded-calling/enterprises | Register a business for Branded Calling |
| [**createBrandedCallingEnterpriseWithHttpInfo**](BrandedCallingApi.md#createBrandedCallingEnterpriseWithHttpInfo) | **POST** /v1/branded-calling/enterprises | Register a business for Branded Calling |
| [**createBrandedCallingIdentity**](BrandedCallingApi.md#createBrandedCallingIdentity) | **POST** /v1/branded-calling/identities | Create a caller identity |
| [**createBrandedCallingIdentityWithHttpInfo**](BrandedCallingApi.md#createBrandedCallingIdentityWithHttpInfo) | **POST** /v1/branded-calling/identities | Create a caller identity |
| [**deleteBrandedCallingEnterprise**](BrandedCallingApi.md#deleteBrandedCallingEnterprise) | **DELETE** /v1/branded-calling/enterprises/{id} | Delete a registered business |
| [**deleteBrandedCallingEnterpriseWithHttpInfo**](BrandedCallingApi.md#deleteBrandedCallingEnterpriseWithHttpInfo) | **DELETE** /v1/branded-calling/enterprises/{id} | Delete a registered business |
| [**deleteBrandedCallingIdentity**](BrandedCallingApi.md#deleteBrandedCallingIdentity) | **DELETE** /v1/branded-calling/identities/{id} | Delete a caller identity |
| [**deleteBrandedCallingIdentityWithHttpInfo**](BrandedCallingApi.md#deleteBrandedCallingIdentityWithHttpInfo) | **DELETE** /v1/branded-calling/identities/{id} | Delete a caller identity |
| [**detachBrandedCallingNumbers**](BrandedCallingApi.md#detachBrandedCallingNumbers) | **DELETE** /v1/branded-calling/identities/{id}/numbers | Detach numbers from an identity |
| [**detachBrandedCallingNumbersWithHttpInfo**](BrandedCallingApi.md#detachBrandedCallingNumbersWithHttpInfo) | **DELETE** /v1/branded-calling/identities/{id}/numbers | Detach numbers from an identity |
| [**getBrandedCallingEnterprise**](BrandedCallingApi.md#getBrandedCallingEnterprise) | **GET** /v1/branded-calling/enterprises/{id} | Get a registered business |
| [**getBrandedCallingEnterpriseWithHttpInfo**](BrandedCallingApi.md#getBrandedCallingEnterpriseWithHttpInfo) | **GET** /v1/branded-calling/enterprises/{id} | Get a registered business |
| [**getBrandedCallingIdentity**](BrandedCallingApi.md#getBrandedCallingIdentity) | **GET** /v1/branded-calling/identities/{id} | Get a caller identity |
| [**getBrandedCallingIdentityWithHttpInfo**](BrandedCallingApi.md#getBrandedCallingIdentityWithHttpInfo) | **GET** /v1/branded-calling/identities/{id} | Get a caller identity |
| [**listBrandedCallingCallReasons**](BrandedCallingApi.md#listBrandedCallingCallReasons) | **GET** /v1/branded-calling/call-reasons | List pre-approved call reasons |
| [**listBrandedCallingCallReasonsWithHttpInfo**](BrandedCallingApi.md#listBrandedCallingCallReasonsWithHttpInfo) | **GET** /v1/branded-calling/call-reasons | List pre-approved call reasons |
| [**listBrandedCallingEnterprises**](BrandedCallingApi.md#listBrandedCallingEnterprises) | **GET** /v1/branded-calling/enterprises | List registered businesses |
| [**listBrandedCallingEnterprisesWithHttpInfo**](BrandedCallingApi.md#listBrandedCallingEnterprisesWithHttpInfo) | **GET** /v1/branded-calling/enterprises | List registered businesses |
| [**listBrandedCallingIdentities**](BrandedCallingApi.md#listBrandedCallingIdentities) | **GET** /v1/branded-calling/identities | List caller identities |
| [**listBrandedCallingIdentitiesWithHttpInfo**](BrandedCallingApi.md#listBrandedCallingIdentitiesWithHttpInfo) | **GET** /v1/branded-calling/identities | List caller identities |
| [**listBrandedCallingIdentityNumbers**](BrandedCallingApi.md#listBrandedCallingIdentityNumbers) | **GET** /v1/branded-calling/identities/{id}/numbers | List the numbers on a caller identity |
| [**listBrandedCallingIdentityNumbersWithHttpInfo**](BrandedCallingApi.md#listBrandedCallingIdentityNumbersWithHttpInfo) | **GET** /v1/branded-calling/identities/{id}/numbers | List the numbers on a caller identity |
| [**resendBrandedCallingAuthorizerCode**](BrandedCallingApi.md#resendBrandedCallingAuthorizerCode) | **POST** /v1/branded-calling/identities/{id}/verify-email | Resend the authorizer&#39;s code |
| [**resendBrandedCallingAuthorizerCodeWithHttpInfo**](BrandedCallingApi.md#resendBrandedCallingAuthorizerCodeWithHttpInfo) | **POST** /v1/branded-calling/identities/{id}/verify-email | Resend the authorizer&#39;s code |
| [**updateBrandedCallingIdentity**](BrandedCallingApi.md#updateBrandedCallingIdentity) | **PATCH** /v1/branded-calling/identities/{id} | Edit or resubmit a caller identity |
| [**updateBrandedCallingIdentityWithHttpInfo**](BrandedCallingApi.md#updateBrandedCallingIdentityWithHttpInfo) | **PATCH** /v1/branded-calling/identities/{id} | Edit or resubmit a caller identity |



## attachBrandedCallingNumbers

> ListBrandedCallingIdentityNumbers200Response attachBrandedCallingNumbers(id, attachBrandedCallingNumbersRequest)

Attach numbers to a verified identity

Files a Letter of Authorization signed by you (Zernio is named as the authorized agent managing the numbers) and opens a vetting batch of up to 15 US numbers you own. The batch is all-or-nothing: one ineligible number refuses the whole call. Each number shows the identity once its own status reaches &#x60;verified&#x60;. A number belongs to one identity at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        AttachBrandedCallingNumbersRequest attachBrandedCallingNumbersRequest = new AttachBrandedCallingNumbersRequest(); // AttachBrandedCallingNumbersRequest | 
        try {
            ListBrandedCallingIdentityNumbers200Response result = apiInstance.attachBrandedCallingNumbers(id, attachBrandedCallingNumbersRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#attachBrandedCallingNumbers");
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
| **id** | **String**|  | |
| **attachBrandedCallingNumbersRequest** | [**AttachBrandedCallingNumbersRequest**](AttachBrandedCallingNumbersRequest.md)|  | |

### Return type

[**ListBrandedCallingIdentityNumbers200Response**](ListBrandedCallingIdentityNumbers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Batch opened. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity or phone number not found |  -  |
| **409** | The identity is not verified yet, or a number already belongs to an identity (code invalid_resource_state). |  -  |
| **422** | A number is not a US number or not active, or the carrier refused the batch (the message names the number). |  -  |

## attachBrandedCallingNumbersWithHttpInfo

> ApiResponse<ListBrandedCallingIdentityNumbers200Response> attachBrandedCallingNumbers attachBrandedCallingNumbersWithHttpInfo(id, attachBrandedCallingNumbersRequest)

Attach numbers to a verified identity

Files a Letter of Authorization signed by you (Zernio is named as the authorized agent managing the numbers) and opens a vetting batch of up to 15 US numbers you own. The batch is all-or-nothing: one ineligible number refuses the whole call. Each number shows the identity once its own status reaches &#x60;verified&#x60;. A number belongs to one identity at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        AttachBrandedCallingNumbersRequest attachBrandedCallingNumbersRequest = new AttachBrandedCallingNumbersRequest(); // AttachBrandedCallingNumbersRequest | 
        try {
            ApiResponse<ListBrandedCallingIdentityNumbers200Response> response = apiInstance.attachBrandedCallingNumbersWithHttpInfo(id, attachBrandedCallingNumbersRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#attachBrandedCallingNumbers");
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
| **id** | **String**|  | |
| **attachBrandedCallingNumbersRequest** | [**AttachBrandedCallingNumbersRequest**](AttachBrandedCallingNumbersRequest.md)|  | |

### Return type

ApiResponse<[**ListBrandedCallingIdentityNumbers200Response**](ListBrandedCallingIdentityNumbers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Batch opened. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity or phone number not found |  -  |
| **409** | The identity is not verified yet, or a number already belongs to an identity (code invalid_resource_state). |  -  |
| **422** | A number is not a US number or not active, or the carrier refused the batch (the message names the number). |  -  |


## confirmBrandedCallingAuthorizerEmail

> BrandedCallingIdentity confirmBrandedCallingAuthorizerEmail(id, confirmBrandedCallingAuthorizerEmailRequest)

Confirm the authorizer&#39;s code

The last customer step. On success the stored references are filed and the identity is submitted to carrier vetting in the same call (&#x60;in_review&#x60;). If a later step fails the identity stays &#x60;pending_email_verification&#x60; with the email already verified; calling again resumes from that step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        ConfirmBrandedCallingAuthorizerEmailRequest confirmBrandedCallingAuthorizerEmailRequest = new ConfirmBrandedCallingAuthorizerEmailRequest(); // ConfirmBrandedCallingAuthorizerEmailRequest | 
        try {
            BrandedCallingIdentity result = apiInstance.confirmBrandedCallingAuthorizerEmail(id, confirmBrandedCallingAuthorizerEmailRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#confirmBrandedCallingAuthorizerEmail");
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
| **id** | **String**|  | |
| **confirmBrandedCallingAuthorizerEmailRequest** | [**ConfirmBrandedCallingAuthorizerEmailRequest**](ConfirmBrandedCallingAuthorizerEmailRequest.md)|  | |

### Return type

[**BrandedCallingIdentity**](BrandedCallingIdentity.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The identity, now in carrier vetting. |  -  |
| **400** | The code is wrong or expired (param code), or the body is invalid. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | The identity is not waiting for a code (code invalid_resource_state). |  -  |

## confirmBrandedCallingAuthorizerEmailWithHttpInfo

> ApiResponse<BrandedCallingIdentity> confirmBrandedCallingAuthorizerEmail confirmBrandedCallingAuthorizerEmailWithHttpInfo(id, confirmBrandedCallingAuthorizerEmailRequest)

Confirm the authorizer&#39;s code

The last customer step. On success the stored references are filed and the identity is submitted to carrier vetting in the same call (&#x60;in_review&#x60;). If a later step fails the identity stays &#x60;pending_email_verification&#x60; with the email already verified; calling again resumes from that step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        ConfirmBrandedCallingAuthorizerEmailRequest confirmBrandedCallingAuthorizerEmailRequest = new ConfirmBrandedCallingAuthorizerEmailRequest(); // ConfirmBrandedCallingAuthorizerEmailRequest | 
        try {
            ApiResponse<BrandedCallingIdentity> response = apiInstance.confirmBrandedCallingAuthorizerEmailWithHttpInfo(id, confirmBrandedCallingAuthorizerEmailRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#confirmBrandedCallingAuthorizerEmail");
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
| **id** | **String**|  | |
| **confirmBrandedCallingAuthorizerEmailRequest** | [**ConfirmBrandedCallingAuthorizerEmailRequest**](ConfirmBrandedCallingAuthorizerEmailRequest.md)|  | |

### Return type

ApiResponse<[**BrandedCallingIdentity**](BrandedCallingIdentity.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The identity, now in carrier vetting. |  -  |
| **400** | The code is wrong or expired (param code), or the body is invalid. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | The identity is not waiting for a code (code invalid_resource_state). |  -  |


## createBrandedCallingEnterprise

> BrandedCallingEnterprise createBrandedCallingEnterprise(createBrandedCallingEnterpriseRequest)

Register a business for Branded Calling

Stores the legal entity behind your caller identities. Nothing is filed with the carrier until the business&#39;s first identity passes review. Only businesses registered in the US or Canada qualify (a FEIN or Canadian equivalent is required); any other country returns &#x60;422&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        CreateBrandedCallingEnterpriseRequest createBrandedCallingEnterpriseRequest = new CreateBrandedCallingEnterpriseRequest(); // CreateBrandedCallingEnterpriseRequest | 
        try {
            BrandedCallingEnterprise result = apiInstance.createBrandedCallingEnterprise(createBrandedCallingEnterpriseRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#createBrandedCallingEnterprise");
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
| **createBrandedCallingEnterpriseRequest** | [**CreateBrandedCallingEnterpriseRequest**](CreateBrandedCallingEnterpriseRequest.md)|  | |

### Return type

[**BrandedCallingEnterprise**](BrandedCallingEnterprise.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Business stored. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **422** | The business is not registered in the US or Canada (code feature_not_available). |  -  |

## createBrandedCallingEnterpriseWithHttpInfo

> ApiResponse<BrandedCallingEnterprise> createBrandedCallingEnterprise createBrandedCallingEnterpriseWithHttpInfo(createBrandedCallingEnterpriseRequest)

Register a business for Branded Calling

Stores the legal entity behind your caller identities. Nothing is filed with the carrier until the business&#39;s first identity passes review. Only businesses registered in the US or Canada qualify (a FEIN or Canadian equivalent is required); any other country returns &#x60;422&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        CreateBrandedCallingEnterpriseRequest createBrandedCallingEnterpriseRequest = new CreateBrandedCallingEnterpriseRequest(); // CreateBrandedCallingEnterpriseRequest | 
        try {
            ApiResponse<BrandedCallingEnterprise> response = apiInstance.createBrandedCallingEnterpriseWithHttpInfo(createBrandedCallingEnterpriseRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#createBrandedCallingEnterprise");
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
| **createBrandedCallingEnterpriseRequest** | [**CreateBrandedCallingEnterpriseRequest**](CreateBrandedCallingEnterpriseRequest.md)|  | |

### Return type

ApiResponse<[**BrandedCallingEnterprise**](BrandedCallingEnterprise.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Business stored. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **422** | The business is not registered in the US or Canada (code feature_not_available). |  -  |


## createBrandedCallingIdentity

> BrandedCallingIdentity createBrandedCallingIdentity(createBrandedCallingIdentityRequest)

Create a caller identity

A caller identity is what the callee sees: display name, logo and call reasons, backed by a registered business and three references the carrier vetting team phones. It starts in Zernio review (&#x60;requested&#x60;). Once approved, the carrier emails the authorizer a 6-digit code; confirm it with the verify-email endpoint and the identity goes into carrier vetting on its own. Track it with &#x60;GET&#x60; or the &#x60;branded_calling.identity.status_updated&#x60; webhook.  Billing: $100 per identity per month, the first month charged when the identity is filed with the carrier and not refunded if the carrier rejects it, then monthly while the identity exists. Branded calls add $0.10 each. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        CreateBrandedCallingIdentityRequest createBrandedCallingIdentityRequest = new CreateBrandedCallingIdentityRequest(); // CreateBrandedCallingIdentityRequest | 
        try {
            BrandedCallingIdentity result = apiInstance.createBrandedCallingIdentity(createBrandedCallingIdentityRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#createBrandedCallingIdentity");
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
| **createBrandedCallingIdentityRequest** | [**CreateBrandedCallingIdentityRequest**](CreateBrandedCallingIdentityRequest.md)|  | |

### Return type

[**BrandedCallingIdentity**](BrandedCallingIdentity.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Identity created, in review. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Usage-based billing is required (code usage_billing_required). |  -  |
| **404** | Business not found |  -  |
| **422** | The logo could not be downloaded or is not an image. |  -  |

## createBrandedCallingIdentityWithHttpInfo

> ApiResponse<BrandedCallingIdentity> createBrandedCallingIdentity createBrandedCallingIdentityWithHttpInfo(createBrandedCallingIdentityRequest)

Create a caller identity

A caller identity is what the callee sees: display name, logo and call reasons, backed by a registered business and three references the carrier vetting team phones. It starts in Zernio review (&#x60;requested&#x60;). Once approved, the carrier emails the authorizer a 6-digit code; confirm it with the verify-email endpoint and the identity goes into carrier vetting on its own. Track it with &#x60;GET&#x60; or the &#x60;branded_calling.identity.status_updated&#x60; webhook.  Billing: $100 per identity per month, the first month charged when the identity is filed with the carrier and not refunded if the carrier rejects it, then monthly while the identity exists. Branded calls add $0.10 each. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        CreateBrandedCallingIdentityRequest createBrandedCallingIdentityRequest = new CreateBrandedCallingIdentityRequest(); // CreateBrandedCallingIdentityRequest | 
        try {
            ApiResponse<BrandedCallingIdentity> response = apiInstance.createBrandedCallingIdentityWithHttpInfo(createBrandedCallingIdentityRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#createBrandedCallingIdentity");
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
| **createBrandedCallingIdentityRequest** | [**CreateBrandedCallingIdentityRequest**](CreateBrandedCallingIdentityRequest.md)|  | |

### Return type

ApiResponse<[**BrandedCallingIdentity**](BrandedCallingIdentity.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Identity created, in review. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Usage-based billing is required (code usage_billing_required). |  -  |
| **404** | Business not found |  -  |
| **422** | The logo could not be downloaded or is not an image. |  -  |


## deleteBrandedCallingEnterprise

> DeleteBrandedCallingEnterprise200Response deleteBrandedCallingEnterprise(id)

Delete a registered business

Refused while the business still has caller identities (delete those first).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            DeleteBrandedCallingEnterprise200Response result = apiInstance.deleteBrandedCallingEnterprise(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#deleteBrandedCallingEnterprise");
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
| **id** | **String**|  | |

### Return type

[**DeleteBrandedCallingEnterprise200Response**](DeleteBrandedCallingEnterprise200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Business not found |  -  |
| **409** | The business still has caller identities (code invalid_resource_state). |  -  |

## deleteBrandedCallingEnterpriseWithHttpInfo

> ApiResponse<DeleteBrandedCallingEnterprise200Response> deleteBrandedCallingEnterprise deleteBrandedCallingEnterpriseWithHttpInfo(id)

Delete a registered business

Refused while the business still has caller identities (delete those first).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<DeleteBrandedCallingEnterprise200Response> response = apiInstance.deleteBrandedCallingEnterpriseWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#deleteBrandedCallingEnterprise");
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
| **id** | **String**|  | |

### Return type

ApiResponse<[**DeleteBrandedCallingEnterprise200Response**](DeleteBrandedCallingEnterprise200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Business not found |  -  |
| **409** | The business still has caller identities (code invalid_resource_state). |  -  |


## deleteBrandedCallingIdentity

> DeleteBrandedCallingEnterprise200Response deleteBrandedCallingIdentity(id)

Delete a caller identity

Detaches its numbers and removes the identity at the carrier, which ends the monthly fee. Refused while an infringement claim is open.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            DeleteBrandedCallingEnterprise200Response result = apiInstance.deleteBrandedCallingIdentity(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#deleteBrandedCallingIdentity");
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
| **id** | **String**|  | |

### Return type

[**DeleteBrandedCallingEnterprise200Response**](DeleteBrandedCallingEnterprise200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | An infringement claim is open on this identity (code invalid_resource_state). |  -  |

## deleteBrandedCallingIdentityWithHttpInfo

> ApiResponse<DeleteBrandedCallingEnterprise200Response> deleteBrandedCallingIdentity deleteBrandedCallingIdentityWithHttpInfo(id)

Delete a caller identity

Detaches its numbers and removes the identity at the carrier, which ends the monthly fee. Refused while an infringement claim is open.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<DeleteBrandedCallingEnterprise200Response> response = apiInstance.deleteBrandedCallingIdentityWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#deleteBrandedCallingIdentity");
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
| **id** | **String**|  | |

### Return type

ApiResponse<[**DeleteBrandedCallingEnterprise200Response**](DeleteBrandedCallingEnterprise200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | An infringement claim is open on this identity (code invalid_resource_state). |  -  |


## detachBrandedCallingNumbers

> DetachBrandedCallingNumbers200Response detachBrandedCallingNumbers(id, detachBrandedCallingNumbersRequest)

Detach numbers from an identity

Deregisters the numbers at the carrier and frees them for another identity. Up to 100 per call.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        DetachBrandedCallingNumbersRequest detachBrandedCallingNumbersRequest = new DetachBrandedCallingNumbersRequest(); // DetachBrandedCallingNumbersRequest | 
        try {
            DetachBrandedCallingNumbers200Response result = apiInstance.detachBrandedCallingNumbers(id, detachBrandedCallingNumbersRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#detachBrandedCallingNumbers");
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
| **id** | **String**|  | |
| **detachBrandedCallingNumbersRequest** | [**DetachBrandedCallingNumbersRequest**](DetachBrandedCallingNumbersRequest.md)|  | |

### Return type

[**DetachBrandedCallingNumbers200Response**](DetachBrandedCallingNumbers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Numbers detached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found, or none of the numbers is attached to it |  -  |

## detachBrandedCallingNumbersWithHttpInfo

> ApiResponse<DetachBrandedCallingNumbers200Response> detachBrandedCallingNumbers detachBrandedCallingNumbersWithHttpInfo(id, detachBrandedCallingNumbersRequest)

Detach numbers from an identity

Deregisters the numbers at the carrier and frees them for another identity. Up to 100 per call.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        DetachBrandedCallingNumbersRequest detachBrandedCallingNumbersRequest = new DetachBrandedCallingNumbersRequest(); // DetachBrandedCallingNumbersRequest | 
        try {
            ApiResponse<DetachBrandedCallingNumbers200Response> response = apiInstance.detachBrandedCallingNumbersWithHttpInfo(id, detachBrandedCallingNumbersRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#detachBrandedCallingNumbers");
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
| **id** | **String**|  | |
| **detachBrandedCallingNumbersRequest** | [**DetachBrandedCallingNumbersRequest**](DetachBrandedCallingNumbersRequest.md)|  | |

### Return type

ApiResponse<[**DetachBrandedCallingNumbers200Response**](DetachBrandedCallingNumbers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Numbers detached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found, or none of the numbers is attached to it |  -  |


## getBrandedCallingEnterprise

> BrandedCallingEnterprise getBrandedCallingEnterprise(id)

Get a registered business

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            BrandedCallingEnterprise result = apiInstance.getBrandedCallingEnterprise(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#getBrandedCallingEnterprise");
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
| **id** | **String**|  | |

### Return type

[**BrandedCallingEnterprise**](BrandedCallingEnterprise.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The business. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Business not found |  -  |

## getBrandedCallingEnterpriseWithHttpInfo

> ApiResponse<BrandedCallingEnterprise> getBrandedCallingEnterprise getBrandedCallingEnterpriseWithHttpInfo(id)

Get a registered business

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<BrandedCallingEnterprise> response = apiInstance.getBrandedCallingEnterpriseWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#getBrandedCallingEnterprise");
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
| **id** | **String**|  | |

### Return type

ApiResponse<[**BrandedCallingEnterprise**](BrandedCallingEnterprise.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The business. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Business not found |  -  |


## getBrandedCallingIdentity

> BrandedCallingIdentity getBrandedCallingIdentity(id)

Get a caller identity

Poll this for review and vetting progress, or subscribe to &#x60;branded_calling.identity.status_updated&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            BrandedCallingIdentity result = apiInstance.getBrandedCallingIdentity(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#getBrandedCallingIdentity");
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
| **id** | **String**|  | |

### Return type

[**BrandedCallingIdentity**](BrandedCallingIdentity.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The identity with its numbers. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |

## getBrandedCallingIdentityWithHttpInfo

> ApiResponse<BrandedCallingIdentity> getBrandedCallingIdentity getBrandedCallingIdentityWithHttpInfo(id)

Get a caller identity

Poll this for review and vetting progress, or subscribe to &#x60;branded_calling.identity.status_updated&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<BrandedCallingIdentity> response = apiInstance.getBrandedCallingIdentityWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#getBrandedCallingIdentity");
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
| **id** | **String**|  | |

### Return type

ApiResponse<[**BrandedCallingIdentity**](BrandedCallingIdentity.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The identity with its numbers. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |


## listBrandedCallingCallReasons

> ListBrandedCallingCallReasons200Response listBrandedCallingCallReasons()

List pre-approved call reasons

The carrier catalogue of call reasons that pass vetting automatically. Any other wording is allowed on an identity but is vetted by hand.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        try {
            ListBrandedCallingCallReasons200Response result = apiInstance.listBrandedCallingCallReasons();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingCallReasons");
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

[**ListBrandedCallingCallReasons200Response**](ListBrandedCallingCallReasons200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The catalogue. |  -  |
| **401** | Unauthorized |  -  |

## listBrandedCallingCallReasonsWithHttpInfo

> ApiResponse<ListBrandedCallingCallReasons200Response> listBrandedCallingCallReasons listBrandedCallingCallReasonsWithHttpInfo()

List pre-approved call reasons

The carrier catalogue of call reasons that pass vetting automatically. Any other wording is allowed on an identity but is vetted by hand.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        try {
            ApiResponse<ListBrandedCallingCallReasons200Response> response = apiInstance.listBrandedCallingCallReasonsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingCallReasons");
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

ApiResponse<[**ListBrandedCallingCallReasons200Response**](ListBrandedCallingCallReasons200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The catalogue. |  -  |
| **401** | Unauthorized |  -  |


## listBrandedCallingEnterprises

> ListBrandedCallingEnterprises200Response listBrandedCallingEnterprises()

List registered businesses

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        try {
            ListBrandedCallingEnterprises200Response result = apiInstance.listBrandedCallingEnterprises();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingEnterprises");
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

[**ListBrandedCallingEnterprises200Response**](ListBrandedCallingEnterprises200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workspace&#39;s businesses. |  -  |
| **401** | Unauthorized |  -  |

## listBrandedCallingEnterprisesWithHttpInfo

> ApiResponse<ListBrandedCallingEnterprises200Response> listBrandedCallingEnterprises listBrandedCallingEnterprisesWithHttpInfo()

List registered businesses

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        try {
            ApiResponse<ListBrandedCallingEnterprises200Response> response = apiInstance.listBrandedCallingEnterprisesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingEnterprises");
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

ApiResponse<[**ListBrandedCallingEnterprises200Response**](ListBrandedCallingEnterprises200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workspace&#39;s businesses. |  -  |
| **401** | Unauthorized |  -  |


## listBrandedCallingIdentities

> ListBrandedCallingIdentities200Response listBrandedCallingIdentities()

List caller identities

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        try {
            ListBrandedCallingIdentities200Response result = apiInstance.listBrandedCallingIdentities();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingIdentities");
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

[**ListBrandedCallingIdentities200Response**](ListBrandedCallingIdentities200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workspace&#39;s identities with their numbers. |  -  |
| **401** | Unauthorized |  -  |

## listBrandedCallingIdentitiesWithHttpInfo

> ApiResponse<ListBrandedCallingIdentities200Response> listBrandedCallingIdentities listBrandedCallingIdentitiesWithHttpInfo()

List caller identities

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        try {
            ApiResponse<ListBrandedCallingIdentities200Response> response = apiInstance.listBrandedCallingIdentitiesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingIdentities");
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

ApiResponse<[**ListBrandedCallingIdentities200Response**](ListBrandedCallingIdentities200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workspace&#39;s identities with their numbers. |  -  |
| **401** | Unauthorized |  -  |


## listBrandedCallingIdentityNumbers

> ListBrandedCallingIdentityNumbers200Response listBrandedCallingIdentityNumbers(id)

List the numbers on a caller identity

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ListBrandedCallingIdentityNumbers200Response result = apiInstance.listBrandedCallingIdentityNumbers(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingIdentityNumbers");
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
| **id** | **String**|  | |

### Return type

[**ListBrandedCallingIdentityNumbers200Response**](ListBrandedCallingIdentityNumbers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attached numbers with their vetting status. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |

## listBrandedCallingIdentityNumbersWithHttpInfo

> ApiResponse<ListBrandedCallingIdentityNumbers200Response> listBrandedCallingIdentityNumbers listBrandedCallingIdentityNumbersWithHttpInfo(id)

List the numbers on a caller identity

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<ListBrandedCallingIdentityNumbers200Response> response = apiInstance.listBrandedCallingIdentityNumbersWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#listBrandedCallingIdentityNumbers");
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
| **id** | **String**|  | |

### Return type

ApiResponse<[**ListBrandedCallingIdentityNumbers200Response**](ListBrandedCallingIdentityNumbers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Attached numbers with their vetting status. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |


## resendBrandedCallingAuthorizerCode

> ResendBrandedCallingAuthorizerCode200Response resendBrandedCallingAuthorizerCode(id)

Resend the authorizer&#39;s code

Emails the authorizer a fresh 6-digit code (the previous one stops working). Only while the identity is &#x60;pending_email_verification&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ResendBrandedCallingAuthorizerCode200Response result = apiInstance.resendBrandedCallingAuthorizerCode(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#resendBrandedCallingAuthorizerCode");
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
| **id** | **String**|  | |

### Return type

[**ResendBrandedCallingAuthorizerCode200Response**](ResendBrandedCallingAuthorizerCode200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Code sent. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | The identity is not waiting for a code (code invalid_resource_state). |  -  |

## resendBrandedCallingAuthorizerCodeWithHttpInfo

> ApiResponse<ResendBrandedCallingAuthorizerCode200Response> resendBrandedCallingAuthorizerCode resendBrandedCallingAuthorizerCodeWithHttpInfo(id)

Resend the authorizer&#39;s code

Emails the authorizer a fresh 6-digit code (the previous one stops working). Only while the identity is &#x60;pending_email_verification&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<ResendBrandedCallingAuthorizerCode200Response> response = apiInstance.resendBrandedCallingAuthorizerCodeWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#resendBrandedCallingAuthorizerCode");
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
| **id** | **String**|  | |

### Return type

ApiResponse<[**ResendBrandedCallingAuthorizerCode200Response**](ResendBrandedCallingAuthorizerCode200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Code sent. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | The identity is not waiting for a code (code invalid_resource_state). |  -  |


## updateBrandedCallingIdentity

> BrandedCallingIdentity updateBrandedCallingIdentity(id, updateBrandedCallingIdentityRequest)

Edit or resubmit a caller identity

Allowed while the identity is &#x60;requested&#x60;, &#x60;changes_requested&#x60; or &#x60;rejected&#x60;. Answering a change request (send &#x60;reviewAnswers&#x60; keyed by point id, and any edited fields) puts it back in review. On a carrier rejection the edits are applied at the carrier and the identity is resubmitted straight away. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        UpdateBrandedCallingIdentityRequest updateBrandedCallingIdentityRequest = new UpdateBrandedCallingIdentityRequest(); // UpdateBrandedCallingIdentityRequest | 
        try {
            BrandedCallingIdentity result = apiInstance.updateBrandedCallingIdentity(id, updateBrandedCallingIdentityRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#updateBrandedCallingIdentity");
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
| **id** | **String**|  | |
| **updateBrandedCallingIdentityRequest** | [**UpdateBrandedCallingIdentityRequest**](UpdateBrandedCallingIdentityRequest.md)|  | |

### Return type

[**BrandedCallingIdentity**](BrandedCallingIdentity.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated identity. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | The identity cannot be edited in its current status (code invalid_resource_state). |  -  |

## updateBrandedCallingIdentityWithHttpInfo

> ApiResponse<BrandedCallingIdentity> updateBrandedCallingIdentity updateBrandedCallingIdentityWithHttpInfo(id, updateBrandedCallingIdentityRequest)

Edit or resubmit a caller identity

Allowed while the identity is &#x60;requested&#x60;, &#x60;changes_requested&#x60; or &#x60;rejected&#x60;. Answering a change request (send &#x60;reviewAnswers&#x60; keyed by point id, and any edited fields) puts it back in review. On a carrier rejection the edits are applied at the carrier and the identity is resubmitted straight away. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BrandedCallingApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BrandedCallingApi apiInstance = new BrandedCallingApi(defaultClient);
        String id = "id_example"; // String | 
        UpdateBrandedCallingIdentityRequest updateBrandedCallingIdentityRequest = new UpdateBrandedCallingIdentityRequest(); // UpdateBrandedCallingIdentityRequest | 
        try {
            ApiResponse<BrandedCallingIdentity> response = apiInstance.updateBrandedCallingIdentityWithHttpInfo(id, updateBrandedCallingIdentityRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BrandedCallingApi#updateBrandedCallingIdentity");
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
| **id** | **String**|  | |
| **updateBrandedCallingIdentityRequest** | [**UpdateBrandedCallingIdentityRequest**](UpdateBrandedCallingIdentityRequest.md)|  | |

### Return type

ApiResponse<[**BrandedCallingIdentity**](BrandedCallingIdentity.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated identity. |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Identity not found |  -  |
| **409** | The identity cannot be edited in its current status (code invalid_resource_state). |  -  |

