# ContactsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreateContacts**](ContactsApi.md#bulkCreateContacts) | **POST** /v1/contacts/bulk | Bulk create contacts |
| [**bulkCreateContactsWithHttpInfo**](ContactsApi.md#bulkCreateContactsWithHttpInfo) | **POST** /v1/contacts/bulk | Bulk create contacts |
| [**createContact**](ContactsApi.md#createContact) | **POST** /v1/contacts | Create contact |
| [**createContactWithHttpInfo**](ContactsApi.md#createContactWithHttpInfo) | **POST** /v1/contacts | Create contact |
| [**deleteContact**](ContactsApi.md#deleteContact) | **DELETE** /v1/contacts/{contactId} | Delete contact |
| [**deleteContactWithHttpInfo**](ContactsApi.md#deleteContactWithHttpInfo) | **DELETE** /v1/contacts/{contactId} | Delete contact |
| [**getContact**](ContactsApi.md#getContact) | **GET** /v1/contacts/{contactId} | Get contact |
| [**getContactWithHttpInfo**](ContactsApi.md#getContactWithHttpInfo) | **GET** /v1/contacts/{contactId} | Get contact |
| [**getContactChannels**](ContactsApi.md#getContactChannels) | **GET** /v1/contacts/{contactId}/channels | List channels for a contact |
| [**getContactChannelsWithHttpInfo**](ContactsApi.md#getContactChannelsWithHttpInfo) | **GET** /v1/contacts/{contactId}/channels | List channels for a contact |
| [**listContacts**](ContactsApi.md#listContacts) | **GET** /v1/contacts | List contacts |
| [**listContactsWithHttpInfo**](ContactsApi.md#listContactsWithHttpInfo) | **GET** /v1/contacts | List contacts |
| [**updateContact**](ContactsApi.md#updateContact) | **PATCH** /v1/contacts/{contactId} | Update contact |
| [**updateContactWithHttpInfo**](ContactsApi.md#updateContactWithHttpInfo) | **PATCH** /v1/contacts/{contactId} | Update contact |



## bulkCreateContacts

> BulkCreateContacts200Response bulkCreateContacts(bulkCreateContactsRequest)

Bulk create contacts

Import up to 1000 contacts at a time. Skips duplicates, merging any new tags onto the existing contact. accountId is required whenever contacts carry a platformIdentifier (or a row-level accountId); platform is always derived from the resolved account, never used to decide whether channels are created, and a mismatched platform 404s as account not found. When accountId is set, each contact must carry a platformIdentifier; a row missing it is rejected individually (reported in errors[], HTTP 200), not a 400 for the whole import. On phone platforms (whatsapp, sms) the platformIdentifier is normalized to digits and a value that is not phone-shaped is rejected per contact and reported in errors[], not imported.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        BulkCreateContactsRequest bulkCreateContactsRequest = new BulkCreateContactsRequest(); // BulkCreateContactsRequest | 
        try {
            BulkCreateContacts200Response result = apiInstance.bulkCreateContacts(bulkCreateContactsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#bulkCreateContacts");
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
| **bulkCreateContactsRequest** | [**BulkCreateContactsRequest**](BulkCreateContactsRequest.md)|  | |

### Return type

[**BulkCreateContacts200Response**](BulkCreateContacts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bulk import results |  -  |
| **400** | Contact missing required field name, or a row carries platformIdentifier/accountId with no top-level accountId to attach it to. A row missing platformIdentifier while accountId IS set is not a 400: it is reported in errors[] under a 200. An accountId on a platform with no contact channels rejects the whole import (code: platform_not_supported, details.supportedPlatforms lists the valid values). |  -  |
| **401** | Unauthorized |  -  |

## bulkCreateContactsWithHttpInfo

> ApiResponse<BulkCreateContacts200Response> bulkCreateContacts bulkCreateContactsWithHttpInfo(bulkCreateContactsRequest)

Bulk create contacts

Import up to 1000 contacts at a time. Skips duplicates, merging any new tags onto the existing contact. accountId is required whenever contacts carry a platformIdentifier (or a row-level accountId); platform is always derived from the resolved account, never used to decide whether channels are created, and a mismatched platform 404s as account not found. When accountId is set, each contact must carry a platformIdentifier; a row missing it is rejected individually (reported in errors[], HTTP 200), not a 400 for the whole import. On phone platforms (whatsapp, sms) the platformIdentifier is normalized to digits and a value that is not phone-shaped is rejected per contact and reported in errors[], not imported.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        BulkCreateContactsRequest bulkCreateContactsRequest = new BulkCreateContactsRequest(); // BulkCreateContactsRequest | 
        try {
            ApiResponse<BulkCreateContacts200Response> response = apiInstance.bulkCreateContactsWithHttpInfo(bulkCreateContactsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#bulkCreateContacts");
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
| **bulkCreateContactsRequest** | [**BulkCreateContactsRequest**](BulkCreateContactsRequest.md)|  | |

### Return type

ApiResponse<[**BulkCreateContacts200Response**](BulkCreateContacts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bulk import results |  -  |
| **400** | Contact missing required field name, or a row carries platformIdentifier/accountId with no top-level accountId to attach it to. A row missing platformIdentifier while accountId IS set is not a 400: it is reported in errors[] under a 200. An accountId on a platform with no contact channels rejects the whole import (code: platform_not_supported, details.supportedPlatforms lists the valid values). |  -  |
| **401** | Unauthorized |  -  |


## createContact

> CreateContact200Response createContact(createContactRequest)

Create contact

Create a new contact. Optionally create a platform channel in the same request by providing accountId, platform, and platformIdentifier.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        CreateContactRequest createContactRequest = new CreateContactRequest(); // CreateContactRequest | 
        try {
            CreateContact200Response result = apiInstance.createContact(createContactRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#createContact");
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
| **createContactRequest** | [**CreateContactRequest**](CreateContactRequest.md)|  | |

### Return type

[**CreateContact200Response**](CreateContact200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact created |  -  |
| **400** | Invalid request. Channel fields are all-or-nothing: accountId, platform and platformIdentifier must be sent together (code: missing_required_field). A platform outside the enum does not support contact channels (code: platform_not_supported, details.supportedPlatforms lists the valid values). |  -  |
| **401** | Unauthorized |  -  |
| **409** | Duplicate channel. The platformIdentifier is already bound to a channel on this accountId. |  -  |

## createContactWithHttpInfo

> ApiResponse<CreateContact200Response> createContact createContactWithHttpInfo(createContactRequest)

Create contact

Create a new contact. Optionally create a platform channel in the same request by providing accountId, platform, and platformIdentifier.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        CreateContactRequest createContactRequest = new CreateContactRequest(); // CreateContactRequest | 
        try {
            ApiResponse<CreateContact200Response> response = apiInstance.createContactWithHttpInfo(createContactRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#createContact");
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
| **createContactRequest** | [**CreateContactRequest**](CreateContactRequest.md)|  | |

### Return type

ApiResponse<[**CreateContact200Response**](CreateContact200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact created |  -  |
| **400** | Invalid request. Channel fields are all-or-nothing: accountId, platform and platformIdentifier must be sent together (code: missing_required_field). A platform outside the enum does not support contact channels (code: platform_not_supported, details.supportedPlatforms lists the valid values). |  -  |
| **401** | Unauthorized |  -  |
| **409** | Duplicate channel. The platformIdentifier is already bound to a channel on this accountId. |  -  |


## deleteContact

> void deleteContact(contactId)

Delete contact

Permanently deletes a contact and all associated channels.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        try {
            apiInstance.deleteContact(contactId);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#deleteContact");
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
| **contactId** | **String**|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## deleteContactWithHttpInfo

> ApiResponse<Void> deleteContact deleteContactWithHttpInfo(contactId)

Delete contact

Permanently deletes a contact and all associated channels.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.deleteContactWithHttpInfo(contactId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#deleteContact");
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
| **contactId** | **String**|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getContact

> GetContact200Response getContact(contactId)

Get contact

Returns a contact with all associated messaging channels.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        try {
            GetContact200Response result = apiInstance.getContact(contactId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#getContact");
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
| **contactId** | **String**|  | |

### Return type

[**GetContact200Response**](GetContact200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact with channels |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getContactWithHttpInfo

> ApiResponse<GetContact200Response> getContact getContactWithHttpInfo(contactId)

Get contact

Returns a contact with all associated messaging channels.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        try {
            ApiResponse<GetContact200Response> response = apiInstance.getContactWithHttpInfo(contactId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#getContact");
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
| **contactId** | **String**|  | |

### Return type

ApiResponse<[**GetContact200Response**](GetContact200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact with channels |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getContactChannels

> GetContactChannels200Response getContactChannels(contactId)

List channels for a contact

Returns all messaging channels linked to a contact (e.g. Instagram DM, Telegram, WhatsApp).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        try {
            GetContactChannels200Response result = apiInstance.getContactChannels(contactId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#getContactChannels");
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
| **contactId** | **String**|  | |

### Return type

[**GetContactChannels200Response**](GetContactChannels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of contact channels |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getContactChannelsWithHttpInfo

> ApiResponse<GetContactChannels200Response> getContactChannels getContactChannelsWithHttpInfo(contactId)

List channels for a contact

Returns all messaging channels linked to a contact (e.g. Instagram DM, Telegram, WhatsApp).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        try {
            ApiResponse<GetContactChannels200Response> response = apiInstance.getContactChannelsWithHttpInfo(contactId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#getContactChannels");
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
| **contactId** | **String**|  | |

### Return type

ApiResponse<[**GetContactChannels200Response**](GetContactChannels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of contact channels |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## listContacts

> ListContacts200Response listContacts(profileId, accountId, search, tag, tags, platform, isSubscribed, limit, skip)

List contacts

List and search contacts for a profile. Supports filtering by tags, platform, subscription status, and text search on name, email and company.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile. Omit to list across all profiles. Matches the profile recorded on the contact itself, which is set when the contact is created and is independent of the profile its account currently belongs to. Filter by accountId to list a contact through its channel instead.
        String accountId = "accountId_example"; // String | Filter by the SocialAccount that owns the contact channel. Contacts are resolved through their channels, so the profileId contact filter is not applied while accountId is set. A profileId sent alongside is still access-checked and still scopes the returned filters.tags list.
        String search = "search_example"; // String | Case-insensitive substring match on the contact name, email and company. Phone numbers and other platform identifiers are not matched: they live on the contact channel, not on the contact. To reach a contact from an inbox webhook, use the conversation.contactId it already carries.
        String tag = "tag_example"; // String | 
        String tags = "tags_example"; // String | Comma-separated tags, matches contacts carrying any of them
        String platform = "instagram"; // String | 
        String isSubscribed = "true"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListContacts200Response result = apiInstance.listContacts(profileId, accountId, search, tag, tags, platform, isSubscribed, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#listContacts");
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
| **profileId** | **String**| Filter by profile. Omit to list across all profiles. Matches the profile recorded on the contact itself, which is set when the contact is created and is independent of the profile its account currently belongs to. Filter by accountId to list a contact through its channel instead. | [optional] |
| **accountId** | **String**| Filter by the SocialAccount that owns the contact channel. Contacts are resolved through their channels, so the profileId contact filter is not applied while accountId is set. A profileId sent alongside is still access-checked and still scopes the returned filters.tags list. | [optional] |
| **search** | **String**| Case-insensitive substring match on the contact name, email and company. Phone numbers and other platform identifiers are not matched: they live on the contact channel, not on the contact. To reach a contact from an inbox webhook, use the conversation.contactId it already carries. | [optional] |
| **tag** | **String**|  | [optional] |
| **tags** | **String**| Comma-separated tags, matches contacts carrying any of them | [optional] |
| **platform** | **String**|  | [optional] [enum: instagram, facebook, telegram, twitter, bluesky, reddit, whatsapp, slack] |
| **isSubscribed** | **String**|  | [optional] [enum: true, false] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListContacts200Response**](ListContacts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contacts list with pagination and filter metadata |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |

## listContactsWithHttpInfo

> ApiResponse<ListContacts200Response> listContacts listContactsWithHttpInfo(profileId, accountId, search, tag, tags, platform, isSubscribed, limit, skip)

List contacts

List and search contacts for a profile. Supports filtering by tags, platform, subscription status, and text search on name, email and company.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile. Omit to list across all profiles. Matches the profile recorded on the contact itself, which is set when the contact is created and is independent of the profile its account currently belongs to. Filter by accountId to list a contact through its channel instead.
        String accountId = "accountId_example"; // String | Filter by the SocialAccount that owns the contact channel. Contacts are resolved through their channels, so the profileId contact filter is not applied while accountId is set. A profileId sent alongside is still access-checked and still scopes the returned filters.tags list.
        String search = "search_example"; // String | Case-insensitive substring match on the contact name, email and company. Phone numbers and other platform identifiers are not matched: they live on the contact channel, not on the contact. To reach a contact from an inbox webhook, use the conversation.contactId it already carries.
        String tag = "tag_example"; // String | 
        String tags = "tags_example"; // String | Comma-separated tags, matches contacts carrying any of them
        String platform = "instagram"; // String | 
        String isSubscribed = "true"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListContacts200Response> response = apiInstance.listContactsWithHttpInfo(profileId, accountId, search, tag, tags, platform, isSubscribed, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#listContacts");
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
| **profileId** | **String**| Filter by profile. Omit to list across all profiles. Matches the profile recorded on the contact itself, which is set when the contact is created and is independent of the profile its account currently belongs to. Filter by accountId to list a contact through its channel instead. | [optional] |
| **accountId** | **String**| Filter by the SocialAccount that owns the contact channel. Contacts are resolved through their channels, so the profileId contact filter is not applied while accountId is set. A profileId sent alongside is still access-checked and still scopes the returned filters.tags list. | [optional] |
| **search** | **String**| Case-insensitive substring match on the contact name, email and company. Phone numbers and other platform identifiers are not matched: they live on the contact channel, not on the contact. To reach a contact from an inbox webhook, use the conversation.contactId it already carries. | [optional] |
| **tag** | **String**|  | [optional] |
| **tags** | **String**| Comma-separated tags, matches contacts carrying any of them | [optional] |
| **platform** | **String**|  | [optional] [enum: instagram, facebook, telegram, twitter, bluesky, reddit, whatsapp, slack] |
| **isSubscribed** | **String**|  | [optional] [enum: true, false] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListContacts200Response**](ListContacts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contacts list with pagination and filter metadata |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |


## updateContact

> UpdateContact200Response updateContact(contactId, updateContactRequest)

Update contact

Update one or more fields on a contact. Only provided fields are changed.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        UpdateContactRequest updateContactRequest = new UpdateContactRequest(); // UpdateContactRequest | 
        try {
            UpdateContact200Response result = apiInstance.updateContact(contactId, updateContactRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#updateContact");
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
| **contactId** | **String**|  | |
| **updateContactRequest** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | [optional] |

### Return type

[**UpdateContact200Response**](UpdateContact200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## updateContactWithHttpInfo

> ApiResponse<UpdateContact200Response> updateContact updateContactWithHttpInfo(contactId, updateContactRequest)

Update contact

Update one or more fields on a contact. Only provided fields are changed.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.ContactsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        ContactsApi apiInstance = new ContactsApi(defaultClient);
        String contactId = "contactId_example"; // String | 
        UpdateContactRequest updateContactRequest = new UpdateContactRequest(); // UpdateContactRequest | 
        try {
            ApiResponse<UpdateContact200Response> response = apiInstance.updateContactWithHttpInfo(contactId, updateContactRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling ContactsApi#updateContact");
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
| **contactId** | **String**|  | |
| **updateContactRequest** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | [optional] |

### Return type

ApiResponse<[**UpdateContact200Response**](UpdateContact200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

