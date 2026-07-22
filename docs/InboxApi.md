# InboxApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWhatsAppMedia**](InboxApi.md#getWhatsAppMedia) | **GET** /v1/whatsapp/media/{mediaId} | Download WhatsApp media |
| [**getWhatsAppMediaWithHttpInfo**](InboxApi.md#getWhatsAppMediaWithHttpInfo) | **GET** /v1/whatsapp/media/{mediaId} | Download WhatsApp media |



## getWhatsAppMedia

> File getWhatsAppMedia(mediaId, accountId)

Download WhatsApp media

Streams the binary for a WhatsApp attachment. This is the endpoint the &#x60;url&#x60; on a WhatsApp &#x60;attachments[]&#x60; entry points at, in both the &#x60;message.received&#x60; webhook and the List messages response.  **This is an authenticated endpoint, not a public link.** Send &#x60;Authorization: Bearer &lt;your API key&gt;&#x60; exactly as you would for any other call. Passing the URL straight to a browser, an LLM vision API, or a no-code \&quot;download file\&quot; step without the header returns &#x60;401&#x60;. This is the most common integration mistake on this endpoint, and it differs from Instagram, Facebook and Telegram, whose &#x60;attachments[].url&#x60; is a direct CDN link that needs no header.  **Fetch on receipt, not lazily.** WhatsApp media lives in Meta&#39;s media store, not ours, and it is removed after a limited retention window (currently 7 days, and Meta has been dropping some inbound media sooner). Once Meta drops it the media is unrecoverable and this endpoint answers &#x60;400&#x60; permanently, so retrying will never succeed. Download and store the bytes when the webhook arrives. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxApi apiInstance = new InboxApi(defaultClient);
        String mediaId = "mediaId_example"; // String | The media id from `attachments[].payload.id`.
        String accountId = "accountId_example"; // String | The WhatsApp account that received the media.
        try {
            File result = apiInstance.getWhatsAppMedia(mediaId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxApi#getWhatsAppMedia");
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
| **mediaId** | **String**| The media id from &#x60;attachments[].payload.id&#x60;. | |
| **accountId** | **String**| The WhatsApp account that received the media. | |

### Return type

[**File**](File.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The media binary, streamed with its original content type. |  -  |
| **400** | Media is no longer available on WhatsApp servers (expired or deleted by Meta). Permanent, do not retry. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found, not accessible to the caller, or the media does not belong to it. |  -  |
| **502** | Meta could not be reached or returned an unexpected error. |  -  |

## getWhatsAppMediaWithHttpInfo

> ApiResponse<File> getWhatsAppMedia getWhatsAppMediaWithHttpInfo(mediaId, accountId)

Download WhatsApp media

Streams the binary for a WhatsApp attachment. This is the endpoint the &#x60;url&#x60; on a WhatsApp &#x60;attachments[]&#x60; entry points at, in both the &#x60;message.received&#x60; webhook and the List messages response.  **This is an authenticated endpoint, not a public link.** Send &#x60;Authorization: Bearer &lt;your API key&gt;&#x60; exactly as you would for any other call. Passing the URL straight to a browser, an LLM vision API, or a no-code \&quot;download file\&quot; step without the header returns &#x60;401&#x60;. This is the most common integration mistake on this endpoint, and it differs from Instagram, Facebook and Telegram, whose &#x60;attachments[].url&#x60; is a direct CDN link that needs no header.  **Fetch on receipt, not lazily.** WhatsApp media lives in Meta&#39;s media store, not ours, and it is removed after a limited retention window (currently 7 days, and Meta has been dropping some inbound media sooner). Once Meta drops it the media is unrecoverable and this endpoint answers &#x60;400&#x60; permanently, so retrying will never succeed. Download and store the bytes when the webhook arrives. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.InboxApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        InboxApi apiInstance = new InboxApi(defaultClient);
        String mediaId = "mediaId_example"; // String | The media id from `attachments[].payload.id`.
        String accountId = "accountId_example"; // String | The WhatsApp account that received the media.
        try {
            ApiResponse<File> response = apiInstance.getWhatsAppMediaWithHttpInfo(mediaId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling InboxApi#getWhatsAppMedia");
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
| **mediaId** | **String**| The media id from &#x60;attachments[].payload.id&#x60;. | |
| **accountId** | **String**| The WhatsApp account that received the media. | |

### Return type

ApiResponse<[**File**](File.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The media binary, streamed with its original content type. |  -  |
| **400** | Media is no longer available on WhatsApp servers (expired or deleted by Meta). Permanent, do not retry. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found, not accessible to the caller, or the media does not belong to it. |  -  |
| **502** | Meta could not be reached or returned an unexpected error. |  -  |

