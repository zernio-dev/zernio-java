# SmsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appealSmsRegistration**](SmsApi.md#appealSmsRegistration) | **POST** /v1/sms/registrations/{id}/appeal | Appeal a rejected campaign |
| [**appealSmsRegistrationWithHttpInfo**](SmsApi.md#appealSmsRegistrationWithHttpInfo) | **POST** /v1/sms/registrations/{id}/appeal | Appeal a rejected campaign |
| [**deactivateSmsRegistration**](SmsApi.md#deactivateSmsRegistration) | **DELETE** /v1/sms/registrations/{id} | Deactivate a brand/campaign registration |
| [**deactivateSmsRegistrationWithHttpInfo**](SmsApi.md#deactivateSmsRegistrationWithHttpInfo) | **DELETE** /v1/sms/registrations/{id} | Deactivate a brand/campaign registration |
| [**disableSmsOnNumber**](SmsApi.md#disableSmsOnNumber) | **DELETE** /v1/phone-numbers/{id}/sms | Disable SMS on a number |
| [**disableSmsOnNumberWithHttpInfo**](SmsApi.md#disableSmsOnNumberWithHttpInfo) | **DELETE** /v1/phone-numbers/{id}/sms | Disable SMS on a number |
| [**enableSmsOnNumber**](SmsApi.md#enableSmsOnNumber) | **POST** /v1/phone-numbers/{id}/sms | Enable SMS on a number |
| [**enableSmsOnNumberWithHttpInfo**](SmsApi.md#enableSmsOnNumberWithHttpInfo) | **POST** /v1/phone-numbers/{id}/sms | Enable SMS on a number |
| [**getSmsRegistration**](SmsApi.md#getSmsRegistration) | **GET** /v1/sms/registrations/{id} | Get a carrier registration |
| [**getSmsRegistrationWithHttpInfo**](SmsApi.md#getSmsRegistrationWithHttpInfo) | **GET** /v1/sms/registrations/{id} | Get a carrier registration |
| [**listSmsOptOuts**](SmsApi.md#listSmsOptOuts) | **GET** /v1/sms/opt-outs | List SMS opt-outs |
| [**listSmsOptOutsWithHttpInfo**](SmsApi.md#listSmsOptOutsWithHttpInfo) | **GET** /v1/sms/opt-outs | List SMS opt-outs |
| [**listSmsRegistrations**](SmsApi.md#listSmsRegistrations) | **GET** /v1/sms/registrations | List carrier registrations |
| [**listSmsRegistrationsWithHttpInfo**](SmsApi.md#listSmsRegistrationsWithHttpInfo) | **GET** /v1/sms/registrations | List carrier registrations |
| [**lookupSmsNumber**](SmsApi.md#lookupSmsNumber) | **GET** /v1/sms/lookup | Look up carrier + line type |
| [**lookupSmsNumberWithHttpInfo**](SmsApi.md#lookupSmsNumberWithHttpInfo) | **GET** /v1/sms/lookup | Look up carrier + line type |
| [**resendSmsRegistrationOtp**](SmsApi.md#resendSmsRegistrationOtp) | **POST** /v1/sms/registrations/{id}/resend-otp | Re-send the sole-prop OTP |
| [**resendSmsRegistrationOtpWithHttpInfo**](SmsApi.md#resendSmsRegistrationOtpWithHttpInfo) | **POST** /v1/sms/registrations/{id}/resend-otp | Re-send the sole-prop OTP |
| [**reuseSmsRegistrationForNumber**](SmsApi.md#reuseSmsRegistrationForNumber) | **POST** /v1/phone-numbers/{id}/sms/reuse-registration | Add number to SMS registration |
| [**reuseSmsRegistrationForNumberWithHttpInfo**](SmsApi.md#reuseSmsRegistrationForNumberWithHttpInfo) | **POST** /v1/phone-numbers/{id}/sms/reuse-registration | Add number to SMS registration |
| [**sendSms**](SmsApi.md#sendSms) | **POST** /v1/sms/messages | Send an SMS/MMS |
| [**sendSmsWithHttpInfo**](SmsApi.md#sendSmsWithHttpInfo) | **POST** /v1/sms/messages | Send an SMS/MMS |
| [**shareSmsRegistration**](SmsApi.md#shareSmsRegistration) | **POST** /v1/sms/registrations/share | Create a registration share link |
| [**shareSmsRegistrationWithHttpInfo**](SmsApi.md#shareSmsRegistrationWithHttpInfo) | **POST** /v1/sms/registrations/share | Create a registration share link |
| [**startSmsRegistration**](SmsApi.md#startSmsRegistration) | **POST** /v1/sms/registrations | Start a carrier registration |
| [**startSmsRegistrationWithHttpInfo**](SmsApi.md#startSmsRegistrationWithHttpInfo) | **POST** /v1/sms/registrations | Start a carrier registration |
| [**uploadSmsOptInProof**](SmsApi.md#uploadSmsOptInProof) | **POST** /v1/sms/registrations/{id}/opt-in-proof | Upload opt-in form proof for an appeal |
| [**uploadSmsOptInProofWithHttpInfo**](SmsApi.md#uploadSmsOptInProofWithHttpInfo) | **POST** /v1/sms/registrations/{id}/opt-in-proof | Upload opt-in form proof for an appeal |
| [**uploadSmsOptInProofFile**](SmsApi.md#uploadSmsOptInProofFile) | **POST** /v1/sms/opt-in-proof | Upload opt-in form proof |
| [**uploadSmsOptInProofFileWithHttpInfo**](SmsApi.md#uploadSmsOptInProofFileWithHttpInfo) | **POST** /v1/sms/opt-in-proof | Upload opt-in form proof |
| [**verifySmsRegistrationOtp**](SmsApi.md#verifySmsRegistrationOtp) | **POST** /v1/sms/registrations/{id}/verify-otp | Submit the sole-prop OTP |
| [**verifySmsRegistrationOtpWithHttpInfo**](SmsApi.md#verifySmsRegistrationOtpWithHttpInfo) | **POST** /v1/sms/registrations/{id}/verify-otp | Submit the sole-prop OTP |



## appealSmsRegistration

> AppealSmsRegistration200Response appealSmsRegistration(id, appealSmsRegistrationRequest)

Appeal a rejected campaign

Appeals a rejected 10DLC campaign with the carrier registry. Only a registration that reached campaign creation can be appealed; a brand-level rejection should be fixed and re-verified instead. On success the registration returns to &#x60;pending&#x60;.  Content rejections (e.g. an opt-in flow without a verifiable form link, or unrealistic samples) should be FIXED in the same call: pass the corrected &#x60;messageFlow&#x60; / &#x60;sample1&#x60; / &#x60;sample2&#x60; and the campaign is updated before the appeal is filed, so the reviewer sees the new content. The current content is on &#x60;GET /v1/sms/registrations/{id}&#x60; (&#x60;campaignContent&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        AppealSmsRegistrationRequest appealSmsRegistrationRequest = new AppealSmsRegistrationRequest(); // AppealSmsRegistrationRequest | 
        try {
            AppealSmsRegistration200Response result = apiInstance.appealSmsRegistration(id, appealSmsRegistrationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#appealSmsRegistration");
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
| **appealSmsRegistrationRequest** | [**AppealSmsRegistrationRequest**](AppealSmsRegistrationRequest.md)|  | |

### Return type

[**AppealSmsRegistration200Response**](AppealSmsRegistration200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Appeal submitted; the registration is pending again. |  -  |
| **400** | Registration has no campaign to appeal; fix the brand and re-verify instead |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |

## appealSmsRegistrationWithHttpInfo

> ApiResponse<AppealSmsRegistration200Response> appealSmsRegistration appealSmsRegistrationWithHttpInfo(id, appealSmsRegistrationRequest)

Appeal a rejected campaign

Appeals a rejected 10DLC campaign with the carrier registry. Only a registration that reached campaign creation can be appealed; a brand-level rejection should be fixed and re-verified instead. On success the registration returns to &#x60;pending&#x60;.  Content rejections (e.g. an opt-in flow without a verifiable form link, or unrealistic samples) should be FIXED in the same call: pass the corrected &#x60;messageFlow&#x60; / &#x60;sample1&#x60; / &#x60;sample2&#x60; and the campaign is updated before the appeal is filed, so the reviewer sees the new content. The current content is on &#x60;GET /v1/sms/registrations/{id}&#x60; (&#x60;campaignContent&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        AppealSmsRegistrationRequest appealSmsRegistrationRequest = new AppealSmsRegistrationRequest(); // AppealSmsRegistrationRequest | 
        try {
            ApiResponse<AppealSmsRegistration200Response> response = apiInstance.appealSmsRegistrationWithHttpInfo(id, appealSmsRegistrationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#appealSmsRegistration");
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
| **appealSmsRegistrationRequest** | [**AppealSmsRegistrationRequest**](AppealSmsRegistrationRequest.md)|  | |

### Return type

ApiResponse<[**AppealSmsRegistration200Response**](AppealSmsRegistration200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Appeal submitted; the registration is pending again. |  -  |
| **400** | Registration has no campaign to appeal; fix the brand and re-verify instead |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |


## deactivateSmsRegistration

> DeactivateSmsRegistration200Response deactivateSmsRegistration(id)

Deactivate a brand/campaign registration

Terminates the campaign with the carrier registry so the recurring monthly campaign fee stops (carriers bill the first 3 months of a campaign regardless). Numbers covered by it can no longer SEND texts — receiving is unaffected — until they&#39;re registered under a new brand. Irreversible: a deactivated campaign cannot be restored; texting again later requires a new registration (new one-time and review fees). Idempotent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            DeactivateSmsRegistration200Response result = apiInstance.deactivateSmsRegistration(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#deactivateSmsRegistration");
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

[**DeactivateSmsRegistration200Response**](DeactivateSmsRegistration200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration deactivated. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |

## deactivateSmsRegistrationWithHttpInfo

> ApiResponse<DeactivateSmsRegistration200Response> deactivateSmsRegistration deactivateSmsRegistrationWithHttpInfo(id)

Deactivate a brand/campaign registration

Terminates the campaign with the carrier registry so the recurring monthly campaign fee stops (carriers bill the first 3 months of a campaign regardless). Numbers covered by it can no longer SEND texts — receiving is unaffected — until they&#39;re registered under a new brand. Irreversible: a deactivated campaign cannot be restored; texting again later requires a new registration (new one-time and review fees). Idempotent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<DeactivateSmsRegistration200Response> response = apiInstance.deactivateSmsRegistrationWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#deactivateSmsRegistration");
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

ApiResponse<[**DeactivateSmsRegistration200Response**](DeactivateSmsRegistration200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration deactivated. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |


## disableSmsOnNumber

> DisableSmsOnNumber200Response disableSmsOnNumber(id)

Disable SMS on a number

Turns off SMS for the number (deactivates its SMS account). The carrier registration is untouched, so re-enabling later just reactivates it, with no re-registration. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            DisableSmsOnNumber200Response result = apiInstance.disableSmsOnNumber(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#disableSmsOnNumber");
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

[**DisableSmsOnNumber200Response**](DisableSmsOnNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SMS disabled. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |

## disableSmsOnNumberWithHttpInfo

> ApiResponse<DisableSmsOnNumber200Response> disableSmsOnNumber disableSmsOnNumberWithHttpInfo(id)

Disable SMS on a number

Turns off SMS for the number (deactivates its SMS account). The carrier registration is untouched, so re-enabling later just reactivates it, with no re-registration. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<DisableSmsOnNumber200Response> response = apiInstance.disableSmsOnNumberWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#disableSmsOnNumber");
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

ApiResponse<[**DisableSmsOnNumber200Response**](DisableSmsOnNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SMS disabled. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |


## enableSmsOnNumber

> EnableSmsOnNumber200Response enableSmsOnNumber(id)

Enable SMS on a number

Turns on SMS for one of your numbers. The number&#39;s real carrier capability is checked first: some number types can&#39;t do SMS at all (&#x60;smsCapable: false&#x60;), and a number still provisioning at the carrier returns &#x60;notReady: true&#x60; (try again once provisioning finishes).  US numbers additionally need a carrier registration before messages deliver; the response tells you which path applies: - &#x60;alreadyRegistered: true&#x60;: a prior registration still covers this   number; SMS was simply reactivated. - &#x60;reusable&#x60; set: you have an approved registration this number can   join in one click via   &#x60;POST /v1/phone-numbers/{id}/sms/reuse-registration&#x60;   (no new brand/campaign, no extra carrier fee). - &#x60;needsRegistration: true&#x60; and no &#x60;reusable&#x60;: start one via   &#x60;POST /v1/sms/registrations&#x60;.  Idempotent: re-running re-attempts any carrier-side setup that failed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID (from GET /v1/phone-numbers).
        try {
            EnableSmsOnNumber200Response result = apiInstance.enableSmsOnNumber(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#enableSmsOnNumber");
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
| **id** | **String**| Phone number record ID (from GET /v1/phone-numbers). | |

### Return type

[**EnableSmsOnNumber200Response**](EnableSmsOnNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result. Check &#x60;enabled&#x60;: a 200 with &#x60;enabled: false&#x60; means the number can&#39;t do SMS (&#x60;smsCapable: false&#x60;) or isn&#39;t ready yet (&#x60;notReady: true&#x60;). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so SMS can&#39;t be enabled on it. |  -  |

## enableSmsOnNumberWithHttpInfo

> ApiResponse<EnableSmsOnNumber200Response> enableSmsOnNumber enableSmsOnNumberWithHttpInfo(id)

Enable SMS on a number

Turns on SMS for one of your numbers. The number&#39;s real carrier capability is checked first: some number types can&#39;t do SMS at all (&#x60;smsCapable: false&#x60;), and a number still provisioning at the carrier returns &#x60;notReady: true&#x60; (try again once provisioning finishes).  US numbers additionally need a carrier registration before messages deliver; the response tells you which path applies: - &#x60;alreadyRegistered: true&#x60;: a prior registration still covers this   number; SMS was simply reactivated. - &#x60;reusable&#x60; set: you have an approved registration this number can   join in one click via   &#x60;POST /v1/phone-numbers/{id}/sms/reuse-registration&#x60;   (no new brand/campaign, no extra carrier fee). - &#x60;needsRegistration: true&#x60; and no &#x60;reusable&#x60;: start one via   &#x60;POST /v1/sms/registrations&#x60;.  Idempotent: re-running re-attempts any carrier-side setup that failed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | Phone number record ID (from GET /v1/phone-numbers).
        try {
            ApiResponse<EnableSmsOnNumber200Response> response = apiInstance.enableSmsOnNumberWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#enableSmsOnNumber");
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
| **id** | **String**| Phone number record ID (from GET /v1/phone-numbers). | |

### Return type

ApiResponse<[**EnableSmsOnNumber200Response**](EnableSmsOnNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result. Check &#x60;enabled&#x60;: a 200 with &#x60;enabled: false&#x60; means the number can&#39;t do SMS (&#x60;smsCapable: false&#x60;) or isn&#39;t ready yet (&#x60;notReady: true&#x60;). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |
| **422** | This number is hosted by your own carrier (brought via WhatsApp embedded signup), so SMS can&#39;t be enabled on it. |  -  |


## getSmsRegistration

> GetSmsRegistration200Response getSmsRegistration(id)

Get a carrier registration

Poll this for approval progress after starting a registration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            GetSmsRegistration200Response result = apiInstance.getSmsRegistration(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#getSmsRegistration");
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

[**GetSmsRegistration200Response**](GetSmsRegistration200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |

## getSmsRegistrationWithHttpInfo

> ApiResponse<GetSmsRegistration200Response> getSmsRegistration getSmsRegistrationWithHttpInfo(id)

Get a carrier registration

Poll this for approval progress after starting a registration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<GetSmsRegistration200Response> response = apiInstance.getSmsRegistrationWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#getSmsRegistration");
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

ApiResponse<[**GetSmsRegistration200Response**](GetSmsRegistration200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |


## listSmsOptOuts

> ListSmsOptOuts200Response listSmsOptOuts(format, limit)

List SMS opt-outs

The recipients who opted out of SMS (replied STOP) across your numbers, most recent first. Compliance surface: you must be able to see and export your opt-out list. Read-only: a recipient is re-subscribed only by replying START. Pass &#x60;format&#x3D;csv&#x60; to download a CSV instead of JSON. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String format = "json"; // String | 
        Integer limit = 500; // Integer | 
        try {
            ListSmsOptOuts200Response result = apiInstance.listSmsOptOuts(format, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#listSmsOptOuts");
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
| **format** | **String**|  | [optional] [default to json] [enum: json, csv] |
| **limit** | **Integer**|  | [optional] [default to 500] |

### Return type

[**ListSmsOptOuts200Response**](ListSmsOptOuts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Opt-out list |  -  |
| **401** | Unauthorized |  -  |

## listSmsOptOutsWithHttpInfo

> ApiResponse<ListSmsOptOuts200Response> listSmsOptOuts listSmsOptOutsWithHttpInfo(format, limit)

List SMS opt-outs

The recipients who opted out of SMS (replied STOP) across your numbers, most recent first. Compliance surface: you must be able to see and export your opt-out list. Read-only: a recipient is re-subscribed only by replying START. Pass &#x60;format&#x3D;csv&#x60; to download a CSV instead of JSON. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String format = "json"; // String | 
        Integer limit = 500; // Integer | 
        try {
            ApiResponse<ListSmsOptOuts200Response> response = apiInstance.listSmsOptOutsWithHttpInfo(format, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#listSmsOptOuts");
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
| **format** | **String**|  | [optional] [default to json] [enum: json, csv] |
| **limit** | **Integer**|  | [optional] [default to 500] |

### Return type

ApiResponse<[**ListSmsOptOuts200Response**](ListSmsOptOuts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Opt-out list |  -  |
| **401** | Unauthorized |  -  |


## listSmsRegistrations

> ListSmsRegistrations200Response listSmsRegistrations()

List carrier registrations

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        try {
            ListSmsRegistrations200Response result = apiInstance.listSmsRegistrations();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#listSmsRegistrations");
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

[**ListSmsRegistrations200Response**](ListSmsRegistrations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registrations, newest first |  -  |
| **401** | Unauthorized |  -  |

## listSmsRegistrationsWithHttpInfo

> ApiResponse<ListSmsRegistrations200Response> listSmsRegistrations listSmsRegistrationsWithHttpInfo()

List carrier registrations

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        try {
            ApiResponse<ListSmsRegistrations200Response> response = apiInstance.listSmsRegistrationsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#listSmsRegistrations");
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

ApiResponse<[**ListSmsRegistrations200Response**](ListSmsRegistrations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registrations, newest first |  -  |
| **401** | Unauthorized |  -  |


## lookupSmsNumber

> LookupSmsNumber200Response lookupSmsNumber(number)

Look up carrier + line type

Carrier name and line type (mobile / landline / voip / toll-free) for a number, plus &#x60;smsReachable&#x60; (landlines can&#39;t receive SMS). Use it to validate recipients before sending. Each lookup is billed by the carrier-data provider, so call it explicitly (e.g. pre-validating an opt-in list), not on every send. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String number = "number_example"; // String | Number to look up (E.164; formatting is normalized).
        try {
            LookupSmsNumber200Response result = apiInstance.lookupSmsNumber(number);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#lookupSmsNumber");
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
| **number** | **String**| Number to look up (E.164; formatting is normalized). | |

### Return type

[**LookupSmsNumber200Response**](LookupSmsNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lookup result. An unknown/invalid number returns lineType &#x60;unknown&#x60; with &#x60;smsReachable&#x60; false rather than an error. |  -  |
| **401** | Unauthorized |  -  |
| **502** | Lookup provider failed |  -  |

## lookupSmsNumberWithHttpInfo

> ApiResponse<LookupSmsNumber200Response> lookupSmsNumber lookupSmsNumberWithHttpInfo(number)

Look up carrier + line type

Carrier name and line type (mobile / landline / voip / toll-free) for a number, plus &#x60;smsReachable&#x60; (landlines can&#39;t receive SMS). Use it to validate recipients before sending. Each lookup is billed by the carrier-data provider, so call it explicitly (e.g. pre-validating an opt-in list), not on every send. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String number = "number_example"; // String | Number to look up (E.164; formatting is normalized).
        try {
            ApiResponse<LookupSmsNumber200Response> response = apiInstance.lookupSmsNumberWithHttpInfo(number);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#lookupSmsNumber");
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
| **number** | **String**| Number to look up (E.164; formatting is normalized). | |

### Return type

ApiResponse<[**LookupSmsNumber200Response**](LookupSmsNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lookup result. An unknown/invalid number returns lineType &#x60;unknown&#x60; with &#x60;smsReachable&#x60; false rather than an error. |  -  |
| **401** | Unauthorized |  -  |
| **502** | Lookup provider failed |  -  |


## resendSmsRegistrationOtp

> ResendSmsRegistrationOtp200Response resendSmsRegistrationOtp(id)

Re-send the sole-prop OTP

Re-sends the sole-proprietor verification PIN to the brand&#39;s mobile number — use it when the original code expired or never arrived. Only valid while the registration is pending and awaiting its OTP; rate limited to one send per minute. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ResendSmsRegistrationOtp200Response result = apiInstance.resendSmsRegistrationOtp(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#resendSmsRegistrationOtp");
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

[**ResendSmsRegistrationOtp200Response**](ResendSmsRegistrationOtp200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new code was sent |  -  |
| **400** | The registration is not awaiting a verification code |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |
| **429** | A code was just sent — wait a minute before requesting another |  -  |

## resendSmsRegistrationOtpWithHttpInfo

> ApiResponse<ResendSmsRegistrationOtp200Response> resendSmsRegistrationOtp resendSmsRegistrationOtpWithHttpInfo(id)

Re-send the sole-prop OTP

Re-sends the sole-proprietor verification PIN to the brand&#39;s mobile number — use it when the original code expired or never arrived. Only valid while the registration is pending and awaiting its OTP; rate limited to one send per minute. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<ResendSmsRegistrationOtp200Response> response = apiInstance.resendSmsRegistrationOtpWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#resendSmsRegistrationOtp");
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

ApiResponse<[**ResendSmsRegistrationOtp200Response**](ResendSmsRegistrationOtp200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new code was sent |  -  |
| **400** | The registration is not awaiting a verification code |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |
| **429** | A code was just sent — wait a minute before requesting another |  -  |


## reuseSmsRegistrationForNumber

> ReuseSmsRegistrationForNumber200Response reuseSmsRegistrationForNumber(id)

Add number to SMS registration

Attaches this number to your existing approved 10DLC campaign instead of running a fresh registration: the number inherits the campaign&#39;s approval (no new brand or campaign, no extra carrier fee). Enable SMS on the number first (&#x60;POST /v1/phone-numbers/{id}/sms&#x60;; its response tells you whether a reusable registration exists). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ReuseSmsRegistrationForNumber200Response result = apiInstance.reuseSmsRegistrationForNumber(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#reuseSmsRegistrationForNumber");
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

[**ReuseSmsRegistrationForNumber200Response**](ReuseSmsRegistrationForNumber200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number added to the existing registration. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |
| **409** | No existing SMS registration to reuse for this number |  -  |

## reuseSmsRegistrationForNumberWithHttpInfo

> ApiResponse<ReuseSmsRegistrationForNumber200Response> reuseSmsRegistrationForNumber reuseSmsRegistrationForNumberWithHttpInfo(id)

Add number to SMS registration

Attaches this number to your existing approved 10DLC campaign instead of running a fresh registration: the number inherits the campaign&#39;s approval (no new brand or campaign, no extra carrier fee). Enable SMS on the number first (&#x60;POST /v1/phone-numbers/{id}/sms&#x60;; its response tells you whether a reusable registration exists). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        try {
            ApiResponse<ReuseSmsRegistrationForNumber200Response> response = apiInstance.reuseSmsRegistrationForNumberWithHttpInfo(id);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#reuseSmsRegistrationForNumber");
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

ApiResponse<[**ReuseSmsRegistrationForNumber200Response**](ReuseSmsRegistrationForNumber200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number added to the existing registration. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |
| **409** | No existing SMS registration to reuse for this number |  -  |


## sendSms

> SendSms200Response sendSms(sendSmsRequest, idempotencyKey)

Send an SMS/MMS

Sends an SMS (or MMS when &#x60;mediaUrls&#x60; is set) from one of your SMS-enabled numbers. At least one of &#x60;text&#x60; / &#x60;mediaUrls&#x60; is required. Both numbers are normalized to E.164, so &#x60;from&#x60; matches regardless of formatting and replies thread into the same inbox conversation.  US numbers must have an approved carrier registration (&#x60;/v1/sms/registrations&#x60;) before messages deliver.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe: same key + same body replays the original response instead of sending a second message; same key + different body returns 422; a key still in flight returns 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        SendSmsRequest sendSmsRequest = new SendSmsRequest(); // SendSmsRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes send retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            SendSms200Response result = apiInstance.sendSms(sendSmsRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#sendSms");
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
| **sendSmsRequest** | [**SendSmsRequest**](SendSmsRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes send retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

[**SendSms200Response**](SendSms200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message accepted for delivery. |  -  |
| **401** | Unauthorized |  -  |
| **404** | No SMS-enabled number matches &#x60;from&#x60; |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different body |  -  |
| **502** | Carrier-side send failed |  -  |

## sendSmsWithHttpInfo

> ApiResponse<SendSms200Response> sendSms sendSmsWithHttpInfo(sendSmsRequest, idempotencyKey)

Send an SMS/MMS

Sends an SMS (or MMS when &#x60;mediaUrls&#x60; is set) from one of your SMS-enabled numbers. At least one of &#x60;text&#x60; / &#x60;mediaUrls&#x60; is required. Both numbers are normalized to E.164, so &#x60;from&#x60; matches regardless of formatting and replies thread into the same inbox conversation.  US numbers must have an approved carrier registration (&#x60;/v1/sms/registrations&#x60;) before messages deliver.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe: same key + same body replays the original response instead of sending a second message; same key + different body returns 422; a key still in flight returns 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        SendSmsRequest sendSmsRequest = new SendSmsRequest(); // SendSmsRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes send retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<SendSms200Response> response = apiInstance.sendSmsWithHttpInfo(sendSmsRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#sendSms");
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
| **sendSmsRequest** | [**SendSmsRequest**](SendSmsRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes send retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

### Return type

ApiResponse<[**SendSms200Response**](SendSms200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message accepted for delivery. |  -  |
| **401** | Unauthorized |  -  |
| **404** | No SMS-enabled number matches &#x60;from&#x60; |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different body |  -  |
| **502** | Carrier-side send failed |  -  |


## shareSmsRegistration

> ShareSmsRegistration200Response shareSmsRegistration(shareSmsRegistrationRequest)

Create a registration share link

Creates a single-use, expiring link (valid 7 days) that lets someone else (whoever has the legal business details) fill in the carrier registration form for one of your numbers, without a Zernio login. The registration is created under your account once the form is submitted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        ShareSmsRegistrationRequest shareSmsRegistrationRequest = new ShareSmsRegistrationRequest(); // ShareSmsRegistrationRequest | 
        try {
            ShareSmsRegistration200Response result = apiInstance.shareSmsRegistration(shareSmsRegistrationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#shareSmsRegistration");
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
| **shareSmsRegistrationRequest** | [**ShareSmsRegistrationRequest**](ShareSmsRegistrationRequest.md)|  | |

### Return type

[**ShareSmsRegistration200Response**](ShareSmsRegistration200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Share link created. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |

## shareSmsRegistrationWithHttpInfo

> ApiResponse<ShareSmsRegistration200Response> shareSmsRegistration shareSmsRegistrationWithHttpInfo(shareSmsRegistrationRequest)

Create a registration share link

Creates a single-use, expiring link (valid 7 days) that lets someone else (whoever has the legal business details) fill in the carrier registration form for one of your numbers, without a Zernio login. The registration is created under your account once the form is submitted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        ShareSmsRegistrationRequest shareSmsRegistrationRequest = new ShareSmsRegistrationRequest(); // ShareSmsRegistrationRequest | 
        try {
            ApiResponse<ShareSmsRegistration200Response> response = apiInstance.shareSmsRegistrationWithHttpInfo(shareSmsRegistrationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#shareSmsRegistration");
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
| **shareSmsRegistrationRequest** | [**ShareSmsRegistrationRequest**](ShareSmsRegistrationRequest.md)|  | |

### Return type

ApiResponse<[**ShareSmsRegistration200Response**](ShareSmsRegistration200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Share link created. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Number not found |  -  |


## startSmsRegistration

> StartSmsRegistration200Response startSmsRegistration(startSmsRegistrationRequest)

Start a carrier registration

Starts the US carrier registration that a number needs before SMS delivers: 10DLC (standard company or sole-proprietor) or toll-free verification. 10DLC needs &#x60;brand&#x60; + &#x60;campaign&#x60;; toll-free needs &#x60;tollFree&#x60;. Approval is asynchronous; poll &#x60;GET /v1/sms/registrations/{id}&#x60; (sole-prop registrations first need the OTP step: a code is texted to the brand&#39;s mobile number, submit it via &#x60;/verify-otp&#x60;).  Already have an approved registration? Add another number to it with &#x60;POST /v1/phone-numbers/{id}/sms/reuse-registration&#x60; instead of registering (and paying the carrier brand fee) again.  Rather have your client fill in the legal business details? Create a share link with &#x60;POST /v1/sms/registrations/share&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        StartSmsRegistrationRequest startSmsRegistrationRequest = new StartSmsRegistrationRequest(); // StartSmsRegistrationRequest | 
        try {
            StartSmsRegistration200Response result = apiInstance.startSmsRegistration(startSmsRegistrationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#startSmsRegistration");
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
| **startSmsRegistrationRequest** | [**StartSmsRegistrationRequest**](StartSmsRegistrationRequest.md)|  | |

### Return type

[**StartSmsRegistration200Response**](StartSmsRegistration200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration submitted. |  -  |
| **401** | Unauthorized |  -  |
| **422** | Carrier registry rejected a field; &#x60;param&#x60; names it when known. |  -  |

## startSmsRegistrationWithHttpInfo

> ApiResponse<StartSmsRegistration200Response> startSmsRegistration startSmsRegistrationWithHttpInfo(startSmsRegistrationRequest)

Start a carrier registration

Starts the US carrier registration that a number needs before SMS delivers: 10DLC (standard company or sole-proprietor) or toll-free verification. 10DLC needs &#x60;brand&#x60; + &#x60;campaign&#x60;; toll-free needs &#x60;tollFree&#x60;. Approval is asynchronous; poll &#x60;GET /v1/sms/registrations/{id}&#x60; (sole-prop registrations first need the OTP step: a code is texted to the brand&#39;s mobile number, submit it via &#x60;/verify-otp&#x60;).  Already have an approved registration? Add another number to it with &#x60;POST /v1/phone-numbers/{id}/sms/reuse-registration&#x60; instead of registering (and paying the carrier brand fee) again.  Rather have your client fill in the legal business details? Create a share link with &#x60;POST /v1/sms/registrations/share&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        StartSmsRegistrationRequest startSmsRegistrationRequest = new StartSmsRegistrationRequest(); // StartSmsRegistrationRequest | 
        try {
            ApiResponse<StartSmsRegistration200Response> response = apiInstance.startSmsRegistrationWithHttpInfo(startSmsRegistrationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#startSmsRegistration");
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
| **startSmsRegistrationRequest** | [**StartSmsRegistrationRequest**](StartSmsRegistrationRequest.md)|  | |

### Return type

ApiResponse<[**StartSmsRegistration200Response**](StartSmsRegistration200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration submitted. |  -  |
| **401** | Unauthorized |  -  |
| **422** | Carrier registry rejected a field; &#x60;param&#x60; names it when known. |  -  |


## uploadSmsOptInProof

> UploadSmsOptInProofFile200Response uploadSmsOptInProof(id, _file)

Upload opt-in form proof for an appeal

Hosts a screenshot (or PDF) of your SMS opt-in form and returns its public URL. Carrier reviewers reject campaigns whose consent can&#39;t be verified and ask for a \&quot;link/screenshot of the opt-in form\&quot; — the registry has no attachment field, so include the returned URL inside the &#x60;messageFlow&#x60; you submit with the appeal (&#x60;POST /v1/sms/registrations/{id}/appeal&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        File _file = new File("/path/to/file"); // File | PNG, JPG, WebP, GIF or PDF, max 4MB.
        try {
            UploadSmsOptInProofFile200Response result = apiInstance.uploadSmsOptInProof(id, _file);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#uploadSmsOptInProof");
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
| **_file** | **File**| PNG, JPG, WebP, GIF or PDF, max 4MB. | |

### Return type

[**UploadSmsOptInProofFile200Response**](UploadSmsOptInProofFile200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File hosted. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |
| **422** | Unsupported file type or file too large |  -  |

## uploadSmsOptInProofWithHttpInfo

> ApiResponse<UploadSmsOptInProofFile200Response> uploadSmsOptInProof uploadSmsOptInProofWithHttpInfo(id, _file)

Upload opt-in form proof for an appeal

Hosts a screenshot (or PDF) of your SMS opt-in form and returns its public URL. Carrier reviewers reject campaigns whose consent can&#39;t be verified and ask for a \&quot;link/screenshot of the opt-in form\&quot; — the registry has no attachment field, so include the returned URL inside the &#x60;messageFlow&#x60; you submit with the appeal (&#x60;POST /v1/sms/registrations/{id}/appeal&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        File _file = new File("/path/to/file"); // File | PNG, JPG, WebP, GIF or PDF, max 4MB.
        try {
            ApiResponse<UploadSmsOptInProofFile200Response> response = apiInstance.uploadSmsOptInProofWithHttpInfo(id, _file);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#uploadSmsOptInProof");
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
| **_file** | **File**| PNG, JPG, WebP, GIF or PDF, max 4MB. | |

### Return type

ApiResponse<[**UploadSmsOptInProofFile200Response**](UploadSmsOptInProofFile200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File hosted. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |
| **422** | Unsupported file type or file too large |  -  |


## uploadSmsOptInProofFile

> UploadSmsOptInProofFile200Response uploadSmsOptInProofFile(_file)

Upload opt-in form proof

Hosts a screenshot (or PDF) of your SMS opt-in form and returns its public URL. Include that URL in the campaign&#39;s &#x60;messageFlow&#x60; (the opt-in workflow text) — the carrier registry has no attachment field, so reviewers verify consent by opening links in that answer. Works before a registration exists (use it when registering) and for appeals. &#x60;/v1/sms/registrations/{id}/opt-in-proof&#x60; is an alias. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        File _file = new File("/path/to/file"); // File | PNG, JPG, WebP, GIF or PDF, max 4MB.
        try {
            UploadSmsOptInProofFile200Response result = apiInstance.uploadSmsOptInProofFile(_file);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#uploadSmsOptInProofFile");
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
| **_file** | **File**| PNG, JPG, WebP, GIF or PDF, max 4MB. | |

### Return type

[**UploadSmsOptInProofFile200Response**](UploadSmsOptInProofFile200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File hosted. |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unsupported file type or file too large |  -  |

## uploadSmsOptInProofFileWithHttpInfo

> ApiResponse<UploadSmsOptInProofFile200Response> uploadSmsOptInProofFile uploadSmsOptInProofFileWithHttpInfo(_file)

Upload opt-in form proof

Hosts a screenshot (or PDF) of your SMS opt-in form and returns its public URL. Include that URL in the campaign&#39;s &#x60;messageFlow&#x60; (the opt-in workflow text) — the carrier registry has no attachment field, so reviewers verify consent by opening links in that answer. Works before a registration exists (use it when registering) and for appeals. &#x60;/v1/sms/registrations/{id}/opt-in-proof&#x60; is an alias. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        File _file = new File("/path/to/file"); // File | PNG, JPG, WebP, GIF or PDF, max 4MB.
        try {
            ApiResponse<UploadSmsOptInProofFile200Response> response = apiInstance.uploadSmsOptInProofFileWithHttpInfo(_file);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#uploadSmsOptInProofFile");
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
| **_file** | **File**| PNG, JPG, WebP, GIF or PDF, max 4MB. | |

### Return type

ApiResponse<[**UploadSmsOptInProofFile200Response**](UploadSmsOptInProofFile200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File hosted. |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unsupported file type or file too large |  -  |


## verifySmsRegistrationOtp

> VerifySmsRegistrationOtp200Response verifySmsRegistrationOtp(id, verifySmsRegistrationOtpRequest)

Submit the sole-prop OTP

Completes sole-proprietor 10DLC brand verification by submitting the one-time PIN texted to the brand&#39;s mobile number. On success the registration continues to campaign creation automatically. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        VerifySmsRegistrationOtpRequest verifySmsRegistrationOtpRequest = new VerifySmsRegistrationOtpRequest(); // VerifySmsRegistrationOtpRequest | 
        try {
            VerifySmsRegistrationOtp200Response result = apiInstance.verifySmsRegistrationOtp(id, verifySmsRegistrationOtpRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#verifySmsRegistrationOtp");
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
| **verifySmsRegistrationOtpRequest** | [**VerifySmsRegistrationOtpRequest**](VerifySmsRegistrationOtpRequest.md)|  | |

### Return type

[**VerifySmsRegistrationOtp200Response**](VerifySmsRegistrationOtp200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OTP result |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |

## verifySmsRegistrationOtpWithHttpInfo

> ApiResponse<VerifySmsRegistrationOtp200Response> verifySmsRegistrationOtp verifySmsRegistrationOtpWithHttpInfo(id, verifySmsRegistrationOtpRequest)

Submit the sole-prop OTP

Completes sole-proprietor 10DLC brand verification by submitting the one-time PIN texted to the brand&#39;s mobile number. On success the registration continues to campaign creation automatically. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.SmsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        SmsApi apiInstance = new SmsApi(defaultClient);
        String id = "id_example"; // String | 
        VerifySmsRegistrationOtpRequest verifySmsRegistrationOtpRequest = new VerifySmsRegistrationOtpRequest(); // VerifySmsRegistrationOtpRequest | 
        try {
            ApiResponse<VerifySmsRegistrationOtp200Response> response = apiInstance.verifySmsRegistrationOtpWithHttpInfo(id, verifySmsRegistrationOtpRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling SmsApi#verifySmsRegistrationOtp");
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
| **verifySmsRegistrationOtpRequest** | [**VerifySmsRegistrationOtpRequest**](VerifySmsRegistrationOtpRequest.md)|  | |

### Return type

ApiResponse<[**VerifySmsRegistrationOtp200Response**](VerifySmsRegistrationOtp200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OTP result |  -  |
| **401** | Unauthorized |  -  |
| **404** | Registration not found |  -  |

