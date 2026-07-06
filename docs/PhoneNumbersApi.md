# PhoneNumbersApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelPhoneNumberPortIn**](PhoneNumbersApi.md#cancelPhoneNumberPortIn) | **DELETE** /v1/phone-numbers/port-in/{id} | Cancel a port-in |
| [**cancelPhoneNumberPortInWithHttpInfo**](PhoneNumbersApi.md#cancelPhoneNumberPortInWithHttpInfo) | **DELETE** /v1/phone-numbers/port-in/{id} | Cancel a port-in |
| [**checkPhoneNumberAvailability**](PhoneNumbersApi.md#checkPhoneNumberAvailability) | **GET** /v1/phone-numbers/availability | Check country availability |
| [**checkPhoneNumberAvailabilityWithHttpInfo**](PhoneNumbersApi.md#checkPhoneNumberAvailabilityWithHttpInfo) | **GET** /v1/phone-numbers/availability | Check country availability |
| [**checkPhoneNumberPortability**](PhoneNumbersApi.md#checkPhoneNumberPortability) | **POST** /v1/phone-numbers/port-in/check | Check portability |
| [**checkPhoneNumberPortabilityWithHttpInfo**](PhoneNumbersApi.md#checkPhoneNumberPortabilityWithHttpInfo) | **POST** /v1/phone-numbers/port-in/check | Check portability |
| [**createPhoneNumberKycLink**](PhoneNumbersApi.md#createPhoneNumberKycLink) | **POST** /v1/phone-numbers/kyc/share | Create a hosted KYC link |
| [**createPhoneNumberKycLinkWithHttpInfo**](PhoneNumbersApi.md#createPhoneNumberKycLinkWithHttpInfo) | **POST** /v1/phone-numbers/kyc/share | Create a hosted KYC link |
| [**createPhoneNumberPortIn**](PhoneNumbersApi.md#createPhoneNumberPortIn) | **POST** /v1/phone-numbers/port-in | Port numbers in |
| [**createPhoneNumberPortInWithHttpInfo**](PhoneNumbersApi.md#createPhoneNumberPortInWithHttpInfo) | **POST** /v1/phone-numbers/port-in | Port numbers in |
| [**getPhoneNumber**](PhoneNumbersApi.md#getPhoneNumber) | **GET** /v1/phone-numbers/{id} | Get phone number |
| [**getPhoneNumberWithHttpInfo**](PhoneNumbersApi.md#getPhoneNumberWithHttpInfo) | **GET** /v1/phone-numbers/{id} | Get phone number |
| [**getPhoneNumberKycForm**](PhoneNumbersApi.md#getPhoneNumberKycForm) | **GET** /v1/phone-numbers/kyc | Get KYC form spec |
| [**getPhoneNumberKycFormWithHttpInfo**](PhoneNumbersApi.md#getPhoneNumberKycFormWithHttpInfo) | **GET** /v1/phone-numbers/kyc | Get KYC form spec |
| [**getPhoneNumberRemediation**](PhoneNumbersApi.md#getPhoneNumberRemediation) | **GET** /v1/phone-numbers/{id}/remediate | Get declined requirements |
| [**getPhoneNumberRemediationWithHttpInfo**](PhoneNumbersApi.md#getPhoneNumberRemediationWithHttpInfo) | **GET** /v1/phone-numbers/{id}/remediate | Get declined requirements |
| [**listPhoneNumberCountries**](PhoneNumbersApi.md#listPhoneNumberCountries) | **GET** /v1/phone-numbers/countries | List offerable number countries |
| [**listPhoneNumberCountriesWithHttpInfo**](PhoneNumbersApi.md#listPhoneNumberCountriesWithHttpInfo) | **GET** /v1/phone-numbers/countries | List offerable number countries |
| [**listPhoneNumberPortIns**](PhoneNumbersApi.md#listPhoneNumberPortIns) | **GET** /v1/phone-numbers/port-in | List port-in orders |
| [**listPhoneNumberPortInsWithHttpInfo**](PhoneNumbersApi.md#listPhoneNumberPortInsWithHttpInfo) | **GET** /v1/phone-numbers/port-in | List port-in orders |
| [**listPhoneNumbers**](PhoneNumbersApi.md#listPhoneNumbers) | **GET** /v1/phone-numbers | List phone numbers |
| [**listPhoneNumbersWithHttpInfo**](PhoneNumbersApi.md#listPhoneNumbersWithHttpInfo) | **GET** /v1/phone-numbers | List phone numbers |
| [**purchasePhoneNumber**](PhoneNumbersApi.md#purchasePhoneNumber) | **POST** /v1/phone-numbers/purchase | Purchase phone number |
| [**purchasePhoneNumberWithHttpInfo**](PhoneNumbersApi.md#purchasePhoneNumberWithHttpInfo) | **POST** /v1/phone-numbers/purchase | Purchase phone number |
| [**releasePhoneNumber**](PhoneNumbersApi.md#releasePhoneNumber) | **DELETE** /v1/phone-numbers/{id} | Release phone number |
| [**releasePhoneNumberWithHttpInfo**](PhoneNumbersApi.md#releasePhoneNumberWithHttpInfo) | **DELETE** /v1/phone-numbers/{id} | Release phone number |
| [**remediatePhoneNumber**](PhoneNumbersApi.md#remediatePhoneNumber) | **POST** /v1/phone-numbers/{id}/remediate | Resubmit a declined number |
| [**remediatePhoneNumberWithHttpInfo**](PhoneNumbersApi.md#remediatePhoneNumberWithHttpInfo) | **POST** /v1/phone-numbers/{id}/remediate | Resubmit a declined number |
| [**reviewPhoneNumberKycPacket**](PhoneNumbersApi.md#reviewPhoneNumberKycPacket) | **POST** /v1/phone-numbers/kyc/review-packet | Pre-review a KYC packet |
| [**reviewPhoneNumberKycPacketWithHttpInfo**](PhoneNumbersApi.md#reviewPhoneNumberKycPacketWithHttpInfo) | **POST** /v1/phone-numbers/kyc/review-packet | Pre-review a KYC packet |
| [**searchAvailablePhoneNumbers**](PhoneNumbersApi.md#searchAvailablePhoneNumbers) | **GET** /v1/phone-numbers/available | Search available numbers |
| [**searchAvailablePhoneNumbersWithHttpInfo**](PhoneNumbersApi.md#searchAvailablePhoneNumbersWithHttpInfo) | **GET** /v1/phone-numbers/available | Search available numbers |
| [**submitPhoneNumberKyc**](PhoneNumbersApi.md#submitPhoneNumberKyc) | **POST** /v1/phone-numbers/kyc | Submit KYC |
| [**submitPhoneNumberKycWithHttpInfo**](PhoneNumbersApi.md#submitPhoneNumberKycWithHttpInfo) | **POST** /v1/phone-numbers/kyc | Submit KYC |
| [**uploadPhoneNumberKycDocument**](PhoneNumbersApi.md#uploadPhoneNumberKycDocument) | **POST** /v1/phone-numbers/kyc/upload-document | Upload a KYC document |
| [**uploadPhoneNumberKycDocumentWithHttpInfo**](PhoneNumbersApi.md#uploadPhoneNumberKycDocumentWithHttpInfo) | **POST** /v1/phone-numbers/kyc/upload-document | Upload a KYC document |
| [**uploadPhoneNumberPortInDocument**](PhoneNumbersApi.md#uploadPhoneNumberPortInDocument) | **POST** /v1/phone-numbers/port-in/documents | Upload a porting document |
| [**uploadPhoneNumberPortInDocumentWithHttpInfo**](PhoneNumbersApi.md#uploadPhoneNumberPortInDocumentWithHttpInfo) | **POST** /v1/phone-numbers/port-in/documents | Upload a porting document |
| [**validatePhoneNumberKycAddress**](PhoneNumbersApi.md#validatePhoneNumberKycAddress) | **POST** /v1/phone-numbers/kyc/validate-address | Pre-validate KYC address |
| [**validatePhoneNumberKycAddressWithHttpInfo**](PhoneNumbersApi.md#validatePhoneNumberKycAddressWithHttpInfo) | **POST** /v1/phone-numbers/kyc/validate-address | Pre-validate KYC address |



## cancelPhoneNumberPortIn

> CancelPhoneNumberPortIn200Response cancelPhoneNumberPortIn(id)

Cancel a port-in

Cancel an in-flight port (wrong number, staying with the old carrier). Only orders that haven&#39;t ported can be cancelled; a completed port is a normal number release instead. The carrier may report &#x60;cancel-pending&#x60; briefly while the losing carrier acknowledges; it settles to &#x60;cancelled&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Porting order ID (from the port-in list).
        try {
            CancelPhoneNumberPortIn200Response result = apiInstance.cancelPhoneNumberPortIn(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#cancelPhoneNumberPortIn");
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
| **id** | **String**| Porting order ID (from the port-in list). | |

### Return type

[**CancelPhoneNumberPortIn200Response**](CancelPhoneNumberPortIn200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cancel accepted (idempotent when already cancelled). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Porting order not found |  -  |
| **409** | Port already completed (release the number instead), or the carrier rejected the cancel (reason included) |  -  |

## cancelPhoneNumberPortInWithHttpInfo

> ApiResponse<CancelPhoneNumberPortIn200Response> cancelPhoneNumberPortIn cancelPhoneNumberPortInWithHttpInfo(id)

Cancel a port-in

Cancel an in-flight port (wrong number, staying with the old carrier). Only orders that haven&#39;t ported can be cancelled; a completed port is a normal number release instead. The carrier may report &#x60;cancel-pending&#x60; briefly while the losing carrier acknowledges; it settles to &#x60;cancelled&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Porting order ID (from the port-in list).
        try {
            ApiResponse<CancelPhoneNumberPortIn200Response> response = apiInstance.cancelPhoneNumberPortInWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#cancelPhoneNumberPortIn");
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
| **id** | **String**| Porting order ID (from the port-in list). | |

### Return type

ApiResponse<[**CancelPhoneNumberPortIn200Response**](CancelPhoneNumberPortIn200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cancel accepted (idempotent when already cancelled). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Porting order not found |  -  |
| **409** | Port already completed (release the number instead), or the carrier rejected the cancel (reason included) |  -  |


## checkPhoneNumberAvailability

> CheckPhoneNumberAvailability200Response checkPhoneNumberAvailability(country)

Check country availability

Pre-purchase check, so you can warn BEFORE a customer invests in KYC (regulated review is async, 1-3 days). Tells you whether we have deliverable inventory, and what address the customer needs:   - &#x60;addressConstraint: geo&#x60;  → the registered address MUST be in one of     the returned &#x60;areas&#x60; (the only place we have stock). A different-area     address passes pre-approval but the number can never be assigned.   - &#x60;addressConstraint: country&#x60; → any in-country address works.   - &#x60;addressConstraint: none&#x60; → field-only / instant country, no address. Call this before starting the KYC form for regulated countries. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | ISO-2 country code.
        try {
            CheckPhoneNumberAvailability200Response result = apiInstance.checkPhoneNumberAvailability(country);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#checkPhoneNumberAvailability");
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
| **country** | **String**| ISO-2 country code. | |

### Return type

[**CheckPhoneNumberAvailability200Response**](CheckPhoneNumberAvailability200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Availability + address constraint. |  -  |
| **400** | Country not offerable |  -  |
| **401** | Unauthorized |  -  |

## checkPhoneNumberAvailabilityWithHttpInfo

> ApiResponse<CheckPhoneNumberAvailability200Response> checkPhoneNumberAvailability checkPhoneNumberAvailabilityWithHttpInfo(country)

Check country availability

Pre-purchase check, so you can warn BEFORE a customer invests in KYC (regulated review is async, 1-3 days). Tells you whether we have deliverable inventory, and what address the customer needs:   - &#x60;addressConstraint: geo&#x60;  → the registered address MUST be in one of     the returned &#x60;areas&#x60; (the only place we have stock). A different-area     address passes pre-approval but the number can never be assigned.   - &#x60;addressConstraint: country&#x60; → any in-country address works.   - &#x60;addressConstraint: none&#x60; → field-only / instant country, no address. Call this before starting the KYC form for regulated countries. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | ISO-2 country code.
        try {
            ApiResponse<CheckPhoneNumberAvailability200Response> response = apiInstance.checkPhoneNumberAvailabilityWithHttpInfo(country);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#checkPhoneNumberAvailability");
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
| **country** | **String**| ISO-2 country code. | |

### Return type

ApiResponse<[**CheckPhoneNumberAvailability200Response**](CheckPhoneNumberAvailability200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Availability + address constraint. |  -  |
| **400** | Country not offerable |  -  |
| **401** | Unauthorized |  -  |


## checkPhoneNumberPortability

> CheckPhoneNumberPortability200Response checkPhoneNumberPortability(checkPhoneNumberPortabilityRequest)

Check portability

Pre-flight portability check: whether each number can be ported in and whether it qualifies for FastPort, BEFORE the user commits to a port order (LOA, invoice, service address). Read-only; creates no order and bills nothing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        CheckPhoneNumberPortabilityRequest checkPhoneNumberPortabilityRequest = new CheckPhoneNumberPortabilityRequest(); // CheckPhoneNumberPortabilityRequest | 
        try {
            CheckPhoneNumberPortability200Response result = apiInstance.checkPhoneNumberPortability(checkPhoneNumberPortabilityRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#checkPhoneNumberPortability");
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
| **checkPhoneNumberPortabilityRequest** | [**CheckPhoneNumberPortabilityRequest**](CheckPhoneNumberPortabilityRequest.md)|  | |

### Return type

[**CheckPhoneNumberPortability200Response**](CheckPhoneNumberPortability200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-number portability. |  -  |
| **401** | Unauthorized |  -  |

## checkPhoneNumberPortabilityWithHttpInfo

> ApiResponse<CheckPhoneNumberPortability200Response> checkPhoneNumberPortability checkPhoneNumberPortabilityWithHttpInfo(checkPhoneNumberPortabilityRequest)

Check portability

Pre-flight portability check: whether each number can be ported in and whether it qualifies for FastPort, BEFORE the user commits to a port order (LOA, invoice, service address). Read-only; creates no order and bills nothing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        CheckPhoneNumberPortabilityRequest checkPhoneNumberPortabilityRequest = new CheckPhoneNumberPortabilityRequest(); // CheckPhoneNumberPortabilityRequest | 
        try {
            ApiResponse<CheckPhoneNumberPortability200Response> response = apiInstance.checkPhoneNumberPortabilityWithHttpInfo(checkPhoneNumberPortabilityRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#checkPhoneNumberPortability");
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
| **checkPhoneNumberPortabilityRequest** | [**CheckPhoneNumberPortabilityRequest**](CheckPhoneNumberPortabilityRequest.md)|  | |

### Return type

ApiResponse<[**CheckPhoneNumberPortability200Response**](CheckPhoneNumberPortability200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-number portability. |  -  |
| **401** | Unauthorized |  -  |


## createPhoneNumberKycLink

> CreatePhoneNumberKycLink200Response createPhoneNumberKycLink(createPhoneNumberKycLinkRequest)

Create a hosted KYC link

Create a single-use, 7-day hosted KYC link that your end customer completes WITHOUT a Zernio login — useful when the person who holds the ID and address is not your team. They fill the regulated verification on a Zernio-hosted page; the number provisions under YOUR account once they submit. Only regulated (KYC) countries are valid: a country that does not require KYC returns 400.  White-label the page with &#x60;branding&#x60; (your company name, logo, brand color). Supply &#x60;redirect_url&#x60; to send the end customer back to your own site after a successful submit (completion params are appended — see below). Listen for the &#x60;whatsapp.number.kyc_submitted&#x60; webhook to react when the form is completed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        CreatePhoneNumberKycLinkRequest createPhoneNumberKycLinkRequest = new CreatePhoneNumberKycLinkRequest(); // CreatePhoneNumberKycLinkRequest | 
        try {
            CreatePhoneNumberKycLink200Response result = apiInstance.createPhoneNumberKycLink(createPhoneNumberKycLinkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#createPhoneNumberKycLink");
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
| **createPhoneNumberKycLinkRequest** | [**CreatePhoneNumberKycLinkRequest**](CreatePhoneNumberKycLinkRequest.md)|  | |

### Return type

[**CreatePhoneNumberKycLink200Response**](CreatePhoneNumberKycLink200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hosted KYC link created. |  -  |
| **400** | Country does not require KYC (not a regulated country). |  -  |
| **401** | Unauthorized |  -  |

## createPhoneNumberKycLinkWithHttpInfo

> ApiResponse<CreatePhoneNumberKycLink200Response> createPhoneNumberKycLink createPhoneNumberKycLinkWithHttpInfo(createPhoneNumberKycLinkRequest)

Create a hosted KYC link

Create a single-use, 7-day hosted KYC link that your end customer completes WITHOUT a Zernio login — useful when the person who holds the ID and address is not your team. They fill the regulated verification on a Zernio-hosted page; the number provisions under YOUR account once they submit. Only regulated (KYC) countries are valid: a country that does not require KYC returns 400.  White-label the page with &#x60;branding&#x60; (your company name, logo, brand color). Supply &#x60;redirect_url&#x60; to send the end customer back to your own site after a successful submit (completion params are appended — see below). Listen for the &#x60;whatsapp.number.kyc_submitted&#x60; webhook to react when the form is completed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        CreatePhoneNumberKycLinkRequest createPhoneNumberKycLinkRequest = new CreatePhoneNumberKycLinkRequest(); // CreatePhoneNumberKycLinkRequest | 
        try {
            ApiResponse<CreatePhoneNumberKycLink200Response> response = apiInstance.createPhoneNumberKycLinkWithHttpInfo(createPhoneNumberKycLinkRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#createPhoneNumberKycLink");
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
| **createPhoneNumberKycLinkRequest** | [**CreatePhoneNumberKycLinkRequest**](CreatePhoneNumberKycLinkRequest.md)|  | |

### Return type

ApiResponse<[**CreatePhoneNumberKycLink200Response**](CreatePhoneNumberKycLink200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hosted KYC link created. |  -  |
| **400** | Country does not require KYC (not a regulated country). |  -  |
| **401** | Unauthorized |  -  |


## createPhoneNumberPortIn

> CreatePhoneNumberPortIn201Response createPhoneNumberPortIn(createPhoneNumberPortInRequest)

Port numbers in

Submit a port-in for one or more existing numbers from another carrier. Creates the carrier order(s), attaches the end-user (current account) info plus the LOA and invoice documents, and submits to the losing carrier. The transfer PIN is forwarded to the carrier and never stored. Ported numbers arrive voice-ready (and SMS-ready where the order supports messaging).  Run the portability check (POST /v1/phone-numbers/port-in/check) and upload the two documents (POST /v1/phone-numbers/port-in/documents) first. The carrier may split the numbers into several orders (by country, number type, losing carrier); &#x60;orders&#x60; carries per-order results, and a partial failure still returns 201 with the failed orders&#39; &#x60;error&#x60; set (they stay as cancellable drafts). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        CreatePhoneNumberPortInRequest createPhoneNumberPortInRequest = new CreatePhoneNumberPortInRequest(); // CreatePhoneNumberPortInRequest | 
        try {
            CreatePhoneNumberPortIn201Response result = apiInstance.createPhoneNumberPortIn(createPhoneNumberPortInRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#createPhoneNumberPortIn");
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
| **createPhoneNumberPortInRequest** | [**CreatePhoneNumberPortInRequest**](CreatePhoneNumberPortInRequest.md)|  | |

### Return type

[**CreatePhoneNumberPortIn201Response**](CreatePhoneNumberPortIn201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Port submitted. Top-level fields mirror the first successfully submitted order; per-order truth (including failures) is in &#x60;orders&#x60;. |  -  |
| **401** | Unauthorized |  -  |
| **409** | A number is already provisioned, or already in an in-flight port |  -  |
| **422** | A number is not portable (reason included), or every split order failed to submit |  -  |

## createPhoneNumberPortInWithHttpInfo

> ApiResponse<CreatePhoneNumberPortIn201Response> createPhoneNumberPortIn createPhoneNumberPortInWithHttpInfo(createPhoneNumberPortInRequest)

Port numbers in

Submit a port-in for one or more existing numbers from another carrier. Creates the carrier order(s), attaches the end-user (current account) info plus the LOA and invoice documents, and submits to the losing carrier. The transfer PIN is forwarded to the carrier and never stored. Ported numbers arrive voice-ready (and SMS-ready where the order supports messaging).  Run the portability check (POST /v1/phone-numbers/port-in/check) and upload the two documents (POST /v1/phone-numbers/port-in/documents) first. The carrier may split the numbers into several orders (by country, number type, losing carrier); &#x60;orders&#x60; carries per-order results, and a partial failure still returns 201 with the failed orders&#39; &#x60;error&#x60; set (they stay as cancellable drafts). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        CreatePhoneNumberPortInRequest createPhoneNumberPortInRequest = new CreatePhoneNumberPortInRequest(); // CreatePhoneNumberPortInRequest | 
        try {
            ApiResponse<CreatePhoneNumberPortIn201Response> response = apiInstance.createPhoneNumberPortInWithHttpInfo(createPhoneNumberPortInRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#createPhoneNumberPortIn");
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
| **createPhoneNumberPortInRequest** | [**CreatePhoneNumberPortInRequest**](CreatePhoneNumberPortInRequest.md)|  | |

### Return type

ApiResponse<[**CreatePhoneNumberPortIn201Response**](CreatePhoneNumberPortIn201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Port submitted. Top-level fields mirror the first successfully submitted order; per-order truth (including failures) is in &#x60;orders&#x60;. |  -  |
| **401** | Unauthorized |  -  |
| **409** | A number is already provisioned, or already in an in-flight port |  -  |
| **422** | A number is not portable (reason included), or every split order failed to submit |  -  |


## getPhoneNumber

> GetPhoneNumber200Response getPhoneNumber(id)

Get phone number

Retrieve the current status of a purchased phone number. Poll this to track Meta pre-verification (US sync path) and, for regulated (Tier 3/4) numbers, the async lifecycle: pending_regulatory → active (or regulatory_declined). When a regulated number has an Onfido ID step, &#x60;onfidoVerificationUrl&#x60; appears here once the order is placed — forward it to the end user. (Or subscribe to the whatsapp.number.* webhooks instead of polling.) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID
        try {
            GetPhoneNumber200Response result = apiInstance.getPhoneNumber(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#getPhoneNumber");
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
| **id** | **String**| Phone number record ID | |

### Return type

[**GetPhoneNumber200Response**](GetPhoneNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getPhoneNumberWithHttpInfo

> ApiResponse<GetPhoneNumber200Response> getPhoneNumber getPhoneNumberWithHttpInfo(id)

Get phone number

Retrieve the current status of a purchased phone number. Poll this to track Meta pre-verification (US sync path) and, for regulated (Tier 3/4) numbers, the async lifecycle: pending_regulatory → active (or regulatory_declined). When a regulated number has an Onfido ID step, &#x60;onfidoVerificationUrl&#x60; appears here once the order is placed — forward it to the end user. (Or subscribe to the whatsapp.number.* webhooks instead of polling.) 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID
        try {
            ApiResponse<GetPhoneNumber200Response> response = apiInstance.getPhoneNumberWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#getPhoneNumber");
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
| **id** | **String**| Phone number record ID | |

### Return type

ApiResponse<[**GetPhoneNumber200Response**](GetPhoneNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getPhoneNumberKycForm

> GetPhoneNumberKycForm200Response getPhoneNumberKycForm(country)

Get KYC form spec

For a Tier 3/4 country, the fields the end customer must provide (Telnyx regulatory requirements) before a number can be ordered: text, date, address, or file (document) per requirement. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | 
        try {
            GetPhoneNumberKycForm200Response result = apiInstance.getPhoneNumberKycForm(country);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#getPhoneNumberKycForm");
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
| **country** | **String**|  | |

### Return type

[**GetPhoneNumberKycForm200Response**](GetPhoneNumberKycForm200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The KYC form spec. |  -  |
| **400** | Country not available |  -  |
| **401** | Unauthorized |  -  |

## getPhoneNumberKycFormWithHttpInfo

> ApiResponse<GetPhoneNumberKycForm200Response> getPhoneNumberKycForm getPhoneNumberKycFormWithHttpInfo(country)

Get KYC form spec

For a Tier 3/4 country, the fields the end customer must provide (Telnyx regulatory requirements) before a number can be ordered: text, date, address, or file (document) per requirement. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | 
        try {
            ApiResponse<GetPhoneNumberKycForm200Response> response = apiInstance.getPhoneNumberKycFormWithHttpInfo(country);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#getPhoneNumberKycForm");
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
| **country** | **String**|  | |

### Return type

ApiResponse<[**GetPhoneNumberKycForm200Response**](GetPhoneNumberKycForm200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The KYC form spec. |  -  |
| **400** | Country not available |  -  |
| **401** | Unauthorized |  -  |


## getPhoneNumberRemediation

> GetPhoneNumberRemediation200Response getPhoneNumberRemediation(id)

Get declined requirements

For a number in &#x60;regulatory_declined&#x60;, returns ONLY the requirements the reviewer flagged declined, as a form spec (same shape as the KYC form GET). The customer fixes just those — Telnyx supports correcting a declined requirement group and re-submitting it (no new number/group). Falls back to the full spec if the provider exposes no per-requirement flags. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID.
        try {
            GetPhoneNumberRemediation200Response result = apiInstance.getPhoneNumberRemediation(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#getPhoneNumberRemediation");
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
| **id** | **String**| Phone number record ID. | |

### Return type

[**GetPhoneNumberRemediation200Response**](GetPhoneNumberRemediation200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The declined requirements to fix. |  -  |
| **400** | Number is not awaiting remediation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |

## getPhoneNumberRemediationWithHttpInfo

> ApiResponse<GetPhoneNumberRemediation200Response> getPhoneNumberRemediation getPhoneNumberRemediationWithHttpInfo(id)

Get declined requirements

For a number in &#x60;regulatory_declined&#x60;, returns ONLY the requirements the reviewer flagged declined, as a form spec (same shape as the KYC form GET). The customer fixes just those — Telnyx supports correcting a declined requirement group and re-submitting it (no new number/group). Falls back to the full spec if the provider exposes no per-requirement flags. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID.
        try {
            ApiResponse<GetPhoneNumberRemediation200Response> response = apiInstance.getPhoneNumberRemediationWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#getPhoneNumberRemediation");
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
| **id** | **String**| Phone number record ID. | |

### Return type

ApiResponse<[**GetPhoneNumberRemediation200Response**](GetPhoneNumberRemediation200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The declined requirements to fix. |  -  |
| **400** | Number is not awaiting remediation |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |


## listPhoneNumberCountries

> ListPhoneNumberCountries200Response listPhoneNumberCountries()

List offerable number countries

The phone number countries available to purchase, each with its flat monthly price (cents), regulatory tier, whether it needs end-user KYC (Tier 3/4), and per-feature availability (PSTN calls, WhatsApp, SMS, and WhatsApp Business Calling outbound). Drives the country picker. Tier-4 countries appear only when enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        try {
            ListPhoneNumberCountries200Response result = apiInstance.listPhoneNumberCountries();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#listPhoneNumberCountries");
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

[**ListPhoneNumberCountries200Response**](ListPhoneNumberCountries200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offerable countries, cheapest first. |  -  |
| **401** | Unauthorized |  -  |

## listPhoneNumberCountriesWithHttpInfo

> ApiResponse<ListPhoneNumberCountries200Response> listPhoneNumberCountries listPhoneNumberCountriesWithHttpInfo()

List offerable number countries

The phone number countries available to purchase, each with its flat monthly price (cents), regulatory tier, whether it needs end-user KYC (Tier 3/4), and per-feature availability (PSTN calls, WhatsApp, SMS, and WhatsApp Business Calling outbound). Drives the country picker. Tier-4 countries appear only when enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        try {
            ApiResponse<ListPhoneNumberCountries200Response> response = apiInstance.listPhoneNumberCountriesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#listPhoneNumberCountries");
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

ApiResponse<[**ListPhoneNumberCountries200Response**](ListPhoneNumberCountries200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offerable countries, cheapest first. |  -  |
| **401** | Unauthorized |  -  |


## listPhoneNumberPortIns

> ListPhoneNumberPortIns200Response listPhoneNumberPortIns()

List port-in orders

Your porting orders, newest first (max 50). Poll this for port progress: pending, confirmed FOC date, exception reason, or ported. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        try {
            ListPhoneNumberPortIns200Response result = apiInstance.listPhoneNumberPortIns();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#listPhoneNumberPortIns");
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

[**ListPhoneNumberPortIns200Response**](ListPhoneNumberPortIns200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Porting orders |  -  |
| **401** | Unauthorized |  -  |

## listPhoneNumberPortInsWithHttpInfo

> ApiResponse<ListPhoneNumberPortIns200Response> listPhoneNumberPortIns listPhoneNumberPortInsWithHttpInfo()

List port-in orders

Your porting orders, newest first (max 50). Poll this for port progress: pending, confirmed FOC date, exception reason, or ported. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        try {
            ApiResponse<ListPhoneNumberPortIns200Response> response = apiInstance.listPhoneNumberPortInsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#listPhoneNumberPortIns");
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

ApiResponse<[**ListPhoneNumberPortIns200Response**](ListPhoneNumberPortIns200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Porting orders |  -  |
| **401** | Unauthorized |  -  |


## listPhoneNumbers

> ListPhoneNumbers200Response listPhoneNumbers(status, profileId)

List phone numbers

List all phone numbers purchased by the authenticated user. By default, released numbers are excluded. Connected (bring-your-own) WhatsApp numbers are returned in the separate &#x60;connected&#x60; array; they are not billed and have no provisioning lifecycle. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String status = "provisioning"; // String | Filter by status (by default excludes released numbers). NOTE: `status=pending_regulatory` returns the \"provisioning\" view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with `regulatoryDeclineReason`) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/phone-numbers/{id}/remediate. `verifying` is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches `active`. 
        String profileId = "profileId_example"; // String | Filter by profile
        try {
            ListPhoneNumbers200Response result = apiInstance.listPhoneNumbers(status, profileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#listPhoneNumbers");
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
| **status** | **String**| Filter by status (by default excludes released numbers). NOTE: &#x60;status&#x3D;pending_regulatory&#x60; returns the \&quot;provisioning\&quot; view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with &#x60;regulatoryDeclineReason&#x60;) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/phone-numbers/{id}/remediate. &#x60;verifying&#x60; is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches &#x60;active&#x60;.  | [optional] [enum: provisioning, verifying, pending_payment, pending_regulatory, regulatory_declined, active, suspended, releasing, released] |
| **profileId** | **String**| Filter by profile | [optional] |

### Return type

[**ListPhoneNumbers200Response**](ListPhoneNumbers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone numbers retrieved successfully |  -  |
| **401** | Unauthorized |  -  |

## listPhoneNumbersWithHttpInfo

> ApiResponse<ListPhoneNumbers200Response> listPhoneNumbers listPhoneNumbersWithHttpInfo(status, profileId)

List phone numbers

List all phone numbers purchased by the authenticated user. By default, released numbers are excluded. Connected (bring-your-own) WhatsApp numbers are returned in the separate &#x60;connected&#x60; array; they are not billed and have no provisioning lifecycle. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String status = "provisioning"; // String | Filter by status (by default excludes released numbers). NOTE: `status=pending_regulatory` returns the \"provisioning\" view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with `regulatoryDeclineReason`) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/phone-numbers/{id}/remediate. `verifying` is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches `active`. 
        String profileId = "profileId_example"; // String | Filter by profile
        try {
            ApiResponse<ListPhoneNumbers200Response> response = apiInstance.listPhoneNumbersWithHttpInfo(status, profileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#listPhoneNumbers");
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
| **status** | **String**| Filter by status (by default excludes released numbers). NOTE: &#x60;status&#x3D;pending_regulatory&#x60; returns the \&quot;provisioning\&quot; view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with &#x60;regulatoryDeclineReason&#x60;) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/phone-numbers/{id}/remediate. &#x60;verifying&#x60; is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches &#x60;active&#x60;.  | [optional] [enum: provisioning, verifying, pending_payment, pending_regulatory, regulatory_declined, active, suspended, releasing, released] |
| **profileId** | **String**| Filter by profile | [optional] |

### Return type

ApiResponse<[**ListPhoneNumbers200Response**](ListPhoneNumbers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone numbers retrieved successfully |  -  |
| **401** | Unauthorized |  -  |


## purchasePhoneNumber

> PurchasePhoneNumber200Response purchasePhoneNumber(purchasePhoneNumberRequest)

Purchase phone number

Initiate purchasing a phone number. Payment-first flow: the user does not pick a specific number. The system either creates a Stripe Checkout Session (first number) or increments the existing subscription quantity and provisions inline (subsequent numbers).  Requires a paid plan. The maximum number of phone numbers is determined by the user&#39;s plan. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        PurchasePhoneNumberRequest purchasePhoneNumberRequest = new PurchasePhoneNumberRequest(); // PurchasePhoneNumberRequest | 
        try {
            PurchasePhoneNumber200Response result = apiInstance.purchasePhoneNumber(purchasePhoneNumberRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#purchasePhoneNumber");
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
| **purchasePhoneNumberRequest** | [**PurchasePhoneNumberRequest**](PurchasePhoneNumberRequest.md)|  | |

### Return type

[**PurchasePhoneNumber200Response**](PurchasePhoneNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Either a checkout URL (first number) or the provisioned phone number (subsequent numbers).  |  -  |
| **400** | Plan limit reached, profileId required, or country not available |  -  |
| **401** | Unauthorized |  -  |
| **403** | A paid plan is required |  -  |
| **409** | Duplicate-purchase protection: another number was purchased for this user within the last 10 minutes. Retry with allowMultiple: true to confirm the additional purchase is intentional.  |  -  |
| **202** | Country requires end-user KYC before the number can be ordered. |  -  |
| **402** | Payment method required (Metronome user with no card on file). Response body carries code: PAYMENT_REQUIRED; add a card, then retry. |  -  |
| **422** | International numbers require usage-based billing (legacy Stripe users are US-only). Response body code: USAGE_BILLING_REQUIRED. |  -  |

## purchasePhoneNumberWithHttpInfo

> ApiResponse<PurchasePhoneNumber200Response> purchasePhoneNumber purchasePhoneNumberWithHttpInfo(purchasePhoneNumberRequest)

Purchase phone number

Initiate purchasing a phone number. Payment-first flow: the user does not pick a specific number. The system either creates a Stripe Checkout Session (first number) or increments the existing subscription quantity and provisions inline (subsequent numbers).  Requires a paid plan. The maximum number of phone numbers is determined by the user&#39;s plan. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        PurchasePhoneNumberRequest purchasePhoneNumberRequest = new PurchasePhoneNumberRequest(); // PurchasePhoneNumberRequest | 
        try {
            ApiResponse<PurchasePhoneNumber200Response> response = apiInstance.purchasePhoneNumberWithHttpInfo(purchasePhoneNumberRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#purchasePhoneNumber");
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
| **purchasePhoneNumberRequest** | [**PurchasePhoneNumberRequest**](PurchasePhoneNumberRequest.md)|  | |

### Return type

ApiResponse<[**PurchasePhoneNumber200Response**](PurchasePhoneNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Either a checkout URL (first number) or the provisioned phone number (subsequent numbers).  |  -  |
| **400** | Plan limit reached, profileId required, or country not available |  -  |
| **401** | Unauthorized |  -  |
| **403** | A paid plan is required |  -  |
| **409** | Duplicate-purchase protection: another number was purchased for this user within the last 10 minutes. Retry with allowMultiple: true to confirm the additional purchase is intentional.  |  -  |
| **202** | Country requires end-user KYC before the number can be ordered. |  -  |
| **402** | Payment method required (Metronome user with no card on file). Response body carries code: PAYMENT_REQUIRED; add a card, then retry. |  -  |
| **422** | International numbers require usage-based billing (legacy Stripe users are US-only). Response body code: USAGE_BILLING_REQUIRED. |  -  |


## releasePhoneNumber

> ReleasePhoneNumber200Response releasePhoneNumber(id)

Release phone number

Release a purchased phone number. This will: 1. Disconnect any linked WhatsApp social account 2. Decrement the Stripe subscription quantity (or cancel if last number) 3. Release the number from Telnyx 4. Mark the number as released 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID
        try {
            ReleasePhoneNumber200Response result = apiInstance.releasePhoneNumber(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#releasePhoneNumber");
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
| **id** | **String**| Phone number record ID | |

### Return type

[**ReleasePhoneNumber200Response**](ReleasePhoneNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number released successfully |  -  |
| **400** | Phone number is already released or being released |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## releasePhoneNumberWithHttpInfo

> ApiResponse<ReleasePhoneNumber200Response> releasePhoneNumber releasePhoneNumberWithHttpInfo(id)

Release phone number

Release a purchased phone number. This will: 1. Disconnect any linked WhatsApp social account 2. Decrement the Stripe subscription quantity (or cancel if last number) 3. Release the number from Telnyx 4. Mark the number as released 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID
        try {
            ApiResponse<ReleasePhoneNumber200Response> response = apiInstance.releasePhoneNumberWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#releasePhoneNumber");
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
| **id** | **String**| Phone number record ID | |

### Return type

ApiResponse<[**ReleasePhoneNumber200Response**](ReleasePhoneNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Phone number released successfully |  -  |
| **400** | Phone number is already released or being released |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## remediatePhoneNumber

> RemediatePhoneNumber200Response remediatePhoneNumber(id, remediatePhoneNumberRequest)

Resubmit a declined number

Submit corrected values/documents for the declined requirement(s). We PATCH them onto the SAME requirement group and re-submit it for approval; the number goes &#x60;regulatory_declined&#x60; → &#x60;pending_regulatory&#x60;. No new number and no new billing. Body shape matches the KYC submit (values / documents / address) — send only the corrected fields. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | 
        RemediatePhoneNumberRequest remediatePhoneNumberRequest = new RemediatePhoneNumberRequest(); // RemediatePhoneNumberRequest | 
        try {
            RemediatePhoneNumber200Response result = apiInstance.remediatePhoneNumber(id, remediatePhoneNumberRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#remediatePhoneNumber");
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
| **remediatePhoneNumberRequest** | [**RemediatePhoneNumberRequest**](RemediatePhoneNumberRequest.md)|  | |

### Return type

[**RemediatePhoneNumber200Response**](RemediatePhoneNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Re-submitted for approval. |  -  |
| **400** | Number is not awaiting remediation / nothing to remediate |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |

## remediatePhoneNumberWithHttpInfo

> ApiResponse<RemediatePhoneNumber200Response> remediatePhoneNumber remediatePhoneNumberWithHttpInfo(id, remediatePhoneNumberRequest)

Resubmit a declined number

Submit corrected values/documents for the declined requirement(s). We PATCH them onto the SAME requirement group and re-submit it for approval; the number goes &#x60;regulatory_declined&#x60; → &#x60;pending_regulatory&#x60;. No new number and no new billing. Body shape matches the KYC submit (values / documents / address) — send only the corrected fields. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | 
        RemediatePhoneNumberRequest remediatePhoneNumberRequest = new RemediatePhoneNumberRequest(); // RemediatePhoneNumberRequest | 
        try {
            ApiResponse<RemediatePhoneNumber200Response> response = apiInstance.remediatePhoneNumberWithHttpInfo(id, remediatePhoneNumberRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#remediatePhoneNumber");
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
| **remediatePhoneNumberRequest** | [**RemediatePhoneNumberRequest**](RemediatePhoneNumberRequest.md)|  | |

### Return type

ApiResponse<[**RemediatePhoneNumber200Response**](RemediatePhoneNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Re-submitted for approval. |  -  |
| **400** | Number is not awaiting remediation / nothing to remediate |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |


## reviewPhoneNumberKycPacket

> ReviewPhoneNumberKycPacket200Response reviewPhoneNumberKycPacket(reviewPhoneNumberKycPacketRequest)

Pre-review a KYC packet

Advisory dry-run of a regulated-KYC packet before submitting: reviews the exact documents the regulator will see (referenced by the ids from POST /v1/phone-numbers/kyc/upload-document) against the declared values and address, and returns plain-language advisories for likely decline reasons (wrong document type, mismatched address, one-sided ID scans). Non-blocking: advisories are warnings, submitting anyway is always allowed, and any review failure degrades to an empty list. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        ReviewPhoneNumberKycPacketRequest reviewPhoneNumberKycPacketRequest = new ReviewPhoneNumberKycPacketRequest(); // ReviewPhoneNumberKycPacketRequest | 
        try {
            ReviewPhoneNumberKycPacket200Response result = apiInstance.reviewPhoneNumberKycPacket(reviewPhoneNumberKycPacketRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#reviewPhoneNumberKycPacket");
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
| **reviewPhoneNumberKycPacketRequest** | [**ReviewPhoneNumberKycPacketRequest**](ReviewPhoneNumberKycPacketRequest.md)|  | |

### Return type

[**ReviewPhoneNumberKycPacket200Response**](ReviewPhoneNumberKycPacket200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Advisories (empty when the packet looks fine or the review was unavailable). |  -  |
| **401** | Unauthorized |  -  |

## reviewPhoneNumberKycPacketWithHttpInfo

> ApiResponse<ReviewPhoneNumberKycPacket200Response> reviewPhoneNumberKycPacket reviewPhoneNumberKycPacketWithHttpInfo(reviewPhoneNumberKycPacketRequest)

Pre-review a KYC packet

Advisory dry-run of a regulated-KYC packet before submitting: reviews the exact documents the regulator will see (referenced by the ids from POST /v1/phone-numbers/kyc/upload-document) against the declared values and address, and returns plain-language advisories for likely decline reasons (wrong document type, mismatched address, one-sided ID scans). Non-blocking: advisories are warnings, submitting anyway is always allowed, and any review failure degrades to an empty list. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        ReviewPhoneNumberKycPacketRequest reviewPhoneNumberKycPacketRequest = new ReviewPhoneNumberKycPacketRequest(); // ReviewPhoneNumberKycPacketRequest | 
        try {
            ApiResponse<ReviewPhoneNumberKycPacket200Response> response = apiInstance.reviewPhoneNumberKycPacketWithHttpInfo(reviewPhoneNumberKycPacketRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#reviewPhoneNumberKycPacket");
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
| **reviewPhoneNumberKycPacketRequest** | [**ReviewPhoneNumberKycPacketRequest**](ReviewPhoneNumberKycPacketRequest.md)|  | |

### Return type

ApiResponse<[**ReviewPhoneNumberKycPacket200Response**](ReviewPhoneNumberKycPacket200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Advisories (empty when the packet looks fine or the review was unavailable). |  -  |
| **401** | Unauthorized |  -  |


## searchAvailablePhoneNumbers

> SearchAvailablePhoneNumbers200Response searchAvailablePhoneNumbers(country, type, prefix, locality, contains, sms, limit)

Search available numbers

Search the provider&#39;s inventory for numbers available to purchase in a country (default US). Optional filters narrow the results. The country must be offerable (see GET /v1/phone-numbers/countries). Voice capability is always required; pass &#x60;sms&#x3D;true&#x60; to only see numbers that can also text (SMS support is per-number, not per-country). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String country = "US"; // String | 
        String type = "type_example"; // String | Number type; defaults to the country's WhatsApp-safe type
        String prefix = "prefix_example"; // String | Area code
        String locality = "locality_example"; // String | City
        String contains = "contains_example"; // String | Pattern to match within the number
        Boolean sms = true; // Boolean | true narrows the pool to SMS-capable numbers. Each result still carries its full `features` list for per-number capability badging.
        Integer limit = 20; // Integer | 
        try {
            SearchAvailablePhoneNumbers200Response result = apiInstance.searchAvailablePhoneNumbers(country, type, prefix, locality, contains, sms, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#searchAvailablePhoneNumbers");
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
| **country** | **String**|  | [optional] [default to US] |
| **type** | **String**| Number type; defaults to the country&#39;s WhatsApp-safe type | [optional] |
| **prefix** | **String**| Area code | [optional] |
| **locality** | **String**| City | [optional] |
| **contains** | **String**| Pattern to match within the number | [optional] |
| **sms** | **Boolean**| true narrows the pool to SMS-capable numbers. Each result still carries its full &#x60;features&#x60; list for per-number capability badging. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**SearchAvailablePhoneNumbers200Response**](SearchAvailablePhoneNumbers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Available numbers. |  -  |
| **400** | Country not available |  -  |
| **401** | Unauthorized |  -  |

## searchAvailablePhoneNumbersWithHttpInfo

> ApiResponse<SearchAvailablePhoneNumbers200Response> searchAvailablePhoneNumbers searchAvailablePhoneNumbersWithHttpInfo(country, type, prefix, locality, contains, sms, limit)

Search available numbers

Search the provider&#39;s inventory for numbers available to purchase in a country (default US). Optional filters narrow the results. The country must be offerable (see GET /v1/phone-numbers/countries). Voice capability is always required; pass &#x60;sms&#x3D;true&#x60; to only see numbers that can also text (SMS support is per-number, not per-country). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String country = "US"; // String | 
        String type = "type_example"; // String | Number type; defaults to the country's WhatsApp-safe type
        String prefix = "prefix_example"; // String | Area code
        String locality = "locality_example"; // String | City
        String contains = "contains_example"; // String | Pattern to match within the number
        Boolean sms = true; // Boolean | true narrows the pool to SMS-capable numbers. Each result still carries its full `features` list for per-number capability badging.
        Integer limit = 20; // Integer | 
        try {
            ApiResponse<SearchAvailablePhoneNumbers200Response> response = apiInstance.searchAvailablePhoneNumbersWithHttpInfo(country, type, prefix, locality, contains, sms, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#searchAvailablePhoneNumbers");
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
| **country** | **String**|  | [optional] [default to US] |
| **type** | **String**| Number type; defaults to the country&#39;s WhatsApp-safe type | [optional] |
| **prefix** | **String**| Area code | [optional] |
| **locality** | **String**| City | [optional] |
| **contains** | **String**| Pattern to match within the number | [optional] |
| **sms** | **Boolean**| true narrows the pool to SMS-capable numbers. Each result still carries its full &#x60;features&#x60; list for per-number capability badging. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

ApiResponse<[**SearchAvailablePhoneNumbers200Response**](SearchAvailablePhoneNumbers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Available numbers. |  -  |
| **400** | Country not available |  -  |
| **401** | Unauthorized |  -  |


## submitPhoneNumberKyc

> SubmitPhoneNumberKyc200Response submitPhoneNumberKyc(submitPhoneNumberKycRequest)

Submit KYC

Submit the end customer&#39;s KYC (textual values, uploaded documents, address) for a Tier 3/4 country. Documents are streamed straight to the number provider and are not stored by Zernio. Builds + submits a regulatory requirement group and claims a pending_regulatory slot; the number is ordered + activated once the provider approves (asynchronous). A customer may hold several same-country numbers in review at once; a double-submit of the SAME attempt is deduped via &#x60;submissionId&#x60;.  For an ID-card document requirement, carriers commonly require BOTH sides: combine the front and back into a single file before uploading (the dashboard does this automatically). A one-sided ID is a common decline reason; fix it via POST /v1/phone-numbers/{id}/remediate.  Before submitting, call GET /v1/phone-numbers/availability to check the country has deliverable inventory and, for geographic-match countries, which area the address must be in — otherwise the submission can pass review yet never be assignable a number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        SubmitPhoneNumberKycRequest submitPhoneNumberKycRequest = new SubmitPhoneNumberKycRequest(); // SubmitPhoneNumberKycRequest | 
        try {
            SubmitPhoneNumberKyc200Response result = apiInstance.submitPhoneNumberKyc(submitPhoneNumberKycRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#submitPhoneNumberKyc");
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
| **submitPhoneNumberKycRequest** | [**SubmitPhoneNumberKycRequest**](SubmitPhoneNumberKycRequest.md)|  | |

### Return type

[**SubmitPhoneNumberKyc200Response**](SubmitPhoneNumberKyc200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | KYC submitted (or already submitted); number pending review. |  -  |
| **400** | Validation error (e.g. address not in-country, file too large) |  -  |
| **409** | reuse requested but no prior approved verification exists for this country |  -  |
| **401** | Unauthorized |  -  |

## submitPhoneNumberKycWithHttpInfo

> ApiResponse<SubmitPhoneNumberKyc200Response> submitPhoneNumberKyc submitPhoneNumberKycWithHttpInfo(submitPhoneNumberKycRequest)

Submit KYC

Submit the end customer&#39;s KYC (textual values, uploaded documents, address) for a Tier 3/4 country. Documents are streamed straight to the number provider and are not stored by Zernio. Builds + submits a regulatory requirement group and claims a pending_regulatory slot; the number is ordered + activated once the provider approves (asynchronous). A customer may hold several same-country numbers in review at once; a double-submit of the SAME attempt is deduped via &#x60;submissionId&#x60;.  For an ID-card document requirement, carriers commonly require BOTH sides: combine the front and back into a single file before uploading (the dashboard does this automatically). A one-sided ID is a common decline reason; fix it via POST /v1/phone-numbers/{id}/remediate.  Before submitting, call GET /v1/phone-numbers/availability to check the country has deliverable inventory and, for geographic-match countries, which area the address must be in — otherwise the submission can pass review yet never be assignable a number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        SubmitPhoneNumberKycRequest submitPhoneNumberKycRequest = new SubmitPhoneNumberKycRequest(); // SubmitPhoneNumberKycRequest | 
        try {
            ApiResponse<SubmitPhoneNumberKyc200Response> response = apiInstance.submitPhoneNumberKycWithHttpInfo(submitPhoneNumberKycRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#submitPhoneNumberKyc");
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
| **submitPhoneNumberKycRequest** | [**SubmitPhoneNumberKycRequest**](SubmitPhoneNumberKycRequest.md)|  | |

### Return type

ApiResponse<[**SubmitPhoneNumberKyc200Response**](SubmitPhoneNumberKyc200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | KYC submitted (or already submitted); number pending review. |  -  |
| **400** | Validation error (e.g. address not in-country, file too large) |  -  |
| **409** | reuse requested but no prior approved verification exists for this country |  -  |
| **401** | Unauthorized |  -  |


## uploadPhoneNumberKycDocument

> UploadPhoneNumberKycDocument200Response uploadPhoneNumberKycDocument(xFilename, body)

Upload a KYC document

Upload ONE document and get back its provider document id, to reference from POST /v1/phone-numbers/kyc via &#x60;documents[].documentId&#x60;. Send the RAW file bytes as the request body (not base64); put the filename in the &#x60;X-Filename&#x60; header. Uploading documents one-per-request keeps each request under the ~4.5MB body limit. The document streams straight to the number provider and is not stored by Zernio. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String xFilename = "xFilename_example"; // String | URL-encoded original filename.
        File body = new File("/path/to/file"); // File | 
        try {
            UploadPhoneNumberKycDocument200Response result = apiInstance.uploadPhoneNumberKycDocument(xFilename, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#uploadPhoneNumberKycDocument");
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
| **xFilename** | **String**| URL-encoded original filename. | |
| **body** | **File**|  | |

### Return type

[**UploadPhoneNumberKycDocument200Response**](UploadPhoneNumberKycDocument200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document uploaded. |  -  |
| **400** | Missing X-Filename, empty body, or file too large (over 20MB). |  -  |
| **401** | Unauthorized |  -  |

## uploadPhoneNumberKycDocumentWithHttpInfo

> ApiResponse<UploadPhoneNumberKycDocument200Response> uploadPhoneNumberKycDocument uploadPhoneNumberKycDocumentWithHttpInfo(xFilename, body)

Upload a KYC document

Upload ONE document and get back its provider document id, to reference from POST /v1/phone-numbers/kyc via &#x60;documents[].documentId&#x60;. Send the RAW file bytes as the request body (not base64); put the filename in the &#x60;X-Filename&#x60; header. Uploading documents one-per-request keeps each request under the ~4.5MB body limit. The document streams straight to the number provider and is not stored by Zernio. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        String xFilename = "xFilename_example"; // String | URL-encoded original filename.
        File body = new File("/path/to/file"); // File | 
        try {
            ApiResponse<UploadPhoneNumberKycDocument200Response> response = apiInstance.uploadPhoneNumberKycDocumentWithHttpInfo(xFilename, body);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#uploadPhoneNumberKycDocument");
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
| **xFilename** | **String**| URL-encoded original filename. | |
| **body** | **File**|  | |

### Return type

ApiResponse<[**UploadPhoneNumberKycDocument200Response**](UploadPhoneNumberKycDocument200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document uploaded. |  -  |
| **400** | Missing X-Filename, empty body, or file too large (over 20MB). |  -  |
| **401** | Unauthorized |  -  |


## uploadPhoneNumberPortInDocument

> UploadPhoneNumberPortInDocument200Response uploadPhoneNumberPortInDocument(_file, kind)

Upload a porting document

Upload ONE porting document (the signed LOA or a recent carrier invoice) and get back its &#x60;documentId&#x60;, which the port-in create request takes as &#x60;loaDocumentId&#x60; / &#x60;invoiceDocumentId&#x60;. PDF, JPEG, or PNG, 10MB max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        File _file = new File("/path/to/file"); // File | The document (PDF/JPEG/PNG, 10MB max).
        String kind = "loa"; // String | Informational; used for the stored filename.
        try {
            UploadPhoneNumberPortInDocument200Response result = apiInstance.uploadPhoneNumberPortInDocument(_file, kind);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#uploadPhoneNumberPortInDocument");
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
| **_file** | **File**| The document (PDF/JPEG/PNG, 10MB max). | |
| **kind** | **String**| Informational; used for the stored filename. | [optional] [enum: loa, invoice] |

### Return type

[**UploadPhoneNumberPortInDocument200Response**](UploadPhoneNumberPortInDocument200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document uploaded. |  -  |
| **400** | Missing file, file too large, or unsupported type |  -  |
| **401** | Unauthorized |  -  |

## uploadPhoneNumberPortInDocumentWithHttpInfo

> ApiResponse<UploadPhoneNumberPortInDocument200Response> uploadPhoneNumberPortInDocument uploadPhoneNumberPortInDocumentWithHttpInfo(_file, kind)

Upload a porting document

Upload ONE porting document (the signed LOA or a recent carrier invoice) and get back its &#x60;documentId&#x60;, which the port-in create request takes as &#x60;loaDocumentId&#x60; / &#x60;invoiceDocumentId&#x60;. PDF, JPEG, or PNG, 10MB max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        File _file = new File("/path/to/file"); // File | The document (PDF/JPEG/PNG, 10MB max).
        String kind = "loa"; // String | Informational; used for the stored filename.
        try {
            ApiResponse<UploadPhoneNumberPortInDocument200Response> response = apiInstance.uploadPhoneNumberPortInDocumentWithHttpInfo(_file, kind);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#uploadPhoneNumberPortInDocument");
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
| **_file** | **File**| The document (PDF/JPEG/PNG, 10MB max). | |
| **kind** | **String**| Informational; used for the stored filename. | [optional] [enum: loa, invoice] |

### Return type

ApiResponse<[**UploadPhoneNumberPortInDocument200Response**](UploadPhoneNumberPortInDocument200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document uploaded. |  -  |
| **400** | Missing file, file too large, or unsupported type |  -  |
| **401** | Unauthorized |  -  |


## validatePhoneNumberKycAddress

> ValidatePhoneNumberKycAddress200Response validatePhoneNumberKycAddress(validatePhoneNumberKycAddressRequest)

Pre-validate KYC address

Optional early check for the address step of a Tier 4 (end-user identity) registration: validates a postal address for deliverability BEFORE the full KYC submit, so it can be corrected before any documents are uploaded. The full submit (POST /v1/phone-numbers/kyc) re-validates the address, so this call is purely a fast feedback path and skipping it is safe. Only the postal address is sent (no documents, no gov-ID fields). A region (&#x60;administrative_area&#x60;) is required by the validator; when it is omitted the pre-check is skipped and &#x60;{ ok: true, skipped: true }&#x60; is returned (the final submit still validates). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        ValidatePhoneNumberKycAddressRequest validatePhoneNumberKycAddressRequest = new ValidatePhoneNumberKycAddressRequest(); // ValidatePhoneNumberKycAddressRequest | 
        try {
            ValidatePhoneNumberKycAddress200Response result = apiInstance.validatePhoneNumberKycAddress(validatePhoneNumberKycAddressRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#validatePhoneNumberKycAddress");
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
| **validatePhoneNumberKycAddressRequest** | [**ValidatePhoneNumberKycAddressRequest**](ValidatePhoneNumberKycAddressRequest.md)|  | |

### Return type

[**ValidatePhoneNumberKycAddress200Response**](ValidatePhoneNumberKycAddress200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Address is deliverable, or the pre-check was skipped (no region supplied). |  -  |
| **400** | The country isn&#39;t offered, or the address could not be verified. When the provider returned usable corrections, &#x60;details.addressSuggestions&#x60; carries them per field for a one-click \&quot;apply suggestion\&quot; card. (Flat error envelope: &#x60;error&#x60; is the human message; &#x60;code&#x60;/&#x60;param&#x60;/&#x60;details&#x60; are top-level siblings.)  |  -  |
| **401** | Unauthorized |  -  |

## validatePhoneNumberKycAddressWithHttpInfo

> ApiResponse<ValidatePhoneNumberKycAddress200Response> validatePhoneNumberKycAddress validatePhoneNumberKycAddressWithHttpInfo(validatePhoneNumberKycAddressRequest)

Pre-validate KYC address

Optional early check for the address step of a Tier 4 (end-user identity) registration: validates a postal address for deliverability BEFORE the full KYC submit, so it can be corrected before any documents are uploaded. The full submit (POST /v1/phone-numbers/kyc) re-validates the address, so this call is purely a fast feedback path and skipping it is safe. Only the postal address is sent (no documents, no gov-ID fields). A region (&#x60;administrative_area&#x60;) is required by the validator; when it is omitted the pre-check is skipped and &#x60;{ ok: true, skipped: true }&#x60; is returned (the final submit still validates). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.PhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        PhoneNumbersApi apiInstance = new PhoneNumbersApi(defaultClient);
        ValidatePhoneNumberKycAddressRequest validatePhoneNumberKycAddressRequest = new ValidatePhoneNumberKycAddressRequest(); // ValidatePhoneNumberKycAddressRequest | 
        try {
            ApiResponse<ValidatePhoneNumberKycAddress200Response> response = apiInstance.validatePhoneNumberKycAddressWithHttpInfo(validatePhoneNumberKycAddressRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling PhoneNumbersApi#validatePhoneNumberKycAddress");
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
| **validatePhoneNumberKycAddressRequest** | [**ValidatePhoneNumberKycAddressRequest**](ValidatePhoneNumberKycAddressRequest.md)|  | |

### Return type

ApiResponse<[**ValidatePhoneNumberKycAddress200Response**](ValidatePhoneNumberKycAddress200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Address is deliverable, or the pre-check was skipped (no region supplied). |  -  |
| **400** | The country isn&#39;t offered, or the address could not be verified. When the provider returned usable corrections, &#x60;details.addressSuggestions&#x60; carries them per field for a one-click \&quot;apply suggestion\&quot; card. (Flat error envelope: &#x60;error&#x60; is the human message; &#x60;code&#x60;/&#x60;param&#x60;/&#x60;details&#x60; are top-level siblings.)  |  -  |
| **401** | Unauthorized |  -  |

