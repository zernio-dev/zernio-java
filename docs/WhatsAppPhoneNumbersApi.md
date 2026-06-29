# WhatsAppPhoneNumbersApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkWhatsAppNumberAvailability**](WhatsAppPhoneNumbersApi.md#checkWhatsAppNumberAvailability) | **GET** /v1/whatsapp/phone-numbers/availability | Check country availability |
| [**checkWhatsAppNumberAvailabilityWithHttpInfo**](WhatsAppPhoneNumbersApi.md#checkWhatsAppNumberAvailabilityWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/availability | Check country availability |
| [**createWhatsAppNumberKycLink**](WhatsAppPhoneNumbersApi.md#createWhatsAppNumberKycLink) | **POST** /v1/whatsapp/phone-numbers/kyc/share | Create a hosted KYC link |
| [**createWhatsAppNumberKycLinkWithHttpInfo**](WhatsAppPhoneNumbersApi.md#createWhatsAppNumberKycLinkWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/kyc/share | Create a hosted KYC link |
| [**getWhatsAppNumberInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberInfo) | **GET** /v1/whatsapp/number-info | Get number status |
| [**getWhatsAppNumberInfoWithHttpInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberInfoWithHttpInfo) | **GET** /v1/whatsapp/number-info | Get number status |
| [**getWhatsAppNumberKycForm**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberKycForm) | **GET** /v1/whatsapp/phone-numbers/kyc | Get KYC form spec |
| [**getWhatsAppNumberKycFormWithHttpInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberKycFormWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/kyc | Get KYC form spec |
| [**getWhatsAppNumberRemediation**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberRemediation) | **GET** /v1/whatsapp/phone-numbers/{id}/remediate | Get declined requirements |
| [**getWhatsAppNumberRemediationWithHttpInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberRemediationWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/{id}/remediate | Get declined requirements |
| [**getWhatsAppPhoneNumber**](WhatsAppPhoneNumbersApi.md#getWhatsAppPhoneNumber) | **GET** /v1/whatsapp/phone-numbers/{phoneNumberId} | Get phone number |
| [**getWhatsAppPhoneNumberWithHttpInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppPhoneNumberWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/{phoneNumberId} | Get phone number |
| [**getWhatsAppPhoneNumbers**](WhatsAppPhoneNumbersApi.md#getWhatsAppPhoneNumbers) | **GET** /v1/whatsapp/phone-numbers | List phone numbers |
| [**getWhatsAppPhoneNumbersWithHttpInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppPhoneNumbersWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers | List phone numbers |
| [**listWhatsAppNumberCountries**](WhatsAppPhoneNumbersApi.md#listWhatsAppNumberCountries) | **GET** /v1/whatsapp/phone-numbers/countries | List offerable number countries |
| [**listWhatsAppNumberCountriesWithHttpInfo**](WhatsAppPhoneNumbersApi.md#listWhatsAppNumberCountriesWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/countries | List offerable number countries |
| [**purchaseWhatsAppPhoneNumber**](WhatsAppPhoneNumbersApi.md#purchaseWhatsAppPhoneNumber) | **POST** /v1/whatsapp/phone-numbers/purchase | Purchase phone number |
| [**purchaseWhatsAppPhoneNumberWithHttpInfo**](WhatsAppPhoneNumbersApi.md#purchaseWhatsAppPhoneNumberWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/purchase | Purchase phone number |
| [**releaseWhatsAppPhoneNumber**](WhatsAppPhoneNumbersApi.md#releaseWhatsAppPhoneNumber) | **DELETE** /v1/whatsapp/phone-numbers/{phoneNumberId} | Release phone number |
| [**releaseWhatsAppPhoneNumberWithHttpInfo**](WhatsAppPhoneNumbersApi.md#releaseWhatsAppPhoneNumberWithHttpInfo) | **DELETE** /v1/whatsapp/phone-numbers/{phoneNumberId} | Release phone number |
| [**remediateWhatsAppNumber**](WhatsAppPhoneNumbersApi.md#remediateWhatsAppNumber) | **POST** /v1/whatsapp/phone-numbers/{id}/remediate | Resubmit a declined number |
| [**remediateWhatsAppNumberWithHttpInfo**](WhatsAppPhoneNumbersApi.md#remediateWhatsAppNumberWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/{id}/remediate | Resubmit a declined number |
| [**searchAvailableWhatsAppNumbers**](WhatsAppPhoneNumbersApi.md#searchAvailableWhatsAppNumbers) | **GET** /v1/whatsapp/phone-numbers/available | Search available numbers |
| [**searchAvailableWhatsAppNumbersWithHttpInfo**](WhatsAppPhoneNumbersApi.md#searchAvailableWhatsAppNumbersWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/available | Search available numbers |
| [**submitWhatsAppNumberKyc**](WhatsAppPhoneNumbersApi.md#submitWhatsAppNumberKyc) | **POST** /v1/whatsapp/phone-numbers/kyc | Submit KYC |
| [**submitWhatsAppNumberKycWithHttpInfo**](WhatsAppPhoneNumbersApi.md#submitWhatsAppNumberKycWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/kyc | Submit KYC |
| [**uploadWhatsAppNumberKycDocument**](WhatsAppPhoneNumbersApi.md#uploadWhatsAppNumberKycDocument) | **POST** /v1/whatsapp/phone-numbers/kyc/upload-document | Upload a KYC document |
| [**uploadWhatsAppNumberKycDocumentWithHttpInfo**](WhatsAppPhoneNumbersApi.md#uploadWhatsAppNumberKycDocumentWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/kyc/upload-document | Upload a KYC document |
| [**validateWhatsAppNumberKycAddress**](WhatsAppPhoneNumbersApi.md#validateWhatsAppNumberKycAddress) | **POST** /v1/whatsapp/phone-numbers/kyc/validate-address | Pre-validate KYC address |
| [**validateWhatsAppNumberKycAddressWithHttpInfo**](WhatsAppPhoneNumbersApi.md#validateWhatsAppNumberKycAddressWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/kyc/validate-address | Pre-validate KYC address |



## checkWhatsAppNumberAvailability

> CheckWhatsAppNumberAvailability200Response checkWhatsAppNumberAvailability(country)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | ISO-2 country code.
        try {
            CheckWhatsAppNumberAvailability200Response result = apiInstance.checkWhatsAppNumberAvailability(country);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#checkWhatsAppNumberAvailability");
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

[**CheckWhatsAppNumberAvailability200Response**](CheckWhatsAppNumberAvailability200Response.md)


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

## checkWhatsAppNumberAvailabilityWithHttpInfo

> ApiResponse<CheckWhatsAppNumberAvailability200Response> checkWhatsAppNumberAvailability checkWhatsAppNumberAvailabilityWithHttpInfo(country)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | ISO-2 country code.
        try {
            ApiResponse<CheckWhatsAppNumberAvailability200Response> response = apiInstance.checkWhatsAppNumberAvailabilityWithHttpInfo(country);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#checkWhatsAppNumberAvailability");
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

ApiResponse<[**CheckWhatsAppNumberAvailability200Response**](CheckWhatsAppNumberAvailability200Response.md)>


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


## createWhatsAppNumberKycLink

> CreateWhatsAppNumberKycLink200Response createWhatsAppNumberKycLink(createWhatsAppNumberKycLinkRequest)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        CreateWhatsAppNumberKycLinkRequest createWhatsAppNumberKycLinkRequest = new CreateWhatsAppNumberKycLinkRequest(); // CreateWhatsAppNumberKycLinkRequest | 
        try {
            CreateWhatsAppNumberKycLink200Response result = apiInstance.createWhatsAppNumberKycLink(createWhatsAppNumberKycLinkRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#createWhatsAppNumberKycLink");
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
| **createWhatsAppNumberKycLinkRequest** | [**CreateWhatsAppNumberKycLinkRequest**](CreateWhatsAppNumberKycLinkRequest.md)|  | |

### Return type

[**CreateWhatsAppNumberKycLink200Response**](CreateWhatsAppNumberKycLink200Response.md)


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

## createWhatsAppNumberKycLinkWithHttpInfo

> ApiResponse<CreateWhatsAppNumberKycLink200Response> createWhatsAppNumberKycLink createWhatsAppNumberKycLinkWithHttpInfo(createWhatsAppNumberKycLinkRequest)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        CreateWhatsAppNumberKycLinkRequest createWhatsAppNumberKycLinkRequest = new CreateWhatsAppNumberKycLinkRequest(); // CreateWhatsAppNumberKycLinkRequest | 
        try {
            ApiResponse<CreateWhatsAppNumberKycLink200Response> response = apiInstance.createWhatsAppNumberKycLinkWithHttpInfo(createWhatsAppNumberKycLinkRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#createWhatsAppNumberKycLink");
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
| **createWhatsAppNumberKycLinkRequest** | [**CreateWhatsAppNumberKycLinkRequest**](CreateWhatsAppNumberKycLinkRequest.md)|  | |

### Return type

ApiResponse<[**CreateWhatsAppNumberKycLink200Response**](CreateWhatsAppNumberKycLink200Response.md)>


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


## getWhatsAppNumberInfo

> GetWhatsAppNumberInfo200Response getWhatsAppNumberInfo(accountId)

Get number status

Live snapshot of a connected number straight from Meta: the phone-number node (display number, display name + approval, quality rating, messaging-limit tier, throughput, official-business badge, connection status, health_status) and its owning WhatsApp Business Account (name, business verification, timezone, health_status). Fetched live because Meta updates quality/tier/name/health over time; the call also refreshes the cached values shown on the connection card. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppNumberInfo200Response result = apiInstance.getWhatsAppNumberInfo(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppNumberInfo");
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

[**GetWhatsAppNumberInfo200Response**](GetWhatsAppNumberInfo200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number + WABA status |  -  |
| **400** | Phone number ID not found on account |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppNumberInfoWithHttpInfo

> ApiResponse<GetWhatsAppNumberInfo200Response> getWhatsAppNumberInfo getWhatsAppNumberInfoWithHttpInfo(accountId)

Get number status

Live snapshot of a connected number straight from Meta: the phone-number node (display number, display name + approval, quality rating, messaging-limit tier, throughput, official-business badge, connection status, health_status) and its owning WhatsApp Business Account (name, business verification, timezone, health_status). Fetched live because Meta updates quality/tier/name/health over time; the call also refreshes the cached values shown on the connection card. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppNumberInfo200Response> response = apiInstance.getWhatsAppNumberInfoWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppNumberInfo");
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

ApiResponse<[**GetWhatsAppNumberInfo200Response**](GetWhatsAppNumberInfo200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number + WABA status |  -  |
| **400** | Phone number ID not found on account |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppNumberKycForm

> GetWhatsAppNumberKycForm200Response getWhatsAppNumberKycForm(country, profileId)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | 
        String profileId = "profileId_example"; // String | 
        try {
            GetWhatsAppNumberKycForm200Response result = apiInstance.getWhatsAppNumberKycForm(country, profileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppNumberKycForm");
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
| **profileId** | **String**|  | |

### Return type

[**GetWhatsAppNumberKycForm200Response**](GetWhatsAppNumberKycForm200Response.md)


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

## getWhatsAppNumberKycFormWithHttpInfo

> ApiResponse<GetWhatsAppNumberKycForm200Response> getWhatsAppNumberKycForm getWhatsAppNumberKycFormWithHttpInfo(country, profileId)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String country = "country_example"; // String | 
        String profileId = "profileId_example"; // String | 
        try {
            ApiResponse<GetWhatsAppNumberKycForm200Response> response = apiInstance.getWhatsAppNumberKycFormWithHttpInfo(country, profileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppNumberKycForm");
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
| **profileId** | **String**|  | |

### Return type

ApiResponse<[**GetWhatsAppNumberKycForm200Response**](GetWhatsAppNumberKycForm200Response.md)>


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


## getWhatsAppNumberRemediation

> GetWhatsAppNumberRemediation200Response getWhatsAppNumberRemediation(id)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | WhatsAppPhoneNumber id.
        try {
            GetWhatsAppNumberRemediation200Response result = apiInstance.getWhatsAppNumberRemediation(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppNumberRemediation");
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
| **id** | **String**| WhatsAppPhoneNumber id. | |

### Return type

[**GetWhatsAppNumberRemediation200Response**](GetWhatsAppNumberRemediation200Response.md)


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

## getWhatsAppNumberRemediationWithHttpInfo

> ApiResponse<GetWhatsAppNumberRemediation200Response> getWhatsAppNumberRemediation getWhatsAppNumberRemediationWithHttpInfo(id)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | WhatsAppPhoneNumber id.
        try {
            ApiResponse<GetWhatsAppNumberRemediation200Response> response = apiInstance.getWhatsAppNumberRemediationWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppNumberRemediation");
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
| **id** | **String**| WhatsAppPhoneNumber id. | |

### Return type

ApiResponse<[**GetWhatsAppNumberRemediation200Response**](GetWhatsAppNumberRemediation200Response.md)>


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


## getWhatsAppPhoneNumber

> GetWhatsAppPhoneNumber200Response getWhatsAppPhoneNumber(phoneNumberId)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String phoneNumberId = "phoneNumberId_example"; // String | Phone number record ID
        try {
            GetWhatsAppPhoneNumber200Response result = apiInstance.getWhatsAppPhoneNumber(phoneNumberId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppPhoneNumber");
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
| **phoneNumberId** | **String**| Phone number record ID | |

### Return type

[**GetWhatsAppPhoneNumber200Response**](GetWhatsAppPhoneNumber200Response.md)


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

## getWhatsAppPhoneNumberWithHttpInfo

> ApiResponse<GetWhatsAppPhoneNumber200Response> getWhatsAppPhoneNumber getWhatsAppPhoneNumberWithHttpInfo(phoneNumberId)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String phoneNumberId = "phoneNumberId_example"; // String | Phone number record ID
        try {
            ApiResponse<GetWhatsAppPhoneNumber200Response> response = apiInstance.getWhatsAppPhoneNumberWithHttpInfo(phoneNumberId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppPhoneNumber");
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
| **phoneNumberId** | **String**| Phone number record ID | |

### Return type

ApiResponse<[**GetWhatsAppPhoneNumber200Response**](GetWhatsAppPhoneNumber200Response.md)>


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


## getWhatsAppPhoneNumbers

> GetWhatsAppPhoneNumbers200Response getWhatsAppPhoneNumbers(status, profileId)

List phone numbers

List all WhatsApp phone numbers purchased by the authenticated user. By default, released numbers are excluded. Connected (bring-your-own) numbers are returned in the separate &#x60;connected&#x60; array — they are not billed and have no provisioning lifecycle. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String status = "provisioning"; // String | Filter by status (by default excludes released numbers). NOTE: `status=pending_regulatory` returns the \"provisioning\" view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with `regulatoryDeclineReason`) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/whatsapp/phone-numbers/{id}/remediate. `verifying` is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches `active`. 
        String profileId = "profileId_example"; // String | Filter by profile
        try {
            GetWhatsAppPhoneNumbers200Response result = apiInstance.getWhatsAppPhoneNumbers(status, profileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppPhoneNumbers");
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
| **status** | **String**| Filter by status (by default excludes released numbers). NOTE: &#x60;status&#x3D;pending_regulatory&#x60; returns the \&quot;provisioning\&quot; view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with &#x60;regulatoryDeclineReason&#x60;) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/whatsapp/phone-numbers/{id}/remediate. &#x60;verifying&#x60; is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches &#x60;active&#x60;.  | [optional] [enum: provisioning, verifying, pending_payment, pending_regulatory, regulatory_declined, active, suspended, releasing, released] |
| **profileId** | **String**| Filter by profile | [optional] |

### Return type

[**GetWhatsAppPhoneNumbers200Response**](GetWhatsAppPhoneNumbers200Response.md)


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

## getWhatsAppPhoneNumbersWithHttpInfo

> ApiResponse<GetWhatsAppPhoneNumbers200Response> getWhatsAppPhoneNumbers getWhatsAppPhoneNumbersWithHttpInfo(status, profileId)

List phone numbers

List all WhatsApp phone numbers purchased by the authenticated user. By default, released numbers are excluded. Connected (bring-your-own) numbers are returned in the separate &#x60;connected&#x60; array — they are not billed and have no provisioning lifecycle. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String status = "provisioning"; // String | Filter by status (by default excludes released numbers). NOTE: `status=pending_regulatory` returns the \"provisioning\" view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with `regulatoryDeclineReason`) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/whatsapp/phone-numbers/{id}/remediate. `verifying` is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches `active`. 
        String profileId = "profileId_example"; // String | Filter by profile
        try {
            ApiResponse<GetWhatsAppPhoneNumbers200Response> response = apiInstance.getWhatsAppPhoneNumbersWithHttpInfo(status, profileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#getWhatsAppPhoneNumbers");
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
| **status** | **String**| Filter by status (by default excludes released numbers). NOTE: &#x60;status&#x3D;pending_regulatory&#x60; returns the \&quot;provisioning\&quot; view — numbers still in review PLUS recently-declined (last 30 days) ones, so a failed registration surfaces (with &#x60;regulatoryDeclineReason&#x60;) instead of silently disappearing. Declined numbers can be re-submitted via POST /v1/whatsapp/phone-numbers/{id}/remediate. &#x60;verifying&#x60; is the short-lived state after the number is provisioned on our side while WhatsApp confirms the activation code; the number is not billed until it reaches &#x60;active&#x60;.  | [optional] [enum: provisioning, verifying, pending_payment, pending_regulatory, regulatory_declined, active, suspended, releasing, released] |
| **profileId** | **String**| Filter by profile | [optional] |

### Return type

ApiResponse<[**GetWhatsAppPhoneNumbers200Response**](GetWhatsAppPhoneNumbers200Response.md)>


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


## listWhatsAppNumberCountries

> ListWhatsAppNumberCountries200Response listWhatsAppNumberCountries()

List offerable number countries

The WhatsApp number countries available to purchase, each with its flat monthly price (cents), regulatory tier, whether it needs end-user KYC (Tier 3/4), and whether outbound calling is available (not BIC-blocked). Drives the country picker. Tier-4 countries appear only when enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        try {
            ListWhatsAppNumberCountries200Response result = apiInstance.listWhatsAppNumberCountries();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#listWhatsAppNumberCountries");
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

[**ListWhatsAppNumberCountries200Response**](ListWhatsAppNumberCountries200Response.md)


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

## listWhatsAppNumberCountriesWithHttpInfo

> ApiResponse<ListWhatsAppNumberCountries200Response> listWhatsAppNumberCountries listWhatsAppNumberCountriesWithHttpInfo()

List offerable number countries

The WhatsApp number countries available to purchase, each with its flat monthly price (cents), regulatory tier, whether it needs end-user KYC (Tier 3/4), and whether outbound calling is available (not BIC-blocked). Drives the country picker. Tier-4 countries appear only when enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        try {
            ApiResponse<ListWhatsAppNumberCountries200Response> response = apiInstance.listWhatsAppNumberCountriesWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#listWhatsAppNumberCountries");
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

ApiResponse<[**ListWhatsAppNumberCountries200Response**](ListWhatsAppNumberCountries200Response.md)>


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


## purchaseWhatsAppPhoneNumber

> PurchaseWhatsAppPhoneNumber200Response purchaseWhatsAppPhoneNumber(purchaseWhatsAppPhoneNumberRequest)

Purchase phone number

Initiate purchasing a WhatsApp phone number. Payment-first flow: the user does not pick a specific number. The system either creates a Stripe Checkout Session (first number) or increments the existing subscription quantity and provisions inline (subsequent numbers).  Requires a paid plan. The maximum number of phone numbers is determined by the user&#39;s plan. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        PurchaseWhatsAppPhoneNumberRequest purchaseWhatsAppPhoneNumberRequest = new PurchaseWhatsAppPhoneNumberRequest(); // PurchaseWhatsAppPhoneNumberRequest | 
        try {
            PurchaseWhatsAppPhoneNumber200Response result = apiInstance.purchaseWhatsAppPhoneNumber(purchaseWhatsAppPhoneNumberRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#purchaseWhatsAppPhoneNumber");
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
| **purchaseWhatsAppPhoneNumberRequest** | [**PurchaseWhatsAppPhoneNumberRequest**](PurchaseWhatsAppPhoneNumberRequest.md)|  | |

### Return type

[**PurchaseWhatsAppPhoneNumber200Response**](PurchaseWhatsAppPhoneNumber200Response.md)


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

## purchaseWhatsAppPhoneNumberWithHttpInfo

> ApiResponse<PurchaseWhatsAppPhoneNumber200Response> purchaseWhatsAppPhoneNumber purchaseWhatsAppPhoneNumberWithHttpInfo(purchaseWhatsAppPhoneNumberRequest)

Purchase phone number

Initiate purchasing a WhatsApp phone number. Payment-first flow: the user does not pick a specific number. The system either creates a Stripe Checkout Session (first number) or increments the existing subscription quantity and provisions inline (subsequent numbers).  Requires a paid plan. The maximum number of phone numbers is determined by the user&#39;s plan. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        PurchaseWhatsAppPhoneNumberRequest purchaseWhatsAppPhoneNumberRequest = new PurchaseWhatsAppPhoneNumberRequest(); // PurchaseWhatsAppPhoneNumberRequest | 
        try {
            ApiResponse<PurchaseWhatsAppPhoneNumber200Response> response = apiInstance.purchaseWhatsAppPhoneNumberWithHttpInfo(purchaseWhatsAppPhoneNumberRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#purchaseWhatsAppPhoneNumber");
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
| **purchaseWhatsAppPhoneNumberRequest** | [**PurchaseWhatsAppPhoneNumberRequest**](PurchaseWhatsAppPhoneNumberRequest.md)|  | |

### Return type

ApiResponse<[**PurchaseWhatsAppPhoneNumber200Response**](PurchaseWhatsAppPhoneNumber200Response.md)>


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


## releaseWhatsAppPhoneNumber

> ReleaseWhatsAppPhoneNumber200Response releaseWhatsAppPhoneNumber(phoneNumberId)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String phoneNumberId = "phoneNumberId_example"; // String | Phone number record ID
        try {
            ReleaseWhatsAppPhoneNumber200Response result = apiInstance.releaseWhatsAppPhoneNumber(phoneNumberId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#releaseWhatsAppPhoneNumber");
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
| **phoneNumberId** | **String**| Phone number record ID | |

### Return type

[**ReleaseWhatsAppPhoneNumber200Response**](ReleaseWhatsAppPhoneNumber200Response.md)


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

## releaseWhatsAppPhoneNumberWithHttpInfo

> ApiResponse<ReleaseWhatsAppPhoneNumber200Response> releaseWhatsAppPhoneNumber releaseWhatsAppPhoneNumberWithHttpInfo(phoneNumberId)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String phoneNumberId = "phoneNumberId_example"; // String | Phone number record ID
        try {
            ApiResponse<ReleaseWhatsAppPhoneNumber200Response> response = apiInstance.releaseWhatsAppPhoneNumberWithHttpInfo(phoneNumberId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#releaseWhatsAppPhoneNumber");
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
| **phoneNumberId** | **String**| Phone number record ID | |

### Return type

ApiResponse<[**ReleaseWhatsAppPhoneNumber200Response**](ReleaseWhatsAppPhoneNumber200Response.md)>


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


## remediateWhatsAppNumber

> RemediateWhatsAppNumber200Response remediateWhatsAppNumber(id, remediateWhatsAppNumberRequest)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | 
        RemediateWhatsAppNumberRequest remediateWhatsAppNumberRequest = new RemediateWhatsAppNumberRequest(); // RemediateWhatsAppNumberRequest | 
        try {
            RemediateWhatsAppNumber200Response result = apiInstance.remediateWhatsAppNumber(id, remediateWhatsAppNumberRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#remediateWhatsAppNumber");
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
| **remediateWhatsAppNumberRequest** | [**RemediateWhatsAppNumberRequest**](RemediateWhatsAppNumberRequest.md)|  | |

### Return type

[**RemediateWhatsAppNumber200Response**](RemediateWhatsAppNumber200Response.md)


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

## remediateWhatsAppNumberWithHttpInfo

> ApiResponse<RemediateWhatsAppNumber200Response> remediateWhatsAppNumber remediateWhatsAppNumberWithHttpInfo(id, remediateWhatsAppNumberRequest)

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
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String id = "id_example"; // String | 
        RemediateWhatsAppNumberRequest remediateWhatsAppNumberRequest = new RemediateWhatsAppNumberRequest(); // RemediateWhatsAppNumberRequest | 
        try {
            ApiResponse<RemediateWhatsAppNumber200Response> response = apiInstance.remediateWhatsAppNumberWithHttpInfo(id, remediateWhatsAppNumberRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#remediateWhatsAppNumber");
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
| **remediateWhatsAppNumberRequest** | [**RemediateWhatsAppNumberRequest**](RemediateWhatsAppNumberRequest.md)|  | |

### Return type

ApiResponse<[**RemediateWhatsAppNumber200Response**](RemediateWhatsAppNumber200Response.md)>


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


## searchAvailableWhatsAppNumbers

> SearchAvailableWhatsAppNumbers200Response searchAvailableWhatsAppNumbers(country, type, prefix, locality, contains, limit)

Search available numbers

Search the provider&#39;s inventory for numbers available to purchase in a country (default US). Optional filters narrow the results. The country must be offerable (see GET /v1/whatsapp/phone-numbers/countries). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String country = "US"; // String | 
        String type = "type_example"; // String | Number type; defaults to the country's WhatsApp-safe type
        String prefix = "prefix_example"; // String | Area code
        String locality = "locality_example"; // String | City
        String contains = "contains_example"; // String | Pattern to match within the number
        Integer limit = 20; // Integer | 
        try {
            SearchAvailableWhatsAppNumbers200Response result = apiInstance.searchAvailableWhatsAppNumbers(country, type, prefix, locality, contains, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#searchAvailableWhatsAppNumbers");
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
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**SearchAvailableWhatsAppNumbers200Response**](SearchAvailableWhatsAppNumbers200Response.md)


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

## searchAvailableWhatsAppNumbersWithHttpInfo

> ApiResponse<SearchAvailableWhatsAppNumbers200Response> searchAvailableWhatsAppNumbers searchAvailableWhatsAppNumbersWithHttpInfo(country, type, prefix, locality, contains, limit)

Search available numbers

Search the provider&#39;s inventory for numbers available to purchase in a country (default US). Optional filters narrow the results. The country must be offerable (see GET /v1/whatsapp/phone-numbers/countries). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String country = "US"; // String | 
        String type = "type_example"; // String | Number type; defaults to the country's WhatsApp-safe type
        String prefix = "prefix_example"; // String | Area code
        String locality = "locality_example"; // String | City
        String contains = "contains_example"; // String | Pattern to match within the number
        Integer limit = 20; // Integer | 
        try {
            ApiResponse<SearchAvailableWhatsAppNumbers200Response> response = apiInstance.searchAvailableWhatsAppNumbersWithHttpInfo(country, type, prefix, locality, contains, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#searchAvailableWhatsAppNumbers");
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
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

ApiResponse<[**SearchAvailableWhatsAppNumbers200Response**](SearchAvailableWhatsAppNumbers200Response.md)>


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


## submitWhatsAppNumberKyc

> SubmitWhatsAppNumberKyc200Response submitWhatsAppNumberKyc(submitWhatsAppNumberKycRequest)

Submit KYC

Submit the end customer&#39;s KYC (textual values, uploaded documents, address) for a Tier 3/4 country. Documents are streamed straight to the number provider and are not stored by Zernio. Builds + submits a regulatory requirement group and claims a pending_regulatory slot; the number is ordered + activated once the provider approves (asynchronous). A customer may hold several same-country numbers in review at once; a double-submit of the SAME attempt is deduped via &#x60;submissionId&#x60;.  For an ID-card document requirement, carriers commonly require BOTH sides: combine the front and back into a single file before uploading (the dashboard does this automatically). A one-sided ID is a common decline reason; fix it via POST /v1/whatsapp/phone-numbers/{id}/remediate.  Before submitting, call GET /v1/whatsapp/phone-numbers/availability to check the country has deliverable inventory and, for geographic-match countries, which area the address must be in — otherwise the submission can pass review yet never be assignable a number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        SubmitWhatsAppNumberKycRequest submitWhatsAppNumberKycRequest = new SubmitWhatsAppNumberKycRequest(); // SubmitWhatsAppNumberKycRequest | 
        try {
            SubmitWhatsAppNumberKyc200Response result = apiInstance.submitWhatsAppNumberKyc(submitWhatsAppNumberKycRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#submitWhatsAppNumberKyc");
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
| **submitWhatsAppNumberKycRequest** | [**SubmitWhatsAppNumberKycRequest**](SubmitWhatsAppNumberKycRequest.md)|  | |

### Return type

[**SubmitWhatsAppNumberKyc200Response**](SubmitWhatsAppNumberKyc200Response.md)


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

## submitWhatsAppNumberKycWithHttpInfo

> ApiResponse<SubmitWhatsAppNumberKyc200Response> submitWhatsAppNumberKyc submitWhatsAppNumberKycWithHttpInfo(submitWhatsAppNumberKycRequest)

Submit KYC

Submit the end customer&#39;s KYC (textual values, uploaded documents, address) for a Tier 3/4 country. Documents are streamed straight to the number provider and are not stored by Zernio. Builds + submits a regulatory requirement group and claims a pending_regulatory slot; the number is ordered + activated once the provider approves (asynchronous). A customer may hold several same-country numbers in review at once; a double-submit of the SAME attempt is deduped via &#x60;submissionId&#x60;.  For an ID-card document requirement, carriers commonly require BOTH sides: combine the front and back into a single file before uploading (the dashboard does this automatically). A one-sided ID is a common decline reason; fix it via POST /v1/whatsapp/phone-numbers/{id}/remediate.  Before submitting, call GET /v1/whatsapp/phone-numbers/availability to check the country has deliverable inventory and, for geographic-match countries, which area the address must be in — otherwise the submission can pass review yet never be assignable a number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        SubmitWhatsAppNumberKycRequest submitWhatsAppNumberKycRequest = new SubmitWhatsAppNumberKycRequest(); // SubmitWhatsAppNumberKycRequest | 
        try {
            ApiResponse<SubmitWhatsAppNumberKyc200Response> response = apiInstance.submitWhatsAppNumberKycWithHttpInfo(submitWhatsAppNumberKycRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#submitWhatsAppNumberKyc");
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
| **submitWhatsAppNumberKycRequest** | [**SubmitWhatsAppNumberKycRequest**](SubmitWhatsAppNumberKycRequest.md)|  | |

### Return type

ApiResponse<[**SubmitWhatsAppNumberKyc200Response**](SubmitWhatsAppNumberKyc200Response.md)>


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


## uploadWhatsAppNumberKycDocument

> UploadWhatsAppNumberKycDocument200Response uploadWhatsAppNumberKycDocument(xFilename, body)

Upload a KYC document

Upload ONE document and get back its provider document id, to reference from POST /v1/whatsapp/phone-numbers/kyc via &#x60;documents[].documentId&#x60;. Send the RAW file bytes as the request body (not base64); put the filename in the &#x60;X-Filename&#x60; header. Uploading documents one-per-request keeps each request under the ~4.5MB body limit. The document streams straight to the number provider and is not stored by Zernio. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String xFilename = "xFilename_example"; // String | URL-encoded original filename.
        File body = new File("/path/to/file"); // File | 
        try {
            UploadWhatsAppNumberKycDocument200Response result = apiInstance.uploadWhatsAppNumberKycDocument(xFilename, body);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#uploadWhatsAppNumberKycDocument");
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

[**UploadWhatsAppNumberKycDocument200Response**](UploadWhatsAppNumberKycDocument200Response.md)


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

## uploadWhatsAppNumberKycDocumentWithHttpInfo

> ApiResponse<UploadWhatsAppNumberKycDocument200Response> uploadWhatsAppNumberKycDocument uploadWhatsAppNumberKycDocumentWithHttpInfo(xFilename, body)

Upload a KYC document

Upload ONE document and get back its provider document id, to reference from POST /v1/whatsapp/phone-numbers/kyc via &#x60;documents[].documentId&#x60;. Send the RAW file bytes as the request body (not base64); put the filename in the &#x60;X-Filename&#x60; header. Uploading documents one-per-request keeps each request under the ~4.5MB body limit. The document streams straight to the number provider and is not stored by Zernio. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        String xFilename = "xFilename_example"; // String | URL-encoded original filename.
        File body = new File("/path/to/file"); // File | 
        try {
            ApiResponse<UploadWhatsAppNumberKycDocument200Response> response = apiInstance.uploadWhatsAppNumberKycDocumentWithHttpInfo(xFilename, body);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#uploadWhatsAppNumberKycDocument");
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

ApiResponse<[**UploadWhatsAppNumberKycDocument200Response**](UploadWhatsAppNumberKycDocument200Response.md)>


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


## validateWhatsAppNumberKycAddress

> ValidateWhatsAppNumberKycAddress200Response validateWhatsAppNumberKycAddress(validateWhatsAppNumberKycAddressRequest)

Pre-validate KYC address

Optional early check for the address step of a Tier 4 (end-user identity) registration: validates a postal address for deliverability BEFORE the full KYC submit, so it can be corrected before any documents are uploaded. The full submit (POST /v1/whatsapp/phone-numbers/kyc) re-validates the address, so this call is purely a fast feedback path and skipping it is safe. Only the postal address is sent (no documents, no gov-ID fields). A region (&#x60;administrative_area&#x60;) is required by the validator; when it is omitted the pre-check is skipped and &#x60;{ ok: true, skipped: true }&#x60; is returned (the final submit still validates). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        ValidateWhatsAppNumberKycAddressRequest validateWhatsAppNumberKycAddressRequest = new ValidateWhatsAppNumberKycAddressRequest(); // ValidateWhatsAppNumberKycAddressRequest | 
        try {
            ValidateWhatsAppNumberKycAddress200Response result = apiInstance.validateWhatsAppNumberKycAddress(validateWhatsAppNumberKycAddressRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#validateWhatsAppNumberKycAddress");
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
| **validateWhatsAppNumberKycAddressRequest** | [**ValidateWhatsAppNumberKycAddressRequest**](ValidateWhatsAppNumberKycAddressRequest.md)|  | |

### Return type

[**ValidateWhatsAppNumberKycAddress200Response**](ValidateWhatsAppNumberKycAddress200Response.md)


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

## validateWhatsAppNumberKycAddressWithHttpInfo

> ApiResponse<ValidateWhatsAppNumberKycAddress200Response> validateWhatsAppNumberKycAddress validateWhatsAppNumberKycAddressWithHttpInfo(validateWhatsAppNumberKycAddressRequest)

Pre-validate KYC address

Optional early check for the address step of a Tier 4 (end-user identity) registration: validates a postal address for deliverability BEFORE the full KYC submit, so it can be corrected before any documents are uploaded. The full submit (POST /v1/whatsapp/phone-numbers/kyc) re-validates the address, so this call is purely a fast feedback path and skipping it is safe. Only the postal address is sent (no documents, no gov-ID fields). A region (&#x60;administrative_area&#x60;) is required by the validator; when it is omitted the pre-check is skipped and &#x60;{ ok: true, skipped: true }&#x60; is returned (the final submit still validates). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppPhoneNumbersApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppPhoneNumbersApi apiInstance = new WhatsAppPhoneNumbersApi(defaultClient);
        ValidateWhatsAppNumberKycAddressRequest validateWhatsAppNumberKycAddressRequest = new ValidateWhatsAppNumberKycAddressRequest(); // ValidateWhatsAppNumberKycAddressRequest | 
        try {
            ApiResponse<ValidateWhatsAppNumberKycAddress200Response> response = apiInstance.validateWhatsAppNumberKycAddressWithHttpInfo(validateWhatsAppNumberKycAddressRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppPhoneNumbersApi#validateWhatsAppNumberKycAddress");
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
| **validateWhatsAppNumberKycAddressRequest** | [**ValidateWhatsAppNumberKycAddressRequest**](ValidateWhatsAppNumberKycAddressRequest.md)|  | |

### Return type

ApiResponse<[**ValidateWhatsAppNumberKycAddress200Response**](ValidateWhatsAppNumberKycAddress200Response.md)>


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

