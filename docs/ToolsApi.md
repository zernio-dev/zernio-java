# ToolsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadTikTokVideo**](ToolsApi.md#downloadTikTokVideo) | **GET** /v1/tools/tiktok/download | Download a TikTok video |
| [**downloadTikTokVideoWithHttpInfo**](ToolsApi.md#downloadTikTokVideoWithHttpInfo) | **GET** /v1/tools/tiktok/download | Download a TikTok video |



## downloadTikTokVideo

> DownloadTikTokVideo200Response downloadTikTokVideo(url, action, formatId)

Download a TikTok video

Get a download URL or list available formats for a TikTok video. Requires Tools API access and uses the Tools API rate limit. Provider gateway failures and provider-side access blocks return 503; an unavailable video returns 404.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ToolsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ToolsApi apiInstance = new ToolsApi(defaultClient);
        String url = "https://www.tiktok.com/@example/video/7412345678901234567"; // String | TikTok video URL or numeric video ID.
        String action = "download"; // String | Return a download URL or the available formats.
        String formatId = "formatId_example"; // String | Format ID from the formats response. Omit to select the first available format.
        try {
            DownloadTikTokVideo200Response result = apiInstance.downloadTikTokVideo(url, action, formatId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ToolsApi#downloadTikTokVideo");
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
| **url** | **String**| TikTok video URL or numeric video ID. | |
| **action** | **String**| Return a download URL or the available formats. | [optional] [default to download] [enum: download, formats] |
| **formatId** | **String**| Format ID from the formats response. Omit to select the first available format. | [optional] |

### Return type

[**DownloadTikTokVideo200Response**](DownloadTikTokVideo200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download URL or available formats. |  -  |
| **400** | Missing or invalid url, action, or formatId. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Tools API access is required. |  -  |
| **404** | The video or a downloadable format was not found. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | The platform returned a server error. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## downloadTikTokVideoWithHttpInfo

> ApiResponse<DownloadTikTokVideo200Response> downloadTikTokVideo downloadTikTokVideoWithHttpInfo(url, action, formatId)

Download a TikTok video

Get a download URL or list available formats for a TikTok video. Requires Tools API access and uses the Tools API rate limit. Provider gateway failures and provider-side access blocks return 503; an unavailable video returns 404.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ToolsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ToolsApi apiInstance = new ToolsApi(defaultClient);
        String url = "https://www.tiktok.com/@example/video/7412345678901234567"; // String | TikTok video URL or numeric video ID.
        String action = "download"; // String | Return a download URL or the available formats.
        String formatId = "formatId_example"; // String | Format ID from the formats response. Omit to select the first available format.
        try {
            ApiResponse<DownloadTikTokVideo200Response> response = apiInstance.downloadTikTokVideoWithHttpInfo(url, action, formatId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ToolsApi#downloadTikTokVideo");
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
| **url** | **String**| TikTok video URL or numeric video ID. | |
| **action** | **String**| Return a download URL or the available formats. | [optional] [default to download] [enum: download, formats] |
| **formatId** | **String**| Format ID from the formats response. Omit to select the first available format. | [optional] |

### Return type

ApiResponse<[**DownloadTikTokVideo200Response**](DownloadTikTokVideo200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download URL or available formats. |  -  |
| **400** | Missing or invalid url, action, or formatId. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Tools API access is required. |  -  |
| **404** | The video or a downloadable format was not found. |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted.  Reddit rate-limits per connected Reddit user (1000 requests per 10-minute window), and that budget is shared by every operation using that account. Retry after the window resets rather than retrying immediately; repeated calls while exhausted do not succeed and keep the budget spent.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **502** | The platform returned a server error. |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

