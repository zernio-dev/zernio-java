# WhatsAppPhoneNumbersApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWhatsAppNumberInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberInfo) | **GET** /v1/whatsapp/number-info | Get number status |
| [**getWhatsAppNumberInfoWithHttpInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberInfoWithHttpInfo) | **GET** /v1/whatsapp/number-info | Get number status |
| [**getWhatsAppNumberKycForm**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberKycForm) | **GET** /v1/whatsapp/phone-numbers/kyc | Get regulated-number KYC form spec |
| [**getWhatsAppNumberKycFormWithHttpInfo**](WhatsAppPhoneNumbersApi.md#getWhatsAppNumberKycFormWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/kyc | Get regulated-number KYC form spec |
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
| [**searchAvailableWhatsAppNumbers**](WhatsAppPhoneNumbersApi.md#searchAvailableWhatsAppNumbers) | **GET** /v1/whatsapp/phone-numbers/available | Search available numbers to purchase |
| [**searchAvailableWhatsAppNumbersWithHttpInfo**](WhatsAppPhoneNumbersApi.md#searchAvailableWhatsAppNumbersWithHttpInfo) | **GET** /v1/whatsapp/phone-numbers/available | Search available numbers to purchase |
| [**submitWhatsAppNumberKyc**](WhatsAppPhoneNumbersApi.md#submitWhatsAppNumberKyc) | **POST** /v1/whatsapp/phone-numbers/kyc | Submit regulated-number KYC |
| [**submitWhatsAppNumberKycWithHttpInfo**](WhatsAppPhoneNumbersApi.md#submitWhatsAppNumberKycWithHttpInfo) | **POST** /v1/whatsapp/phone-numbers/kyc | Submit regulated-number KYC |



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

Get regulated-number KYC form spec

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

Get regulated-number KYC form spec

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

List all WhatsApp phone numbers purchased by the authenticated user. By default, released numbers are excluded. 

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
        String status = "provisioning"; // String | Filter by status (by default excludes released numbers)
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
| **status** | **String**| Filter by status (by default excludes released numbers) | [optional] [enum: provisioning, pending_payment, pending_regulatory, regulatory_declined, active, suspended, releasing, released] |
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

List all WhatsApp phone numbers purchased by the authenticated user. By default, released numbers are excluded. 

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
        String status = "provisioning"; // String | Filter by status (by default excludes released numbers)
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
| **status** | **String**| Filter by status (by default excludes released numbers) | [optional] [enum: provisioning, pending_payment, pending_regulatory, regulatory_declined, active, suspended, releasing, released] |
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
| **400** | Plan limit reached |  -  |
| **401** | Unauthorized |  -  |
| **403** | A paid plan is required |  -  |
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
| **400** | Plan limit reached |  -  |
| **401** | Unauthorized |  -  |
| **403** | A paid plan is required |  -  |
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


## searchAvailableWhatsAppNumbers

> SearchAvailableWhatsAppNumbers200Response searchAvailableWhatsAppNumbers(country, type, prefix, locality, contains, limit)

Search available numbers to purchase

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

Search available numbers to purchase

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

Submit regulated-number KYC

Submit the end customer&#39;s KYC (textual values, uploaded documents, address) for a Tier 3/4 country. Documents are streamed straight to the number provider and are not stored by Zernio. Builds + submits a regulatory requirement group and claims a pending_regulatory slot; the number is ordered + activated once the provider approves (asynchronous). Idempotent per (owner, country). 

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
| **400** | Validation error (e.g. address not in-country |  -  |
| **409** | reuse requested but no prior approved verification exists for this country |  -  |
| **401** | Unauthorized |  -  |

## submitWhatsAppNumberKycWithHttpInfo

> ApiResponse<SubmitWhatsAppNumberKyc200Response> submitWhatsAppNumberKyc submitWhatsAppNumberKycWithHttpInfo(submitWhatsAppNumberKycRequest)

Submit regulated-number KYC

Submit the end customer&#39;s KYC (textual values, uploaded documents, address) for a Tier 3/4 country. Documents are streamed straight to the number provider and are not stored by Zernio. Builds + submits a regulatory requirement group and claims a pending_regulatory slot; the number is ordered + activated once the provider approves (asynchronous). Idempotent per (owner, country). 

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
| **400** | Validation error (e.g. address not in-country |  -  |
| **409** | reuse requested but no prior approved verification exists for this country |  -  |
| **401** | Unauthorized |  -  |

