# SmsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendSms**](SmsApi.md#sendSms) | **POST** /v1/sms/messages | Send an SMS or MMS |
| [**sendSmsWithHttpInfo**](SmsApi.md#sendSmsWithHttpInfo) | **POST** /v1/sms/messages | Send an SMS or MMS |



## sendSms

> SendSms200Response sendSms(sendSmsRequest)

Send an SMS or MMS

Send a text (SMS) or media (MMS) message from one of your SMS-enabled numbers.  Provide &#x60;text&#x60;, &#x60;mediaUrls&#x60;, or both. Supply an &#x60;Idempotency-Key&#x60; header to make retries safe (a repeated key replays the original result instead of sending again). US numbers must have an approved carrier registration before they can deliver. 

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
        try {
            SendSms200Response result = apiInstance.sendSms(sendSmsRequest);
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

## sendSmsWithHttpInfo

> ApiResponse<SendSms200Response> sendSms sendSmsWithHttpInfo(sendSmsRequest)

Send an SMS or MMS

Send a text (SMS) or media (MMS) message from one of your SMS-enabled numbers.  Provide &#x60;text&#x60;, &#x60;mediaUrls&#x60;, or both. Supply an &#x60;Idempotency-Key&#x60; header to make retries safe (a repeated key replays the original result instead of sending again). US numbers must have an approved carrier registration before they can deliver. 

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
        try {
            ApiResponse<SendSms200Response> response = apiInstance.sendSmsWithHttpInfo(sendSmsRequest);
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

