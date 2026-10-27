# FilesApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFilePickerSession**](FilesApi.md#createFilePickerSession) | **POST** /v1/files/picker-sessions | Create a hosted Google Picker session |
| [**createFilePickerSessionWithHttpInfo**](FilesApi.md#createFilePickerSessionWithHttpInfo) | **POST** /v1/files/picker-sessions | Create a hosted Google Picker session |
| [**createFolder**](FilesApi.md#createFolder) | **POST** /v1/files/folders | Create a folder |
| [**createFolderWithHttpInfo**](FilesApi.md#createFolderWithHttpInfo) | **POST** /v1/files/folders | Create a folder |
| [**downloadFile**](FilesApi.md#downloadFile) | **GET** /v1/files/{fileId}/download | Download a file |
| [**downloadFileWithHttpInfo**](FilesApi.md#downloadFileWithHttpInfo) | **GET** /v1/files/{fileId}/download | Download a file |
| [**getFile**](FilesApi.md#getFile) | **GET** /v1/files/{fileId} | Get a file or folder |
| [**getFileWithHttpInfo**](FilesApi.md#getFileWithHttpInfo) | **GET** /v1/files/{fileId} | Get a file or folder |
| [**getFileShareLink**](FilesApi.md#getFileShareLink) | **GET** /v1/files/{fileId}/share-link | Get an anyone-with-the-link share link |
| [**getFileShareLinkWithHttpInfo**](FilesApi.md#getFileShareLinkWithHttpInfo) | **GET** /v1/files/{fileId}/share-link | Get an anyone-with-the-link share link |
| [**listFiles**](FilesApi.md#listFiles) | **GET** /v1/files | List files in a folder or search the drive |
| [**listFilesWithHttpInfo**](FilesApi.md#listFilesWithHttpInfo) | **GET** /v1/files | List files in a folder or search the drive |
| [**trashFile**](FilesApi.md#trashFile) | **DELETE** /v1/files/{fileId} | Move a file to the trash |
| [**trashFileWithHttpInfo**](FilesApi.md#trashFileWithHttpInfo) | **DELETE** /v1/files/{fileId} | Move a file to the trash |
| [**updateFile**](FilesApi.md#updateFile) | **PATCH** /v1/files/{fileId} | Rename or move a file |
| [**updateFileWithHttpInfo**](FilesApi.md#updateFileWithHttpInfo) | **PATCH** /v1/files/{fileId} | Rename or move a file |
| [**uploadFile**](FilesApi.md#uploadFile) | **POST** /v1/files | Upload a file |
| [**uploadFileWithHttpInfo**](FilesApi.md#uploadFileWithHttpInfo) | **POST** /v1/files | Upload a file |



## createFilePickerSession

> CreateFilePickerSession201Response createFilePickerSession(createFilePickerSessionRequest)

Create a hosted Google Picker session

Google accounts are connected with &#x60;drive.file&#x60;, so Zernio opens only files it created or the user picked (see the Files tag). This is how your end user grants files: create a session, send the user to &#x60;url&#x60;, and they pick files in Google Picker on a Zernio-hosted page.  When they finish, the browser is sent to &#x60;redirectUrl&#x60; with these query params added (existing params are kept):    - &#x60;status&#x3D;picked&#x60;, &#x60;pickerSessionId&#x60;, &#x60;fileIds&#x60; (comma-separated Drive file ids, already checked against Drive), or   - &#x60;status&#x3D;cancelled&#x60;, &#x60;pickerSessionId&#x60; when the user pressed Cancel.  A &#x60;file.picked&#x60; webhook fires on every successful pick, so &#x60;redirectUrl&#x60; is optional for server-side integrations. Closing the picker without picking keeps the session open; the user can try again until it expires.  The URL is single-use and expires after 30 minutes; create a new session for every pick. Google accounts only: Microsoft accounts answer 400 &#x60;platform_not_supported&#x60; because OneDrive needs no picker. Picks are permanent grants: once picked, a file stays readable through the Files endpoints until the user removes Zernio from their Google account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        CreateFilePickerSessionRequest createFilePickerSessionRequest = new CreateFilePickerSessionRequest(); // CreateFilePickerSessionRequest | 
        try {
            CreateFilePickerSession201Response result = apiInstance.createFilePickerSession(createFilePickerSessionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createFilePickerSession");
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
| **createFilePickerSessionRequest** | [**CreateFilePickerSessionRequest**](CreateFilePickerSessionRequest.md)|  | |

### Return type

[**CreateFilePickerSession201Response**](CreateFilePickerSession201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The session |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## createFilePickerSessionWithHttpInfo

> ApiResponse<CreateFilePickerSession201Response> createFilePickerSession createFilePickerSessionWithHttpInfo(createFilePickerSessionRequest)

Create a hosted Google Picker session

Google accounts are connected with &#x60;drive.file&#x60;, so Zernio opens only files it created or the user picked (see the Files tag). This is how your end user grants files: create a session, send the user to &#x60;url&#x60;, and they pick files in Google Picker on a Zernio-hosted page.  When they finish, the browser is sent to &#x60;redirectUrl&#x60; with these query params added (existing params are kept):    - &#x60;status&#x3D;picked&#x60;, &#x60;pickerSessionId&#x60;, &#x60;fileIds&#x60; (comma-separated Drive file ids, already checked against Drive), or   - &#x60;status&#x3D;cancelled&#x60;, &#x60;pickerSessionId&#x60; when the user pressed Cancel.  A &#x60;file.picked&#x60; webhook fires on every successful pick, so &#x60;redirectUrl&#x60; is optional for server-side integrations. Closing the picker without picking keeps the session open; the user can try again until it expires.  The URL is single-use and expires after 30 minutes; create a new session for every pick. Google accounts only: Microsoft accounts answer 400 &#x60;platform_not_supported&#x60; because OneDrive needs no picker. Picks are permanent grants: once picked, a file stays readable through the Files endpoints until the user removes Zernio from their Google account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        CreateFilePickerSessionRequest createFilePickerSessionRequest = new CreateFilePickerSessionRequest(); // CreateFilePickerSessionRequest | 
        try {
            ApiResponse<CreateFilePickerSession201Response> response = apiInstance.createFilePickerSessionWithHttpInfo(createFilePickerSessionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createFilePickerSession");
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
| **createFilePickerSessionRequest** | [**CreateFilePickerSessionRequest**](CreateFilePickerSessionRequest.md)|  | |

### Return type

ApiResponse<[**CreateFilePickerSession201Response**](CreateFilePickerSession201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The session |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## createFolder

> UploadFile201Response createFolder(createFolderRequest)

Create a folder

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        CreateFolderRequest createFolderRequest = new CreateFolderRequest(); // CreateFolderRequest | 
        try {
            UploadFile201Response result = apiInstance.createFolder(createFolderRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createFolder");
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
| **createFolderRequest** | [**CreateFolderRequest**](CreateFolderRequest.md)|  | |

### Return type

[**UploadFile201Response**](UploadFile201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The folder |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## createFolderWithHttpInfo

> ApiResponse<UploadFile201Response> createFolder createFolderWithHttpInfo(createFolderRequest)

Create a folder

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        CreateFolderRequest createFolderRequest = new CreateFolderRequest(); // CreateFolderRequest | 
        try {
            ApiResponse<UploadFile201Response> response = apiInstance.createFolderWithHttpInfo(createFolderRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#createFolder");
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
| **createFolderRequest** | [**CreateFolderRequest**](CreateFolderRequest.md)|  | |

### Return type

ApiResponse<[**UploadFile201Response**](UploadFile201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The folder |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## downloadFile

> File downloadFile(fileId, accountId)

Download a file

Streams the bytes with &#x60;Content-Disposition: attachment&#x60;. Google Docs, Slides and Drawings arrive as PDF/PNG and Sheets as XLSX, named with the export extension. Folders answer 400.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            File result = apiInstance.downloadFile(fileId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#downloadFile");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

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
| **200** | The file bytes |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |

## downloadFileWithHttpInfo

> ApiResponse<File> downloadFile downloadFileWithHttpInfo(fileId, accountId)

Download a file

Streams the bytes with &#x60;Content-Disposition: attachment&#x60;. Google Docs, Slides and Drawings arrive as PDF/PNG and Sheets as XLSX, named with the export extension. Folders answer 400.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<File> response = apiInstance.downloadFileWithHttpInfo(fileId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#downloadFile");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

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
| **200** | The file bytes |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |


## getFile

> UploadFile201Response getFile(fileId, accountId)

Get a file or folder

On Google Drive, a file Zernio neither created nor was given through Google Picker answers 404 &#x60;resource_not_found&#x60; with &#x60;details: { fileId, reason: file_not_granted }&#x60;; send the user through &#x60;POST /v1/files/picker-sessions&#x60; (pass the id in &#x60;fileIds&#x60; to show it first). The same 404 applies to download, update, trash and share-link.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            UploadFile201Response result = apiInstance.getFile(fileId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#getFile");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**UploadFile201Response**](UploadFile201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The item |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |

## getFileWithHttpInfo

> ApiResponse<UploadFile201Response> getFile getFileWithHttpInfo(fileId, accountId)

Get a file or folder

On Google Drive, a file Zernio neither created nor was given through Google Picker answers 404 &#x60;resource_not_found&#x60; with &#x60;details: { fileId, reason: file_not_granted }&#x60;; send the user through &#x60;POST /v1/files/picker-sessions&#x60; (pass the id in &#x60;fileIds&#x60; to show it first). The same 404 applies to download, update, trash and share-link.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<UploadFile201Response> response = apiInstance.getFileWithHttpInfo(fileId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#getFile");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**UploadFile201Response**](UploadFile201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The item |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |


## getFileShareLink

> GetFileShareLink200Response getFileShareLink(fileId, accountId)

Get an anyone-with-the-link share link

Grants read access to anyone holding the link (Drive &#x60;anyone&#x60; permission, OneDrive anonymous view link) and returns it. The grant stays until it is revoked on the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            GetFileShareLink200Response result = apiInstance.getFileShareLink(fileId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#getFileShareLink");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**GetFileShareLink200Response**](GetFileShareLink200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |

## getFileShareLinkWithHttpInfo

> ApiResponse<GetFileShareLink200Response> getFileShareLink getFileShareLinkWithHttpInfo(fileId, accountId)

Get an anyone-with-the-link share link

Grants read access to anyone holding the link (Drive &#x60;anyone&#x60; permission, OneDrive anonymous view link) and returns it. The grant stays until it is revoked on the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<GetFileShareLink200Response> response = apiInstance.getFileShareLinkWithHttpInfo(fileId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#getFileShareLink");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**GetFileShareLink200Response**](GetFileShareLink200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |


## listFiles

> ListFiles200Response listFiles(accountId, folderId, q, cursor, limit)

List files in a folder or search the drive

Children of &#x60;folderId&#x60; (the root by default), folders first. With &#x60;q&#x60; and no &#x60;folderId&#x60; the whole drive is searched by name (on Google, every drive the app can see, shared drives included). The account must have been connected with &#x60;scopes&#x3D;files&#x60; (412 &#x60;account_scope_missing&#x60; otherwise). Cursors are opaque and provider-issued. Google Drive returns only files Zernio created or the user picked (see the Files tag): an unpicked folder lists empty.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String folderId = "folderId_example"; // String | Provider folder id; omit for the root.
        String q = "q_example"; // String | Name search.
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        try {
            ListFiles200Response result = apiInstance.listFiles(accountId, folderId, q, cursor, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#listFiles");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **folderId** | **String**| Provider folder id; omit for the root. | [optional] |
| **q** | **String**| Name search. | [optional] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**ListFiles200Response**](ListFiles200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Files |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## listFilesWithHttpInfo

> ApiResponse<ListFiles200Response> listFiles listFilesWithHttpInfo(accountId, folderId, q, cursor, limit)

List files in a folder or search the drive

Children of &#x60;folderId&#x60; (the root by default), folders first. With &#x60;q&#x60; and no &#x60;folderId&#x60; the whole drive is searched by name (on Google, every drive the app can see, shared drives included). The account must have been connected with &#x60;scopes&#x3D;files&#x60; (412 &#x60;account_scope_missing&#x60; otherwise). Cursors are opaque and provider-issued. Google Drive returns only files Zernio created or the user picked (see the Files tag): an unpicked folder lists empty.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        String folderId = "folderId_example"; // String | Provider folder id; omit for the root.
        String q = "q_example"; // String | Name search.
        String cursor = "cursor_example"; // String | 
        Integer limit = 50; // Integer | 
        try {
            ApiResponse<ListFiles200Response> response = apiInstance.listFilesWithHttpInfo(accountId, folderId, q, cursor, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#listFiles");
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
| **accountId** | **String**| The connected Google or Microsoft account. | |
| **folderId** | **String**| Provider folder id; omit for the root. | [optional] |
| **q** | **String**| Name search. | [optional] |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

ApiResponse<[**ListFiles200Response**](ListFiles200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Files |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |


## trashFile

> TrashFile200Response trashFile(fileId, accountId)

Move a file to the trash

Drive trash or the OneDrive recycle bin; nothing is destroyed and the user can restore it on the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            TrashFile200Response result = apiInstance.trashFile(fileId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#trashFile");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

[**TrashFile200Response**](TrashFile200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trashed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |

## trashFileWithHttpInfo

> ApiResponse<TrashFile200Response> trashFile trashFileWithHttpInfo(fileId, accountId)

Move a file to the trash

Drive trash or the OneDrive recycle bin; nothing is destroyed and the user can restore it on the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        String accountId = "accountId_example"; // String | The connected Google or Microsoft account.
        try {
            ApiResponse<TrashFile200Response> response = apiInstance.trashFileWithHttpInfo(fileId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#trashFile");
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
| **fileId** | **String**|  | |
| **accountId** | **String**| The connected Google or Microsoft account. | |

### Return type

ApiResponse<[**TrashFile200Response**](TrashFile200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Trashed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |


## updateFile

> UploadFile201Response updateFile(fileId, updateFileRequest)

Rename or move a file

&#x60;parentId&#x60; moves the item into another folder; &#x60;name&#x60; renames it. At least one is required.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        UpdateFileRequest updateFileRequest = new UpdateFileRequest(); // UpdateFileRequest | 
        try {
            UploadFile201Response result = apiInstance.updateFile(fileId, updateFileRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#updateFile");
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
| **fileId** | **String**|  | |
| **updateFileRequest** | [**UpdateFileRequest**](UpdateFileRequest.md)|  | |

### Return type

[**UploadFile201Response**](UploadFile201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated item |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |

## updateFileWithHttpInfo

> ApiResponse<UploadFile201Response> updateFile updateFileWithHttpInfo(fileId, updateFileRequest)

Rename or move a file

&#x60;parentId&#x60; moves the item into another folder; &#x60;name&#x60; renames it. At least one is required.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        String fileId = "fileId_example"; // String | 
        UpdateFileRequest updateFileRequest = new UpdateFileRequest(); // UpdateFileRequest | 
        try {
            ApiResponse<UploadFile201Response> response = apiInstance.updateFileWithHttpInfo(fileId, updateFileRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#updateFile");
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
| **fileId** | **String**|  | |
| **updateFileRequest** | [**UpdateFileRequest**](UpdateFileRequest.md)|  | |

### Return type

ApiResponse<[**UploadFile201Response**](UploadFile201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated item |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |
| **404** | Resource not found |  -  |


## uploadFile

> UploadFile201Response uploadFile(uploadFileRequest)

Upload a file

Either &#x60;multipart/form-data&#x60; with the file under &#x60;file&#x60; plus &#x60;accountId&#x60;, &#x60;name&#x60; (defaults to the file name) and &#x60;parentId&#x60;, or JSON with a public &#x60;url&#x60; the file is fetched from (100 MB cap). Large files go through the provider&#39;s resumable upload.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        UploadFileRequest uploadFileRequest = new UploadFileRequest(); // UploadFileRequest | 
        try {
            UploadFile201Response result = apiInstance.uploadFile(uploadFileRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#uploadFile");
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
| **uploadFileRequest** | [**UploadFileRequest**](UploadFileRequest.md)|  | |

### Return type

[**UploadFile201Response**](UploadFile201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The stored file |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

## uploadFileWithHttpInfo

> ApiResponse<UploadFile201Response> uploadFile uploadFileWithHttpInfo(uploadFileRequest)

Upload a file

Either &#x60;multipart/form-data&#x60; with the file under &#x60;file&#x60; plus &#x60;accountId&#x60;, &#x60;name&#x60; (defaults to the file name) and &#x60;parentId&#x60;, or JSON with a public &#x60;url&#x60; the file is fetched from (100 MB cap). Large files go through the provider&#39;s resumable upload.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.FilesApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        FilesApi apiInstance = new FilesApi(defaultClient);
        UploadFileRequest uploadFileRequest = new UploadFileRequest(); // UploadFileRequest | 
        try {
            ApiResponse<UploadFile201Response> response = apiInstance.uploadFileWithHttpInfo(uploadFileRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling FilesApi#uploadFile");
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
| **uploadFileRequest** | [**UploadFileRequest**](UploadFileRequest.md)|  | |

### Return type

ApiResponse<[**UploadFile201Response**](UploadFile201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The stored file |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **412** | The connected account cannot serve this request until something outside the request changes. Two codes:    - &#x60;account_scope_missing&#x60;: the account was connected without the area this endpoint needs (&#x60;details.grantedAreas&#x60;, &#x60;details.missingArea&#x60;), or Google reports the grant lacks a permission. Reconnect with a wider &#x60;scopes&#x3D;&#x60;.   - &#x60;admin_consent_required&#x60; (Microsoft): the tenant requires an administrator&#39;s approval; &#x60;details.adminConsentUrl&#x60; is the Microsoft Entra admin-consent link to hand to one. It opens in a browser with no API key and stays valid for one hour; &#x60;GET /v1/connect/microsoft/admin-consent&#x60; mints a fresh one.  |  -  |

